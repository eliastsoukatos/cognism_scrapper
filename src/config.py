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
PAGE_LOAD_TIMEOUT = lambda: randomize_wait_time(int(os.getenv("PAGE_LOAD_TIMEOUT", 10)))
EXTRA_RENDER_TIME = lambda: randomize_wait_time(int(os.getenv("EXTRA_RENDER_TIME", 3)))
SCROLL_WAIT_TIME = lambda: randomize_wait_time(int(os.getenv("SCROLL_WAIT_TIME", 1)))
TAB_LOAD_TIME = lambda: randomize_wait_time(int(os.getenv("TAB_LOAD_TIME", 3)))  # Now a function
SCROLL_ITERATIONS = int(os.getenv("SCROLL_ITERATIONS", 3))  # Fixed integer
