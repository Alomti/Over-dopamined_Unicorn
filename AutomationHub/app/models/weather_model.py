from pydantic import BaseModel

class WeatherModel(BaseModel):
    temp: float
    wind_Speed: float
    chance_of_rain: int

class TestModel(BaseModel):
    city: str
    forecast: int