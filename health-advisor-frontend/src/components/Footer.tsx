import React from 'react';

export const Footer: React.FC = () => {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="bg-gray-900 text-gray-300 mt-12 border-t border-gray-800">
      <div className="max-w-6xl mx-auto px-4 py-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
          <div>
            <h3 className="text-white font-semibold mb-4">About</h3>
            <p className="text-sm leading-relaxed">
              Health Advisor AI provides professional health analysis powered by advanced AI technology.
            </p>
          </div>
          <div>
            <h3 className="text-white font-semibold mb-4">Important</h3>
            <p className="text-sm">
              This tool is for informational purposes only. Always consult healthcare professionals for medical advice.
            </p>
          </div>
          <div>
            <h3 className="text-white font-semibold mb-4">Contact</h3>
            <p className="text-sm">For support or feedback, please reach out through GitHub.</p>
          </div>
        </div>
        <div className="border-t border-gray-800 pt-6 text-center text-sm">
          <p>&copy; {currentYear} Health Advisor AI. All rights reserved.</p>
          <p className="mt-2">Developed by Sajid Flutter Developer</p>
        </div>
      </div>
    </footer>
  );
};
