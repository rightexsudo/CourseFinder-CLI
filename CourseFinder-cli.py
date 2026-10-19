import argparse
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from colorama import init, Fore, Style
init(autoreset=True)

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

def scrape_platform(driver, search_topic, platform_name):
    formatted_topic = search_topic.strip().lower().replace(" ", "-")
    
    if platform_name == "edraak":
        url = f"https://www.edraak.org/explore/?query={search_topic}"
    elif platform_name == "m3aarif":
        url = f"https://www.m3aarf.com/?search_for={search_topic}"
    elif platform_name == "greatlearning":
        url = f"https://www.mygreatlearning.com/{formatted_topic}/free-courses"
    else:
        return
    
    print(f"\n[-] Scraping platform: {platform_name.upper()} ...")
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
    
    courses_data = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        title = a_tag.get_text(strip=True)
        
        if len(title) > 3:
            if search_topic.lower() in title.lower():
                if href.startswith('/'):
                    if platform_name == "edraak":
                        full_url = f"https://www.edraak.org{href}"
                    elif platform_name == "m3aarif":
                        full_url = f"https://www.m3aarf.com{href}"
                    else:
                        full_url = f"https://www.mygreatlearning.com{href}"
                else:
                    full_url = href
                
                course_entry = f"{title}\n{full_url}"
                if course_entry not in courses_data:
                    courses_data.append(course_entry)

    if courses_data:
        file_name = f"courses_{platform_name}_{formatted_topic}.txt"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(f"Filtered courses from {platform_name} for '{search_topic}':\n\n")
            for i, course in enumerate(courses_data, start=1):
                file.write(f"{i}. {course}\n\n")
        print(Fore.GREEN + f"[+] Saved {len(courses_data)} courses from {platform_name} to '{file_name}'.")
    else:
        print(Fore.RED + f"[!] No courses found on {platform_name}.")

def scrape_all_platforms(search_topic, browser_type):
    driver = get_driver(browser_type)
    platforms = ["greatlearning", "edraak", "m3aarif"]
    
    try:
        for platform in platforms:
            scrape_platform(driver, search_topic, platform)
    finally:
        driver.quit()
        print(Style.RESET_ALL + "\nThank you for using CourseFinder-CLI! Happy learning")

if __name__ == "__main__":
    detective_banner = Fore.LIGHTBLUE_EX + r"""
       .---.
      /     \
     |_______|
    /         \
   (===========)
     \  o   o /
      |  ___ |       [ CourseFinder-CLI ]
      \  \=/ /
      /`  .  `\     
     / /|   |\ \
    (_/ |   | \_)
    """
    print(detective_banner)

    parser = argparse.ArgumentParser(description="CourseFinder-CLI: Search free courses across multiple platforms.")
    parser.add_argument("-t", "--topic", required=True, help="Search topic (e.g., sql, python, excel)")
    parser.add_argument("-b", "--browser", default="brave", choices=["brave", "edge", "chrome"], help="Browser to use: brave, edge, or chrome")
    
    args = parser.parse_args()
    scrape_all_platforms(args.topic, args.browser)
