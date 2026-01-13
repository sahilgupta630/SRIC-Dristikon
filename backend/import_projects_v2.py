
import pandas as pd
import sqlite3
import os
import sys
from datetime import datetime

sys.path.append(os.getcwd())
try:
    from app.core.database import SessionLocal, engine, Base
    from app.models.generated_models import (
        SricProjectMaster, 
        SricProjectInchargeDetails, 
        AccProjectBalance
    )
except ImportError:
    print("Could not import app models.")
    sys.exit(1)

def clean_money(val):
    if pd.isna(val): return 0.0
    if isinstance(val, (int, float)): return float(val)
    val = str(val).replace(',', '').replace('₹', '').strip()
    try:
        return float(val)
    except:
        return 0.0

def import_project_list(excel_path, db_path):
    print(f"Reading {excel_path}...")
    xl = pd.ExcelFile(excel_path)
    # Find active projects sheet
    target_sheet = next((s for s in xl.sheet_names if "Active" in s), None)
    if not target_sheet:
        target_sheet = xl.sheet_names[0]
    
    print(f"Importing from: {target_sheet}")
    df = pd.read_excel(excel_path, sheet_name=target_sheet)
    
    # Normalize headers
    df.columns = [str(c).lower().strip().replace(' ', '_').replace('.', '') for c in df.columns]
    
    # Reset DB
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    
    projects_added = 0
    
    for idx, row in df.iterrows():
        # fields
        p_code = str(row.get('user_proj_code') or row.get('project_no') or f"PROJ-{idx}")
        p_title = str(row.get('project_title') or row.get('title') or "Untitled")
        pi_name = str(row.get('pi_name') or row.get('pi') or row.get('coordinator') or "Unknown")
        dept = str(row.get('department') or row.get('dept') or "Unspecified")
        p_type = str(row.get('ptype') or "Sponsored")
        
        sanctioned = clean_money(row.get('sanctioned_amount') or row.get('amount'))
        
        start_dt = row.get('start_date') or row.get('date_of_start')
        close_dt = row.get('close_date') or row.get('date_of_completion')
        
        def parse_date(d):
            if pd.isna(d): return None
            if isinstance(d, datetime): return d.date()
            return None

        # 1. Project Master
        # project_code is Integer PK. user_project_code is String.
        # title, total_sanctioned_grant, date_of_commencement, closing_date
        proj = SricProjectMaster(
            project_code=idx+1, # Explicit ID
            user_project_code=p_code,
            title=p_title[:200],
            project_type=p_type,
            total_sanctioned_grant=sanctioned,
            date_of_commencement=parse_date(start_dt),
            closing_date=parse_date(close_dt),
            sric_cl_flg='N', # Open
            delete_flag='N'
        )
        session.add(proj)
        
        # 2. Incharge Details (PI)
        # user_project_code, stakeholder_name, stakeholder_dept
        pi_record = SricProjectInchargeDetails(
            user_project_code=p_code,
            stakeholder_name=pi_name,
            stakeholder_dept=dept,
            stakeholder_type='PI',
            type='Internal'
        )
        session.add(pi_record)
        
        # 3. Balance (Optional, if table exists and matches)
        # AccProjectBalance might require project_code (Integer FK)
        bal_record = AccProjectBalance(
            project_code=idx+1,
            sanctioned_grant=sanctioned,
            dict_available_balance=sanctioned,  # Assume full balance for now
            total_expenditure=0,
            receipt_amount=sanctioned
        )
        session.add(bal_record)
        
        projects_added += 1

    try:
        session.commit()
        print(f"Success! Imported {projects_added} projects.")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    import_project_list("SRIC project list.xlsx", "sric_db.sqlite")
