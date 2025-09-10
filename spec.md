# 要求
Pythonスクリプト generate_stock_data_csv.py を作成せよ。

# 最終成果物
stock_data.csv として保存せよ。

以下の列を含むこと。
- 銘柄コード string
- 銘柄名 string
- 市場区分 string
- 日経225構成銘柄有無 bool
- 終値 int
- 取引高 int
- 時価総額 int
- PBR float
- PER float

# 処理
「JPXデータダウンロード」サブ処理により、JPXから東証上場の銘柄一覧を取得せよ。
「日経225構成銘柄一覧ダウンロード」サブ処理により、日経225構成銘柄有無を判定せよ。
「株価等情報取得」サブ処理により、終値等の情報を取得せよ。

# サブ処理
サブ処理は関数として記述せよ。

## JPXデータダウンロード
fetch_jpx_data.py, parse_jpx_data.py を参考にせよ。
ダウンロードしたファイルは data_j.xls として保存せよ。

## 日経225構成銘柄一覧ダウンロード
get_nikkei225_code.py を参考にせよ。
ダウンロードしたファイルは nikkei_stock_average_weight_jp.csv として保存せよ。

## 株価等情報取得
get_stock_data.py を参考にせよ。
経過状況のわかるように、取得対象の銘柄コード、銘柄一覧を逐次出力せよ。

# 備考
ライブラリはインストール済みである。
よって `uv add` の処理は不要である。

Pythonスクリプトを実行する場合には `uv run script.py` のように実行せよ。
