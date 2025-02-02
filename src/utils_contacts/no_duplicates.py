import sqlite3
import os
from utils_contacts.load_file import get_urls_from_file
from utils.create_database import create_table
from config import OVERWRITE_SEGMENT  # Import overwrite setting

# Get the correct database path dynamically
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Gets 'utils_contacts' folder path
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, "../../contacts.db"))  # Adjust to correct database

def get_existing_urls():
    """
    Fetches all existing Cognism URLs from the contacts table in the SQLite database.
    
    :return: A dictionary of URLs with their associated segments.
    """
   
    if not os.path.exists(DB_PATH):
        print(f"⚠️ Database file not found: {DB_PATH}. Ensuring database structure...")
        create_table()  # Call the function from database.py
        print(f"✅ Database ready at: {DB_PATH}")
    
    # Create the contacts table if it does not exist

    try:
        print(f"🔍 Connecting to database at: {DB_PATH}")  # Debugging
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("SELECT Cognism_URL, Segment FROM contacts")
        existing_urls = {row[0]: row[1] for row in cursor.fetchall() if row[0]}  # Store as {url: segment}

        conn.close()
        print(f"✅ Found {len(existing_urls)} existing URLs in database.")
        return existing_urls

    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
        return {}

def update_segment(url, new_segment):
    """
    Updates the segment for an existing Cognism URL in the database.

    :param url: The Cognism URL to update.
    :param new_segment: The new segment to overwrite.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("UPDATE contacts SET Segment = ? WHERE Cognism_URL = ?", (new_segment, url))
        conn.commit()
        conn.close()
        print(f"🔄 Updated segment for URL: {url}")

    except sqlite3.Error as e:
        print(f"❌ Error updating segment for {url}: {e}")

def filter_new_urls():
    """
    Filters out URLs that already exist in the database.
    If a URL exists but has a different segment, update the segment (if enabled in config).
    
    :return: A list of new URLs that are not present in the database.
    """
    # Load URLs from the CSV file
    url_entries = get_urls_from_file()
    print(f"📥 Loaded {len(url_entries)} URLs from CSV.")

    # Get existing URLs from the database
    existing_urls = get_existing_urls()

    new_urls = []  # Store new URLs only

    for entry in url_entries:
        url = entry["url"]
        segment = entry["segment"]

        if url in existing_urls:
            # Check if segment is different
            if existing_urls[url] != segment:
                print(f"⚠️ URL found in database, but segment is different: {url}")
                print(f"   - Old segment: {existing_urls[url]}")
                print(f"   - New segment: {segment}")

                # Update segment if overwriting is enabled
                if OVERWRITE_SEGMENT:
                    update_segment(url, segment)
                    print("✅ Segment updated in database.")
                else:
                    print("🚫 Segment overwrite is disabled. Keeping old segment.")

        else:
            new_urls.append(entry)  # Only add completely new URLs

    print(f"✅ {len(new_urls)} new URLs found (not in database).")
    return new_urls
