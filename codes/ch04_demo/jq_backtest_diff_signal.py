"""
聚宽回测示例：基于收盘价差分(diff)生成交易信号。

核心逻辑：
- 以“昨日收盘涨跌(diff) > 0” 作为今日开盘是否持仓的信号，避免未来函数。
- 每个交易日开盘附近调仓：信号为 1 则满仓，信号为 0 则清仓。

使用方式：
- 将本文件复制到聚宽“策略研究/回测”里直接运行。
"""

import numpy as np


def initialize(context):
    # 标的：贵州茅台
    g.security = "600519.XSHG"

    # 开盘后不久再调仓，避免开盘瞬时数据不稳定
    run_daily(trade, time="09:35")


def trade(context):
    # 取最近 3 天日线：用于计算 diff 与取“昨日信号”
    df = get_price(
        g.security,
        count=3,
        frequency="daily",
        fields=["open", "close"],
        panel=False,
    )

    if df is None or df.empty:
        return

    # Pandas diff(): 当日收盘 - 前一日收盘
    df["diff"] = df["close"].diff()

    # Signal: diff > 0 -> 1 else 0
    df["signal"] = np.where(df["diff"] > 0, 1, 0)

    # 避免未来函数：用“昨日收盘生成的信号”决定“今日开盘是否持仓”
    if len(df) < 2:
        return
    signal_yesterday = int(df["signal"].iloc[-2])

    if signal_yesterday == 1:
        order_target_percent(g.security, 1.0)
    else:
        order_target_percent(g.security, 0.0)

    # 可选：调试输出（回测日志里看）
    log.info(
        "signal_yesterday=%s, close_yesterday=%.2f, close_today=%.2f",
        signal_yesterday,
        float(df["close"].iloc[-2]),
        float(df["close"].iloc[-1]),
    )

