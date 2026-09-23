# Figmin XR + 本機 AI：操作手冊

目標：先通文字與物件操作，再通中文語音。下面是待執行步驟，不表示本專案已完成實測。

## 1. 環境紀錄

記下 Quest 型號／OS、Figmin 版本、Mac 型號／macOS、本機 AI 客戶端版本。確認商店頁支援該頭戴裝置。首選以 Quest 3/3S 作 MR 驗證目標，但不假定使用者持有此型號。

Quest 和 Mac 接同一 LAN，避免訪客 Wi-Fi／AP isolation。開放必要的區網連線，不把 bridge 直接曝露公網。保留 Mac 的螢幕與終端可查看錯誤。

## 2. 準備 uv

先在 Mac Terminal 執行：

```bash
command -v uv
command -v uvx
uv --version
```

未安裝時按 https://docs.astral.sh/uv/getting-started/installation/ 安裝適合 macOS 的版本。
如已裝 Homebrew，可用 `brew install uv`。不要照抄 Figmin 官方頁面的 Windows winget 指令到 Mac。

## 3. 啟動 bridge

官方標準 bridge 命令：

```bash
uvx figmin-bridge
```

第一次可能下載 Python 套件及語音資源；等 ready 後，記錄終端顯示的實際連線地址，保持程序運行。Apple Silicon 不使用 NVIDIA 專用的 `figmin-bridge-gpu` 路徑。

**Mac 相容性關卡：** 官方教學主要展示 Windows，本次沒有 Mac bridge 安裝測試。若套件解析、語音引擎或音訊裝置失敗，記錄完整錯誤與版本，查其當前文件；不可憑名稱假設具備 Metal 加速，也不可編造未查證的啟動參數。若場景控制成功、語音失敗，分別記錄，勿混為全部成功。可再評估其他 bridge 主機或路線 B。

## 4. 設定 MCP 客戶端

使用支援本機 STDIO MCP 的 Codex／ChatGPT 桌面開發環境，按實際版本介面設定。

若已安裝 Codex CLI：

```bash
codex mcp add figmin-xr -- uvx figmin-mcp
codex mcp list
```

或合併下列設定至既有 `~/.codex/config.toml`，**保留其他設定**：

```toml
[mcp_servers.figmin-xr]
command = "uvx"
args = ["figmin-mcp"]
```

GUI 找不到 uvx 時，用 `command -v uvx` 得到的絕對路徑替換 command。重新啟動客戶端，確認 MCP 工具已載入。只有連線列表出現不代表 Quest 已連線。

官方 MCP 文件：https://developers.openai.com/codex/mcp/

目前 hosted web 對話不能僅靠修改 Mac 本機設定就自動取得 LAN 工具。本步應在連得到 bridge 的本機客戶端進行。

## 5. Quest 端加入

1. 啟動／更新 Figmin XR。
2. 在 Discover 的 Featured 找到 MCP Agent。
3. 輸入 bridge 終端顯示的電腦地址，按 Connect。
4. 若看不到 MCP Agent，先確認版本／功能開放狀態，依官方支援排查。
5. 本機 AI 客戶端讀取 Figmin MCP help，再加入 session。

adapter 的本機 daemon 位址與 Quest 需輸入的 LAN 地址不是同一概念；Quest 上的 localhost 指 Quest 本身，不是 Mac。不要憑 PyPI 的 loopback 範例硬填 Quest 連線欄。

## 6. 第一輪驗證

在本機 AI 客戶端貼：

> 請透過 Figmin XR MCP 加入目前 session，先閱讀 help，列出可用的場景查詢與建立工具。使用繁體中文，稱呼自己「小克」。先回報是否真的連線成功，再於使用者前方約一公尺建立一個紅色小方塊。執行後讀回物件狀態，不要僅口頭宣稱成功。若目前工具無法建立該形狀，請說明原因與可用替代。

先文字驗證建物件 → 用手柄選取／移動 → 再說「把這個改成藍色」。若「這個」指涉不明，要求確認選取目標。

確認操作成功後：
- 開啟 dictation，使用語言按鈕選中文；中文 TTS 另測。
- 說：「小克，幫我建立一個球。」
- 說：「把我選到的這個放大兩倍。」
- 說：「列出場景裡目前有哪些物件。」
- 測保存／重新載入；區分 App 內保存與重開後的實體空間定位。

## 7. 保存與效能

使用 Figmin 官方支援的保存機制；腳本結束後保留物件與跨次啟動保存是不同問題，須各自驗證。物件的名稱、尺寸、顏色、位置與旋轉需讀回比對。

先做 10 個簡單物件，再增加至 50 個。若語音慢，拆量 STT、模型回覆與 TTS 時間；若畫面慢，拆量物件數、模型複雜度與每幀腳本更新。不要每個渲染幀呼叫 LLM。

## 8. 常見問題

| 現象 | 排查 |
|---|---|
| uvx 找不到 | 新開終端；GUI 使用絕對路徑 |
| MCP 可見但沒場景 | bridge 是否 running；Quest 是否 Connect；agent 是否 join |
| Quest 連不到 | 正確 LAN IP、防火牆、AP isolation、同網段路由 |
| 文字可用但語音失敗 | 麥克風權限、語言、STT/TTS 套件与音訊日誌 |
| AI 說完成但沒有物件 | 看工具結果與場景讀回；保留 request/error |
| 重開後物件不見／漂移 | 分別檢查保存與空間 anchor；不能只存世界座標 |

通過後把實測日期、版本、測試結果記入 docs/04 的表格；不要把未測項目改成通過。

主要來源：https://www.figmin.com/mcp.html 、 https://pypi.org/project/figmin-mcp/ 、 https://www.figmin.com/api/documentation.html
