# 第一個展示：先跑通六步流程

本輪優先順序：Figmin XR 既有功能 → MCP 連線 → 語音／手柄 → 保存重開。
不在本輪開發獨立 Unity APK、不接付費 text-to-3D，也不要求新的硬體。

**目前交付：Mac 啟動／設定腳本、session 指令與驗收表。尚未在 Mac 或 Quest 執行。**

## 在 Mac 啟動

本機 AI Agent 可 clone repo 後執行；已有 checkout 時先檢查未提交修改再更新，不要直接覆蓋。

```bash
git clone https://github.com/pcpcchen-coder/ChatGPTinQUEST.git
cd ChatGPTinQUEST
bash scripts/start-demo-mac.sh
```

也可在 clone 完成後雙擊 `Start-First-Demo.command`。如從 ZIP 解壓而沒有執行權限，直接使用上述 bash 命令。

腳本會確認 macOS 和 uv，使用 uv 管理 Python 3.11 執行設定器，將 Figmin MCP 加到目前 CODEX_HOME（未設定時為 ~/.codex）。既有 TOML 會備份，其他文字設定原樣保留；同名衝突、停用或無法解析時停止，不覆蓋。之後在前景執行官方 `uvx figmin-bridge`。

腳本不安裝 Figmin App、不處理帳戶登入、不自動開啟麥克風或修改防火牆。若 uv 尚未安裝，本機 Agent 可依終端顯示的官方網址處理。套件首次下載／Mac 語音相容性失敗時，應看實際錯誤定位。

重新啟動本機 AI 客戶端使 MCP 生效；把 `prompts/FIRST_DEMO_SESSION.md` 交給它。先確認工具清單有 Figmin，再戴 Quest。

## Quest 上只做這幾件事

1. 安裝／啟動 Figmin XR；確認商店支援你的型號與目前版本。
2. 和 Mac 接同一個可互通 LAN。
3. Discover → Featured → MCP Agent，輸入 bridge 終端顯示的地址，按 Connect。
4. 開啟語音輸入並選中文，允許所需麥克風權限。
5. 告訴本機 Agent「我已連線」，由它讀 help、加入 session，再開始下面六步。

官方來源：https://www.figmin.com/mcp.html
MCP 設定來源：https://developers.openai.com/codex/mcp/

## 六步驗收

在空白測試場景執行。首個方塊命名為 `CQ-DEMO-CUBE-01`，邊長 20 cm；放大兩倍明確定義為每邊 40 cm，不是體積兩倍。語音文字測試不等於語音測試通過。

| 步驟 | George 的操作 | Agent 必須取得的證據 |
|---|---|---|
| 1 | 說「小克，在前方一公尺建立紅色方塊」 | 工具成功結果、穩定物件 ID、顏色紅、邊長 20 cm；實機看到可操作物件 |
| 2 | 用手柄選取方塊 | 讀取目前選取 ID；不能因只有一個物件就假裝讀到了手柄選取 |
| 3 | 說「把這個放大兩倍，改成藍色」 | 同一個 ID、顏色藍、邊長 40 cm；重試不再乘兩倍 |
| 4 | 用手柄抓起來，放到另一個位置 | 放開後讀回位置／旋轉，與先前不同；不能沿用 AI 快取的舊座標 |
| 5 | 說「儲存為我的實驗室」 | 確認目前工具有保存能力；保存回執／檔案位置與當前物件 snapshot |
| 6 | 完全退出 Figmin，再開啟並說「載入我的實驗室」 | 重新連線後載入；一個藍色 40 cm 方塊，恢復步驟 4 的場景相對變換 |

恢復場景相對座標與精準鎖定真實房間是不同驗收。初版驗前者，實體桌面精準對齊後續另測 anchor。不要因重新定位導致座標系改變就直接宣稱物件恢復正確。

如果目前 MCP 不能操作保存：查其 help 與 Figmin 保存功能；可以先讓使用者按原生保存完成「手動保存」部分驗證，但**語音保存步驟仍是 Blocked**。必要時針對保存補 Spatial App，不得口頭說已存好。保存功能是端到端通過的必要條件。

## 本機測試結果

建立 `local-results/first-demo.md`（已 gitignore），填入：

```text
Quest 型號／OS：
Mac／macOS：
Figmin、bridge、MCP、AI 客戶端版本：
步驟 1：NOT_RUN / PASS / FAIL / BLOCKED；證據：
步驟 2：NOT_RUN / PASS / FAIL / BLOCKED；證據：
步驟 3：NOT_RUN / PASS / FAIL / BLOCKED；證據：
步驟 4：NOT_RUN / PASS / FAIL / BLOCKED；證據：
步驟 5：NOT_RUN / PASS / FAIL / BLOCKED；證據：
步驟 6：NOT_RUN / PASS / FAIL / BLOCKED；證據：
語音 STT／TTS 狀態：
語音結束→物件變化的耗時：
尚待修復：
```

只在六步皆有證據且語音往返可用時宣布端到端通過。公開 repo 只提交去識別化摘要，不提交家庭場景、LAN 位址、聊天／語音紀錄或設定備份。

## 回復 MCP 設定

停止 bridge 後，由本機 Agent 只移除 `mcp_servers.figmin-xr` 區塊；保留其他設定。設定器備份位於設定檔同一目錄、前綴 `config.toml.before-quest-`。如啟動後又改過其他設定，先做差異合併，不要整份回蓋。重新啟動客戶端。

## 程式驗證範圍

2026-09-23 在雲端 Linux 執行 Python 設定器測試與 Bash 語法检查。這只驗證保留既有設定、備份、冪等與錯誤停止，不代表第三方 bridge 可在 Apple Silicon 執行，也不代表上述六步已通過。
