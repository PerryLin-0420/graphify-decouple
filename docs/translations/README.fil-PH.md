<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>Isang fork ng <a href="https://github.com/Graphify-Labs/graphify">graphify</a> na nagdaragdag ng <code>graphify decouple</code></b> — 0-LLM, risk-scored na mga kandidato para sa Extract Class sa mga god object, muling bineberipika laban sa aktwal na source (hindi lang sa call graph) bago ito magrekomenda ng kahit ano. Tingnan ang <a href="#decouple-mga-kandidatong-extract-class-na-may-risk-score">Decouple: mga kandidatong Extract-Class na may risk score</a> sa ibaba.
</p>

<div align="center">
<details><summary><b>Basahin ito sa ibang wika</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>Bukas na ang early access sa graphify platform bago ang pampublikong v1 launch: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

I-type ang `/graphify` sa iyong AI coding assistant at imamapa nito ang buong proyekto mo (code, dokumento, PDF, larawan, video) tungo sa isang **knowledge graph** na maaari mong **i-query sa halip na mag-grep** sa mga file.

- **Libre ang code maps, at ganap na lokal.** Pinapa-parse ang code gamit ang tree-sitter AST: deterministiko, walang LLM, walang lumalabas sa makina mo. (Ang mga dokumento, PDF, larawan at video ay gumagamit ng modelo ng iyong assistant, o ng naka-configure na API key, para sa isang semantic pass.)
- **Ipinapaliwanag ang bawat edge.** Ang bawat koneksyon ay nakatatak na `EXTRACTED` (tahasan sa source) o `INFERRED` (nilutas ng graphify), kaya alam mo kung ano ang direktang nabasa at ano ang hinuha.
- **Hindi ito vector index.** Walang embeddings, walang vector store: isang tunay na graph na tinatahak mo. Magtanong, tunton ang path sa pagitan ng dalawang bagay, o ipaliwanag ang isang konsepto.

