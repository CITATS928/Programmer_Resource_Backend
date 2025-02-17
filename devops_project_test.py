import re
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def scrape_devops_projects():
    """
    Scrape DevOps projects from GeeksForGeeks, limiting to 10 valid projects.
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
        url = "https://www.geeksforgeeks.org/devops-projects/"

        driver.get(url)
        time.sleep(5)

        project_elements = driver.find_elements(By.TAG_NAME, "h3")

        for project_element in project_elements:
            if len(projects) >= 10:
                break

            try:
                raw_name = project_element.text.strip()

                # remove "number. " at the beginning
                name = re.sub(r"^\d+\.\s*", "", raw_name) 

                link = "No link found"

                # get the link for the project
                try:
                    link_element = project_element.find_element(By.XPATH, "./following::blockquote[1]//a")
                    link = link_element.get_attribute("href").strip()
                except Exception:
                    pass

                if name and link != "No link found":
                    projects.append({
                        "name": name,
                        "link": link
                    })

            except Exception as e:
                print(f"Error extracting project: {e}")

        return projects[:10]
    finally:
        driver.quit()


def save_to_file(data, filename="devops_projects.json"):
    """
    Save data to JSON file
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Data saved to {filename}")


if __name__ == '__main__':
    project_data = scrape_devops_projects()
    if project_data:
        save_to_file(project_data)
    else:
        print("No projects found.")
