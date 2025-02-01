import time
from utils.auth import wait_for_manual_login
from utils.navigate import open_new_tabs  # ✅ Maneja la navegación de forma correcta
from utils.scraper import scrape_page
from utils.csv_writer import save_to_csv
from utils.selenium_setup import initialize_driver
from utils.load_file import get_urls_from_file

def main():
    """Main process for Cognism scraping."""

    # Cargar las URLs desde el archivo
    urls = get_urls_from_file()
    if not urls:
        print("⚠️ No valid URLs found in urls.txt.")
        return

    # Inicializar WebDriver
    driver = initialize_driver()

    # Abrir la página de inicio de sesión de Cognism
    driver.get("https://app.cognism.com/auth/sign-in")
    wait_for_manual_login(driver)

    # Guardar la pestaña inicial de login
    login_tab = driver.current_window_handle  

    # Procesar las URLs en lotes
    for tabs in open_new_tabs(driver, urls):  
        for tab in tabs:
            try:
                driver.switch_to.window(tab)  # Cambia a la pestaña abierta
                extracted_data = scrape_page(driver)  # Extrae datos
                if extracted_data:
                    save_to_csv(extracted_data)
                time.sleep(2)  
            except Exception as e:
                print(f"⚠️ Error processing tab: {e}")

        # Cierra SOLO los tabs procesados
        for tab in tabs:
            try:
                driver.switch_to.window(tab)
                driver.close()
            except Exception as e:
                print(f"⚠️ Error closing tab: {e}")

        # **Asegurar que volvemos a la pestaña de login ANTES de abrir nuevas pestañas**
        try:
            driver.switch_to.window(login_tab)
        except Exception as e:
            print(f"⚠️ Error switching back to login tab: {e}")

    print("✅ Scraping completed.")
    driver.quit()

if __name__ == "__main__":
    main()
