from selenium.webdriver.common.by import By

# US States and their respective Timezones
STATE_TIMEZONE_MAPPING = {
    "California": "PT", "Oregon": "PT", "Washington": "PT", "Nevada": "PT",
    "Idaho": "MT", "Montana": "MT", "Wyoming": "MT", "Utah": "MT", "Colorado": "MT", "Arizona": "MT", "New Mexico": "MT",
    "North Dakota": "CT", "South Dakota": "CT", "Nebraska": "CT", "Kansas": "CT", "Oklahoma": "CT", "Texas": "CT",
    "Minnesota": "CT", "Iowa": "CT", "Missouri": "CT", "Arkansas": "CT", "Louisiana": "CT", "Wisconsin": "CT", "Illinois": "CT",
    "Mississippi": "CT", "Alabama": "CT", "Tennessee": "CT", "Kentucky": "CT",
    "Indiana": "ET", "Ohio": "ET", "West Virginia": "ET", "Virginia": "ET", "North Carolina": "ET", "South Carolina": "ET",
    "Georgia": "ET", "Florida": "ET", "Michigan": "ET", "Pennsylvania": "ET", "New York": "ET", "New Jersey": "ET",
    "Connecticut": "ET", "Rhode Island": "ET", "Massachusetts": "ET", "Vermont": "ET", "New Hampshire": "ET", "Maine": "ET"
}

def extract_location(driver):
    """Extracts the person's location details (City, State, Country) and assigns a timezone if in the USA."""
    try:
        # Find the second div inside the role/location container
        location_element = driver.find_element(By.XPATH, "//div[contains(@class, 't-text-sm t-text-dark-400')]/div[2]")
        full_location = location_element.text.strip()

        # Remove unnecessary new lines
        full_location = full_location.replace("\n", ", ").replace("  ", " ")

        # Debugging print statement (remove in production)
        print(f"📍 Raw Location Extracted: {full_location}")

        # Split into City, State, Country
        location_parts = [part.strip() for part in full_location.split(",")]

        city = location_parts[0] if len(location_parts) > 0 else "Not found"
        state = location_parts[1] if len(location_parts) > 1 else "Not found"
        country = location_parts[2] if len(location_parts) > 2 else "Not found"

        # Determine timezone if country is United States
        timezone = STATE_TIMEZONE_MAPPING.get(state, "Not found") if country == "United States" else "Not applicable"

        # Debugging print statement (remove in production)
        print(f"🌍 Parsed Location: City: {city}, State: {state}, Country: {country}, Timezone: {timezone}")

        return city, state, country, timezone
    except Exception as e:
        print(f"⚠️ Error extracting location: {e}")
        return "Not found", "Not found", "Not found", "Not applicable"
