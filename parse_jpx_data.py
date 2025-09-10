import pandas

df = pandas.read_excel("./data_j.xls")
selected_columns = df[["コード", "銘柄名", "市場・商品区分"]]

filter_values = [
    "プライム（内国株式）",
    "スタンダード（内国株式）",
    "グロース（内国株式）",
]
filtered_df = selected_columns[selected_columns["市場・商品区分"].isin(filter_values)]

filtered_df.to_csv("./common_stock.csv", index=False)
