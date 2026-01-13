
import sys
import os
sys.path.append(os.getcwd())

from app.core.database import SessionLocal
from app.services.dashboard_service import DashboardService

try:
    db = SessionLocal()
    service = DashboardService(db)
    projects = service.get_recent_projects()
    print(f"Found {len(projects)} projects")
    for p in projects:
        print(f"ID: {p.id}, Code: {p.user_project_code}, PI: {p.pi}, Dept: {p.department}")

except Exception as e:
    print("Error:", e)
    import traceback
    traceback.print_exc()
finally:
    db.close()
