import pandas
import urllib.request

URL_PREFIX = "https://indexes.nikkei.co.jp/nkave/archives/file/"
FILE_NAME = "nikkei_stock_average_weight_jp.csv"


def nikkei225_download():
    opener = urllib.request.build_opener()
    opener.addheaders = [("User-Agent", "dummy")]
    urllib.request.install_opener(opener)

    url = URL_PREFIX + FILE_NAME
    urllib.request.urlretrieve(url, FILE_NAME)

    df = pandas.read_csv(FILE_NAME, encoding="sjis")

    df = df[["コード", "社名"]]
    df = df.rename(columns={"コード": "銘柄コード", "社名": "銘柄名"})
    df = df.dropna()
    df["銘柄コード"] = df["銘柄コード"].astype(int)

    df.to_csv("nikkei225_data.csv", index=False, encoding="utf-8")


if __name__ == "__main__":
    nikkei225_download()
