import time
from scraper_utils import scrape_page  # Import scraping function
from auth_utils import wait_for_manual_login  # Import login function
from csv_utils import save_to_csv  # Import CSV saving function
from selenium_setup import initialize_driver  # Import Selenium setup
from file_utils import get_url_from_file  # Import URL reading function

def main():
    """Main process for Cognism scraping."""
    
    # 🔹 Read URL from text file
    url = get_url_from_file()

    if not url.startswith("http"):
        print("❌ Error: Invalid URL format in urls.txt. Please enter a valid URL.")
        return

    # 🔹 Initialize WebDriver
    driver = initialize_driver()

    # 🔹 Open Cognism for manual login
    driver.get("https://app.cognism.com/login")
    wait_for_manual_login(driver)  # Pass driver instance

    # 🔹 Once the user confirms login, proceed with scraping
    extracted_data = scrape_page(driver, url)  # Pass driver instance
    if extracted_data:
        save_to_csv(extracted_data)  # Save data to CSV

    print("🚀 Scraping completed.")
    driver.quit()

if __name__ == "__main__":
    main()

