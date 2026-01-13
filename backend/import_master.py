
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
        SricProjectMaster
    )
except ImportError:
    print("Could not import app models.")
    sys.exit(1)

def import_project_master(excel_path):
    print(f"Reading {excel_path}...")
    xl = pd.ExcelFile(excel_path)
    target_sheet = next((s for s in xl.sheet_names if "Active" in s), xl.sheet_names[0])
    
    df = pd.read_excel(excel_path, sheet_name=target_sheet)
    df.columns = [str(c).lower().strip().replace(' ', '_').replace('.', '') for c in df.columns]
    
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    
    # Wipe Master Only
    session.query(SricProjectMaster).delete()
    
    count = 0
    seen = set()
    
    for idx, row in df.iterrows():
        try:
            ucode = str(row.get('user_project_code')).strip()
            if not ucode or ucode == 'nan': ucode = f"G-{idx}"
            
            if ucode in seen: continue
            seen.add(ucode)
            
            proj = SricProjectMaster(
                project_code=idx+1,
                user_project_code=ucode,
                title=str(row.get('title') or "No Title")[:100],
                sric_cl_flg='N',
                delete_flag='N'
            )
            session.add(proj)
            session.flush()
            count +=1
        except Exception as e:
            print(f"Row {idx} failed: {e}")
            
    session.commit()
    print(f"Imported {count} to Master.")

if __name__ == "__main__":
    import_project_master("SRIC project list.xlsx")
