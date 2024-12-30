from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json


def scrape_project():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    

    try:

        projects = []
        # max_projects = 10
        url = "https://www.frontendpractice.com/projects"

        driver.get(url)
        time.sleep(5)

        # while len(projects) < projects:
        project_elements = driver.find_elements(By.CSS_SELECTOR, ".ProjectCardstyled__CardCopy-sc-dqey3j-1 a")

        for project in project_elements:
            try:
                name = project.find_element(By.CSS_SELECTOR, "p.cardTitle").text.strip()
                link = project.get_attribute("href")

                projects.append({
                    "name": name,
                    "link": link
                })
            except Exception as e:
                print(f"Error extracting project: {e}")
        
        return {
            "topic": "Frontend",
            "books": projects
        }
    finally:
        driver.quit()




def save_courses(data, filename='frontend_projects.json'):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Courses saved to {filename}")
    

if __name__ == '__main__':
    projects = scrape_project()
    if projects:
        save_courses(projects)