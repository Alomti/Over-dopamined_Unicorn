import requests
import os
from dotenv import load_dotenv
def get_weatherAPI(localization):
    try:
        load_dotenv()
    except FileNotFoundError:
        print('Error: Missing file ".env" in project directory')
    except ValueError as e:
        print(f'Syntax error in .env at line {e}')
    try:
        key = os.getenv('WEATHER_API_KEY')
        if not key:
            raise ValueError('Missing value "WEATHER_API_KEY" in .env')
        base_url = 'https://api.weatherapi.com/v1/current.json?'
        params = {
            'key': key,
            'q': localization,
            'aqi': 'yes'
        }

        conn = requests.get(base_url, params)
        conn.raise_for_status()
        data = conn.json()
        return {
            'success': True,
            'data': {
                'temp': data['current']['temp_c'],
                'wind': data['current']['wind_kph']
                }
        }
    except ValueError as e:
        return {
            'success': False,
            'error': str(e)
        }
    except (KeyError, IndexError) as e:
        return {
            'success': False,
            'error': f'Error processing data: {e}'
        }
    except requests.exceptions.RequestException as e:
        return {
            'success': False,
            'error': f'An error occurred: {e}'
        }
    except Exception:
        return {
            'success': False,
            'error': 'Unknown error'
        }