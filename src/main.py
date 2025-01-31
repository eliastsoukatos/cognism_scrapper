import time
from scraper_utils import scrape_page  # Import scraping function
from auth_utils import wait_for_manual_login  # Import login function
from navigate import open_new_tab  # Import new tab navigation
from csv_utils import save_to_csv  # Import CSV saving function
from selenium_setup import initialize_driver  # Import Selenium setup
from file_utils import get_url_from_file  # Import URL fetching function

def main():
    """Main process for Cognism scraping."""
    
    # 🔹 Initialize WebDriver
    driver = initialize_driver()

    # 🔹 Open Cognism for manual login
    driver.get("https://app.cognism.com/login")
    wait_for_manual_login(driver)  # Wait for manual login

    # 🔹 Fetch URL from file
    url = get_url_from_file()  # Fetch the URL here

    if not url.startswith("http"):
        print("Error: Invalid URL format in urls.txt. Please enter a valid URL.")
        return

    # 🔹 Open a new tab and navigate to profile URL
    open_new_tab(driver, url)  # Now correctly passing (driver, url)

    # 🔹 Scrape the page
    extracted_data = scrape_page(driver, url)  # Pass driver + URL correctly
    if extracted_data:
        save_to_csv(extracted_data)  # Save data to CSV

    print("Scraping completed.")
    driver.quit()

if __name__ == "__main__":
    main()
