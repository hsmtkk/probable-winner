import pandas
import re
import urllib.request
import urllib.parse

URL = "https://www.jpx.co.jp/markets/statistics-equities/misc/01.html"


def jpx_download():
    with urllib.request.urlopen(URL) as response:
        html_content = response.read().decode("utf-8")

    match = re.search(r'href="([^"]*data_j\.xls)"', html_content)
    xls_path = match.group(1)
    xls_url = urllib.parse.urljoin(URL, xls_path)

    urllib.request.urlretrieve(xls_url, "data_j.xls")
    df = pandas.read_excel("data_j.xls", header=0)

    df = df[["コード", "銘柄名", "市場・商品区分"]]
    df = df.rename(
        columns={
            "コード": "銘柄コード",
            "銘柄名": "銘柄名",
            "市場・商品区分": "市場区分",
        }
    )
    df = df.dropna(subset=["銘柄コード"])

    df.to_csv("jpx_data.csv", index=False, encoding="utf-8")


if __name__ == "__main__":
    jpx_download()
