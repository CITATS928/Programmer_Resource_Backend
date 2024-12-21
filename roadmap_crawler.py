# use for dynamic web pages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# use for static web pages
import requests
from bs4 import BeautifulSoup
import json


def get_roadmap():
    url = 'https://roadmap.sh/frontend'

    response = requests.get(url)
    if response.status_code != 200:
        print('Failed to fetch the page: {response.status_code}')
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # get title base on h1 tag
    title = soup.find('h1').text.strip()

    # get value of 'data-title'
    data_titles = [item['data-title'] for item in soup.find_all(attrs={"data-title": True})]

    return {
        'title': title,
        'steps': data_titles
    }


def get_roadmap_with_selenium():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        url = 'https://roadmap.sh/frontend'
        driver.get(url)

        # loading
        time.sleep(5)

        title = driver.find_element(By.TAG_NAME, 'h1').text.strip()

        # find all the elements that include 'data-title', then get the value of 'data-title'
        element = driver.find_elements(By.XPATH, '//*[@data-title and @data-parent-title]')
        # data_titles = [item.get_attribute('data-title') for item in element]

        roadmap_data = {}
        for item in element:
            parent_title = item.get_attribute('data-parent-title')
            data_title = item.get_attribute('data-title')

            # sort the data based on parent_title
            if parent_title not in roadmap_data:
                roadmap_data[parent_title] = []
            roadmap_data[parent_title].append(data_title)


        return {
            'title': title,
            'steps': roadmap_data
        }
    finally:
        driver.quit()


def save_roadmap(data, filename='roadmap.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f'Roadmap saved to {filename}')


if __name__ == '__main__':
    # roadmap = get_roadmap()
    roadmap = get_roadmap_with_selenium()
    if roadmap:
        save_roadmap(roadmap)