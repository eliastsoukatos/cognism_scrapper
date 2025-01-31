import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import PAGE_LOAD_TIMEOUT, EXTRA_RENDER_TIME, SCROLL_WAIT_TIME, SCROLL_ITERATIONS
from extractors.extract_email import extract_email
from extractors.extract_mobile_phone import extract_mobile_phone
from extractors.extract_name import extract_name  # Import Name extractor

def scrape_page(driver, url):
    """Navigates to the URL and extracts Name, Last Name, Email, and Mobile Phone."""
    
    # Ensure URL is properly formatted
    if not url.startswith("http"):
        print(f"⚠️ Invalid URL provided: {url}")
        return None

    print(f"📡 Navigating to: {url}...")
    driver.get(url.strip())  # Strip any spaces from the URL

    try:
        # 🔹 Wait for the page to fully load
        WebDriverWait(driver, PAGE_LOAD_TIMEOUT).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        time.sleep(EXTRA_RENDER_TIME)  # Extra time for rendering

        # 🔹 Scroll to trigger lazy loading
        for _ in range(SCROLL_ITERATIONS):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_WAIT_TIME)

        # 🔹 Extract Name, Last Name, Email, and Mobile Phone
        first_name, last_name = extract_name(driver)
        email = extract_email(driver)
        mobile_phone = extract_mobile_phone(driver)

        print(f"🆔 Name: {first_name} {last_name}")
        print(f"📩 Email: {email}")
        print(f"📱 Mobile Phone: {mobile_phone}")

        return {
            "Name": first_name,
            "Last Name": last_name,
            "Mobile Phone": mobile_phone,
            "Email": email
        }

    except Exception as e:
        print(f"⚠️ Error during scraping: {e}")
        return None
