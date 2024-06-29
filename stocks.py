import robin_stocks.robinhood as r
from webull import webull
from datetime import datetime, timedelta
from discord import SyncWebhook
import pandas as pd
import json, time
import pytz
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

def discord_message(messages):
    webhook_url = config['credentials']['WEBHOOK']
    if webhook_url == None:
        return
    webhook = SyncWebhook.from_url(url=webhook_url)
    webhook.send(content=f"```{messages}```")


def rh_login():
    """
    Robinhood Login:
    username: "Your Username" - Most likely your email
    password: "Your Robinhood password to login"

    """
    user = config['credentials']['USERNAME']
    password = config['credentials']['PASSWORD']
    login = r.authentication.login(username=user, password=password, expiresIn=None, scope='internal', by_sms=True, store_session=True, mfa_code=None, pickle_name='')
    if login.get('access_token'):
        print("Good to go! Logged into Robinhood")
        pass


def stock_limit_order(symbol,quantity,limitPrice,exHours,ac):
    orders = r.orders.order_buy_limit(symbol, quantity, limitPrice, account_number=ac, timeInForce='gtc', extendedHours=exHours, jsonify=True)
    print(orders)