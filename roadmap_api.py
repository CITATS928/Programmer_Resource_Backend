from pymongo import MongoClient
import json

# MongoDB connection setup
CONNECTION_STRING = "mongodb+srv://root:root@programmerresource.dbqww.mongodb.net/"
client = MongoClient(CONNECTION_STRING)
db = client["Programmer_Resource"]
collection = db["Roadmap"]

data = {
    "id": 1,
    "name": "Frontend Engineer",
    "learning_path": {
      "CoreFundamentals": {
         "HTML": [
             "Learn basic syntax",
             "Forms and validations",
             "Accessibility (WCAG principles)",
             "SEO fundamentals"
             ],
         "CSS": [
             "Learn the basics",
             "Layout techniques (Flexbox, Grid)",
             "Responsive design (Media Queries, Mobile-first approach)",
             "CSS preprocessors (Sass, Less)"
             ],
         "JavaScript": [
             "Master the basics (Variables, Loops, Functions, etc.)",
             "DOM manipulation",
             "Fetch API / Ajax",
             "ES6+ modern JavaScript features"
             ],
         "WebAndBrowserBasics": [
             "What is hosting?",
             "How DNS works",
             "How browsers work (Reflow, Repaint, Critical Rendering Path)",
             "Web security fundamentals (CORS, HTTPS, OWASP security risks)"
         ]
 },
     "DevelopmentTools": {
         "VersionControlAndCollaboration": [
             "Git basics (branches, merges, conflict resolution)",
             "VCS hosting platforms (GitHub, GitLab, Bitbucket)"
         ],
         "PackageManagers": [
             "npm",
             "pnpm",
             "yarn"
         ],
         "BuildTools": [
             "Module bundlers (Webpack, Parcel, Vite)",
             "Build optimization tools (SWC, esbuild)"
         ],
         "Testing": [
             "Unit testing (Jest, Vitest)",
             "End-to-end testing (Cypress, Playwright)"
         ]
 },
     "FrontendArchitectureAndFrameworks": {
         "CSSArchitecture": [
             "BEM methodology",
             "CSS-in-JS (Styled Components, Emotion)",
             "Utility-first frameworks (Tailwind CSS)"
         ],
         "JavaScriptFrameworksAndLibraries": [
             "React",
             "Vue.js",
             "Angular",
             "Svelte"
         ],
         "ServerSideRenderingAndRouting": [
             "Next.js",
             "Nuxt.js",
             "react-router"
         ],
         "ComponentizationAndVisualization": [
             "Web components (HTML templates, Shadow DOM)",
             "State management (Redux, Zustand, Pinia)",
             "Data visualization tools (D3.js, Chart.js)"
         ]
 },
     "AdvancedTopics": {
         "PerformanceOptimization": [
             "PRPL pattern",
             "RAIL model",
             "Performance metrics (Lighthouse, Web Vitals)"
         ],
         "AuthenticationAndSecurity": [
             "Authentication strategies (JWT, OAuth, SSO)",
             "Secure coding practices (XSS, CSRF protection)"
         ],
         "TypeChecking": [
             "TypeScript fundamentals",
             "Static analysis tools (ESLint, Prettier)"
         ],
         "FullStackAndCrossPlatformExpansion": [
             "GraphQL (Apollo, Relay Modern)",
             "Cross-platform development (React Native, Flutter)",
             "Progressive Web Apps (PWA)"
         ]
     }
 },
    "skills": [
         "HTML/CSS/JavaScript basics",
         "DOM manipulation",
         "Responsive design principles",
         "Version control with Git",
         "Package management",
         "Module bundling and build tools",
         "Testing frameworks",
         "CSS-in-JS and utility frameworks",
         "JavaScript frameworks and libraries (React, Vue, Angular)",
         "Server-side rendering (SSR)",
         "State management",
         "Data visualization",
         "Performance optimization",
         "Authentication and security best practices",
         "TypeScript and type checking",
         "Cross-platform development",
         "GraphQL basics",
         "Progressive Web App (PWA) development" 
    ],
    "tools": [
         "Git",
         "GitHub",
         "GitLab",
         "npm",
         "pnpm",
         "yarn",
         "Webpack",
         "Parcel",
         "Vite",
         "SWC",
         "esbuild",
         "Jest",
         "Vitest",
         "Cypress",
         "Playwright",
         "Tailwind CSS",
         "Styled Components",
         "Emotion",
         "React",
         "Vue.js",
         "Angular",
         "Svelte",
         "Next.js",
         "Nuxt.js",
         "Redux",
         "Zustand",
         "Pinia",
         "D3.js",
         "Chart.js",
         "Lighthouse",
         "Prettier",
         "ESLint",
         "React Native",
         "Flutter",
         "Apollo",
         "Relay Modern"
    ]
  }

# Inserting data into MongoDB
collection.insert_one(data)