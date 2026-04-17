"""
JQData 本地可视化示例：收盘价曲线 + diff 信号标记。

说明：
- 信号用“昨日收盘 diff”生成，避免未来函数：signal_today = (diff.shift(1) > 0)
- 图上标记的是“信号出现的日期对应的收盘价位置”，不等同于真实成交价（通常次日开盘）。
"""

import datetime
import os

import matplotlib.pyplot as plt
import numpy as np
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
            "  python codes/ch01_demo/jqdata_plot_signal.py"
        )

    auth(user, password)

    code = "600519.XSHG"
    today = datetime.date.today().strftime("%Y-%m-%d")
    year = datetime.date.today().year
    start_year = f"{year}-01-01"

    try:
        df = get_price(
            security=code,
            start_date=start_year,
            end_date=today,
            frequency="daily",
            fields=["open", "close", "high", "low", "volume", "money"],
            panel=False,
        )
        if df is None or df.empty:
            raise SystemExit("拉取数据为空（可能是非交易日/权限/网络问题）。")

        df["diff"] = df["close"].diff()
        # 用昨日 diff 生成今日信号，避免未来函数
        df["signal"] = np.where(df["diff"].shift(1) > 0, 1, 0)

        plt.figure(figsize=(12, 6))
        df["close"].plot(linewidth=2, color="k", grid=True)

        # 这里延续你截图的标记含义：Signal=1 绿色倒三角；Signal=0 红色正三角
        plt.scatter(
            df["close"].loc[df.signal == 1].index,
            df["close"].loc[df.signal == 1],
            marker="v",
            s=70,
            c="g",
            label="Signal=1",
        )
        plt.scatter(
            df["close"].loc[df.signal == 0].index,
            df["close"].loc[df.signal == 0],
            marker="^",
            s=70,
            c="r",
            label="Signal=0",
        )

        plt.title("600519 贵州茅台：收盘价与 diff 信号（signal 使用 diff.shift(1)）")
        plt.legend()
        plt.tight_layout()
        plt.show()
    finally:
        logout()


if __name__ == "__main__":
    main()

