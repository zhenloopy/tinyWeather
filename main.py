import requests
import json
import subprocess


def getWeatherData():
    url = "https://api.weather.gov/gridpoints/HGX/28,135/forecast"
    r = requests.get(url, headers={"User-Agent": "(TinyWeather.1.1.0, zhenloopy@gmail.com)"}).json()

    todayForecast = r["properties"]["periods"][0]["detailedForecast"]
    keywords = ["storm", "rain"]

    if any([x in todayForecast for x in keywords]):
        subprocess.run(['notify-send', '-i', '/home/zhenloopy/tinyWeather/weathericon.png', 'Weather Alert', 'It will rain today', '-u', 'critical'], check=True, text=True)



getWeatherData()