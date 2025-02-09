import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def scrape_backend_projects():
    """
    Scrape backend projects from masteringbackend.com
    """
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        projects = []
        url = "https://projects.masteringbackend.com/projects"

        driver.get(url)
        time.sleep(5)  # 等待动态内容加载

        # 获取所有项目的 img (包含项目名称) 和 a (包含项目链接)
        project_elements = driver.find_elements(By.CSS_SELECTOR, "a[href^='/projects/']")

        for project in project_elements:
            try:
                name_element = project.find_element(By.XPATH, "./preceding-sibling::div//img")
                name = name_element.get_attribute("alt").strip() if name_element else "Unknown Project"

                link = project.get_attribute("href").strip()
                if link and name:
                    projects.append({"name": name, "link": link})
            except Exception as e:
                print(f"Error extracting project: {e}")

        return projects
    finally:
        driver.quit()


def save_to_file(data, filename="backend_projects.json"):
    """
    Save data to JSON file
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Data saved to {filename}")


if __name__ == '__main__':
    project_data = scrape_backend_projects()
    if project_data:
        save_to_file(project_data)
    else:
        print("No projects found.")
