import os
from utils.auth import wait_for_manual_login
from utils.selenium_setup import initialize_driver
from utils_urls.urls_scraper import scrape_urls
from utils_urls.input_urls_db import save_urls_to_db  # ✅ Import DB function

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Hides TensorFlow warnings

def run_urls_scraper():
    """Logs into Cognism using Selenium, waits for manual login, and prompts for industry segment input."""
    
    # Initialize WebDriver
    driver = initialize_driver()

    # Open Cognism login page
    driver.get("https://app.cognism.com/auth/sign-in")
    wait_for_manual_login(driver)

    print("✅ Successfully logged into Cognism.")

    print(f"Now create a search of contacts on Cognism and input their segment.")

    # Prompt user for input
    segment = input("📌 Input the Company's Industry Segment: ")

    print(f"✅ Industry segment selected: {segment}")

    # Scrape URLs
    urls_result = scrape_urls(driver, segment)

    # Save to database if scraping was successful
    if urls_result and "URLs" in urls_result:
        save_urls_to_db(urls_result["URLs"])

    return driver, segment  # Optional: Return values for later use
