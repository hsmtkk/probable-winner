# 指示
以下処理を行うPythonスクリプト stock_price_get.py を作成せよ。

# 処理内容
1. jpx_nikkei225_data.csv ファイルを読み込む。
2. 下記の出力のとおり、各行に前日終値や時価総額などの株価関連情報を付与する。
3. stock_price_data.csv ファイルに書き込む。

## yfinanceの処理に関する指定
yfinance Tickersは複数の銘柄コードを引数にとれる。
処理の高速化のため、100件以内のできるだけ多くの銘柄コードをまとめて、処理を行うこと。
(例)銘柄コードが250件ある場合、100, 100, 50件とまとめる。

(例)
```
tickers = yfinace.Tickers("1234 5678")
```

## 進捗状況の表示
ループ1回ごとに進捗状況を表示せよ。

# 入力
../jpx_nikkei225_join/jpx_nikkei225_data.csv

# 出力
ファイル名 stock_price_data.csv
文字エンコーディング UTF-8
ヘッダ行 あり

列
- 銘柄コード string
- 銘柄名 string
- 市場区分 string
- 日経225採否 boolean
- 前日終値 int
- 時価総額 int
- 平均取引量 int
- PBR float
- PER float

# 参考とするウェブサイト
https://ranaroussi.github.io/yfinance/
https://financialmarkets.hatenablog.com/entry/2024/06/26/165744

# 共通仕様
../common.md を参照せよ。
