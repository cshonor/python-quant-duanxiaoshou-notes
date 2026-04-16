# CH01 Demo

将书中第 1 章示例代码按小节保存为 `.py` 文件，运行方式在笔记 `notes/ch01-python-base/ch01-note.md` 中记录。

## 当前示例

- `akshare_stock_daily.py`：使用 `akshare` 获取 A 股日线数据的最小示例。
- `tushare_daily.py`：使用 `tushare` 获取 A 股日线数据（需要 Token）。

## 运行方式

```bash
python codes/ch01_demo/akshare_stock_daily.py
```

`tushare` 版本（建议把 token 放环境变量，避免写进代码/仓库）：

```bash
# PowerShell:
$env:TUSHARE_TOKEN="你的token"
python codes/ch01_demo/tushare_daily.py
```
