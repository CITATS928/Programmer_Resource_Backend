from pymongo import MongoClient
import json

# MongoDB connection setup
CONNECTION_STRING = "mongodb+srv://root:root@programmerresource.dbqww.mongodb.net/"
client = MongoClient(CONNECTION_STRING)
db = client["Programmer_Resource"]
collection = db["Roadmap"]

data = {
    "roles": [
        {
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
        },
        {
            "id": 2,
            "name": "Backend Engineer",
            "learning_path": {
                "CoreFundamentals": {
                    "ProgrammingLanguages": [
                        "Learn a backend language (Python, Java, JavaScript, Go, Ruby, etc.)",
                        "Understand syntax, data types, and control structures",
                        "Learn OOP (Object-Oriented Programming) and Functional Programming principles",
                        "Understand error handling and debugging techniques"
                    ],
                    "Databases": [
                        "SQL fundamentals (MySQL, PostgreSQL, SQL Server)",
                        "NoSQL databases (MongoDB, Redis, Cassandra)",
                        "Database design and normalization",
                        "Indexing, query optimization, and transactions"
                    ],
                    "WebAndNetworkingBasics": [
                        "Understand how the internet works (HTTP, HTTPS, FTP, DNS, etc.)",
                        "Learn about RESTful APIs and GraphQL",
                        "Understand authentication (OAuth, JWT, API keys)",
                        "Learn about session management and cookies"
                    ]
                },
                "DevelopmentTools": {
                    "VersionControlAndCollaboration": [
                        "Git basics (branches, merges, conflict resolution)",
                        "Git workflows (GitHub flow, GitFlow, trunk-based development)",
                        "VCS hosting platforms (GitHub, GitLab, Bitbucket)"
                    ],
                    "PackageManagers": [
                        "pip (Python)",
                        "npm (JavaScript)",
                        "Maven (Java)",
                        "Gradle (Java)"
                    ],
                    "BuildTools": [
                        "Containerization with Docker",
                        "CI/CD tools (Jenkins, GitHub Actions, GitLab CI/CD)"
                    ],
                    "Testing": [
                        "Unit testing (pytest, JUnit, Mocha)",
                        "Integration testing (Postman, Jest, Newman)"
                    ]
                },
                "BackendArchitectureAndFrameworks": {
                    "BackendFrameworks": [
                        "Django",
                        "Flask",
                        "Spring Boot",
                        "Express.js",
                        "NestJS",
                        "FastAPI",
                        "Ruby on Rails"
                    ],
                    "APIDevelopment": [
                        "REST API design best practices",
                        "GraphQL implementation",
                        "gRPC and protocol buffers"
                    ],
                    "CachingAndPerformance": [
                        "Server-side caching (Redis, Memcached)",
                        "CDN integration (Cloudflare, Akamai)"
                    ],
                    "MessageQueuesAndEventDrivenArchitecture": [
                        "Kafka",
                        "RabbitMQ",
                        "AWS SQS"
                    ]
                }
            },
            "skills": [
                "Proficiency in backend programming languages (Python, Java, JavaScript, Go, Ruby, etc.)",
                "Understanding of RESTful APIs and GraphQL",
                "Database management (SQL and NoSQL)",
                "Authentication and authorization (OAuth, JWT)",
                "Performance optimization and caching",
                "Version control with Git",
                "Containerization (Docker, Kubernetes)",
                "Building and maintaining CI/CD pipelines",
                "Monitoring and logging systems",
                "Cloud computing (AWS, Azure, Google Cloud)"
            ],
            "tools": [
                "Git",
                "GitHub",
                "GitLab",
                "Docker",
                "Kubernetes",
                "Jenkins",
                "Terraform",
                "Postman",
                "MySQL",
                "PostgreSQL",
                "MongoDB",
                "Redis",
                "Elasticsearch",
                "Kafka",
                "RabbitMQ",
                "Spring Boot",
                "Django",
                "Flask",
                "Express.js",
                "FastAPI",
                "GraphQL",
                "AWS Lambda",
                "Google Cloud Functions",
                "Azure Functions",
                "Prometheus",
                "ELK Stack",
                "Datadog"
            ]
        },
    {
    "id": 3,
    "name": "DevOps Engineer",
    "learning_path": {
        "CoreFundamentals": {
            "OperatingSystems": [
                "Learn Linux fundamentals (Ubuntu, CentOS, Alpine, etc.)",
                "Understand shell scripting (Bash, Zsh, PowerShell)",
                "Process management, permissions, and system monitoring",
                "Networking basics (TCP/IP, DNS, HTTP, HTTPS, FTP)"
            ],
            "VersionControlAndCollaboration": [
                "Git fundamentals (branches, merges, rebases, conflict resolution)",
                "Git workflows (GitHub Flow, GitFlow, trunk-based development)",
                "VCS hosting platforms (GitHub, GitLab, Bitbucket)"
            ],
            "NetworkingAndSecurity": [
                "Networking protocols (TCP/IP, SSH, VPN, DNS, Load Balancing)",
                "Firewalls, proxies, and reverse proxies (Nginx, HAProxy)",
                "Security principles (IAM, TLS/SSL, SSH hardening, OWASP Top 10)"
            ],
            "InfrastructureAsCode": [
                "Infrastructure provisioning tools (Terraform, AWS CloudFormation)",
                "Configuration management (Ansible, Chef, Puppet, SaltStack)",
                "Server automation and infrastructure templating"
            ]
        },
        "DevelopmentTools": {
            "CI/CD": [
                "Continuous Integration concepts (Jenkins, GitHub Actions, GitLab CI/CD, CircleCI)",
                "Continuous Deployment and Continuous Delivery (Canary, Blue-Green, Rolling Updates)",
                "Automating software builds and releases"
            ],
            "ContainerizationAndOrchestration": [
                "Docker fundamentals (image creation, networking, multi-stage builds)",
                "Container orchestration (Kubernetes, Docker Swarm, Amazon ECS)",
                "Service mesh technologies (Istio, Linkerd)"
            ],
            "MonitoringAndLogging": [
                "System monitoring (Prometheus, Grafana, Nagios, Datadog)",
                "Centralized logging (ELK Stack - Elasticsearch, Logstash, Kibana)",
                "Application performance monitoring (New Relic, OpenTelemetry)"
            ],
            "CloudAndServerless": [
                "Cloud computing platforms (AWS, Azure, Google Cloud)",
                "Serverless computing (AWS Lambda, Azure Functions, Google Cloud Functions)",
                "Hybrid and multi-cloud strategies"
            ]
        },
        "AdvancedTopics": {
            "SiteReliabilityEngineering": [
                "SLI/SLO/SLA principles",
                "Chaos engineering (Gremlin, Netflix Chaos Monkey)",
                "Incident response and post-mortem analysis"
            ],
            "SecurityAndCompliance": [
                "Secrets management (Vault, AWS Secrets Manager, Doppler)",
                "Policy as code (OPA, AWS SCPs)",
                "Compliance frameworks (ISO 27001, SOC 2, GDPR, HIPAA)"
            ],
            "NetworkingOptimization": [
                "Load balancing (HAProxy, Nginx, AWS ALB)",
                "Content Delivery Networks (Cloudflare, Fastly, Akamai)",
                "Optimizing latency and bandwidth usage"
            ],
            "CostOptimizationAndFinOps": [
                "Cloud cost management (AWS Cost Explorer, Google Cloud Billing, Azure Cost Management)",
                "Autoscaling and resource efficiency strategies",
                "Spot instances, reserved instances, and savings plans"
            ]
        }
    },
    "skills": [
        "Proficiency in Linux system administration",
        "Understanding of networking (TCP/IP, DNS, Load Balancing, Firewalls)",
        "Version control with Git",
        "Experience with Infrastructure as Code (Terraform, Ansible, CloudFormation)",
        "CI/CD pipeline automation (Jenkins, GitHub Actions, GitLab CI/CD)",
        "Containerization and orchestration (Docker, Kubernetes, Helm)",
        "Cloud computing platforms (AWS, Azure, GCP)",
        "Monitoring and logging tools (Prometheus, Grafana, ELK Stack)",
        "Security best practices (IAM, VPNs, Secrets Management, OWASP)",
        "Incident response and disaster recovery planning",
        "Cost optimization and resource efficiency in cloud computing"
    ],
    "tools": [
        "Linux",
        "Git",
        "GitHub",
        "GitLab",
        "Bitbucket",
        "Docker",
        "Kubernetes",
        "Helm",
        "Terraform",
        "Ansible",
        "Jenkins",
        "GitHub Actions",
        "GitLab CI/CD",
        "CircleCI",
        "Prometheus",
        "Grafana",
        "ELK Stack (Elasticsearch, Logstash, Kibana)",
        "Cloudflare",
        "AWS",
        "Google Cloud",
        "Azure",
        "AWS Lambda",
        "Google Cloud Functions",
        "Azure Functions",
        "CloudFormation",
        "Vault",
        "HAProxy",
        "NGINX",
        "Fastly",
        "Akamai"
    ]
}

    ]
}


old_data2 = {
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