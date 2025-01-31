import time
from scraper_utils import scrape_page  # Importing the function
from auth_utils import wait_for_manual_login  # Importing the auth function
from csv_utils import save_to_csv  # Importing the CSV saving function
from selenium_setup import initialize_driver  # Importing the Selenium setup function

def main():
    """Main process for Cognism scraping."""
    url = input("\n🔗 Enter the URL to scrape: ").strip()  # Ensure no spaces

    if not url.startswith("http"):
        print("❌ Error: Invalid URL format. Please enter a valid URL.")
        return

    # 🔹 Initialize WebDriver
    driver = initialize_driver()

    # 🔹 Open Cognism for manual login
    driver.get("https://app.cognism.com/auth/sign-in")
    wait_for_manual_login(driver)  # Pass driver instance

    # 🔹 Once the user confirms login, proceed with scraping
    extracted_data = scrape_page(driver, url)  # Pass driver instance
    if extracted_data:
        save_to_csv(extracted_data)  # Using the function from csv_utils.py

    print("🚀 Scraping completed.")
    driver.quit()

if __name__ == "__main__":
    main()
