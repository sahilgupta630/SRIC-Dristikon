
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
        SricProjectInchargeDetails
    )
except ImportError:
    pass

def import_details(excel_path):
    print("Importing Details...")
    xl = pd.ExcelFile(excel_path)
    target_sheet = next((s for s in xl.sheet_names if "Active" in s), xl.sheet_names[0])
    df = pd.read_excel(excel_path, sheet_name=target_sheet)
    df.columns = [str(c).lower().strip().replace(' ', '_').replace('.', '') for c in df.columns]
    
    session = SessionLocal()
    session.query(SricProjectInchargeDetails).delete()
    
    count = 0
    seen = set()
    
    for idx, row in df.iterrows():
        ucode = str(row.get('user_project_code')).strip()
        if not ucode or ucode == 'nan': ucode = f"G-{idx}"
        if ucode in seen: continue
        seen.add(ucode)
        
        pi = str(row.get('pi') or "Unknown")
        dept = str(row.get('project_deptname') or "Unknown")
        
        det = SricProjectInchargeDetails(
            user_project_code=ucode,
            stakeholder_name=pi[:100],
            stakeholder_dept=dept[:100],
            stakeholder_type='PI',
            type='Internal'
        )
        session.add(det)
        try:
            session.flush()
            count += 1
        except Exception as e:
            print(f"PI Fail {ucode}: {e}")
            
    session.commit()
    print(f"Imported {count} PI Details.")

if __name__ == "__main__":
    import_details("SRIC project list.xlsx")
