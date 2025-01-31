import csv
import os
import time

def save_to_csv(data, filename="output.csv"):
    """Saves the extracted data to a CSV file, retrying if the file is locked."""
    max_retries = 5
    retry_delay = 2  # Seconds to wait before retrying

    for attempt in range(max_retries):
        try:
            file_exists = os.path.exists(filename)
            with open(filename, mode="a", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=[
                    "Name", "Last Name", "Mobile Phone", "Email", "Role",
                    "City", "State", "Country", "Timezone", "LinkedIn URL",
                    "Company Name", "Website", "Employees", "Founded"
                ])
                if not file_exists:
                    writer.writeheader()
                writer.writerow(data)

            print(f"Data saved to {filename}")
            return
        except PermissionError:
            print(f"File {filename} is locked. Retrying {attempt+1}/{max_retries}...")
            time.sleep(retry_delay)

    print(f"Unable to write to {filename}. Ensure the file is not open and try again.")
