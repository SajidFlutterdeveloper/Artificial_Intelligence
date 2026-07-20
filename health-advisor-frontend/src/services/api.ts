import axios, { AxiosInstance } from 'axios';
import { HealthAnalysisResponse, ApiError } from '../types/index';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

const apiClient: AxiosInstance = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const healthAdvisorAPI = {
  /**
   * Analyze patient health information
   * @param patientData - Patient information text
   * @returns Health analysis response
   */
  analyzeHealth: async (patientData: string): Promise<HealthAnalysisResponse> => {
    try {
      const response = await apiClient.post<HealthAnalysisResponse>(
        '/api/analyze',
        { patient_data: patientData }
      );
      return response.data;
    } catch (error) {
      if (axios.isAxiosError(error)) {
        const apiError = error.response?.data as ApiError | undefined;
        throw new Error(apiError?.detail || error.message || 'Failed to analyze health');
      }
      throw new Error('An unexpected error occurred');
    }
  },

  /**
   * Check API health status
   * @returns Health check response
   */
  checkHealth: async (): Promise<{ status: string; service: string; version: string }> => {
    try {
      const response = await apiClient.get('/api/health');
      return response.data;
    } catch (error) {
      throw new Error('Failed to connect to API');
    }
  },
};

export default apiClient;
