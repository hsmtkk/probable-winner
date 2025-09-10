# 指示
以下処理を行うPythonスクリプト generate_stock_data_csv.py を作成せよ。

# 処理内容
「JPXデータダウンロード」「日経225銘柄一覧ダウンロード」を行う。
また「株価等情報取得」により株価等の情報を取得する。
上3つのサブ処理を結合し、以下の出力を生成する。

# 出力
stock_data.csv ファイルを生成する。
stock_data.csv ファイルは、以下の項目を含む。
- 銘柄コード string
- 銘柄名 string
- 市場区分 string
- 日経225指標採用有無 boolean
- 前日終値 int
- 平均出来高 int
- 時価総額 int
- PBR float
- PER float

# サブ処理
サブ処理はそれぞれ関数として実装せよ。

## JPXデータダウンロード
以下Webサイトに掲載の、
https://www.jpx.co.jp/markets/statistics-equities/misc/01.html
data_j.xls ファイルをダウンロードする。
data_j.xls ファイルは、以下の項目を含む。
- 銘柄コード
- 銘柄名
- 市場区分

## 日経225銘柄一覧ダウンロード
https://indexes.nikkei.co.jp/nkave/archives/file/nikkei_stock_average_weight_jp.csv
をダウンロードする。
nikkei_stock_average_weight_jp.csv ファイルは、以下の項目を含む。
- 銘柄コード

## 株価等情報取得
yfinanceライブラリを使用する。
使用例は以下を参考とせよ。
https://ranaroussi.github.io/yfinance/
https://financialmarkets.hatenablog.com/entry/2024/06/26/165744

なおTickersは複数のシンボルを受け入れられる。
```
tickers = yf.Tickers('1234.T 5678.T')
```

処理高速化のため、できるかぎり多くのシンボルをまとめて実行せよ。
ただし上限は100件とする。

# コーディング
エラー処理は不要である。
正常系のみ考慮せよ。

# 外部ライブラリ
yfinance
pandas
を使用する。
ライブラリはインストール済みのため、インストール処理は不要である。

# 実行
uvを使う。
uv run script.py
のように実行せよ。
