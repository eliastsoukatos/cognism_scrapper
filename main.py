import sys
import os

# Add src to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from src.main_urls import run_urls_scraper
from src.main_contacts import run_contacts_scraper

def main():
    print("Welcome to the Cognism Scraper.")
    print("Press 1 to start scraping URLs from your database.")
    print("Press 2 to start scraping the contacts from your database.")

    user_input = input("Enter your choice: ")

    if user_input == "1":
        run_urls_scraper()    
    elif user_input == "2":
        run_contacts_scraper()
    else:
        print("❌ Invalid option. Exiting...")

if __name__ == "__main__":
    main()
