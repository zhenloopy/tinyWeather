# tinyWeather
tinyWeather is designed to be a lightweight weather app for Linux. It is extremely limited in scope. When ran, it will:
- Use your IP address to find your approximate location and call the NWS API
- Show a popup notification telling you the high and low temperatures for today, as well as the presence of storms including rain, snow, tornados, and hurricanes
- Can be configured to use any icon for the notification by replacing the image currently in the directory (has to be the same name!)
- Systemd timer is set up to run on boot and once a day at midnight (this is why sudo is required)
- Setup script both automates setting up, stopping, and removing the program

Planned functionality:
- Have optional notifications for certain types of weather (maybe a hurricane should be notified differently than a thunderstorm)
- Make the process of changing icons easier 

## Getting Started
Clone this repo wherever you'd like. To set up the program, run `bash setupTinyWeather.sh` or your shell equivalent from this repo. It will set up a systemd timer that gets a weather report once per day at midnight.\
This script should be POSIX-compatible, but my experience is limited so if this program doesn't work on your shell, create an issue with details and I'll work on it!\

## Configuration
To modify the icon being used in the notification, replace the default `weathericon.png` with another png of your choice. This png must also be named "weathericon.png", otherwise it won't be recognized.

## Removing tinyWeather
To remove tinyWeather, run `bash setupTinyWeather.sh` again. This time, choose option `b` (option `a` is still a work in progress). This will stop the systemd timer. Then, you can choose whether or not you want to delete the repo completely. If you accidentally stop the program when you don't want to, simply run `bash setupTinyWeather.sh` again to reinstate the timer!

## Contributions
This project is still in active development. Feel free to submit pull requests or request features! The ultimate goal is that after installation, you don't have to do anything except run the setup program.
