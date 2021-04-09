# TradeOgre Discord Bot

The TradeOgre Discord Bot is meant for people who want to know price data for certain currency pairs without having to leave their comfortable Discord server.

[Invite Link](https://discord.com/api/oauth2/authorize?client_id=829825884243492905&permissions=0&scope=bot)

(Until I can figure out how to run this off a cloud service, I'm going to be running this off my RPI3B+, so be gentle.)

## Commands

- !price {BTC/LTC} {TICKER} {MULTIPLIER} - gets current price data including: high, low and current price.
- !donate - shows devleoper BTC address.
- !online - checks if TradeOgre is online.

## Local Setup

1. I recommend setting up a python virtual environment first.

```
$ python -m venv virtualenv
```

2. Install dependencies via pip

```
$ pip install -r requirements.txt
```

3. Run the bot

```
$ TOKEN="<your bot token>" ./bot.py
```

# below is from the original readme

## Message from Tron

Hey everyone! I'm 17 and I'm extremley interested in the world of Programming, Computer Science, and Blockchain technologies. I came to this project with an open mind, ready to see how my prior programming skills fared in terms of making a fully functional Discord Bot, which I previously had only done once before. If you want to use this app then I highly recommend you use [this link](https://discordapp.com/api/oauth2/authorize?client_id=521134829216071730&permissions=0&scope=bot) to invite the Discord bot to your server and start using it. If you have any feature suggestions then feel free to shoot me an email at tron.schell@protonmail.com.
