import time
from selenium.webdriver.common.keys import Keys

def open_new_tab(driver, url):
    """Opens a new tab with the profile URL and switches to it."""
    
    if not url.startswith("http"):
        print("Error: Invalid URL format in urls.txt. Please enter a valid URL.")
        return

    print(f"Opening new tab: {url}")

    # Open a new tab
    driver.execute_script("window.open('', '_blank');")

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[-1])  # ✅ Always switch to the latest tab

    # Navigate to the URL in the new tab
    driver.get(url)

    # Ensure the page loads
    time.sleep(3)  # Optional delay to ensure page loads properly
