# ChatGPTinQUEST

在 Meta Quest 內，透過中文語音與手柄和 AI 互動，讓 AI 建立、修改並解說可操作的虛擬物件。

**狀態：研究與專案規劃完成；尚未完成裝置安裝、Quest 實測或自製 APK。**  
調研日期：2026-09-23。此專案並非 OpenAI 或 Meta 官方產品。

## 調研結論與路線

已有高度接近需求的產品，第一個應驗證的是 **Figmin XR + MCP + 本機 AI 客戶端**。官方已描述語音互動、場景理解、內容建立與空間應用程式能力，也提供 Codex 接入步驟。不要先花數週重做整個 XR 編輯器。

但「已有功能說明」不等於「已在 George 的 Quest / Mac 上驗收」。中文語音品質、Apple Silicon 的 bridge 相容性、具體 Quest 型號支援及保存流程均待實機確認。

| 路線 | 何時採用 | 預期成果 |
|---|---|---|
| A：Figmin XR 整合（優先） | 先驗證核心體驗 | 說話建立物件、指向修改、手柄操作、場景保存 |
| B：Unity 原生 App（備案） | A 無法達標，或需要完整客製化 | 自有 APK、工具協定、UI、模型與資產管線 |
| C：ForgeXR 試用 | 比較語音生成世界體驗 | 供體驗對照；自有 ChatGPT 接入未證實 |

核心邊界：物件存在於 Figmin XR 或本專案自己的場景。此計畫不承諾跨 App 修改其他遊戲、Horizon Worlds 或 Quest 系統主畫面。

## 文件入口

1. [現成 App 比較與來源](docs/01-existing-apps.md)
2. [Figmin XR 接線與實機操作](docs/02-figmin-quickstart.md)
3. [自製 App 架構與實作步驟](docs/03-native-app-plan.md)
4. [里程碑與驗收案例](docs/04-roadmap-and-acceptance.md)
5. [交給本機 AI Agent 的執行指令](prompts/LOCAL_AGENT_START.md)

## 先做的事

- 確認 Quest 型號、系統版本、Figmin XR 商店相容性與目前價格。
- Quest 與 Mac 使用同一個可互通的 LAN。
- 按文件 02 建立 bridge 與 MCP 連接，先文字建立物件，再加中文語音。
- 按文件 04 留下實測記錄；過關後優先擴充 Figmin Spatial App。
- 無法過關時，依文件 03 分階段開發 Unity 版本。

## ChatGPT、Codex 與 API 的差異

A 路線是支援 MCP 的本機 AI 客戶端控制 Figmin。它不是把現有 ChatGPT 聊天記憶自動複製到 Quest，也不是把 ChatGPT 網頁語音直接嵌入 App。能否使用現有登入與方案，取決於實際客戶端、帳戶權限及用量限制。

B 路線如採 OpenAI API，需另行配置 API 專案與預算；不得假定 ChatGPT 訂閱自動抵扣 API。API 金鑰只放後端，不能包進 APK。模型與價格在實作時再次查官方文件。

## 第一個展示情境

「小克，在前方一公尺建立紅色方塊。」  
→ 手柄選取 →「把這個放大兩倍，改成藍色。」  
→ 用手柄抓取移動 →「儲存為我的實驗室。」  
→ 重開後恢復物件狀態。

進一步可建立電池模組、儲能櫃與換電站教學場景；工程尺寸、電力與物理模擬需另外驗證，不能把視覺模型視為工程計算結果。

## 官方參考

- https://www.figmin.com/mcp.html
- https://www.figmin.com/api/documentation.html
- https://developers.openai.com/codex/mcp/
- https://developers.openai.com/api/docs/guides/realtime-mcp
- https://developers.meta.com/horizon/documentation/unity/unity-project-setup/
