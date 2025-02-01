import sqlite3
import time
import os

DB_NAME = "contacts.db"

def print_db_path():
    """Prints the absolute path of the database file."""
    db_path = os.path.abspath(DB_NAME)
    print(f"📂 Using database: {db_path}")

def create_table():
    """Ensures the contacts table exists."""
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
    print("✅ Database table ensured.")

def save_to_db(data):
    """
    Saves extracted data to contacts.db.
    """
    max_retries = 5
    retry_delay = 2  # Seconds to wait before retrying

    for attempt in range(max_retries):
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()

            # Ensure the table exists before inserting
            create_table()

            # Insert data into the table
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

            conn.commit()  # Save changes
            conn.close()  # Close connection

            print("✅ Data successfully saved to contacts.db")
            return
        except sqlite3.OperationalError as e:
            print(f"❌ Database error: {e}. Retrying {attempt+1}/{max_retries}...")
            time.sleep(retry_delay)
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            break

    print(f"❌ Unable to write to database {DB_NAME}. Ensure it is accessible.")

