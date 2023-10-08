from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
api_key = 'heAj6AFoMcyzpysHedRbzXUSyfHXIN0IneGHJWF9WLL1iEjM2eWuMTxq2TVG0Jmp'
api_secret = 'FXPx83URlWTSaGVRm7Oa7uCzqhKjKEeOCGQ39zdtQWFvV4MaGJWifx3ZvtfbScOF'
client = Client(api_key, api_secret)


priceCoin = client.get_order_book(symbol='BTCUSDT')
prices = client.get_all_tickers()

print(priceCoin)
# get market depth
prices = client.get_all_tickers()

for i in prices:
    print(i)