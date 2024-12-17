if [ -f tinyWeather.py ]
then
	mv tinyWeather.py /usr/local/bin && chmod -x /usr/local/bin/tinyWeather.py
	sudo mv -t /etc/systemd/user/ tinyWeather.service tinyWeather.timer
	systemctl --user daemon-reload && systemctl --user start tinyWeather.timer
else
	echo "you already ran setup!"
fi
