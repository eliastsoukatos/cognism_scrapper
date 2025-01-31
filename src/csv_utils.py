import csv
import os

def save_to_csv(data, filename="output.csv"):
    """Saves the extracted data to a CSV file correctly formatted."""
    file_exists = os.path.exists(filename)

    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "Name", "Last Name", "Mobile Phone", "Email", "Role", "City", "State", "Country", "Timezone", "LinkedIn URL"
        ])

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "Name": data["Name"],
            "Last Name": data["Last Name"],
            "Mobile Phone": data["Mobile Phone"],
            "Email": data["Email"],
            "Role": data["Role"],
            "City": data["City"],
            "State": data["State"],
            "Country": data["Country"],
            "Timezone": data["Timezone"],
            "LinkedIn URL": data["LinkedIn URL"]
        })

        print(f"💾 Data saved to {filename}")
