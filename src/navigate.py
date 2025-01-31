import time
from config import TAB_LOAD_TIME  
def open_new_tab(driver, url):
    """Opens a new tab with the profile URL and switches to it."""
    
    if not url.startswith("http"):
        print("Error: Invalid URL format in urls.txt. Please enter a valid URL.")
        return

    print(f"Opening new tab: {url}")

    # Open a new tab
    driver.execute_script("window.open('', '_blank');")

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[-1])  

    # Navigate to the URL in the new tab
    driver.get(url)

    # Ensure the page loads
    time.sleep(TAB_LOAD_TIME) 
