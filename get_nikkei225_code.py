import urllib.request

import pandas

CSV_URL = "https://indexes.nikkei.co.jp/nkave/archives/file/nikkei_stock_average_weight_jp.csv"

req = urllib.request.Request(CSV_URL)
req.add_header("User-Agent", "dummy")

with urllib.request.urlopen(req) as f:
    with open("nikkei_stock_average_weight_jp.csv", "wb") as g:
        g.write(f.read())

df = pandas.read_csv("nikkei_stock_average_weight_jp.csv", encoding="shift_jis")
print(df[["コード"]])
