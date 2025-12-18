import os
from dotenv import load_dotenv

load_dotenv()  # loads .env from project root

GOOGLE_API_KEY = GOOGLE_API_KEY

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is missing")

