import time
import csv
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# 🔹 Configure Selenium with Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Open Chrome in full screen
options.add_argument("--disable-dev-shm-usage")  # Prevents crashes
options.add_argument("--no-sandbox")  # Avoids issues in some environments
options.add_argument("--disable-gpu")  # Fixes GPU-related errors

# 🔹 Start Selenium WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

def wait_for_manual_login():
    """Waits for the user to manually log into Cognism."""
    print("\n🔑 Please log in to Cognism manually.")
    print("📌 Once you are on the profile page you want to scrape, return to the terminal and press ENTER.")
    input("⌨️ Press ENTER to continue...")

def scrape_page(url):
    """Navigates to the URL and extracts the person's information."""
    print(f"📡 Navigating to: {url}...")
    driver.get(url)

    try:
        # 🔹 Wait for the page to fully load
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        time.sleep(5)  # Extra time for rendering

        # 🔹 Scroll to trigger lazy loading
        for _ in range(5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        # 🔹 Extract email using refined XPath
        try:
            email_element = driver.find_element(By.XPATH, "//a[contains(@class, 't-text-primary-600') and starts-with(@href, 'mailto:')]")
            email = email_element.get_attribute("href").replace("mailto:", "").strip()
        except:
            email = "Not found"

        print(f"✅ Extracted Email: {email}")

        return {"Email": email}

    except Exception as e:
        print(f"⚠️ Error during scraping: {e}")
        return None



def save_to_csv(data):
    """Saves the extracted data to a CSV file."""
    file_exists = os.path.exists("output.csv")

    with open("output.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())

        # Write the header only if the file is new
        if not file_exists:
            writer.writeheader()

        writer.writerow(data)
        print(f"💾 Data saved to output.csv")

def main():
    """Main process for Cognism scraping."""
    url = input("\n🔗 Enter the URL to scrape: ")

    # 🔹 Open Cognism for manual login
    driver.get("https://app.cognism.com/login")
    wait_for_manual_login()

    # 🔹 Once the user confirms login, proceed with scraping
    extracted_data = scrape_page(url)
    if extracted_data:
        save_to_csv(extracted_data)

    print("🚀 Scraping completed.")
    driver.quit()

if __name__ == "__main__":
    main()
