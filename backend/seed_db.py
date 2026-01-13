
import pandas as pd
import sys
import os
from datetime import datetime

sys.path.append(os.getcwd())

from app.core.database import SessionLocal, engine, Base
from app.models.generated_models import (
    SricProjectMaster, 
    SricProjectInchargeDetails,
    AccProjectBalance, 
    ProjectProposalMaster, 
    SponsorMaster, 
    SricProjectStaffMaster, 
    StaffSalaryFellowshipClaim
)

# Create tables
SricProjectMaster.metadata.create_all(bind=engine)
SricProjectInchargeDetails.metadata.create_all(bind=engine)
AccProjectBalance.metadata.create_all(bind=engine)
ProjectProposalMaster.metadata.create_all(bind=engine)
SponsorMaster.metadata.create_all(bind=engine)
SricProjectStaffMaster.metadata.create_all(bind=engine)
StaffSalaryFellowshipClaim.metadata.create_all(bind=engine)

def parse_date(date_val):
    if pd.isna(date_val):
        return None
    try:
        return pd.to_datetime(date_val).date()
    except:
        return None


def seed_projects():
    print("Seeding mock data for SricProjectMaster...")
    
    db = SessionLocal()
    
    # Check if data exists
    if db.query(SricProjectMaster).count() > 0:
        print("Data already exists. Skipping seed.")
        db.close()
        return

    # Create mock projects
    mock_projects = [
        {
            "project_code": 1001,
            "title": "AI-Powered Healthcare Diagnostics Platform",
            "total_sanctioned_grant": 8500000,
            "date_of_commencement": datetime(2023, 1, 15).date(),
            "closing_date": datetime(2025, 1, 15).date(),
            "sric_cl_flg": "A",
            "user_project_code": "1001",
            "delete_flag": "N",
            "sric_virtual_project_flag": "N",
            "project_type": "Sponsored"
        },
        {
            "project_code": 1002,
            "title": "Smart Grid Optimization using IoT and Machine Learning",
            "total_sanctioned_grant": 7200000,
            "date_of_commencement": datetime(2023, 3, 1).date(),
            "closing_date": datetime(2024, 9, 1).date(),
            "sric_cl_flg": "A",
            "user_project_code": "1002",
            "delete_flag": "N",
            "sric_virtual_project_flag": "N",
            "project_type": "Sponsored"
        },
        {
            "project_code": 1003,
            "title": "Autonomous Robot for Industrial Safety Inspection",
            "total_sanctioned_grant": 9500000,
            "date_of_commencement": datetime(2023, 6, 1).date(),
            "closing_date": datetime(2025, 12, 1).date(),
            "sric_cl_flg": "A",
            "user_project_code": "1003",
            "delete_flag": "N",
            "sric_virtual_project_flag": "N",
            "project_type": "Sponsored"
        },
        {
            "project_code": 1004,
            "title": "Quantum Computing for Cryptographic Applications",
            "total_sanctioned_grant": 12500000,
            "date_of_commencement": datetime(2024, 1, 1).date(),
            "closing_date": datetime(2028, 1, 1).date(),
            "sric_cl_flg": "A",
            "user_project_code": "1004",
            "delete_flag": "N",
            "sric_virtual_project_flag": "N",
            "project_type": "Sponsored"
        }
    ]
    
    for p_data in mock_projects:
        # Create Project
        project = SricProjectMaster(**p_data)
        db.add(project)
        
        # Create PI Logic
        pi_name = "Dr. Unknown"
        dept = "General"
        
        if p_data["user_project_code"] == "1001":
            pi_name = "Dr. Rajesh Kumar"
            dept = "CSE"
        elif p_data["user_project_code"] == "1002":
             pi_name = "Prof. Ananya Sharma"
             dept = "EE"
        elif p_data["user_project_code"] == "1003":
             pi_name = "Dr. Vikram Singh"
             dept = "ME"
        elif p_data["user_project_code"] == "1004":
             pi_name = "Prof. Sarah Gupta"
             dept = "Physics"
             
        pi_details = SricProjectInchargeDetails(
            user_project_code=p_data["user_project_code"],
            type="PI", # Principal Investigator
            stakeholder_name=pi_name,
            stakeholder_dept=dept,
            stakeholder_type="Faculty"
        )
        db.add(pi_details)

        # 3. Seed Balance (Financial Health)
        # Assuming project_code in AccProjectBalance links to user_project_code or project_code. 
        # Schema says project_code is INTEGER.
        balance = AccProjectBalance(
            project_code=p_data["project_code"],
            balance_date=datetime.now(),
            op_balance=float(p_data["total_sanctioned_grant"]),
            receipt_amount=float(p_data["total_sanctioned_grant"]) * 0.8,
            payment_amount=float(p_data["total_sanctioned_grant"]) * 0.3, # Spent 30%
            cl_balance=float(p_data["total_sanctioned_grant"]) * 0.5,
            created_by="system",
            deleted_flag="N"
        )
        db.add(balance)

    # 4. Seed Sponsors (Portfolio)
    sponsors = [
        {"sponsor_code": 1, "sponsor_name": "DST", "sponsor_type": "Govt", "country": "India", "delete_flag": "N"},
        {"sponsor_code": 2, "sponsor_name": "ISRO", "sponsor_type": "Govt", "country": "India", "delete_flag": "N"},
        {"sponsor_code": 3, "sponsor_name": "Google Research", "sponsor_type": "Private", "country": "USA", "delete_flag": "N"},
        {"sponsor_code": 4, "sponsor_name": "Tata Steel", "sponsor_type": "Private", "country": "India", "delete_flag": "N"},
    ]
    for s in sponsors:
        db.add(SponsorMaster(**s))

    # 5. Seed Project Staff (HR)
    # Linking to user_project_code 1001 for now
    staff_members = [
        {"empno": "S001", "empname": "Rahul Verma", "empdesg": "JRF", "user_project_code": "1001", "project_code": "1001", "emp_sex": "M", "in_service": "Y"},
        {"empno": "S002", "empname": "Priya Singh", "empdesg": "SRF", "user_project_code": "1001", "project_code": "1001", "emp_sex": "F", "in_service": "Y"},
        {"empno": "S003", "empname": "Amit Sharma", "empdesg": "RA", "user_project_code": "1002", "project_code": "1002", "emp_sex": "M", "in_service": "Y"},
    ]
    for staff in staff_members:
        db.add(SricProjectStaffMaster(**staff))

    # 6. Seed Proposals (Pipeline)
    proposals = [
        {"proposal_code": 501, "proposal_version": 1.0, "proposal_user_code": "P501", "project_type": "Sponsored", "title": "Advanced AI for Climate", "status": "Submitted", "project_cost": 5000000, "creation_date": datetime(2024, 1, 15), "acceptance_flag": "N", "delete_flag": "N", "created_by": "system"},
        {"proposal_code": 502, "proposal_version": 1.0, "proposal_user_code": "P502", "project_type": "Sponsored", "title": "Robotics in Agriculture", "status": "Approved", "project_cost": 8000000, "creation_date": datetime(2023, 11, 20), "acceptance_flag": "Y", "delete_flag": "N", "created_by": "system"},
        {"proposal_code": 503, "proposal_version": 1.0, "proposal_user_code": "P503", "project_type": "Consultancy", "title": "Quantum Sensors", "status": "Pending", "project_cost": 12000000, "creation_date": datetime(2024, 2, 10), "acceptance_flag": "N", "delete_flag": "N", "created_by": "system"},
    ]
    for prop in proposals:
        db.add(ProjectProposalMaster(**prop))
        
    try:
        db.commit()
        print(f"Seeded {len(mock_projects)} mock projects and supporting tables.")
    except Exception as e:
        with open("seed_error.txt", "w") as f:
            f.write(str(e))
        print(f"Error seeding data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_projects()
