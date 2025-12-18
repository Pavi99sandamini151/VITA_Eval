import os
from dotenv import load_dotenv

load_dotenv()  # loads .env from project root

GOOGLE_API_KEY = "AIzaSyAmybAXRfuglyKjyzfjLlV5qWSSwUY6W8k"

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is missing")
