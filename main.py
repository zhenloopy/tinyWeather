import requests
import json


def getWeatherData():
    url = "https://api.weather.gov/gridpoints/HGX/28,135/forecast"
    r = requests.get(url, headers={"User-Agent": "(abcdeTinyWeather.1.1.0, testemail@gmail.com)"}).json()

    todayForecast = r["properties"]["periods"][0]["detailedForecast"]
    keywords = ["storm", "rain"]

    if any([x in todayForecast for x in keywords]):
        print("rain")
    else:
        print("clear")



getWeatherData()