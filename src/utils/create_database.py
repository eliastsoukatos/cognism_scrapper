import sqlite3
import os

DB_NAME = "contacts.db"

def get_db_path():
    """Obtiene la ruta absoluta de la base de datos."""
    return os.path.abspath(DB_NAME)

def create_table():
    """Crea la base de datos y la tabla si no existen."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            Last_Name TEXT,
            Mobile_Phone TEXT,
            Email TEXT,
            Role TEXT,
            City TEXT,
            State TEXT,
            Country TEXT,
            Timezone TEXT,
            LinkedIn_URL TEXT,
            Company_Name TEXT,
            Website TEXT,
            Employees TEXT,
            Founded TEXT,
            Segment TEXT,
            Timestamp TEXT,
            Cognism_URL TEXT
        )
    ''')

    conn.commit()
    conn.close()
    print(f"✅ Database table ensured at {get_db_path()}")

# Si el script se ejecuta directamente, creará la base de datos
if __name__ == "__main__":
    create_table()
