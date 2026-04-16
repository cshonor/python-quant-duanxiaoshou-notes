# 《Python量化交易实战》学习仓库

> 作者：段小手  
> 主线：Python 语法 → 金融数据 → 指标回测 → 策略 → 模拟盘 / 实盘 → 完整 Demo  
> 目标：**零基础入门量化 + Python 工程落地**，笔记与可运行源码一一对应。

## 仓库结构

| 路径 | 说明 |
|------|------|
| `notes/` | 各章 Markdown 学习笔记（与书本章节对齐） |
| `codes/` | 书中 Demo 源码复刻，按章节与 `project-final` 存放 |
| `assets/` | 截图、回测效果图等 |
| `env/requirements.txt` | Python 依赖 |

## 学习大纲与进度

在对应章节前打勾表示已完成（可按自己节奏改）。

- [ ] **CH01**
- [ ] **CH02**
- [ ] **CH03**
- [ ] **CH04**
- [ ] **CH05**
- [ ] **CH06**
- [ ] **CH07**
- [ ] **CH08**
- [ ] **CH09**
- [ ] **CH10**
- [ ] **CH11**
- [ ] **CH12**
- [ ] **CH13**
- [ ] **CH14**
- [ ] **CH15**
- [ ] **Project** 书中最终完整量化项目（见 `codes/project-final/`）

**当前进度：** 从 CH01 开始，边看书边更新 `notes/` 与 `codes/`。

## 环境准备

在**本仓库根目录**（含 `notes/`、`codes/`、`env/` 的目录）下执行：

```bash
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r env/requirements.txt
```

## 笔记规范（每章一个 `chXX-note.md`）

1. 本章知识点摘要  
2. 书本重点摘抄  
3. 自己的理解与通俗总结  
4. 踩坑记录、报错与解决  
5. Demo 代码拆分讲解（对应 `codes/chXX_demo/`）

## 代码规范

- `codes/` 尽量**复刻书中示例**，一页代码对应一个 `.py` 文件时可按小节命名。  
- 补全书里省略的 `import` 与依赖；必要处用注释扩充说明。  
- 运行前确认数据接口 Token / 网络权限等按书本要求配置。

## 许可与声明

本仓库为个人学习笔记与代码整理，图书版权归作者与出版社所有。请勿将笔记用于商业转载而未获授权。
