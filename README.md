# Steam-Telegram
You can gamble or use SteamApi to check your friend's time in games

# Guide 
First of all, you need to install libraries such as: python-steam-api, pyTelegramBotAPI.
This bot was hosted on linux, so i installed them in a Python virtual environment

$ python -m venv my-tg-bot

$ my-tg-bot/bin/pip install python-steam-api

$ my-tg-bot/bin/pip install pyTelegramBotAPI

# "pipx is strongly recommended for installing applications" but "For libraries ... you should create a virtual environment yourself."

Secondly, add your Telegram Bot Token and Steam API Key to .env via

$ nano .env

or use any text editor

$ python3 bot.py

# If you want to change something, feel free to do so
['appid', 'name', 'playtime_2weeks', 'playtime_forever', 'img_icon_url', #'playtime_windows_forever', 'playtime_mac_forever', 'playtime_linux_forever', #'playtime_deck_forever']
