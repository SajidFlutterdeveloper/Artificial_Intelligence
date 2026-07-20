import React, { useState } from 'react';
import { Send, Loader } from 'lucide-react';

interface InputFormProps {
  onSubmit: (data: string) => Promise<void>;
  isLoading: boolean;
}

export const InputForm: React.FC<InputFormProps> = ({ onSubmit, isLoading }) => {
  const [patientData, setPatientData] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');

    if (!patientData.trim() || patientData.trim().length < 10) {
      setError('Please enter at least 10 characters of patient information');
      return;
    }

    try {
      await onSubmit(patientData);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    }
  };

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label htmlFor="patientData" className="block text-sm font-semibold text-gray-700 mb-2">
            Patient Information
          </label>
          <textarea
            id="patientData"
            value={patientData}
            onChange={(e) => {
              setPatientData(e.target.value);
              setError('');
            }}
            placeholder="Enter patient information here... (e.g., Age: 35, Weight: 85kg, Height: 180cm, Exercise: 2 times/week, Diet: Mixed, Sleep: 6 hours)"
            className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent resize-none"
            rows={6}
            disabled={isLoading}
          />
          <p className="text-xs text-gray-500 mt-2">Minimum 10 characters required</p>
        </div>

        {error && (
          <div className="bg-red-50 border border-red-200 rounded-lg p-3 text-red-700 text-sm">
            ⚠️ {error}
          </div>
        )}

        <button
          type="submit"
          disabled={isLoading || !patientData.trim()}
          className="w-full bg-gradient-to-r from-primary-600 to-primary-500 text-white font-semibold py-3 rounded-lg hover:shadow-lg transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
        >
          {isLoading ? (
            <>
              <Loader className="w-5 h-5 animate-spin" />
              Analyzing...
            </>
          ) : (
            <>
              <Send className="w-5 h-5" />
              Analyze Health
            </>
          )}
        </button>
      </form>
    </div>
  );
};
