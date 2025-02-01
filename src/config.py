import os
import random
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials
COGNISM_EMAIL = os.getenv("COGNISM_EMAIL")
COGNISM_PASSWORD = os.getenv("COGNISM_PASSWORD")

# Function to introduce variability in waiting times
def randomize_wait_time(base_time):
    return round(base_time * random.uniform(0.5, 1.5), 2)

# Time settings with randomization
SCROLL_ITERATIONS = int(os.getenv("SCROLL_ITERATIONS", 3))  # Fixed integer

PAGE_LOAD_TIMEOUT = float(os.getenv("PAGE_LOAD_TIMEOUT", 10))  # ✅ Allows decimal values
EXTRA_RENDER_TIME = float(os.getenv("EXTRA_RENDER_TIME", 3))  # ✅ Allows decimal values
SCROLL_WAIT_TIME = float(os.getenv("SCROLL_WAIT_TIME", 1))  # ✅ Allows decimal values
TAB_LOAD_TIME = float(os.getenv("TAB_LOAD_TIME", 3))  # ✅ Fixes error with decimals

# Variable for batch size
TABS_PER_BATCH = int(os.getenv("TABS_PER_BATCH", 2))  # Default to 2 if not set