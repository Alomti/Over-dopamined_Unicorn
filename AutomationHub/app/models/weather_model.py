from pydantic import BaseModel

class WeatherModel(BaseModel):
    temp: float
    wind_Speed: float
    chance_of_rain: int

class HistoryModel(BaseModel):
    history: list

class AddWeather(BaseModel):
    city: str
    temp: float
    wind_Speed: float

class AddResponse(BaseModel):
    message: str