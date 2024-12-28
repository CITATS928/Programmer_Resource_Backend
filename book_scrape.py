from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json


def scrape_book():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    books = []
    max_books = 10
    url = "https://www.goodreads.com/search?page=1&q=frontend&qid=ZLdchY1S03&search_type=books&tab=books&utf8=%E2%9C%93"

    driver.get(url)
    time.sleep(5)

    while len(books) < max_books:
        pass




def save_courses(data, filename='frontend_books.json'):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Courses saved to {filename}")
    

if __name__ == '__main__':
    books = scrape_book()
    if books:
        save_courses(books)