import alpaca_trade_api as tradeapi
import time
import os 
import config



api = tradeapi.REST(config.api_key, config.api_secret, config.api_endpoint, api_version='v2')
account = api.get_account()
