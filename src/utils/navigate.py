import time
from config import TAB_LOAD_TIME

def open_new_tab(driver, url):
    """Opens a new tab with the profile URL and switches to it, avoiding unnecessary reloads."""
    
    if not url.startswith("http"):
        print("Error: Invalid URL format in urls.txt. Please enter a valid URL.")
        return

    print(f"Opening new tab: {url}")

    # Open a new tab **directly with the URL**
    driver.execute_script(f"window.open('{url}', '_blank');")

    # Switch to the new tab (last opened tab)
    driver.switch_to.window(driver.window_handles[-1])  

    # Ensure the page loads
    time.sleep(TAB_LOAD_TIME)  # Controlled by .env
