import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials
COGNISM_EMAIL = os.getenv("COGNISM_EMAIL")
COGNISM_PASSWORD = os.getenv("COGNISM_PASSWORD")

# Time settings
PAGE_LOAD_TIMEOUT = int(os.getenv("PAGE_LOAD_TIMEOUT", 10))
EXTRA_RENDER_TIME = int(os.getenv("EXTRA_RENDER_TIME", 3))
SCROLL_WAIT_TIME = int(os.getenv("SCROLL_WAIT_TIME", 1))
SCROLL_ITERATIONS = int(os.getenv("SCROLL_ITERATIONS", 3))