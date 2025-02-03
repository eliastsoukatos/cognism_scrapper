import sqlite3
from utils.create_database import get_db_path, create_table

def save_urls_to_db(urls_data):
    """Guarda la lista de URLs en la base de datos."""
    if not urls_data or not isinstance(urls_data, list):
        print("⚠️ No URLs to save or incorrect format.")
        return
    
    try:
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        # Asegurar que la tabla exista antes de insertar datos
        create_table()

        for entry in urls_data:
            segment = entry["segment"]
            url = entry["url"]
            timestamp = entry["timestamp"]

            cursor.execute(
                "INSERT OR IGNORE INTO urls (segment, url, timestamp) VALUES (?, ?, ?)",
                (segment, url, timestamp)
            )

        conn.commit()
        conn.close()
        print(f"✅ {len(urls_data)} URLs saved to database.")

    except Exception as e:
        print(f"⚠️ Error saving URLs to database: {e}")
