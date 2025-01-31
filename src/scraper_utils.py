import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import PAGE_LOAD_TIMEOUT, EXTRA_RENDER_TIME, SCROLL_WAIT_TIME, SCROLL_ITERATIONS
from extractors.extract_email import extract_email
from extractors.extract_mobile_phone import extract_mobile_phone
from extractors.extract_name import extract_name
from extractors.extract_role import extract_role
from extractors.extract_location import extract_location

def scrape_page(driver, url):
    """Navigates to the URL and extracts all relevant data."""
    
    if not url.startswith("http"):
        print(f"⚠️ Invalid URL provided: {url}")
        return None

    print(f"📡 Navigating to: {url}...")
    driver.get(url.strip())

    try:
        WebDriverWait(driver, PAGE_LOAD_TIMEOUT).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        time.sleep(EXTRA_RENDER_TIME)

        for _ in range(SCROLL_ITERATIONS):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_WAIT_TIME)

        first_name, last_name = extract_name(driver)
        email = extract_email(driver)
        mobile_phone = extract_mobile_phone(driver)
        role = extract_role(driver)
        city, state, country, timezone = extract_location(driver)

        print(f"🆔 Name: {first_name} {last_name}")
        print(f"📩 Email: {email}")
        print(f"📱 Mobile Phone: {mobile_phone}")
        print(f"💼 Role: {role}")
        print(f"📍 Location: {city}, {state}, {country} | Timezone: {timezone}")

        return {
            "Name": first_name,
            "Last Name": last_name,
            "Mobile Phone": mobile_phone,
            "Email": email,
            "Role": role,
            "City": city,
            "State": state,
            "Country": country,
            "Timezone": timezone
        }

    except Exception as e:
        print(f"⚠️ Error during scraping: {e}")
        return None
