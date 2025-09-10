import pandas as pd


def jpx_nikkei225_join():
    jpx_data_path = "../jpx_download/jpx_data.csv"
    nikkei225_data_path = "../nikkei225_download/nikkei225_data.csv"
    output_file_path = "jpx_nikkei225_data.csv"

    df_jpx = pd.read_csv(jpx_data_path, encoding="utf-8")
    df_nikkei225 = pd.read_csv(nikkei225_data_path, encoding="utf-8")

    nikkei225_codes = set(df_nikkei225["銘柄コード"].astype(str))

    df_jpx["日経225採否"] = df_jpx["銘柄コード"].astype(str).isin(nikkei225_codes)

    output_df = df_jpx[["銘柄コード", "銘柄名", "市場区分", "日経225採否"]]

    output_df.to_csv(output_file_path, index=False, encoding="utf-8")


if __name__ == "__main__":
    jpx_nikkei225_join()
