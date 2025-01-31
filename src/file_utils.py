def get_url_from_file(file_path="urls.txt"):
    """Reads the first URL from a text file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            url = file.readline().strip()  # Read first line and strip spaces
            if not url:
                raise ValueError("⚠️ The URL file is empty. Please add a URL to urls.txt.")
            return url
    except FileNotFoundError:
        print("❌ Error: urls.txt file not found. Please create the file and add a URL.")
        exit(1)
    except Exception as e:
        print(f"❌ Error reading URL file: {e}")
        exit(1)
