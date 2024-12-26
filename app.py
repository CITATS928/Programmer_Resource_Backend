from flask import Flask, jsonify, request

roles_data = [
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
        "Implement accessibility features to comply with web accessibility standards."],
    "category": "Frontend",
    "salary_range": {
    	"entry_level": "$65,000 - $85,000",
    	"mid_level": "$85,000 - $110,000",
    	"senior_level": "$110,000 - $150,000"
    }
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
        "Participate in system architecture discussions and contribute to the overall application design."],
    "category": "Backend",
    "salary_range": {
    	"entry_level": "$70,000 - $90,000",
    	"mid_level": "$90,000 - $120,000",
    	"senior_level": "$120,000 - $160,000"
}
     }
]

learning_path = [
    {
       "id": 1,
       "name": "Frontend Engineer",
       "learning_path": [
         "Learn the basics of web development: HTML, CSS, and JavaScript.",
         "Understand responsive design and CSS frameworks (e.g., Bootstrap, Tailwind CSS).",
         "Learn JavaScript frameworks/libraries (e.g., React, Angular, Vue.js).",
         "Gain knowledge of version control systems (e.g., Git).",
         "Understand RESTful APIs and how to integrate them into web applications.",
         "Learn about state management libraries (e.g., Redux, Vuex).",
         "Study web performance optimization techniques.",
         "Familiarize with accessibility standards (e.g., WCAG).",
         "Learn testing frameworks for frontend (e.g., Jest, Cypress).",
         "Stay updated on modern web development trends and tools."
       ],
       "skills": [
         "Proficiency in HTML, CSS, and JavaScript.",
         "Knowledge of frontend frameworks (React, Angular, Vue.js).",
         "Understanding of web accessibility and responsive design principles.",
         "Basic knowledge of backend communication (e.g., REST APIs, GraphQL).",
         "Strong debugging and troubleshooting skills.",
         "Familiarity with browser developer tools.",
         "Ability to write clean, maintainable code."
       ],
       "tools": [
         "Frontend frameworks/libraries: React, Angular, Vue.js",
         "CSS preprocessors: SASS, LESS",
         "Version control: Git, GitHub/GitLab/Bitbucket",
         "Build tools: Webpack, Vite, Parcel",
         "Testing tools: Jest, Mocha, Cypress",
         "Design tools: Figma, Adobe XD, Sketch",
         "Browser developer tools (e.g., Chrome DevTools)"
       ]
     },
   {
       "id": 2, 
       "name": "Backend Engineer",
       "learning_path": [
         "Learn the basics of programming (e.g., Python, Java, JavaScript, Ruby, etc.).",
         "Understand how web servers and HTTP protocols work.",
         "Study server-side programming frameworks (e.g., Node.js, Django, Flask, Spring Boot).",
         "Learn database management and query languages (e.g., SQL, MongoDB).",
         "Understand RESTful API design and implementation.",
         "Familiarize with authentication and authorization techniques (e.g., OAuth, JWT).",
         "Learn about containerization and deployment (e.g., Docker, Kubernetes).",
         "Study cloud services (e.g., AWS, Azure, Google Cloud).",
         "Learn version control (e.g., Git) and CI/CD pipelines.",
         "Understand software architecture and design patterns."
       ],
       "skills": [
         "Proficiency in a backend programming language (e.g., Python, Java, Node.js).",
         "Strong understanding of databases and SQL/NoSQL.",
         "Experience with server-side frameworks (e.g., Express.js, Spring Boot, Flask).",
         "Knowledge of API design and integration.",
         "Familiarity with cloud platforms and deployment processes.",
         "Understanding of version control systems (e.g., Git).",
         "Ability to write clean, scalable, and secure code."
       ],
       "tools": [
         "Programming languages: Python, Java, JavaScript (Node.js), Ruby",
         "Frameworks: Express.js, Django, Flask, Spring Boot",
         "Databases: MySQL, PostgreSQL, MongoDB, Redis",
         "Version control: Git, GitHub/GitLab/Bitbucket",
         "Deployment tools: Docker, Kubernetes",
         "API testing tools: Postman, Swagger",
         "Cloud platforms: AWS, Azure, Google Cloud"
       ]
     }
   ]

