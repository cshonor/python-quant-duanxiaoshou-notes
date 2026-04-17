"""
聚宽 JQData：贵州茅台（600519）当日日线 + 当年全部日 K。

账号密码请用环境变量传入，勿写进代码或提交到仓库。
"""

import datetime
import os

from jqdatasdk import auth, get_price, logout


def main():
    user = os.getenv("JQ_USERNAME")
    password = os.getenv("JQ_PASSWORD")
    if not user or not password:
        raise SystemExit(
            "未检测到环境变量 JQ_USERNAME / JQ_PASSWORD。\n"
            "PowerShell 示例：\n"
            '  $env:JQ_USERNAME="你的聚宽账号"\n'
            '  $env:JQ_PASSWORD="你的密码"\n'
            "  python codes/ch01_demo/jqdata_maotai.py"
        )

    auth(user, password)

    code = "600519.XSHG"
    today = datetime.date.today().strftime("%Y-%m-%d")
    year = datetime.date.today().year

    try:
        price_today = get_price(
            security=code,
            start_date=today,
            end_date=today,
            frequency="daily",
        )
        print("===== 贵州茅台 当日日K（若为非交易日可能为空）=====")
        print(price_today)

        start_year = f"{year}-01-01"
        df_year = get_price(
            security=code,
            start_date=start_year,
            end_date=today,
            frequency="daily",
        )
        # Pandas: diff() / pct_change() 计算涨跌额与涨跌幅
        if "close" in df_year.columns:
            df_year["diff_close"] = df_year["close"].diff()
            df_year["pct_close"] = df_year["close"].pct_change()

        print("\n===== 贵州茅台 当年所有日K（含 diff/pct） =====")
        show_cols = [c for c in ["open", "close", "high", "low", "volume", "money", "diff_close", "pct_close"] if c in df_year.columns]
        print(df_year[show_cols].tail(10) if show_cols else df_year.tail(10))
    finally:
        logout()


if __name__ == "__main__":
    main()
