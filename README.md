[English](./README_EN.md)

```
       __      __    ________
      / /___  / /_  / ____/ /___ __      __
 __  / / __ \/ __ \/ /   / / __ `/ | /| / /
/ /_/ / /_/ / /_/ / /___/ / /_/ /| |/ |/ /
\____/\____/_.___/\____/_/\__,_/ |__/|__/
```

# JobClaw — AI 帮你投简历，你只管躺平

[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)

> **一句话说清楚：** JobClaw 是一个开源的 AI 求职 Agent——自动抓岗位、用大模型帮你匹配、一键批量投递，投完还给你发消息汇报。  
> 你要做的，就是写好简历，然后等面试通知。

---

## 😩 痛点：求职为什么这么累？

每个找过工作的人都懂：

- **Boss直聘刷到手酸**，拉勾、前程无忧还没看
- 每个岗位都要点进去看 JD，**人肉判断匹不匹配**
- 觉得还行就投，但一天下来才投了十几个
- 投完之后**石沉大海**，哪个回了、哪个没回，全靠记忆

你的时间应该花在**准备面试和提升自己**上，不是重复劳动。

## 🦀 JobClaw 帮你做什么？

| 步骤 | 人工 | JobClaw |
| --- | --- | --- |
| 搜岗位 | 多平台来回切，关键词一个个试 | **自动抓取** Boss直聘 + LinkedIn，后续支持拉勾、前程无忧 |
| 看 JD | 一个个点开，人肉阅读 | **LLM 智能匹配**，打分 + 给理由 |
| 投简历 | 点「立即沟通」/「投递」，重复 100 遍 | **自动投递**高匹配岗位 |
| 跟进状态 | Excel？备忘录？全靠脑子？ | **Telegram / Discord 实时通知** |

**简单说：你配好简历和偏好，JobClaw 帮你 24 小时无休投递。**

## 🚀 快速开始

```bash
# 1. 克隆安装
pip install -e .

# 2. 安装浏览器内核（Playwright 需要）
playwright install chromium

# 3. 登录 Boss直聘（弹出浏览器，手动登录）
jobclaw login --platform boss

# 4. 配置密钥（API key 等，cookie 已通过 login 自动保存）
cp .env.example .env
# 编辑 .env 填入你的配置

# 5. 填写你的求职画像
cp profiles/example.yaml profiles/me.yaml
# 编辑 profiles/me.yaml —— 你的技能、期望薪资、偏好城市等

# 6. 开跑！
jobclaw run --profile profiles/me.yaml --query "Python 工程师"
```

就这么简单。跑起来之后去喝杯咖啡，等 Telegram 通知就行。

## 🏗️ 架构

```text
+---------------------+
|   Profile Loader    |  你的简历 / 求职画像 (YAML)
+----------+----------+
           |
           v
+---------------------+      +----------------------+
|   Scraper Layer     |----->| Unified Job Objects  |
| Boss直聘 / LinkedIn |      | (Pydantic 标准化)     |
+----------+----------+      +----------+-----------+
           |                            |
           v                            v
+---------------------+      +----------------------+
|   LLM Matcher       |----->| 匹配分数 + 匹配理由   |
+----------+----------+      +----------+-----------+
           |                            |
           v                            v
+---------------------+      +----------------------+
|  Auto Applier       |----->| 投递状态              |
| Boss直聘 / LinkedIn |      | 已投 / 失败 / 跳过    |
+----------+----------+      +----------+-----------+
           |                            |
           +------------+---------------+
                        v
              +--------------------+
              | Notification Layer |
              | Telegram / Discord |
              +--------------------+
```

详细设计文档见 [docs/architecture.md](./docs/architecture.md)。

## 📋 支持平台

| 平台 | 状态 | 说明 |
| --- | --- | --- |
| **Boss直聘** (zhipin.com) | ✅ 已支持 | 抓取 + 自动打招呼投递 |
| **LinkedIn** | ✅ 已支持 | 抓取 + Easy Apply 投递 |
| 拉勾 (Lagou) | 🔜 计划中 | 适配器开发中 |
| 前程无忧 (51Job) | 🔜 计划中 | 适配器开发中 |

## 🔧 CLI 用法

```bash
# 交互式登录（弹出浏览器，手动登录后自动保存 cookie）
jobclaw login --platform boss

# 检查已保存的 cookie 是否有效
jobclaw login --platform boss --check

# 校验你的 profile 文件格式
jobclaw validate-profile --profile profiles/example.yaml

# 只抓取，不投递（先看看抓到什么）
jobclaw scrape --platform all --query "后端工程师" --limit 20

# 完整流程：抓取 → 匹配 → 投递 → 通知
jobclaw run --platform all --profile profiles/example.yaml --query "AI 工程师" --limit 20
```

## 📂 项目结构

```text
jobclaw/
  applier/       # 各平台自动投递适配器
  auth/          # 交互式登录 + cookie 持久化管理
  matcher/       # LLM 匹配打分
  notifier/      # Telegram / Discord 通知
  profile/       # 用户画像加载
  scraper/       # 各平台爬虫
  cli.py         # CLI 入口
  config.py      # 配置管理
  models.py      # Pydantic 数据模型
profiles/
  example.yaml   # 画像模板
docs/
  architecture.md
tests/
  test_models.py
```

## 🤝 参与贡献

欢迎 PR！特别欢迎：

- 🔌 **新平台适配器**（拉勾、前程无忧、猎聘……）
- 🧠 **更好的匹配策略**（prompt 调优、多维度评分）
- 🔒 **稳定性改进**（反爬对抗、断点续跑）
- 📢 **新通知渠道**（微信、飞书、钉钉）

```bash
pip install -e .[dev]
pytest -q
```

提 PR 前请跑测试、加类型标注、更新相关文档。

## ⚠️ 合规声明

自动化操作求职平台可能受到平台条款和当地法律的限制。请在合法合规、个人授权范围内使用本项目。作者不对滥用行为承担责任。

## 📜 许可证

MIT License — 详见 [LICENSE](./LICENSE)。
