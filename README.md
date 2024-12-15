# tinyWeather
tinyWeather is designed to be a lightweight weather app for Linux. It is extremely limited in scope. When ran, it will:
- Use your IP address to find your approximate location and call the NWS API
- Show a popup notification telling you the high and low temperatures for today, as well as the presence of storms including rain, snow, tornados, and hurricanes
- Can be configured to use any icon for the notification by modifying source

Planned functionality:
- Get called once per day. Options for when the system is booted, at midnight or some other time, or when called from command line
- Have optional notifications for certain types of weather (maybe a hurricane should be notified differently than a thunderstorm)
- Make the process of changing icons easier than modifying source

## Getting Started
Clone this repo wherever you'd like. When you want to get a weather report, `cd` into this directory and run `python3 tinyWeather.py`. This will make a notification pop up on screen with the current weather information.\
\
To modify the icon being used in the notification, change the path of the icon being used in the subprocess to the path of the icon you wish to use.

## Contributions
This project is still in active development. Feel free to submit pull requests or request features! The ultimate goal is that after installation, you don't have to do anything except (optionally) adjust when you want alerts and what you want in them.