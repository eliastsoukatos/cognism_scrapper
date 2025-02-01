import time
from config import TAB_LOAD_TIME, TABS_PER_BATCH  # Import new batch size variable

def open_new_tabs(driver, urls):
    """
    Opens URLs in new tabs in batches.
    :param driver: The Selenium WebDriver.
    :param urls: List of URLs to open.
    """
    for i in range(0, len(urls), TABS_PER_BATCH):
        batch = urls[i:i + TABS_PER_BATCH]  # Get a batch of URLs

        for url in batch:
            if not url.startswith("http"):
                print(f"Skipping invalid URL: {url}")
                continue

            driver.execute_script("window.open('', '_blank');")
            driver.switch_to.window(driver.window_handles[-1])  
            driver.get(url)
            time.sleep(TAB_LOAD_TIME) 


        # Process each tab before opening new ones
        yield driver.window_handles[-TABS_PER_BATCH:]  # Return the last opened tabs
