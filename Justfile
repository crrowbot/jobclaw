# JobClaw 任务自动化配置
# 使用 `just <任务名>` 运行

# 默认任务
default:
    @echo "可用任务："
    @just --list

# 环境设置
setup:
    uv sync --dev
    @echo "依赖安装完成！"

install-browser:
    uv run playwright install chromium
    @echo "Chromium 浏览器安装完成"

# 登录相关
login:
    uv run jobclaw login --platform boss

login-check:
    uv run jobclaw login --platform boss --check

# 测试运行
test-scrape:
    uv run jobclaw scrape --source boss --limit 3

test-run:
    uv run jobclaw run --profile profiles/me.yaml --dry-run=true

# 实际运行（会真正投递！）
run:
    uv run jobclaw run --profile profiles/me.yaml --dry-run=false

# 代码质量
lint:
    uv run ruff check jobclaw/

format:
    uv run ruff format jobclaw/

type-check:
    uv run mypy jobclaw/

# 测试
test:
    uv run pytest tests/ -v

# 清理
clean:
    rm -rf .venv
    rm -rf __pycache__
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete 2>/dev/null || true
    @echo "清理完成"

# 构建
build:
    uv build
    @echo "构建产物在 dist/ 目录"

# 一次性完整设置（首次运行）
init: setup install-browser
    @echo "=========================================="
    @echo "JobClaw 初始化完成！"
    @echo "下一步："
    @echo "1. 编辑 .env 文件配置 API keys（可选）"
    @echo "2. 运行 'just login' 登录 BOSS直聘"
    @echo "3. 创建 profiles/me.yaml 个人资料"
    @echo "4. 运行 'just test-scrape' 测试爬取"
    @echo "=========================================="
