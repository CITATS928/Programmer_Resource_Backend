from pymongo import MongoClient


# MongoDB connection setup
CONNECTION_STRING = "mongodb+srv://root:root@programmerresource.dbqww.mongodb.net/"
client = MongoClient(CONNECTION_STRING)
db = client["Programmer_Resource"]
collection = db["Tools"]

data = {
    "id": 1,
    "role": "Frontend Engineer",
    "tools": [
      {
        "name": "Chrome DevTools",
        "description": "Chrome DevTools is a set of web developer tools built directly into the Google Chrome browser. It provides powerful debugging, network inspection, and performance profiling features.",
        "link": "https://developer.chrome.com/docs/devtools/",
        "category": "Browser Developer Tools",
        "use_case": "Debugging, network analysis, and performance profiling."
      },
      {
        "name": "Bootstrap",
        "description": "Bootstrap is a free and open-source CSS framework for responsive and mobile-first web development. It provides pre-styled components and utilities for building modern websites quickly.",
        "link": "https://getbootstrap.com/",
        "category": "CSS Framework",
        "use_case": "Building responsive websites with reusable components."
      },
      {
        "name": "jQuery",
        "description": "jQuery is a fast, small, and feature-rich JavaScript library. It simplifies HTML DOM traversal, event handling, and AJAX interactions for rapid web development.",
        "link": "https://jquery.com/",
        "category": "JavaScript Library",
        "use_case": "DOM manipulation and AJAX handling."
      },
      {
        "name": "CodePen",
        "description": "CodePen is an online code editor and community for testing and showcasing user-created HTML, CSS, and JavaScript code snippets.",
        "link": "https://codepen.io/",
        "category": "Online Code Editor",
        "use_case": "Quickly prototyping and sharing frontend ideas."
      },
      {
        "name": "Google Fonts",
        "description": "Google Fonts is a library of free and open-source fonts that you can integrate into web projects to enhance typography.",
        "link": "https://fonts.google.com/",
        "category": "Typography Tool",
        "use_case": "Integrating free fonts for improved web typography."
      },
      {
        "name": "Grunt",
        "description": "Grunt is a JavaScript task runner that helps automate repetitive tasks like minification, compilation, and testing.",
        "link": "https://gruntjs.com/",
        "category": "Task Runner",
        "use_case": "Automating build tasks for web projects."
      },
      {
        "name": "Next.js",
        "description": "Next.js is a React framework for server-side rendering and building static web applications. It provides features like API routes, file-based routing, and serverless deployment.",
        "link": "https://nextjs.org/",
        "category": "React Framework",
        "use_case": "Building SEO-friendly and performant React applications."
      },
      {
        "name": "TypeScript",
        "description": "TypeScript is a superset of JavaScript that adds static typing and enhanced developer tooling. It improves code maintainability and reduces bugs.",
        "link": "https://www.typescriptlang.org/",
        "category": "Programming Language",
        "use_case": "Writing scalable and maintainable JavaScript code."
      },
      {
        "name": "Sass",
        "description": "Sass is a CSS preprocessor that adds features like variables, nested rules, and mixins to regular CSS, making stylesheets more maintainable.",
        "link": "https://sass-lang.com/",
        "category": "CSS Preprocessor",
        "use_case": "Writing reusable and organized CSS."
      },
      {
        "name": "Vue.js",
        "description": "Vue.js is a progressive JavaScript framework for building user interfaces. It's lightweight and suitable for integrating into projects incrementally.",
        "link": "https://vuejs.org/",
        "category": "JavaScript Framework",
        "use_case": "Building lightweight, flexible frontend applications."
      },
      {
        "name": "Visual Studio Code",
        "description": "Visual Studio Code is a powerful, open-source code editor with built-in support for debugging, version control, and extensions.",
        "link": "https://code.visualstudio.com/",
        "category": "Code Editor",
        "use_case": "Developing, debugging, and managing code efficiently."
      },
      {
        "name": "Npm",
        "description": "Npm is a package manager for JavaScript. It helps developers install, share, and manage dependencies in their projects.",
        "link": "https://www.npmjs.com/",
        "category": "Package Manager",
        "use_case": "Managing project dependencies."
      },
      {
        "name": "Figma",
        "description": "Figma is a web-based UI/UX design tool that enables teams to collaborate in real-time on design projects.",
        "link": "https://www.figma.com/",
        "category": "Design Tool",
        "use_case": "Collaborative UI/UX design."
      },
      {
        "name": "Lighthouse",
        "description": "Lighthouse is an open-source, automated tool for improving the performance, quality, and correctness of web applications.",
        "link": "https://developer.chrome.com/docs/lighthouse/",
        "category": "Performance Analysis Tool",
        "use_case": "Auditing and optimizing web performance."
      }
    ]
  }
  
collection.insert_one(data)