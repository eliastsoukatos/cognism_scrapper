import os
from utils.auth import wait_for_manual_login
from utils.selenium_setup import initialize_driver  # ✅ Updated import path
from utils_urls.urls_scraper import scrape_url  # ✅ Import scrape_url

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
    industry_segment = input("📌 Input the Company's Industry Segment: ")

    print(f"✅ Industry segment selected: {industry_segment}")

    # Llamar a la función scrape_url
    scrape_url(driver)

    return driver, industry_segment  # Optional: Return values for later use
