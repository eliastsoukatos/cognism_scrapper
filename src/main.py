import time
from utils.scraper import scrape_page  # Import scraping function
from utils.auth import wait_for_manual_login  # Import login function
from utils.navigate import open_new_tabs  # Import new tab navigation
from utils.csv_writer import save_to_csv  # Import CSV saving function
from utils.selenium_setup import initialize_driver  # Import Selenium setup
from utils.load_file import get_urls_from_file  # Import URL reading function

def main():
    """Main process for Cognism scraping."""
    
    # Read all URLs from the text file
    urls = get_urls_from_file()
    if not urls:
        print("No valid URLs found in urls.txt.")
        return

    # Initialize WebDriver
    driver = initialize_driver()

    # Open Cognism login page
    driver.get("https://app.cognism.com/auth/sign-in")
    wait_for_manual_login(driver)  # Wait for manual login

    # Process URLs in batches of 2
    for tabs in open_new_tabs(driver, urls, batch_size=2):
        for tab in tabs:
            driver.switch_to.window(tab)  # Switch to each opened tab
            extracted_data = scrape_page(driver)  # Extract data from the tab
            if extracted_data:
                save_to_csv(extracted_data)  # Save data to CSV
            time.sleep(2)  # Small delay between scraping sessions

        # Close processed tabs before opening new ones
        for tab in tabs:
            driver.switch_to.window(tab)
            driver.close()

        # Switch back to the main window before continuing
        driver.switch_to.window(driver.window_handles[0])

    print("Scraping completed.")
    driver.quit()

if __name__ == "__main__":
    main()
