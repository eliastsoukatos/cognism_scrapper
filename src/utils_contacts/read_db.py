import sqlite3
from utils.create_database import get_db_path

def get_urls_from_db():
    """
    Retrieves all URLs from the 'urls' table in the contacts.db database.
    
    :return: A list of dictionaries [{segment, url, timestamp}, ...]
    """
    try:
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        cursor.execute("SELECT segment, url, timestamp FROM urls")
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            print("⚠️ The database contains no URLs.")
            return []

        urls = [{"segment": row[0], "url": row[1], "timestamp": row[2]} for row in rows]
        return urls

    except Exception as e:
        print(f"❌ Error retrieving URLs from database: {e}")
        return []
