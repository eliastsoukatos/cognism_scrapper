import time
from config import TAB_LOAD_TIME, TABS_PER_BATCH  # Import batch size and timing settings

def open_new_tabs(driver, urls):
    """
    Opens URLs in new tabs in batches and ensures proper navigation.
    :param driver: The Selenium WebDriver.
    :param urls: List of URLs to open.
    """
    for i in range(0, len(urls), TABS_PER_BATCH):
        batch = urls[i:i + TABS_PER_BATCH]  # Get a batch of URLs
        opened_tabs = []  # Track opened tabs

        for url in batch:
            if not url.startswith("http"):
                print(f"Skipping invalid URL: {url}")
                continue

            driver.execute_script("window.open('', '_blank');")
            driver.switch_to.window(driver.window_handles[-1])  
            driver.get(url)
            time.sleep(TAB_LOAD_TIME)
            opened_tabs.append(driver.window_handles[-1])  # Store new tab handles

        yield opened_tabs  # Return only the new tabs opened in this batch
