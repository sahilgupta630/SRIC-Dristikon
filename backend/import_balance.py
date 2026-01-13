
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
        AccProjectBalance
    )
except ImportError:
    pass

def clean_money(val):
    if pd.isna(val): return 0.0
    try:
        val = str(val).replace(',', '').replace('₹', '').strip()
        return float(val)
    except:
        return 0.0

def import_balance(excel_path):
    print("Importing Balance...")
    xl = pd.ExcelFile(excel_path)
    target_sheet = next((s for s in xl.sheet_names if "Active" in s), xl.sheet_names[0])
    df = pd.read_excel(excel_path, sheet_name=target_sheet)
    df.columns = [str(c).lower().strip().replace(' ', '_').replace('.', '') for c in df.columns]
    
    session = SessionLocal()
    session.query(AccProjectBalance).delete()
    
    count = 0
    seen_codes = set()
    
    for idx, row in df.iterrows():
        ucode = str(row.get('user_project_code')).strip()
        if not ucode or ucode == 'nan': ucode = f"G-{idx}"
        if ucode in seen_codes: continue
        seen_codes.add(ucode)
        
        val = clean_money(row.get('project_value'))
        project_id = idx + 1 # Matching what we did in Master
        
        bal = AccProjectBalance(
            project_code=project_id,
            balance_date=datetime.now().date(),
            op_balance=0.0,
            receipt_amount=val,
            payment_amount=0.0,
            cl_balance=val,
            deleted_flag='N',
            created_by='script'
        )
        session.add(bal)
        try:
            session.flush()
            count += 1
        except Exception as e:
            print(f"Balance Fail {project_id}: {e}")
            
    session.commit()
    print(f"Imported {count} Balance Records.")

if __name__ == "__main__":
    import_balance("SRIC project list.xlsx")
