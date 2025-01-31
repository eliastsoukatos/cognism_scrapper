import os
import random
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials
COGNISM_EMAIL = os.getenv("COGNISM_EMAIL")
COGNISM_PASSWORD = os.getenv("COGNISM_PASSWORD")

# Function to add variability to wait times (±50%)
def randomize_wait_time(base_time):
    """Returns a randomized wait time within ±50% range."""
    variation = random.uniform(0.5, 1.5)  # Generates a multiplier between 0.5x and 1.5x
    return max(1, int(base_time * variation))  # Ensures minimum wait time of 1 second

# Time settings with variability
PAGE_LOAD_TIMEOUT = lambda: randomize_wait_time(int(os.getenv("PAGE_LOAD_TIMEOUT", 10)))
EXTRA_RENDER_TIME = lambda: randomize_wait_time(int(os.getenv("EXTRA_RENDER_TIME", 3)))
SCROLL_WAIT_TIME = lambda: randomize_wait_time(int(os.getenv("SCROLL_WAIT_TIME", 1)))
TAB_LOAD_TIME = lambda: randomize_wait_time(int(os.getenv("TAB_LOAD_TIME", 3)))

# Fixed iteration count (no need to randomize this)
SCROLL_ITERATIONS = int(os.getenv("SCROLL_ITERATIONS", 3))
