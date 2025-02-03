from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utils_urls.urls_scraper import scrape_urls
from utils_urls.input_urls_db import save_urls_to_db

def navigate_and_scrape(driver, segment):
    """Navigates through pages and scrapes contacts until the last page."""
    page_number = 1  # Track the number of pages scraped

    while True:
        print(f"📄 Scraping Page {page_number}...")

        # Scrape the current page
        urls_data = scrape_urls(driver, segment)
        if urls_data and "URLs" in urls_data:
            save_urls_to_db(urls_data["URLs"])

        # Try to find the 'Next' button
        try:
            next_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-cognism='paginate-next-a']"))
            )
        except:
            print("✅ Reached the last page. Stopping scraping.")
            break  # If the button doesn't exist, stop scraping

        # Check if the button is disabled (if applicable)
        if "disabled" in next_button.get_attribute("class"):
            print("✅ Pagination ended (Next button disabled).")
            break

        # Click the next button
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(3)  # Wait for new data to load

        # After clicking, check if the URL list changes
        new_urls_data = scrape_urls(driver, segment)

        # If new_urls_data is empty or identical to the previous list, we are at the last page
        if not new_urls_data or new_urls_data["URLs"] == urls_data["URLs"]:
            print("✅ No new contacts found. Stopping scraping.")
            break

        page_number += 1  # Move to the next page
