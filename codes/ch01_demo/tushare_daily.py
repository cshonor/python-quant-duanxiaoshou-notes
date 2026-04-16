import os

import tushare as ts


def main():
    token = os.getenv("TUSHARE_TOKEN")
    if not token:
        raise SystemExit(
            "未检测到环境变量 TUSHARE_TOKEN。\n"
            "PowerShell 设置方式：\n"
            '  $env:TUSHARE_TOKEN="你的token"\n'
            "然后再运行本脚本。"
        )

    pro = ts.pro_api(token)

    # 以贵州茅台为例
    df = pro.daily(ts_code="600519.SH", start_date="20200101", end_date="20250101")

    print("贵州茅台日线数据预览:")
    print(df.head())


if __name__ == "__main__":
    main()
