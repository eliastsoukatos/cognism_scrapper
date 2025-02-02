import sqlite3
import os

def get_database_path(db_name):
    """
    Gets the correct database path dynamically.
    """
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.abspath(os.path.join(BASE_DIR, f"../../{db_name}"))
    return DB_PATH

def check_database(db_name):
    """
    Connects to the given database and lists all tables and their structure.
    """
    DB_PATH = get_database_path(db_name)

    if not os.path.exists(DB_PATH):
        print(f"❌ Database file not found: {DB_PATH}")
        exit(1)

    print(f"\n🔍 Connecting to database at: {DB_PATH}")

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Fetch all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if not tables:
            print("⚠️ No tables found in the database.")
            conn.close()
            return
        
        print("\n📋 Tables in the database:")
        for idx, table in enumerate(tables, start=1):
            print(f"{idx}. {table[0]}")

        # Print structure of each table
        print("\n🔎 Checking table structures...")
        for table in tables:
            table_name = table[0]
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()

            print(f"\n📝 Structure of table: {table_name}")
            print("Column ID | Column Name       | Data Type")
            print("-" * 50)
            for column in columns:
                print(f"{column[0]:<9} | {column[1]:<16} | {column[2]:<10}")

        conn.close()

    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")

if __name__ == "__main__":
    print("\n📂 Select a database to check:")
    print("1️⃣ contacts.db")
    print("2️⃣ urls.db")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        check_database("contacts.db")
    elif choice == "2":
        check_database("urls.db")
    else:
        print("❌ Invalid choice. Exiting.")
