#!/bin/bash
set -euo pipefail
QUEST_PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [[ "$(uname -s)" != Darwin ]]; then
  echo "此腳本必須在你的 Mac 執行；不會在雲端 Linux 啟動 bridge。" >&2
  exit 2
fi

# Finder-launched Terminal may not inherit Homebrew's PATH.
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:$PATH"
if ! command -v uv >/dev/null || ! command -v uvx >/dev/null; then
  echo "缺少 uv／uvx。請本機 Agent 按官方文件安裝後重跑："
  echo "https://docs.astral.sh/uv/getting-started/installation/"
  echo "如果已安裝 Homebrew，可執行：brew install uv"
  exit 3
fi

QUEST_UVX="$(command -v uvx)"
echo "ChatGPTinQUEST：第一個展示流程"
uv --version
echo "1. 設定本機 MCP（保留其他設定並備份；不讀取登入憑證）。"
uv run --no-project --python 3.11 "$QUEST_PROJECT_DIR/scripts/configure_mcp.py" --uvx "$QUEST_UVX"
echo "2. 重新啟動本機 AI 客戶端，載入 prompts/FIRST_DEMO_SESSION.md。"
echo "3. 等 bridge 顯示 ready；Quest 與 Mac 同 LAN。"
echo "4. Quest：Figmin XR → Discover → Featured → MCP Agent，輸入下方 bridge 顯示的地址。"
echo "5. 由本機 AI Agent 讀取 Figmin help 並加入 session。"
echo "首次可能需要下載語音資源。此程序不表示 Quest 已連線。Ctrl-C 可停止。"
exec "$QUEST_UVX" figmin-bridge
