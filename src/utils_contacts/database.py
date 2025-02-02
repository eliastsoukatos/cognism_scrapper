import sqlite3
import time
import os
from utils.create_database import create_table, get_db_path

DB_NAME = "contacts.db"

def print_db_path():
    """Imprime la ruta de la base de datos."""
    print(f"📂 Using database: {get_db_path()}")

def save_to_db(data):
    """
    Guarda datos en la base de datos de contactos.
    """
    max_retries = 5
    retry_delay = 2  # Segundos antes de reintentar

    for attempt in range(max_retries):
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()

            # Asegurar que la tabla existe antes de insertar datos
            create_table()

            # Insertar datos en la tabla
            cursor.execute('''
                INSERT INTO contacts (
                    Name, Last_Name, Mobile_Phone, Email, Role,
                    City, State, Country, Timezone, LinkedIn_URL,
                    Company_Name, Website, Employees, Founded,
                    Segment, Timestamp, Cognism_URL
                ) VALUES (
                    :Name, :Last_Name, :Mobile_Phone, :Email, :Role,
                    :City, :State, :Country, :Timezone, :LinkedIn_URL,
                    :Company_Name, :Website, :Employees, :Founded,
                    :Segment, :Timestamp, :Cognism_URL
                )
            ''', data)

            conn.commit()
            conn.close()
            print("✅ Data successfully saved to contacts.db")
            return
        except sqlite3.OperationalError as e:
            print(f"❌ Database error: {e}. Retrying {attempt+1}/{max_retries}...")
            time.sleep(retry_delay)
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            break

    print(f"❌ Unable to write to database {DB_NAME}. Ensure it is accessible.")
