
import sys
import os
sys.path.append(os.getcwd())
try:
    from app.models.generated_models import AccProjectBalance, ProjectProposalMaster, SponsorMaster, SricProjectStaffMaster, StaffSalaryFellowshipClaim
    
    tables = [AccProjectBalance, ProjectProposalMaster, SponsorMaster, SricProjectStaffMaster, StaffSalaryFellowshipClaim]
    
    with open("new_kpi_tables.txt", "w", encoding="utf-8") as f:
        for t in tables:
            f.write(f"\n--- {t.__name__} Columns ---\n")
            try:
                for col in t.__table__.columns:
                    f.write(f"{col.name}: {col.type}\n")
            except Exception as e:
                f.write(f"Error reading columns: {e}\n")

except ImportError as e:
    with open("new_kpi_tables.txt", "w", encoding="utf-8") as f:
        f.write(f"Import Error: {e}")
