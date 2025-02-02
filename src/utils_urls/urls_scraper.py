from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_url(driver):
    """Extrae el URL de la página actualmente cargada y lo completa con el dominio base."""
    try:
        # Espera a que la página cargue completamente
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Extrae el URL
        try:
            url_element = driver.find_element(By.XPATH, "//a[contains(@class, 't-text-primary-600')]")
            relative_url = url_element.get_attribute("href")
            full_url = f"https://app.cognism.com{relative_url}" if relative_url.startswith("/") else relative_url
        except:
            full_url = "Not found"
        
        print(f"🔗 URL: {full_url}")
        
        return {"URL": full_url}

    except Exception as e:
        print(f"⚠️ Error during scraping: {e}")
        return None