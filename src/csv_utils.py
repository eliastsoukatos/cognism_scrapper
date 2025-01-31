import csv
import os

def save_to_csv(data, filename="output.csv"):
    """Saves the extracted data to a CSV file."""
    file_exists = os.path.exists(filename)

    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())

        # Write the header only if the file is new
        if not file_exists:
            writer.writeheader()

        writer.writerow(data)
        print(f"💾 Data saved to {filename}")
