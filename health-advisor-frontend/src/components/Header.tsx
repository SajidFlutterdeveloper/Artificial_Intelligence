import React from 'react';
import { Heart } from 'lucide-react';

export const Header: React.FC = () => {
  return (
    <header className="bg-gradient-to-r from-primary-600 to-primary-500 text-white shadow-lg">
      <div className="max-w-6xl mx-auto px-4 py-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="bg-white/20 p-2 rounded-lg backdrop-blur">
              <Heart className="w-8 h-8" fill="currentColor" />
            </div>
            <div>
              <h1 className="text-3xl font-bold">Health Advisor AI</h1>
              <p className="text-primary-100 text-sm">Professional Health Analysis Powered by AI</p>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};
