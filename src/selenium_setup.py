from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def initialize_driver():
    """Configures and initializes the Selenium WebDriver for Chrome."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Open Chrome in full screen
    options.add_argument("--disable-dev-shm-usage")  # Prevents crashes
    options.add_argument("--no-sandbox")  # Avoids issues in some environments
    options.add_argument("--disable-gpu")  # Fixes GPU-related errors

    # Initialize WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    return driver
