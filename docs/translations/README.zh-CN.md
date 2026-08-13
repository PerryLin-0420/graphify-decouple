<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>fork 自 <a href="https://github.com/Graphify-Labs/graphify">graphify</a>,新增了 <code>graphify decouple</code> 指令</b> —— 面向神级对象的 0-LLM、风险评分 Extract-Class 候选方案,在给出任何建议之前都会针对实际源码(而非只看调用图)重新验证。参见下文的 <a href="#decouple-风险评分的-extract-class-候选方案">Decouple: 风险评分的 Extract-Class 候选方案</a>。
</p>

<div align="center">
<details><summary><b>阅读其他语言版本</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>graphify 平台在 v1 正式版发布前已开放抢先体验:<a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

在你的 AI 编码助手中输入 `/graphify`,它就会把你的整个项目(代码、文档、PDF、图片、视频)映射成一张**知识图谱**,让你可以直接**查询**,而不必再对文件反复 grep。

- **代码映射完全免费、完全本地化。** 代码通过 tree-sitter AST 解析:确定性处理,不需要 LLM,任何内容都不会离开你的机器。(文档、PDF、图片和视频会使用你助手的模型,或你配置的 API key,进行语义分析。)
- **每条边都有解释。** 每个连接都会被标记为 `EXTRACTED`(源码中明确存在)或 `INFERRED`(由 graphify 推断得出),所以你可以清楚区分哪些是直接读取的,哪些是推断出来的。
- **不是向量索引。** 没有 embeddings,没有向量数据库:这是一张你可以真正遍历的图。你可以提问、追踪两个事物之间的路径,或是解释某个概念。

