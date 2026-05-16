"""
Configuration settings for the test automation framework.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Browser Configuration
BROWSER = os.getenv("BROWSER", "chrome").lower()
HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "5"))
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "20"))

# URLs - Part 1: Basic Assertions
GOOGLE_URL = "https://www.google.com"

# URLs - Part 2: Restaurant Search
GOOGLE_MAPS_URL = "https://maps.google.com"

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
SCREENSHOT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots")

# Ensure directories exist
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(SCREENSHOT_DIR, exist_ok=True)
