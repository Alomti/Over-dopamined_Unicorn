from fastapi import FastAPI, HTTPException
import httpx
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
async def put_out_weather(city: str) -> WeatherModel:
    try:
        result = await get_weather(weather_KEY, city, timeout)
        model = WeatherModel(**result)
    except httpx.TimeoutException:
        logger.error('Timeout with WeatherApi connection')
        raise HTTPException(
            status_code=504,
            detail='To long waiting time for response from weather API'
        )
    except httpx.HTTPStatusError as e:
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
        elif status_code in (429, 502, 503):
            logger.error(f'HTTPError code: {status_code}')
            raise HTTPException(
                status_code=503,
                detail='Service Unavailable'
            )
        else:
            logger.error(f'Unexcepted error {e}')
            raise HTTPException(
                status_code=500,
                detail='Unexcepted requuests error'
            )
            
    except httpx.ConnectError as e:
        logger.error(f'Cnonection Error {e} with Weather API')
        raise HTTPException(
            status_code=503,
            detail='Failed to connect with Weather API'
        )
    except httpx.RequestError as e:
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
    return model

@app.post('/weather/test', response_model=TestModel)
def put_out_weather(data: TestModel) -> TestModel:
    try:
        response = data
        return response
    except Exception as e:
        logger.error(f'Unexpected error: {e}')
        raise HTTPException(
            status_code=500,
            detail='Unexpected error'
        )