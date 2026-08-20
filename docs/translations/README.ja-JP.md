<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b><a href="https://github.com/Graphify-Labs/graphify">graphify</a> のフォークで、<code>graphify decouple</code> を追加</b> — god object 向けに、0-LLM でリスクスコア付けされた Extract Class 候補を提示し、（コールグラフだけでなく）実際のソースコードに対して再検証してから初めて推奨します。詳しくは下記の <a href="#decouple-リスクスコア付き-extract-class-候補">Decouple: リスクスコア付き Extract Class 候補</a> を参照してください。
</p>

<div align="center">
<details><summary><b>他の言語で読む</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>公開 v1 リリース前の graphify プラットフォームへの早期アクセスを受付中です: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

AI コーディングアシスタントで `/graphify` と入力するだけで、プロジェクト全体（コード、ドキュメント、PDF、画像、動画）を **ナレッジグラフ** にマッピングし、ファイルを grep する代わりに **クエリ** できるようになります。

- **コードマップは無料・完全ローカル。** コードは tree-sitter の AST で解析されます。決定論的で LLM 不要、何もマシンの外に出ません。（ドキュメント、PDF、画像、動画はセマンティック処理のためにアシスタントのモデル、または設定済みの API キーを利用します。）
- **すべてのエッジに根拠がある。** 各つながりには `EXTRACTED`（ソースに明示的に存在）または `INFERRED`（graphify が推論して解決）のタグが付くため、直接読み取られたものと推論されたものを区別できます。
- **ベクトルインデックスではない。** 埋め込みもベクトルストアも使わない、実際にたどれるグラフです。質問をする、2 つのものの間の経路をたどる、1 つの概念を説明する、といったことができます。

