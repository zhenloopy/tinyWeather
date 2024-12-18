if [ -f tinyWeather.py ]
then
	mv tinyWeather.py /usr/local/bin && chmod -x /usr/local/bin/tinyWeather.py
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
		mv /usr/local/bin/tinyWeather.py .
		sudo mv /etc/systemd/user/tinyWeather* .
		systemctl --user daemon-reload
		echo "Systemd service and timer stopped. Do you want to remove tinyWeather completely? (y/n)"
		read deleteChoice
		if [ "$deleteChoice" = "y" ]; then cd ..; rm -rf -- tinyWeather/
		fi
	else
		echo "Setup cancelled."
	fi
fi
