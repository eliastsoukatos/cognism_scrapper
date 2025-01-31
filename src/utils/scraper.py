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
from extractors.extract_linkedin import extract_linkedin
from extractors.extract_company import extract_company  # Import Company Extractor

def scrape_page(driver):
    """Extracts all relevant data from the already loaded page (URL should be loaded before calling this)."""

    try:
        # 🔹 Ensure the page has fully loaded before scraping
        WebDriverWait(driver, PAGE_LOAD_TIMEOUT).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        time.sleep(EXTRA_RENDER_TIME)

        # 🔹 Scroll to trigger lazy loading
        for _ in range(SCROLL_ITERATIONS):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_WAIT_TIME)

        # 🔹 Extract Data
        first_name, last_name = extract_name(driver)
        email = extract_email(driver)
        mobile_phone = extract_mobile_phone(driver)
        role = extract_role(driver)
        city, state, country, timezone = extract_location(driver)
        linkedin_url = extract_linkedin(driver)
        company_name, website, employees, founded = extract_company(driver)  # Extract Company Details

        # 🔹 Format data properly
        role = role.replace("\n", " ")  # Remove line breaks from role

        print(f"Name: {first_name} {last_name}")
        print(f"Email: {email}")
        print(f"Mobile Phone: {mobile_phone}")
        print(f"Role: {role}")
        print(f"Location: {city}, {state}, {country} | Timezone: {timezone}")
        print(f"LinkedIn: {linkedin_url}")
        print(f"Company: {company_name} | Website: {website} | Employees: {employees} | Founded: {founded}")

        return {
            "Name": first_name,
            "Last Name": last_name,
            "Mobile Phone": mobile_phone,
            "Email": email,
            "Role": role,
            "City": city,
            "State": state,
            "Country": country,
            "Timezone": timezone,
            "LinkedIn URL": linkedin_url,
            "Company Name": company_name,
            "Website": website,
            "Employees": employees,
            "Founded": founded
        }

    except Exception as e:
        print(f"Error during scraping: {e}")
        return None
