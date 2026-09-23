# 在 Mac 上執行的 Agent 接手指令

把以下內容交給具有本機終端與 MCP 設定存取權的 AI Agent。本指令不代表目前雲端對話已連到 Mac／Quest。

---

請接手 https://github.com/pcpcchen-coder/ChatGPTinQUEST 。

目標：在 Quest 中以繁體中文語音與手柄和「小克」互動，依語音建立、修改並保存真正可操作的虛擬物件。

先讀 README.md 及 docs/01–04。先做 Figmin XR + MCP 驗證；不要直接重寫 Unity App。

執行順序：
1. 檢查本機 macOS、CPU 架構、uv/uvx、AI 客戶端與既有 MCP 設定。不要輸出任何秘密。
2. 確認真正 Quest 型號與 Figmin 版本；需要使用者在頭戴裝置操作時，只提供當下必要的動作。
3. 保留其他 MCP 設定，新增 figmin-xr adapter。查目前官方文件，記錄實際安裝版本。不要永久修改全域 Python。
4. 啟動標準 figmin-bridge；Mac 不用 NVIDIA 專用 bridge。若有相容性錯誤先定位，不能捏造已成功。
5. 告知 Quest 要連的真實 LAN 地址；檢查 bridge 與 session 連線。
6. 讀 Figmin MCP help 後加入；先用文字指令查場景並建立紅色小方塊，讀回工具結果。
7. 加入中文語音與語音回覆，測手柄選取、抓取與「把這個變藍／放大兩倍」。
8. 按 docs/04 記錄 T01–T10；未測保持未測。只有實機 ACK／讀回／畫面證據才能稱為成功。
9. 把實測版本、問題、修復與驗收結果寫入 repo 的新測試報告。
10. 如果 A 無法達標，先說明具體缺口，按 docs/03 提出最小自製實作切片。

限制：
- 不覆蓋既有環境／場景；大量刪除或載入覆蓋前需要明確確認。
- 不把 bridge 直接曝露公網；不要把金鑰、LAN 詳細配置或原始私人錄音提交公開 repo。
- 不購買產品、不啟用新的付費服務，除非使用者授權。
- 不從其他聊天複製 token，也不把 ChatGPT 登入憑證當作任意 API 金鑰。
- 不自動複製 Figmin 專有套件原始碼到本 repo。
- 回報完成、未完成、實測結果與下一步；不要把文件完成說成 APK 完成。

---