> 想要一个始终在线、在后台持续更新的版本,覆盖你的代码、文档和会议,而不只是按需运行?这正是我们在 **[graphify.com](https://graphify.com)** 打造的东西,抢先体验现已开放:**[app.graphify.com](https://app.graphify.com/login)**。

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="graphify 交互式 graph.html 展示 FastAPI 代码库构建成的力导向知识图谱,并附带检测到的社区图例" width="900">
</p>
<p align="center">
  <em>由 graphify 绘制的 FastAPI 代码库图谱。每个节点都是一个概念,颜色代表检测到的社区,整张图在 graph.html 中都可以点击交互。</em>
</p>

**快速开始**(30 秒):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

然后,在你的 AI 助手中:

```
/graphify .
```

就这样。你会得到**三个文件**:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**支持平台包括** Claude Code、Cursor、Codex、Gemini CLI、GitHub Copilot,以及另外 15 种以上——[选择你的平台](#安装)。

---

## 效果演示

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="graphify path 查询:终端请求 FastAPI 与 ModelField 之间的最短路径,答案会在知识图谱中逐跳点亮显示" width="900">
</p>

图谱构建完成后,你就可以直接查询它,而不必再读文件。以下是在上面展示的 FastAPI 代码库上运行 graphify 得到的真实输出:

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

每条边都带有一个**置信度标签**(`EXTRACTED` = 源码中明确存在,`INFERRED` = 通过推断解析得出),所以你可以分清哪些是直接读取的,哪些是推断出来的。`graphify query "<question>"` 会针对一个自然语言问题返回一个范围受限的子图,而 `graphify path A B` 则会追踪任意两个事物之间的连接方式。

---

## Decouple: 风险评分的 Extract-Class 候选方案

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple:MainWindow 这个神级节点拆分成多个风险评分候选类,其中两个类之间出现共享状态警告" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html:MainWindow 提议拆分出的 5 个类,Node Info 面板打开在 Main Window Axis and Range Controls 上,显示与 Main Window Controller Core 之间有 0.608 的状态重叠" width="900">
</p>
<p align="center">
  <em>在真实项目上运行得到的 DECOUPLE.html——点击任意一个提议的类,就能准确看到它与哪个类共享状态,以及具体共享了什么。</em>
</p>

同一个页面也会直接画出拆分本身。切换 **Preview decoupled view** 会把神级类自己的方法换成提议的类,并就地重新接线——你看到的是接线的变化,而不是另外画一张图:

| 拆分前——今天的神级类 | 拆分后——Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="切换前的 DECOUPLE.html:单个 MainWindow 枢纽节点,自己的方法向四周展开" width="440"> | <img src="../decouple-after.png" alt="切换后的 DECOUPLE.html:同一个节点缩成 5 个菱形的提议类,绿色虚线表示哪些方法被抽取到各个类,红色线表示其中两个类仍共享的实例状态" width="440"> |
| 一个节点里放着自己的 47 个方法,每一个都只能通过这个类才能访问。 | 提议的类。绿色虚线 = 哪些东西被抽取到各个类;红色 = 其中两个类仍然共享的实例状态,而这正是决定 `split` 还是 `keep_as_is` 的关键。只有通过风险阈值的候选才会被画出来——这里是 6 个里的 5 个,所以有一个方法没有对应的菱形可以落脚。 |

`graphify decouple` 会找出神级对象,并告诉你拆分它们是否真的值得——而不只是告诉你它们"很大"。

这个功能要抓的正是这种失败模式:一个有 47 个方法的类,单纯靠调用图聚类会很乐意地把它拆成 5 个看起来很整齐的分组,但这些分组底层其实都在读写同一份 `self._chart_style` / `self._crosshair` 实例状态。就算把这个拆分方案上线,你也并没有真正解耦任何东西——你只是把方法搬到了新文件里,它们依然无法被独立测试、修改或推理,因为它们都还需要传回同一份共享状态。只看调用图的工具根本看不到这一点;必须回到实际源码才行。

**两项检查,都是 0-LLM,都是确定性的:**

1. **这真的是一个神级对象吗?** 一个度数很高的节点,可能是真正的神级对象(有大量属于自己的方法,分散在互不相关的职责上——这时 Extract Class 才适用),也可能只是一个被过度引用的 hub/数据模型(自身方法很少,大多是*被别人引用*——拆分它的方法体没有任何意义,真正该做的是收窄它的接口,而不是拆类)。`classify_god_node` 是靠 `member_ratio` 而不是原始度数来区分这两者——正是这个差异,让 `TraceSource`(84 条边,但只有 6 个属于自己的方法)不会收到一个虚假的拆分建议,而 `MainWindow`(88 条边,47 个属于自己的方法)则会正确地收到拆分建议。
2. **拆分真的能降低耦合吗?** 系统会把 `risk_before`(该神级节点当前的规模/耦合度/碎片化程度)与 `risk_after` 做比较——`risk_after` 是拆分本身会引入的新风险:原本是类内部、不可见的调用边,拆分后会变成显式的类间依赖;调用方现在可能需要依赖不止一个新类;以及——这一点是调用图在结构上根本做不到的——提议的各个分组之间,`self`/`this` 实例状态(读取、写入,以及共享的辅助方法调用,三者分别加权:共享的**写入**权重高于共享的读取)实际重叠了多少。这一步会直接用 tree-sitter 重新解析神级节点自身的源码文件;它不依赖 graphify 自身抽取出的图谱,因为该图谱从不记录任何语言的字段级访问。只有当 `risk_after` 低于 `risk_before` 达到某个阈值时,方案才会建议 `split`;否则结果就是 `marginal` 或 `keep_as_is`,一个不建议拆分的候选会以数字形式呈现,而不会被画成一个还要你凭肉眼去怀疑的图形。

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

会在 `graph.json` 旁边输出三个文件:

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

**状态共享检查的语言覆盖情况**(上面提到的纯调用图分类,对 graphify 能抽取的所有语言都适用;下表专门针对用来验证 `self`/`this` 状态重叠的源码重新解析这一步):

| 语言 | 是否支持 | 备注 |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` 是独立的 AST 节点,而不是被包一层的字段访问——已做专门处理 |
| C# | ✅ | |
| Rust | ✅ | 通过 `impl` 块访问的 `self.x` |
| Ruby | ✅ | `@x`(主流写法)+ `self.foo` 调用 |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | 按方法逐个解析 receiver——Go 没有 `self`/`this` 关键字,所以 receiver 名称(例如 `func (f *Foo) M()` 里的 `f`)每个方法都要重新解析 |
| C | ❌ | struct 指针参数没有任何语法标记能把它和其他参数区分开——没有完整类型推断就没有可靠信号 |

如果神级节点所在的语言不受支持,或者其源码无法读取,就会被标记为 `state_analysis: "skipped"`——分类和调用图评分仍然会照常执行,但最终建议只会基于调用图本身,而不会悄悄假设状态检查已经通过。

---

## graphify 能做什么

开箱即用,你能得到:

| 功能 | 你会得到什么 |
|---|---|
| **神级节点** | 连接最多的概念,让你看清楚一切都会流经哪里 |
| **社区** | 图谱被拆分为多个子系统(使用 Leiden 算法),并附带免 LLM 的标签 |
| **跨文件链接** | 跨约 40 种语言、通过 tree-sitter AST 解析得到的 `calls` / `imports` / `inherits` / `mixes_in` 关系 |
| **查询、路径、解释** | 提问、追踪两个事物之间的路径,或解释某个概念——全部基于 `graph.json` |
| **原因说明 + 文档引用** | `# NOTE:` / `# WHY:` 注释以及 ADR/RFC 引用,会变成与代码相连的一等节点 |
| **不只是代码** | 文档、PDF、图片,以及视频/音频,都会被映射进同一张图谱 |
| **本地优先** | 代码在本地通过 tree-sitter 解析(不需要 LLM,任何内容都不会离开你的机器);只有对文档/媒体做语义分析时才会调用后端,而且只有在你配置了后端的情况下才会调用 |

---

## 基准测试

| 基准测试 | 指标 | graphify | 业界其他方案 |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | QA 准确率 | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | QA 准确率 | **76%** | 与 dense RAG 打平 |
| 构建图谱 | LLM 额度消耗 | **0** | 大多数系统按 token 计费 |

所有系统都在同一套测试框架下、用相同的模型和预算跑测试,并由一个评审模型打分,该评审模型又用第二个评审模型做过盲测校验(一致率 90.6%,Cohen's kappa 0.81)。完整的分系统表格、代码理解(code-intelligence)结果,以及复现命令请见:**[BENCHMARKS.md](../../BENCHMARKS.md)**。

---

## 前置条件

| 需求 | 最低版本 | 检查方式 | 安装方式 |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(推荐)* | 任意版本 | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(备选)* | 任意版本 | `pipx --version` | `pip install pipx` |

**macOS 快速安装(Homebrew):**
```bash
brew install python@3.12 uv
```

**Windows 快速安装:**
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

## 安装

> **官方包:** PyPI 上的包名是 `graphifyy`(双写 y)。PyPI 上其他 `graphify*` 开头的包与本项目无关。CLI 命令依然是 `graphify`。

**第一步——安装包:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**第二步——把 skill 注册到你的 AI 助手:**

```bash
graphify install
```

就这样。打开你的 AI 助手,输入 `/graphify .`

如果想把助手 skill 安装到当前仓库,而不是你的用户 profile 目录下,加上 `--project`:

```bash
graphify install --project
graphify install --project --platform codex
```

项目范围内的安装,会把文件写到当前目录下,例如
`.claude/skills/graphify/SKILL.md` 或 `.agents/skills/graphify/SKILL.md`(外加一个
skill 按需加载的 `references/` sidecar),并会为可以提交的文件打印出
`git add` 提示。
支持项目范围安装的各平台专属命令都接受同一个参数,
例如 `graphify claude install --project` 或 `graphify codex install --project`。

> **PowerShell 提示:** 请使用 `graphify .` 而不是 `/graphify .`——在 PowerShell 中,开头的斜杠会被当成路径分隔符。

> **提示 `graphify: command not found`?** `uv tool install` / `pipx install` 会把 `graphify` 命令放进它们各自的 tool bin 目录(`~/.local/bin`)。如果安装完你的 shell 马上就找不到这个命令——在全新的 macOS + zsh 环境下很常见——说明这个目录还没加入你的 `PATH`:运行 `uv tool update-shell`(或 `pipx ensurepath`),然后打开一个新终端。如果用的是原生 `pip`,把 `~/.local/bin`(Linux)或 `~/Library/Python/3.x/bin`(Mac)加入你的 PATH,或者直接运行 `python -m graphify`。

> **想用 `uvx` / `uv tool run` 直接运行而不安装?** 要写包名,而不是命令名:`uvx --from graphifyy graphify install`。直接写 `uvx graphify …` 会失败(报错 `No solution found … no versions of graphify`),因为 `uv tool run` 会把第一个词当成*包名*来解析,而这个包其实叫 `graphifyy`——`graphify` 命令是包在里面的。

> **在 Mac/Windows 上请尽量避免用 `pip install`。** skill 在运行时会从 `graphify-out/.graphify_python` 解析 Python 环境;如果这个路径指向的环境和 `pip` 安装包时用的环境不一样,你就会遇到 `ModuleNotFoundError: No module named 'graphify'`。`uv tool install` 和 `pipx install` 会把这个包隔离在各自独立的环境中,完全避免这个问题。

> **Git hooks 与 uv tool / pipx:** `graphify hook install` 会在安装时把当前解释器的路径直接写死进 hook 脚本里,所以即使在 `~/.local/bin` 不在 PATH 里的 GUI git 客户端或 CI runner 中,post-commit hook 也能正常触发。如果你重新安装或升级了 graphify,请重新运行一次 `graphify hook install` 来刷新写死的路径。

> **严格模式(Claude Code):** `graphify install --project --strict` 会让助手真正去使用图谱。默认安装只是*提示*助手在读文件之前先运行 `graphify query`;严格模式则会*拦截*一个会话里第一次读取原始源码的动作,把它重定向到图谱,之后再恢复为提示模式(所以每个会话最多只会触发一次,也不会卡住)。可以在运行时用 `GRAPHIFY_HOOK_STRICT=1`/`0` 切换;默认安装行为不受影响(依然是软提示)。

<details>
<summary><b>选择你的平台</b>(20 多种助手,点击展开)</summary>

| 平台 | 安装命令 |
|----------|----------------|
| Claude Code (Linux/Mac) | `graphify install` |
| Claude Code (Windows) | `graphify install` (auto-detected) or `graphify install --platform windows` |
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
| Agent Skills (cross-framework) | `graphify install --platform agents` (alias `--platform skills`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify install --platform pi` |
| Cursor | `graphify cursor install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

Codex 用户还需要在 `~/.codex/config.toml` 的 `[features]` 下开启 `multi_agent = true`,才能进行并行提取。CodeBuddy 使用的是与 Claude Code 相同的 Agent 工具和 PreToolUse hook 机制。Factory Droid 使用 `Task` 工具进行并行子代理调度。OpenClaw 和 Aider 目前使用的是顺序提取(这两个平台的并行 agent 支持还比较早期)。Trae 使用 Agent 工具进行并行子代理调度,并且**不**支持 `PreToolUse` hook,所以 AGENTS.md 是它的常驻机制。

`--platform agents`(别名 `--platform skills`)针对的是通用的跨框架 [Agent-Skills](https://github.com/anthropics/skills) 位置:全局安装时用规范定义的用户级全局目录 `~/.agents/skills/`(由 `npx skills` 以及符合该规范的框架读取),项目级(`--project`)安装则用 `./.agents/skills/`。而单纯的 `graphify install` 在设计上就只针对单一平台(Claude Code)——如果你想让任何读取 `.agents/skills` 的框架都能发现这个 skill,就该用专门的 `agents` 平台。

> Codex 使用 `$graphify` 而不是 `/graphify`。

</details>

<details>
<summary><b>可选扩展</b>(按需安装)</summary>

| 扩展 | 新增功能 | 安装方式 |
|---|---|---|
| `pdf` | PDF 提取 | `uv tool install "graphifyy[pdf]"` |
| `office` | `.docx` 和 `.xlsx` 支持 | `uv tool install "graphifyy[office]"` |
| `google` | Google Sheets 渲染 | `uv tool install "graphifyy[google]"` |
| `video` | 视频/音频转录(faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | MCP stdio 服务器 | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Neo4j 推送支持 | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | FalkorDB 推送支持 | `uv tool install "graphifyy[falkordb]"` |
| `svg` | SVG 图谱导出 | `uv tool install "graphifyy[svg]"` |
| `leiden` | Leiden 社区发现算法(仅限 Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Ollama 本地推理 | `uv tool install "graphifyy[ollama]"` |
| `openai` | OpenAI / OpenAI 兼容 API | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic Claude API(`--backend claude`,使用 `ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock(使用 IAM,不需要 API key) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service(`--backend azure`,使用 `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "graphifyy[openai]"` |
| `sql` | SQL schema 提取 | `uv tool install "graphifyy[sql]"` |
| `postgres` | 实时 PostgreSQL 内省(`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | BYOND DreamMaker `.dm`/`.dme` AST 提取(如果没有匹配你平台的 wheel,可能需要 C 编译器 + `python3-dev`) | `uv tool install "graphifyy[dm]"` |
| `terraform` | Terraform / HCL `.tf`/`.tfvars`/`.hcl` AST 提取 | `uv tool install "graphifyy[terraform]"` |
| `pascal` | Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` AST 提取(`calls`/`inherits` 边更准确;缺失时会退回到基于正则表达式的提取器) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | 中文查询分词(jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | 以上全部功能 | `uv tool install "graphifyy[all]"` |

</details>

---

## 让你的助手始终使用图谱

构建好图谱之后,在你的项目里运行一次:

| 平台 | 命令 |
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
| Agent Skills (cross-framework) | `graphify agents install` (alias `graphify skills install`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify pi install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

这会写入一个小配置文件,告诉你的助手在回答代码库相关问题时先查阅知识图谱,优先使用像 `graphify query "<question>"` 这样范围受限的查询,而不是去读完整报告或对原始文件做 grep。

- **支持 hook 的平台**(Claude Code、Gemini CLI):在执行搜索类工具调用之前(在 Claude Code 上,还包括在通过 Read/Glob 工具逐个读取源码文件之前),会自动触发一个 hook,把你的助手引导去走图谱这条路径。
- **依赖指令文件的平台**(Codex、OpenCode、Cursor 等):持久化的指令文件(`AGENTS.md`、`.cursor/rules/` 等)提供同样的"优先查询图谱"引导。

`GRAPH_REPORT.md` 仍然可以用于整体架构层面的审阅。

**CodeBuddy** 会做和 Claude Code 一样的两件事:在 `CODEBUDDY.md` 中写入一段内容,告诉 CodeBuddy 在回答架构问题之前先读 `graphify-out/GRAPH_REPORT.md`;并安装 `PreToolUse` hook(写入 `.codebuddy/settings.json`),在执行 Bash 搜索命令和文件读取之前触发,引导它改用 `graphify query`。

**Codex** 会写入 `AGENTS.md`,这才是在该平台上真正承载常驻图谱引导的机制。`graphify codex install` 也会在 `.codex/hooks.json` 中注册一个 `PreToolUse` hook(`graphify hook-check`),但这个条目故意被设计成**空操作**:Codex Desktop 会拒绝 `PreToolUse` 上的 `hookSpecificOutput.additionalContext`,所以在这里发出提示会导致 Bash 工具调用失败。与 Claude Code 不同(在 Claude Code 上是 hook `graphify hook-guard` 负责发出提示),在 Codex 上这个 hook 会触发,但故意什么都不做,`AGENTS.md` 才是真正的常驻机制。

**Kilo Code** 会把 Graphify skill 安装到 `~/.config/kilo/skills/graphify/SKILL.md`,并把原生 `/graphify` 命令安装到 `~/.config/kilo/command/graphify.md`。`graphify kilo install` 还会写入 `AGENTS.md`,以及一个原生的 `tool.execute.before` 插件(`.kilo/plugins/graphify.js` + `.kilo/kilo.json` 或 `.kilo/kilo.jsonc` 注册),这样 Kilo 就能通过原生的 `.kilo` 配置获得同样的常驻图谱提醒行为。

**Cursor** 会写入带有 `alwaysApply: true` 的 `.cursor/rules/graphify.mdc`,所以 Cursor 会在每次对话中自动包含它,不需要 hook。

如果想一次性从所有平台移除 graphify:运行 `graphify uninstall`(加上 `--purge` 可以连 `graphify-out/` 一起删除)。也可以使用各平台专属的命令(例如 `graphify claude uninstall`)。

---

## 报告里有什么

- **神级节点** —— 你项目中连接最多的概念。所有东西几乎都会流经这些节点。
- **意外连接(Surprising connections)** —— 存在于不同文件或模块之间的关联,按"有多出人意料"排序。
- **"为什么"** —— 行内注释(`# NOTE:`、`# WHY:`、`# HACK:`)、docstring,以及文档中的设计理由,都会被抽取为独立节点,并与它们所解释的代码相连。
- **建议提问(Suggested questions)** —— 4 到 5 个图谱特别擅长回答的问题。
- **置信度标签(Confidence tags)** —— 每一条被推断出的关系都会标记为 `EXTRACTED`、`INFERRED` 或 `AMBIGUOUS`。你始终清楚哪些是找到的事实,哪些是猜测。

---

## 支持处理哪些文件

| 类型 | 扩展名 |
|------|-----------|
| 代码(36 种 tree-sitter 语法) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml`(`.dm`/`.dme` 需要 `uv tool install graphifyy[dm]`;`.mts`/`.cts` 复用 TypeScript 语法,`.cc`/`.cxx` 以及 CUDA 的 `.cu`/`.cuh` 和 Metal 的 `.metal` 复用 C++ 语法) |
| Salesforce Apex | `.cls .trigger`(基于正则表达式;支持 classes、interfaces、enums、methods、triggers、SOQL/DML 边) |
| Terraform / HCL | `.tf .tfvars .hcl`(需要 `uv tool install graphifyy[terraform]`) |
| MCP 配置文件 | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` —— 抽取 server 节点、包引用、环境变量需求 |
| 包清单文件(Package manifests) | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` —— 每个包(按名称)对应一个规范化的包节点,外加 `depends_on` 边,所以一个被多份清单引用的包会合并成同一个 hub 节点 |
| 文档 | `.md .mdx .qmd .html .txt .rst .yaml .yml`(markdown 里的 `[text](./other.md)` 链接和 `[[wikilinks]]` 会变成文档之间的 `references` 边) |
| Office 文档 | `.docx .xlsx`(需要 `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides`(需要手动开启;需要 `gws` 认证和 `--google-workspace`;Sheets 还需要 `uv tool install graphifyy[google]`) |
| PDF | `.pdf` |
| 图片 | `.png .jpg .webp .gif` |
| 视频 / 音频 | `.mp4 .mov .mp3 .wav` 以及更多格式(需要 `uv tool install graphifyy[video]`) |
| YouTube / URL | 任意视频 URL(需要 `uv tool install graphifyy[video]`) |

代码是**完全本地提取、不需要任何 API 调用**的(通过 tree-sitter 生成 AST)。其他所有内容都会经过你的 AI 助手的模型 API。

Google Drive for desktop 生成的 `.gdoc`、`.gsheet`、`.gslides` 文件只是快捷方式指针,
并不包含文档内容本身。如果想在无头(headless)提取中纳入原生的 Google Docs、Sheets 和 Slides,
请先安装并登录 [`gws` CLI](https://github.com/googleworkspace/cli),然后运行:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

你也可以设置 `GRAPHIFY_GOOGLE_WORKSPACE=1`。Graphify 会把这些快捷方式导出成 Markdown sidecar 文件,放进
`graphify-out/converted/`,然后再提取这些文件。

---

## 常用命令

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

参见上文的 [Decouple: 风险评分的 Extract-Class 候选方案](#decouple-风险评分的-extract-class-候选方案),或下文的[完整命令参考](#完整命令参考)。

---

## 忽略文件

在你的项目根目录创建一个 `.graphifyignore` 文件——语法和 `.gitignore` 完全一样,包括 `!` 取反语法。

**`.gitignore` 会被自动遵守。** graphify 会读取每个目录下的 `.gitignore`。如果同时存在 `.graphifyignore`,两者会被**合并**——`.graphifyignore` 的规则最后生效,所以出现冲突时以它为准(包括 `!` 取反规则)。添加 `.graphifyignore` 只会排除更多文件,永远不会重新纳入一个已经被 `.gitignore` 排除的文件。子目录的作用范围和 git 的行为一致——一个 ignore 文件只会影响它自己所在的子树。

如果被 git 忽略的生成代码或转译代码也应该被纳入图谱,给 `graphify extract` 加上 `--no-gitignore`。这会禁用 `.gitignore` 和 `.git/info/exclude`;`.graphifyignore` 依然会生效。

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

## 团队协作设置

`graphify-out/` 是打算被提交到 git 里的,这样团队里的每个人一开始就能拿到一张地图。

**建议在 `.gitignore` 中加入:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` 现在是可移植的——key 以相对路径存储,加载时会重新锚定,所以提交它是安全的,并且可以避免第一次 checkout 时整个重新构建。

**工作流:**
1. 由一个人运行 `/graphify .`,并提交 `graphify-out/`。
2. 其他人拉取代码——他们的助手会立刻读取这张图谱。
3. 运行 `graphify hook install`,让图谱在每次 commit 后自动重建(只用 AST,没有 API 成本)。这一步还会设置一个 git merge driver,让 `graph.json` 永远不会留下冲突标记——两个开发者并行提交时,他们的图谱会自动做 union 合并。
4. 当文档或论文发生变化时,运行 `/graphify --update` 来刷新对应的节点。

---

## 直接使用图谱

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

MCP 服务器会给你的助手提供结构化访问能力:`query_graph`、`get_node`、`get_neighbors`、`shortest_path`、`list_prs`、`get_pr_impact`、`triage_prs`。

### 共享 HTTP 服务器

`--transport stdio`(默认值)会为每个开发者各自启动一个本地服务器。`--transport http` 则会通过 MCP Streamable HTTP 传输协议提供同样的工具,所以一个共享进程就能为整个团队提供图谱服务——客户端只需把 IDE 的 MCP 配置指向 `http://<host>:8080/mcp`,而不必在本地运行 graphify。

| 参数 | 默认值 | 用途 |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | 使用的传输协议 |
| `--host` | `127.0.0.1` | HTTP 绑定地址(用 `0.0.0.0` 可以让服务暴露到 localhost 之外) |
| `--port` | `8080` | HTTP 绑定端口 |
| `--api-key` | env `GRAPHIFY_API_KEY` | 要求请求携带 `Authorization: Bearer <key>`(或 `X-API-Key`) |
| `--path` | `/mcp` | HTTP 挂载路径 |
| `--json-response` | off | 返回纯 JSON,而不是 SSE 流 |
| `--stateless` | off | 不保留每个会话的状态(适用于负载均衡 / CI 部署场景) |
| `--session-timeout` | `3600` | 在 N 秒后回收空闲的有状态会话(`0` 表示禁用) |

默认绑定的 `127.0.0.1` 只能在本机回环访问。如果要在共享主机上对外暴露,请**同时**设置 `--host 0.0.0.0` 和 `--api-key`。在容器中运行:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **WSL / Linux 提示:** Ubuntu 自带的是 `python3`,而不是 `python`。用虚拟环境(venv)可以避免冲突:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## 环境变量

以下环境变量只有在**无头 / CI 提取**(`graphify extract`)场景下才需要。如果是在你的 IDE 里通过 `/graphify` skill 运行,模型 API 由你的 IDE 会话提供——不需要额外的 key。

| 变量 | 用途 | 何时需要 |
|---|---|---|
| `ANTHROPIC_API_KEY` | Claude(Anthropic)后端 | `--backend claude` |
| `ANTHROPIC_BASE_URL` | Anthropic 兼容端点 URL(LiteLLM 代理、网关等) | `--backend claude`(默认值:`https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Claude 后端使用的模型名——如果是自定义端点,用你服务器暴露出来的模型名/别名 | `--backend claude`(默认值:`claude-sonnet-4-6`) |
| `GEMINI_API_KEY` or `GOOGLE_API_KEY` | Google Gemini 后端 | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI 或 OpenAI 兼容 API | `--backend openai`(本地服务器接受任意非空值) |
| `OPENAI_BASE_URL` | OpenAI 兼容服务器 URL(llama.cpp、vLLM、LM Studio 等) | `--backend openai`(默认值:`https://api.openai.com/v1`) |
| `OPENAI_MODEL` | OpenAI 后端使用的模型名——如果是自建服务器,用你服务器暴露出来的模型名/别名(可查它的 `/v1/models` 接口),例如 llama.cpp 里的 `LFM2.5-8B-A1B-UD-Q4_K_XL` | `--backend openai`(默认值:`gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | DeepSeek 后端 | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Kimi Code 后端 | `--backend kimi` |
| `OLLAMA_BASE_URL` | Ollama 本地推理 URL | `--backend ollama`(默认值:`http://localhost:11434`) |
| `OLLAMA_MODEL` | Ollama 模型名 | `--backend ollama`(默认:自动检测) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | 覆盖 Ollama KV-cache 窗口大小 | 可选——默认自动确定大小 |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Ollama 模型保持加载的分钟数 | 可选——设为 `0` 表示每处理完一个 chunk 就卸载 |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI Service 后端 | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | Azure 资源端点 URL | `--backend azure`(需要和 API key 一起提供) |
| `AZURE_OPENAI_API_VERSION` | 覆盖 Azure API 版本 | 可选——默认 `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` or `GRAPHIFY_AZURE_MODEL` | Azure 部署名称 | 可选——默认 `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock——标准凭证链 | `--backend bedrock`(不需要 API key,使用 IAM) |
| `GRAPHIFY_MAX_WORKERS` | AST 并行线程数 | 可选——也可以用 `--max-workers` 参数 |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | 为内容密集的语料提高输出上限 | 可选——例如大文件可以设为 `32768` |
| `GRAPHIFY_API_TIMEOUT` | HTTP、claude-cli、Anthropic SDK 和 Bedrock 后端的单次调用超时秒数(默认:600) | 可选——也可以用 `--api-timeout` 参数 |
| `GRAPHIFY_MAX_RETRIES` | 遇到限流(429)请求时的最大重试次数(默认:6;会遵循 `Retry-After`) | 可选——如果所在组织限流较严格(例如 kimi)可以调高;`0` 表示禁用 |
| `GRAPHIFY_FORCE` | 即使节点更少也强制重建图谱 | 可选——也可以用 `--force` 参数 |
| `GRAPHIFY_GOOGLE_WORKSPACE` | 自动开启 Google Workspace 导出 | 可选——设为 `1` |
| `GRAPHIFY_TRIAGE_BACKEND` | `graphify prs --triage` 使用的后端 | 可选——会根据现有的 key 自动检测 |
| `GRAPHIFY_TRIAGE_MODEL` | 覆盖 triage 使用的模型 | 可选——例如 `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | 设为 `1` 可开启本地查询日志(路径为 `~/.cache/graphify-queries.log`,记录每次 query/path/explain 的问题内容 + 语料路径)。默认关闭——除非你主动开启,否则不会写入任何内容(#1797) | 可选 |
| `GRAPHIFY_QUERY_LOG` | 开启查询日志,并把它写到这个路径,而不是默认路径 | 可选——除非设置了这个变量或 `_ENABLE`,否则默认关闭 |
| `GRAPHIFY_QUERY_LOG_DISABLE` | 设为 `1` 可强制关闭查询日志(优先级高于开启相关的变量) | 可选 |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | 日志开启时,同时记录完整的子图响应内容(默认关闭) | 可选 |
| `GRAPHIFY_MAX_GRAPH_BYTES` | 覆盖 `graph.json` 默认 512 MiB 的大小上限——例如 `700MB`、`2GB`,或直接写字节数 | 可选——适用于非常大的语料 |
| `GRAPHIFY_MAX_CONTEXTS` | 一个多项目 MCP 服务器最多保留的非默认项目图谱数量 | 可选——默认:`8`;非法值会使用 `8`,小于 `1` 的值会使用 `1` |
| `GRAPHIFY_LLM_TEMPERATURE` | 覆盖语义提取使用的 LLM temperature——例如 `0.7`,或设为 `none` 表示不传该参数 | 可选——对 o1/o3/o4/gpt-5 等推理模型会自动省略 |

---

## 隐私

- **代码文件** —— 通过 tree-sitter 在本地处理。任何内容都不会离开你的机器。纯代码语料不需要任何 API key——`graphify extract` 可以完全离线运行。在混合仓库中,加上 `--code-only` 就只会索引代码,跳过原本需要 LLM 处理的文档/PDF/图片。
- **视频 / 音频** —— 使用 faster-whisper 在本地转录。任何内容都不会离开你的机器。
- **文档、PDF、图片** —— 会发送给你的 AI 助手做语义提取(通过 `/graphify` skill,使用你 IDE 会话所运行的任意模型)。无头模式下的 `graphify extract` 需要 `GEMINI_API_KEY` / `GOOGLE_API_KEY`(Gemini)、`MOONSHOT_API_KEY`(Kimi)、`ANTHROPIC_API_KEY`(Claude)、`OPENAI_API_KEY`(OpenAI)、`DEEPSEEK_API_KEY`(DeepSeek)、一个正在运行的 Ollama 实例(`OLLAMA_BASE_URL`)、通过标准凭证链提供的 AWS 凭证(Bedrock——不需要 API key,使用 IAM),或者 `claude` CLI 可执行文件(Claude Code——不需要 API key,使用你的 Claude 订阅)。`--dedup-llm` 参数用的是同一个 key。
- **数据落地(Data residency)** —— `graphify extract` 会根据设置了哪个 API key 自动检测使用哪个提供方(优先级:Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama)。如果代码有数据落地方面的要求,请使用 `--backend ollama`(完全本地)或显式传入 `--backend` 参数。Kimi(`MOONSHOT_API_KEY`)会把请求路由到位于中国的 Moonshot AI 服务器。
- **没有遥测**,没有使用情况追踪,没有数据分析。
- **查询日志** —— 每一次 `graphify query`、`graphify path`、`graphify explain` 以及 MCP 的 `query_graph` 调用,都会以 JSON Lines 格式记录到 `~/.cache/graphify-queries.log`(时间戳、问题内容、语料、返回的节点、耗时)。默认**不会**存储完整的子图响应。设置 `GRAPHIFY_QUERY_LOG_DISABLE=1` 可以退出记录,或者设置 `GRAPHIFY_QUERY_LOG=/dev/null` 在不禁用相关代码路径的情况下让日志静默。

---

## 疑难排解

**安装后出现 `graphify: command not found`**
CLI 已经安装好了,但它的 bin 目录不在你 shell 的 `PATH` 里。根据你的安装方式选择对应的修复方法:
- **uv**(`uv tool install graphifyy`):命令会落在 uv 的 tool bin 目录(`~/.local/bin`),全新的 macOS/zsh 环境通常没有把它加进 `PATH`。运行 `uv tool update-shell`,然后打开一个新终端。(可以用 `uv tool dir --bin` 找到这个目录。)
- **pipx**(`pipx install graphifyy`):运行 `pipx ensurepath`,然后打开一个新终端。
- **pip**(`pip install graphifyy`):pip 会把脚本安装到一个用户 bin 目录,这个目录可能不在 `PATH` 里——在 `~/.zshrc`/`~/.bashrc` 中把 `~/Library/Python/3.x/bin`(macOS)或 `~/.local/bin`(Linux)加入你的 `PATH`,或者直接运行 `python -m graphify`。

**`uvx graphify …` 或 `uv tool run graphify …` 无法解析出 `graphify`**
PyPI 上的包名是 `graphifyy`;`graphify` 只是它提供的命令名。`uv tool run` 会把第一个词当成*包名*来处理,所以它会去找一个叫 `graphify` 的包,并报错 `No solution found … no versions of graphify`。请显式指定包名:`uvx --from graphifyy graphify install`(等价于 `uv tool run --from graphifyy graphify install`)。或者先执行一次 `uv tool install graphifyy`,之后直接调用 `graphify` 即可。

**`uv run --with graphifyy python -m graphify` 会悄悄运行一个更旧的安装版本**
`uv run` 用的是你*系统*的 Python,所以如果系统里还留着一个更旧的 `graphifyy`(比如之前执行过 `pip install graphifyy`),Python 会在 `sys.path` 里先找到那个旧版本,`--with graphifyy` 并不会覆盖它。运行时不会报错,但你得到的其实是*旧版本*的行为——例如 `OPENAI_BASE_URL` 这类环境变量覆盖会被悄悄忽略,导致请求打到默认端点,并返回一个看起来像 key 错误的 401。这种情况的标志是一行 `warning: skill is from graphify <newer>, package is <older>`——这说明加载的是另一个安装版本,而不只是 skill 文件过期。可以这样检查实际加载的是哪个版本:
```bash
python -c "import graphify; print(graphify.__file__)"
```
然后直接运行已安装的命令(它用的是 uv 管理的那份副本),或者删掉过期的系统副本:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` 能用,但 `graphify` 命令不行**
你 shell 的 `PATH` 里没有包含命令被安装到的那个 bin 目录。相比原生 `pip`,更推荐使用 `uv tool install` / `pipx install`,然后运行 `uv tool update-shell` / `pipx ensurepath` 并打开一个新终端(参见上面的安装说明)。

**在 PowerShell 中,`/graphify .` 会报 "path not recognized"**
PowerShell 会把开头的 `/` 当成路径分隔符。在 Windows 上请使用 `graphify .`(不带斜杠)。

**执行 `--update` 或重建后,图谱节点变少了**
如果一次重构删除了文件,旧节点会残留下来。加上 `--force`(或设置 `GRAPHIFY_FORCE=1`)可以在重建结果节点更少的情况下依然覆盖写入。

**`extract` 退出并提示 "extraction was incomplete ... refusing to overwrite"**
当一次提取过程崩溃,或者遍历没能完整读完整个语料时,这次运行的结果会比完整运行的结果小,所以 `graphify extract` 会拒绝用这个不完整的结果去覆盖一个更大的既有图谱(以保护你的 `graph.json`)。请先修复根本原因再重新运行,或者加上 `--allow-partial` 强制覆盖。

**同一个实体在图谱里出现了重复节点(幽灵重复)**
幽灵重复(同一个符号出现两次——一次来自带源码位置的 AST 提取,一次来自不带源码位置的语义提取)现在会在构建时自动合并。如果你在 v0.8.33 之前构建的图谱里看到这个问题,运行一次完整的重新提取来清理:
```bash
graphify extract . --force
```

**Ollama 显存不足 / 超出上下文窗口**
KV-cache 窗口大小是自动确定的,但对你的 GPU 来说可能还是太大了。可以调小它:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**出现 `LLM returned invalid JSON` / `Unterminated string` 警告**
模型的 JSON 响应触碰到了输出 token 上限,在字符串中途被截断。graphify 会自动恢复(它会把这个 chunk 拆开、分别重新提取,而一份过大的单一文档会先按标题/段落边界切分,以确保整个文件依然被完整覆盖),所以这些警告只是噪音,并不代表数据丢失。要减少这类情况,可以提高输出上限,或缩小每个 chunk 的输出:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
如果用的是像 OpenRouter 这样的云端网关,相比 Ollama shim,更建议使用 `--backend openai`(设置 `OPENAI_BASE_URL`)——这是一条更干净的 OpenAI 兼容路径。如果模型本身有自己的最大输出上限,调低 `--token-budget` 是更可靠的手段。

**图谱 HTML 太大,浏览器打不开(节点数 > 5000)**
跳过 HTML 生成,直接使用 JSON:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**两个开发者同时提交后,`graph.json` 出现了冲突标记**
运行 `graphify hook install`——它会设置一个 git merge driver,自动对 `graph.json` 做 union 合并,这样就不会再出现冲突。

**文档或 PDF 提取出来的节点/边是空的**
文档、PDF 和图片需要调用 LLM——纯代码语料不需要 key。请检查你的 API key 是否设置正确,以及后端是否正确:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**IDE 中出现 skill 版本不匹配的警告**
你安装的 graphify 版本和 skill 文件对不上。更新方法:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**每次 `graphify extract` 之后,Claude Code 的 prompt cache 都会失效**
Graphify 会把输出文件(`graph.json`、`graphify-out/`)写进工作区。如果这些路径没有被忽略,每次写入都会让 Claude Code 的 prompt cache 失效,导致下一轮对话时不得不按 cache-write 的费率重新完整上传一次。请把它们加入 `.claudeignore`:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## 完整命令参考

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

> **社区命名:** 在 agent 环境中(Claude Code、Gemini CLI),命名社区的工作由 agent 自己完成。如果直接运行裸 CLI,`cluster-only` 会用已配置的后端(内置的,或自定义的 OpenAI 兼容提供方)自动命名——传入 `--no-label` 可以保留 `Community N` 这种占位名,或者运行 `graphify label` 按需(重新)生成名称。

---

## 了解更多

- [工作原理](../how-it-works.md) —— 提取流水线、社区发现、置信度评分、基准测试
- [ARCHITECTURE.md](../../ARCHITECTURE.md) —— 模块拆解,以及如何新增一种语言支持
- [可选集成](../docker-mcp-sqlite.md) —— Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) —— 讲述 graphify 背后理念的书,完整梳理其架构

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) 是构建在 graphify 之上的常驻层——它把同样的图谱方法应用到你整个工作场景:会议、文件、文档和代码,并在后台持续更新。

专为这样的个人和团队打造:他们的工作分散在成百上千场对话和文档里,靠自己永远无法完整重建。

**[前往 graphify.com 加入候补名单](https://graphify.com)。** 免费试用即将上线。

---

<details>
<summary>贡献指南</summary>

### 开发环境搭建

本项目使用 [uv](https://docs.astral.sh/uv/) 管理开发流程。安装一次之后:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

验证可编辑安装(editable install):
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### 运行测试

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> macOS 提示:测试套件里同时包含 `sample.f90` 和 `sample.F90` 两个 fixture。在不区分大小写的 HFS+ / APFS 文件系统上,这两个文件会冲突。如果需要同时测试这两种 Fortran 变体,请在 Linux 或 Docker 容器中运行。

### Git 工作流

- 日常开发工作在 `v8` 分支上进行。
- Commit 风格:`fix: <description>` / `feat: <description>` / `docs: <description>`
- 在提交 PR 之前,运行 `uv run pytest tests/ -q` 并确认测试通过。
- 每新增一个语言提取器,都要在 `tests/fixtures/` 添加对应的 fixture 文件,并在 `tests/test_languages.py` 添加测试。

### 可以贡献什么

**Worked examples(实际案例)** 是最有价值的贡献方式。对一个真实语料运行 `/graphify`,把输出保存到 `worked/{slug}/`,写一份诚实的 `review.md`,说明图谱哪些地方做对了、哪些地方做错了,然后提交 PR。

**提取相关的 bug** —— 提 issue 时请附上输入文件、对应的缓存条目(`graphify-out/cache/`),以及具体漏掉了什么或哪里出错了。

模块职责说明和如何新增语言支持,请参见 [ARCHITECTURE.md](../../ARCHITECTURE.md)。

</details>
