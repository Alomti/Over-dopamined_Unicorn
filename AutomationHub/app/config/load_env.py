from pathlib import Path
from dotenv import load_dotenv
import os
import logging
logger = logging.getLogger(__name__)

base_dir = Path(__file__).parents[2].resolve()
load_dotenv(base_dir/ '.env')

weather_KEY = os.getenv('weather_KEY')
if not weather_KEY:
    raise ValueError('Error: No value "weather_KEY in .env file')
timeout = os.getenv('timeout')
if not timeout:
    timeout = 10
else:
    timeout = int(timeout)