reference = [
    {
       "id": 1,
       "name": "Frontend Engineer",
       "courses": [
               "Udemy - The Complete JavaScript Cours",
               "Frontend Masters - Complete Intro to React"
       ],
       "books": [
         "HTML and CSS: Design and Build Websites",
         "JavaScript: The Good Parts"
       ],
       "certifications": [
        "Frontend Development Certification (w3school)",
        "Meta Front-End Developer Professiona (coursera)"
       ],
       "practice_projects": [ 
            "Develop a weather app using a public API.", 
            "Develop a website version dictionary."
       ]
     },
   {
       "id": 2, 
       "name": "Backend Engineer",
       "courses": [
               "Udemy - The Complete Node.js Developer Course",
               "LinkedIn Learning - Learning REST API"
       ],
       "books": [
         "Flask Web Development",
         "REST API Design Rulebook"
       ],
       "certifications": [
         "Meta Back-End Developer Professional Certificate (Coursera)",
         "Back End Development and APIs Certification"
       ],
       "practice_projects": [ 
            "Personal Blogging Platform API", 
            "To-Do List API"
       ]
     }
   ]

job_market =  [
    {
    "id": 1,
    "name": "Frontend Engineer",
      "United States": {
        "San Francisco": {
          "salary": "$140,000 per year",
          "open_positions": 500,
          "websites": ["Indeed", "LinkedIn"]
        },
        "New York": {
          "salary": "$140,000 per year",
          "open_positions": 450,
          "websites": ["Indeed", "LinkedIn"]
        }
      },
      "China": {
        "Beijing": {
          "salary": "¥200,000 per year",
          "open_positions": 300,
          "websites": ["51Job", "Zhaopin"]
        },
        "Shanghai": {
          "salary": "¥180,000 per year",
          "open_positions": 280,
          "websites": ["51Job", "Zhaopin"]
        }
      }
    },
    {
    "id": 2,
    "name": "Backend Engineer",
      "United States": {
        "San Francisco": {
          "salary": "$150,000 per year",
          "open_positions": 480,
          "websites": ["Indeed", "LinkedIn"]
        },
        "New York": {
          "salary": "$130,000 per year",
          "open_positions": 430,
          "websites": ["Indeed", "LinkedIn"]
        }
      },
      "China": {
        "Beijing": {
          "salary": "¥220,000 per year",
          "open_positions": 290,
          "websites": ["51Job", "Zhaopin"]
        },
        "Shanghai": {
          "salary": "¥200,000 per year",
          "open_positions": 270,
          "websites": ["51Job", "Zhaopin"]
        }
      }
    }
]


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask!'

@app.route('/roles')
def get_roles():
    role_name = request.args.get('name') 
    if role_name:
        filter =[role for role in roles_data if role['name'].lower() == role_name.replace('_', ' ').lower()]
        if filter:
            return jsonify(filter[0])
        else:
            return jsonify({"error": "Role not found."}), 404

    return jsonify(roles_data)

@app.route('/learning_path')
def get_learning_path():
    role_name = request.args.get('name') 
    if role_name:
        filter =[role for role in learning_path if role['name'].lower() == role_name.replace('_', ' ').lower()]
        if filter:
            return jsonify(filter[0])
        else:
            return jsonify({"error": "Role not found."}), 404
    return jsonify(learning_path)

@app.route('/reference')
def get_reference():
    role_name = request.args.get('name') 
    if role_name:
        filter =[role for role in reference if role['name'].lower() == role_name.replace('_', ' ').lower()]
        if filter:
            return jsonify(filter[0])
        else:
            return jsonify({"error": "Role not found."}), 404
    return jsonify(reference)

@app.route('/job_market')
def get_job_market():
    role_name = request.args.get('name') 
    if role_name:
        filter =[role for role in job_market if role['name'].lower() == role_name.replace('_', ' ').lower()]
        if filter:
            return jsonify(filter[0])
        else:
            return jsonify({"error": "Role not found."}), 404
    return jsonify(job_market)

if __name__ == '__main__':
    # for local development
    app.run(host="0.0.0.0", port=5001, debug=True)

    # for docker
    #app.run(host="0.0.0.0", port=5000, debug=True)