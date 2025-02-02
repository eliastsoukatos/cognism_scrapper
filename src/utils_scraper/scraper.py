import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import PAGE_LOAD_TIMEOUT, EXTRA_RENDER_TIME, SCROLL_WAIT_TIME, SCROLL_ITERATIONS
from contact_extractors.extract_email import extract_email
from contact_extractors.extract_mobile_phone import extract_mobile_phone
from contact_extractors.extract_name import extract_name
from contact_extractors.extract_role import extract_role
from contact_extractors.extract_location import extract_location
from contact_extractors.extract_linkedin import extract_linkedin
from contact_extractors.extract_company import extract_company

def scrape_page(driver):
    """Extracts all relevant data from the currently loaded page."""
    try:
        # Espera a que la página cargue completamente
        WebDriverWait(driver, PAGE_LOAD_TIMEOUT).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        time.sleep(EXTRA_RENDER_TIME)

        # Realiza un scroll para cargar más contenido si es necesario
        for _ in range(SCROLL_ITERATIONS):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_WAIT_TIME)

        # Extrae los datos de la página
        first_name, last_name = extract_name(driver)
        email = extract_email(driver)
        mobile_phone = extract_mobile_phone(driver)

        try:
            role = extract_role(driver)
        except:
            print("⚠️ Error extracting role. Element not found.")
            role = "Not found"

        try:
            city, state, country, timezone = extract_location(driver)
        except:
            print("⚠️ Error extracting location. Element not found.")
            city, state, country, timezone = "Not found", "Not found", "Not found", "Not applicable"

        try:
            linkedin_url = extract_linkedin(driver)
        except:
            print("⚠️ Error extracting LinkedIn URL. Element not found.")
            linkedin_url = "Not found"

        try:
            company_name, website, employees, founded = extract_company(driver)
        except:
            print("⚠️ Error extracting company details. Element not found.")
            company_name, website, employees, founded = "Not found", "Not found", "Not found", "Not found"

        # Imprime los datos extraídos
        print(f"💼 Role: {role}")
        print(f"📍 Location: {city}, {state}, {country} | Timezone: {timezone}")
        print(f"🔗 LinkedIn: {linkedin_url}")
        print(f"🏢 Company: {company_name} | Website: {website} | Employees: {employees} | Founded: {founded}")

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
        print(f"⚠️ Error during scraping: {e}")
        return None
