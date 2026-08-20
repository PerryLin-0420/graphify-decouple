<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>Un fork al <a href="https://github.com/Graphify-Labs/graphify">graphify</a> care adaugă <code>graphify decouple</code></b> — candidați Extract Class cu scor de risc pentru god objects, 0-LLM, re-verificați față de sursa reală (nu doar față de call graph) înainte să recomande ceva. Vezi <a href="#decouple-candidați-extract-class-cu-scor-de-risc">Decouple: candidați Extract Class cu scor de risc</a> mai jos.
</p>

<div align="center">
<details><summary><b>Citește acest text în alte limbi</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>Accesul timpuriu la platforma graphify este deschis înainte de lansarea publică v1: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

Scrie `/graphify` în asistentul tău AI de programare și acesta îți transpune întregul proiect (cod, documente, PDF-uri, imagini, video) într-un **graf de cunoștințe** pe care îl poți **interoga în loc să faci grep** prin fișiere.

- **Hărți de cod gratuite, complet locale.** Codul este parsat cu AST tree-sitter: determinist, fără LLM, nimic nu îți părăsește mașina. (Documentele, PDF-urile, imaginile și clipurile video folosesc modelul asistentului tău, sau o cheie API configurată, pentru o trecere semantică.)
- **Fiecare muchie este explicată.** Fiecare conexiune este etichetată `EXTRACTED` (explicită în sursă) sau `INFERRED` (rezolvată de graphify), astfel încât poți distinge ce a fost citit direct de ce a fost dedus.
- **Nu este un index vectorial.** Fără embedding-uri, fără vector store: un graf real pe care îl parcurgi. Pune o întrebare, urmărește drumul dintre două lucruri sau cere explicarea unui concept.

