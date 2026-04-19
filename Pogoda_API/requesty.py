import requests
import unicodedata
import json
from datetime import datetime
from pathlib import Path
APIkey = '8a65fbf5e5b34f3cafc180341261104'
plik = Path(__file__).parent / 'weather_history.json'

def load_data():
    if not plik.exists():
        return []
    else:
        try:
            with open(plik, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data
        except json.JSONDecodeError:
            return []
def save_data(data):
    with open(plik, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
history_of_weather = load_data()

def sort_history():
    history_of_weather.sort(key=lambda x: x['date'])

def history_limit():
    if len(history_of_weather) > 10:
        del history_of_weather[0]

def show_history():
    for d in history_of_weather:
        print("")
        print(f"Name: {d['name']}")
        print(f"Country: {d['country']}")
        print(f"Temperature: {d['temp']}")
        print(f"Wind speed: {d['windspeed']}")
        print(f"Date: {d['date']}")
        print("")

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
        data_to_history = {
            'name': data['location']['name'],
            'country': data['location']['country'],
            'temp': data['current']['temp_c'],
            'windspeed': data['current']['wind_kph'],
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
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


while True:
    print("")
    try:
        choice = int(input(
            'Choose option:\n'
            '1-Show weather in location\n'
            '2-Show your history\n'
            '3-exit'
            ))
    except ValueError:
        print("")
        print('Invalid option. Please choose number between 1-3')
        continue
    if choice not in [1, 2, 3]:
        print("")
        print('Invalid option. Please choose number between 1-3')
        continue
    elif choice == 1:
            location = input("Enter a location: ")
            print("")
            get_locations(location)
    elif choice == 2:
        show_history()
    else:
        break