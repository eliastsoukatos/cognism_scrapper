from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_urls(driver):
    """Extrae todos los URLs de perfiles de personas en la página, implementando desplazamiento para listas virtualizadas."""
    try:
        print("⏳ Waiting for the page to load...")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        print("✅ Page loaded. Waiting for contacts table...")
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, '/search/prospects/persons/') and contains(@class, 't-text-primary-600')]"))
        )

        print("🔍 Searching for URLs...")

        # Get the scrollable container
        scroll_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cdk-virtual-scroll-viewport"))
        )

        # Set to store unique URLs
        seen_urls = set()
        previous_count = 0

        while True:
            # Extract URLs currently visible
            url_elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/search/prospects/persons/') and contains(@class, 't-text-primary-600')]")
            
            for elem in url_elements:
                href = elem.get_attribute("href")
                if href and "/search/prospects/persons/" in href:
                    full_url = f"https://app.cognism.com{href}" if href.startswith("/") else href
                    seen_urls.add(full_url)

            # Scroll down inside the virtualized container
            driver.execute_script("arguments[0].scrollBy(0, 300);", scroll_container)
            time.sleep(1.5)  # Wait for new elements to load

            # Check if new URLs were found
            if len(seen_urls) == previous_count:
                break  # Stop if no new URLs are loaded
            
            previous_count = len(seen_urls)

        print(f"🔗 Total URLs Extracted: {len(seen_urls)}")
        for url in seen_urls:
            print(url)

        return {"URLs": list(seen_urls)}

    except Exception as e:
        print(f"⚠️ Error during scrolling & scraping: {e}")
        return None
