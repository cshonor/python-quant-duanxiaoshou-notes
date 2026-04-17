# JQData 与 Tushare 常用接口对照

> 说明：**聚宽 JQData**（`jqdatasdk`）与 **Tushare**（`tushare` Pro）都是「本地 Python 拉金融数据」的常见方案，但**不是同一套 API**，证券代码格式、复权方式也有差异。下表便于对照与迁移思路，具体字段以官方文档为准。

## 一、定位一句话

| 项目 | 说明 |
|------|------|
| **Tushare** | 第三方通用数据接口，需注册 token，有免费与付费权限。 |
| **JQData** | 聚宽官方数据 SDK，本地安装 `jqdatasdk`，用聚宽账号登录，有免费额度与付费扩容。 |
| **聚宽网页内置 API** | 仅在聚宽研究/回测环境内使用，无需单独装 `jqdatasdk`。 |

## 二、环境与登录

| 步骤 | JQData | Tushare（Pro） |
|------|--------|----------------|
| 安装 | `pip install jqdatasdk` | `pip install tushare` |
| 认证 | `jq.auth('账号', '密码')` | `pro = ts.pro_api('你的token')` |

## 三、常用接口对照

| 目的 | JQData（`jqdatasdk`） | Tushare（`pro`） |
|------|------------------------|------------------|
| A 股日线（含复权示例） | `get_price('000001.XSHE', start_date='...', end_date='...', frequency='daily', fq='pre')` | `pro.daily(ts_code='000001.SZ', start_date='...', end_date='...')`（日线默认不复权，复权需配合 `adj_factor` 等文档说明） |
| 股票列表 | `get_all_securities(types=['stock'])` | `pro.stock_basic(...)` |
| 指数成分股 | `get_index_stocks('000300.XSHG')` | `pro.index_weight(index_code='399300.SZ', ...)` 等（指数代码格式与接口名以文档为准） |
| 交易日历 | `get_trade_days(...)` | `pro.trade_cal(...)` |
| 财务数据 | `get_fundamentals(query(...), date=...)` | `pro.income` / `pro.balancesheet` / `pro.fina_indicator` 等 |

## 四、代码格式与复权（最易混）

1. **证券代码**
   - 聚宽常见：`000001.XSHE`、`600519.XSHG`。
   - Tushare 日线常见：`000001.SZ`、`600519.SH`。
2. **复权**
   - JQ：`get_price` 的 `fq` 参数可一次指定前复权等。
   - Tushare：`daily` 等接口的复权规则以官方说明为准，常需单独处理因子或接口组合。

## 五、怎么选（复习）

- **只在聚宽网页里写策略、回测**：优先用**平台内置 API**，不必强行上 Tushare。
- **在本地 Python 拉数据、自己做研究/回测**：**Tushare** 或 **JQData** 二选一即可；本书若用 Tushare，迁移到 JQData 时重点改**登录方式 + 代码格式 + 复权**。
