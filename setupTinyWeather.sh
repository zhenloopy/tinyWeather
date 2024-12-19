if [ -f tinyWeather.py ]
then
	if ! [ -d tinyWeatherDirectory ] 
	then
		ln -s "$(pwd)" tinyWeatherDirectory
	fi
	mv -t /usr/local/bin tinyWeather.py tinyWeatherDirectory
	sudo mv -t /etc/systemd/user/ tinyWeather.service tinyWeather.timer
	systemctl --user daemon-reload && systemctl --user start tinyWeather.timer

else
	echo "You already setup tinyWeather. Do you want to
a) change configuration
b) remove tinyWeather
Enter a, b, or anything else to exit."
	read setupChoice
	if [ "$setupChoice" = "a" ]
	then
		echo "TODO: SETUP CONFIG CHANGE"

	elif [ "$setupChoice" = "b" ]
	then
		sudo mv /etc/systemd/user/tinyWeather* .
		mv -t . /usr/local/bin/tinyWeather.py /usr/local/bin/tinyWeatherDirectory
		systemctl --user daemon-reload
		echo "Systemd service and timer stopped. Do you want to remove tinyWeather completely? (y/n)"
		read -r deleteChoice
		if [ "$deleteChoice" = "y" ]; then cd ..; rm -rf -- tinyWeather/
		fi

	else
		echo "Setup cancelled."
	fi
fi
