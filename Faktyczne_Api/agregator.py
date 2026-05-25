from api_clients.ip_client import get_ipAPI
from api_clients.weather_client import get_weatherAPI

class Agregator:
    def __init__(self, ip):
        self.ip = ip
    
    def get_ip(self):
        ip_data = get_ipAPI(self.ip)
        if ip_data['success'] == False:
            continent = city = ip_data['error']
        else:
            continent = ip_data['data']['continent']
            city = ip_data['data']['city']
        return continent, city
    
    def get_weather(self, city):
        if city == 'Error with dowlanding ip data.':
            temp_c = wind_speed = 'Can not downland weather data without localisation data.'
        else:
            weather_data = get_weatherAPI(city)
            if weather_data['success'] == False:
                if city == None:
                    temp_c = wind_speed = 'No city to get weather data'
                else:
                    temp_c = wind_speed = weather_data['error']
            else:
                temp_c = weather_data['data']['temp']
                wind_speed = weather_data['data']['wind']
        return temp_c, wind_speed

    def __str__(self):
        continent, city = self.get_ip()
        temp, windspeed = self.get_weather(city)
        return f'Continent: {continent}, City: {city}, Temp: {temp}, Windspeed: {windspeed}'
