
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.generated_models import (
    SricProjectMaster, 
    SricProjectInchargeDetails, 
    AccProjectBalance, 
    ProjectProposalMaster,
    SponsorMaster,
    SricProjectStaffMaster
)
from app.schemas.dashboard import (
    KPIMetrics, ProjectSummary, ExecutiveMetrics, FinancialMetrics, 
    PortfolioMetrics, HRMetrics, DepartmentMetrics, PipelineMetrics
)
from datetime import datetime, timedelta

class DashboardService:
    def __init__(self, db: Session):
        self.db = db

    def get_kpi_metrics(self) -> KPIMetrics:
        # Legacy Support
        total_funding = self.db.query(func.sum(SricProjectMaster.total_sanctioned_grant)).scalar() or 0.0
        active_projects = self.db.query(SricProjectMaster).filter(SricProjectMaster.sric_cl_flg != 'C').count()
        return KPIMetrics(
            funding=float(total_funding),
            projects=active_projects,
            deployments=87, patents=156, companies=234, researchers=567, roi=385.0, impact=94.5
        )

    def get_recent_projects(self, limit: int = 10) -> list[ProjectSummary]:
        results = []
        query = (
            self.db.query(SricProjectMaster, SricProjectInchargeDetails)
            .outerjoin(SricProjectInchargeDetails, SricProjectMaster.user_project_code == SricProjectInchargeDetails.user_project_code)
            .filter(SricProjectMaster.sric_cl_flg != 'C')
            .limit(limit)
        )
        seen = set()
        for p, pi_details in query.all():
            if p.project_code in seen: continue
            seen.add(p.project_code)
            
            start, end = p.date_of_commencement, p.closing_date
            duration_str = f"{(end - start).days // 30} months" if start and end else "N/A"
            
            results.append(ProjectSummary(
                id=p.project_code,
                user_project_code=p.user_project_code,
                title=p.title or "Untitled",
                pi=pi_details.stakeholder_name if pi_details else "Dr. Unknown",
                department=pi_details.stakeholder_dept if pi_details else "General",
                funding=float(p.total_sanctioned_grant or 0.0) / 100000,
                duration=duration_str,
                progress=50, team=5, summary=f"Project regarding {p.title}", keywords=["Research"], status="In Progress"
            ))
        return results

    # 1. Executive Summary
    def get_executive_summary(self) -> ExecutiveMetrics:
        active_projects = self.db.query(SricProjectMaster).filter(SricProjectMaster.sric_cl_flg != 'C').count()
        total_sanctioned = self.db.query(func.sum(SricProjectMaster.total_sanctioned_grant)).scalar() or 0.0
        total_balance = self.db.query(func.sum(AccProjectBalance.cl_balance)).scalar() or 0.0
        
        # Closing soon < 30 days
        next_30_days = datetime.now().date() + timedelta(days=30)
        closing_soon = self.db.query(SricProjectMaster).filter(
            SricProjectMaster.closing_date <= next_30_days,
            SricProjectMaster.sric_cl_flg != 'C'
        ).count()

        # Success Rate
        total_proposals = self.db.query(ProjectProposalMaster).count()
        approved_proposals = self.db.query(ProjectProposalMaster).filter(ProjectProposalMaster.status == 'Approved').count()
        rate = (approved_proposals / total_proposals * 100) if total_proposals > 0 else 0.0
        
        return ExecutiveMetrics(
            total_active_projects=active_projects,
            total_sanctioned_funds=float(total_sanctioned),
            total_available_balance=float(total_balance),
            projects_closing_soon=closing_soon,
            proposal_success_rate=rate
        )

    # 2. Financial Health
    def get_financial_health(self) -> FinancialMetrics:
        receipts = self.db.query(func.sum(AccProjectBalance.receipt_amount)).scalar() or 0.0
        payments = self.db.query(func.sum(AccProjectBalance.payment_amount)).scalar() or 0.0
        negative_bal = self.db.query(AccProjectBalance).filter(AccProjectBalance.cl_balance < 0).count()
        
        return FinancialMetrics(
            funds_received_ytd=float(receipts),
            total_expenditure_ytd=float(payments),
            pending_invoices=1250000.0, # Mocked for now (no bill table seeded)
            overhead_collection=float(receipts) * 0.15, # Approximated as 15% of receipts
            negative_balance_projects=negative_bal
        )

    # 3. Project Portfolio
    def get_project_portfolio(self) -> PortfolioMetrics:
        sponsored = self.db.query(SricProjectMaster).filter(SricProjectMaster.project_type == 'Sponsored').count()
        consultancy = self.db.query(SricProjectMaster).filter(SricProjectMaster.project_type == 'Consultancy').count()
        
        # Sponsor Distribution
        # Note: SponsorMaster links to projects via sponsor_code usually, but we haven't seeded that link fully.
        # We will count sponsors directly for distribution proxy
        govt = self.db.query(SponsorMaster).filter(SponsorMaster.sponsor_type == 'Govt').count()
        private = self.db.query(SponsorMaster).filter(SponsorMaster.sponsor_type == 'Private').count()
        
        distributions = {"Govt": govt, "Private": private, "International": 0}
        
        return PortfolioMetrics(
            sponsored_count=sponsored,
            consultancy_count=consultancy,
            sponsor_type_distribution=distributions,
            avg_project_duration_months=24, # simplified
            delayed_projects_count=2
        )

    # 4. HR Metrics
    def get_hr_metrics(self) -> HRMetrics:
        total_staff = self.db.query(SricProjectStaffMaster).filter(SricProjectStaffMaster.in_service == 'Y').count()
        
        jrfs = self.db.query(SricProjectStaffMaster).filter(SricProjectStaffMaster.empdesg == 'JRF').count()
        srfs = self.db.query(SricProjectStaffMaster).filter(SricProjectStaffMaster.empdesg == 'SRF').count()
        ras = self.db.query(SricProjectStaffMaster).filter(SricProjectStaffMaster.empdesg == 'RA').count()
        
        males = self.db.query(SricProjectStaffMaster).filter(SricProjectStaffMaster.emp_sex == 'M').count()
        females = self.db.query(SricProjectStaffMaster).filter(SricProjectStaffMaster.emp_sex == 'F').count()
        
        return HRMetrics(
            total_project_staff=total_staff,
            staff_role_breakdown={"JRF": jrfs, "SRF": srfs, "RA": ras},
            salary_outflow_monthly=float(total_staff * 35000), # Approx
            pending_hra_claims=5,
            gender_diversity_ratio=f"{males}:{females}"
        )

    # 5. Pipeline
    def get_pipeline_metrics(self) -> PipelineMetrics:
        submitted = self.db.query(ProjectProposalMaster).filter(ProjectProposalMaster.status == 'Submitted').count()
        value = self.db.query(func.sum(ProjectProposalMaster.project_cost)).filter(ProjectProposalMaster.status == 'Submitted').scalar() or 0.0
        pending = self.db.query(ProjectProposalMaster).filter(ProjectProposalMaster.status == 'Pending').count()
        
        return PipelineMetrics(
            proposals_submitted=submitted,
            pipeline_value=float(value),
            pending_approvals=pending
        )
