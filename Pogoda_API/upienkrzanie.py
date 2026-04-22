from dotenv import load_dotenv
import os
import requests
import unicodedata
from datetime import datetime, timedelta
from obsluga_json import load_data, save_data, WeatherHistory
load_dotenv()

APIkey = os.getenv('WEATHER_API_KEY')
if not APIkey:
    raise ValueError("Missing WEATHER_API_KEY in .env")

class Weather_Manager():
    def __init__(self):
        self.history_of_weather = load_data()
    
    def usun_polskie_znaki(self, text):
        return unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('ascii')

    def sort_history(self):
        self.history_of_weather.sort(key=lambda x: x.date)

    def sort_by_lastthreedays(self):
        three_days_ago = datetime.now() - timedelta(days=3)
        self.history_of_weather = [i for i in self.history_of_weather if datetime.strptime(i.date, '%Y-%m-%d %H:%M:%S') >= three_days_ago]
    
    def sort_by_city(self, city):
        self.history_of_weather = [i for i in self.history_of_weather if i.name.lower() == city.lower()]

    def history_limit(self):
        if len(self.history_of_weather) > 10:
            del self.history_of_weather[0]
    
    def __str__(self):
        return "\n\n".join(str(x) for x in self.history_of_weather)

weather_manager = Weather_Manager()
def get_locations(city):
    city = weather_manager.usun_polskie_znaki(city)
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
        weather_manager.history_of_weather.append(data_to_history)
        weather_manager.sort_history()
        weather_manager.history_limit()
        save_data(weather_manager.history_of_weather)
        return data_to_history
    except (KeyError, IndexError) as e:
        print(f"Error processing data: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None