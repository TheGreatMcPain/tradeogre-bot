#!/usr/bin/env python
import requests, os


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


# Get the BTC value of a crypto
def get_price_btc(markets, currency: str):
    for market in markets:
        if "LTC-{}".format(currency.upper()) in market.keys():
            return market["LTC-{}".format(currency.upper())]

    for market in markets:
        if "BTC-{}".format(currency.upper()) in market.keys():
            return market["BTC-{}".format(currency.upper())]

    return None


markets = requests.get("https://tradeogre.com/api/v1/markets").json()

print(get_price_btc(markets, "TRTL"))
