from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

def scrape_crouses(base_url, max = 40):
    pass

def save_courses(data, filename='frontend_courses.json'):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Courses saved to {filename}")
    pass

if __name__ == '__main__':
    courses = scrape_crouses()
    if courses:
        save_courses(courses)