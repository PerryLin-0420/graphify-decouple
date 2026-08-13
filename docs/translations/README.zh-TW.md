<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>本專案 fork 自 <a href="https://github.com/Graphify-Labs/graphify">graphify</a>,新增了 <code>graphify decouple</code></b> —— 針對神級物件、0-LLM、根據風險評分的 Extract-Class 候選方案,在推薦任何做法之前,都會回頭比對實際原始碼(而不只是呼叫圖)進行再次驗證。詳見下方的 <a href="#decouple-根據風險評分的-extract-class-候選方案">Decouple: 根據風險評分的 Extract-Class 候選方案</a>。
</p>

<div align="center">
<details><summary><b>閱讀其他語言版本</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>在 v1 正式版推出之前,graphify 平台已開放搶先體驗:<a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

在你的 AI 程式碼助手中輸入 `/graphify`,它就會把你整個專案(程式碼、文件、PDF、圖片、影片)對應成一份可以**查詢而非用 grep 翻找**檔案的**知識圖譜**。

- **程式碼地圖完全免費、完全在地端執行。** 程式碼是用 tree-sitter AST 解析的:確定性運算、不使用 LLM、任何內容都不會離開你的機器。(文件、PDF、圖片與影片則會使用你助手所用的模型,或你設定的 API 金鑰,進行語意分析。)
- **每一條邊都有說明。** 每個連結都會標記為 `EXTRACTED`(原始碼中明確存在)或 `INFERRED`(由 graphify 解析而得),讓你清楚分辨哪些是直接讀到的、哪些是推論出來的。
- **不是向量索引。** 沒有 embedding、沒有向量資料庫:是一個你可以實際走訪的圖譜。你可以提問、追蹤兩個事物之間的路徑,或是請它解釋單一概念。

