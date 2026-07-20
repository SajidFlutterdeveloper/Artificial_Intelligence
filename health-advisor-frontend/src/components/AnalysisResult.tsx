import React from 'react';
import { HealthAnalysisResponse } from '../types/index';
import { CheckCircle, AlertCircle, Lightbulb, AlertTriangle, Download, Share2 } from 'lucide-react';

interface AnalysisResultProps {
  data: HealthAnalysisResponse;
  onReset: () => void;
}

export const AnalysisResult: React.FC<AnalysisResultProps> = ({ data, onReset }) => {
  const handleDownload = () => {
    const content = `HEALTH ADVISOR AI - ANALYSIS REPORT
=====================================

Analysis Date: ${new Date(data.timestamp).toLocaleString()}

HEALTH SUMMARY
--------------
${data.summary}

HEALTHY HABITS
--------------
${data.healthy_habits.map((h) => `✓ ${h}`).join('\n')}

AREAS FOR IMPROVEMENT
---------------------
${data.unhealthy_habits.map((h) => `⚠ ${h}`).join('\n')}

RECOMMENDATIONS
---------------
${data.recommendations.map((r) => `• ${r}`).join('\n')}

DISCLAIMER
----------
${data.disclaimer}`;

    const element = document.createElement('a');
    element.setAttribute('href', `data:text/plain;charset=utf-8,${encodeURIComponent(content)}`);
    element.setAttribute('download', `health-analysis-${Date.now()}.txt`);
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
  };

  const handleShare = async () => {
    const shareText = `Health Analysis Report:\n${data.summary}`;
    if (navigator.share) {
      try {
        await navigator.share({
          title: 'Health Advisor AI Analysis',
          text: shareText,
        });
      } catch (err) {
        console.log('Share cancelled or failed');
      }
    } else {
      alert('Sharing not supported on this device');
    }
  };

  return (
    <div className="space-y-6 animate-slide-up">
      {/* Summary Section */}
      <div className="bg-gradient-to-r from-blue-50 to-blue-100 rounded-lg p-6 border border-blue-200">
        <h2 className="text-2xl font-bold text-blue-900 mb-3">Health Summary</h2>
        <p className="text-blue-800 leading-relaxed">{data.summary}</p>
      </div>

      {/* Healthy Habits */}
      <div className="bg-green-50 rounded-lg p-6 border border-green-200">
        <div className="flex items-center gap-2 mb-4">
          <CheckCircle className="w-6 h-6 text-green-600" />
          <h3 className="text-xl font-bold text-green-900">Healthy Habits ({data.healthy_habits.length})</h3>
        </div>
        <div className="space-y-2">
          {data.healthy_habits.length > 0 ? (
            data.healthy_habits.map((habit, idx) => (
              <div key={idx} className="flex items-start gap-2 text-green-800">
                <span className="text-green-600 font-bold mt-1">✓</span>
                <p>{habit}</p>
              </div>
            ))
          ) : (
            <p className="text-green-700">No specific healthy habits identified.</p>
          )}
        </div>
      </div>

      {/* Unhealthy Habits */}
      <div className="bg-red-50 rounded-lg p-6 border border-red-200">
        <div className="flex items-center gap-2 mb-4">
          <AlertCircle className="w-6 h-6 text-red-600" />
          <h3 className="text-xl font-bold text-red-900">Areas for Improvement ({data.unhealthy_habits.length})</h3>
        </div>
        <div className="space-y-2">
          {data.unhealthy_habits.length > 0 ? (
            data.unhealthy_habits.map((habit, idx) => (
              <div key={idx} className="flex items-start gap-2 text-red-800">
                <span className="text-red-600 font-bold mt-1">⚠</span>
                <p>{habit}</p>
              </div>
            ))
          ) : (
            <p className="text-red-700">No specific areas for improvement identified.</p>
          )}
        </div>
      </div>

      {/* Recommendations */}
      <div className="bg-amber-50 rounded-lg p-6 border border-amber-200">
        <div className="flex items-center gap-2 mb-4">
          <Lightbulb className="w-6 h-6 text-amber-600" />
          <h3 className="text-xl font-bold text-amber-900">Recommendations ({data.recommendations.length})</h3>
        </div>
        <div className="space-y-3">
          {data.recommendations.length > 0 ? (
            data.recommendations.map((rec, idx) => (
              <div key={idx} className="flex items-start gap-3">
                <span className="bg-amber-600 text-white rounded-full w-6 h-6 flex items-center justify-center text-sm font-bold flex-shrink-0">
                  {idx + 1}
                </span>
                <p className="text-amber-900 pt-1">{rec}</p>
              </div>
            ))
          ) : (
            <p className="text-amber-700">No specific recommendations at this time.</p>
          )}
        </div>
      </div>

      {/* Disclaimer */}
      <div className="bg-purple-50 rounded-lg p-6 border border-purple-200">
        <div className="flex items-center gap-2 mb-3">
          <AlertTriangle className="w-6 h-6 text-purple-600" />
          <h3 className="text-lg font-bold text-purple-900">Important Disclaimer</h3>
        </div>
        <p className="text-purple-800 text-sm leading-relaxed">{data.disclaimer}</p>
      </div>

      {/* Action Buttons */}
      <div className="flex gap-3 flex-wrap">
        <button
          onClick={handleDownload}
          className="flex-1 min-w-[200px] bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-lg transition-colors flex items-center justify-center gap-2"
        >
          <Download className="w-5 h-5" />
          Download Report
        </button>
        <button
          onClick={handleShare}
          className="flex-1 min-w-[200px] bg-green-600 hover:bg-green-700 text-white font-semibold py-3 rounded-lg transition-colors flex items-center justify-center gap-2"
        >
          <Share2 className="w-5 h-5" />
          Share Report
        </button>
        <button
          onClick={onReset}
          className="flex-1 min-w-[200px] bg-gray-600 hover:bg-gray-700 text-white font-semibold py-3 rounded-lg transition-colors"
        >
          New Analysis
        </button>
      </div>
    </div>
  );
};
