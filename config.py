import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read values from environment
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Custom config values
SYMBOL = "BTCUSDT"
INTERVAL = "3m"  # Can be '1m', '3m', '5m', etc.

# Optional: Raise error if credentials are missing
if not API_KEY or not API_SECRET:
    raise Exception("Binance API credentials are missing. Check your .env file.")
