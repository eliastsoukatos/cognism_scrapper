import time
from config import TAB_LOAD_TIME  # Import randomized time function

def open_new_tabs(driver, urls, batch_size=2):
    """
    Opens URLs in new tabs in batches.
    :param driver: The Selenium WebDriver.
    :param urls: List of URLs to open.
    :param batch_size: Number of tabs to open at a time.
    """
    for i in range(0, len(urls), batch_size):
        batch = urls[i:i + batch_size]  # Get a batch of URLs
        
        #print(f"Opening batch: {batch}")

        for url in batch:
            if not url.startswith("http"):
                print(f"Skipping invalid URL: {url}")
                continue

            #print(f"Opening new tab: {url}")
            driver.execute_script("window.open('', '_blank');")
            driver.switch_to.window(driver.window_handles[-1])  
            driver.get(url)
            time.sleep(TAB_LOAD_TIME())  # Wait for tab to load

        # Process each tab before opening new ones
        yield driver.window_handles[-batch_size:]  # Return the last opened tabs
