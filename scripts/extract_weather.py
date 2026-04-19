import requests

def fetch_weather_data():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": -26.2041,
        "longitude": 28.0473,
        "current_weather": True
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception("Failed to fetch weather data")

    return response.json()