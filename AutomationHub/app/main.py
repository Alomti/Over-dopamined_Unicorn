from fastapi import FastAPI, HTTPException
import requests
import logging
logger = logging.getLogger(__name__)
try:
    from AutomationHub.app.config.load_env import weather_KEY, timeout
except ValueError as e:
    logger.error(f'Error with geting API keys. {e}')
    raise SystemExit(1)
from AutomationHub.app.services.weather_service import get_weather
from AutomationHub.app.models.weather_model import WeatherModel, TestModel

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

@app.post('/weather/test', response_model=TestModel)
def put_out_weather(data: TestModel) -> TestModel:
    try:
        response = data
        return response
    except requests.exceptions.Timeout:
        logger.error('Timeout with WeatherApi connection')
        raise HTTPException(
            status_code=504,
            detail='To long waiting time for response from weather API'
        )
    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code
        if status_code == 500:
            logger.error(f'HTTPError code: {status_code}')
            raise HTTPException(
                status_code=503,
                detail='Weather API have internal problem beyond our influence'
            )
        elif status_code == 400:
            logger.error(f'HTTPError code: {status_code}')
            raise HTTPException(
                status_code=400,
                detail='Bad Request'
            )
        elif status_code in (401, 403):
            logger.error(f'HTTPError code: {status_code}')
            raise HTTPException(
                status_code=502,
                detail='Bad Gateway'
            )
        elif status_code == 404:
            logger.error(f'HTTPError code: {status_code}')
            raise HTTPException(
                status_code=404,
                detail='Not Found That City'
            )
        elif status_code in (429, 500, 502, 503):
            logger.error(f'HTTPError code: {status_code}')
            raise HTTPException(
                status_code=503,
                detail='Service Unavailable'
            )
    except requests.exceptions.ConnectionError as e:
        logger.error(f'Cnonection Error {e} with Weather API')
        raise HTTPException(
            status_code=503,
            detail='Failed to connect with Weather API'
        )
    except requests.exceptions.RequestException as e:
        logger.error(f'Unexpected requests error: {e}')
        raise HTTPException(
            status_code=500,
            detail='Unexpected requests error'
        )
    except Exception as e:
        logger.error(f'Unexpected error: {e}')
        raise HTTPException(
            status_code=500,
            detail='Unexpected error'
        )