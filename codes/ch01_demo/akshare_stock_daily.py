import akshare as ak


def main():
    # 以贵州茅台为例，拉取前复权日线数据。
    df = ak.stock_zh_a_hist(
        symbol="600519",
        period="daily",
        start_date="20200101",
        end_date="20250101",
        adjust="qfq",
    )

    print("贵州茅台日线数据预览:")
    print(df.head())


if __name__ == "__main__":
    main()
