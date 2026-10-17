import argparse
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def get_driver(browser_type):
    browser = browser_type.lower()
    if browser == "edge":
        print("Using Microsoft Edge...")
        options = EdgeOptions()
        return webdriver.Edge(options=options)
    elif browser == "chrome":
        print("Using Chrome Browser...")
        options = ChromeOptions()
        return webdriver.Chrome(options=options)
    else:
        print("Using Brave Browser...")
        options = ChromeOptions()
        options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        return webdriver.Chrome(options=options)

def scrape_courses(search_topic, browser_type):
    driver = get_driver(browser_type)
    
    formatted_topic = search_topic.strip().lower().replace(" ", "-")
    url = f"https://www.mygreatlearning.com/{formatted_topic}/free-courses"
    
    driver.get(url)
    time.sleep(3)
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    
    courses_data = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        title = a_tag.get_text(strip=True)
        
        if ('/academy/learn-for-free/courses/' in href or '/courses/' in href) and len(title) > 3:
            full_url = f"https://www.mygreatlearning.com{href}" if href.startswith('/') else href
            
            if search_topic.lower() in title.lower():
                course_entry = f"{title}\n{full_url}"
                if course_entry not in courses_data:
                    courses_data.append(course_entry)

    if courses_data:
        file_name = f"courses_{formatted_topic}.txt"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(f"Filtered courses for '{search_topic}':\n\n")
            for i, course in enumerate(courses_data, start=1):
                file.write(f"{i}. {course}\n\n")
        print(f"Saved {len(courses_data)} courses to '{file_name}'.")
    else:
        print("No courses found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CourseFinder-CLI: Search and filter free courses easily.")
    parser.add_argument("-t", "--topic", required=True, help="Search topic (e.g., sql, python, excel)")
    parser.add_argument("-b", "--browser", default="brave", choices=["brave", "edge", "chrome"], help="Browser to use: brave, edge, or chrome")
    
    args = parser.parse_args()
    scrape_courses(args.topic, args.browser)