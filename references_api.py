import requests
import json

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
    pass


def scrape_projects():
    pass


def save_to_file(data, filename="frontend_courses.json"):
    """
    
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Data saved to {filename}")

if __name__ == '__main__':
    # Fetch data
    courses = fetch_udemy_courses()
    books = scrape_books()
    projects = scrape_projects()

    # Combind data
    combined_data = {
        "id": 1,
        "name": "Frontend Engineer",
        "courses": courses,
        "books": books,
        "projects": projects
    }

    # Save data to file
    save_to_file(combined_data)