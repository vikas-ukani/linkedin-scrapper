import csv, time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

LINKEDIN_AUTH_URL = 'https://www.linkedin.com/login'
LINKEDIN_SEARCH_URL = "https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22103644278%22%5D&keywords="

# AUTH CREDENTIALS
LINKEDIN_EMAIL = 'LINKEDIN_EMAIL'
LINKEDIN_PASSWORD = 'LINKEDIN_PASSWORD'

# Make sure to update search term in array format. => ["Search anything inside braces."]
SEARCH_TERMS =  ["staffing recruiting", "recruting agencies"]

def create_driver():
    return webdriver.Firefox()

def authenticate(driver):
    print("Authenticating...")
    # Navigate to the LinkedIn login page
    driver.get(LINKEDIN_AUTH_URL)
    time.sleep(2)

    username_field = driver.find_element(By.NAME, 'session_key')
    password_field = driver.find_element(By.NAME,'session_password')

    # Enter the username/email and password
    username_field.send_keys(LINKEDIN_EMAIL)
    password_field.send_keys(LINKEDIN_PASSWORD)

    # Find and click the login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    time.sleep(20)
    

def scrape_linkedin_companies(search_term, driver, writer):
    print("Authentication Success...")
    driver.get(f"{LINKEDIN_SEARCH_URL}{search_term}")

    time.sleep(2)

    # Set Max Iteration here. 
    for i in range(1, 100):
        soup = BeautifulSoup(driver.page_source, "html.parser")
        company_list = soup.find("ul", {"class": "reusable-search__entity-result-list"})
        if company_list:
            for company in company_list.find_all("li"):
                conpany_link = company.find("a", {"class": "app-aware-link"}).get("href")
                conpany_name = company.find("span", {"class": "entity-result__title-text"}).find('a').text.strip().replace('"', "").replace("'", "").replace('"', "")

                print(f"page: {i}. Company Name: {conpany_name}")
                # Saving Company lists to csv file. file name: "company-lists.csv"
                writer.writerow([conpany_name, conpany_link])
            
            # Scroll to bottom at footer.
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

            # Go to Next Page.
            nextLink = driver.find_element(By.XPATH, '//button[normalize-space()="Next"]')
            if nextLink.is_enabled() is True:
                nextLink.click()
                time.sleep(2)
            else:
                print("No more pages to scrape.")
                break


# Application Initialization.
if __name__ == "__main__":
    driver = create_driver()

    # Authenticate to LinkedIn.
    authenticate(driver)

    # Creating Writer to save scrapped results to file
    file = open('company-lists.csv', "w", newline='')
    writer = csv.writer(file)
    writer.writerow(['Company Name', 'Company Link'])


    # Search Term
    
    for search_term in SEARCH_TERMS:
        scrape_linkedin_companies(search_term, driver=driver, writer=writer)

    # Close File at the end.
    file.close()

    print(f"Companies has been exported.")
    driver.quit()