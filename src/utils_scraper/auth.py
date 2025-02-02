import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import COGNISM_EMAIL, COGNISM_PASSWORD

def wait_for_manual_login(driver):
    """Auto-fills login credentials but does NOT submit the form (for manual CAPTCHA verification)."""
    print("\nOpening Cognism login page...")

    # Wait for page to load and ensure login form is present
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
    except Exception as e:
        print("Error: Page took too long to load.")
        return

    # Wait until the email input field is visible
    try:
        email_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='email']"))
        )
        password_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']"))
        )

        # Clear any pre-filled values
        email_input.clear()
        password_input.clear()

        # Fill in the credentials
        email_input.send_keys(COGNISM_EMAIL)
        password_input.send_keys(COGNISM_PASSWORD)

        print("Credentials auto-filled. Please complete CAPTCHA and login manually.")
        print("Once you are logged in, press ENTER in the terminal.")
        input("Press ENTER to continue after logging in...")

    except Exception as e:
        print(f"Error: Unable to locate email/password fields. \n{e}")
