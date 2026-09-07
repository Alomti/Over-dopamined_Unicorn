from dotenv import load_dotenv
import os
import logging
logger = logging.getLogger(__name__)
load_dotenv()

weather_KEY = os.getenv('weather_KEY')
if not weather_KEY:
    raise ValueError('Error: No value "weather_KEY in .env file')
timeout = int(os.getenv('timeout'))
if not timeout:
    timeout = 10