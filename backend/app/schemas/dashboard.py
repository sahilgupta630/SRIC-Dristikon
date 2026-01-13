
from pydantic import BaseModel
from typing import List, Optional, Dict

class KPIMetrics(BaseModel):
    funding: float
    projects: int
    deployments: int
    patents: int
    companies: int
    researchers: int
    roi: float
    impact: float

class ProjectSummary(BaseModel):
    id: int
    user_project_code: Optional[str]
    title: Optional[str]
    pi: str
    department: str
    funding: float
    duration: str
    progress: int
    team: int
    summary: str
    keywords: List[str]
    status: str

# 1. Executive Summary
class ExecutiveMetrics(BaseModel):
    total_active_projects: int
    total_sanctioned_funds: float
    total_available_balance: float
    projects_closing_soon: int
    proposal_success_rate: float

# 2. Financial Health
class FinancialMetrics(BaseModel):
    funds_received_ytd: float
    total_expenditure_ytd: float
    pending_invoices: float
    overhead_collection: float
    negative_balance_projects: int

# 3. Project Portfolio
class PortfolioMetrics(BaseModel):
    sponsored_count: int
    consultancy_count: int
    sponsor_type_distribution: Dict[str, int] # e.g. {"Govt": 10, "Private": 5}
    avg_project_duration_months: int
    delayed_projects_count: int

# 4. HR Metrics
class HRMetrics(BaseModel):
    total_project_staff: int
    staff_role_breakdown: Dict[str, int]
    salary_outflow_monthly: float
    pending_hra_claims: int
    gender_diversity_ratio: str # "M:F"

# 5. Department Performance
class DepartmentMetrics(BaseModel):
    department: str
    total_funding: float
    project_count: int

# 6. Pipeline
class PipelineMetrics(BaseModel):
    proposals_submitted: int
    pipeline_value: float
    pending_approvals: int
