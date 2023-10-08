import json
import requests
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
api_key = 'heAj6AFoMcyzpysHedRbzXUSyfHXIN0IneGHJWF9WLL1iEjM2eWuMTxq2TVG0Jmp'
api_secret = 'FXPx83URlWTSaGVRm7Oa7uCzqhKjKEeOCGQ39zdtQWFvV4MaGJWifx3ZvtfbScOF'
client = Client(api_key, api_secret)

key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"


#------Old version-----
# data = requests.get(key)
# data = data.json()
# price = data['price']
# symbol = data['symbol']
#----------------------

# priceCoin = client.get_order_book(symbol='BTCUSDT')

class ticker:
    def __init__(self, symbol):
        self.symbol = symbol
        obj = {
            "symbol" : f"{symbol}",
            "close" : [],
            "RSIs" : [],
            
            
        }


Whitelist = ['BTCUSDT']
# prices = client.get_all_tickers()



pricesOfCoin = []

while True:
    prices = client.get_all_tickers()
    for i in prices:
        if i['symbol'] in Whitelist:
            pricesOfCoin.append(i['price'])
            print(i['symbol'], i['price'])
            
        # print(i['symbol'], i['price'])


print(price)
print(symbol)