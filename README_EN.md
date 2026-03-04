[中文](./README.md)

```
       __      __    ________
      / /___  / /_  / ____/ /___ __      __
 __  / / __ \/ __ \/ /   / / __ `/ | /| / /
/ /_/ / /_/ / /_/ / /___/ / /_/ /| |/ |/ /
\____/\____/_.___/\____/_/\__,_/ |__/|__/
```

# JobClaw — Stop Applying Manually. Let AI Do the Grunt Work.

[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)

> **TL;DR:** JobClaw is an open-source AI job hunting agent. It scrapes job listings, matches them against your profile using LLMs, auto-applies to the best fits, and notifies you of results.  
> You write the resume. JobClaw does the rest.

---

## The Problem

Job hunting is a grind. Everyone knows it:

- You scroll through **LinkedIn** for hours, tweaking keywords, opening tabs
- You read each JD manually to decide if it's worth applying
- You click "Easy Apply" dozens of times a day — same info, over and over
- You lose track of what you applied to, what ghosted you, what's pending

Your time is better spent **preparing for interviews and building skills** — not copy-pasting your resume into web forms.

## What JobClaw Does

| Step | Manual | JobClaw |
| --- | --- | --- |
| Find jobs | Jump between platforms, try different keywords | **Auto-scrape** LinkedIn + Boss直聘, more coming |
| Evaluate fit | Read each JD, gut-feel it | **LLM-powered matching** with scores and explanations |
| Apply | Click "Apply" 100 times | **Auto-apply** to high-match roles |
| Track status | Spreadsheet? Sticky notes? Memory? | **Real-time Telegram / Discord notifications** |

**Set up your profile once. Let JobClaw run 24/7.**

## Quick Start

```bash
# 1. Clone & install
pip install -e .

# 2. Install browser runtime (required by Playwright)
playwright install chromium

# 3. Configure secrets (API keys, platform cookies, etc.)
cp .env.example .env
# Edit .env with your settings

# 4. Set up your job profile
cp profiles/example.yaml profiles/me.yaml
# Edit profiles/me.yaml — your skills, salary expectations, preferred locations

# 5. Launch
jobclaw run --profile profiles/me.yaml --query "Python Engineer"
```

That's it. Grab a coffee and wait for notifications.

## Architecture

```text
+---------------------+
|   Profile Loader    |  Your resume / preferences (YAML)
+----------+----------+
           |
           v
+---------------------+      +----------------------+
|   Scraper Layer     |----->| Unified Job Objects  |
| LinkedIn / Boss直聘 |      | (Pydantic Models)    |
+----------+----------+      +----------+-----------+
           |                            |
           v                            v
+---------------------+      +----------------------+
|   LLM Matcher       |----->| Match Score + Reason |
+----------+----------+      +----------+-----------+
           |                            |
           v                            v
+---------------------+      +----------------------+
|  Auto Applier       |----->| Application Status   |
| LinkedIn / Boss直聘 |      | Submitted / Failed   |
+----------+----------+      +----------+-----------+
           |                            |
           +------------+---------------+
                        v
              +--------------------+
              | Notification Layer |
              | Telegram / Discord |
              +--------------------+
```

See detailed design in [docs/architecture.md](./docs/architecture.md).

## Supported Platforms

| Platform | Status | Notes |
| --- | --- | --- |
| **LinkedIn** | ✅ Supported | Scraping + Easy Apply |
| **Boss直聘** (zhipin.com) | ✅ Supported | Scraping + auto-apply |
| Lagou (拉勾) | 🔜 Planned | Adapter in progress |
| 51Job | 🔜 Planned | Adapter in progress |

## CLI Usage

```bash
# Validate your profile file
jobclaw validate-profile --profile profiles/example.yaml

# Scrape only (preview without applying)
jobclaw scrape --platform all --query "Backend Engineer" --limit 20

# Full pipeline: scrape → match → apply → notify
jobclaw run --platform all --profile profiles/example.yaml --query "AI Engineer" --limit 20
```

## Repository Layout

```text
jobclaw/
  applier/       # Per-platform auto-apply adapters
  matcher/       # LLM matching & scoring
  notifier/      # Telegram / Discord notifications
  profile/       # User profile loading
  scraper/       # Per-platform scrapers
  cli.py         # CLI entry point
  config.py      # Configuration management
  models.py      # Pydantic data models
profiles/
  example.yaml   # Profile template
docs/
  architecture.md
tests/
  test_models.py
```

## Contributing

PRs are welcome! Especially:

- 🔌 **New platform adapters** (Indeed, Glassdoor, more regional sites)
- 🧠 **Better matching strategies** (prompt tuning, multi-dimensional scoring)
- 🔒 **Reliability improvements** (anti-bot resilience, checkpointing)
- 📢 **New notification channels** (Slack, email, webhooks)

```bash
pip install -e .[dev]
pytest -q
```

Before opening a PR: run tests, add type annotations, and update relevant docs.

## Legal & Responsible Use

Automated interactions with job platforms may be subject to their terms of service and local regulations. Use this project responsibly and only on accounts you are authorized to operate. The authors are not liable for misuse.

## License

MIT License — see [LICENSE](./LICENSE).
