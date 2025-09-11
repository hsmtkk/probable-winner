import pandas
import yfinance

BATCH_SIZE = 100


def main():
    input_file = "../jpx_nikkei225_join/jpx_nikkei225_data.csv"
    output_file = "stock_price_data.csv"

    df = pandas.read_csv(input_file, encoding="utf-8")

    stock_codes = df["銘柄コード"].astype(str).tolist()
    total_count = len(stock_codes)

    for i in range(0, total_count, BATCH_SIZE):
        start = i
        end = i + BATCH_SIZE
        print(f"processing {start} ~ {end} / {total_count}")
        ticker_symbols = map(lambda t: t + ".T", stock_codes[i : i + BATCH_SIZE])
        ticker_symbols = " ".join(ticker_symbols)
        tickers = yfinance.Tickers(ticker_symbols)
        for t in tickers.tickers:
            info = tickers.tickers[t].info
            previous_close = int(info.get("previousClose", 0))
            market_cap = int(info.get("marketCap", 0))
            average_volume = int(info.get("averageVolume", 0))
            pbr = float(info.get("priceToBook", 0))
            per = float(info.get("trailingPE", 0))
            stock_code = t.replace(".T", "")
            df.loc[df["銘柄コード"] == stock_code, ["前日終値"]] = previous_close
            df.loc[df["銘柄コード"] == stock_code, ["時価総額"]] = market_cap
            df.loc[df["銘柄コード"] == stock_code, ["平均取引量"]] = average_volume
            df.loc[df["銘柄コード"] == stock_code, ["PBR"]] = pbr
            df.loc[df["銘柄コード"] == stock_code, ["PER"]] = per

    df.to_csv(output_file, index=False, encoding="utf-8")


if __name__ == "__main__":
    main()
