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

    title = soup.find('h1').text.strip()
    roadmap_steps = [item.text.strip() for item in soup.select("ul li")]

    return {
        'title': title,
        'steps': roadmap_steps
    }


def save_roadmap(data, filename='roadmap.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f'Roadmap saved to {filename}')


if __name__ == '__main__':
    roadmap = get_roadmap()
    if roadmap:
        save_roadmap(roadmap)