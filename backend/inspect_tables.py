
import sys
import os
sys.path.append(os.getcwd())
try:
    from app.models.generated_models import SricProjectInchargeDetails, ViwEmpmas, ViwDpcode, SricProjectMaster
    
    tables = [SricProjectInchargeDetails, ViwEmpmas, ViwDpcode, SricProjectMaster]
    
    with open("table_columns.txt", "w", encoding="utf-8") as f:
        for t in tables:
            f.write(f"\n--- {t.__name__} Columns ---\n")
            for col in t.__table__.columns:
                f.write(f"{col.name}: {col.type}\n")

except ImportError as e:
    print(f"Import Error: {e}")
