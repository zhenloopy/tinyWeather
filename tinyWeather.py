#!/usr/bin/env python3
import requests
import subprocess


def getURL():
    ip = requests.get("http://ip-api.com/json/?fields=lat,lon").json()
    url = requests.get("https://api.weather.gov/points/" + str(ip["lat"]) + "," + str(ip["lon"])).json()["properties"]["forecast"]
    return url
    

def getWeatherData(url):
    r = requests.get(url, headers={"User-Agent": "(TinyWeather.1.1.0, zhenloopy@gmail.com)"}).json()

    todayForecast = r["properties"]["periods"][0]["detailedForecast"]
    todayPrecipChance = r["properties"]["periods"][0]["probabilityOfPrecipitation"]["value"]
    todayLow = r["properties"]["periods"][1]["temperature"]
    todayHigh = r["properties"]["periods"][0]["temperature"]
    keywords = ["storm", "rain", "sleet", "snow", "tornado", "hurricane"]

    message = "Low: " + str(todayLow) + ", High: " + str(todayHigh)
    if any([x in todayForecast for x in keywords]) and todayPrecipChance != None and todayPrecipChance >= 40:
        message += ", Storms expected"
    
    subprocess.run(['env', 'DISPLAY=:0', 'notify-send', '-i', '/home/zhenloopy/tinyWeather/weathericon.png', 'Weather Alert', message, '-u', 'critical'], check=False, text=True)


url = getURL()
getWeatherData(url)
