import csv

def get_urls_from_file(file_path="urls.csv"):
    """
    Reads all URLs from a CSV file and returns a list of dictionaries containing:
    - segment (industry/category)
    - url (Cognism search link)
    - timestamp (date when the URL was added)
    
    :param file_path: The CSV file containing the URLs.
    :return: A list of dictionaries [{segment, url, timestamp}, ...]
    """
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            urls = []

            for row in reader:
                if len(row) < 3:
                    print(f"⚠️ Skipping malformed row: {row}")
                    continue  # Skip if row doesn't have all three values
                
                segment, url, timestamp = row  # Extract values
                if not url.startswith("http"):
                    print(f"⚠️ Skipping invalid URL: {url}")
                    continue
                
                urls.append({"segment": segment.strip(), "url": url.strip(), "timestamp": timestamp.strip()})

            if not urls:
                raise ValueError("⚠️ The CSV file is empty or contains no valid URLs.")

            return urls
    
    except FileNotFoundError:
        print("❌ Error: urls.csv file not found. Please create the file and add URLs.")
        exit(1)
    except Exception as e:
        print(f"❌ Error reading CSV file: {e}")
        exit(1)
