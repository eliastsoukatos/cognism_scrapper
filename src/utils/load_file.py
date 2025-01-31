def get_urls_from_file(file_path="urls.txt"):
    """Reads all URLs from a text file and returns them as a list."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            urls = [line.strip() for line in file if line.strip()]  # Read all lines and remove empty ones
            if not urls:
                raise ValueError("The URL file is empty. Please add URLs to urls.txt.")
            return urls
    except FileNotFoundError:
        print("Error: urls.txt file not found. Please create the file and add URLs.")
        exit(1)
    except Exception as e:
        print(f"Error reading URL file: {e}")
        exit(1)
