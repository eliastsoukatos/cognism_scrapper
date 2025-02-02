import sqlite3
import os
from utils.load_file import get_urls_from_file

# Get the correct database path dynamically
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Gets 'utils' folder path
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, "../../contacts.db"))  # Adjust to correct database

def get_existing_urls():
    """
    Fetches all existing Cognism URLs from the contacts table in the SQLite database.
    
    :return: A set of URLs already present in the database.
    """
    if not os.path.exists(DB_PATH):
        print(f"❌ Database file not found: {DB_PATH}")
        exit(1)

    try:
        print(f"🔍 Connecting to database at: {DB_PATH}")  # Debugging
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("SELECT Cognism_URL FROM contacts")
        existing_urls = {row[0] for row in cursor.fetchall() if row[0]}  # Convert to a set for fast lookup

        conn.close()
        print(f"✅ Found {len(existing_urls)} existing URLs in database.")
        return existing_urls

    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
        return set()

def filter_new_urls():
    """
    Filters out URLs that already exist in the database.
    
    :return: A list of new URLs that are not present in the database.
    """
    # Load URLs from the CSV file
    url_entries = get_urls_from_file()
    print(f"📥 Loaded {len(url_entries)} URLs from CSV.")

    # Get existing URLs from the database
    existing_urls = get_existing_urls()

    # Filter out URLs that already exist
    new_urls = [entry for entry in url_entries if entry["url"] not in existing_urls]

    print(f"✅ {len(new_urls)} new URLs found (not in database).")
    return new_urls
