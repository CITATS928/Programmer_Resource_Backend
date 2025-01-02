import requests
import json

def fetch_udemy_courses():
    """
    Fetch courses from Udemy API and return them in the desired format.
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
        
        return {
            "id": 1,
            "name": "Frontend Engineer",
            "courses": courses
        }
    
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch courses: {e}")
        return {
            "id": 1,
            "name": "Frontend Engineer",
            "courses": []
        }

def save_courses_to_file(data, filename="courses.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Courses saved to {filename}")

if __name__ == '__main__':
    formatted_data = fetch_udemy_courses()
    
    print(json.dumps(formatted_data, ensure_ascii=False, indent=4))
    save_courses_to_file(formatted_data)