> 想要一個隨時在背景中運作、持續更新你的程式碼、文件與會議記錄,而不只是隨選查詢的版本嗎?這正是我們在 **[graphify.com](https://graphify.com)** 打造的東西,現在就可以在 **[app.graphify.com](https://app.graphify.com/login)** 搶先體驗。

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="graphify 互動式 graph.html,以力導向圖將 FastAPI 程式碼庫呈現為知識圖譜,並附上偵測到的社群圖例" width="900">
</p>
<p align="center">
  <em>由 graphify 建置的 FastAPI 程式碼庫圖譜。每個節點都是一個概念,顏色代表偵測到的社群,整張圖在 graph.html 中都可以點擊互動。</em>
</p>

**開始使用**(30 秒):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

接著,在你的 AI 助手裡輸入:

```
/graphify .
```

就這樣。你會得到**三個檔案**:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**支援平台:** Claude Code、Cursor、Codex、Gemini CLI、GitHub Copilot 等 15 種以上工具 — [挑選你的平台](#安裝)。

---

## 實際操作展示

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="graphify 路徑查詢:終端機詢問 FastAPI 與 ModelField 之間的最短路徑,答案沿著知識圖譜一跳一跳亮起" width="900">
</p>

圖譜建好之後,你可以直接查詢它,而不用再去讀檔案。以下是實際輸出,graphify 對上方展示的 FastAPI 程式碼庫執行後的結果:

```text
$ graphify explain "APIRouter"
Node: APIRouter
  Source:    routing.py L2210
  Community: 2
  Degree:    47

Connections (47):
  --> RequestValidationError [uses] [INFERRED]
  --> Dependant [uses] [INFERRED]
  --> .get() [method] [EXTRACTED]
  <-- __init__.py [imports] [EXTRACTED]
  ...

$ graphify path "FastAPI" "ModelField"
Shortest path (3 hops):
  FastAPI --uses--> DefaultPlaceholder <--references-- get_request_handler() --references--> ModelField
```

每一條邊都帶有**信心標記**(`EXTRACTED` = 原始碼中明確存在,`INFERRED` = 由解析推導而來),讓你能分辨哪些是直接讀到的、哪些是推論出來的。`graphify query "<question>"` 會針對一個口語化的問題回傳一個範圍縮小的子圖,而 `graphify path A B` 則會追蹤任兩個事物之間的關聯。

---

## Decouple: 根據風險評分的 Extract-Class 候選方案

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple:MainWindow 這個神級節點拆分成多個風險評分候選類別,其中兩者之間出現共享狀態警告" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html:MainWindow 提出的 5 個類別,Node Info 面板開啟於 Main Window Axis and Range Controls,顯示與 Main Window Controller Core 有 0.608 的狀態重疊" width="900">
</p>
<p align="center">
  <em>DECOUPLE.html 在一次真實執行(AutoCheck/Touchstone Explorer)上的畫面 — 點擊任一個提議的類別,就能準確看到它和哪個類別共享狀態,以及具體共享了什麼。</em>
</p>

`graphify decouple` 會找出神級物件,並告訴你拆分它是否真的值得 — 而不只是告訴你它很大。

這個功能是為了抓住這種失敗模式而存在的:一個有 47 個方法的類別,呼叫圖聚類演算法很樂意把它拆成 5 個看起來乾淨俐落的群組,但這些群組底層其實仍然在讀寫完全相同的 `self._chart_style` / `self._crosshair` 實例狀態。如果就這樣把這個拆分方案發布出去,你其實什麼都沒有解耦 — 你只是把方法搬到新檔案裡,而它們仍然無法被獨立測試、修改或推理,因為它們全部都還需要依賴同一份被傳回來的共享狀態。只看呼叫圖的工具完全看不到這一點;它必須回頭檢視實際原始碼。

**兩項檢查,兩者都是 0-LLM、都是確定性的:**

1. **這真的是神級物件嗎?** 高度數的節點可能是真正的神級物件(擁有大量「自己的」方法,分散在互不相關的職責上 — 適用 Extract Class),也可能只是一個被過度參照的樞紐 / 資料模型(自己的方法很少,大多是「被外部參照」— 拆分它的本體不會有任何效果;真正的解法是收斂它的介面,而不是抽取類別)。`classify_god_node` 是靠 `member_ratio` 而不是原始度數來區分這兩者的差異 — 正是這個差異,讓 `TraceSource`(84 條邊,但自己的方法只有 6 個)不會拿到一個假的拆分建議,而 `MainWindow`(88 條邊,自己的方法有 47 個)則正確地拿到了拆分建議。
2. **拆分之後真的能降低耦合嗎?** `risk_before`(神級節點目前的大小 / 耦合度 / 碎片化程度)會拿來和 `risk_after` 比較 — 也就是拆分方案本身會帶來的「新」風險:原本是類別內部隱形邊界的跨群組呼叫,拆分後會變成明確的類別間依賴;呼叫端會需要依賴不只一個新類別;還有一項呼叫圖在結構上完全做不到的檢查 — 提議的群組之間到底共享了多少 `self`/`this` 實例狀態(讀取、寫入,以及共享輔助方法呼叫,三者權重各不相同:共享的**寫入**權重高於共享的讀取)。這一步會直接用 tree-sitter 重新解析神級節點自己的原始碼檔案;它不依賴 graphify 自己抽取出來的圖譜,因為那份圖譜從來不會記錄任何語言的欄位層級存取。只有當 `risk_after` 低於 `risk_before` 到達某個門檻以下時,方案才會建議 `split` — 否則就是 `marginal` 或 `keep_as_is`,而被建議不要拆分的候選方案一律以數字方式回報,絕不會畫成一個要你憑肉眼猜測的圖形。

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

在 `graph.json` 旁邊會輸出三個檔案:

```
graphify-out/
├── DECOUPLE_PLAN.md   # human-readable: per god node, classification, risk_before -> risk_after,
│                      # which methods move where, and exactly which attributes/writes/calls are shared
├── decouple.json      # the same plan as structured data — feed it to any AI or script
└── DECOUPLE.html      # the SAME force-directed graph.html renderer, not a separate diagram:
                       # a "Preview decoupled view" toggle swaps the real methods for the proposed
                       # classes and re-routes their edges live, so you see the wiring change, not
                       # just a before/after screenshot; click any proposed class to see exactly
                       # which other class it shares state with and what specifically is shared
```

**狀態共享檢查的語言涵蓋範圍**(上面提到的純呼叫圖分類方式,適用於 graphify 能擷取的每一種語言;下面這張表則專門針對驗證 `self`/`this` 狀態重疊的原始碼重新解析功能):

| 語言 | 是否支援 | 備註 |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` 是獨立的 AST 節點,而不是包裝過的欄位存取 — 有特別處理 |
| C# | ✅ | |
| Rust | ✅ | 透過 `impl` 區塊使用 `self.x` |
| Ruby | ✅ | `@x`(主流慣用寫法)+ `self.foo` 呼叫 |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | 逐一方法解析接收器(receiver)— Go 沒有 `self`/`this` 關鍵字,所以每個方法都要重新解析接收器名稱(例如 `func (f *Foo) M()` 中的 `f`) |
| C | ❌ | struct 指標參數在語法上沒有任何標記可以和其他參數區分開來 — 沒有完整型別推論就無法可靠判斷 |

未受支援語言中的神級節點,或是原始碼無法讀取的節點,會被標記為 `state_analysis: "skipped"` — 分類與呼叫圖評分仍會照常執行,但最終建議只會依據呼叫圖本身,而不會默默假設狀態檢查已經通過。

---

## 這個工具能做什麼

開箱即用你可以得到:

| 功能 | 你會得到什麼 |
|---|---|
| **神級節點** | 連結數最多的概念,讓你看清所有東西都流經哪裡 |
| **社群** | 圖譜依子系統拆分(Leiden 演算法),標籤不使用 LLM |
| **跨檔案連結** | 透過 tree-sitter AST,在約 40 種語言之間解析 `calls` / `imports` / `inherits` / `mixes_in` |
| **查詢、路徑、解釋** | 提問、追蹤兩者之間的路徑,或針對 `graph.json` 解釋單一概念 |
| **理由與文件參照** | `# NOTE:` / `# WHY:` 註解與 ADR/RFC 引用都會成為與程式碼相連的一級節點 |
| **不只是程式碼** | 文件、PDF、圖片與影音都會對應進同一張圖譜 |
| **在地優先** | 程式碼在本機用 tree-sitter 解析(不使用 LLM、任何內容都不離開你的機器);只有針對文件 / 媒體的語意分析才會呼叫後端,而且只有在你設定的情況下才會發生 |

---

## 基準測試

| 基準測試 | 指標 | graphify | 同類系統 |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | QA accuracy | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | QA accuracy | **76%** | tied with dense RAG |
| Graph build | LLM credits | **0** | per-token for most systems |

所有系統都在相同的測試框架、相同的模型與相同的預算下執行,並由一個評審模型評分,再與第二個評審模型做盲驗證(一致率 90.6%,Cohen's kappa 0.81)。完整的逐系統表格、程式碼智能(code-intelligence)測試結果與重現指令,請見:**[BENCHMARKS.md](../../BENCHMARKS.md)**。

---

## 事前準備

| 需求 | 最低版本 | 檢查方式 | 安裝方式 |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(建議)* | 不限 | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(替代方案)* | 不限 | `pipx --version` | `pip install pipx` |

**macOS 快速安裝(Homebrew):**
```bash
brew install python@3.12 uv
```

**Windows 快速安裝:**
```powershell
winget install astral-sh.uv
```

**Ubuntu/Debian:**
```bash
sudo apt install python3.12 python3-pip pipx
# or install uv:
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## 安裝

> **官方套件:** PyPI 上的套件名稱是 `graphifyy`(兩個 y)。PyPI 上其他以 `graphify*` 開頭的套件與本專案無關。CLI 指令本身仍然是 `graphify`。

**步驟一 — 安裝套件:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**步驟二 — 向你的 AI 助手註冊這個技能:**

```bash
graphify install
```

就這樣。打開你的 AI 助手,輸入 `/graphify .`

如果想把助手技能安裝到目前的 repository,而不是你的使用者設定檔,加上 `--project`:

```bash
graphify install --project
graphify install --project --platform codex
```

專案範圍的安裝會寫入目前目錄底下,例如
`.claude/skills/graphify/SKILL.md` 或 `.agents/skills/graphify/SKILL.md`(外加一個
技能會依需求載入的 `references/` 附屬目錄),並且
會印出可以提交的檔案的 `git add` 提示。
支援專案範圍安裝的個別平台指令都接受相同的參數,
例如 `graphify claude install --project` 或 `graphify codex install --project`。

> **PowerShell 注意事項:** 請用 `graphify .`,不要用 `/graphify .` — 在 PowerShell 中開頭的斜線會被當成路徑分隔符號。

> **`graphify: command not found`?** `uv tool install` / `pipx install` 會把 `graphify` 指令放進它們自己的工具 bin 目錄(`~/.local/bin`)。如果安裝完之後你的 shell 找不到這個指令 — 在全新的 macOS + zsh 環境上很常見 — 代表那個目錄還沒加進你的 `PATH`:執行 `uv tool update-shell`(或 `pipx ensurepath`),然後開一個新的終端機。如果是用純 `pip` 安裝,請把 `~/.local/bin`(Linux)或 `~/Library/Python/3.x/bin`(Mac)加進你的 PATH,或是改用 `python -m graphify`。

> **想用 `uvx` / `uv tool run` 而不是直接安裝?** 要指定的是套件名稱,而不是指令名稱:`uvx --from graphifyy graphify install`。單純的 `uvx graphify …` 會失敗(`No solution found … no versions of graphify`),因為 `uv tool run` 會把第一個字當成*套件*來解析,而套件名稱是 `graphifyy` — `graphify` 這個指令是包在裡面的。

> **請盡量避免在 Mac/Windows 上用 `pip install`。** 這個技能在執行時會從 `graphify-out/.graphify_python` 解析 Python 路徑;如果那個路徑指到的環境跟 `pip` 安裝套件的環境不一樣,就會出現 `ModuleNotFoundError: No module named 'graphify'`。`uv tool install` 和 `pipx install` 會把套件隔離在自己的環境裡,完全避開這個問題。

> **Git hook 與 uv tool / pipx:** `graphify hook install` 會在安裝當下,把目前的直譯器路徑直接寫死進 hook 腳本裡,所以即使在 `~/.local/bin` 不在 PATH 上的 GUI git 客戶端或 CI 執行環境中,post-commit hook 也能正常觸發。如果你重新安裝或升級 graphify,記得重新執行一次 `graphify hook install` 來更新寫死的路徑。

> **嚴格模式(Claude Code):** `graphify install --project --strict` 會讓助手真正去使用這份圖譜。預設安裝只會「提醒」助手在讀檔案之前先跑 `graphify query`;嚴格模式則會「攔截」一次 session 中第一次直接讀取原始碼的動作,把它導向圖譜,然後恢復成提醒模式(所以每個 session 最多只會觸發一次,也不會卡住)。可以用 `GRAPHIFY_HOOK_STRICT=1`/`0` 在執行期切換;預設安裝行為不變(軟性提醒)。

<details>
<summary><b>挑選你的平台</b>(20 種以上的助手,點擊展開)</summary>

| Platform | Install command |
|----------|----------------|
| Claude Code (Linux/Mac) | `graphify install` |
| Claude Code (Windows) | `graphify install`(自動偵測)或 `graphify install --platform windows` |
| CodeBuddy | `graphify install --platform codebuddy` |
| Codex | `graphify install --platform codex` |
| OpenCode | `graphify install --platform opencode` |
| Kilo Code | `graphify install --platform kilo` |
| GitHub Copilot CLI | `graphify install --platform copilot` |
| VS Code Copilot Chat | `graphify vscode install` |
| Aider | `graphify install --platform aider` |
| OpenClaw | `graphify install --platform claw` |
| Factory Droid | `graphify install --platform droid` |
| Trae | `graphify install --platform trae` |
| Trae CN | `graphify install --platform trae-cn` |
| Gemini CLI | `graphify install --platform gemini` |
| Hermes | `graphify install --platform hermes` |
| Kimi Code | `graphify install --platform kimi` |
| Amp | `graphify amp install` |
| Agent Skills (cross-framework) | `graphify install --platform agents`(別名 `--platform skills`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify install --platform pi` |
| Cursor | `graphify cursor install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

Codex 使用者還需要在 `~/.codex/config.toml` 的 `[features]` 底下加上 `multi_agent = true` 才能進行平行擷取。CodeBuddy 使用跟 Claude Code 相同的 Agent 工具與 PreToolUse hook 機制。Factory Droid 使用 `Task` 工具做平行子代理派工。OpenClaw 和 Aider 使用循序擷取(這兩個平台的平行代理支援還在早期階段)。Trae 使用 Agent 工具做平行子代理派工,而且**不**支援 `PreToolUse` hook,所以 AGENTS.md 是常駐運作的機制。

`--platform agents`(別名 `--platform skills`)對應到通用的跨框架 [Agent-Skills](https://github.com/anthropics/skills) 位置:規格定義的使用者全域路徑 `~/.agents/skills/`(給 `npx skills` 和符合規格的框架讀取)用於全域安裝,而 `./.agents/skills/` 則用於專案(`--project`)安裝。單純的 `graphify install` 依設計仍然只鎖定單一平台(Claude Code)— 想讓技能能被任何讀取 `.agents/skills` 的框架發現,請使用具名的 `agents` 平台。

> Codex 使用 `$graphify` 而不是 `/graphify`。

</details>

<details>
<summary><b>可選擴充套件</b>(只安裝你需要的)</summary>

| 擴充套件 | 新增功能 | 安裝方式 |
|---|---|---|
| `pdf` | PDF 擷取 | `uv tool install "graphifyy[pdf]"` |
| `office` | `.docx` 與 `.xlsx` 支援 | `uv tool install "graphifyy[office]"` |
| `google` | Google 試算表渲染 | `uv tool install "graphifyy[google]"` |
| `video` | 影片/音訊轉錄(faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | MCP stdio 伺服器 | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Neo4j 推送支援 | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | FalkorDB 推送支援 | `uv tool install "graphifyy[falkordb]"` |
| `svg` | SVG 圖譜匯出 | `uv tool install "graphifyy[svg]"` |
| `leiden` | Leiden 社群偵測(僅限 Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Ollama 本機推論 | `uv tool install "graphifyy[ollama]"` |
| `openai` | OpenAI / 相容 OpenAI 的 API | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic Claude API(`--backend claude`,使用 `ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock(使用 IAM,不需要 API 金鑰) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service(`--backend azure`,使用 `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "graphifyy[openai]"` |
| `sql` | SQL schema 擷取 | `uv tool install "graphifyy[sql]"` |
| `postgres` | 即時 PostgreSQL 內省(`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | BYOND DreamMaker `.dm`/`.dme` AST 擷取(若沒有符合你平台的 wheel,可能需要 C 編譯器 + `python3-dev`) | `uv tool install "graphifyy[dm]"` |
| `terraform` | Terraform / HCL `.tf`/`.tfvars`/`.hcl` AST 擷取 | `uv tool install "graphifyy[terraform]"` |
| `pascal` | Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` AST 擷取(更精準的 `calls`/`inherits` 邊;若無此套件則退回使用正規表示式擷取器) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | 中文查詢斷詞(jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | 以上全部 | `uv tool install "graphifyy[all]"` |

</details>

---

## 讓您的助手隨時使用這份圖譜

建好圖譜之後,在你的專案裡執行一次以下指令:

| Platform | Command |
|----------|---------|
| Claude Code | `graphify claude install` |
| CodeBuddy | `graphify codebuddy install` |
| Codex | `graphify codex install` |
| OpenCode | `graphify opencode install` |
| Kilo Code | `graphify kilo install` |
| GitHub Copilot CLI | `graphify copilot install` |
| VS Code Copilot Chat | `graphify vscode install` |
| Aider | `graphify aider install` |
| OpenClaw | `graphify claw install` |
| Factory Droid | `graphify droid install` |
| Trae | `graphify trae install` |
| Trae CN | `graphify trae-cn install` |
| Cursor | `graphify cursor install` |
| Gemini CLI | `graphify gemini install` |
| Hermes | `graphify hermes install` |
| Kimi Code | `graphify install --platform kimi` |
| Amp | `graphify amp install` |
| Agent Skills (cross-framework) | `graphify agents install`(別名 `graphify skills install`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify pi install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

這會寫入一個小型設定檔,告訴你的助手在回答程式碼庫相關問題時要參考知識圖譜,並且優先使用像 `graphify query "<question>"` 這種範圍明確的查詢,而不是讀取完整報告或直接翻找原始檔案。

- **Hook 型平台**(Claude Code、Gemini CLI):在搜尋類工具呼叫之前(在 Claude Code 上,也包含透過 Read/Glob 工具逐一讀取原始碼檔案之前)會自動觸發一個 hook,把你的助手導向圖譜路徑。
- **指令檔型平台**(Codex、OpenCode、Cursor 等):常駐的指令檔(`AGENTS.md`、`.cursor/rules/` 等)會提供同樣「優先查詢」的指引。

`GRAPH_REPORT.md` 仍然可以用來做整體架構的檢視。

**CodeBuddy** 做的事跟 Claude Code 一樣:寫入一段 `CODEBUDDY.md`,告訴 CodeBuddy 在回答架構相關問題之前先讀 `graphify-out/GRAPH_REPORT.md`,並安裝 `PreToolUse` hook(`.codebuddy/settings.json`),在 Bash 搜尋指令與讀檔之前觸發,引導它改用 `graphify query`。

**Codex** 會寫入 `AGENTS.md`,這才是這個平台上真正承載常駐圖譜指引的地方。`graphify codex install` 也會在 `.codex/hooks.json` 註冊一個 `PreToolUse` hook(`graphify hook-check`),但那個項目刻意設計成**空操作**:Codex Desktop 在 `PreToolUse` 上會拒絕 `hookSpecificOutput.additionalContext`,所以在那裡發出提醒會讓 Bash 工具呼叫壞掉。跟 Claude Code 不同——Claude Code 是靠 hook(`graphify hook-guard`)來提醒——在 Codex 上這個 hook 會觸發但故意什麼都不做,`AGENTS.md` 才是常駐運作的機制。

**Kilo Code** 會把 Graphify 技能安裝到 `~/.config/kilo/skills/graphify/SKILL.md`,並把原生的 `/graphify` 指令安裝到 `~/.config/kilo/command/graphify.md`。`graphify kilo install` 也會寫入 `AGENTS.md`,外加一個原生的 `tool.execute.before` 外掛(`.kilo/plugins/graphify.js` + 在 `.kilo/kilo.json` 或 `.kilo/kilo.jsonc` 中註冊),讓 Kilo 透過原生的 `.kilo` 設定得到同樣的常駐圖譜提醒行為。

**Cursor** 會寫入 `.cursor/rules/graphify.mdc` 並設定 `alwaysApply: true`,所以 Cursor 會自動把它納入每一次對話,不需要 hook。

想從所有平台一次移除 graphify:`graphify uninstall`(加上 `--purge` 可以連 `graphify-out/` 一起刪除)。也可以用個別平台的指令(例如 `graphify claude uninstall`)。

---

## 報告內容

- **神級節點** — 你專案中連結數最多的概念。所有東西都會流經這些節點。
- **令人意外的連結** — 分屬不同檔案或模組之間的關聯,依「意外程度」排序。
- **「為什麼」** — 行內註解(`# NOTE:`、`# WHY:`、`# HACK:`)、docstring,以及文件中的設計理由,都會被抽取成獨立節點,連結到它們所解釋的程式碼。
- **建議問題** — 4 到 5 個特別適合用這份圖譜來回答的問題。
- **信心標記** — 每一段推論出來的關係都會標記為 `EXTRACTED`、`INFERRED` 或 `AMBIGUOUS`。你隨時都能分辨哪些是找到的、哪些是猜的。

---

## 支援哪些檔案類型

| 類型 | 副檔名 |
|------|-----------|
| 程式碼(36 種 tree-sitter 文法) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml`(`.dm`/`.dme` 需要 `uv tool install graphifyy[dm]`;`.mts`/`.cts` 沿用 TypeScript 文法,`.cc`/`.cxx` 與 CUDA 的 `.cu`/`.cuh` 以及 Metal 的 `.metal` 沿用 C++ 文法) |
| Salesforce Apex | `.cls .trigger`(以正規表示式為基礎;涵蓋類別、介面、enum、方法、trigger、SOQL/DML 邊) |
| Terraform / HCL | `.tf .tfvars .hcl`(需要 `uv tool install graphifyy[terraform]`) |
| MCP 設定檔 | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — 會擷取伺服器節點、套件參照、環境變數需求 |
| 套件清單 | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — 每個套件(依名稱)產生一個標準化節點,加上 `depends_on` 邊,所以被多份清單參照的套件會是同一個樞紐節點 |
| 文件 | `.md .mdx .qmd .html .txt .rst .yaml .yml`(markdown 的 `[text](./other.md)` 連結與 `[[wikilinks]]` 會變成文件之間的 `references` 邊) |
| Office | `.docx .xlsx`(需要 `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides`(選用功能;需要 `gws` 驗證與 `--google-workspace`;試算表需要 `uv tool install graphifyy[google]`) |
| PDF | `.pdf` |
| 圖片 | `.png .jpg .webp .gif` |
| 影片 / 音訊 | `.mp4 .mov .mp3 .wav` 及更多格式(需要 `uv tool install graphifyy[video]`) |
| YouTube / URL | 任何影片網址(需要 `uv tool install graphifyy[video]`) |

程式碼是**完全在地端擷取、不呼叫任何 API**(透過 tree-sitter 產生 AST)。其他所有內容都會經過你 AI 助手的模型 API。

Google Drive 桌面版的 `.gdoc`、`.gsheet`、`.gslides` 檔案只是捷徑指標,
並不是文件內容本身。若要在無介面(headless)擷取中納入原生的 Google
文件、試算表和簡報,請先安裝並驗證
[`gws` CLI](https://github.com/googleworkspace/cli),然後執行:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

你也可以設定 `GRAPHIFY_GOOGLE_WORKSPACE=1`。Graphify 會把捷徑匯出成
`graphify-out/converted/` 底下的 Markdown 附屬檔案,再擷取那些檔案。

---

## 常用指令

```bash
/graphify .                        # build graph for current folder
/graphify ./docs --update          # re-extract only changed files
/graphify . --cluster-only         # rerun clustering without re-extracting
/graphify . --cluster-only --resolution 1.5      # more granular communities
/graphify . --cluster-only --exclude-hubs 99     # suppress utility super-hubs from god-node rankings
/graphify . --no-viz               # skip the HTML, just the report + JSON
/graphify . --wiki                 # build a markdown wiki from the graph
graphify export callflow-html      # Mermaid architecture/call-flow HTML (auto-regenerates on every git commit if hook is installed)

/graphify query "what connects auth to the database?"
/graphify path "UserService" "DatabasePool"
/graphify explain "RateLimiter"

/graphify add https://arxiv.org/abs/1706.03762   # fetch a paper and add it
/graphify add <youtube-url>                       # transcribe and add a video

graphify hook install              # auto-rebuild on git commit
graphify merge-graphs a.json b.json              # combine two graphs

graphify prs                       # PR dashboard: CI state, review status, worktree mapping
graphify prs 42                    # deep dive on PR #42 with graph impact
graphify prs --triage              # AI ranks your review queue (uses whatever backend is configured)
graphify prs --conflicts           # PRs sharing graph communities — merge-order risk

graphify decouple --project-root .   # risk-scored Extract-Class candidates for god objects
```

見上方的 [Decouple: 根據風險評分的 Extract-Class 候選方案](#decouple-根據風險評分的-extract-class-候選方案),或下方的[完整指令參考](#完整指令參考)。

---

## 忽略檔案

在你的專案根目錄建立 `.graphifyignore` — 語法和 `.gitignore` 一樣,包含 `!` 反向排除。

**`.gitignore` 會自動被遵守。** graphify 會讀取每個目錄裡的 `.gitignore`。如果同時存在 `.graphifyignore`,兩者會**合併** — `.graphifyignore` 的規則會最後套用,所以衝突時以它為準(包含 `!` 反向排除)。新增 `.graphifyignore` 只會排除更多檔案,絕不會把已經被 `.gitignore` 排除的檔案重新納入。子目錄的作用範圍規則跟 git 一樣 — 一個 ignore 檔案只會影響自己那個子樹。

當被 git 忽略的產生檔或轉譯後程式碼也需要納入圖譜時,對 `graphify extract` 傳入 `--no-gitignore`。這會停用 `.gitignore` 和 `.git/info/exclude`;`.graphifyignore` 仍然有效。

```
# .graphifyignore
node_modules/
dist/
*.generated.py

# only index src/, ignore everything else
*
!src/
!src/**
```

---

## 團隊設定

`graphify-out/` 應該要提交進 git,讓團隊裡的每個人一開始就有這份地圖可以用。

**建議加進 `.gitignore` 的項目:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` 現在具備可攜性 — 裡面的 key 都存成相對路徑,並在載入時重新定位,所以提交它是安全的,也能避免第一次 checkout 時要整個重建。

**工作流程:**
1. 由一個人執行 `/graphify .` 並提交 `graphify-out/`。
2. 其他人 pull 下來後 — 他們的助手就能立刻讀取這份圖譜。
3. 執行 `graphify hook install`,在每次 commit 之後自動重建(只用 AST,沒有 API 成本)。這也會設定一個 git merge driver,讓 `graph.json` 永遠不會留下衝突標記 — 兩個開發者同時 commit 時,他們的圖譜會自動做 union merge。
4. 當文件或論文有更動時,執行 `/graphify --update` 來更新那些節點。

---

## 直接使用圖譜

```bash
# query the graph from the terminal
graphify query "show the auth flow"
graphify query "what connects DigestAuth to Response?" --graph graphify-out/graph.json

# expose the graph as an MCP server (for repeated tool-call access)
python -m graphify.serve graphify-out/graph.json
python -m graphify.serve --graph graphify-out/graph.json  # --graph flag also accepted

# register with Kimi Code:
kimi mcp add --transport stdio graphify -- python -m graphify.serve graphify-out/graph.json

# or serve over HTTP so a whole team points at one URL (no local graphify needed):
python -m graphify.serve graphify-out/graph.json --transport http --port 8080
python -m graphify.serve graphify-out/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

MCP 伺服器會給你的助手結構化的存取能力:`query_graph`、`get_node`、`get_neighbors`、`shortest_path`、`list_prs`、`get_pr_impact`、`triage_prs`。

### 共用 HTTP 伺服器

`--transport stdio`(預設值)會替每個開發者各自啟動一個本機伺服器。`--transport http` 則透過 MCP Streamable HTTP transport 提供相同的工具,讓一個共用的行程就能為整個團隊提供圖譜服務 — 客戶端只要把 IDE 的 MCP 設定指向 `http://<host>:8080/mcp`,不需要在本機執行 graphify。

| 參數 | 預設值 | 用途 |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | 要提供服務的 transport |
| `--host` | `127.0.0.1` | HTTP 綁定的主機(用 `0.0.0.0` 可以對外部暴露,不只 localhost) |
| `--port` | `8080` | HTTP 綁定的埠號 |
| `--api-key` | 環境變數 `GRAPHIFY_API_KEY` | 要求 `Authorization: Bearer <key>`(或 `X-API-Key`) |
| `--path` | `/mcp` | HTTP 掛載路徑 |
| `--json-response` | 關閉 | 回傳一般 JSON 而不是 SSE 串流 |
| `--stateless` | 關閉 | 不保留 per-session 狀態(適合負載平衡 / CI 部署) |
| `--session-timeout` | `3600` | 幾秒後回收閒置的 stateful session(`0` 表示停用) |

預設的 `127.0.0.1` 綁定只限本機存取(loopback-only)。要在共用主機上對外開放時,請同時設定 `--host 0.0.0.0` **和** `--api-key`。在容器中執行它:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **WSL / Linux 注意事項:** Ubuntu 內建的是 `python3`,不是 `python`。用虛擬環境(venv)可以避免衝突:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## 環境變數

這些只有在**無介面 / CI 擷取**(`graphify extract`)時才需要。透過你 IDE 裡的 `/graphify` 技能執行時,模型 API 是由你的 IDE session 提供的 — 不需要額外的金鑰。

| 變數 | 用途 | 何時需要 |
|---|---|---|
| `ANTHROPIC_API_KEY` | Claude(Anthropic)後端 | `--backend claude` |
| `ANTHROPIC_BASE_URL` | 相容 Anthropic 的端點網址(LiteLLM proxy、gateway 等) | `--backend claude`(預設:`https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Claude 後端使用的模型名稱 — 若是自訂端點,請用你伺服器實際提供的模型名稱/別名 | `--backend claude`(預設:`claude-sonnet-4-6`) |
| `GEMINI_API_KEY` 或 `GOOGLE_API_KEY` | Google Gemini 後端 | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI 或相容 OpenAI 的 API | `--backend openai`(本機伺服器可接受任何非空字串) |
| `OPENAI_BASE_URL` | 相容 OpenAI 的伺服器網址(llama.cpp、vLLM、LM Studio 等) | `--backend openai`(預設:`https://api.openai.com/v1`) |
| `OPENAI_MODEL` | OpenAI 後端使用的模型名稱 — 若是自架伺服器,請用你伺服器提供的模型名稱/別名(可查它的 `/v1/models` 端點),例如 llama.cpp 用 `LFM2.5-8B-A1B-UD-Q4_K_XL` | `--backend openai`(預設:`gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | DeepSeek 後端 | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Kimi Code 後端 | `--backend kimi` |
| `OLLAMA_BASE_URL` | Ollama 本機推論網址 | `--backend ollama`(預設:`http://localhost:11434`) |
| `OLLAMA_MODEL` | Ollama 模型名稱 | `--backend ollama`(預設:自動偵測) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | 覆寫 Ollama 的 KV-cache 視窗大小 | 選用 — 預設會自動調整大小 |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Ollama 模型保持載入的分鐘數 | 選用 — 設為 `0` 表示每個區塊處理完就卸載 |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI Service 後端 | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | Azure 資源端點網址 | `--backend azure`(需與 API 金鑰一起設定) |
| `AZURE_OPENAI_API_VERSION` | 覆寫 Azure API 版本 | 選用 — 預設 `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` 或 `GRAPHIFY_AZURE_MODEL` | Azure 部署名稱 | 選用 — 預設 `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — 標準憑證鏈 | `--backend bedrock`(不需要 API 金鑰,使用 IAM) |
| `GRAPHIFY_MAX_WORKERS` | AST 平行處理的執行緒數 | 選用 — 也可以用 `--max-workers` 參數 |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | 針對高密度語料庫拉高輸出上限 | 選用 — 例如大型檔案可設為 `32768` |
| `GRAPHIFY_API_TIMEOUT` | HTTP、claude-cli、Anthropic SDK、Bedrock 後端每次呼叫的逾時秒數(預設:600) | 選用 — 也可以用 `--api-timeout` 參數 |
| `GRAPHIFY_MAX_RETRIES` | 遇到速率限制(429)時,放棄前要重試幾次(預設:6;會遵守 `Retry-After`) | 選用 — 針對限制嚴格的機構(例如 kimi)可調高;`0` 表示停用 |
| `GRAPHIFY_FORCE` | 即使節點數變少也強制重建圖譜 | 選用 — 也可以用 `--force` 參數 |
| `GRAPHIFY_GOOGLE_WORKSPACE` | 自動啟用 Google Workspace 匯出 | 選用 — 設為 `1` |
| `GRAPHIFY_TRIAGE_BACKEND` | `graphify prs --triage` 使用的後端 | 選用 — 會依可用的金鑰自動偵測 |
| `GRAPHIFY_TRIAGE_MODEL` | 覆寫 triage 使用的模型 | 選用 — 例如 `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | 設為 `1` 可開啟本機查詢紀錄,寫入 `~/.cache/graphify-queries.log`(記錄每次 query/path/explain 的問題內容 + 語料庫路徑)。預設關閉 — 除非你主動選擇加入,否則不會寫入任何內容(#1797) | 選用 |
| `GRAPHIFY_QUERY_LOG` | 啟用查詢紀錄,並改寫入這個指定路徑 | 選用 — 除非設定這個或 `_ENABLE`,否則預設關閉 |
| `GRAPHIFY_QUERY_LOG_DISABLE` | 設為 `1` 可強制關閉查詢紀錄(優先權高於啟用相關變數) | 選用 |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | 在紀錄功能開啟時,一併記錄完整的子圖回應內容(預設關閉) | 選用 |
| `GRAPHIFY_MAX_GRAPH_BYTES` | 覆寫 512 MiB 的 graph.json 大小上限 — 例如 `700MB`、`2GB` 或純位元組數 | 選用 — 適合非常大的語料庫 |
| `GRAPHIFY_MAX_CONTEXTS` | 單一多專案 MCP 伺服器最多保留的非預設專案圖譜數量 | 選用 — 預設:`8`;無效值會使用 `8`,小於 `1` 的值會使用 `1` |
| `GRAPHIFY_LLM_TEMPERATURE` | 覆寫語意擷取用的 LLM temperature — 例如 `0.7`,或用 `none` 省略此參數 | 選用 — o1/o3/o4/gpt-5 這類推理模型會自動省略 |

---

## 隱私

- **程式碼檔案** — 透過 tree-sitter 在本機處理。任何內容都不會離開你的機器。只有程式碼的語料庫不需要任何 API 金鑰 — `graphify extract` 可以完全離線執行。在混合型 repository 中,加上 `--code-only` 只索引程式碼,跳過原本需要 LLM 的文件/PDF/圖片。
- **影片 / 音訊** — 用 faster-whisper 在本機轉錄。任何內容都不會離開你的機器。
- **文件、PDF、圖片** — 會送到你的 AI 助手做語意擷取(透過 `/graphify` 技能,使用你 IDE session 所執行的任何模型)。無介面的 `graphify extract` 需要 `GEMINI_API_KEY` / `GOOGLE_API_KEY`(Gemini)、`MOONSHOT_API_KEY`(Kimi)、`ANTHROPIC_API_KEY`(Claude)、`OPENAI_API_KEY`(OpenAI)、`DEEPSEEK_API_KEY`(DeepSeek)、一個正在執行的 Ollama 實例(`OLLAMA_BASE_URL`)、透過標準供應鏈提供的 AWS 憑證(Bedrock — 不需要 API 金鑰,使用 IAM),或是 `claude` CLI 執行檔(Claude Code — 不需要 API 金鑰,使用你的 Claude 訂閱)。`--dedup-llm` 參數用的是同一組金鑰。
- **資料落地(Data residency)** — `graphify extract` 會依照哪一組 API 金鑰有設定,自動偵測要使用哪個供應商(優先順序:Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama)。若你的程式碼有資料落地方面的規範限制,請用 `--backend ollama`(完全在地端)或明確指定 `--backend` 參數。Kimi(`MOONSHOT_API_KEY`)會把請求路由到中國的 Moonshot AI 伺服器。
- **沒有遙測**,不追蹤使用情形,沒有任何分析。
- **查詢紀錄** — 每一次 `graphify query`、`graphify path`、`graphify explain`,以及 MCP 的 `query_graph` 呼叫,都會以 JSON Lines 格式記錄到 `~/.cache/graphify-queries.log`(時間戳記、問題內容、語料庫、回傳的節點數、耗時)。預設**不會**儲存完整的子圖回應內容。設定 `GRAPHIFY_QUERY_LOG_DISABLE=1` 可以選擇退出,或設定 `GRAPHIFY_QUERY_LOG=/dev/null` 可以在不停用程式碼路徑的情況下讓紀錄靜默。

---

## 疑難排解

**安裝完後出現 `graphify: command not found`**
CLI 已經安裝好了,但它的 bin 目錄不在你 shell 的 `PATH` 裡。依照你安裝的方式選擇對應的解法:
- **uv**(`uv tool install graphifyy`):指令會放在 uv 的工具 bin 目錄(`~/.local/bin`),在全新的 macOS/zsh 環境中,這個目錄通常不在 `PATH` 上。執行 `uv tool update-shell`,然後開一個新的終端機。(可以用 `uv tool dir --bin` 找到這個目錄。)
- **pipx**(`pipx install graphifyy`):執行 `pipx ensurepath`,然後開一個新的終端機。
- **pip**(`pip install graphifyy`):pip 會把指令安裝到使用者的 bin 目錄,可能不在 `PATH` 上 — 把 `~/Library/Python/3.x/bin`(macOS)或 `~/.local/bin`(Linux)加進你 `~/.zshrc`/`~/.bashrc` 裡的 `PATH`,或者直接執行 `python -m graphify`。

**`uvx graphify …` 或 `uv tool run graphify …` 找不到 `graphify`**
PyPI 上的套件名稱是 `graphifyy`;`graphify` 只是它提供的指令。`uv tool run` 會把第一個字當成*套件名稱*,所以它會去找一個叫做 `graphify` 的套件,並回報 `No solution found … no versions of graphify`。要明確指定套件名稱:`uvx --from graphifyy graphify install`(等同於 `uv tool run --from graphifyy graphify install`)。或者先執行一次 `uv tool install graphifyy`,之後直接呼叫 `graphify` 就好。

**`uv run --with graphifyy python -m graphify` 悄悄執行了舊版安裝**
`uv run` 用的是你*系統*的 Python,所以如果系統裡還有一份較舊的 `graphifyy`(例如之前 `pip install graphifyy` 裝的),Python 可能會在 `sys.path` 裡先找到那一份,`--with graphifyy` 不會覆蓋它。它不會報錯,但你拿到的是*舊版*的行為 — 例如像 `OPENAI_BASE_URL` 這種環境變數覆寫會被悄悄忽略,導致請求打到預設端點,然後回傳一個看起來像金鑰錯誤的 401。判斷特徵是一行 `warning: skill is from graphify <newer>, package is <older>` — 這代表載入的是另一份安裝,而不只是技能檔案過舊。檢查實際載入的是哪一份:
```bash
python -c "import graphify; print(graphify.__file__)"
```
然後直接執行已安裝好的指令(它會用 uv 管理的那一份),或是移除系統裡舊的那份:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` 可以用,但 `graphify` 指令不行**
你 shell 的 `PATH` 沒有包含這個指令安裝到的 bin 目錄。建議優先使用 `uv tool install` / `pipx install` 而不是純 `pip`,然後執行 `uv tool update-shell` / `pipx ensurepath` 並開一個新的終端機(參見上面的安裝說明)。

**在 PowerShell 執行 `/graphify .` 出現「path not recognized」**
PowerShell 會把開頭的 `/` 當成路徑分隔符號。在 Windows 上請用 `graphify .`(不加斜線)。

**`--update` 或重建之後圖譜的節點變少了**
如果重構刪除了檔案,舊節點會殘留下來。傳入 `--force`(或設定 `GRAPHIFY_FORCE=1`)可以在重建結果節點數變少時仍然覆寫。

**`extract` 結束時顯示「extraction was incomplete ... refusing to overwrite」**
當某次擷取過程中途崩潰,或掃描沒能完整讀完語料庫時,這次的結果會比一次完整執行還要小,所以 `graphify extract` 會拒絕用這個不完整的結果覆寫既有、比較大的圖譜(用來保護你的 `graph.json`)。請先修好根本的失敗原因再重跑一次,或是傳入 `--allow-partial` 強制覆寫。

**圖譜裡同一個實體出現重複節點(ghost duplicates)**
「幽靈重複節點」(同一個符號出現兩次 — 一次來自帶有原始碼位置的 AST 擷取,一次來自沒有位置資訊的語意擷取)現在會在建置時自動合併。如果你在 v0.8.33 之前建置的圖譜中看到這個狀況,執行一次完整的重新擷取就能清乾淨:
```bash
graphify extract . --force
```

**Ollama 顯示 VRAM 不足 / 超出 context window**
KV-cache 視窗大小雖然會自動調整,但對你的 GPU 來說可能還是太大。把它調小:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**出現 `LLM returned invalid JSON` / `Unterminated string` 警告**
模型的 JSON 回應碰到輸出 token 上限,在字串中間被截斷了。graphify 會自動復原(它會把區塊拆開重新擷取,而過大的單一文件也會先在標題/段落邊界切開,確保整份檔案還是會被涵蓋到),所以這些警告雖然吵,但不會造成資料遺失。想減少這種狀況,可以拉高輸出上限或縮小每個區塊的輸出:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
如果你用的是像 OpenRouter 這種雲端 gateway,建議用 `--backend openai`(設定 `OPENAI_BASE_URL`)而不是 Ollama 的相容層 — 這是一條更乾淨的 OpenAI 相容路徑。如果模型本身有自己的最大輸出上限,調低 `--token-budget` 會是比較可靠的手段。

**圖譜 HTML 太大,瀏覽器打不開(超過 5000 個節點)**
跳過 HTML 產生,直接用 JSON:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**兩個開發者同時 commit 之後,`graph.json` 出現衝突標記**
執行 `graphify hook install` — 它會設定一個 git merge driver,自動 union merge `graph.json`,讓衝突根本不會發生。

**針對文件或 PDF 的擷取回傳空的節點/邊**
文件、PDF 和圖片都需要呼叫 LLM — 只有程式碼的語料庫不需要金鑰。確認你的 API 金鑰有設定,而且後端設定正確:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**IDE 出現技能版本不符的警告**
你安裝的 graphify 版本跟技能檔案的版本不一樣。更新方式:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**每次執行 `graphify extract` 後,Claude Code 的 prompt 快取都會失效**
Graphify 會把輸出檔案(`graph.json`、`graphify-out/`)寫進你的工作目錄。如果這些路徑沒有被忽略,每一次寫入都會讓 Claude Code 的 prompt 快取失效,下一輪對話就得整份重新上傳,而且是用快取寫入的計價方式。把它們加進 `.claudeignore`:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## 完整指令參考

```
/graphify                          # run on current directory
/graphify ./raw                    # run on a specific folder
/graphify ./raw --mode deep        # more aggressive relationship extraction
graphify extract ./raw --code-only # index code only — local AST, no API key (skips docs/PDFs/images); an `extract` flag, not a skill flag
/graphify ./raw --update           # re-extract only changed files
/graphify ./raw --directed         # preserve edge direction
/graphify ./raw --cluster-only     # rerun clustering on existing graph
/graphify ./raw --no-viz           # skip HTML visualization
/graphify ./raw --obsidian         # generate Obsidian vault
/graphify ./raw --obsidian --obsidian-dir ~/vault  # write into an existing vault (never overwrites your own notes or .obsidian config)
/graphify ./raw --wiki             # build agent-crawlable markdown wiki
/graphify ./raw --svg              # export graph.svg
/graphify ./raw --graphml          # export for Gephi / yEd
/graphify ./raw --neo4j            # generate cypher.txt for Neo4j
/graphify ./raw --neo4j-push bolt://localhost:7687
/graphify ./raw --falkordb         # generate cypher.txt for FalkorDB
/graphify ./raw --falkordb-push falkordb://localhost:6379
/graphify ./raw --watch            # auto-sync as files change
/graphify ./raw --mcp              # start MCP stdio server

/graphify add https://arxiv.org/abs/1706.03762
/graphify add <video-url>
/graphify add https://... --author "Name" --contributor "Name"

/graphify query "what connects attention to the optimizer?"
/graphify query "..." --dfs --budget 1500
/graphify path "DigestAuth" "Response"
/graphify explain "SwinTransformer"

graphify save-result --question "Q" --answer "A" --nodes Foo Bar --outcome useful   # record how a Q&A turned out (work memory; outcome ∈ useful|dead_end|corrected)
graphify reflect                   # aggregate graphify-out/memory/ outcomes into reflections/LESSONS.md
graphify reflect --if-stale        # no-op when LESSONS.md is already newer than every input (cheap to run each session)
graphify reflect --out docs/LESSONS.md    # write the lessons doc somewhere else
graphify reflect --graph graphify-out/graph.json  # group lessons by community + write the work-memory overlay (.graphify_learning.json)
                                   # the overlay tags nodes preferred/tentative/contested (recency-weighted, with provenance);
                                   # graphify explain / query then show a "Lesson:" hint, flagged "code changed — re-verify" when the source moved on

graphify uninstall                 # remove from all platforms in one shot
graphify uninstall --purge         # also delete graphify-out/
graphify uninstall --project --platform codex  # remove project-scoped install files only

graphify hook install              # post-commit + post-checkout hooks
graphify hook uninstall
graphify hook status

# always-on assistant instructions - platform-specific
graphify claude install            # CLAUDE.md + PreToolUse hook (Claude Code)
graphify claude uninstall
graphify codebuddy install         # CODEBUDDY.md + PreToolUse hook (CodeBuddy)
graphify codebuddy uninstall
graphify codex install             # AGENTS.md + PreToolUse hook in .codex/hooks.json (Codex)
graphify opencode install          # AGENTS.md + tool.execute.before plugin (OpenCode)
graphify kilo install              # native Kilo skill + /graphify command + AGENTS.md + .kilo plugin
graphify kilo uninstall
graphify cursor install            # .cursor/rules/graphify.mdc (Cursor)
graphify cursor uninstall
graphify gemini install            # GEMINI.md + BeforeTool hook (Gemini CLI)
graphify gemini uninstall
graphify copilot install           # skill file (GitHub Copilot CLI)
graphify copilot uninstall
graphify aider install             # AGENTS.md (Aider)
graphify aider uninstall
graphify claw install              # AGENTS.md (OpenClaw)
graphify claw uninstall
graphify droid install             # AGENTS.md (Factory Droid)
graphify droid uninstall
graphify trae install              # AGENTS.md (Trae)
graphify trae uninstall
graphify trae-cn install           # AGENTS.md (Trae CN)
graphify trae-cn uninstall
graphify hermes install             # AGENTS.md + ~/.hermes/skills/ (Hermes)
graphify hermes uninstall
graphify amp install               # skill file (Amp)
graphify amp uninstall
graphify agents install            # ~/.agents/skills/ + AGENTS.md (cross-framework; alias: graphify skills)
graphify agents uninstall
graphify kiro install               # .kiro/skills/ + .kiro/steering/graphify.md (Kiro IDE/CLI)
graphify kiro uninstall
graphify pi install                # skill file (Pi coding agent)
graphify pi uninstall
graphify devin install             # skill file + .windsurf/rules/graphify.md (Devin CLI)
graphify devin uninstall
graphify antigravity install       # .agents/rules + .agents/workflows (Google Antigravity)
graphify antigravity uninstall

graphify extract ./docs                        # headless LLM extraction for CI (no IDE needed)
graphify extract ./docs --backend gemini       # explicit backend: gemini, kimi, claude, openai, deepseek, ollama, bedrock, or claude-cli
graphify extract ./docs --backend gemini --model gemini-3.1-pro-preview
graphify extract ./docs --backend ollama       # local Ollama (set OLLAMA_BASE_URL / OLLAMA_MODEL) - no API key needed for loopback
OPENAI_BASE_URL=http://localhost:8080/v1 OPENAI_MODEL=my-model graphify extract ./docs --backend openai   # any OpenAI-compatible server (llama.cpp, vLLM, LM Studio)
ANTHROPIC_BASE_URL=http://localhost:4000 ANTHROPIC_MODEL=my-model graphify extract ./docs --backend claude   # any Anthropic-compatible endpoint (LiteLLM proxy, gateways)
GRAPHIFY_OLLAMA_NUM_CTX=32768 graphify extract ./docs --backend ollama   # override KV-cache window (auto-sized by default)
GRAPHIFY_OLLAMA_KEEP_ALIVE=0 graphify extract ./docs --backend ollama    # unload model after each chunk (saves VRAM on small GPUs)
graphify extract ./docs --backend bedrock      # AWS Bedrock via IAM - no API key, uses AWS credential chain
graphify extract ./docs --backend claude-cli   # route through Claude Code CLI - no API key, uses your Claude subscription
graphify extract ./docs --backend azure        # Azure OpenAI (set AZURE_OPENAI_API_KEY + AZURE_OPENAI_ENDPOINT)
graphify extract ./docs --max-workers 16       # AST parallelism (also GRAPHIFY_MAX_WORKERS)
graphify extract --postgres "postgresql://user:pass@host/db"   # introspect live PostgreSQL schema directly
graphify extract ./my-workspace --cargo        # introspect Rust Cargo workspace dependencies directly
graphify extract ./docs --token-budget 30000   # smaller semantic chunks for local/small models
graphify extract ./docs --max-concurrency 2    # fewer parallel LLM calls (useful for local inference)
graphify extract ./docs --api-timeout 900      # longer HTTP timeout for slow local models (default 600s)
graphify extract ./docs --google-workspace     # export .gdoc/.gsheet/.gslides via gws before extraction
graphify extract ./src --no-gitignore          # include git-ignored source; still honor .graphifyignore
graphify extract ./docs --mode deep            # richer semantic extraction via extended system prompt
graphify extract ./docs --no-cluster           # raw extraction only, skip clustering
graphify extract ./docs --timing               # print per-stage wall-clock timings to stderr (also works on cluster-only)
graphify extract ./docs --force                # overwrite graph.json even if new graph has fewer nodes (use after refactors or to clear ghost duplicates)
graphify extract ./docs --dedup-llm            # LLM tiebreaker for ambiguous entity pairs (uses same API key)
graphify extract ./docs --global --as myrepo   # extract and register into the cross-project global graph
GRAPHIFY_MAX_OUTPUT_TOKENS=32768 graphify extract ./docs --backend claude  # raise output cap for dense corpora

graphify export callflow-html                       # graphify-out/<project>-callflow.html
graphify export callflow-html --max-sections 8      # cap generated architecture sections
graphify export callflow-html --output docs/arch.html
graphify export callflow-html ./some-repo/graphify-out

graphify global add graphify-out/graph.json --as myrepo   # register a project graph into ~/.graphify/global-graph.json
graphify global remove myrepo                         # remove a project from the global graph
graphify global list                                  # show all registered repos + node/edge counts
graphify global path                                  # print path to the global graph file

graphify prs                              # PR dashboard: CI, review, worktree, graph impact
graphify prs 42                           # deep dive on PR #42
graphify prs --triage                     # AI triage ranking (auto-detects backend from env)
graphify prs --worktrees                  # worktree → branch → PR mapping
graphify prs --conflicts                  # PRs sharing graph communities (merge-order risk)
graphify prs --base main                  # filter to PRs targeting a specific base branch
graphify prs --repo owner/repo            # run against a different GitHub repo
GRAPHIFY_TRIAGE_BACKEND=kimi graphify prs --triage   # use a specific backend for triage

graphify clone https://github.com/karpathy/nanoGPT
graphify merge-graphs a.json b.json --out merged.json
graphify --version                                    # print installed version
graphify watch ./src
graphify check-update ./src
graphify update ./src
graphify update ./src --no-cluster  # skip reclustering, write raw AST graph only
graphify update ./src --force       # overwrite even if new graph has fewer nodes
graphify cluster-only ./my-project
graphify cluster-only ./my-project --graph path/to/graph.json  # custom graph location
graphify cluster-only ./my-project --max-concurrency 16 --batch-size 200  # parallel community labeling (large graphs)
graphify cluster-only ./my-project --resolution 1.5            # more, smaller communities
graphify cluster-only ./my-project --exclude-hubs 99           # exclude p99 degree nodes from partitioning
graphify cluster-only ./my-project --no-label                  # keep "Community N" placeholders
graphify cluster-only ./my-project --backend=gemini            # backend for community naming
graphify cluster-only ./my-project --backend=gemini --model gemini-2.5-pro  # specific model
graphify label ./my-project                                    # (re)name communities with the configured backend
graphify label ./my-project --backend=openai --model gpt-4o   # force a specific backend and model

graphify decouple                                    # analyze graphify-out/graph.json, call-graph score only
graphify decouple --graph path/to/graph.json          # custom graph location
graphify decouple --project-root .                    # + the self/this state-sharing check (see language table above)
graphify decouple --top 20                            # analyze more god nodes (default 10)
graphify decouple --min-group-size 2                  # allow smaller candidate groups (default 3)
graphify decouple --net-benefit-threshold 10          # require a bigger margin before recommending a split (default 5.0)
graphify decouple --extracted-only                    # ignore INFERRED/AMBIGUOUS member edges
graphify decouple --no-state-check                    # skip the source re-parse, call-graph-only scoring
graphify decouple --output-dir docs/decouple           # write DECOUPLE_PLAN.md/decouple.json/DECOUPLE.html elsewhere
graphify decouple --no-html                           # skip DECOUPLE.html generation
graphify decouple --json                              # print decouple.json to stdout instead of writing files
```

> **社群名稱:** 在代理型工具內(Claude Code、Gemini CLI)裡,代理本身會自己替社群命名。當你直接執行 CLI 本身時,`cluster-only` 會用設定好的後端(內建或自訂的相容 OpenAI 供應商)自動命名 — 傳入 `--no-label` 可以保留 `Community N`,或執行 `graphify label` 隨時(重新)產生名稱。

---

## 深入了解

- [運作原理](../how-it-works.md) — 擷取流程、社群偵測、信心分數評分、基準測試
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — 模組拆解、如何新增一種語言
- [選用整合功能](../docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — 講述 graphify 背後理念、以及完整架構的書

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) 是建構在 graphify 之上的常駐運作層 — 它把同樣的圖譜方法套用到你的整個工作情境:會議、檔案、文件與程式碼,並且會在背景持續更新。

專為那些工作內容橫跨數百場對話與文件、多到自己都無法完整重建的個人與團隊而打造。

**[加入 graphify.com 的候補名單](https://graphify.com)。** 免費試用即將推出。

---

<details>
<summary>貢獻指南</summary>

### 開發環境設定

本專案在開發流程中使用 [uv](https://docs.astral.sh/uv/)。安裝一次之後:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

驗證 editable 安裝是否成功:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### 執行測試

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> macOS 注意事項:測試套件裡同時有 `sample.f90` 和 `sample.F90` 這兩個 fixture。它們在不區分大小寫的 HFS+ / APFS 檔案系統上會互相衝突。如果你需要同時測試這兩種 Fortran 變體,請在 Linux 或 Docker 容器裡執行。

### Git 工作流程

- 主要開發都在 `v8` 分支上進行。
- Commit 訊息風格:`fix: <description>` / `feat: <description>` / `docs: <description>`
- 開 PR 之前,先執行 `uv run pytest tests/ -q` 並確認測試通過。
- 針對任何新增的語言擷取器,請在 `tests/fixtures/` 新增對應的 fixture 檔案,並在 `tests/test_languages.py` 新增測試。

### 可以貢獻什麼

**實測範例**是最有幫助的貢獻類型。對一個真實的語料庫執行 `/graphify`,把輸出結果存到 `worked/{slug}/`,寫一份誠實的 `review.md`,說明圖譜哪裡做對了、哪裡做錯了,然後開一個 PR。

**擷取相關的 bug** — 開一個 issue,附上輸入檔案、快取項目(`graphify-out/cache/`),以及哪裡被漏掉或搞錯了。

詳見 [ARCHITECTURE.md](../../ARCHITECTURE.md) 了解模組職責與如何新增一種語言。

</details>
