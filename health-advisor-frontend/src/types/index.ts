export interface HealthAnalysisResponse {
  summary: string;
  healthy_habits: string[];
  unhealthy_habits: string[];
  recommendations: string[];
  disclaimer: string;
  timestamp: string;
}

export interface AnalysisState {
  loading: boolean;
  error: string | null;
  data: HealthAnalysisResponse | null;
}

export interface ApiError {
  detail: string;
  status_code: number;
}
