# Programmer_Resource_Backend

A structured learning platform designed to help aspiring programmers explore career paths, essential tools, and real-world projects across six engineering roles: Frontend Engineer, Backend Engineer, DevOps, Data Engineering, Data analyst, and Data Scientist.

![Tech Stack](https://img.shields.io/badge/Backend-Flask-blue) ![Automation](https://img.shields.io/badge/Automation-GitHub%20Actions-green) ![Database](https://img.shields.io/badge/Database-MongoDB-yellow)  

---

## 🚀 Overview  

**Programmer Resource** is designed to help aspiring software engineers navigate different career paths by providing:  
✅ **Role-Based Learning Paths:** Clear roadmaps for different engineering disciplines.
✅ **Curated Toolkits:** A categorized list of industry-standard tools with descriptions and tutorials.  
✅ **Real-world projects:** A collection of hands-on projects from various sources.
✅ **Automated updates:** Uses GitHub Actions and Selenium to periodically scrape and update content.
✅ **API Endpoints:** Provides access to structured data for further use.

---

## 🔧 Tech Stack  

- **Backend:** Flask, MongoDB, REST API  
- **Automation:** Selenium, GitHub Actions  
- **Infrastructure:** Docker, AWS

---

## 📡 API Endpoints

📌 The following API endpoints provide structured data:

|Method|Endpoint|Description|
|------|--------|-----------|
|GET|/roles|Returns all available programming roles.|
|GET|/roadmap?name=frontend_engineer|Retrieves the roadmap for a specified role.|
|GET|/tools?name=docker|Fetches details about a specific tool.|
|GET|/projects?name=devops|Lists projects related to a specific role.|

---

## 📦 Installation & Usage

### 🔧 Local Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/programmer-resource.git
cd programmer-resource
```

2. Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate   # macOS/Linux
env\Scripts\activate    #Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up MongoDB (Update .env with your MONGO_CONNECTION_STRING).

5. Run the Flask app:

```bash
python app.py
```

---

## Frontend Github link

[Frontend GitHub link](https://github.com/survivzhang/programResource_frontend)

## DevOps Github link

[DevOps GitHub link](https://github.com/zhppian/Programmer_Resource_DevOps)