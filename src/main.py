import time
from utils.scraper import scrape_page  # Import scraping function
from utils.auth import wait_for_manual_login  # Import login function
from utils.navigate import open_new_tab  # Import new tab navigation
from utils.csv_writer import save_to_csv  # Import CSV saving function
from utils.selenium_setup import initialize_driver  # Import Selenium setup
from utils.load_file import get_url_from_file  # Import URL reading function

def main():
    """Main process for Cognism scraping."""
    
    # 🔹 Read URL from text file
    url = get_url_from_file()

    if not url.startswith("http"):
        print("Error: Invalid URL format in urls.txt. Please enter a valid URL.")
        return

    # 🔹 Initialize WebDriver
    driver = initialize_driver()

    # 🔹 Open Cognism for manual login
    driver.get("https://app.cognism.com/auth/sign-in")
    wait_for_manual_login(driver)  # Wait for manual login

    # 🔹 Open a new tab and navigate to profile URL
    open_new_tab(driver, url)  # ✅ The new tab loads the URL

    # 🔹 Once the page is already loaded, extract data
    extracted_data = scrape_page(driver)  # ✅ No need to pass `url`, it's already loaded
    if extracted_data:
        save_to_csv(extracted_data)  # Save data to CSV

    print("Scraping completed.")
    driver.quit()

if __name__ == "__main__":
    main()
