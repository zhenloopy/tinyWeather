#!/usr/bin/env python3
import requests
import os
from shlex import split
from subprocess import run, PIPE, check_output



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

    message = "\"Low: " + str(todayLow) + ", High: " + str(todayHigh)
    if any([x in todayForecast for x in keywords]) and todayPrecipChance != None and todayPrecipChance >= 40:
        message += ", Storms expected"
    message += "\""

    with open('direct.temp', "w") as outfile:
        run(["readlink", "-f", "tinyWeatherDirectory"], stdout=outfile)

    with open('direct.temp', "r") as infile:
        fullPath = infile.readline().strip('\n')

    desktopOutput = os.environ.get('DESKTOP_SESSION')
    if (desktopOutput is not None):
        run(split("env DISPLAY=:0 notify-send -i " + fullPath + "/weathericon.png \"Weather Alert\" " + message + " -u critical"), check=False, text=True)
    else:
        print("Weather Alert: " + message)

    os.remove('direct.temp')

url = getURL()
getWeatherData(url)
