from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

def scrape_crouses():
    """
    This function is used to scrape the courses from udemy, including the course name, description and link.
    """

    # Chrome options， pretend to be a real user
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)


    
    try:
        courses = []
        max_courses = 5
        url = "https://www.udemy.com/courses/search/?lang=en&p=1&q=frontend&ratings=4.5&sort=relevance&src=sac"

        driver.get(url)
        time.sleep(5)

        while len(courses) < max_courses:
            # wait for the page to load
            try:
                WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-purpose='course-title-url']")))
            except Exception as e:
                print("Error: TimeoutException occurred.")
                raise e

            # search and save course data
            course_elements = driver.find_elements(By.CSS_SELECTOR, "[data-purpose='course-title-url']")
            for course in course_elements:
                try:
                    name = course.text.strip().split('\n')[0]
                    description = course.text.strip().split('\n')[1]
                    link = course.find_element(By.TAG_NAME, "a").get_attribute("href")
                    courses.append({
                        "name": name, 
                        "description": description,
                        "link": link}
                        )
                except Exception as e:
                    print(f"Error extracting course: {e}")

            # check reach max
            if len(courses) >= max_courses:
                break

            # next page
            try:
                next_button = driver.find_element(By.CSS_SELECTOR, ".pagination--next--5n7Tn")
                if "disabled" in next_button.get_attribute("class"):
                    break  # this is the last page
                next_button.click()
                time.sleep(5)
            except Exception as e:
                print(f"Error clicking next: {e}")
                break

        return {
            "id": 1,
            "name": "Frontend Engineer",
            "courses": courses[:max_courses]
        }
    
    finally:
        driver.quit()


def save_courses(data, filename='frontend_courses.json'):
    """
    This function is used to save the courses to a json file
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Courses saved to {filename}")
    pass

if __name__ == '__main__':
    courses = scrape_crouses()
    if courses:
        save_courses(courses)