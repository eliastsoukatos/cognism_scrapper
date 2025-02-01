import time
from utils.auth import wait_for_manual_login
from utils.navigate import open_new_tabs
from utils.scraper import scrape_page
from utils.csv_writer import save_to_csv
from utils.selenium_setup import initialize_driver
from utils.load_file import get_urls_from_file
from config import SCRAPING_DELAY  # ✅ Import randomized delay time

def main():
    """Main process for Cognism scraping."""

    # Load URLs from file
    url_entries = get_urls_from_file()
    if not url_entries:
        print("⚠️ No valid URLs found in urls.csv.")
        return

    # Extract only the URL list for navigation
    urls = [entry["url"] for entry in url_entries]  # ✅ Pass only URLs to `open_new_tabs()`

    # Initialize WebDriver
    driver = initialize_driver()

    # Open Cognism login page
    driver.get("https://app.cognism.com/auth/sign-in")
    wait_for_manual_login(driver)

    # Save the initial login tab
    login_tab = driver.current_window_handle  

    # Process URLs in batches
    for batch_index, tabs in enumerate(open_new_tabs(driver, urls)):  
        for tab_index, tab in enumerate(tabs):
            try:
                driver.switch_to.window(tab)  # Switch to opened tab
                
                # Get the corresponding data entry (segment, timestamp, URL)
                data_entry = url_entries[(batch_index * len(tabs)) + tab_index]  # ✅ Get full row
                
                extracted_data = scrape_page(driver)  # Extract data
                if extracted_data:
                    # ✅ Merge extracted data with segment, timestamp, and Cognism URL
                    extracted_data.update({
                        "Segment": data_entry["segment"],
                        "Timestamp": data_entry["timestamp"],
                        "Cognism URL": data_entry["url"]
                    })
                    save_to_csv(extracted_data)
                
                time.sleep(SCRAPING_DELAY)  # ✅ Uses randomized wait time
                
            except Exception as e:
                print(f"⚠️ Error processing tab: {e}")

        # Close ONLY the processed tabs
        for tab in tabs:
            try:
                driver.switch_to.window(tab)
                driver.close()
            except Exception as e:
                print(f"⚠️ Error closing tab: {e}")

        # Ensure we switch back to login tab BEFORE opening new tabs
        try:
            driver.switch_to.window(login_tab)
        except Exception as e:
            print(f"⚠️ Error switching back to login tab: {e}")

    print("✅ Scraping completed.")
    driver.quit()

if __name__ == "__main__":
    main()
