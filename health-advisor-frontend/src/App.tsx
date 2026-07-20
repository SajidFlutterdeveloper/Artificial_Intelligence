import React, { useState } from 'react';
import { Header } from './components/Header';
import { InputForm } from './components/InputForm';
import { AnalysisResult } from './components/AnalysisResult';
import { ErrorMessage } from './components/ErrorMessage';
import { Footer } from './components/Footer';
import { healthAdvisorAPI } from './services/api';
import { HealthAnalysisResponse } from './types/index';

function App() {
  const [analysisData, setAnalysisData] = useState<HealthAnalysisResponse | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleAnalyze = async (patientData: string) => {
    setIsLoading(true);
    setError(null);

    try {
      const result = await healthAdvisorAPI.analyzeHealth(patientData);
      setAnalysisData(result);
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Failed to analyze health';
      setError(errorMessage);
      console.error('Analysis error:', err);
    } finally {
      setIsLoading(false);
    }
  };

  const handleReset = () => {
    setAnalysisData(null);
    setError(null);
  };

  const handleDismissError = () => {
    setError(null);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 flex flex-col">
      <Header />

      <main className="flex-1 max-w-6xl w-full mx-auto px-4 py-8">
        {error && <ErrorMessage message={error} onDismiss={handleDismissError} />}

        {analysisData ? (
          <AnalysisResult data={analysisData} onReset={handleReset} />
        ) : (
          <div className="space-y-6">
            <div className="text-center mb-8">
              <h2 className="text-3xl font-bold text-gray-900 mb-2">Health Analysis</h2>
              <p className="text-gray-600 max-w-2xl mx-auto">
                Enter patient information below for a comprehensive AI-powered health analysis. Our system will provide
                insights on healthy habits, areas for improvement, and personalized recommendations.
              </p>
            </div>
            <InputForm onSubmit={handleAnalyze} isLoading={isLoading} />
          </div>
        )}
      </main>

      <Footer />
    </div>
  );
}

export default App;