> Gusto mo ba itong laging bukas, nag-a-update sa background sa kabuuan ng iyong code, dokumento at meeting sa halip na on demand lamang? Iyan ang ginagawa namin sa **[graphify.com](https://graphify.com)**, at bukas na ngayon ang early access sa **[app.graphify.com](https://app.graphify.com/login)**.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="ang interactive na graph.html ng graphify na nagpapakita ng FastAPI codebase bilang force-directed knowledge graph na may legend ng mga natuklasang community" width="900">
</p>
<p align="center">
  <em>Ang FastAPI codebase na minapa ng graphify. Bawat node ay isang konsepto, ang mga kulay ay natuklasang mga community, at ang lahat ay maki-click sa graph.html.</em>
</p>

**Magsimula** (30 segundo):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

Pagkatapos, sa iyong AI assistant:

```
/graphify .
```

Ayun na. Makakakuha ka ng **tatlong file**:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**Gumagana sa** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, at 15+ pa — [piliin ang iyong platform](#pag-install).

---

## Tingnan ito sa aksyon

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="path query ng graphify: humihingi ang isang terminal ng pinakamaikling path sa pagitan ng FastAPI at ModelField, at nag-iilaw ang sagot hop-by-hop sa buong knowledge graph" width="900">
</p>

Kapag naitayo na ang graph, ini-query mo ito sa halip na magbasa ng mga file. Tunay na output, graphify na pinatakbo sa FastAPI codebase na ipinakita sa itaas:

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

Bawat edge ay may dalang **confidence tag** (`EXTRACTED` = tahasan sa source, `INFERRED` = nakuha sa pamamagitan ng resolution), kaya alam mo kung ano ang direktang nabasa at ano ang hinuha. Ang `graphify query "<question>"` ay nagbabalik ng scoped na subgraph para sa isang tanong sa payak na wika, at ang `graphify path A B` ay tinutunton kung paano konektado ang alinmang dalawang bagay.

---

## Decouple: mga kandidatong Extract-Class na may risk score

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: ang god node na MainWindow na nahahati sa mga kandidatong klase na may risk score, may babala tungkol sa shared state sa pagitan ng dalawa sa kanila" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: ang 5 iminungkahing klase ng MainWindow, bukas ang Node Info panel sa Main Window Axis and Range Controls na nagpapakita ng 0.608 na state overlap sa Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>DECOUPLE.html sa isang totoong run — ang pag-click sa isang iminungkahing klase ay nagpapakita kung aling ibang klase ang kaniyang kahati sa state, at kung ano mismo ang pinagsasaluhan.</em>
</p>

Ang parehong pahina ay nagre-render din ng mismong split. Ang pag-toggle ng **Preview decoupled view** ay pinapalitan ang sariling mga method ng god class ng mga iminungkahing klase at niruruta muli ang mga edge sa mismong kinalalagyan — ang pagbabago sa wiring, hindi isang muling iginuhit na diagram:

| Bago — ang god class ngayon | Pagkatapos — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html bago ang toggle: iisang MainWindow hub node na may sariling mga method na nakabuka sa paligid nito" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html pagkatapos ng toggle: ang parehong node na naging 5 diamond na hugis ng iminungkahing klase, berdeng putol-putol na edge na nagpapakita kung aling mga method ang na-extract sa bawat isa, pulang edge na nagpapakita ng pinagsasaluhang instance state sa pagitan ng dalawa sa kanila" width="440"> |
| Isang node na may hawak na 47 sariling method, at bawat isa sa kanila ay maaabot lamang sa pamamagitan ng klase. | Ang mga iminungkahing klase. Berdeng putol-putol = kung ano ang na-extract sa bawat isa; pula = ang instance state na pinagsasaluhan pa rin ng dalawa sa kanila, na siya mismong nagpapasya sa pagitan ng `split` at `keep_as_is`. Ang mga kandidatong nakapasa lang sa risk threshold ang iginuguhit — dito 5 sa 6, kaya may isang method na walang diamond na madadapuan. |

Hinahanap ng `graphify decouple` ang mga god object at sinasabi nito sa iyo kung talagang sulit ba ang paghahati sa kanila — hindi lamang na malalaki sila.

Ang failure mode na hinuhuli nito: isang klase na may 47 method na masaya namang hinahati ng call-graph clustering sa 5 grupong mukhang maayos, ngunit lahat sila ay nagbabasa at nagsusulat pa rin sa eksaktong parehong `self._chart_style` / `self._crosshair` na instance state sa ilalim. Ipadala mo ang split na iyon at wala kang na-decouple — inilipat mo lang ang mga method sa mga bagong file na hindi pa rin matetest, mababago, o maiintindihan nang nakapag-iisa, dahil kailangan pa rin nilang lahat na maipasa pabalik ang parehong shared state. Isang tool na tumitingin lang sa call graph ay talagang hindi ito makikita; kailangan nitong bumalik sa aktwal na source.

**Dalawang pagsusuri, parehong 0-LLM, parehong deterministiko:**

1. **God Object nga ba talaga ito?** Ang isang node na may mataas na degree ay maaaring tunay na God Object (maraming SARILING method, kalat sa magkakawalang-ugnayang responsibilidad — angkop ang Extract Class) o isang sobrang na-refer na hub/data model (kaunting sariling method, karamihan ay *papasok* na reference — walang naitutulong ang paghahati sa katawan nito; ang solusyon ay pakitirin ang interface, hindi mag-extract ng klase). Pinaghihiwalay ng `classify_god_node` ang dalawang ito sa pamamagitan ng `member_ratio`, hindi ng hilaw na degree — ang pagkakaibang pumipigil sa `TraceSource` (84 edge, ngunit 6 lang ang sariling method) na makatanggap ng palpak na mungkahing split, na tama namang natatanggap ng `MainWindow` (88 edge, 47 sariling method).
2. **Talaga bang mababawasan ng split ang coupling?** Ang `risk_before` (ang kasalukuyang laki/coupling/fragmentation ng god node) ay ikinukumpara sa `risk_after` — ang BAGONG panganib na ipapasok mismo ng split: mga cross-group na tawag na dating hindi nakikitang intra-class na edge at nagiging tahasang inter-class na dependency, mga caller na kailangang umasa na ngayon sa mahigit isang bagong klase, at — ang pagsusuring hindi kayang gawin ng isang call graph sa estruktura nito — kung gaano karaming `self`/`this` na instance state (mga read, write, at pinagsasaluhang tawag sa helper method, hiwalay na tinitimbang: mas mataas ang iskor ng pinagsasaluhang **write** kaysa sa pinagsasaluhang read) ang tunay na pinagsasaluhan ng mga iminungkahing grupo. Muli nitong pina-parse nang direkta ang sariling source file ng god node gamit ang tree-sitter; hindi ito umaasa sa sariling extracted graph ng graphify, na hindi kailanman nagtatala ng field-level na access para sa anumang wika. Tanging kapag lumagpas ang `risk_after` sa isang threshold na mas mababa kaysa `risk_before` inirerekomenda ng plano ang `split` — kung hindi, ito ay `marginal` o `keep_as_is`, at ang hindi hinihikayat na kandidato ay iniuulat bilang numero, hindi kailanman iginuguhit bilang hugis na kailangan mong duda-dudahan sa mata.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

Naglalabas ng tatlong file sa tabi ng `graph.json`:

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

**Saklaw ng wika para sa state-sharing check** (ang call-graph-only na klasipikasyon sa itaas ay gumagana para sa bawat wikang ine-extract ng graphify; ang talaang ito ay partikular para sa source re-parse na nagbeberipika sa overlap ng `self`/`this` state):

| Wika | Suportado | Mga tala |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | ang `this.foo()` ay sarili nitong AST node, hindi isang nakabalot na field access — hayagang hinahawakan |
| C# | ✅ | |
| Rust | ✅ | `self.x` sa pamamagitan ng mga `impl` block |
| Ruby | ✅ | `@x` (ang nangingibabaw na idyoma) + mga tawag na `self.foo` |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | per-method na resolusyon ng receiver — walang `self`/`this` keyword ang Go, kaya ang pangalan ng receiver (`f` sa `func (f *Foo) M()`) ay muling nilulutas para sa bawat method |
| C | ❌ | ang isang struct-pointer na parameter ay walang syntactic na marka na nagpapabukod dito sa alinmang ibang parameter — walang maaasahang senyas kung wala ang ganap na type inference |

Ang isang god node sa wikang hindi suportado, o isang node na hindi mabasa ang source, ay minamarkahan ng `state_analysis: "skipped"` — tumatakbo pa rin ang klasipikasyon at ang call-graph score, ngunit ang rekomendasyon ay nakasalalay sa call graph lamang sa halip na tahimik na ipagpalagay na pumasa ang state check.

---

## Ano ang ginagawa nito

Ano ang makukuha mo agad:

| Kakayahan | Ano ang makukuha mo |
|---|---|
| **God nodes** | Ang pinaka-konektadong mga konsepto, para makita mo kung saan dumadaloy ang lahat |
| **Communities** | Ang graph na hinati sa mga subsystem (Leiden), na may LLM-free na mga label |
| **Cross-file links** | `calls` / `imports` / `inherits` / `mixes_in` na nilutas sa ~40 wika sa pamamagitan ng tree-sitter AST |
| **Query, path, explain** | Magtanong, tunton ang path sa pagitan ng dalawang bagay, o ipaliwanag ang isang konsepto, lahat laban sa `graph.json` |
| **Rationale + doc refs** | Ang mga komentong `# NOTE:` / `# WHY:` at mga sipi ng ADR/RFC ay nagiging first-class na node na naka-link sa code |
| **Higit pa sa code** | Ang mga dokumento, PDF, larawan, at video/audio ay pawang napapasok sa iisang graph |
| **Local-first** | Ang code ay lokal na pina-parse gamit ang tree-sitter (walang LLM, walang lumalabas sa makina mo); ang semantic pass lamang sa mga dokumento/media ang tumatawag sa isang backend, at kung nag-configure ka lang ng isa |

---

## Benchmarks

| Benchmark | Metric | graphify | Field |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | QA accuracy | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | QA accuracy | **76%** | kapantay ng dense RAG |
| Pagtayo ng graph | LLM credits | **0** | per-token para sa karamihan ng sistema |

Bawat sistema ay tumakbo sa parehong harness na may parehong modelo at budget, iniskor ng isang judge na blind-validated laban sa pangalawang judge (90.6% na pagkakasundo, Cohen's kappa 0.81). Kumpletong talaan bawat sistema, ang resulta sa code intelligence, at mga command para sa reproduksyon: **[BENCHMARKS.md](../../BENCHMARKS.md)**.

---

## Mga kinakailangan

| Kinakailangan | Minimum | Pagsusuri | Pag-install |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(inirerekomenda)* | kahit alin | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(alternatibo)* | kahit alin | `pipx --version` | `pip install pipx` |

**Mabilisang pag-install sa macOS (Homebrew):**
```bash
brew install python@3.12 uv
```

**Mabilisang pag-install sa Windows:**
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

## Pag-install

> **Opisyal na package:** Ang PyPI package ay `graphifyy` (dalawang y). Ang iba pang `graphify*` na package sa PyPI ay walang kaugnayan. Ang CLI command ay `graphify` pa rin.

**Hakbang 1 — i-install ang package:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**Hakbang 2 — irehistro ang skill sa iyong AI assistant:**

```bash
graphify install
```

Ayun na. Buksan ang iyong AI assistant at i-type ang `/graphify .`

Upang i-install ang assistant skill sa kasalukuyang repository sa halip na sa iyong user
profile, idagdag ang `--project`:

```bash
graphify install --project
graphify install --project --platform codex
```

Ang mga project-scoped na pag-install ay nagsusulat sa ilalim ng kasalukuyang directory, halimbawa
`.claude/skills/graphify/SKILL.md` o `.agents/skills/graphify/SKILL.md` (kasama ang isang
`references/` sidecar na nilo-load ng skill kapag kailangan), at
nagpi-print ng `git add` na hint para sa mga file na maaaring i-commit.
Ang mga per-platform na command na sumusuporta sa project-scoped na pag-install ay tumatanggap ng parehong flag,
halimbawa `graphify claude install --project` o `graphify codex install --project`.

> **Tala sa PowerShell:** Gamitin ang `graphify .` hindi ang `/graphify .` — ang paunang slash ay path separator sa PowerShell.

> **`graphify: command not found`?** Inilalagay ng `uv tool install` / `pipx install` ang `graphify` command sa kanilang tool bin dir (`~/.local/bin`). Kung hindi ito makita ng shell mo agad pagkatapos ng install — karaniwan sa bagong macOS + zsh setup — hindi pa nasa `PATH` mo ang direktoryong iyon: patakbuhin ang `uv tool update-shell` (o `pipx ensurepath`), pagkatapos ay magbukas ng bagong terminal. Sa payak na `pip`, idagdag ang `~/.local/bin` (Linux) o `~/Library/Python/3.x/bin` (Mac) sa iyong PATH, o patakbuhin ang `python -m graphify`.

> **Tumatakbo gamit ang `uvx` / `uv tool run` sa halip na mag-install?** Pangalanan ang package, hindi ang command: `uvx --from graphifyy graphify install`. Ang payak na `uvx graphify …` ay nabibigo (`No solution found … no versions of graphify`) dahil binabasa ng `uv tool run` ang unang salita bilang isang *package*, at ang package ay `graphifyy` — ang `graphify` command ay nasa loob nito.

> **Iwasan ang `pip install` sa Mac/Windows** kung kaya. Nilulutas ng skill ang Python sa runtime mula sa `graphify-out/.graphify_python`; kung nakaturo iyon sa ibang environment kaysa sa kung saan nag-install ang `pip` ng package, makakakuha ka ng `ModuleNotFoundError: No module named 'graphify'`. Ang `uv tool install` at `pipx install` ay ikinukubli ang package sa sarili nilang env at ganap na iniiwasan ito.

> **Mga git hook at uv tool / pipx:** Ini-embed ng `graphify hook install` ang kasalukuyang interpreter path nang direkta sa mga hook script sa oras ng pag-install, kaya tama ang pag-andar ng post-commit hook kahit sa mga GUI git client at CI runner kung saan wala sa PATH ang `~/.local/bin`. Kung mag-i-install ka ulit o mag-a-upgrade ng graphify, patakbuhin muli ang `graphify hook install` upang i-refresh ang naka-embed na path.

> **Strict mode (Claude Code):** Ginagawa ng `graphify install --project --strict` na talagang gamitin ng assistant ang graph. Ang default na install ay *nagtutulak* lamang dito na patakbuhin ang `graphify query` bago magbasa ng mga file; hinaharangan ng strict mode ang unang hilaw na pagbabasa ng source sa isang session at inilalayo ito papunta sa graph, pagkatapos ay babalik sa pagtutulak (kaya bumibigat ito nang isang beses lang bawat session at hindi kailanman naiipit). I-toggle sa runtime gamit ang `GRAPHIFY_HOOK_STRICT=1`/`0`; hindi nagbabago ang default na install (malumanay na tulak).

<details>
<summary><b>Piliin ang iyong platform</b> (20+ assistant, i-click para lumawak)</summary>

| Platform | Install command |
|----------|----------------|
| Claude Code (Linux/Mac) | `graphify install` |
| Claude Code (Windows) | `graphify install` (awtomatikong natutukoy) o `graphify install --platform windows` |
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

Kailangan din ng mga user ng Codex ang `multi_agent = true` sa ilalim ng `[features]` sa `~/.codex/config.toml` para sa parallel extraction. Ginagamit ng CodeBuddy ang parehong Agent tool at PreToolUse hook na mekanismo tulad ng Claude Code. Ginagamit ng Factory Droid ang `Task` tool para sa parallel subagent dispatch. Ang OpenClaw at Aider ay gumagamit ng sequential extraction (maaga pa ang suporta sa parallel agent sa mga platform na iyon). Ginagamit ng Trae ang Agent tool para sa parallel subagent dispatch at **hindi** ito sumusuporta sa mga `PreToolUse` hook, kaya ang AGENTS.md ang always-on na mekanismo.

Ang `--platform agents` (alias `--platform skills`) ay tumutumbok sa mga generic na cross-framework na lokasyon ng [Agent-Skills](https://github.com/anthropics/skills): ang user-global na `~/.agents/skills/` ng spec (binabasa ng `npx skills` at ng mga spec-compliant na framework) para sa global install, at `./.agents/skills/` para sa project (`--project`) install. Ang payak na `graphify install` ay nananatiling single-platform (Claude Code) sa disenyo — gamitin ang pinangalanang `agents` platform kapag gusto mong matuklasan ang skill ng anumang framework na nagbabasa ng `.agents/skills`.

> Gumagamit ang Codex ng `$graphify` sa halip na `/graphify`.

</details>

<details>
<summary><b>Mga opsyonal na extra</b> (i-install lang ang kailangan mo)</summary>

| Extra | Ano ang idinaragdag nito | Pag-install |
|---|---|---|
| `pdf` | Pag-extract ng PDF | `uv tool install "graphifyy[pdf]"` |
| `office` | Suporta sa `.docx` at `.xlsx` | `uv tool install "graphifyy[office]"` |
| `google` | Pag-render ng Google Sheets | `uv tool install "graphifyy[google]"` |
| `video` | Transkripsyon ng video/audio (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | MCP stdio server | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Suporta sa Neo4j push | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | Suporta sa FalkorDB push | `uv tool install "graphifyy[falkordb]"` |
| `svg` | SVG graph export | `uv tool install "graphifyy[svg]"` |
| `leiden` | Leiden community detection (Python < 3.13 lamang) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Lokal na inference sa Ollama | `uv tool install "graphifyy[ollama]"` |
| `openai` | OpenAI / OpenAI-compatible na mga API | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic Claude API (`--backend claude`, gumagamit ng `ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (gumagamit ng IAM, walang API key) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, gumagamit ng `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "graphifyy[openai]"` |
| `sql` | Pag-extract ng SQL schema | `uv tool install "graphifyy[sql]"` |
| `postgres` | Live na introspection ng PostgreSQL (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | Pag-extract ng AST para sa BYOND DreamMaker `.dm`/`.dme` (maaaring mangailangan ng C compiler + `python3-dev` kung walang wheel na tugma sa platform mo) | `uv tool install "graphifyy[dm]"` |
| `terraform` | Pag-extract ng AST para sa Terraform / HCL `.tf`/`.tfvars`/`.hcl` | `uv tool install "graphifyy[terraform]"` |
| `pascal` | Pag-extract ng AST para sa Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` (mas tumpak na `calls`/`inherits` na edge; babalik sa regex extractor kapag wala) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | Segmentasyon ng Chinese query (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | Lahat ng nasa itaas | `uv tool install "graphifyy[all]"` |

</details>

---

## Palaging gamitin ng iyong assistant ang graph

Patakbuhin ito nang isang beses sa iyong proyekto pagkatapos magtayo ng graph:

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

Nagsusulat ito ng maliit na config file na nagsasabi sa iyong assistant na kumonsulta sa knowledge graph para sa mga tanong tungkol sa codebase, na mas pinipili ang mga scoped na query gaya ng `graphify query "<question>"` kaysa sa pagbabasa ng buong report o pag-grep sa mga hilaw na file.

- **Mga hook platform** (Claude Code, Gemini CLI): awtomatikong pumuputok ang isang hook bago ang mga tool call na tila paghahanap (at, sa Claude Code, bago magbasa ng mga source file nang isa-isa sa pamamagitan ng Read/Glob na tool) at itinutulak ang iyong assistant patungo sa graph path.
- **Mga instruction-file platform** (Codex, OpenCode, Cursor, atbp.): ang mga persistent na instruction file (`AGENTS.md`, `.cursor/rules/`, atbp.) ay nagbibigay ng parehong query-first na gabay.

Available pa rin ang `GRAPH_REPORT.md` para sa malawakang pagsusuri ng arkitektura.

Ginagawa ng **CodeBuddy** ang parehong dalawang bagay tulad ng Claude Code: nagsusulat ito ng seksyon sa `CODEBUDDY.md` na nag-uutos sa CodeBuddy na basahin ang `graphify-out/GRAPH_REPORT.md` bago sumagot sa mga tanong tungkol sa arkitektura, at nag-i-install ng mga `PreToolUse` hook (`.codebuddy/settings.json`) na pumuputok bago ang mga Bash search command at pagbabasa ng file, na itinutulak patungo sa `graphify query` sa halip.

Nagsusulat ang **Codex** sa `AGENTS.md`, na siyang talagang nagdadala ng always-on na gabay sa graph sa platform na ito. Nagrerehistro rin ang `graphify codex install` ng isang `PreToolUse` hook sa `.codex/hooks.json` (`graphify hook-check`), ngunit ang entry na iyon ay sadyang **no-op**: tinatanggihan ng Codex Desktop ang `hookSpecificOutput.additionalContext` sa `PreToolUse`, kaya kung maglalabas ng tulak doon ay masisira ang mga Bash tool call. Hindi tulad sa Claude Code, kung saan ang hook (`graphify hook-guard`) ang nagtutulak, sa Codex ay pumuputok ang hook at sinadyang walang ginagawa, at ang `AGENTS.md` ang always-on na mekanismo.

Ini-install ng **Kilo Code** ang Graphify skill sa `~/.config/kilo/skills/graphify/SKILL.md` at isang native na `/graphify` command sa `~/.config/kilo/command/graphify.md`. Nagsusulat din ang `graphify kilo install` ng `AGENTS.md` kasama ang isang native na `tool.execute.before` plugin (`.kilo/plugins/graphify.js` + pagrehistro sa `.kilo/kilo.json` o `.kilo/kilo.jsonc`) para makuha ng Kilo ang parehong always-on na paalala tungkol sa graph sa pamamagitan ng native na `.kilo` config.

Nagsusulat ang **Cursor** ng `.cursor/rules/graphify.mdc` na may `alwaysApply: true`, kaya awtomatikong isinasama ito ng Cursor sa bawat pag-uusap, walang kailangang hook.

Upang alisin ang graphify sa lahat ng platform nang sabay: `graphify uninstall` (idagdag ang `--purge` upang burahin din ang `graphify-out/`). O gamitin ang per-platform na command (hal. `graphify claude uninstall`).

---

## Ano ang nasa report

- **God nodes** — ang pinaka-konektadong mga konsepto sa iyong proyekto. Lahat ay dumadaan dito.
- **Nakagugulat na koneksyon** — mga link sa pagitan ng mga bagay na nasa magkaibang file o module. Isinasaayos ayon sa kung gaano ka-hindi-inaasahan.
- **Ang "bakit"** — ang mga inline na komento (`# NOTE:`, `# WHY:`, `# HACK:`), docstring, at design rationale mula sa mga dokumento ay ini-extract bilang hiwalay na node na naka-link sa code na ipinapaliwanag nila.
- **Mga iminungkahing tanong** — 4–5 tanong na natatanging kayang sagutin ng graph.
- **Confidence tag** — bawat hinuhang relasyon ay minamarkahan ng `EXTRACTED`, `INFERRED`, o `AMBIGUOUS`. Lagi mong alam kung ano ang natagpuan kumpara sa hinulaan.

---

## Anong mga file ang kaya nito

| Uri | Extension |
|------|-----------|
| Code (36 tree-sitter grammar) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (ang `.dm`/`.dme` ay nangangailangan ng `uv tool install graphifyy[dm]`; ang `.mts`/`.cts` ay gumagamit muli ng TypeScript grammar, ang `.cc`/`.cxx` at CUDA `.cu`/`.cuh` at Metal `.metal` ay gumagamit muli ng C++ grammar) |
| Salesforce Apex | `.cls .trigger` (regex-based; mga class, interface, enum, method, trigger, SOQL/DML na edge) |
| Terraform / HCL | `.tf .tfvars .hcl` (nangangailangan ng `uv tool install graphifyy[terraform]`) |
| Mga MCP config | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — ini-extract ang mga server node, package ref, kinakailangang env var |
| Mga package manifest | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — isang kanonikal na package node bawat package (ayon sa pangalan) kasama ang mga `depends_on` na edge, kaya ang isang package na ni-reference mula sa maraming manifest ay iisang hub |
| Mga dokumento | `.md .mdx .qmd .html .txt .rst .yaml .yml` (ang mga markdown na link na `[text](./other.md)` at `[[wikilinks]]` ay nagiging `references` na edge sa pagitan ng mga dokumento) |
| Office | `.docx .xlsx` (nangangailangan ng `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (opt-in; nangangailangan ng `gws` auth at `--google-workspace`; ang Sheets ay nangangailangan ng `uv tool install graphifyy[google]`) |
| Mga PDF | `.pdf` |
| Mga larawan | `.png .jpg .webp .gif` |
| Video / Audio | `.mp4 .mov .mp3 .wav` at iba pa (nangangailangan ng `uv tool install graphifyy[video]`) |
| YouTube / URL | anumang video URL (nangangailangan ng `uv tool install graphifyy[video]`) |

Ang code ay ini-extract **nang lokal nang walang API call** (AST sa pamamagitan ng tree-sitter). Ang lahat ng iba pa ay dumadaan sa model API ng iyong AI assistant.

Ang mga `.gdoc`, `.gsheet`, at `.gslides` na file ng Google Drive for desktop ay mga
shortcut pointer, hindi nilalaman ng dokumento. Upang isama ang native na Google Docs, Sheets, at Slides
sa isang headless na extraction, i-install at i-authenticate ang
[`gws` CLI](https://github.com/googleworkspace/cli), pagkatapos ay patakbuhin:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

Maaari mo ring itakda ang `GRAPHIFY_GOOGLE_WORKSPACE=1`. Ine-export ng Graphify ang mga shortcut sa
`graphify-out/converted/` bilang Markdown sidecar, pagkatapos ay ini-extract ang mga file na iyon.

---

## Mga karaniwang command

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

Tingnan ang [Decouple: mga kandidatong Extract-Class na may risk score](#decouple-mga-kandidatong-extract-class-na-may-risk-score) sa itaas, o ang [buong sanggunian ng mga command](#buong-sanggunian-ng-mga-command) sa ibaba.

---

## Pag-ignore sa mga file

Gumawa ng `.graphifyignore` sa root ng iyong proyekto — parehong syntax ng `.gitignore`, kasama ang `!` na negasyon.

**Awtomatikong iginagalang ang `.gitignore`.** Binabasa ng graphify ang `.gitignore` sa bawat direktoryo. Kung may `.graphifyignore` din, ang dalawa ay **pinagsasama** — ang mga pattern ng `.graphifyignore` ay sinusuri huli, kaya sila ang nananaig sa mga hidwaan (kasama ang mga `!` na negasyon). Ang pagdaragdag ng `.graphifyignore` ay palaging nagbubukod lamang ng mas marami; hindi nito muling isinasama ang isang file na naibukod na ng iyong `.gitignore`. Ang saklaw sa subdirectory ay gumagana katulad ng sa git — ang isang ignore file ay nakakaapekto lamang sa sarili nitong subtree.

Ipasa ang `--no-gitignore` sa `graphify extract` kapag ang git-ignored na generated o transpiled na code ay nararapat na nasa graph. Idi-disable nito ang `.gitignore` at `.git/info/exclude`; ang `.graphifyignore` ay gumagana pa rin.

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

## Setup ng team

Ang `graphify-out/` ay nilalayong i-commit sa git para lahat sa team ay magsimula na may mapa.

**Inirerekomendang dagdag sa `.gitignore`:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> Portable na ngayon ang `manifest.json` — ang mga key ay iniimbak bilang relative path at muling ini-anchor sa pag-load, kaya ligtas itong i-commit at naiiwasan ang buong rebuild sa unang checkout.

**Workflow:**
1. Isang tao ang magpapatakbo ng `/graphify .` at magko-commit ng `graphify-out/`.
2. Magpu-pull ang lahat — babasahin agad ng kanilang assistant ang graph.
3. Patakbuhin ang `graphify hook install` upang awtomatikong magtayo muli pagkatapos ng bawat commit (AST lamang, walang API cost). Nagtatakda rin ito ng git merge driver kaya hindi kailanman naiiwang may conflict marker ang `graph.json` — ang dalawang dev na sabay na nag-commit ay awtomatikong napagsasama ang kanilang graph sa union merge.
4. Kapag nagbago ang mga dokumento o papel, patakbuhin ang `/graphify --update` upang i-refresh ang mga node na iyon.

---

## Paggamit ng graph nang direkta

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

Binibigyan ng MCP server ang iyong assistant ng structured na access: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Shared na HTTP server

Ang `--transport stdio` (ang default) ay naglulunsad ng isang lokal na server bawat developer. Ang `--transport http` ay naghahain ng parehong mga tool sa pamamagitan ng MCP Streamable HTTP transport, kaya ang iisang shared na proseso ay makapaghahain ng graph para sa buong team — itinuturo ng mga client ang kanilang IDE MCP config sa `http://<host>:8080/mcp` sa halip na magpatakbo ng graphify nang lokal.

| Flag | Default | Layunin |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Transport na paghahainan |
| `--host` | `127.0.0.1` | HTTP bind host (gamitin ang `0.0.0.0` upang ilantad lampas sa localhost) |
| `--port` | `8080` | HTTP bind port |
| `--api-key` | env `GRAPHIFY_API_KEY` | Nangangailangan ng `Authorization: Bearer <key>` (o `X-API-Key`) |
| `--path` | `/mcp` | HTTP mount path |
| `--json-response` | naka-off | Nagbabalik ng payak na JSON sa halip na SSE stream |
| `--stateless` | naka-off | Walang per-session na state (para sa load-balanced / CI na deployment) |
| `--session-timeout` | `3600` | Nililinis ang mga idle na stateful session pagkatapos ng N segundo (`0` upang i-disable) |

Ang default na `127.0.0.1` bind ay loopback lamang. Itakda ang `--host 0.0.0.0` **at** `--api-key` nang magkasama kapag inilalantad sa isang shared na host. Patakbuhin ito sa isang container:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **Tala sa WSL / Linux:** Ang Ubuntu ay may `python3`, hindi `python`. Gumamit ng venv upang maiwasan ang mga hidwaan:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## Mga environment variable

Kailangan lang ang mga ito para sa **headless / CI na extraction** (`graphify extract`). Kapag tumatakbo sa pamamagitan ng `/graphify` skill sa loob ng iyong IDE, ang model API ay ibinibigay ng iyong IDE session — walang kailangang dagdag na key.

| Variable | Ginagamit para sa | Kailan kailangan |
|---|---|---|
| `ANTHROPIC_API_KEY` | Claude (Anthropic) na backend | `--backend claude` |
| `ANTHROPIC_BASE_URL` | Anthropic-compatible na endpoint URL (LiteLLM proxy, gateway, ...) | `--backend claude` (default: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Pangalan ng modelo para sa Claude backend — para sa custom na endpoint, gamitin ang pangalan/alias ng modelong inilalantad ng server mo | `--backend claude` (default: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` o `GOOGLE_API_KEY` | Google Gemini na backend | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI o OpenAI-compatible na mga API | `--backend openai` (tumatanggap ang mga lokal na server ng anumang hindi-blangkong halaga) |
| `OPENAI_BASE_URL` | OpenAI-compatible na server URL (llama.cpp, vLLM, LM Studio, ...) | `--backend openai` (default: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | Pangalan ng modelo para sa OpenAI backend — para sa self-hosted na server, gamitin ang pangalan/alias ng modelong inilalantad ng server mo (tingnan ang `/v1/models` endpoint nito), hal. `LFM2.5-8B-A1B-UD-Q4_K_XL` para sa llama.cpp | `--backend openai` (default: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | DeepSeek na backend | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Kimi Code na backend | `--backend kimi` |
| `OLLAMA_BASE_URL` | URL ng lokal na Ollama inference | `--backend ollama` (default: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Pangalan ng modelo ng Ollama | `--backend ollama` (default: awtomatikong tuklas) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | I-override ang laki ng KV-cache window ng Ollama | opsyonal — awtomatikong sinusukat bilang default |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Minuto na mananatiling naka-load ang modelo ng Ollama | opsyonal — itakda sa `0` upang i-unload pagkatapos ng bawat chunk |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI Service na backend | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | URL ng endpoint ng Azure resource | `--backend azure` (kinakailangan kasabay ng API key) |
| `AZURE_OPENAI_API_VERSION` | Pag-override sa bersyon ng Azure API | opsyonal — default `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` o `GRAPHIFY_AZURE_MODEL` | Pangalan ng Azure deployment | opsyonal — default `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — standard na credential chain | `--backend bedrock` (walang API key, gumagamit ng IAM) |
| `GRAPHIFY_MAX_WORKERS` | Bilang ng thread para sa AST parallelism | opsyonal — mayroon ding `--max-workers` na flag |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Itaas ang output cap para sa siksik na corpora | opsyonal — hal. `32768` para sa malalaking file |
| `GRAPHIFY_API_TIMEOUT` | Per-call na timeout sa segundo para sa HTTP, claude-cli, Anthropic SDK, at Bedrock na backend (default: 600) | opsyonal — mayroon ding `--api-timeout` na flag |
| `GRAPHIFY_MAX_RETRIES` | Ilang beses uulitin ang isang rate-limited (429) na request bago sumuko (default: 6; iginagalang ang `Retry-After`) | opsyonal — itaas para sa mahigpit na per-org na limitasyon (hal. kimi); `0` upang i-disable |
| `GRAPHIFY_FORCE` | Ipilit ang graph rebuild kahit mas kaunti ang node | opsyonal — mayroon ding `--force` na flag |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Awtomatikong buksan ang Google Workspace export | opsyonal — itakda sa `1` |
| `GRAPHIFY_TRIAGE_BACKEND` | Backend para sa `graphify prs --triage` | opsyonal — awtomatikong natutukoy mula sa mga available na key |
| `GRAPHIFY_TRIAGE_MODEL` | Pag-override ng modelo para sa triage | opsyonal — hal. `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | Itakda sa `1` upang buksan ang lokal na query log sa `~/.cache/graphify-queries.log` (itinatala ang bawat tanong sa query/path/explain + corpus path). Naka-off bilang default — walang isinusulat maliban kung mag-opt in ka (#1797) | opsyonal |
| `GRAPHIFY_QUERY_LOG` | Buksan ang query log at isulat ito sa path na ito sa halip na sa default | opsyonal — naka-off maliban kung nakatakda ito o ang `_ENABLE` |
| `GRAPHIFY_QUERY_LOG_DISABLE` | Itakda sa `1` upang piliting isara ang query log (nananaig sa mga enable na variable) | opsyonal |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | Kapag naka-on ang log, itala rin ang buong subgraph na tugon (naka-off bilang default) | opsyonal |
| `GRAPHIFY_MAX_GRAPH_BYTES` | I-override ang 512 MiB na limitasyon sa laki ng graph.json — hal. `700MB`, `2GB`, o payak na byte | opsyonal — kapaki-pakinabang para sa napakalaking corpora |
| `GRAPHIFY_MAX_CONTEXTS` | Pinakamaraming hindi-default na project graph na pinananatili ng isang multi-project MCP server | opsyonal — default: `8`; ang mga di-wastong halaga ay gumagamit ng `8`, at ang mga halagang mas mababa sa `1` ay gumagamit ng `1` |
| `GRAPHIFY_LLM_TEMPERATURE` | I-override ang LLM temperature para sa semantic extraction — hal. `0.7`, o `none` upang alisin | opsyonal — awtomatikong inaalis para sa o1/o3/o4/gpt-5 na reasoning model |

---

## Privacy

- **Mga code file** — pinoproseso nang lokal sa pamamagitan ng tree-sitter. Walang lumalabas sa makina mo. Ang isang code-only na corpus ay hindi nangangailangan ng API key — tumatakbo ang `graphify extract` nang ganap na offline. Sa isang halo-halong repo, idagdag ang `--code-only` upang i-index lang ang code at laktawan ang mga dokumento/PDF/larawan na mangangailangan sana ng LLM.
- **Video / audio** — nililipat sa teksto nang lokal gamit ang faster-whisper. Walang lumalabas sa makina mo.
- **Mga dokumento, PDF, larawan** — ipinapadala sa iyong AI assistant para sa semantic extraction (sa pamamagitan ng `/graphify` skill, gamit ang anumang modelo na pinapatakbo ng iyong IDE session). Ang headless na `graphify extract` ay nangangailangan ng `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), isang tumatakbong Ollama instance (`OLLAMA_BASE_URL`), AWS credential sa pamamagitan ng standard na provider chain (Bedrock — walang API key na kailangan, gumagamit ng IAM), o ang `claude` CLI binary (Claude Code — walang API key na kailangan, gumagamit ng iyong Claude subscription). Ang `--dedup-llm` na flag ay gumagamit ng parehong key.
- **Data residency** — awtomatikong tinutukoy ng `graphify extract` kung aling provider ang gagamitin batay sa kung aling API key ang nakatakda (prayoridad: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). Para sa code na may mga kinakailangan sa data residency, gamitin ang `--backend ollama` (ganap na lokal) o ipasa ang isang tahasang `--backend` na flag. Ang Kimi (`MOONSHOT_API_KEY`) ay dumadaan sa mga server ng Moonshot AI sa China.
- **Walang telemetry**, walang usage tracking, walang analytics.
- **Query logging** — bawat `graphify query`, `graphify path`, `graphify explain`, at MCP na `query_graph` na tawag ay itinatala sa `~/.cache/graphify-queries.log` sa format na JSON Lines (timestamp, tanong, corpus, mga node na ibinalik, tagal). Ang buong subgraph na tugon ay **hindi** iniimbak bilang default. Itakda ang `GRAPHIFY_QUERY_LOG_DISABLE=1` upang mag-opt out, o `GRAPHIFY_QUERY_LOG=/dev/null` upang patahimikin nang hindi ini-disable ang code path.

---

## Mga Limitasyon at Hangganan

Ano ang sinasadyang **hindi** ginagawa ng graphify, at kung saan humihinto ang saklaw nito:

- **Hindi ito semantic/vector search engine.** Ang graph ay structural — mga node at typed edge na nalutas mula sa source, hindi embeddings. Tinatahak ng `graphify query`/`path`/`explain` ang estrukturang iyon; hindi nila kayang ilabas ang isang koneksyon na hindi kinakatawan bilang edge, kahit "semantically" itong may kaugnayan. Walang similarity/nearest-neighbor na fallback.
- **Ang mga dokumento, PDF, larawan, at headless na video/URL extraction ay hindi eksklusibong lokal.** Tanging ang code (tree-sitter AST) at audio/video transcription (faster-whisper) lamang ang tumatakbo nang ganap na offline. Ang pag-extract ng mga dokumento/PDF/larawan ay palaging tumatawag ng LLM — ang modelo ng iyong AI assistant sa pamamagitan ng `/graphify` skill, o isang naka-configure na backend API key para sa headless na `graphify extract`. Tingnan ang [Privacy](#privacy) sa itaas para sa eksaktong flag o key na kailangan ng bawat landas.
- **Hindi saklaw ng state-sharing check ng decouple ang lahat ng wika.** Walang maaasahang senyas na `self`/`this` ang C nang walang ganap na type inference, kaya ito ay hindi kasama (tingnan ang [talaan ng saklaw ng wika](#decouple-mga-kandidatong-extract-class-na-may-risk-score) sa itaas). Ang isang god node sa wikang hindi suportado, o isang node na hindi mabasa ang source, ay bumabalik sa call-graph-only na pag-iskor (`state_analysis: "skipped"`) sa halip na isang beripikadong state check.
- **Ang 3D data-flow floor ay isang name heuristic, hindi dataflow/taint analysis.** Ang I/O-boundary detection ng `data_floor` (parser, loader, reader, writer, DB/HTTP client) ay tumutugma batay sa naming convention (`boundary_reason`); ang isang boundary node na may hindi-karaniwang pangalan ay maaaring hindi mahuli, kaya nauunderstate kung gaano kalalim ang natitirang bahagi ng graph.
- **Ang mga confidence tag ay ang sariling resolution confidence ng graphify, hindi ganap na katotohanan.** Ang mga edge na `INFERRED` at `AMBIGUOUS` ay best-effort na resolution at maaari pa ring mali, lalo na para sa mga lubhang dynamic na idyoma (reflection, runtime dispatch, metaprogramming) na hindi kayang lubos na lutasin ng anumang static na AST pass.
- **Ang HTML visualization at ang laki ng graph ay pareho may kisame.** Ang `graph.html` / `DECOUPLE.html` ay lumalaktaw sa pagbuo kapag lampas na sa 5,000 node bilang default (`MAX_NODES_FOR_VIZ`, itinataas sa pamamagitan ng `GRAPHIFY_VIZ_NODE_LIMIT`); ang `graph.json` mismo ay may limitasyong 512 MiB (`GRAPHIFY_MAX_GRAPH_BYTES` upang i-override). Gamitin ang `--no-viz` kasama ng `query`/`path`/`explain` para sa mga corpus na lampas sa alinman sa dalawang limitasyon.
- **Ang cross-project awareness ay opt-in, hindi awtomatiko.** Nakikita lamang ng `graphify query` ang isang graph na itinuturo mo. Ang mga tanong na sumasaklaw sa maraming repo ay nangangailangan ng tahasang pagrehistro muna sa bawat proyekto sa shared graph (`graphify global add`, may limitasyong `GRAPHIFY_MAX_CONTEXTS` na hindi-default na context bawat MCP server) — hindi kailanman sinisiyasat ng graphify ang iyong makina para sa ibang repo nang mag-isa.
- **Ang parallel multi-agent extraction ay nakadepende sa platform.** Kailangan nito ng suporta sa panig ng assistant para sa paglulunsad ng subagent (`multi_agent = true` sa `~/.codex/config.toml` para sa Codex, ang Agent/Task tool sa Claude Code/CodeBuddy/Factory Droid/Trae). Ang OpenClaw at Aider sa ngayon ay sunud-sunod (sequential) lamang ang extraction.
- **Ang shared MCP HTTP server ay naka-bind lamang sa loopback bilang default.** Ang pag-abot dito mula sa ibang makina ay nangangailangan ng tahasang `--host 0.0.0.0` **at** `--api-key`; hindi pinamamahalaan ng graphify ang TLS o anumang awtentikasyon lampas sa iisang bearer token na iyon.
- **Ipinapakahulugan ng PowerShell ang paunang `/` bilang path separator.** Nabibigo ang `/graphify .` sa Windows PowerShell dahil dito, hindi dahil sa bug ng graphify — gamitin sa halip ang `graphify .`.

---

## Pag-troubleshoot

**`graphify: command not found` pagkatapos mag-install**
Naka-install ang CLI ngunit wala sa `PATH` ng shell mo ang bin directory nito. Piliin ang lunas ayon sa paraan ng pag-install mo:
- **uv** (`uv tool install graphifyy`): napupunta ang command sa tool bin dir ng uv (`~/.local/bin`), na kadalasang wala sa `PATH` sa isang bagong macOS/zsh na setup. Patakbuhin ang `uv tool update-shell`, pagkatapos ay magbukas ng bagong terminal. (Hanapin ang direktoryo gamit ang `uv tool dir --bin`.)
- **pipx** (`pipx install graphifyy`): patakbuhin ang `pipx ensurepath`, pagkatapos ay magbukas ng bagong terminal.
- **pip** (`pip install graphifyy`): ini-install ng pip ang mga script sa isang user bin dir na maaaring wala sa `PATH` — idagdag ang `~/Library/Python/3.x/bin` (macOS) o `~/.local/bin` (Linux) sa iyong `PATH` sa `~/.zshrc`/`~/.bashrc`, o patakbuhin na lang ang `python -m graphify`.

**Nabibigo ang `uvx graphify …` o `uv tool run graphify …` na lutasin ang `graphify`**
Ang PyPI package ay `graphifyy`; ang `graphify` ay ang command lamang na ibinibigay nito. Itinuturing ng `uv tool run` ang unang salita bilang *pangalan ng package*, kaya naghahanap ito ng package na tinatawag na `graphify` at nag-uulat ng `No solution found … no versions of graphify`. Pangalanan nang tahasan ang package: `uvx --from graphifyy graphify install` (kapareho ng `uv tool run --from graphifyy graphify install`). O `uv tool install graphifyy` nang isang beses at pagkatapos ay tawagin ang `graphify` nang direkta.

**Tahimik na nagpapatakbo ng mas lumang install ang `uv run --with graphifyy python -m graphify`**
Gumagamit ang `uv run` ng *system* Python mo, kaya kung may mas lumang `graphifyy` din doon (hal. isang dating `pip install graphifyy`), makikita ng Python ang kopyang iyon muna sa `sys.path` at hindi ito papalitan ng `--with graphifyy`. Tumatakbo ito nang walang error, ngunit makukuha mo ang ugali ng *lumang* bersyon — hal. tahimik na binabalewala ang mga env override gaya ng `OPENAI_BASE_URL`, kaya tumatama ang mga request sa default na endpoint at nabibigo sa 401 na mukhang masamang key. Ang fingerprint ay isang linyang `warning: skill is from graphify <newer>, package is <older>` — ibig sabihin ay ibang install ang na-load, hindi lang lumang skill. Suriin kung aling kopya talaga ang na-load:
```bash
python -c "import graphify; print(graphify.__file__)"
```
Pagkatapos ay patakbuhin nang direkta ang naka-install na command (ginagamit nito ang kopyang pinamamahalaan ng uv), o alisin ang lumang kopya ng system:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**Gumagana ang `python -m graphify` ngunit hindi ang `graphify` na command**
Hindi kasama sa `PATH` ng shell mo ang bin directory kung saan naka-install ang command. Mas piliin ang `uv tool install` / `pipx install` kaysa sa payak na `pip`, pagkatapos ay patakbuhin ang `uv tool update-shell` / `pipx ensurepath` at magbukas ng bagong terminal (tingnan ang mga tala sa pag-install sa itaas).

**Nagdudulot ang `/graphify .` ng "path not recognized" sa PowerShell**
Itinuturing ng PowerShell ang paunang `/` bilang path separator. Gamitin ang `graphify .` (walang slash) sa Windows.

**Mas kaunti ang node ng graph pagkatapos ng `--update` o rebuild**
Kung may refactor na nagbura ng mga file, nananatili ang mga lumang node. Ipasa ang `--force` (o itakda ang `GRAPHIFY_FORCE=1`) upang i-overwrite kahit mas kaunti ang node ng rebuild.

**Lumalabas ang `extract` na may "extraction was incomplete ... refusing to overwrite"**
Kapag nag-crash ang isang extraction pass o hindi kayang basahin nang buo ng walk ang corpus, mas maliit ang magiging run kaysa sa kumpleto, kaya tumatanggi ang `graphify extract` na i-overwrite ang mas malaking umiiral na graph gamit ang bahagyang resulta (pinoprotektahan ang `graph.json` mo). Ayusin ang pinagmumulan ng pagkabigo at patakbuhin muli, o ipasa ang `--allow-partial` upang mag-overwrite pa rin.

**May duplicate na node ang graph para sa parehong entity (ghost duplicate)**
Ang mga ghost duplicate (parehong simbolo na lumitaw nang dalawang beses — isa mula sa AST extraction na may source location, isa mula sa semantic extraction na wala) ay awtomatiko nang pinagsasama sa build time. Kung makikita mo ito sa isang graph na itinayo bago ang v0.8.33, magpatakbo ng buong re-extract upang linisin:
```bash
graphify extract . --force
```

**Naubusan ng VRAM ang Ollama / lumagpas sa context window**
Awtomatikong sinusukat ang KV-cache window ngunit maaaring masyadong malaki para sa GPU mo. Bawasan ito:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**Mga babalang `LLM returned invalid JSON` / `Unterminated string`**
Umabot sa limitasyon ng output token ang JSON na tugon ng modelo at naputol sa gitna ng string. Awtomatikong nakababawi ang graphify (hinahati nito ang chunk at ini-extract muli ang mga kalahati, at ang isang labis-labis na laking dokumento ay unang hinihiwa sa hangganan ng heading/talata para masaklaw pa rin ang buong file), kaya maingay ang mga babalang ito ngunit hindi pagkawala ng data. Upang bawasan ang gulo, itaas ang output cap o paliitin ang output ng bawat chunk:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
Sa isang cloud gateway gaya ng OpenRouter, mas piliin ang `--backend openai` (itakda ang `OPENAI_BASE_URL`) kaysa sa Ollama shim — mas malinis itong OpenAI-compatible na daan. Kung may sariling max-output na limitasyon ang modelo, ang pagbaba ng `--token-budget` ang maaasahang panghawakan.

**Masyadong malaki ang graph HTML para buksan sa browser (>5000 node)**
Laktawan ang pagbuo ng HTML at gamitin nang direkta ang JSON:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**May conflict marker ang `graph.json` matapos sabay na mag-commit ang dalawang dev**
Patakbuhin ang `graphify hook install` — nagtatakda ito ng git merge driver na awtomatikong union-merge ang `graph.json` kaya hindi na nangyayari ang mga hidwaan.

**Nagbabalik ng walang lamang node/edge ang extraction para sa mga dokumento o PDF**
Ang mga dokumento, PDF, at larawan ay nangangailangan ng tawag sa LLM — ang mga code-only na corpora ay hindi nangangailangan ng key. Tiyaking nakatakda ang API key mo at tama ang backend:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**Babala tungkol sa hindi tugmang bersyon ng skill sa iyong IDE**
Iba ang naka-install mong bersyon ng graphify sa skill file. I-update:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**Nawawalan ng bisa ang prompt cache ng Claude Code pagkatapos ng bawat `graphify extract`**
Nagsusulat ang Graphify ng mga output file (`graph.json`, `graphify-out/`) sa workspace. Kung hindi na-ignore ang mga path na iyon, bawat pagsulat ay nagpapawalang-bisa sa prompt cache ng Claude Code, na pumipilit ng buong re-upload sa cache-write na rate sa susunod na turn. Idagdag ang mga ito sa `.claudeignore`:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## Buong sanggunian ng mga command

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

> **Mga pangalan ng community:** sa loob ng isang agent (Claude Code, Gemini CLI) ang agent mismo ang nagpapangalan sa mga community. Kapag pinatakbo mo ang payak na CLI, awtomatikong pinapangalanan ng `cluster-only` ang mga ito gamit ang naka-configure na backend (built-in o custom na OpenAI-compatible na provider) — ipasa ang `--no-label` upang panatilihin ang `Community N`, o patakbuhin ang `graphify label` upang (muling) bumuo ng mga pangalan kapag kailangan.

---

## Matuto pa

- [Paano ito gumagana](../how-it-works.md) — ang extraction pipeline, community detection, confidence scoring, benchmarks
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — paghahati ng module, paano magdagdag ng wika
- [Mga opsyonal na integrasyon](../docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — ang aklat tungkol sa mga ideya sa likod ng graphify, ang arkitektura mula simula hanggang wakas

---

## graphify Enterprise

Ang [**graphify Enterprise**](https://graphify.com) ang always-on na layer na itinayo sa ibabaw ng graphify — inilalapat nito ang parehong graph na paraan sa buong konteksto ng iyong trabaho: mga meeting, file, dokumento, at code, patuloy na nag-a-update sa background.

Ginawa para sa mga tao at team na ang trabaho ay nakakalat sa daan-daang pag-uusap at dokumento na hindi na nila kayang tipunin muli nang buo.

**[Sumali sa waitlist sa graphify.com](https://graphify.com).** Malapit nang ilunsad ang libreng subok.

---

<details>
<summary>Pag-aambag</summary>

### Setup para sa development

Gumagamit ang proyekto ng [uv](https://docs.astral.sh/uv/) para sa dev workflow. I-install ito nang isang beses, pagkatapos:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

Beripikahin ang editable na install:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### Pagpapatakbo ng mga test

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> Tala para sa macOS: kasama sa test suite ang parehong `sample.f90` at `sample.F90` na fixture. Nagbabanggaan ang mga ito sa case-insensitive na HFS+ / APFS na file system. Patakbuhin sa Linux o sa isang Docker container kung kailangan mong subukin ang parehong bersyon ng Fortran nang sabay.

### Git workflow

- Nangyayari ang aktibong development sa `v8` na branch.
- Estilo ng commit: `fix: <description>` / `feat: <description>` / `docs: <description>`
- Bago magbukas ng PR, patakbuhin ang `uv run pytest tests/ -q` at tiyaking pumasa ito.
- Magdagdag ng fixture file sa `tests/fixtures/` at mga test sa `tests/test_languages.py` para sa anumang bagong language extractor.

### Ano ang maiaambag

**Mga worked example** ang pinakakapaki-pakinabang na ambag. Patakbuhin ang `/graphify` sa isang totoong corpus, i-save ang output sa `worked/{slug}/`, sumulat ng tapat na `review.md` na sumasaklaw sa kung ano ang tama at mali sa graph, at magbukas ng PR.

**Mga bug sa extraction** — magbukas ng issue kasama ang input file, ang cache entry (`graphify-out/cache/`), at kung ano ang nakaligtaan o mali.

Tingnan ang [ARCHITECTURE.md](../../ARCHITECTURE.md) para sa mga responsibilidad ng module at kung paano magdagdag ng wika.

</details>