> 必要なときだけでなく、コード・ドキュメント・会議の内容をまたいでバックグラウンドで常時更新され続けるものが欲しいですか？ それはまさに私たちが **[graphify.com](https://graphify.com)** で構築しているものです。早期アクセスは **[app.graphify.com](https://app.graphify.com/login)** で今すぐ開始できます。

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="FastAPI コードベースを力学モデルによるナレッジグラフとして表示する graphify のインタラクティブな graph.html。検出されたコミュニティの凡例付き" width="900">
</p>
<p align="center">
  <em>graphify によってマッピングされた FastAPI コードベース。各ノードは 1 つの概念、色は検出されたコミュニティを表し、全体が graph.html 上でクリック可能です。</em>
</p>

**はじめかた**（30 秒）:

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

続いて、AI アシスタント内で:

```
/graphify .
```

これだけです。**3 つのファイル** が生成されます。

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**対応環境:** Claude Code、Cursor、Codex、Gemini CLI、GitHub Copilot ほか 15 種類以上 — [対応プラットフォームから選ぶ](#インストール)。

---

## 実際の動作を見る

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="graphify のパスクエリ: ターミナルで FastAPI と ModelField の間の最短経路を尋ね、その答えがナレッジグラフ上でホップごとに点灯していく様子" width="900">
</p>

グラフが構築されたら、ファイルを読む代わりにそれをクエリします。以下は、上記の FastAPI コードベースに対して graphify を実行した実際の出力です。

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

すべてのエッジには **信頼度タグ** が付きます（`EXTRACTED` = ソースに明示的に存在、`INFERRED` = 解決によって導出）。そのため、直接読み取られたものと推論されたものを区別できます。`graphify query "<question>"` は平易な言葉での質問に対してスコープを絞った部分グラフを返し、`graphify path A B` は任意の 2 つのものがどうつながっているかをたどります。

---

## Decouple: リスクスコア付き Extract Class 候補

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: MainWindow という god node がリスクスコア付きの候補クラスへ分割される様子。2 つのクラス間で状態が共有されているという警告付き" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: MainWindow に提案された 5 つのクラス。Main Window Axis and Range Controls の Node Info パネルが開き、Main Window Controller Core との状態オーバーラップが 0.608 であることを示している" width="900">
</p>
<p align="center">
  <em>実際の実行での DECOUPLE.html — 提案されたクラスをクリックすると、他のどのクラスと状態を共有しているか、具体的に何を共有しているかが正確に表示されます。</em>
</p>

同じページが分割そのものも描画します。**Preview decoupled view** を切り替えると、god クラス自身のメソッドが提案クラスに置き換わり、エッジがその場で再配線されます — 描き直した図ではなく、配線の変化そのものです:

| 分割前 — 現在の god クラス | 分割後 — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="トグル前の DECOUPLE.html: 単一の MainWindow ハブノードと、その周囲に広がる自身のメソッド群" width="440"> | <img src="../decouple-after.png" alt="トグル後の DECOUPLE.html: 同じノードが 5 つのひし形の提案クラスに縮小され、緑の破線がどのメソッドがどのクラスに抽出されたかを、赤い線が 2 つのクラスが共有したままのインスタンス状態を示している" width="440"> |
| 1 つのノードが自身のメソッド 47 個を抱え、そのすべてがこのクラス経由でしか到達できません。 | 提案されたクラス群。緑の破線 = それぞれに何が抽出されたか、赤 = 2 つのクラスが依然として共有しているインスタンス状態で、これがまさに `split` か `keep_as_is` かを決めます。リスクしきい値を超えた候補だけが描画されます — ここでは 6 個中 5 個なので、1 つのメソッドには着地するひし形がありません。 |

`graphify decouple` は god object を見つけ出し、それが単に「大きい」だけでなく、分割する価値が実際にあるかどうかを教えてくれます。

これが捕まえようとしている失敗パターンはこうです。47 個のメソッドを持つクラスがあり、コールグラフによるクラスタリングは喜んで 5 つの見た目の整ったグループに分割します。しかし、その裏では全グループが依然として同じ `self._chart_style` / `self._crosshair` というインスタンス状態を読み書きしています。この分割をそのまま出荷しても、何も疎結合にはなっていません — メソッドを新しいファイルに移しただけで、結局は同じ共有状態を渡し戻す必要があるため、個別にテストも、変更も、理解もできないままです。コールグラフだけを見るツールにはこれがまったく見えません。実際のソースまで立ち返る必要があります。

**2 つのチェック、どちらも 0-LLM・決定論的:**

1. **そもそも God Object なのか？** 次数（degree）の高いノードは、真の God Object（自分自身のメソッドが多数あり、無関係な責務にまたがっている — Extract Class が有効）である場合もあれば、過剰に参照されているハブ／データモデル（自分自身のメソッドは少なく、大半が *受信側* の参照）である場合もあります。後者の場合、本体を分割しても何も改善しません。修正すべきはインターフェースを狭めることであり、クラスを抽出することではありません。`classify_god_node` は生の次数ではなく `member_ratio` によってこの 2 つを区別します。この違いによって、`TraceSource`（84 本のエッジを持つが、自分自身のメソッドはわずか 6 個）は誤った分割提案を受けずに済み、一方で `MainWindow`（88 本のエッジ、自分自身のメソッド 47 個）には正しく提案が出されます。
2. **その分割は実際に結合度を下げるのか？** `risk_before`（god node の現在のサイズ・結合度・断片化）を `risk_after`（分割そのものが新たにもたらすリスク）と比較します。`risk_after` には、これまでクラス内部の見えないエッジだったものがクラス間の明示的な依存関係になってしまうグループ間呼び出し、複数の新クラスに依存することになる呼び出し元、そして — コールグラフには構造的に不可能なチェックである — 提案されたグループが実際にどれだけの `self`/`this` インスタンス状態（読み取り・書き込み・共有ヘルパーメソッド呼び出しをそれぞれ別重みで評価。共有された **書き込み** は共有された読み取りよりも高いスコアになります）を共有しているかが含まれます。これは god node 自身のソースファイルを tree-sitter で直接再パースするものであり、フィールドレベルのアクセスをどの言語についても記録しない graphify 自身の抽出済みグラフには依存しません。`risk_after` が `risk_before` を一定のしきい値以上下回った場合にのみ、プランは `split` を推奨します。それ以外は `marginal` または `keep_as_is` となり、推奨されない候補は目で見て疑わなければならない図形としてではなく、常に数値として報告されます。

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

`graph.json` と同じ場所に 3 つのファイルを出力します。

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

**状態共有チェックの言語対応表**（上記のコールグラフのみによる分類は graphify が抽出できるすべての言語で動作します。この表は特に、`self`/`this` の状態オーバーラップを検証するソース再パースについてのものです）:

| Language | Supported | Notes |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` is its own AST node, not a wrapped field access — handled explicitly |
| C# | ✅ | |
| Rust | ✅ | `self.x` via `impl` blocks |
| Ruby | ✅ | `@x` (the dominant idiom) + `self.foo` calls |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | per-method receiver resolution — Go has no `self`/`this` keyword, so the receiver name (`f` in `func (f *Foo) M()`) is resolved fresh for every method |
| C | ❌ | a struct-pointer parameter has no syntactic marker distinguishing it from any other parameter — no reliable signal without full type inference |

未対応言語の god node、またはソースを読み取れない god node は `state_analysis: "skipped"` としてマークされます。分類とコールグラフスコアはそのまま実行されますが、推奨結果は状態チェックが通ったと黙って仮定するのではなく、コールグラフのみに基づくことになります。

---

## できること

標準で得られるもの:

| Capability | What you get |
|---|---|
| **God nodes** | The most-connected concepts, so you see what everything flows through |
| **Communities** | The graph split into subsystems (Leiden), with LLM-free labels |
| **Cross-file links** | `calls` / `imports` / `inherits` / `mixes_in` resolved across ~40 languages via tree-sitter AST |
| **Query, path, explain** | Ask a question, trace the path between two things, or explain one concept, all against `graph.json` |
| **Rationale + doc refs** | `# NOTE:` / `# WHY:` comments and ADR/RFC citations become first-class nodes linked to the code |
| **Beyond code** | Docs, PDFs, images, and video/audio all map into the same graph |
| **Local-first** | Code is parsed locally with tree-sitter (no LLM, nothing leaves your machine); only the semantic pass over docs/media calls a backend, and only if you configure one |

---

## ベンチマーク

| Benchmark | Metric | graphify | Field |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | QA accuracy | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | QA accuracy | **76%** | tied with dense RAG |
| Graph build | LLM credits | **0** | per-token for most systems |

すべてのシステムは同一のハーネス、同一のモデル、同一の予算で実行され、第 2 の判定者に対して盲検検証された判定者によって採点されています（一致率 90.6%、Cohen's kappa 0.81）。システムごとの詳細な表、コードインテリジェンスの結果、再現手順の全文は **[BENCHMARKS.md](../../BENCHMARKS.md)** を参照してください。

---

## 前提条件

| Requirement | Minimum | Check | Install |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(recommended)* | any | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(alternative)* | any | `pipx --version` | `pip install pipx` |

**macOS でのクイックインストール（Homebrew）:**
```bash
brew install python@3.12 uv
```

**Windows でのクイックインストール:**
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

## インストール

> **公式パッケージについて:** PyPI パッケージ名は `graphifyy`（y が 2 つ）です。PyPI 上の他の `graphify*` パッケージは無関係です。CLI コマンドは引き続き `graphify` です。

**ステップ 1 — パッケージをインストール:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**ステップ 2 — AI アシスタントにスキルを登録:**

```bash
graphify install
```

これだけです。AI アシスタントを開いて `/graphify .` と入力してください。

ユーザープロファイルではなく現在のリポジトリにアシスタントスキルをインストールしたい場合は、`--project` を付けます。

```bash
graphify install --project
graphify install --project --platform codex
```

プロジェクトスコープのインストールはカレントディレクトリ配下に書き込まれます。例えば
`.claude/skills/graphify/SKILL.md` や `.agents/skills/graphify/SKILL.md`（スキルがオンデマンドで読み込む
`references/` サイドカー付き）などで、
コミット対象になり得るファイルについて `git add` のヒントを表示します。
プロジェクトスコープのインストールに対応するプラットフォーム別コマンドも同じフラグを受け付けます。
例えば `graphify claude install --project` や `graphify codex install --project` です。

> **PowerShell での注意点:** `/graphify .` ではなく `graphify .` を使ってください — PowerShell では先頭のスラッシュはパス区切り文字として扱われます。

> **`graphify: command not found` になる場合?** `uv tool install` / `pipx install` は `graphify` コマンドをそれぞれのツール用 bin ディレクトリ（`~/.local/bin`）に配置します。インストール直後にシェルがコマンドを見つけられない場合（新規の macOS + zsh 環境でよくあります）、そのディレクトリがまだ `PATH` に含まれていません。`uv tool update-shell`（または `pipx ensurepath`）を実行してから、新しいターミナルを開いてください。素の `pip` を使った場合は、`~/.local/bin`（Linux）または `~/Library/Python/3.x/bin`（Mac）を `PATH` に追加するか、`python -m graphify` を実行してください。

> **インストールの代わりに `uvx` / `uv tool run` を使う場合?** コマンド名ではなくパッケージ名を指定してください: `uvx --from graphifyy graphify install`。素の `uvx graphify …` は失敗します（`No solution found … no versions of graphify`）。これは `uv tool run` が最初の単語を *パッケージ名* として読み取るためで、実際のパッケージ名は `graphifyy` です — `graphify` コマンドはその中に含まれています。

> **Mac/Windows では可能なら `pip install` を避けてください。** スキルは実行時に `graphify-out/.graphify_python` から Python を解決します。それが `pip` でパッケージをインストールしたのとは別の環境を指している場合、`ModuleNotFoundError: No module named 'graphify'` が発生します。`uv tool install` と `pipx install` はパッケージを専用環境に隔離するため、この問題を完全に回避できます。

> **Git フックと uv tool / pipx について:** `graphify hook install` は現在のインタープリタのパスをインストール時にフックスクリプトへ直接埋め込むため、`~/.local/bin` が `PATH` に含まれない GUI の git クライアントや CI ランナーでも post-commit フックが正しく発火します。graphify を再インストールまたはアップグレードした場合は、`graphify hook install` を再実行して埋め込まれたパスを更新してください。

> **Strict モード（Claude Code）:** `graphify install --project --strict` は、アシスタントに実際にグラフを使わせるようにします。デフォルトのインストールでは、ファイルを読む前に `graphify query` を実行するよう *促す* だけですが、strict モードではセッション最初の生のソース読み取りを実際に *ブロック* してグラフへ誘導し、その後は通常の促しに戻ります（セッションごとに最大 1 回しか発動せず、動かなくなることもありません）。`GRAPHIFY_HOOK_STRICT=1`/`0` で実行時に切り替え可能です。デフォルトのインストール挙動（ソフトな促し）は変わりません。

<details>
<summary><b>対応プラットフォームから選ぶ</b>（20 種類以上のアシスタント、クリックして展開）</summary>

| Platform | Install command |
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

Codex を使う場合は、並列抽出のために `~/.codex/config.toml` の `[features]` 配下で `multi_agent = true` も必要です。CodeBuddy は Claude Code と同じ Agent ツールおよび PreToolUse フック機構を使用します。Factory Droid は並列サブエージェント実行のために `Task` ツールを使用します。OpenClaw と Aider は逐次抽出を使用します（これらのプラットフォームでの並列エージェント対応はまだ初期段階です）。Trae は並列サブエージェント実行のために Agent ツールを使用し、`PreToolUse` フックには対応して **いない** ため、AGENTS.md が常時稼働の仕組みになっています。

`--platform agents`（エイリアス `--platform skills`）は、汎用のクロスフレームワーク [Agent-Skills](https://github.com/anthropics/skills) の配置場所を対象とします。グローバルインストールには仕様上のユーザーグローバルな `~/.agents/skills/`（`npx skills` や仕様準拠のフレームワークが読み込みます）を、プロジェクト（`--project`）インストールには `./.agents/skills/` を使います。素の `graphify install` は設計上 Claude Code 専用のままです — `.agents/skills` を読むあらゆるフレームワークにスキルを発見させたい場合は、名前付きの `agents` プラットフォームを使ってください。

> Codex では `/graphify` の代わりに `$graphify` を使います。

</details>

<details>
<summary><b>オプションの拡張機能</b>（必要なものだけインストール）</summary>

| Extra | What it adds | Install |
|---|---|---|
| `pdf` | PDF extraction | `uv tool install "graphifyy[pdf]"` |
| `office` | `.docx` and `.xlsx` support | `uv tool install "graphifyy[office]"` |
| `google` | Google Sheets rendering | `uv tool install "graphifyy[google]"` |
| `video` | Video/audio transcription (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | MCP stdio server | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Neo4j push support | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | FalkorDB push support | `uv tool install "graphifyy[falkordb]"` |
| `svg` | SVG graph export | `uv tool install "graphifyy[svg]"` |
| `leiden` | Leiden community detection (Python < 3.13 only) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Ollama local inference | `uv tool install "graphifyy[ollama]"` |
| `openai` | OpenAI / OpenAI-compatible APIs | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic Claude API (`--backend claude`, uses `ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (uses IAM, no API key) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, uses `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "graphifyy[openai]"` |
| `sql` | SQL schema extraction | `uv tool install "graphifyy[sql]"` |
| `postgres` | Live PostgreSQL introspection (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | BYOND DreamMaker `.dm`/`.dme` AST extraction (may need a C compiler + `python3-dev` if no wheel matches your platform) | `uv tool install "graphifyy[dm]"` |
| `terraform` | Terraform / HCL `.tf`/`.tfvars`/`.hcl` AST extraction | `uv tool install "graphifyy[terraform]"` |
| `pascal` | Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` AST extraction (more accurate `calls`/`inherits` edges; falls back to a regex extractor when absent) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | Chinese query segmentation (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | Everything above | `uv tool install "graphifyy[all]"` |

</details>

---

## アシスタントに常にグラフを使わせる

グラフを構築した後、プロジェクトで一度だけ実行してください。

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
| Agent Skills (cross-framework) | `graphify agents install` (alias `graphify skills install`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify pi install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

これにより、コードベースに関する質問に対して、完全なレポートを読んだり生のファイルを grep したりするよりも `graphify query "<question>"` のようなスコープを絞ったクエリを優先し、ナレッジグラフを参照するようアシスタントに指示する小さな設定ファイルが書き込まれます。

- **フック対応プラットフォーム**（Claude Code、Gemini CLI）: 検索系のツール呼び出しの前（Claude Code では Read/Glob ツールでソースファイルを 1 つずつ読む前にも）にフックが自動的に発火し、アシスタントをグラフのパスへ促します。
- **命令ファイル対応プラットフォーム**（Codex、OpenCode、Cursor など）: 永続的な命令ファイル（`AGENTS.md`、`.cursor/rules/` など）が同じクエリ優先のガイダンスを提供します。

`GRAPH_REPORT.md` は広範なアーキテクチャレビュー用として引き続き利用できます。

**CodeBuddy** は Claude Code と同じ 2 つのことを行います。`CODEBUDDY.md` のセクションに、アーキテクチャに関する質問に答える前に `graphify-out/GRAPH_REPORT.md` を読むよう CodeBuddy に指示する内容を書き込み、Bash の検索コマンドやファイル読み取りの前に発火して `graphify query` を使うよう促す `PreToolUse` フック（`.codebuddy/settings.json`）をインストールします。

**Codex** は `AGENTS.md` に書き込みます。これがこのプラットフォームで常時稼働のグラフガイダンスを実際に担う仕組みです。`graphify codex install` は `.codex/hooks.json` にも `PreToolUse` フック（`graphify hook-check`）を登録しますが、このエントリは意図的に **何もしません**。Codex Desktop は `PreToolUse` での `hookSpecificOutput.additionalContext` を拒否するため、そこで促しを出すと Bash ツール呼び出しが壊れてしまうからです。フック（`graphify hook-guard`）が実際に促しを行う Claude Code とは異なり、Codex ではフックは発火しても意図的に何もせず、`AGENTS.md` が常時稼働の仕組みになっています。

**Kilo Code** は Graphify スキルを `~/.config/kilo/skills/graphify/SKILL.md` に、ネイティブの `/graphify` コマンドを `~/.config/kilo/command/graphify.md` にインストールします。`graphify kilo install` はさらに `AGENTS.md` と、ネイティブの `tool.execute.before` プラグイン（`.kilo/plugins/graphify.js` と `.kilo/kilo.json` または `.kilo/kilo.jsonc` への登録）を書き込むため、Kilo はネイティブの `.kilo` 設定を通じて同じ常時稼働のグラフリマインダーの挙動を得られます。

**Cursor** は `alwaysApply: true` を指定した `.cursor/rules/graphify.mdc` を書き込むため、Cursor はフックなしですべての会話に自動的にそれを含めます。

すべてのプラットフォームから graphify を一括で削除するには: `graphify uninstall`（`graphify-out/` も削除するには `--purge` を追加）。またはプラットフォーム別のコマンド（例: `graphify claude uninstall`）を使ってください。

---

## レポートの内容

- **God nodes** — プロジェクト内で最も多く接続されている概念。すべてがここを経由します。
- **意外なつながり** — 異なるファイルやモジュールに存在するもの同士のリンク。意外性の高さでランク付けされます。
- **「なぜ」** — インラインコメント（`# NOTE:`、`# WHY:`、`# HACK:`）、docstring、ドキュメントからの設計上の根拠が、それらが説明しているコードにリンクされた個別のノードとして抽出されます。
- **提案される質問** — このグラフだからこそ答えられる 4〜5 個の質問。
- **信頼度タグ** — 推論されたすべての関係には `EXTRACTED`、`INFERRED`、`AMBIGUOUS` のいずれかが付きます。何が見つかったもので何が推測されたものか、常に把握できます。

---

## 対応しているファイル

| Type | Extensions |
|------|-----------|
| Code (36 tree-sitter grammars) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme` requires `uv tool install graphifyy[dm]`; `.mts`/`.cts` reuse the TypeScript grammar, `.cc`/`.cxx` and CUDA `.cu`/`.cuh` and Metal `.metal` reuse the C++ grammar) |
| Salesforce Apex | `.cls .trigger` (regex-based; classes, interfaces, enums, methods, triggers, SOQL/DML edges) |
| Terraform / HCL | `.tf .tfvars .hcl` (requires `uv tool install graphifyy[terraform]`) |
| MCP configs | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — extracts server nodes, package refs, env var requirements |
| Package manifests | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — one canonical package node per package (by name) plus `depends_on` edges, so a package referenced from many manifests is a single hub |
| Docs | `.md .mdx .qmd .html .txt .rst .yaml .yml` (markdown `[text](./other.md)` links and `[[wikilinks]]` become `references` edges between docs) |
| Office | `.docx .xlsx` (requires `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (opt-in; requires `gws` auth and `--google-workspace`; Sheets need `uv tool install graphifyy[google]`) |
| PDFs | `.pdf` |
| Images | `.png .jpg .webp .gif` |
| Video / Audio | `.mp4 .mov .mp3 .wav` and more (requires `uv tool install graphifyy[video]`) |
| YouTube / URLs | any video URL (requires `uv tool install graphifyy[video]`) |

コードは **API 呼び出しなしでローカルに** 抽出されます（tree-sitter による AST）。それ以外はすべて AI アシスタントのモデル API を経由します。

Google Drive デスクトップ版の `.gdoc`、`.gsheet`、`.gslides` ファイルはショートカットへのポインタであり、ドキュメントの内容そのものではありません。ヘッドレス抽出でネイティブの
Google ドキュメント・スプレッドシート・スライドを含めるには、
[`gws` CLI](https://github.com/googleworkspace/cli) をインストールして認証した上で、次を実行してください。

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

`GRAPHIFY_GOOGLE_WORKSPACE=1` を設定することもできます。Graphify はショートカットを
`graphify-out/converted/` へ Markdown サイドカーとしてエクスポートし、それらのファイルを抽出します。

---

## よく使うコマンド

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
graphify god-nodes                                # list the most-connected nodes (architectural hubs)

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

上記の[Decouple: リスクスコア付き Extract Class 候補](#decouple-リスクスコア付き-extract-class-候補)、または下記の[コマンドリファレンス全体](#コマンドリファレンス全体)を参照してください。

---

## ファイルの除外

プロジェクトルートに `.graphifyignore` を作成してください — 構文は `.gitignore` と同じで、`!` による否定も使えます。

**`.gitignore` は自動的に尊重されます。** graphify は各ディレクトリの `.gitignore` を読み込みます。`.graphifyignore` も存在する場合、両者は **マージ** されます — `.graphifyignore` のパターンが最後に評価されるため、競合時（`!` による否定を含む）はこちらが優先されます。`.graphifyignore` を追加しても除外対象が増えるだけで、`.gitignore` がすでに除外しているファイルを再度含めることはありません。サブディレクトリのスコープの扱いは git と同様です — ignore ファイルは自分自身のサブツリーにのみ影響します。

git 管理外の生成コードやトランスパイル済みコードをグラフに含めたい場合は、`graphify extract` に `--no-gitignore` を渡してください。これにより `.gitignore` と `.git/info/exclude` が無効になりますが、`.graphifyignore` は引き続き適用されます。

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

## チームでのセットアップ

`graphify-out/` は git にコミットすることを想定しています。そうすることでチーム全員が最初からマップを持てます。

**推奨する `.gitignore` への追加:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` は現在ポータブルです — キーは相対パスとして保存され、読み込み時に再アンカーされるため、コミットしても安全であり、初回チェックアウト時のフルリビルドを回避できます。

**ワークフロー:**
1. 1 人が `/graphify .` を実行し、`graphify-out/` をコミットします。
2. 他のメンバーが pull すると、そのアシスタントはすぐにグラフを読み込めます。
3. `graphify hook install` を実行して、各コミット後に自動リビルドされるようにします（AST のみ、API コストなし）。これにより git のマージドライバーも設定され、`graph.json` にコンフリクトマーカーが残ることがなくなります — 2 人の開発者が並行してコミットしても、それぞれのグラフは自動的にユニオンマージされます。
4. ドキュメントや論文が変更されたら、`/graphify --update` を実行してそれらのノードを更新してください。

---

## グラフを直接使う

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

MCP サーバーは、アシスタントに構造化されたアクセス手段を提供します: `query_graph`、`get_node`、`get_neighbors`、`shortest_path`、`list_prs`、`get_pr_impact`、`triage_prs`。

### 共有 HTTP サーバー

`--transport stdio`（デフォルト）は開発者ごとにローカルサーバーを 1 つ起動します。`--transport http` は同じツール群を MCP Streamable HTTP トランスポート経由で提供するため、単一の共有プロセスがチーム全体のグラフを配信できます — クライアントは、ローカルで graphify を実行する代わりに、IDE の MCP 設定で `http://<host>:8080/mcp` を指定します。

| Flag | Default | Purpose |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Transport to serve on |
| `--host` | `127.0.0.1` | HTTP bind host (use `0.0.0.0` to expose beyond localhost) |
| `--port` | `8080` | HTTP bind port |
| `--api-key` | env `GRAPHIFY_API_KEY` | Require `Authorization: Bearer <key>` (or `X-API-Key`) |
| `--path` | `/mcp` | HTTP mount path |
| `--json-response` | off | Return plain JSON instead of SSE streams |
| `--stateless` | off | No per-session state (for load-balanced / CI deployments) |
| `--session-timeout` | `3600` | Reap idle stateful sessions after N seconds (`0` disables) |

デフォルトの `127.0.0.1` バインドはループバック専用です。共有ホストに公開する場合は `--host 0.0.0.0` と `--api-key` を **両方** 設定してください。コンテナで実行する場合:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **WSL / Linux での注意点:** Ubuntu は `python` ではなく `python3` を同梱しています。競合を避けるため venv を使ってください。
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## 環境変数

これらは **ヘッドレス／CI での抽出**（`graphify extract`）にのみ必要です。IDE 内で `/graphify` スキルを実行する場合、モデル API は IDE セッションから提供されるため、追加のキーは不要です。

| Variable | Used for | When required |
|---|---|---|
| `ANTHROPIC_API_KEY` | Claude (Anthropic) backend | `--backend claude` |
| `ANTHROPIC_BASE_URL` | Anthropic-compatible endpoint URL (LiteLLM proxy, gateways, ...) | `--backend claude` (default: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Model name for the Claude backend — for custom endpoints, use the model name/alias your server exposes | `--backend claude` (default: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` or `GOOGLE_API_KEY` | Google Gemini backend | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI or OpenAI-compatible APIs | `--backend openai` (local servers accept any non-empty value) |
| `OPENAI_BASE_URL` | OpenAI-compatible server URL (llama.cpp, vLLM, LM Studio, ...) | `--backend openai` (default: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | Model name for the OpenAI backend — for self-hosted servers, use the model name/alias your server exposes (check its `/v1/models` endpoint), e.g. `LFM2.5-8B-A1B-UD-Q4_K_XL` for llama.cpp | `--backend openai` (default: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | DeepSeek backend | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Kimi Code backend | `--backend kimi` |
| `OLLAMA_BASE_URL` | Ollama local inference URL | `--backend ollama` (default: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Ollama model name | `--backend ollama` (default: auto-detect) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Override Ollama KV-cache window size | optional — auto-sized by default |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Minutes to keep Ollama model loaded | optional — set `0` to unload after each chunk |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI Service backend | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | Azure resource endpoint URL | `--backend azure` (required alongside API key) |
| `AZURE_OPENAI_API_VERSION` | Azure API version override | optional — default `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` or `GRAPHIFY_AZURE_MODEL` | Azure deployment name | optional — default `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — standard credential chain | `--backend bedrock` (no API key, uses IAM) |
| `GRAPHIFY_MAX_WORKERS` | AST parallelism thread count | optional — also `--max-workers` flag |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Raise output cap for dense corpora | optional — e.g. `32768` for large files |
| `GRAPHIFY_API_TIMEOUT` | Per-call timeout in seconds for HTTP, claude-cli, Anthropic SDK, and Bedrock backends (default: 600) | optional — also `--api-timeout` flag |
| `GRAPHIFY_MAX_RETRIES` | How many times to retry a rate-limited (429) request before giving up (default: 6; honors `Retry-After`) | optional — raise for strict per-org limits (e.g. kimi); `0` disables |
| `GRAPHIFY_FORCE` | Force graph rebuild even with fewer nodes | optional — also `--force` flag |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Auto-enable Google Workspace export | optional — set to `1` |
| `GRAPHIFY_TRIAGE_BACKEND` | Backend for `graphify prs --triage` | optional — auto-detected from available keys |
| `GRAPHIFY_TRIAGE_MODEL` | Model override for triage | optional — e.g. `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | Set to `1` to turn on the local query log at `~/.cache/graphify-queries.log` (records each query/path/explain question + corpus path). Off by default — nothing is written unless you opt in (#1797) | optional |
| `GRAPHIFY_QUERY_LOG` | Enable the query log and write it to this path instead of the default | optional — off unless this or `_ENABLE` is set |
| `GRAPHIFY_QUERY_LOG_DISABLE` | Set to `1` to force the query log off (wins over the enable vars) | optional |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | When the log is enabled, also record full subgraph responses (off by default) | optional |
| `GRAPHIFY_MAX_GRAPH_BYTES` | Override the 512 MiB graph.json size cap — e.g. `700MB`, `2GB`, or plain bytes | optional — useful for very large corpora |
| `GRAPHIFY_MAX_CONTEXTS` | Maximum number of non-default project graphs retained by one multi-project MCP server | optional — default: `8`; invalid values use `8`, and values below `1` use `1` |
| `GRAPHIFY_LLM_TEMPERATURE` | Override LLM temperature for semantic extraction — e.g. `0.7`, or `none` to omit | optional — auto-omitted for o1/o3/o4/gpt-5 reasoning models |

---

## プライバシー

- **コードファイル** — tree-sitter によりローカルで処理されます。何もマシンの外には出ません。コードのみのコーパスには API キーは不要です — `graphify extract` は完全にオフラインで動作します。混在リポジトリでは、`--code-only` を追加すると、それ以外の場合 LLM を必要とするドキュメント／PDF／画像をスキップして、コードのみをインデックスできます。
- **動画・音声** — faster-whisper によりローカルで文字起こしされます。何もマシンの外には出ません。
- **ドキュメント、PDF、画像** — セマンティック抽出のために AI アシスタントへ送信されます（`/graphify` スキル経由。IDE セッションが実行しているモデルを使用）。ヘッドレスの `graphify extract` には、`GEMINI_API_KEY` / `GOOGLE_API_KEY`（Gemini）、`MOONSHOT_API_KEY`（Kimi）、`ANTHROPIC_API_KEY`（Claude）、`OPENAI_API_KEY`（OpenAI）、`DEEPSEEK_API_KEY`（DeepSeek）、稼働中の Ollama インスタンス（`OLLAMA_BASE_URL`）、標準のプロバイダーチェーン経由の AWS 認証情報（Bedrock — API キー不要、IAM を使用）、または `claude` CLI バイナリ（Claude Code — API キー不要、Claude サブスクリプションを使用）のいずれかが必要です。`--dedup-llm` フラグも同じキーを使用します。
- **データレジデンシー** — `graphify extract` は、どの API キーが設定されているかによって使用するプロバイダーを自動検出します（優先順位: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama）。データレジデンシー要件のあるコードには `--backend ollama`（完全ローカル）を使うか、明示的に `--backend` フラグを指定してください。Kimi（`MOONSHOT_API_KEY`）は中国国内の Moonshot AI サーバーへルーティングされます。
- **テレメトリなし**。使用状況の追跡もアナリティクスもありません。
- **クエリログ** — `graphify query`、`graphify path`、`graphify explain`、および MCP の `query_graph` 呼び出しは、それぞれ JSON Lines 形式で `~/.cache/graphify-queries.log` に記録されます（タイムスタンプ、質問内容、コーパス、返されたノード数、所要時間）。完全な部分グラフのレスポンスはデフォルトでは **保存されません**。オプトアウトするには `GRAPHIFY_QUERY_LOG_DISABLE=1` を設定するか、コードパスを無効化せずに出力を抑制するには `GRAPHIFY_QUERY_LOG=/dev/null` を設定してください。

---

## 制限事項と適用範囲

graphify が意図的に**行わない**こと、そしてカバー範囲がどこで途切れるかを示します。

- **セマンティック／ベクトル検索エンジンではありません。** グラフは構造的なものです — ノードと型付きエッジはソースから解決されたものであり、埋め込み(embeddings)ではありません。`graphify query`/`path`/`explain` はその構造をたどるだけなので、エッジとして表現されていないつながりは、たとえ「意味的に」関連していても見つけられません。類似度・最近傍探索によるフォールバックはありません。
- **ドキュメント、PDF、画像、およびヘッドレスでの動画/URL 抽出はローカル完結ではありません。** 完全にオフラインで動作するのは、コード(tree-sitter AST)と音声/動画の文字起こし(faster-whisper)だけです。ドキュメント/PDF/画像の抽出は常に LLM を呼び出します — `/graphify` スキル経由で AI アシスタントのモデルを使うか、ヘッドレスの `graphify extract` では設定済みのバックエンド API キーを使います。各経路でどのフラグ・キーが必要かは、上記の[プライバシー](#プライバシー)を参照してください。
- **decouple の状態共有チェックは、すべての言語をカバーしているわけではありません。** C 言語には完全な型推論なしでは信頼できる `self`/`this` のシグナルがないため、対象外です(上記の[言語対応表](#decouple-リスクスコア付き-extract-class-候補)を参照)。未対応言語の god node、またはソースを読み取れない god node は、検証済みの状態チェックではなく、コールグラフのみに基づくスコアリング(`state_analysis: "skipped"`)にフォールバックします。
- **3D のデータフローの深さ(floor)は名前によるヒューリスティックであり、データフロー/汚染(taint)解析ではありません。** `data_floor` の I/O 境界検出(パーサー、ローダー、リーダー、ライター、DB/HTTP クライアント)は命名規則(`boundary_reason`)に基づいてマッチングされます。慣例的でない名前の境界ノードは見逃される可能性があり、グラフの残りの部分がどれだけ深いかを過小評価することになります。
- **信頼度タグは graphify 自身の解決に対する確信度であり、絶対的な事実ではありません。** `INFERRED` と `AMBIGUOUS` のエッジはベストエフォートで解決されたものであり、依然として誤っている可能性があります。特に、静的な AST 解析では完全に解決できない、動的性の高いイディオム(リフレクション、実行時ディスパッチ、メタプログラミング)ではその傾向が強くなります。
- **HTML 可視化とグラフサイズには、どちらにも上限があります。** `graph.html` / `DECOUPLE.html` はデフォルトでノード数が 5,000 を超えると生成をスキップします(`MAX_NODES_FOR_VIZ`。`GRAPHIFY_VIZ_NODE_LIMIT` で引き上げ可能)。`graph.json` 自体は 512 MiB が上限です(`GRAPHIFY_MAX_GRAPH_BYTES` で上書き可能)。どちらかの上限を超えるコーパスには、`--no-viz` と `query`/`path`/`explain` を組み合わせて使ってください。
- **プロジェクト横断の認識はオプトインであり、自動ではありません。** `graphify query` が見るのは、指定した 1 つのグラフだけです。複数リポジトリにまたがる質問をするには、まず各プロジェクトを共有グラフへ明示的に登録する必要があります(`graphify global add`。MCP サーバーごとに `GRAPHIFY_MAX_CONTEXTS` 個までのデフォルト以外のコンテキストに制限されます)— graphify が自分からマシン上の他のリポジトリをスキャンすることはありません。
- **並列マルチエージェント抽出はプラットフォームに依存します。** サブエージェントを起動するアシスタント側のサポートが必要です(Codex では `~/.codex/config.toml` の `multi_agent = true`、Claude Code/CodeBuddy/Factory Droid/Trae では Agent/Task ツール)。OpenClaw と Aider は現状、逐次抽出のみに対応しています。
- **共有の MCP HTTP サーバーは、デフォルトでループバックのみにバインドされます。** 別のマシンから到達するには、`--host 0.0.0.0` **と** `--api-key` の両方を明示的に指定する必要があります。graphify はその 1 つのベアラートークン以外の TLS や認証は管理しません。
- **PowerShell は先頭の `/` をパス区切りとして解釈します。** そのため `/graphify .` は Windows PowerShell では失敗します。これは graphify のバグではなく、代わりに `graphify .` を使ってください。

---

## トラブルシューティング

**インストール後に `graphify: command not found` になる**
CLI 自体はインストールされていますが、その bin ディレクトリがシェルの `PATH` に含まれていません。インストール方法に応じた対処法を選んでください。
- **uv**（`uv tool install graphifyy`）: コマンドは uv のツール用 bin ディレクトリ（`~/.local/bin`）に配置されます。新規の macOS/zsh 環境ではこれが `PATH` に含まれていないことがよくあります。`uv tool update-shell` を実行してから、新しいターミナルを開いてください。（ディレクトリは `uv tool dir --bin` で確認できます。）
- **pipx**（`pipx install graphifyy`）: `pipx ensurepath` を実行してから、新しいターミナルを開いてください。
- **pip**（`pip install graphifyy`）: pip はスクリプトをユーザー用 bin ディレクトリにインストールしますが、これが `PATH` に含まれていないことがあります — `~/.zshrc`/`~/.bashrc` の `PATH` に `~/Library/Python/3.x/bin`（macOS）や `~/.local/bin`（Linux）を追加するか、単純に `python -m graphify` を実行してください。

**`uvx graphify …` や `uv tool run graphify …` が `graphify` を解決できない**
PyPI パッケージ名は `graphifyy` であり、`graphify` はそのパッケージが提供するコマンドにすぎません。`uv tool run` は最初の単語を *パッケージ名* として扱うため、`graphify` という名前のパッケージを探しにいき、`No solution found … no versions of graphify` というエラーになります。パッケージ名を明示的に指定してください: `uvx --from graphifyy graphify install`（`uv tool run --from graphifyy graphify install` と同じ）。または、一度 `uv tool install graphifyy` を実行してから直接 `graphify` を呼び出してください。

**`uv run --with graphifyy python -m graphify` が静かに古いインストールを実行する**
`uv run` は *システム* Python を使用するため、古い `graphifyy` もそこに存在する場合（例えば過去に `pip install graphifyy` していた場合）、Python は `sys.path` 上でそちらを先に見つけてしまい、`--with graphifyy` はそれを上書きできません。エラーなしで実行されますが、動作は *古い* バージョンのものになります — 例えば `OPENAI_BASE_URL` のような環境変数による上書きが黙って無視され、リクエストがデフォルトのエンドポイントに送られ、キーが不正であるかのように見える 401 エラーで失敗します。その特徴は `warning: skill is from graphify <newer>, package is <older>` という行です — これは古いスキルというだけでなく、別のインストールが読み込まれたことを意味します。実際にどのコピーが読み込まれたかを確認してください。
```bash
python -c "import graphify; print(graphify.__file__)"
```
その上で、インストール済みのコマンドを直接実行する（uv 管理下のコピーを使います）か、古いシステムコピーを削除してください。
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` は動くが `graphify` コマンドは動かない**
シェルの `PATH` に、コマンドがインストールされた bin ディレクトリが含まれていません。素の `pip` よりも `uv tool install` / `pipx install` を優先し、`uv tool update-shell` / `pipx ensurepath` を実行してから新しいターミナルを開いてください（上記のインストールに関する注記を参照）。

**PowerShell で `/graphify .` が "path not recognized" になる**
PowerShell は先頭の `/` をパス区切り文字として扱います。Windows では `graphify .`（スラッシュなし）を使ってください。

**`--update` や再構築の後にグラフのノード数が減っている**
リファクタリングでファイルが削除された場合、古いノードが残り続けます。リビルドの結果ノード数が減る場合でも上書きするには `--force` を渡す（または `GRAPHIFY_FORCE=1` を設定する）してください。

**`extract` が "extraction was incomplete ... refusing to overwrite" で終了する**
抽出パスがクラッシュしたり、走査がコーパスを完全に読み切れなかったりした場合、その実行結果は完全な実行より小さくなるため、`graphify extract` は既存のより大きなグラフを部分的な結果で上書きすることを拒否します（`graph.json` を保護するためです）。根本原因を修正して再実行するか、`--allow-partial` を渡してとにかく上書きしてください。

**同じエンティティに対して重複ノードがある（ゴースト重複）**
ゴースト重複（同じシンボルが 2 回現れる状態 — 1 回はソース位置付きの AST 抽出から、もう 1 回はソース位置なしのセマンティック抽出から）は、現在ビルド時に自動的にマージされます。v0.8.33 より前に構築されたグラフでこれが見られる場合は、フル再抽出を実行してクリーンアップしてください。
```bash
graphify extract . --force
```

**Ollama が VRAM 不足になる／コンテキストウィンドウを超過する**
KV キャッシュのウィンドウは自動調整されますが、GPU に対して大きすぎる場合があります。縮小してください。
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**`LLM returned invalid JSON` / `Unterminated string` の警告**
モデルの JSON レスポンスが出力トークン上限に達し、文字列の途中で切り詰められました。graphify は自動的に回復します（チャンクを分割して両方を再抽出します。また、大きすぎる単一のドキュメントは、ファイル全体が漏れなくカバーされるよう見出しや段落の境界で先に分割されます）。そのためこれらの警告はノイズにはなりますがデータの欠落にはなりません。この振れを減らすには、出力上限を上げるか、各チャンクの出力を小さくしてください。
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
OpenRouter のようなクラウドゲートウェイを使う場合は、Ollama シムよりも `--backend openai`（`OPENAI_BASE_URL` を設定）を使う方がきれいな OpenAI 互換パスになります。モデル自体に最大出力の上限がある場合は、`--token-budget` を下げるのが確実な手段です。

**グラフの HTML が大きすぎてブラウザで開けない（5000 ノード超）**
HTML 生成をスキップして、JSON を直接使ってください。
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**2 人の開発者が同時にコミットした後、`graph.json` にコンフリクトマーカーが残る**
`graphify hook install` を実行してください — コンフリクトが決して起きないよう `graph.json` を自動的にユニオンマージする git のマージドライバーが設定されます。

**ドキュメントや PDF の抽出結果が空のノード／エッジになる**
ドキュメント、PDF、画像には LLM 呼び出しが必要です — コードのみのコーパスにはキーは不要です。API キーが設定されており、バックエンドが正しいことを確認してください。
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**IDE 内でスキルのバージョン不一致の警告が出る**
インストール済みの graphify のバージョンとスキルファイルのバージョンが異なります。更新してください。
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**`graphify extract` のたびに Claude Code のプロンプトキャッシュが無効化される**
Graphify は出力ファイル（`graph.json`、`graphify-out/`）をワークスペースに書き込みます。これらのパスが無視されていない場合、書き込みのたびに Claude Code のプロンプトキャッシュが無効化され、次のターンでキャッシュ書き込みレートでの全量再アップロードが強制されます。`.claudeignore` に追加してください。
```text
# .claudeignore
graph.json
graphify-out/
```

---

## コマンドリファレンス全体

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

graphify god-nodes                 # list the most-connected nodes (architectural hubs)
graphify god-nodes --top 20 --json # more results, machine-readable

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

graphify tree                                       # graphify-out/GRAPH_TREE.html — D3 collapsible-tree view of graph.json
graphify tree --root ./src --max-children 200 --output docs/tree.html

graphify diagnose multigraph                        # report same-endpoint edge collapse risk in graph.json
graphify diagnose multigraph --json --max-examples 10

graphify benchmark                                  # measure token reduction vs a naive full-corpus approach
graphify benchmark graphify-out/graph.json

# git merge driver for graph.json — set up by `graphify hook install`, not run by hand:
graphify merge-driver <base> <current> <other>

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

> **コミュニティ名について:** エージェント内（Claude Code、Gemini CLI）では、エージェント自身がコミュニティに名前を付けます。素の CLI を実行する場合、`cluster-only` が設定済みのバックエンド（組み込み、またはカスタムの OpenAI 互換プロバイダー）で自動的に名前を付けます — `--no-label` を渡すと `Community N` のままにでき、`graphify label` を実行するとオンデマンドで名前を（再）生成できます。

---

## さらに詳しく

- [仕組み](../how-it-works.md) — 抽出パイプライン、コミュニティ検出、信頼度スコアリング、ベンチマーク
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — モジュール構成、言語の追加方法
- [オプションの統合](../docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — graphify の背後にあるアイデアとアーキテクチャ全体を解説した書籍

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) は graphify の上に構築された常時稼働レイヤーです — 同じグラフのアプローチを、会議・ファイル・ドキュメント・コードを含むあなたの作業コンテキスト全体に適用し、バックグラウンドで継続的に更新し続けます。

何百もの会話やドキュメントにまたがって仕事をしていて、それらを完全には再構築できない個人やチームのために作られています。

**[graphify.com でウェイトリストに参加](https://graphify.com)。** 無料トライアルは近日公開予定です。

---

<details>
<summary>コントリビューション</summary>

### 開発環境のセットアップ

このプロジェクトは開発ワークフローに [uv](https://docs.astral.sh/uv/) を使用しています。一度インストールした後、次を実行してください。

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

editable インストールを確認する:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### テストの実行

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> macOS での注意点: テストスイートには `sample.f90` と `sample.F90` の両方のフィクスチャが含まれています。これらは大文字小文字を区別しない HFS+ / APFS ファイルシステムでは衝突します。両方の Fortran バリアントを同時にテストする必要がある場合は、Linux または Docker コンテナ上で実行してください。

### Git ワークフロー

- 開発は `v8` ブランチ上で行われます。
- コミットスタイル: `fix: <description>` / `feat: <description>` / `docs: <description>`
- PR を開く前に `uv run pytest tests/ -q` を実行し、パスすることを確認してください。
- 新しい言語エクストラクタを追加する場合は、`tests/fixtures/` にフィクスチャファイルを、`tests/test_languages.py` にテストを追加してください。

### コントリビューションの内容

**実例（Worked examples）** が最も有用なコントリビューションです。実際のコーパスに対して `/graphify` を実行し、出力を `worked/{slug}/` に保存し、グラフが正しく捉えたことと間違えたことの両方を率直に書いた `review.md` を添えて PR を開いてください。

**抽出のバグ** — 入力ファイル、キャッシュエントリ（`graphify-out/cache/`）、そして何が抜け落ちていたか・間違っていたかを添えて Issue を開いてください。

モジュールの責務と言語の追加方法については [ARCHITECTURE.md](../../ARCHITECTURE.md) を参照してください。

</details>
