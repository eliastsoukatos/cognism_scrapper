import os
from utils.auth import wait_for_manual_login
from utils.selenium_setup import initialize_driver  # ✅ Updated import path

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Hides TensorFlow warnings

def run_urls_scraper():
    """Logs into Cognism using Selenium and waits for manual login."""
    
    # Initialize WebDriver
    driver = initialize_driver()

    # Open Cognism login page
    driver.get("https://app.cognism.com/auth/sign-in")
    wait_for_manual_login(driver)

    print("✅ Successfully logged into Cognism.")

    return driver  # Optional: Return the driver if needed later