> Vrei asta mereu activ, actualizându-se în fundal peste codul, documentele și ședințele tale, nu doar la cerere? Exact asta construim la **[graphify.com](https://graphify.com)**, iar accesul timpuriu este deschis acum la **[app.graphify.com](https://app.graphify.com/login)**.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="graph.html interactiv din graphify, arătând codebase-ul FastAPI ca un graf de cunoștințe force-directed, cu o legendă a comunităților detectate" width="900">
</p>
<p align="center">
  <em>Codebase-ul FastAPI cartografiat de graphify. Fiecare nod este un concept, culorile sunt comunități detectate, iar totul este clicabil în graph.html.</em>
</p>

**Primii pași** (30 de secunde):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

Apoi, în asistentul tău AI:

```
/graphify .
```

Asta e tot. Primești **trei fișiere**:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**Funcționează în** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot și încă 15+ — [alege-ți platforma](#instalare).

---

## Vezi-l în acțiune

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="interogare de drum în graphify: un terminal cere cel mai scurt drum dintre FastAPI și ModelField, iar răspunsul se aprinde pas cu pas prin graful de cunoștințe" width="900">
</p>

Odată construit graful, îl interoghezi în loc să citești fișiere. Ieșire reală, graphify rulat pe codebase-ul FastAPI arătat mai sus:

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

Fiecare muchie poartă o **etichetă de încredere** (`EXTRACTED` = explicită în sursă, `INFERRED` = derivată prin rezolvare), așa că poți distinge ce a fost citit direct de ce a fost dedus. `graphify query "<question>"` returnează un subgraf delimitat pentru o întrebare în limbaj natural, iar `graphify path A B` urmărește cum se leagă oricare două lucruri.

---

## Decouple: candidați Extract Class cu scor de risc

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: nodul god MainWindow se împarte în clase candidat cu scor de risc, cu un avertisment de stare partajată între două dintre ele" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: cele 5 clase propuse pentru MainWindow, panoul Node Info deschis pe Main Window Axis and Range Controls, arătând o suprapunere de stare de 0,608 cu Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>DECOUPLE.html pe o rulare reală — un clic pe o clasă propusă arată exact cu ce altă clasă își partajează starea și ce anume este partajat.</em>
</p>

Aceeași pagină randează și împărțirea în sine. Comutarea pe **Preview decoupled view** înlocuiește metodele proprii ale clasei god cu clasele propuse și reorientează muchiile pe loc — schimbarea de cablaj, nu o diagramă redesenată:

| Înainte — clasa god de azi | După — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html înainte de comutare: un singur nod hub MainWindow cu propriile metode desfășurate în jurul lui" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html după comutare: același nod redus la 5 clase propuse în formă de romb, muchii verzi punctate care arată ce metode au fost extrase în fiecare, muchii roșii care arată starea de instanță partajată între două dintre ele" width="440"> |
| Un singur nod care ține 47 dintre propriile metode, fiecare dintre ele accesibilă doar prin clasă. | Clasele propuse. Verde punctat = ce a fost extras în fiecare; roșu = starea de instanță pe care două dintre ele încă o partajează, exact ceea ce decide între `split` și `keep_as_is`. Sunt desenați doar candidații care trec pragul de risc — aici 5 din 6, motiv pentru care o metodă nu are niciun romb pe care să aterizeze. |

`graphify decouple` găsește god objects și îți spune dacă împărțirea lor merită cu adevărat — nu doar că sunt mari.

Modul de eșec pe care există ca să îl prindă: o clasă cu 47 de metode pe care clusterizarea pe call graph o împarte fericită în 5 grupuri cu aspect ordonat, dintre care toate citesc și scriu dedesubt exact aceeași stare de instanță `self._chart_style` / `self._crosshair`. Livrează acea împărțire și nu ai decuplat nimic — ai mutat metode în fișiere noi care tot nu pot fi testate, modificate sau înțelese independent, pentru că toate au în continuare nevoie ca aceeași stare partajată să le fie pasată înapoi. Un instrument care se uită doar la call graph nu poate vedea deloc acest lucru; trebuie să se întoarcă la sursa reală.

**Două verificări, ambele 0-LLM, ambele deterministe:**

1. **Este într-adevăr un God Object?** Un nod cu grad mare poate fi un God Object veritabil (multe metode PROPRII, răspândite pe responsabilități fără legătură — Extract Class se aplică) sau un hub/model de date supra-referențiat (puține metode proprii, majoritar referințe *de intrare* — împărțirea corpului nu ajută cu nimic; soluția e îngustarea interfeței, nu extragerea unei clase). `classify_god_node` le deosebește prin `member_ratio`, nu prin gradul brut — diferența care îl ferește pe `TraceSource` (84 de muchii, dar doar 6 metode proprii) de o sugestie de împărțire falsă, pe care `MainWindow` (88 de muchii, 47 de metode proprii) o primește pe bună dreptate.
2. **Ar reduce împărțirea cuplarea, cu adevărat?** `risk_before` (dimensiunea/cuplarea/fragmentarea actuală a nodului god) este comparat cu `risk_after` — riscul NOU pe care l-ar introduce împărțirea însăși: apeluri între grupuri care erau muchii invizibile în interiorul clasei și devin dependențe explicite între clase, apelanți care ar trebui acum să depindă de mai mult de o clasă nouă și — verificarea pe care un call graph nu o poate face structural — cât din starea de instanță `self`/`this` (citiri, scrieri și apeluri partajate de metode helper, ponderate separat: o **scriere** partajată primește un scor mai mare decât o citire partajată) au efectiv în comun grupurile propuse. Aceasta re-parsează direct fișierul sursă al nodului god cu tree-sitter; nu se bazează pe graful extras de graphify, care nu înregistrează niciodată accesul la nivel de câmp, pentru nicio limbă. Doar când `risk_after` coboară sub un prag față de `risk_before`, planul recomandă `split` — altfel este `marginal` sau `keep_as_is`, iar un candidat descurajat este raportat ca un număr, niciodată desenat ca o formă pe care să fii nevoit să o pui la îndoială cu ochiul.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

Produce trei fișiere lângă `graph.json`:

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

**Acoperirea de limbaje pentru verificarea partajării de stare** (clasificarea bazată doar pe call graph de mai sus funcționează pentru orice limbaj pe care graphify îl extrage; acest tabel se referă specific la re-parsarea sursei care verifică suprapunerea stării `self`/`this`):

| Limbaj | Suportat | Note |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` este un nod AST propriu, nu un acces la câmp împachetat — tratat explicit |
| C# | ✅ | |
| Rust | ✅ | `self.x` prin blocuri `impl` |
| Ruby | ✅ | `@x` (idiomul dominant) + apeluri `self.foo` |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | rezolvarea receiver-ului per metodă — Go nu are cuvânt-cheie `self`/`this`, așa că numele receiver-ului (`f` în `func (f *Foo) M()`) este rezolvat din nou pentru fiecare metodă |
| C | ❌ | un parametru de tip pointer la struct nu are niciun marcaj sintactic care să îl distingă de orice alt parametru — niciun semnal fiabil fără inferență completă de tipuri |

Un nod god într-un limbaj nesuportat, sau unul a cărui sursă nu poate fi citită, este marcat cu `state_analysis: "skipped"` — clasificarea și scorul pe call graph rulează în continuare, dar recomandarea se sprijină doar pe call graph, în loc să presupună tacit că verificarea de stare a trecut.

---

## Ce face

Ce primești direct din cutie:

| Capabilitate | Ce primești |
|---|---|
| **God nodes** | Cele mai conectate concepte, ca să vezi prin ce trece totul |
| **Comunități** | Graful împărțit în subsisteme (Leiden), cu etichete fără LLM |
| **Legături între fișiere** | `calls` / `imports` / `inherits` / `mixes_in` rezolvate în ~40 de limbaje prin AST tree-sitter |
| **Query, path, explain** | Pune o întrebare, urmărește drumul dintre două lucruri sau cere explicarea unui concept, totul pe baza `graph.json` |
| **Motivație + referințe la documente** | Comentariile `# NOTE:` / `# WHY:` și citările ADR/RFC devin noduri de sine stătătoare, legate de cod |
| **Dincolo de cod** | Documentele, PDF-urile, imaginile și video/audio se mapează toate în același graf |
| **Local-first** | Codul este parsat local cu tree-sitter (fără LLM, nimic nu îți părăsește mașina); doar trecerea semantică peste documente/media apelează un backend, și doar dacă îl configurezi |

---

## Benchmark-uri

| Benchmark | Metrică | graphify | Domeniu |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | QA accuracy | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | QA accuracy | **76%** | la egalitate cu dense RAG |
| Construirea grafului | credite LLM | **0** | per token la majoritatea sistemelor |

Fiecare sistem a rulat pe același harness, cu același model și aceleași bugete, punctat de un judge validat orb față de un al doilea judge (90,6% acord, kappa Cohen 0,81). Tabelele complete pe sistem, rezultatul de code intelligence și comenzile de reproducere: **[BENCHMARKS.md](../../BENCHMARKS.md)**.

---

## Cerințe preliminare

| Cerință | Minim | Verificare | Instalare |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(recomandat)* | oricare | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(alternativă)* | oricare | `pipx --version` | `pip install pipx` |

**Instalare rapidă pe macOS (Homebrew):**
```bash
brew install python@3.12 uv
```

**Instalare rapidă pe Windows:**
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

## Instalare

> **Pachetul oficial:** pachetul PyPI este `graphifyy` (cu doi de y). Alte pachete `graphify*` de pe PyPI nu sunt afiliate. Comanda CLI rămâne `graphify`.

**Pasul 1 — instalează pachetul:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**Pasul 2 — înregistrează skill-ul în asistentul tău AI:**

```bash
graphify install
```

Asta e tot. Deschide-ți asistentul AI și scrie `/graphify .`

Pentru a instala skill-ul asistentului în repository-ul curent în loc de profilul
tău de utilizator, adaugă `--project`:

```bash
graphify install --project
graphify install --project --platform codex
```

Instalările la nivel de proiect scriu în directorul curent, de exemplu
`.claude/skills/graphify/SKILL.md` sau `.agents/skills/graphify/SKILL.md` (plus un
sidecar `references/` pe care skill-ul îl încarcă la cerere), și
afișează un indiciu `git add` pentru fișierele care pot fi comise.
Comenzile per platformă care suportă instalări la nivel de proiect acceptă același flag,
de exemplu `graphify claude install --project` sau `graphify codex install --project`.

> **Notă pentru PowerShell:** folosește `graphify .`, nu `/graphify .` — slash-ul de la început este separator de cale în PowerShell.

> **`graphify: command not found`?** `uv tool install` / `pipx install` pun comanda `graphify` în directorul lor bin pentru unelte (`~/.local/bin`). Dacă shell-ul tău nu o găsește imediat după instalare — obișnuit pe un setup proaspăt macOS + zsh — acel director nu este încă în `PATH`: rulează `uv tool update-shell` (sau `pipx ensurepath`), apoi deschide un terminal nou. Cu `pip` simplu, adaugă `~/.local/bin` (Linux) sau `~/Library/Python/3.x/bin` (Mac) în PATH, ori rulează `python -m graphify`.

> **Rulezi cu `uvx` / `uv tool run` în loc să instalezi?** Numește pachetul, nu comanda: `uvx --from graphifyy graphify install`. Un simplu `uvx graphify …` eșuează (`No solution found … no versions of graphify`), pentru că `uv tool run` citește primul cuvânt ca *pachet*, iar pachetul este `graphifyy` — comanda `graphify` se află în interiorul lui.

> **Evită `pip install` pe Mac/Windows** dacă poți. Skill-ul rezolvă Python la runtime din `graphify-out/.graphify_python`; dacă acesta indică un alt mediu decât cel în care `pip` a instalat pachetul, vei primi `ModuleNotFoundError: No module named 'graphify'`. `uv tool install` și `pipx install` izolează pachetul în propriul mediu și evită complet acest lucru.

> **Git hooks și uv tool / pipx:** `graphify hook install` încorporează calea interpretorului curent direct în scripturile de hook la momentul instalării, astfel încât hook-ul post-commit se declanșează corect chiar și în clienți git grafici și în runnere CI unde `~/.local/bin` nu este în PATH. Dacă reinstalezi sau actualizezi graphify, rulează din nou `graphify hook install` pentru a împrospăta calea încorporată.

> **Modul strict (Claude Code):** `graphify install --project --strict` face ca asistentul să folosească efectiv graful. Instalarea implicită doar îl *împinge* să ruleze `graphify query` înainte de a citi fișiere; modul strict *blochează* prima citire de sursă brută dintr-o sesiune și o redirecționează către graf, apoi revine la împingerea blândă (deci se declanșează cel mult o dată pe sesiune și nu rămâne niciodată blocat). Comută la runtime cu `GRAPHIFY_HOOK_STRICT=1`/`0`; instalarea implicită rămâne neschimbată (împingere blândă).

<details>
<summary><b>Alege-ți platforma</b> (20+ asistenți, dă clic pentru a extinde)</summary>

| Platformă | Comandă de instalare |
|----------|----------------|
| Claude Code (Linux/Mac) | `graphify install` |
| Claude Code (Windows) | `graphify install` (detectat automat) sau `graphify install --platform windows` |
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
| Agent Skills (multi-framework) | `graphify install --platform agents` (alias `--platform skills`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify install --platform pi` |
| Cursor | `graphify cursor install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

Utilizatorii Codex au nevoie și de `multi_agent = true` sub `[features]` în `~/.codex/config.toml` pentru extragere paralelă. CodeBuddy folosește același mecanism de tool Agent și hook PreToolUse ca Claude Code. Factory Droid folosește tool-ul `Task` pentru dispecerizarea paralelă a subagenților. OpenClaw și Aider folosesc extragere secvențială (suportul pentru agenți paraleli este încă timpuriu pe acele platforme). Trae folosește tool-ul Agent pentru dispecerizarea paralelă a subagenților și **nu** suportă hook-uri `PreToolUse`, așa că AGENTS.md este mecanismul mereu activ.

`--platform agents` (alias `--platform skills`) țintește locațiile generice, multi-framework [Agent-Skills](https://github.com/anthropics/skills): `~/.agents/skills/` global pe utilizator, conform specificației (citit de `npx skills` și de framework-urile conforme cu specificația) pentru o instalare globală, și `./.agents/skills/` pentru o instalare de proiect (`--project`). Simplul `graphify install` rămâne intenționat pe o singură platformă (Claude Code) — folosește platforma numită `agents` când vrei ca skill-ul să fie descoperibil de orice framework care citește `.agents/skills`.

> Codex folosește `$graphify` în loc de `/graphify`.

</details>

<details>
<summary><b>Extra-uri opționale</b> (instalează doar ce îți trebuie)</summary>

| Extra | Ce adaugă | Instalare |
|---|---|---|
| `pdf` | Extragere din PDF | `uv tool install "graphifyy[pdf]"` |
| `office` | Suport pentru `.docx` și `.xlsx` | `uv tool install "graphifyy[office]"` |
| `google` | Randare Google Sheets | `uv tool install "graphifyy[google]"` |
| `video` | Transcriere video/audio (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | Server MCP stdio | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Suport push către Neo4j | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | Suport push către FalkorDB | `uv tool install "graphifyy[falkordb]"` |
| `svg` | Export graf în SVG | `uv tool install "graphifyy[svg]"` |
| `leiden` | Detecție de comunități Leiden (doar Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Inferență locală Ollama | `uv tool install "graphifyy[ollama]"` |
| `openai` | API-uri OpenAI / compatibile OpenAI | `uv tool install "graphifyy[openai]"` |
| `gemini` | API Google Gemini | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | API Anthropic Claude (`--backend claude`, folosește `ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (folosește IAM, fără cheie API) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, folosește `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "graphifyy[openai]"` |
| `sql` | Extragerea schemei SQL | `uv tool install "graphifyy[sql]"` |
| `postgres` | Introspecție live PostgreSQL (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | Extragere AST BYOND DreamMaker `.dm`/`.dme` (poate necesita un compilator C + `python3-dev` dacă niciun wheel nu se potrivește platformei tale) | `uv tool install "graphifyy[dm]"` |
| `terraform` | Extragere AST Terraform / HCL `.tf`/`.tfvars`/`.hcl` | `uv tool install "graphifyy[terraform]"` |
| `pascal` | Extragere AST Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` (muchii `calls`/`inherits` mai exacte; în lipsa lui se revine la un extractor pe bază de regex) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | Segmentare a interogărilor în chineză (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | Tot ce e mai sus | `uv tool install "graphifyy[all]"` |

</details>

---

## Fă-ți asistentul să folosească mereu graful

Rulează asta o dată în proiectul tău, după ce ai construit un graf:

| Platformă | Comandă |
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
| Agent Skills (multi-framework) | `graphify agents install` (alias `graphify skills install`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify pi install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

Aceasta scrie un mic fișier de configurare care îi spune asistentului tău să consulte graful de cunoștințe pentru întrebări despre codebase, preferând interogări delimitate precum `graphify query "<question>"` în locul citirii raportului complet sau al grep-ului prin fișiere brute.

- **Platforme cu hook** (Claude Code, Gemini CLI): un hook se declanșează automat înaintea apelurilor de tool de tip căutare (și, pe Claude Code, înaintea citirii fișierelor sursă unul câte unul prin tool-urile Read/Glob) și îți împinge asistentul spre calea grafului.
- **Platforme cu fișiere de instrucțiuni** (Codex, OpenCode, Cursor etc.): fișierele de instrucțiuni persistente (`AGENTS.md`, `.cursor/rules/` etc.) oferă aceeași îndrumare de tip query-first.

`GRAPH_REPORT.md` rămâne disponibil pentru o trecere în revistă amplă a arhitecturii.

**CodeBuddy** face aceleași două lucruri ca Claude Code: scrie o secțiune `CODEBUDDY.md` care îi spune lui CodeBuddy să citească `graphify-out/GRAPH_REPORT.md` înainte de a răspunde la întrebări de arhitectură și instalează hook-uri `PreToolUse` (`.codebuddy/settings.json`) care se declanșează înaintea comenzilor Bash de căutare și a citirilor de fișiere, împingând în schimb spre `graphify query`.

**Codex** scrie în `AGENTS.md`, care este ceea ce poartă efectiv îndrumarea mereu activă spre graf pe această platformă. `graphify codex install` înregistrează și un hook `PreToolUse` în `.codex/hooks.json` (`graphify hook-check`), dar acea intrare este intenționat un **no-op**: Codex Desktop respinge `hookSpecificOutput.additionalContext` pe `PreToolUse`, deci emiterea unei împingeri acolo ar strica apelurile tool-ului Bash. Spre deosebire de Claude Code, unde hook-ul (`graphify hook-guard`) face împingerea, pe Codex hook-ul se declanșează și nu face nimic intenționat, iar `AGENTS.md` este mecanismul mereu activ.

**Kilo Code** instalează skill-ul Graphify în `~/.config/kilo/skills/graphify/SKILL.md` și o comandă nativă `/graphify` în `~/.config/kilo/command/graphify.md`. `graphify kilo install` scrie și `AGENTS.md`, plus un plugin nativ `tool.execute.before` (`.kilo/plugins/graphify.js` + înregistrare în `.kilo/kilo.json` sau `.kilo/kilo.jsonc`), astfel încât Kilo primește același comportament mereu activ de reamintire a grafului prin configurația nativă `.kilo`.

**Cursor** scrie `.cursor/rules/graphify.mdc` cu `alwaysApply: true`, deci Cursor îl include automat în fiecare conversație, fără hook.

Pentru a elimina graphify de pe toate platformele dintr-o dată: `graphify uninstall` (adaugă `--purge` ca să ștergi și `graphify-out/`). Sau folosește comanda per platformă (de ex. `graphify claude uninstall`).

---

## Ce conține raportul

- **God nodes** — cele mai conectate concepte din proiectul tău. Totul trece prin ele.
- **Conexiuni surprinzătoare** — legături între lucruri care trăiesc în fișiere sau module diferite. Clasate după cât de neașteptate sunt.
- **„De ce"-ul** — comentariile inline (`# NOTE:`, `# WHY:`, `# HACK:`), docstring-urile și motivația de design din documente sunt extrase ca noduri separate, legate de codul pe care îl explică.
- **Întrebări sugerate** — 4–5 întrebări la care graful este cel mai bine poziționat să răspundă.
- **Etichete de încredere** — fiecare relație dedusă este marcată `EXTRACTED`, `INFERRED` sau `AMBIGUOUS`. Știi mereu ce a fost găsit față de ce a fost ghicit.

---

## Ce fișiere procesează

| Tip | Extensii |
|------|-----------|
| Cod (36 de gramatici tree-sitter) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme` necesită `uv tool install graphifyy[dm]`; `.mts`/`.cts` refolosesc gramatica TypeScript, `.cc`/`.cxx` și CUDA `.cu`/`.cuh` și Metal `.metal` refolosesc gramatica C++) |
| Salesforce Apex | `.cls .trigger` (bazat pe regex; clase, interfețe, enum-uri, metode, triggere, muchii SOQL/DML) |
| Terraform / HCL | `.tf .tfvars .hcl` (necesită `uv tool install graphifyy[terraform]`) |
| Configurații MCP | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — extrage noduri de server, referințe de pachete, cerințe de variabile de mediu |
| Manifeste de pachete | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — un nod canonic de pachet per pachet (după nume) plus muchii `depends_on`, astfel încât un pachet referențiat din multe manifeste este un singur hub |
| Documente | `.md .mdx .qmd .html .txt .rst .yaml .yml` (linkurile markdown `[text](./other.md)` și `[[wikilinks]]` devin muchii `references` între documente) |
| Office | `.docx .xlsx` (necesită `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (opt-in; necesită autentificare `gws` și `--google-workspace`; Sheets necesită `uv tool install graphifyy[google]`) |
| PDF-uri | `.pdf` |
| Imagini | `.png .jpg .webp .gif` |
| Video / Audio | `.mp4 .mov .mp3 .wav` și altele (necesită `uv tool install graphifyy[video]`) |
| YouTube / URL-uri | orice URL video (necesită `uv tool install graphifyy[video]`) |

Codul este extras **local, fără apeluri API** (AST prin tree-sitter). Tot restul trece prin API-ul de model al asistentului tău AI.

Fișierele `.gdoc`, `.gsheet` și `.gslides` din Google Drive for desktop sunt
pointeri de tip shortcut, nu conținut de document. Pentru a include documente
native Google Docs, Sheets și Slides într-o extragere headless, instalează și
autentifică [`gws` CLI](https://github.com/googleworkspace/cli), apoi rulează:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

Poți seta și `GRAPHIFY_GOOGLE_WORKSPACE=1`. Graphify exportă shortcut-urile în
`graphify-out/converted/` ca fișiere sidecar Markdown, apoi extrage acele fișiere.

---

## Comenzi uzuale

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

Vezi [Decouple: candidați Extract Class cu scor de risc](#decouple-candidați-extract-class-cu-scor-de-risc) mai sus, sau [referința completă a comenzilor](#referință-completă-a-comenzilor) mai jos.

---

## Ignorarea fișierelor

Creează un `.graphifyignore` în rădăcina proiectului — aceeași sintaxă ca `.gitignore`, inclusiv negarea cu `!`.

**`.gitignore` este respectat automat.** graphify citește `.gitignore` din fiecare director. Dacă există și un `.graphifyignore`, cele două sunt **combinate** — tiparele din `.graphifyignore` sunt evaluate ultimele, deci câștigă în caz de conflict (inclusiv negările cu `!`). Adăugarea unui `.graphifyignore` doar exclude mai mult; nu reinclude niciodată un fișier pe care `.gitignore` l-a exclus deja. Domeniul de aplicare pe subdirectoare funcționează la fel ca în git — un fișier de ignorare afectează doar propriul subarbore.

Trimite `--no-gitignore` către `graphify extract` atunci când codul generat sau transpilat ignorat de git trebuie totuși să apară în graf. Asta dezactivează `.gitignore` și `.git/info/exclude`; `.graphifyignore` se aplică în continuare.

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

## Configurare pentru echipă

`graphify-out/` este menit să fie comis în git, ca toată lumea din echipă să pornească cu o hartă.

**Adăugiri recomandate la `.gitignore`:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` este acum portabil — cheile sunt stocate ca rute relative și re-ancorate la încărcare, deci comiterea lui este sigură și evită o reconstruire completă la primul checkout.

**Flux de lucru:**
1. O persoană rulează `/graphify .` și comite `graphify-out/`.
2. Toți ceilalți fac pull — asistentul lor citește graful imediat.
3. Rulează `graphify hook install` pentru reconstruire automată după fiecare commit (doar AST, fără costuri API). Asta configurează și un merge driver git, astfel încât `graph.json` să nu rămână niciodată cu marcaje de conflict — doi dezvoltatori care comit în paralel primesc automat grafurile unificate prin union.
4. Când se schimbă documentele sau lucrările, rulează `/graphify --update` pentru a împrospăta acele noduri.

---

## Folosirea directă a grafului

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

Serverul MCP îi dă asistentului tău acces structurat: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Server HTTP partajat

`--transport stdio` (implicit) pornește câte un server local pentru fiecare dezvoltator. `--transport http` servește aceleași tool-uri peste transportul MCP Streamable HTTP, astfel încât un singur proces partajat poate servi graful pentru toată echipa — clienții își îndreaptă configurația MCP din IDE spre `http://<host>:8080/mcp` în loc să ruleze graphify local.

| Flag | Implicit | Scop |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Transportul pe care se servește |
| `--host` | `127.0.0.1` | Host-ul de bind HTTP (folosește `0.0.0.0` pentru expunere dincolo de localhost) |
| `--port` | `8080` | Portul de bind HTTP |
| `--api-key` | env `GRAPHIFY_API_KEY` | Cere `Authorization: Bearer <key>` (sau `X-API-Key`) |
| `--path` | `/mcp` | Calea de montare HTTP |
| `--json-response` | dezactivat | Returnează JSON simplu în loc de fluxuri SSE |
| `--stateless` | dezactivat | Fără stare per sesiune (pentru deployment-uri cu load balancing / CI) |
| `--session-timeout` | `3600` | Curăță sesiunile inactive cu stare după N secunde (`0` dezactivează) |

Bind-ul implicit `127.0.0.1` este doar loopback. Setează `--host 0.0.0.0` **și** `--api-key` împreună când îl expui pe un host partajat. Rulează-l într-un container:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **Notă WSL / Linux:** Ubuntu livrează `python3`, nu `python`. Folosește un venv ca să eviți conflictele:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## Variabile de mediu

Acestea sunt necesare doar pentru **extragerea headless / în CI** (`graphify extract`). Când rulezi prin skill-ul `/graphify` în IDE-ul tău, API-ul de model este furnizat de sesiunea IDE — nu sunt necesare chei suplimentare.

| Variabilă | Folosită pentru | Când este necesară |
|---|---|---|
| `ANTHROPIC_API_KEY` | Backend Claude (Anthropic) | `--backend claude` |
| `ANTHROPIC_BASE_URL` | URL de endpoint compatibil Anthropic (proxy LiteLLM, gateway-uri, ...) | `--backend claude` (implicit: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Numele modelului pentru backend-ul Claude — pentru endpoint-uri proprii, folosește numele/aliasul de model expus de serverul tău | `--backend claude` (implicit: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` sau `GOOGLE_API_KEY` | Backend Google Gemini | `--backend gemini` |
| `OPENAI_API_KEY` | API-uri OpenAI sau compatibile OpenAI | `--backend openai` (serverele locale acceptă orice valoare nevidă) |
| `OPENAI_BASE_URL` | URL de server compatibil OpenAI (llama.cpp, vLLM, LM Studio, ...) | `--backend openai` (implicit: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | Numele modelului pentru backend-ul OpenAI — pentru servere self-hosted, folosește numele/aliasul de model expus de serverul tău (verifică endpoint-ul `/v1/models`), de ex. `LFM2.5-8B-A1B-UD-Q4_K_XL` pentru llama.cpp | `--backend openai` (implicit: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | Backend DeepSeek | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Backend Kimi Code | `--backend kimi` |
| `OLLAMA_BASE_URL` | URL pentru inferență locală Ollama | `--backend ollama` (implicit: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Numele modelului Ollama | `--backend ollama` (implicit: detectare automată) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Suprascrie dimensiunea ferestrei de KV-cache Ollama | opțional — dimensionată automat implicit |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Minute cât rămâne încărcat modelul Ollama | opțional — setează `0` pentru descărcare după fiecare chunk |
| `AZURE_OPENAI_API_KEY` | Backend Azure OpenAI Service | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | URL-ul endpoint-ului resursei Azure | `--backend azure` (necesar alături de cheia API) |
| `AZURE_OPENAI_API_VERSION` | Suprascrie versiunea API Azure | opțional — implicit `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` sau `GRAPHIFY_AZURE_MODEL` | Numele deployment-ului Azure | opțional — implicit `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — lanțul standard de credențiale | `--backend bedrock` (fără cheie API, folosește IAM) |
| `GRAPHIFY_MAX_WORKERS` | Numărul de fire pentru paralelismul AST | opțional — și ca flag `--max-workers` |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Ridică plafonul de output pentru corpusuri dense | opțional — de ex. `32768` pentru fișiere mari |
| `GRAPHIFY_API_TIMEOUT` | Timeout per apel, în secunde, pentru backend-urile HTTP, claude-cli, Anthropic SDK și Bedrock (implicit: 600) | opțional — și ca flag `--api-timeout` |
| `GRAPHIFY_MAX_RETRIES` | De câte ori se reîncearcă o cerere limitată de rată (429) înainte de a renunța (implicit: 6; respectă `Retry-After`) | opțional — crește-l pentru limite stricte pe organizație (de ex. kimi); `0` dezactivează |
| `GRAPHIFY_FORCE` | Forțează reconstruirea grafului chiar și cu mai puține noduri | opțional — și ca flag `--force` |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Activează automat exportul Google Workspace | opțional — setează la `1` |
| `GRAPHIFY_TRIAGE_BACKEND` | Backend pentru `graphify prs --triage` | opțional — detectat automat din cheile disponibile |
| `GRAPHIFY_TRIAGE_MODEL` | Suprascriere de model pentru triaj | opțional — de ex. `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | Setează la `1` pentru a activa jurnalul local de interogări la `~/.cache/graphify-queries.log` (înregistrează fiecare întrebare query/path/explain + calea corpusului). Dezactivat implicit — nu se scrie nimic dacă nu optezi (#1797) | opțional |
| `GRAPHIFY_QUERY_LOG` | Activează jurnalul de interogări și îl scrie la această cale în loc de cea implicită | opțional — dezactivat dacă nu este setat acesta sau `_ENABLE` |
| `GRAPHIFY_QUERY_LOG_DISABLE` | Setează la `1` pentru a forța dezactivarea jurnalului de interogări (are prioritate față de variabilele de activare) | opțional |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | Când jurnalul este activ, înregistrează și răspunsurile complete de subgraf (dezactivat implicit) | opțional |
| `GRAPHIFY_MAX_GRAPH_BYTES` | Suprascrie plafonul de 512 MiB pentru dimensiunea graph.json — de ex. `700MB`, `2GB` sau octeți simpli | opțional — util pentru corpusuri foarte mari |
| `GRAPHIFY_MAX_CONTEXTS` | Numărul maxim de grafuri de proiect non-implicite reținute de un server MCP multi-proiect | opțional — implicit: `8`; valorile invalide folosesc `8`, iar cele sub `1` folosesc `1` |
| `GRAPHIFY_LLM_TEMPERATURE` | Suprascrie temperatura LLM pentru extragerea semantică — de ex. `0.7`, sau `none` pentru omitere | opțional — omisă automat pentru modelele de raționament o1/o3/o4/gpt-5 |

---

## Confidențialitate

- **Fișiere de cod** — procesate local prin tree-sitter. Nimic nu îți părăsește mașina. Un corpus format doar din cod nu are nevoie de cheie API — `graphify extract` rulează complet offline. Pe un repo mixt, adaugă `--code-only` ca să indexezi doar codul și să sari peste documentele/PDF-urile/imaginile care altfel ar necesita un LLM.
- **Video / audio** — transcris local cu faster-whisper. Nimic nu îți părăsește mașina.
- **Documente, PDF-uri, imagini** — trimise asistentului tău AI pentru extragere semantică (prin skill-ul `/graphify`, folosind modelul pe care îl rulează sesiunea ta de IDE). `graphify extract` headless necesită `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), o instanță Ollama pornită (`OLLAMA_BASE_URL`), credențiale AWS prin lanțul standard de provideri (Bedrock — fără cheie API, folosește IAM), sau binarul CLI `claude` (Claude Code — fără cheie API, folosește abonamentul tău Claude). Flag-ul `--dedup-llm` folosește aceeași cheie.
- **Rezidența datelor** — `graphify extract` detectează automat ce provider să folosească, în funcție de cheia API setată (prioritate: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). Pentru cod cu cerințe de rezidență a datelor, folosește `--backend ollama` (complet local) sau trimite un flag `--backend` explicit. Kimi (`MOONSHOT_API_KEY`) rutează către serverele Moonshot AI din China.
- **Fără telemetrie**, fără urmărirea utilizării, fără analytics.
- **Jurnalizarea interogărilor** — fiecare apel `graphify query`, `graphify path`, `graphify explain` și MCP `query_graph` este jurnalizat în `~/.cache/graphify-queries.log` în format JSON Lines (timestamp, întrebare, corpus, noduri returnate, durată). Răspunsurile complete de subgraf **nu** sunt stocate implicit. Setează `GRAPHIFY_QUERY_LOG_DISABLE=1` pentru a renunța, sau `GRAPHIFY_QUERY_LOG=/dev/null` pentru a-l reduce la tăcere fără a dezactiva calea de cod.

---

## Limitări și granițe

Ce anume nu face graphify în mod deliberat, și unde se oprește acoperirea sa:

- **Nu este un motor de căutare semantică/vectorială.** Graful este structural — noduri și muchii tipizate, rezolvate din sursă, nu embedding-uri. `graphify query`/`path`/`explain` parcurg această structură; nu pot scoate la iveală o conexiune care nu este reprezentată ca muchie, chiar dacă este „semantic" înrudită. Nu există o alternativă de similaritate/celui-mai-apropiat-vecin.
- **Documentele, PDF-urile, imaginile și extragerea headless de video/URL-uri nu sunt exclusiv locale.** Doar codul (AST tree-sitter) și transcrierea audio/video (faster-whisper) rulează complet offline. Extragerea documentelor/PDF-urilor/imaginilor apelează întotdeauna un LLM — modelul asistentului tău AI prin skill-ul `/graphify`, sau o cheie API de backend configurată pentru `graphify extract` headless. Vezi [Confidențialitate](#confidențialitate) mai sus pentru a afla exact de ce flag sau cheie are nevoie fiecare cale.
- **Verificarea de partajare a stării din decouple nu acoperă toate limbajele.** C nu are niciun semnal fiabil de `self`/`this` fără inferență completă de tipuri, deci este exclus (vezi [tabelul de acoperire a limbajelor](#decouple-candidați-extract-class-cu-scor-de-risc) de mai sus). Un nod god într-un limbaj nesuportat, sau a cărui sursă nu poate fi citită, revine la o scorare bazată doar pe call graph (`state_analysis: "skipped"`) în loc de o verificare de stare confirmată.
- **Pragul de flux de date 3D este o euristică de nume, nu o analiză de flux de date/taint.** Detecția limitelor I/O din `data_floor` (parsere, loadere, cititori, scriitori, clienți DB/HTTP) se potrivește pe baza convențiilor de denumire (`boundary_reason`); un nod de limită cu un nume neconvențional poate fi ratat, subestimând cât de adânc se află restul grafului.
- **Etichetele de încredere reprezintă încrederea proprie de rezolvare a graphify, nu adevărul absolut.** Muchiile `INFERRED` și `AMBIGUOUS` sunt rezolvări de tip best-effort și pot fi în continuare greșite, mai ales pentru idiomuri foarte dinamice (reflection, dispatch la runtime, metaprogramare) pe care nicio trecere statică AST nu le poate rezolva complet.
- **Vizualizarea HTML și dimensiunea grafului au amândouă un plafon.** `graph.html` / `DECOUPLE.html` sar peste generare peste 5.000 de noduri, implicit (`MAX_NODES_FOR_VIZ`, crescut prin `GRAPHIFY_VIZ_NODE_LIMIT`); `graph.json` însuși este plafonat la 512 MiB (`GRAPHIFY_MAX_GRAPH_BYTES` pentru a suprascrie). Folosește `--no-viz` plus `query`/`path`/`explain` pentru corpusuri care depășesc oricare dintre limite.
- **Conștientizarea între proiecte este opt-in, nu automată.** `graphify query` vede doar graful unic către care îl îndrepți. Întrebările pe mai multe repo-uri necesită înregistrarea explicită a fiecărui proiect în graful partajat, mai întâi (`graphify global add`, plafonat la `GRAPHIFY_MAX_CONTEXTS` contexte non-implicite per server MCP) — graphify nu îți scanează niciodată singur mașina în căutarea altor repo-uri.
- **Extragerea paralelă cu mai mulți agenți depinde de platformă.** Are nevoie de suport din partea asistentului pentru lansarea de subagenți (`multi_agent = true` în `~/.codex/config.toml` pentru Codex, tool-ul Agent/Task pe Claude Code/CodeBuddy/Factory Droid/Trae). OpenClaw și Aider extrag momentan doar secvențial.
- **Serverul MCP HTTP partajat se leagă implicit doar de loopback.** Accesarea lui de pe altă mașină necesită explicit `--host 0.0.0.0` **și** `--api-key`; graphify nu gestionează TLS sau vreo altă autentificare dincolo de acel unic token de tip bearer.
- **PowerShell interpretează un `/` de la început ca separator de cale.** `/graphify .` eșuează din acest motiv în Windows PowerShell, nu dintr-o eroare de graphify — folosește în schimb `graphify .`.

---

## Depanare

**`graphify: command not found` după instalare**
CLI-ul este instalat, dar directorul lui bin nu se află în `PATH`-ul shell-ului tău. Alege soluția potrivită modului în care ai instalat:
- **uv** (`uv tool install graphifyy`): comanda ajunge în directorul bin pentru unelte al uv (`~/.local/bin`), care pe un setup proaspăt macOS/zsh adesea nu este în `PATH`. Rulează `uv tool update-shell`, apoi deschide un terminal nou. (Găsești directorul cu `uv tool dir --bin`.)
- **pipx** (`pipx install graphifyy`): rulează `pipx ensurepath`, apoi deschide un terminal nou.
- **pip** (`pip install graphifyy`): pip instalează scripturile într-un director bin de utilizator care s-ar putea să nu fie în `PATH` — adaugă `~/Library/Python/3.x/bin` (macOS) sau `~/.local/bin` (Linux) în `PATH`-ul din `~/.zshrc`/`~/.bashrc`, ori pur și simplu rulează `python -m graphify`.

**`uvx graphify …` sau `uv tool run graphify …` nu reușește să rezolve `graphify`**
Pachetul PyPI este `graphifyy`; `graphify` este doar comanda pe care o oferă. `uv tool run` tratează primul cuvânt ca *nume de pachet*, deci caută un pachet numit `graphify` și raportează `No solution found … no versions of graphify`. Numește pachetul explicit: `uvx --from graphifyy graphify install` (echivalent cu `uv tool run --from graphifyy graphify install`). Sau rulează `uv tool install graphifyy` o dată și apoi apelează direct `graphify`.

**`uv run --with graphifyy python -m graphify` rulează în tăcere o instalare mai veche**
`uv run` folosește Python-ul tău de *sistem*, deci dacă acolo trăiește și un `graphifyy` mai vechi (de ex. de la un `pip install graphifyy` anterior), Python poate găsi întâi acea copie în `sys.path`, iar `--with graphifyy` nu o va suprascrie. Rulează fără eroare, dar obții comportamentul versiunii *vechi* — de exemplu, suprascrierile de mediu precum `OPENAI_BASE_URL` sunt ignorate în tăcere, deci cererile ajung la endpoint-ul implicit și eșuează cu un 401 care arată ca o cheie greșită. Semnătura este o linie `warning: skill is from graphify <newer>, package is <older>` — asta înseamnă că s-a încărcat o altă instalare, nu doar un skill învechit. Verifică ce copie s-a încărcat efectiv:
```bash
python -c "import graphify; print(graphify.__file__)"
```
Apoi rulează direct comanda instalată (ea folosește copia gestionată de uv), sau elimină copia de sistem învechită:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` funcționează, dar comanda `graphify` nu**
`PATH`-ul shell-ului tău nu include directorul bin în care a fost instalată comanda. Preferă `uv tool install` / `pipx install` în locul lui `pip` simplu, apoi rulează `uv tool update-shell` / `pipx ensurepath` și deschide un terminal nou (vezi notele de instalare de mai sus).

**`/graphify .` provoacă „path not recognized" în PowerShell**
PowerShell tratează un `/` de la început ca separator de cale. Folosește `graphify .` (fără slash) pe Windows.

**Graful are mai puține noduri după `--update` sau după reconstruire**
Dacă un refactoring a șters fișiere, nodurile vechi rămân. Trimite `--force` (sau setează `GRAPHIFY_FORCE=1`) ca să suprascrii chiar și când reconstruirea are mai puține noduri.

**`extract` iese cu „extraction was incomplete ... refusing to overwrite"**
Când o trecere de extragere se blochează sau o parcurgere nu poate citi complet corpusul, rularea ar fi mai mică decât una completă, așa că `graphify extract` refuză să suprascrie un graf existent mai mare cu rezultatul parțial (protejându-ți `graph.json`). Rezolvă cauza de bază și rulează din nou, sau trimite `--allow-partial` ca să suprascrii oricum.

**Graful are noduri duplicate pentru aceeași entitate (duplicate fantomă)**
Duplicatele fantomă (același simbol apărând de două ori — o dată din extragerea AST, cu locație în sursă, o dată din extragerea semantică, fără) sunt acum unite automat la momentul construirii. Dacă vezi asta într-un graf construit înainte de v0.8.33, rulează o re-extragere completă pentru curățare:
```bash
graphify extract . --force
```

**Ollama rămâne fără VRAM / fereastra de context este depășită**
Fereastra de KV-cache este dimensionată automat, dar poate fi prea mare pentru GPU-ul tău. Redu-o:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**Avertismente `LLM returned invalid JSON` / `Unterminated string`**
Răspunsul JSON al modelului a atins limita de token-uri de output și a fost tăiat la mijlocul unui string. graphify se recuperează automat (împarte chunk-ul și re-extrage jumătățile, iar un document unic supradimensionat este mai întâi tăiat la limite de titlu/paragraf, deci fișierul întreg rămâne acoperit), așa că aceste avertismente sunt zgomotoase, dar nu înseamnă pierdere de date. Ca să reduci agitația, ridică plafonul de output sau micșorează output-ul fiecărui chunk:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
Cu un gateway cloud precum OpenRouter, preferă `--backend openai` (setează `OPENAI_BASE_URL`) în locul shim-ului Ollama — este o cale compatibilă OpenAI mai curată. Dacă modelul are propriul plafon de output maxim, scăderea lui `--token-budget` este pârghia sigură.

**HTML-ul grafului este prea mare pentru a fi deschis într-un browser (>5000 de noduri)**
Sari peste generarea HTML și folosește direct JSON-ul:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**`graph.json` are marcaje de conflict după ce doi dezvoltatori comit în același timp**
Rulează `graphify hook install` — configurează un merge driver git care unifică `graph.json` prin union automat, astfel încât conflictele nu apar niciodată.

**Extragerea returnează noduri/muchii goale pentru documente sau PDF-uri**
Documentele, PDF-urile și imaginile necesită un apel LLM — corpusurile doar cu cod nu au nevoie de cheie. Verifică dacă cheia API este setată și backend-ul este corect:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**Avertisment de nepotrivire a versiunii skill-ului în IDE-ul tău**
Versiunea de graphify instalată diferă de fișierul de skill. Actualizează:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**Cache-ul de prompt din Claude Code este invalidat după fiecare `graphify extract`**
Graphify scrie fișiere de output (`graph.json`, `graphify-out/`) în workspace. Dacă acele căi nu sunt ignorate, fiecare scriere invalidează cache-ul de prompt al Claude Code, forțând un re-upload complet la tarife de cache-write la tura următoare. Adaugă-le în `.claudeignore`:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## Referință completă a comenzilor

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

> **Numele comunităților:** în interiorul unui agent (Claude Code, Gemini CLI), agentul denumește el însuși comunitățile. Când rulezi CLI-ul simplu, `cluster-only` le denumește automat cu backend-ul configurat (integrat sau un provider propriu compatibil OpenAI) — trimite `--no-label` ca să păstrezi `Community N`, sau rulează `graphify label` ca să (re)generezi numele la cerere.

---

## Află mai multe

- [Cum funcționează](../how-it-works.md) — pipeline-ul de extragere, detecția de comunități, scorul de încredere, benchmark-urile
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — împărțirea pe module, cum să adaugi o limbă
- [Integrări opționale](../docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — cartea despre ideile din spatele graphify, arhitectura de la un cap la altul

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) este stratul mereu activ construit peste graphify — aplică aceeași abordare bazată pe graf întregului tău context de lucru: ședințe, fișiere, documente și cod, actualizându-se continuu în fundal.

Construit pentru oameni și echipe a căror muncă se întinde peste sute de conversații și documente pe care nu le pot reconstitui niciodată complet.

**[Înscrie-te pe lista de așteptare la graphify.com](https://graphify.com).** Perioada de probă gratuită se lansează în curând.

---

<details>
<summary>Contribuții</summary>

### Configurarea mediului de dezvoltare

Proiectul folosește [uv](https://docs.astral.sh/uv/) pentru fluxul de dezvoltare. Instalează-l o dată, apoi:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

Verifică instalarea editabilă:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### Rularea testelor

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> Notă pentru macOS: suita de teste include atât fixture-ul `sample.f90`, cât și `sample.F90`. Acestea se ciocnesc pe sisteme de fișiere HFS+ / APFS insensibile la majuscule. Rulează pe Linux sau într-un container Docker dacă trebuie să testezi ambele variante Fortran simultan.

### Fluxul git

- Dezvoltarea activă are loc pe branch-ul `v8`.
- Stilul de commit: `fix: <description>` / `feat: <description>` / `docs: <description>`
- Înainte de a deschide un PR, rulează `uv run pytest tests/ -q` și confirmă că trece.
- Adaugă un fișier fixture în `tests/fixtures/` și teste în `tests/test_languages.py` pentru orice extractor de limbaj nou.

### Ce poți contribui

**Exemplele lucrate** sunt cea mai utilă contribuție. Rulează `/graphify` pe un corpus real, salvează ieșirea în `worked/{slug}/`, scrie un `review.md` onest despre ce a nimerit și ce a greșit graful, și deschide un PR.

**Erori de extragere** — deschide un issue cu fișierul de intrare, intrarea din cache (`graphify-out/cache/`) și ce a fost omis sau greșit.

Vezi [ARCHITECTURE.md](../../ARCHITECTURE.md) pentru responsabilitățile modulelor și cum să adaugi o limbă.

</details>
