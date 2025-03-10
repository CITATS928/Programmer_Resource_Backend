from pymongo import MongoClient
import json

# MongoDB connection setup
CONNECTION_STRING = "mongodb+srv://root:root@programmerresource.dbqww.mongodb.net/"
client = MongoClient(CONNECTION_STRING)
db = client["Programmer_Resource"]
collection = db["Role"]

data = {
    "roles": [
        {
            "id": 1,
            "name": "Frontend Engineer",
            "description": "A Frontend Engineer is responsible for developing the visual and interactive aspects of web applications and websites. They work closely with designers, backend developers, and other team members to create user-friendly interfaces that provide a seamless user experience. They ensure the design is implemented accurately, and the application is responsive, accessible, and performs well across various devices and browsers.",
            "responsibilities": [ 
                "Develop and maintain the user-facing components of web applications using HTML, CSS, and JavaScript.",
                "Collaborate with UI/UX designers to implement visually appealing and functional designs.",
                "Optimize web applications for maximum speed and scalability.",
                "Ensure cross-browser and cross-platform compatibility.",
                "Integrate APIs and backend services into the frontend.",
                "Write clean, maintainable, and well-documented code.",
                "Debug and fix issues in a timely manner.",
                "Stay up-to-date with emerging frontend technologies and frameworks.",
                "Participate in code reviews and contribute to team discussions on best practices.",
                "Implement accessibility features to comply with web accessibility standards."
            ],
            "category": "Frontend",
            "salary_range": {
                "entry_level": "$65,000 - $85,000",
                "mid_level": "$85,000 - $110,000",
                "senior_level": "$110,000 - $150,000"
            },
            "Learning_difficulty": 4,
            "Salary_level": 4,
            "Market_demand": 4,
            "Job_stability": 4,
            "Career_Prospects": 5
        },
        {
            "id": 2,
            "name": "Backend Engineer",
            "description": "A Backend Engineer is responsible for building and maintaining the server-side logic and infrastructure of web applications. They focus on creating and managing the components that process data, handle business logic, and interact with databases and external APIs. Backend Engineers ensure that the system is robust, secure, and scalable to support the application's frontend and user needs.",
            "responsibilities": [
                "Design, develop, and maintain server-side logic and APIs.",
                "Build and manage databases, ensuring data integrity and optimization.",
                "Collaborate with frontend developers to integrate user-facing elements with server-side logic.",
                "Write reusable, testable, and efficient code.",
                "Ensure application performance, scalability, and security.",
                "Implement authentication and authorization mechanisms.",
                "Troubleshoot and debug backend issues in a timely manner.",
                "Monitor and maintain server environments and deployment processes.",
                "Stay updated on backend technologies, frameworks, and best practices.",
                "Participate in system architecture discussions and contribute to the overall application design."
            ],
            "category": "Backend",
            "salary_range": {
                "entry_level": "$70,000 - $90,000",
                "mid_level": "$90,000 - $120,000",
                "senior_level": "$120,000 - $160,000"
            },
            "Learning_difficulty": 4,
            "Salary_level": 4,
            "Market_demand": 4,
            "Job_stability": 4,
            "Career_Prospects": 5
        },
        {
            "id": 3,
            "name": "DevOps Engineer",
            "description": "A DevOps Engineer is responsible for bridging the gap between software development and IT operations. They focus on automating processes, improving system reliability, and enhancing the efficiency of software delivery. DevOps Engineers work with CI/CD pipelines, cloud infrastructure, monitoring, and security to ensure a smooth and scalable deployment process.",
            "responsibilities": [
                "Design, implement, and maintain CI/CD pipelines for automated software deployment.",
                "Manage cloud infrastructure and provisioning using tools like Terraform and AWS.",
                "Monitor system performance, identify bottlenecks, and ensure system reliability.",
                "Automate repetitive tasks using scripting languages such as Bash, Python, or Ansible.",
                "Manage containerized applications using Docker and Kubernetes.",
                "Ensure security best practices for cloud infrastructure and deployments.",
                "Optimize system performance and scalability for high-traffic applications.",
                "Collaborate with development teams to improve code quality and deployment speed.",
                "Implement logging and monitoring tools like Prometheus, Grafana, and ELK Stack.",
                "Respond to system failures and incidents, conducting root cause analysis and remediation."
            ],
            "category": "DevOps",
            "salary_range": {
                "entry_level": "$75,000 - $100,000",
                "mid_level": "$100,000 - $130,000",
                "senior_level": "$130,000 - $180,000"
            },
            "Learning_difficulty": 5,
            "Salary_level": 5,
            "Market_demand": 4,
            "Job_stability": 4,
            "Career_Prospects": 5
        }

    ],
}

# Insert data into MongoDB collection
collection.insert_one(data)