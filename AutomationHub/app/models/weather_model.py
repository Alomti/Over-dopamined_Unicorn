from pydantic import BaseModel

class WeatherModel(BaseModel):
    temp = float
    wind_Speed = float
    chance_of_rain = int