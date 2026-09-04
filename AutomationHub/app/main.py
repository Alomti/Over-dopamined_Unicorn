from fastapi import FastAPI
import requests
import logging
logger = logging.getLogger(__name__)
try:
    from AutomationHub.app.config.settings import weather_KEY, timeout
except ValueError as e:
    logger.error(f'Error with geting API keys. {e}')
    raise SystemExit(1)
from AutomationHub.app.services.weather_service import get_weather
from AutomationHub.app.models.weather_model import WeatherModel

app = FastAPI()

print('Backend starting...')

@app.get('/weather', response_model=WeatherModel)
def put_out_weather(city: str) -> WeatherModel:
    try:
        result = get_weather(weather_KEY, city, timeout)
        model = WeatherModel(**result)
    except requests.exceptions.ConnectionError as e:
        logger.error(f"Server connection error for weather: {e}")
        return {'To co jeszcze do ustalenia typ ale you know that i know gdzie to umieścić'}
    except requests.exceptions.Timeout as e:
        logger.error(f"Response timeout for weather: {e}")
    except requests.exceptions.HTTPError as e:
        logger.error(f"Server returned an HTTP error for weather: {e}")
    except requests.exceptions.JSONDecodeError as e:
        logger.error(f"The response from weather is not a valid JSON format: {e}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Unexcepted error requests for weather: {e}")
    return model
