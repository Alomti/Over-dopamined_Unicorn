from dotenv import load_dotenv
import os
import requests
import unicodedata
from datetime import datetime
from obsluga_json import load_data, save_data, WeatherHistory
load_dotenv()
APIkey = os.getenv('WEATHER_API_KEY')
history_of_weather = load_data()

def sort_history():
    history_of_weather.sort(key=lambda x: x.date)

def history_limit():
    if len(history_of_weather) > 10:
        del history_of_weather[0]

def show_history():
    print(history_of_weather)

def usun_polskie_znaki(text):
    return unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('ascii')
def get_locations(city):
    city = usun_polskie_znaki(city)
    try:
        url = f'https://api.weatherapi.com/v1/current.json'
        parametry = {'key': APIkey, 'q': city}
        response = requests.get(url, params=parametry, timeout=7)
        response.raise_for_status()
        data = response.json()
        data_to_history = WeatherHistory(
            name=data['location']['name'],
            country=data['location']['country'],
            temp=data['current']['temp_c'],
            windspeed=data['current']['wind_kph'],
            date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
        print(
            f"Place: {data['location']['name']}\n"
            f"Country: {data['location']['country']}\n"
            f"Temperature: {data['current']['temp_c']} Celsius\n"
            f"windspeed: {data['current']['wind_kph']}KPH"
            )
        history_of_weather.append(data_to_history)
        sort_history()
        history_limit()
        save_data(history_of_weather)
        return data_to_history
    except (KeyError, IndexError) as e:
        print(f"Error processing data: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None