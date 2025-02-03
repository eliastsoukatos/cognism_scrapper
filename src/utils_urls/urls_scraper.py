from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_urls(driver):
    """Extrae todos los URLs de perfiles de personas en la página actualmente cargada y los completa con el dominio base."""
    try:
        # Espera a que la página cargue completamente
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Extrae solo los URLs de personas (excluyendo compañías)
        try:
            url_elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/search/prospects/persons/')]")
            urls = [
                f"https://app.cognism.com{elem.get_attribute('href')}" if elem.get_attribute('href').startswith("/") else elem.get_attribute('href')
                for elem in url_elements
            ]
        except:
            urls = []
        
        print("🔗 Extracted URLs (People Only):")
        for url in urls:
            print(url)
        
        return {"URLs": urls}

    except Exception as e:
        print(f"⚠️ Error during scraping: {e}")
        return None
