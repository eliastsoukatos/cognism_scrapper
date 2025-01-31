import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import PAGE_LOAD_TIMEOUT, EXTRA_RENDER_TIME, SCROLL_WAIT_TIME, SCROLL_ITERATIONS

def scrape_page(driver, url):
    """Navigates to the URL and extracts the person's information."""
    
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
