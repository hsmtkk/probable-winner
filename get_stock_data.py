import yfinance

tickers = yfinance.Tickers("1301.T 1332.T")
print(tickers)
print(tickers.tickers)

for symbol in tickers.tickers:
    t = tickers.tickers[symbol]
    info = t.info
    print(info["longName"])
# info = data.info

# long_name = info["longName"]
# short_name = info["shortName"]
# previous_close = info["previousClose"]
# average_volume = info["averageVolume"]
# market_capacity = info["marketCap"]
# pbr = info["priceToBook"]
# per = info["trailingPE"]

# print(long_name)
# print(short_name)
# print(previous_close)
# print(average_volume)
# print(market_capacity)
# print(pbr)
# print(per)
