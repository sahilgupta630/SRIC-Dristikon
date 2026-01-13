
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.dashboard_service import DashboardService
from app.schemas.dashboard import (
    KPIMetrics, ProjectSummary, ExecutiveMetrics, FinancialMetrics, 
    PortfolioMetrics, HRMetrics, PipelineMetrics
)

router = APIRouter()

def get_service(db: Session = Depends(get_db)) -> DashboardService:
    return DashboardService(db)

@router.get("/kpi", response_model=KPIMetrics)
def get_kpi_metrics(service: DashboardService = Depends(get_service)):
    return service.get_kpi_metrics()

@router.get("/projects", response_model=list[ProjectSummary])
def get_recent_projects(limit: int = 10, service: DashboardService = Depends(get_service)):
    return service.get_recent_projects(limit)

@router.get("/executive", response_model=ExecutiveMetrics)
def get_executive_summary(service: DashboardService = Depends(get_service)):
    return service.get_executive_summary()

@router.get("/financial", response_model=FinancialMetrics)
def get_financial_health(service: DashboardService = Depends(get_service)):
    return service.get_financial_health()

@router.get("/portfolio", response_model=PortfolioMetrics)
def get_portfolio_metrics(service: DashboardService = Depends(get_service)):
    return service.get_project_portfolio()

@router.get("/hr", response_model=HRMetrics)
def get_hr_metrics(service: DashboardService = Depends(get_service)):
    return service.get_hr_metrics()

@router.get("/pipeline", response_model=PipelineMetrics)
def get_pipeline_metrics(service: DashboardService = Depends(get_service)):
    return service.get_pipeline_metrics()
