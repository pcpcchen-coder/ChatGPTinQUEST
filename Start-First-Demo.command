#!/bin/bash
QUEST_PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$QUEST_PROJECT_DIR/scripts/start-demo-mac.sh"
QUEST_EXIT=$?
if [[ "$QUEST_EXIT" -ne 0 ]]; then
  echo "啟動未完成（代碼 $QUEST_EXIT）。請把錯誤交給本機 Agent 排查。"
  read -r -p "按 Enter 關閉…" || true
fi
exit "$QUEST_EXIT"
