from pymongo import MongoClient


# MongoDB connection setup
CONNECTION_STRING = "mongodb+srv://root:root@programmerresource.dbqww.mongodb.net/"
client = MongoClient(CONNECTION_STRING)
db = client["Programmer_Resource"]
collection = db["Tools"]


# data = {
#     "tools": [
#         {
#             "id": 1,
#             "role": "Frontend Engineer",
#             "tools": [
#                 {
#                     "name": "Chrome DevTools",
#                     "description": "Chrome DevTools is a set of web developer tools built directly into the Google Chrome browser. It provides powerful debugging, network inspection, and performance profiling features.",
#                     "link": "https://developer.chrome.com/docs/devtools/",
#                     "category": "Browser Developer Tools",
#                     "use_case": "Debugging, network analysis, and performance profiling."
#                 },
#                 {
#                     "name": "React",
#                     "description": "React is a popular JavaScript library for building fast and interactive user interfaces. It emphasizes a component-based architecture, enabling developers to create reusable UI components.",
#                     "link": "https://reactjs.org/",
#                     "category": "JavaScript Library",
#                     "use_case": "Building user interfaces and single-page applications (SPAs)."
#                 },
#                 {
#                     "name": "Bootstrap",
#                     "description": "Bootstrap is a free and open-source CSS framework for responsive and mobile-first web development. It provides pre-styled components and utilities for building modern websites quickly.",
#                     "link": "https://getbootstrap.com/",
#                     "category": "CSS Framework",
#                     "use_case": "Building responsive websites with reusable components."
#                 },
#                 {
#                     "name": "TypeScript",
#                     "description": "TypeScript is a superset of JavaScript that adds static typing and enhanced developer tooling. It improves code maintainability and reduces bugs.",
#                     "link": "https://www.typescriptlang.org/",
#                     "category": "Programming Language",
#                     "use_case": "Writing scalable and maintainable JavaScript code."
#                 },
#                 {
#                     "name": "Next.js",
#                     "description": "Next.js is a React framework for server-side rendering and building static web applications. It provides features like API routes, file-based routing, and serverless deployment.",
#                     "link": "https://nextjs.org/",
#                     "category": "React Framework",
#                     "use_case": "Building SEO-friendly and performant React applications."
#                 }
#             ]
#         },
#         {
#             "id": 2,
#             "role": "Backend Engineer",
#             "tools": [
#                 {
#                     "name": "Postman",
#                     "description": "Postman is a popular API testing tool that enables developers to design, test, and document APIs with ease.",
#                     "link": "https://www.postman.com/",
#                     "category": "API Testing",
#                     "use_case": "Testing and documenting REST and GraphQL APIs."
#                 },
#                 {
#                     "name": "MySQL",
#                     "description": "MySQL is a widely-used relational database management system (RDBMS) known for its reliability and scalability.",
#                     "link": "https://www.mysql.com/",
#                     "category": "Database",
#                     "use_case": "Storing and managing relational data efficiently."
#                 },
#                 {
#                     "name": "MongoDB",
#                     "description": "MongoDB is a NoSQL database designed for high performance, scalability, and ease of development.",
#                     "link": "https://www.mongodb.com/",
#                     "category": "NoSQL Database",
#                     "use_case": "Storing and managing unstructured or semi-structured data."
#                 },
#                 {
#                     "name": "Spring Boot",
#                     "description": "Spring Boot is a Java-based framework that simplifies building stand-alone, production-grade backend services.",
#                     "link": "https://spring.io/projects/spring-boot",
#                     "category": "Backend Framework",
#                     "use_case": "Developing scalable and maintainable backend applications in Java."
#                 },
#                 {
#                     "name": "Express.js",
#                     "description": "Express.js is a fast and minimalistic web framework for Node.js, making backend development easier and more flexible.",
#                     "link": "https://expressjs.com/",
#                     "category": "Backend Framework",
#                     "use_case": "Developing backend services and RESTful APIs using Node.js."
#                 },
#                 {
#                     "name": "Kafka",
#                     "description": "Apache Kafka is a distributed event streaming platform used for high-throughput messaging and data streaming applications.",
#                     "link": "https://kafka.apache.org/",
#                     "category": "Message Broker",
#                     "use_case": "Processing real-time event streams."
#                 }
#             ]
#         },
#         {
#             "id": 3,
#             "role": "DevOps Engineer",
#             "tools": [
#                 {
#                     "name": "Docker",
#                     "description": "Docker is a platform that enables developers to build, share, and run containerized applications efficiently.",
#                     "link": "https://www.docker.com/",
#                     "category": "Containerization",
#                     "use_case": "Creating lightweight, portable, and consistent environments for applications."
#                 },
#                 {
#                     "name": "Kubernetes",
#                     "description": "Kubernetes is an open-source container orchestration system for automating application deployment, scaling, and management.",
#                     "link": "https://kubernetes.io/",
#                     "category": "Container Orchestration",
#                     "use_case": "Managing and scaling containerized applications in production."
#                 },
#                 {
#                     "name": "Terraform",
#                     "description": "Terraform is an Infrastructure as Code (IaC) tool for managing cloud infrastructure through declarative configurations.",
#                     "link": "https://www.terraform.io/",
#                     "category": "Infrastructure as Code (IaC)",
#                     "use_case": "Automating and managing infrastructure provisioning."
#                 },
#                 {
#                     "name": "Ansible",
#                     "description": "Ansible is a configuration management tool that automates software provisioning, configuration, and application deployment.",
#                     "link": "https://www.ansible.com/",
#                     "category": "Configuration Management",
#                     "use_case": "Automating repetitive IT tasks and managing system configurations."
#                 },
#                 {
#                     "name": "Jenkins",
#                     "description": "Jenkins is an open-source automation server used for building, testing, and deploying software.",
#                     "link": "https://www.jenkins.io/",
#                     "category": "CI/CD",
#                     "use_case": "Automating software build and deployment pipelines."
#                 },
#                 {
#                     "name": "Grafana",
#                     "description": "Grafana is a popular open-source tool for visualizing and analyzing metrics from multiple sources.",
#                     "link": "https://grafana.com/",
#                     "category": "Monitoring & Visualization",
#                     "use_case": "Creating dashboards to monitor infrastructure and applications."
#                 },
#                 {
#                     "name": "AWS",
#                     "description": "Amazon Web Services (AWS) is a comprehensive cloud computing platform offering storage, compute power, and networking solutions.",
#                     "link": "https://aws.amazon.com/",
#                     "category": "Cloud Provider",
#                     "use_case": "Deploying and managing cloud-based applications and infrastructure."
#                 }
#             ]
#         }
#     ]
# }
data = {
    "tools": [
        {
            "id": 1,
            "role": "Frontend Engineer",
            "tools": [
                {
                    "name": "Chrome DevTools",
                    "description": "Chrome DevTools is a set of web developer tools built directly into the Google Chrome browser. It provides powerful debugging, network inspection, and performance profiling features.",
                    "link": "https://developer.chrome.com/docs/devtools/",
                    "category": "Browser Developer Tools",
                    "use_case": "Debugging, network analysis, and performance profiling.",
                    "tutorial": "https://developer.chrome.com/docs/devtools/"
                },
                {
                    "name": "React",
                    "description": "React is a popular JavaScript library for building fast and interactive user interfaces. It emphasizes a component-based architecture, enabling developers to create reusable UI components.",
                    "link": "https://reactjs.org/",
                    "category": "JavaScript Library",
                    "use_case": "Building user interfaces and single-page applications (SPAs).",
                    "tutorial": "https://react.dev/learn"
                },
                {
                    "name": "Bootstrap",
                    "description": "Bootstrap is a free and open-source CSS framework for responsive and mobile-first web development. It provides pre-styled components and utilities for building modern websites quickly.",
                    "link": "https://getbootstrap.com/",
                    "category": "CSS Framework",
                    "use_case": "Building responsive websites with reusable components.",
                    "tutorial": "https://getbootstrap.com/docs/5.0/getting-started/introduction/"
                },
                {
                    "name": "TypeScript",
                    "description": "TypeScript is a superset of JavaScript that adds static typing and enhanced developer tooling. It improves code maintainability and reduces bugs.",
                    "link": "https://www.typescriptlang.org/",
                    "category": "Programming Language",
                    "use_case": "Writing scalable and maintainable JavaScript code.",
                    "tutorial": "https://www.typescriptlang.org/docs/"
                },
                {
                    "name": "Next.js",
                    "description": "Next.js is a React framework for server-side rendering and building static web applications. It provides features like API routes, file-based routing, and serverless deployment.",
                    "link": "https://nextjs.org/",
                    "category": "React Framework",
                    "use_case": "Building SEO-friendly and performant React applications.",
                    "tutorial": "https://nextjs.org/learn"
                }
            ]
        },
        {
            "id": 2,
            "role": "Backend Engineer",
            "tools": [
                {
                    "name": "Postman",
                    "description": "Postman is a popular API testing tool that enables developers to design, test, and document APIs with ease.",
                    "link": "https://www.postman.com/",
                    "category": "API Testing",
                    "use_case": "Testing and documenting REST and GraphQL APIs.",
                    "tutorial": "https://learning.postman.com/docs/getting-started/introduction/"
                },
                {
                    "name": "MySQL",
                    "description": "MySQL is a widely-used relational database management system (RDBMS) known for its reliability and scalability.",
                    "link": "https://www.mysql.com/",
                    "category": "Database",
                    "use_case": "Storing and managing relational data efficiently.",
                    "tutorial": "https://dev.mysql.com/doc/"
                },
                {
                    "name": "MongoDB",
                    "description": "MongoDB is a NoSQL database designed for high performance, scalability, and ease of development.",
                    "link": "https://www.mongodb.com/",
                    "category": "NoSQL Database",
                    "use_case": "Storing and managing unstructured or semi-structured data.",
                    "tutorial": "https://www.mongodb.com/docs/"
                },
                {
                    "name": "Spring Boot",
                    "description": "Spring Boot is a Java-based framework that simplifies building stand-alone, production-grade backend services.",
                    "link": "https://spring.io/projects/spring-boot",
                    "category": "Backend Framework",
                    "use_case": "Developing scalable and maintainable backend applications in Java.",
                    "tutorial": "https://spring.io/guides/gs/spring-boot/"
                },
                {
                    "name": "Express.js",
                    "description": "Express.js is a fast and minimalistic web framework for Node.js, making backend development easier and more flexible.",
                    "link": "https://expressjs.com/",
                    "category": "Backend Framework",
                    "use_case": "Developing backend services and RESTful APIs using Node.js.",
                    "tutorial": "https://expressjs.com/en/starter/installing.html"
                },
                {
                    "name": "Kafka",
                    "description": "Apache Kafka is a distributed event streaming platform used for high-throughput messaging and data streaming applications.",
                    "link": "https://kafka.apache.org/",
                    "category": "Message Broker",
                    "use_case": "Processing real-time event streams.",
                    "tutorial": "https://kafka.apache.org/documentation/"
                }
            ]
        },
        {
            "id": 3,
            "role": "DevOps Engineer",
            "tools": [
                {
                    "name": "Docker",
                    "description": "Docker is a platform that enables developers to build, share, and run containerized applications efficiently.",
                    "link": "https://www.docker.com/",
                    "category": "Containerization",
                    "use_case": "Creating lightweight, portable, and consistent environments for applications.",
                    "tutorial": "https://docs.docker.com/get-started/"
                },
                {
                    "name": "Kubernetes",
                    "description": "Kubernetes is an open-source container orchestration system for automating application deployment, scaling, and management.",
                    "link": "https://kubernetes.io/",
                    "category": "Container Orchestration",
                    "use_case": "Managing and scaling containerized applications in production.",
                    "tutorial": "https://kubernetes.io/docs/tutorials/"
                },
                {
                    "name": "Terraform",
                    "description": "Terraform is an Infrastructure as Code (IaC) tool for managing cloud infrastructure through declarative configurations.",
                    "link": "https://www.terraform.io/",
                    "category": "Infrastructure as Code (IaC)",
                    "use_case": "Automating and managing infrastructure provisioning.",
                    "tutorial": "https://developer.hashicorp.com/terraform/tutorials"
                },
                {
                    "name": "Ansible",
                    "description": "Ansible is a configuration management tool that automates software provisioning, configuration, and application deployment.",
                    "link": "https://www.ansible.com/",
                    "category": "Configuration Management",
                    "use_case": "Automating repetitive IT tasks and managing system configurations.",
                    "tutorial": "https://docs.ansible.com/ansible/latest/getting_started/index.html"
                },
                {
                    "name": "Jenkins",
                    "description": "Jenkins is an open-source automation server used for building, testing, and deploying software.",
                    "link": "https://www.jenkins.io/",
                    "category": "CI/CD",
                    "use_case": "Automating software build and deployment pipelines.",
                    "tutorial": "https://www.jenkins.io/doc/tutorials/"
                },
                {
                    "name": "Grafana",
                    "description": "Grafana is a popular open-source tool for visualizing and analyzing metrics from multiple sources.",
                    "link": "https://grafana.com/",
                    "category": "Monitoring & Visualization",
                    "use_case": "Creating dashboards to monitor infrastructure and applications.",
                    "tutorial": "https://grafana.com/docs/grafana/latest/getting-started/getting-started/"
                },
                {
                    "name": "AWS",
                    "description": "Amazon Web Services (AWS) is a comprehensive cloud computing platform offering storage, compute power, and networking solutions.",
                    "link": "https://aws.amazon.com/",
                    "category": "Cloud Provider",
                    "use_case": "Deploying and managing cloud-based applications and infrastructure.",
                    "tutorial": "https://aws.amazon.com/getting-started/"
                }
            ]
        }
    ]
}

  
collection.insert_one(data)