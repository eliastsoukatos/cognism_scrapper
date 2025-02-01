import time
from utils.scraper import scrape_page  # Import scraping function
from utils.auth import wait_for_manual_login  # Import login function
from utils.navigate import open_new_tabs  # Import new tab navigation
from utils.csv_writer import save_to_csv  # Import CSV saving function
from utils.selenium_setup import initialize_driver  # Import Selenium setup
from utils.load_file import get_urls_from_file  # Import URL reading function

def main():
    """Main process for Cognism scraping."""

    # Read URLs from file
    urls = get_urls_from_file()
    if not urls:
        print("⚠️ No valid URLs found in urls.txt.")
        return

    # Initialize WebDriver
    driver = initialize_driver()

    # Open Cognism login page
    driver.get("https://app.cognism.com/auth/sign-in")
    wait_for_manual_login(driver)

    # Process URLs in batches
    for tabs in open_new_tabs(driver, urls):
        for tab in tabs:
            try:
                driver.switch_to.window(tab)
                extracted_data = scrape_page(driver)
                if extracted_data:
                    save_to_csv(extracted_data)
                time.sleep(2)  # Small delay to avoid rate limits
            except Exception as e:
                print(f"⚠️ Error processing tab: {e}")

        # Close processed tabs safely
        for tab in tabs:
            try:
                driver.switch_to.window(tab)
                driver.close()
            except Exception as e:
                print(f"⚠️ Error closing tab: {e}")

        # Ensure main window is still valid before switching back
        try:
            if driver.window_handles:
                driver.switch_to.window(driver.window_handles[0])
            else:
                print("⚠️ No active windows remaining. Closing session.")
                driver.quit()
                return
        except Exception as e:
            print(f"⚠️ Error switching back to main window: {e}")

    print("✅ Scraping completed.")
    driver.quit()

if __name__ == "__main__":
    main()
