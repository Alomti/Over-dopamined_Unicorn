import httpx

async def get_weather(key, city, timeout):
    url = 'https://api.weatherapi.com/v1/current.json'
    params = {'key': key, 'q': city}
    async with httpx.AsyncClient() as client:
        response = await client.get(url , params=params, timeout=timeout)
        response.raise_for_status()
        raw = response.json()
    weather = {
        'temp': raw['current']['temp_c'],
        'wind_Speed': raw['current']['wind_kph'],
        'chance_of_rain': raw['current']['will_it_rain']
        }
    return weather

