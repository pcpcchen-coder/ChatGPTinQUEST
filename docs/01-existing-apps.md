# 現成產品調研

查閱日期：2026-09-23。以下是網站／文件證據，不是安裝後的測試報告。商店價格、地區、功能版本和帳號資格仍需在裝置確認。

## 比較

| 產品 | 已查得能力 | 與需求的缺口／待確認 | 判斷 |
|---|---|---|---|
| Figmin XR + MCP | 自帶 AI 客戶端接入、語音、場景查看與建立、Spatial App、手柄輸入 | Mac bridge、中文 STT/TTS、實際延遲與跨次保存未實測 | 最優先驗證 |
| ForgeXR | 官網描述 Quest Browser、語音／文字建世界、手與控制器；beta 有 fair-use 限制 | 未確認指定 OpenAI 模型或自己的 ChatGPT 帳號；未登入驗證 | 第二體驗候選 |
| Prompt Party | Meta 商店存在，生成並放置物件的產品描述；Early Access | 未證實自有 ChatGPT 接入、完整助理對話和中文能力 | 部分符合 |
| Tri3D | 文字生成模型、抓取縮放、房間保存；頁面 US$3 起 | 2025-12-20 作者公告需更新基礎設施；當前可用性不確定 | 不建議列首選 |
| Spatial Lingo | Meta 官方開源 Unity AI／語音 MR 範例 | 主題是語言學習與真實物件辨識，非通用物件生成助理 | 自製時參考架構 |

「没有完全相同的產品」無法靠網搜證明。此輪已找到高度符合的現成整合，因此先試用／驗收，再決定自製，不能宣稱市場沒有。

## Figmin XR 為何適合先試

官方將 AI 客戶端、MCP adapter 與本機 bridge 串接至 Quest 場景；AI 可檢查場景並生成空間應用。其 JS API 管理物件變換、物理與互動，避免從頭建 XR 編輯器。[F1–F3]

需要區分三種「建立」：
- 生成幾何／程式：快速生成方塊、文字、圖形與組合物件。
- 匯入既有模型：由資產庫取得 GLB，再放置與調整。
- 生成全新網格：需另外的 text-to-3D 管線；不把每個物件建立請求都視為高品質即時網格生成。

官方說 MCP 功能不需額外 Figmin 雲端付費服務，不代表 App、AI 客戶端或生成模型完全免費。[F1]

## 來源

| ID | 一手來源 | 支持內容 |
|---|---|---|
| F1 | https://www.figmin.com/mcp.html | AI／語音／本機 bridge／Codex 接入流程 |
| F2 | https://www.figmin.com/ | Quest 平台、創作、模型匯入 |
| F3 | https://www.figmin.com/api/documentation.html | Spatial App、控制器、物件 API；頁面標示 API v0.2 / July 2026 |
| F4 | https://pypi.org/project/figmin-mcp/ | adapter、Python >=3.11；檢索版本 0.2.2；專有授權 |
| W1 | https://forgexr.app/ | WebXR 語音世界建立；beta |
| P1 | https://www.meta.com/experiences/prompt-party/8040139252776662/ | 商店產品、Early Access |
| T1 | https://cazforshort.itch.io/tri3d-quest-ai-object-generation | 功能、價格、APK |
| T2 | https://cazforshort.itch.io/tri3d-quest-ai-object-generation/devlog/1155980/game-needs-update | 作者維護狀態 |
| M1 | https://github.com/oculus-samples/Unity-SpatialLingo | 官方開源參考程式 |
| M2 | https://developers.meta.com/horizon/documentation/unity/unity-sample-spatial-lingo/ | 範例功能 |

本次未核實 Figmin 台灣帳戶價格，不引用其他地區舊價作購買承諾。從 Figmin 官網或 Quest 商店搜尋完整名稱確認版本與相容裝置。
