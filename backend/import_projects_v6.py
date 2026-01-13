
import pandas as pd
import sqlite3
import os
import sys
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError

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
    try:
        val = str(val).replace(',', '').replace('₹', '').strip()
        return float(val)
    except:
        return 0.0

def import_project_list(excel_path, db_path):
    print(f"Reading {excel_path}...")
    xl = pd.ExcelFile(excel_path)
    target_sheet = next((s for s in xl.sheet_names if "Active" in s), xl.sheet_names[0])
    
    print(f"Importing from: {target_sheet}")
    df = pd.read_excel(excel_path, sheet_name=target_sheet)
    df.columns = [str(c).lower().strip().replace(' ', '_').replace('.', '') for c in df.columns]
    
    # Drop and Create
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    
    projects_added = 0
    seen_codes = set()
    
    for idx, row in df.iterrows():
        try:
            p_user_code = str(row.get('user_project_code')).strip()
            # If user_project_code is missing or "nan", generate one
            if not p_user_code or p_user_code.lower() == 'nan':
                 p_user_code = f"GEN-{idx}"

            if p_user_code in seen_codes:
                # print(f"Skipping duplicate code: {p_user_code}")
                continue 
            
            seen_codes.add(p_user_code)

            p_title = str(row.get('title') or "Untitled")
            p_dept = str(row.get('project_deptname') or "Unspecified")
            p_pi = str(row.get('pi') or "Unknown PI")
            p_type = str(row.get('ptype') or "Sponsored")
            p_val = clean_money(row.get('project_value'))
            
            d_start = row.get('date_of_commencement') 
            if not isinstance(d_start, (datetime, pd.Timestamp)): d_start = None
            else: d_start = d_start.date()

            d_close = row.get('closing_date')
            if not isinstance(d_close, (datetime, pd.Timestamp)): d_close = None
            else: d_close = d_close.date()
            
            internal_id = projects_added + 1
            
            proj = SricProjectMaster(
                project_code=internal_id, 
                user_project_code=p_user_code,
                title=p_title[:500],
                project_type=p_type,
                total_sanctioned_grant=p_val,
                date_of_commencement=d_start,
                closing_date=d_close,
                sric_cl_flg='N', 
                delete_flag='N'
            )
            session.add(proj)
            
            pi_record = SricProjectInchargeDetails(
                user_project_code=p_user_code,
                stakeholder_name=p_pi[:100],
                stakeholder_dept=p_dept[:100],
                stakeholder_type='PI',
                type='Internal'
            )
            session.add(pi_record)
            
            bal_record = AccProjectBalance(
                project_code=internal_id,
                balance_date=datetime.now().date(),
                op_balance=0.0,
                receipt_amount=p_val, 
                payment_amount=0.0,
                cl_balance=p_val, 
                deleted_flag='N',
                created_by='ImportScript',
                creation_date=datetime.now()
            )
            session.add(bal_record)
            
            # Flush periodically or on every row to catch error immediately
            session.flush() 
            projects_added += 1
            
        except Exception as row_e:
            print(f"Error processing row {idx}: {row_e}")
            continue

    try:
        session.commit()
        print(f"Success! Imported {projects_added} distinct projects.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"DB Error at commit: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    import_project_list("SRIC project list.xlsx", "sric_db.sqlite")
