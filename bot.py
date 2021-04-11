#!/usr/bin/env python
import discord, json, asyncio, requests, os
from discord.ext.commands import Bot

client = Bot(command_prefix="!")


# Get the USD (USDT) value of BTC or LTC
def calulate_USDT(markets, currency):
    # Get the current USDT-BTC and BTC-LTC prices
    for market in markets:
        if "USDT-BTC" in market.keys():
            price_usdt_btc = float(market['USDT-BTC']['price'])

        if "BTC-LTC" in market.keys():
            price_btc_ltc = float(market['BTC-LTC']['price'])

    if currency == "LTC":
        return price_usdt_btc * price_btc_ltc
    else:
        return price_usdt_btc


@client.event
async def on_ready():
    print("Logged in")
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name="Shrek 2"))


@client.command(help="Displays the current/high/low price of a ticker.")
#Tradeogre prices
async def price(ctx, currency: str, crypto: str, multiplier: float = 1):

    input1 = currency.upper()
    input2 = crypto.upper()
    ticker = "{}-{}".format(input1, input2)

    # Get market data from TradeOgre
    url = "https://tradeogre.com/api/v1/markets"
    response = requests.get(url)
    markets = response.json()

    # Search the markets for the specified ticker.
    data = None
    for market in markets:
        if ticker in market.keys():
            data = market[ticker]
            break

    # If we can't find the ticker, exit.
    if not data:
        await ctx.send("Not a supported currency pair")
        return

    # Get prices and multiply them with 'multiplier'
    price_data = float(data['price']) * multiplier
    high_data = float(data['high']) * multiplier
    low_data = float(data['low']) * multiplier

    # Get the est. USD price as well.
    price_usdt = calulate_USDT(markets, input1) * float(
        data['price']) * multiplier

    # Convert each value to a string
    # 'str() will use scientific notation on really low values.'
    price_data = "{:.8f}".format(price_data)
    high_data = "{:.8f}".format(high_data)
    low_data = "{:.8f}".format(low_data)
    price_usdt = "{:.8f}".format(price_usdt)

    finalString = "Multiplier: " + str(multiplier) + '\n'
    finalString += "Current Price ({}): ".format(input1) + price_data + '\n'
    finalString += "24hr High ({}): ".format(input1) + high_data + '\n'
    finalString += "24hr Low ({}): ".format(input1) + low_data + '\n'

    if currency != "USDT":
        finalString += "\nEst. USD (USDT): " + price_usdt

    embed = discord.Embed(title='{}-{}'.format(input1, input2),
                          description=finalString,
                          color=0x00ff00)

    await ctx.send(embed=embed)


@client.command(help="Displays donation addresses")
async def donate(ctx):
    addresses = "ZONiiX's (original author) "
    addresses += "BTC: 3CuYbCWtKdW6PqZHHF1oJjpmeX5Ddp6SrV\n\n"
    addresses += "TheGreatMcPain's (author of this fork): "
    addresses += "See: https://github.com/TheGreatMcPain"

    embed = discord.Embed(title="Donation addresses",
                          description=addresses,
                          color=0xff6666)

    await ctx.send(embed=embed)


@client.command(help="Checks if tradeogre is online")
async def online(ctx):
    response = requests.get("https://tradeogre.com/api/v1/markets")
    if response.ok:
        await ctx.send("Tradeogre is online.")
    else:
        await ctx.send("Tradeogre is offline.")


client.run(os.environ.get('TOKEN', None))
