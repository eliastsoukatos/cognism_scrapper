import time
import csv
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from scraper_utils import scrape_page  # Importing the function
from auth_utils import wait_for_manual_login  # Importing the auth function

# 🔹 Configure Selenium with Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Open Chrome in full screen
options.add_argument("--disable-dev-shm-usage")  # Prevents crashes
options.add_argument("--no-sandbox")  # Avoids issues in some environments
options.add_argument("--disable-gpu")  # Fixes GPU-related errors

# 🔹 Start Selenium WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

def save_to_csv(data):
    """Saves the extracted data to a CSV file."""
    file_exists = os.path.exists("output.csv")

    with open("output.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())

        # Write the header only if the file is new
        if not file_exists:
            writer.writeheader()

        writer.writerow(data)
        print(f"💾 Data saved to output.csv")

def main():
    """Main process for Cognism scraping."""
    url = input("\n🔗 Enter the URL to scrape: ").strip()  # Ensure no spaces

    if not url.startswith("http"):
        print("❌ Error: Invalid URL format. Please enter a valid URL.")
        return

    # 🔹 Open Cognism for manual login
    driver.get("https://app.cognism.com/login")
    wait_for_manual_login(driver)  # Pass driver instance

    # 🔹 Once the user confirms login, proceed with scraping
    extracted_data = scrape_page(driver, url)  # Pass driver instance
    if extracted_data:
        save_to_csv(extracted_data)

    print("🚀 Scraping completed.")
    driver.quit()

if __name__ == "__main__":
    main()
