# 指示
以下処理を行うPythonスクリプト jpx_nikkei225_join.py を作成せよ。

# 入力
jpx_download/jpx_data.csv ファイル
nikkei225_download/nikkei225_data.csv ファイル

# 処理内容
jpx_data.csv ファイルに「日経225採否」の列を加える。
nikkei225_data.csv に銘柄コードのある場合、「日経225採否」は真である。
ない場合、「日経225採否」は偽である。

# 出力
ファイル名 jpx_nikkei225_data.csv 
文字エンコーディング UTF-8
ヘッダ行 あり

列
- 銘柄コード string
- 銘柄名 string
- 市場区分 string
- 日経225採否 boolean

# 共通仕様
../common.md を参照せよ。
