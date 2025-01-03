import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fetch_udemy_courses():
    """
    
    """
    url = "https://udemy-api2.p.rapidapi.com/v1/udemy/search"
    querystring = {"text":"frontend"}

    payload = {
        "page": 1,
        "page_size": 5, 
        "sort": "popularity", 
        "locale": "en_US",  
    }
    
    headers = {
        # this is fake key, replace with next line when using
		"x-rapidapi-key": "this is fake key, replace with next line when using",
        # "x-rapidapi-key": "210261bd2amsh9126e118f249d79p1ca575jsn5f5626ea0598",
		"x-rapidapi-host": "udemy-api2.p.rapidapi.com",
		"Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()

        courses = []
        for course in data.get("data", {}).get("courses", []):
            course_info = {
                "name": course.get("title", "N/A"),
                "description": course.get("headline", "N/A").replace("<strong>", "").replace("</strong>", ""),
                "link": f"https://www.udemy.com{course.get('url')}"
            }
            courses.append(course_info)

        return courses
    

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch courses: {e}")
        return []
    

def scrape_books():
    """
    
    """
    options = Options()
    # Add headless mode and other options to compatible with Docker
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
        books = []
        max_books = 10
        url = "https://www.goodreads.com/search?page=1&q=frontend&qid=ZLdchY1S03&search_type=books&tab=books&utf8=%E2%9C%93"

        driver.get(url)
        time.sleep(5)

        while len(books) < max_books:
            # wait for the page to load
            try:
                WebDriverWait(driver, 30).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tableList .bookTitle"))
                )
            except Exception as e:
                print("Error: TimeoutException occurred.")
                raise e
            
            book_elements = driver.find_elements(By.CSS_SELECTOR, ".tableList .bookTitle")
            author_elements = driver.find_elements(By.CSS_SELECTOR, ".tableList .authorName")

            for book, author in zip(book_elements, author_elements):
                try:
                    title = book.text.strip()
                    link = book.get_attribute("href")
                    author = author.text.strip()
                    books.append({
                        "title": title,
                        "author": author,
                        "link": link
                    })
                except Exception as e:
                    print(f"Error extracting book title: {e}")

            # check reach max
            if len(books) >= max_books:
                break

            # next page
            try:
                next_page = driver.find_element(By.CSS_SELECTOR, ".next_page")
                if "disabled" in next_page.get_attribute("class"):
                    break
                next_page.click()
                time.sleep(5)
            except Exception as e:
                print("Error: No more pages.")
                break
        return books
                    
    finally:
        driver.quit()


def scrape_projects():
    """
    
    """
    options = Options()

    # Add headless mode and other options to compatible with Docker
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
        url = "https://www.frontendpractice.com/projects"

        driver.get(url)
        time.sleep(5)

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
        return projects
    finally:
        driver.quit()


def save_to_file(data, filename="frontend_references.json"):
    """
    
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Data saved to {filename}")

if __name__ == '__main__':
    # Fetch data
    # courses = fetch_udemy_courses()
    books = scrape_books()
    projects = scrape_projects()

    # Combind data
    combined_data = {
        "id": 1,
        "name": "Frontend Engineer",
        # "courses": courses,
        "books": books,
        "projects": projects
    }

    # Save data to file
    save_to_file(combined_data)