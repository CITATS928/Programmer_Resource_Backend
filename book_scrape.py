from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
from pymongo import MongoClient


# MongoDB connection setup
CONNECTION_STRING = "mongodb+srv://root:root@programmerresource.dbqww.mongodb.net/"
client = MongoClient(CONNECTION_STRING)
db = client["test"]
collection = db["Reference"]

def scrape_book():
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

        return {
            "id": 1,
            "topic": "Frontend",
            "books": books[:max_books]
        }
        # return books
    finally:
        driver.quit()




def save_courses(data, filename='frontend_books.json'):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Courses saved to {filename}")
    

def save_to_mongodb(data):
    collection.insert_one(data)

if __name__ == '__main__':
    books = scrape_book()
    if books:
        save_to_mongodb(books)