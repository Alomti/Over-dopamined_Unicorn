import json
from pathlib import Path
plik = Path(__file__).parent / 'weather_history.json'
if not plik.exists():
    plik.touch()

class WeatherHistory:
    def __init__(self, name, country, temp, windspeed, date):
        self.name = name
        self.country = country
        self.temp = temp
        self.windspeed = windspeed
        self.date = date

    def to_dict(self):
        return {
            'name': self.name,
            'country': self.country,
            'temp': self.temp,
            'windspeed': self.windspeed,
            'date': self.date
        }

    def __str__(self):
        return f"Name: {self.name}\nCountry: {self.country}\nTemperature: {self.temp}\nWind speed: {self.windspeed}\nDate: {self.date}"

def load_data():
    if not plik.exists():
        return []
    else:
        try:
            with open(plik, 'r', encoding='utf-8') as f:
                raw = json.load(f)
                data = [WeatherHistory(name=r['name'], country=r['country'], temp=r['temp'], windspeed=r['windspeed'], date=r['date']) for r in raw]
                return data
        except json.JSONDecodeError:
            return []
def save_data(data):
    formated_data = [d.to_dict() for d in data]
    with open(plik, 'w', encoding='utf-8') as f:
        json.dump(formated_data, f, ensure_ascii=False, indent=4)
        

history = load_data()
print(history)