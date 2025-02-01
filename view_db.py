import sqlite3

def choose_database():
    """
    Prompt the user to choose between `contacts.db` and `urls.db`.
    """
    while True:
        print("\n📂 Select a database to view:")
        print("1️⃣ contacts.db")
        print("2️⃣ urls.db")
        choice = input("Enter the number of your choice (1 or 2): ").strip()

        if choice == "1":
            return "contacts.db"
        elif choice == "2":
            return "urls.db"
        else:
            print("❌ Invalid choice. Please enter 1 or 2.")

def view_data(db_name):
    """
    Retrieves and displays all data from the chosen database.
    """
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Get the table names in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if not tables:
            print(f"⚠️ No tables found in {db_name}.")
            conn.close()
            return
        
        # Display available tables
        print(f"\n📊 Tables in {db_name}:")
        for idx, table in enumerate(tables):
            print(f"{idx + 1}. {table[0]}")

        # Ask user to select a table
        table_choice = input("\nEnter the table name to view data: ").strip()

        if table_choice not in [t[0] for t in tables]:
            print("❌ Invalid table name. Please try again.")
            conn.close()
            return

        # Fetch all data from the chosen table
        cursor.execute(f"SELECT * FROM {table_choice}")
        rows = cursor.fetchall()

        # Print column names
        column_names = [description[0] for description in cursor.description]
        print("\n📋 Data in table:", table_choice)
        print(f"{' | '.join(column_names)}")
        print("-" * 100)

        # Print each row
        for row in rows:
            print(row)

        conn.close()
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")

# Main Execution
if __name__ == "__main__":
    selected_db = choose_database()
    view_data(selected_db)
