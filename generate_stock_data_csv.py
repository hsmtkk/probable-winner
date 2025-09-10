import re
import time
import urllib.request
import pandas
import yfinance


def fetch_and_parse_jpx_data():
    """
    JPXから東証上場の銘柄一覧を取得し、DataFrameとして返す
    """
    print("JPXデータを取得しています...")
    # JPXのページからExcelファイルのリンクを取得
    jpx_base_url = "https://www.jpx.co.jp"
    jpx_page_url = jpx_base_url + "/markets/statistics-equities/misc/01.html"
    with urllib.request.urlopen(jpx_page_url) as f:
        html_content = f.read().decode("utf-8")

    match = re.search(r'<a href="([^"]*data_j.xls)"', html_content)
    link_suffix = match.group(1)
    xls_link = jpx_base_url + link_suffix

    # Excelファイルをダウンロード
    xls_filename = "data_j.xls"
    with urllib.request.urlopen(xls_link) as f:
        with open(xls_filename, "wb") as g:
            g.write(f.read())

    # ダウンロードしたExcelをパース
    df = pandas.read_excel(xls_filename)
    selected_columns = df[["コード", "銘柄名", "市場・商品区分"]]

    filter_values = [
        "プライム（内国株式）",
        "スタンダード（内国株式）",
        "グロース（内国株式）",
    ]
    filtered_df = selected_columns[
        selected_columns["市場・商品区分"].isin(filter_values)
    ].copy()
    print("JPXデータの取得が完了しました。")
    return filtered_df[["コード", "銘柄名", "市場・商品区分"]]


def get_nikkei225_codes():
    """
    日経225構成銘柄のコード一覧をセットとして返す
    """
    print("日経225構成銘柄の情報を取得しています...")
    csv_url = "https://indexes.nikkei.co.jp/nkave/archives/file/nikkei_stock_average_weight_jp.csv"
    csv_filename = "nikkei_stock_average_weight_jp.csv"
    req = urllib.request.Request(csv_url, headers={"User-Agent": "dummy"})
    with urllib.request.urlopen(req) as f:
        with open(csv_filename, "wb") as g:
            g.write(f.read())
    df = pandas.read_csv(csv_filename, encoding="shift_jis")
    print("日経225構成銘柄の取得が完了しました。")
    return set(df["コード"])


def get_stock_info(ticker_code):
    """
    銘柄コードから株価情報を取得する
    """
    ticker_symbol = f"{ticker_code}.T"
    data = yfinance.Ticker(ticker_symbol)
    info = data.info
    return {
        "終値": int(info.get("regularMarketPrice", 0)),
        "取引高": int(info.get("regularMarketVolume", 0)),
        "時価総額": int(info.get("marketCap", 0)),
        "PBR": float(info.get("priceToBook", 0.0)),
        "PER": float(info.get("trailingPE", 0.0)),
    }


def main():
    """
    メイン処理
    """
    jpx_stocks = fetch_and_parse_jpx_data()
    nikkei225_codes = get_nikkei225_codes()

    all_stock_data = []
    total_stocks = len(jpx_stocks)

    index = 0
    for _, row in jpx_stocks.iterrows():
        index += 1
        code = row["コード"]
        name = row["銘柄名"]

        print(
            f"({index}/{total_stocks}) 銘柄コード: {code}, 銘柄名: {name} の情報を取得中..."
        )

        stock_info = get_stock_info(code)
        is_nikkei225 = code in nikkei225_codes
        all_stock_data.append(
            {
                "銘柄コード": str(code),
                "銘柄名": name,
                "日経225構成銘柄有無": is_nikkei225,
                **stock_info,
            }
        )

        time.sleep(1)

    # DataFrameを作成してCSVに保存
    output_df = pandas.DataFrame(all_stock_data)
    output_filename = "stock_data.csv"
    output_df.to_csv(output_filename, index=False, encoding="utf-8")
    print(f"処理が完了しました。{output_filename} にデータを保存しました。")


if __name__ == "__main__":
    main()
