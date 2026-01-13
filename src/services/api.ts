
const API_BASE_URL = 'http://localhost:8000/api/v1/dashboard';

export interface KPIMetricsData {
    funding: number;
    deployments: number;
    patents: number;
    companies: number;
    projects: number;
    researchers: number;
    roi: number;
    impact: number;
}

export interface ProjectSummary {
    id: number;
    user_project_code?: string;
    title: string;
    pi: string;
    department: string;
    funding: number;
    duration: string;
    progress: number;
    team: number;
    summary: string;
    keywords: string[];
    status: string;
}

export const fetchKPIMetrics = async (): Promise<KPIMetricsData> => {
    const response = await fetch(`${API_BASE_URL}/kpi`);
    if (!response.ok) {
        throw new Error('Failed to fetch KPI metrics');
    }
    return response.json();
};

export const fetchRecentProjects = async (): Promise<ProjectSummary[]> => {
    const response = await fetch(`${API_BASE_URL}/projects`);
    if (!response.ok) {
        throw new Error('Failed to fetch recent projects');
    }
    return response.json();
};

// 1. Executive Summary
export interface ExecutiveMetrics {
    total_active_projects: number;
    total_sanctioned_funds: number;
    total_available_balance: number;
    projects_closing_soon: number;
    proposal_success_rate: number;
}

// 2. Financial Health
export interface FinancialMetrics {
    funds_received_ytd: number;
    total_expenditure_ytd: number;
    pending_invoices: number;
    overhead_collection: number;
    negative_balance_projects: number;
}

// 3. Project Portfolio
export interface PortfolioMetrics {
    sponsored_count: number;
    consultancy_count: number;
    sponsor_type_distribution: Record<string, number>;
    avg_project_duration_months: number;
    delayed_projects_count: number;
}

// 4. HR Metrics
export interface HRMetrics {
    total_project_staff: number;
    staff_role_breakdown: Record<string, number>;
    salary_outflow_monthly: number;
    pending_hra_claims: number;
    gender_diversity_ratio: string;
}

// 6. Pipeline Metrics
export interface PipelineMetrics {
    proposals_submitted: number;
    pipeline_value: number;
    pending_approvals: number;
}

export const fetchExecutiveMetrics = async (): Promise<ExecutiveMetrics> => {
    const response = await fetch(`${API_BASE_URL}/executive`);
    return response.json();
};

export const fetchFinancialMetrics = async (): Promise<FinancialMetrics> => {
    const response = await fetch(`${API_BASE_URL}/financial`);
    return response.json();
};

export const fetchPortfolioMetrics = async (): Promise<PortfolioMetrics> => {
    const response = await fetch(`${API_BASE_URL}/portfolio`);
    return response.json();
};

export const fetchHRMetrics = async (): Promise<HRMetrics> => {
    const response = await fetch(`${API_BASE_URL}/hr`);
    return response.json();
};

export const fetchPipelineMetrics = async (): Promise<PipelineMetrics> => {
    const response = await fetch(`${API_BASE_URL}/pipeline`);
    return response.json();
};
