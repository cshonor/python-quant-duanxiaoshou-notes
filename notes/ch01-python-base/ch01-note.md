# 第 01 章学习笔记 — Python 基础

> 章节主题：（看书后填写，如：环境、语法、与量化相关的 Python 基础）  
> 日期：

---

## 一、本章知识点摘要

-

---

## 二、书本重点摘抄

-

---

## 三、自己的理解 + 通俗总结

-

---

## 四、踩坑记录 / 报错与解决

| 现象 | 原因 | 解决办法 |
|------|------|----------|
|      |      |          |

---

## 五、Demo 代码拆分讲解

（对应目录：`codes/ch01_demo/`）

- `akshare_stock_daily.py`
- 用途：演示如何在国内环境直接拉取 A 股历史日线数据。
- 说明：相比 `pandas-datareader + Yahoo Finance`，`akshare` 更适合当前入门环境，通常不需要额外代理。
- 运行：`python codes/ch01_demo/akshare_stock_daily.py`

- `tushare_daily.py`
- 用途：使用 `tushare` 获取 A 股日线数据（更贴合国内数据生态）。
- 准备：先注册 Tushare 并获取 token，建议设置为环境变量 `TUSHARE_TOKEN`。
- 运行：`$env:TUSHARE_TOKEN="你的token"; python codes/ch01_demo/tushare_daily.py`

---

## 六、延伸与待办（可选）

-
