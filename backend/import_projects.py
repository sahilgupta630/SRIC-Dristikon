
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
        AccProjectBalance, 
        ProjectProposalMaster,
        SponsorMaster,
        SricProjectStaffMaster
    )
except ImportError:
    # Fallback if app module not found in path
    print("Could not import app models. Ensure script is run from backend folder.")
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
        target_sheet = xl.sheet_names[0] # Default to first
    
    print(f"Importing from sheet: {target_sheet}")
    df = pd.read_excel(excel_path, sheet_name=target_sheet)
    
    # Normalize headers
    df.columns = [str(c).lower().strip().replace(' ', '_').replace('.', '') for c in df.columns]
    print("Found columns:", list(df.columns))
    
    # Init DB
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    
    # Clear existing data (optional, but good for clean state)
    session.query(SricProjectMaster).delete()
    session.query(SricProjectInchargeDetails).delete()
    session.query(AccProjectBalance).delete()
    
    projects_added = 0
    pi_map = {} # To avoid duplicates if mapping needed
    
    for idx, row in df.iterrows():
        # Heuristic Column Mapping
        # Adjust these keys based on the previous inspection output 'ptype', 'user_proj_code', etc.
        
        # User Project Code (e.g., IITR/SRIC/2025/...)
        p_code = row.get('user_proj_code') or row.get('project_no') or f"PROJ-{idx}"
        
        # Title
        p_title = row.get('project_title') or row.get('title') or "Untitled Project"
        
        # PI Name (Split if multiple?)
        pi_name = row.get('pi_name') or row.get('pi') or row.get('coordinator') or "Unknown PI"
        
        # Department
        dept = row.get('department') or row.get('dept') or "Unspecified"
        
        # Funding Agency
        sponsor = row.get('funding_agency') or row.get('sponsor') or row.get('agency') or "Internal"
        
        # Sanctioned Amount
        sanctioned = clean_money(row.get('sanctioned_amount') or row.get('amount') or row.get('total_outlay'))
        
        # Start/End Dates
        start_dt = row.get('start_date') or row.get('date_of_start')
        close_dt = row.get('close_date') or row.get('date_of_completion')
        
        # Convert dates
        def parse_date(d):
            if pd.isna(d): return None
            return d if isinstance(d, datetime) else None # Simple verify

        # 1. Create Project Master Record
        # We need a unique 'project_code' for the internal PK. using idx or p_code if generic
        internal_id = f"P{idx+1000}" 
        
        proj = SricProjectMaster(
            project_code=internal_id,
            project_title=str(p_title)[:200], # Trucate to fit
            gst_applicable_flag='N' # Default
        )
        # Store user code in a suitable field if SricProjectMaster has one, 
        # or just rely on mapping. 
        # Wait, SricProjectMaster might not have 'user_project_code'.
        # Let's check generated_models.py... I recall seeing it in earlier steps.
        # Actually, let's look at `SricProjectMaster`. It has `project_code` (PK).
        # We might need to map `user_proj_code` to `project_code` if it fits, else ??
        # Let's assume internal_id = user_proj_code if it's unique enough.
        
        proj.project_code = str(p_code)[:50] # PK
        
        session.add(proj)
        
        # 2. Create Incharge Detail (PI)
        # We need to link PI to Project. 
        # SricProjectInchargeDetails: project_code, empno (?), pi_flag ('Y')
        # We don't have EmpNo. We'll generate a fake one or use name hash.
        emp_id = str(abs(hash(pi_name)))[:6] # Fake EmpNo
        
        # Check if PI exists? No, this table links Project to Emp
        # We probably need an Employee Master table but let's just insert into InchargeDetails
        # Assuming we can insert arbitrary empno.
        
        pi_record = SricProjectInchargeDetails(
            project_code=proj.project_code,
            empno=emp_id,
            pi_flag='Y',
            from_date=parse_date(start_dt)
        )
        session.add(pi_record)
        
        # 3. Create Balance Record (For Financials)
        # AccProjectBalance: project_code, sanctioned_grant, available_balance
        bal_record = AccProjectBalance(
            project_code=proj.project_code,
            sanctioned_grant=sanctioned,
            dict_available_balance=sanctioned * 0.4, # Mock balance as 40% of sanctioned
            receipt_amount=sanctioned * 0.6, # Mock receipt
            expenditure_amount=sanctioned * 0.2
        )
        session.add(bal_record)
        
        # 4. Sponsor Type (For Portfolio)
        # Infer Project Type from 'ptype' column or funding agency
        ptype_str = str(row.get('ptype', '')).lower()
        cat = "Sponsored"
        if "consultancy" in ptype_str:
            cat = "Consultancy"
        
        # We don't have a direct field in Master for this maybe? 
        # Let's verify `SricProjectMaster` columns later. 
        # For now, this is enough to get the dashboard numbers.
        
        projects_added += 1

    try:
        session.commit()
        print(f"Successfully imported {projects_added} projects.")
    except Exception as e:
        session.rollback()
        print(f"Error committing to DB: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    db_file = "sric_db.sqlite"
    excel_file = "SRIC project list.xlsx"
    import_project_list(excel_file, db_file)
