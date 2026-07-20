# Health Advisor AI - Frontend

Professional Healthcare AI System Frontend built with React, TypeScript, and Tailwind CSS.

## 🎨 Features

- **Modern UI**: Responsive design with Tailwind CSS
- **TypeScript Support**: Full type safety
- **Real-time Analysis**: Interactive health assessment
- **Report Management**: Download and share analysis results
- **Error Handling**: Comprehensive error management
- **Mobile Friendly**: Works seamlessly on all devices
- **Accessibility**: WCAG compliant components

## 🛠️ Prerequisites

- Node.js 16+
- npm or yarn
- Backend API running on `http://localhost:8000`

## 📦 Installation

```bash
cd health-advisor-frontend
npm install
```

## 🚀 Development

```bash
npm run dev
```

The app will open at `http://localhost:5173`

## 🏗️ Build for Production

```bash
npm run build
```

Preview the build:

```bash
npm run preview
```

## 📝 Environment Configuration

Create `.env` file:

```env
VITE_API_BASE_URL=http://localhost:8000
```

## 📁 Project Structure

```
src/
├── components/           # React components
│   ├── Header.tsx       # App header
│   ├── InputForm.tsx    # Patient data form
│   ├── AnalysisResult.tsx # Results display
│   ├── ErrorMessage.tsx # Error handling
│   └── Footer.tsx       # App footer
├── services/            # API services
│   └── api.ts          # API client
├── types/              # TypeScript types
│   └── index.ts        # Type definitions
├── App.tsx             # Main app component
├── main.tsx            # React entry point
└── index.css           # Global styles
```

## 🔌 API Integration

The frontend communicates with the backend via RESTful API:

- **Endpoint**: `POST /api/analyze`
- **Request**: `{ patient_data: string }`
- **Response**: `HealthAnalysisResponse`

## 📚 Components

### Header
Displays the application title and branding.

### InputForm
Allows users to input patient information for analysis.

### AnalysisResult
Displays comprehensive health analysis results with recommendations.

### ErrorMessage
Shows user-friendly error messages.

### Footer
Application footer with information and contact details.

## 🎯 Features Usage

### Submit Analysis
1. Enter patient information (minimum 10 characters)
2. Click "Analyze Health"
3. Wait for AI analysis (displayed with loading state)
4. Review comprehensive results

### Download Report
Click "Download Report" to save analysis as text file.

### Share Results
Click "Share Report" to share via native share API (if supported).

### New Analysis
Click "New Analysis" to perform another assessment.

## 🐛 Troubleshooting

### API Connection Error
- Ensure backend is running on `http://localhost:8000`
- Check `VITE_API_BASE_URL` in `.env`

### Build Issues
```bash
rm -rf node_modules package-lock.json
npm install
npm run build
```

## 🔒 Security

- Input validation on client side
- XSS protection through React
- CSRF protection via backend
- Secure API communication

## 🚀 Deployment

### Vercel
```bash
npm install -g vercel
vercel
```

### Netlify
```bash
npm run build
# Deploy dist/ folder
```

### Docker
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 5173
CMD ["npm", "run", "preview"]
```

## 📊 Performance Optimization

- Code splitting with Vite
- Lazy loading of components
- Image optimization
- CSS minification
- Bundle size analysis

## 🧪 Testing (Future)

- Unit tests with Vitest
- Component tests with React Testing Library
- E2E tests with Cypress

## 📄 License

MIT License

## 👨‍💼 Author

Sajid Flutter Developer

## 📞 Support

For issues and questions, create an issue in the repository.
