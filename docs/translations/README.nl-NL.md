<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>Een fork van <a href="https://github.com/Graphify-Labs/graphify">graphify</a> die <code>graphify decouple</code> toevoegt</b> — 0-LLM, risicogescoorde Extract-Class-kandidaten voor god-objecten, opnieuw geverifieerd tegen de daadwerkelijke broncode (niet alleen de aanroepgraaf) voordat er iets wordt aanbevolen. Zie <a href="#decouple-risicogescoorde-extract-class-kandidaten">Decouple: risicogescoorde Extract-Class-kandidaten</a> hieronder.
</p>

<div align="center">
<details><summary><b>Lees dit in andere talen</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>Vroegtijdige toegang tot het graphify-platform is open vóór de publieke v1-lancering: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

Typ `/graphify` in je AI-codeassistent en het brengt je hele project (code, documenten, PDF's, afbeeldingen, video's) in kaart als een **kennisgraaf** die je kunt **bevragen in plaats van er doorheen te grepen**.

- **Codekaarten gratis en volledig lokaal.** Code wordt geparsed met tree-sitter AST: deterministisch, geen LLM, niets verlaat je machine. (Documenten, PDF's, afbeeldingen en video gebruiken het model van je assistent, of een geconfigureerde API-sleutel, voor een semantische pass.)
- **Elke edge wordt verklaard.** Elke verbinding is gelabeld als `EXTRACTED` (expliciet in de bron) of `INFERRED` (afgeleid door graphify), zodat je kunt zien wat direct is uitgelezen versus wat is afgeleid.
- **Geen vectorindex.** Geen embeddings, geen vectorstore: een echte graaf die je doorloopt. Stel een vraag, volg het pad tussen twee dingen, of laat één concept uitleggen.

> Wil je dit altijd actief hebben, continu bijgewerkt op de achtergrond over je code, documenten en meetings heen, in plaats van alleen op aanvraag? Dat is wat we bouwen bij **[graphify.com](https://graphify.com)**, en vroegtijdige toegang is nu open op **[app.graphify.com](https://app.graphify.com/login)**.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="graphify's interactieve graph.html met de FastAPI-codebase als force-directed kennisgraaf met een legenda van gedetecteerde gemeenschappen" width="900">
</p>
<p align="center">
  <em>De FastAPI-codebase in kaart gebracht door graphify. Elk knooppunt is een concept, kleuren zijn gedetecteerde gemeenschappen, en het geheel is klikbaar in graph.html.</em>
</p>

**Aan de slag** (30 seconden):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

Vervolgens, in je AI-assistent:

```
/graphify .
```

Dat is het. Je krijgt **drie bestanden**:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**Werkt in** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot en 15+ andere — [kies je platform](#installatie).

---

## Zie het in actie

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="graphify path-query: een terminal vraagt om het kortste pad tussen FastAPI en ModelField, en het antwoord licht sprong voor sprong op door de kennisgraaf" width="900">
</p>

Zodra de graaf is gebouwd, bevraag je hem in plaats van bestanden te lezen. Echte output, graphify uitgevoerd op de hierboven getoonde FastAPI-codebase:

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

Elke edge draagt een **betrouwbaarheidslabel** (`EXTRACTED` = expliciet in de bron, `INFERRED` = afgeleid door resolutie), zodat je kunt zien wat direct is uitgelezen versus wat is afgeleid. `graphify query "<vraag>"` geeft een afgebakende subgraaf terug voor een vraag in gewone taal, en `graphify path A B` volgt hoe twee dingen met elkaar verbonden zijn.

---

## Decouple: risicogescoorde Extract-Class-kandidaten

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: MainWindow god-knooppunt splitst zich in risicogescoorde kandidaatklassen, met een gedeelde-state-waarschuwing tussen twee daarvan" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: de 5 voorgestelde klassen van MainWindow, Node Info-paneel geopend op Main Window Axis and Range Controls, met een state-overlap van 0,608 met Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>DECOUPLE.html bij een echte run — klik op een voorgestelde klasse en zie precies met welke andere klasse hij state deelt, en wat er specifiek wordt gedeeld.</em>
</p>

Dezelfde pagina rendert ook de splitsing zelf. Met **Preview decoupled view** wissel je de eigen methodes van de god class in voor de voorgestelde klassen en worden de edges ter plekke opnieuw gerouteerd — de bedradingswijziging, niet een opnieuw getekend diagram:

| Voor — de god class vandaag | Na — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html vóór de toggle: één MainWindow-hubknoop met zijn eigen methodes eromheen uitgewaaierd" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html na de toggle: dezelfde knoop teruggebracht tot 5 ruitvormige voorgestelde klassen, groen gestippelde edges die tonen welke methodes in welke klasse zijn geëxtraheerd, rode edges die de gedeelde instance state tussen twee ervan tonen" width="440"> |
| Eén knoop met 47 eigen methodes, die stuk voor stuk alleen via de klasse bereikbaar zijn. | De voorgestelde klassen. Groen gestippeld = wat er in elke klasse is geëxtraheerd; rood = de instance state die twee ervan nog steeds delen, precies wat de keuze tussen `split` en `keep_as_is` bepaalt. Alleen kandidaten die de risicodrempel halen worden getekend — hier 5 van 6, en daarom heeft één methode geen ruit om op te landen. |

`graphify decouple` vindt god-objecten en vertelt je of ze splitsen daadwerkelijk de moeite waard is — niet alleen dát ze groot zijn.

Het faalscenario waar dit voor bedoeld is om op te vangen: een klasse met 47 methoden die aanroepgraaf-clustering vrolijk opsplitst in 5 nette groepen, die allemaal onderliggend nog steeds dezelfde `self._chart_style` / `self._crosshair`-instantiestate lezen en schrijven. Verscheep die split en je hebt niets ontkoppeld — je hebt methoden verplaatst naar nieuwe bestanden die nog steeds niet los van elkaar getest, gewijzigd of doordacht kunnen worden, omdat ze allemaal nog dezelfde gedeelde state terug moeten krijgen. Een tool die alleen naar de aanroepgraaf kijkt, kan dit helemaal niet zien; hij moet terug naar de daadwerkelijke broncode.

**Twee controles, allebei 0-LLM, allebei deterministisch:**

1. **Is dit überhaupt een God Object?** Een knooppunt met een hoge graad kan een echt God Object zijn (veel van zijn EIGEN methoden, verspreid over ongerelateerde verantwoordelijkheden — Extract Class is van toepassing) of een overmatig gerefereerde hub/datamodel (weinig eigen methoden, vooral *inkomende* verwijzingen — het splitsen van zijn body doet niets; de oplossing is het versmallen van zijn interface, niet het extraheren van een klasse). `classify_god_node` maakt dit onderscheid op basis van `member_ratio`, niet de ruwe graad — het verschil dat voorkomt dat `TraceSource` (84 edges, maar slechts 6 eigen methoden) een onterechte splitsuggestie krijgt die `MainWindow` (88 edges, 47 eigen methoden) terecht wél krijgt.
2. **Zou de split de koppeling daadwerkelijk verminderen?** `risk_before` (de huidige omvang/koppeling/fragmentatie van het god-knooppunt) wordt vergeleken met `risk_after` — het NIEUWE risico dat de split zelf zou introduceren: cross-groep-aanroepen die onzichtbare intra-klasse-edges waren en expliciete inter-klasse-afhankelijkheden worden, callers die nu van meer dan één nieuwe klasse afhankelijk zouden moeten zijn, en — de controle die een aanroepgraaf structureel niet kan uitvoeren — hoeveel `self`/`this`-instantiestate (lezen, schrijven en gedeelde helper-methode-aanroepen, apart gewogen: een gedeelde **schrijfactie** weegt zwaarder dan een gedeelde leesactie) de voorgestelde groepen daadwerkelijk gemeen hebben. Dit parset het eigen bronbestand van het god-knooppunt rechtstreeks opnieuw met tree-sitter; het steunt niet op de eigen geëxtraheerde graaf van graphify, die voor geen enkele taal veldniveau-toegang vastlegt. Alleen wanneer `risk_after` onder een drempel ten opzichte van `risk_before` uitkomt, beveelt het plan `split` aan — anders is het `marginal` of `keep_as_is`, en een afgeraden kandidaat wordt gerapporteerd als een getal, nooit getekend als een vorm die je met het blote oog moet beoordelen.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

Levert drie bestanden op naast `graph.json`:

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

**Taaldekking voor de state-sharing-controle** (de bovenstaande classificatie op basis van alleen de aanroepgraaf werkt voor elke taal die graphify extraheert; deze tabel gaat specifiek over de opnieuw geparste bron die `self`/`this`-state-overlap verifieert):

| Language | Supported | Notes |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` is een eigen AST-knooppunt, geen ingepakte veldtoegang — wordt expliciet afgehandeld |
| C# | ✅ | |
| Rust | ✅ | `self.x` via `impl`-blokken |
| Ruby | ✅ | `@x` (het dominante idioom) + `self.foo`-aanroepen |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | resolutie per methode-ontvanger — Go heeft geen `self`/`this`-sleutelwoord, dus de naam van de ontvanger (`f` in `func (f *Foo) M()`) wordt voor elke methode opnieuw bepaald |
| C | ❌ | een struct-pointerparameter heeft geen syntactische markering die hem onderscheidt van elke andere parameter — geen betrouwbaar signaal zonder volledige type-inferentie |

Een god-knooppunt in een niet-ondersteunde taal, of waarvan de bron niet gelezen kan worden, wordt gemarkeerd als `state_analysis: "skipped"` — de classificatie en de aanroepgraaf-score draaien nog steeds, maar de aanbeveling rust dan alleen op de aanroepgraaf in plaats van stilzwijgend aan te nemen dat de state-controle geslaagd is.

---

## Wat het doet

Wat je standaard krijgt:

| Capability | What you get |
|---|---|
| **Godknooppunten** | De meest verbonden concepten, zodat je ziet waar alles doorheen loopt |
| **Gemeenschappen** | De graaf opgesplitst in subsystemen (Leiden), met LLM-vrije labels |
| **Cross-file-koppelingen** | `calls` / `imports` / `inherits` / `mixes_in` herkend over ~40 talen via tree-sitter AST |
| **Query, path, explain** | Stel een vraag, volg het pad tussen twee dingen, of laat één concept uitleggen — allemaal tegen `graph.json` |
| **Rationale + documentverwijzingen** | `# NOTE:` / `# WHY:`-commentaar en ADR/RFC-verwijzingen worden eersteklas knooppunten die aan de code zijn gekoppeld |
| **Meer dan code** | Documenten, PDF's, afbeeldingen en video/audio worden allemaal in dezelfde graaf afgebeeld |
| **Lokaal-eerst** | Code wordt lokaal geparsed met tree-sitter (geen LLM, niets verlaat je machine); alleen de semantische pass over documenten/media roept een backend aan, en alleen als je er een configureert |

---

## Benchmarks

| Benchmark | Metriek | graphify | Veld |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | QA accuracy | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | QA accuracy | **76%** | gelijkstaand aan dense RAG |
| Graph build | LLM credits | **0** | per token voor de meeste systemen |

Elk systeem draaide op dezelfde testopstelling met hetzelfde model en dezelfde budgetten, beoordeeld door een blind gevalideerde jury tegen een tweede jury (90,6% overeenstemming, Cohen's kappa 0,81). Volledige per-systeem-tabellen, het resultaat voor code-intelligentie, en reproductiecommando's: **[BENCHMARKS.md](../../BENCHMARKS.md)**.

---

## Vereisten

| Requirement | Minimum | Check | Install |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(aanbevolen)* | elke versie | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(alternatief)* | elke versie | `pipx --version` | `pip install pipx` |

**Snelle installatie voor macOS (Homebrew):**
```bash
brew install python@3.12 uv
```

**Snelle installatie voor Windows:**
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

## Installatie

> **Officieel pakket:** Het PyPI-pakket is `graphifyy` (dubbele y). Andere `graphify*`-pakketten op PyPI zijn niet gelieerd. Het CLI-commando blijft `graphify`.

**Stap 1 — installeer het pakket:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**Stap 2 — registreer de vaardigheid bij je AI-assistent:**

```bash
graphify install
```

Dat is alles. Open je AI-assistent en typ `/graphify .`

Om de assistent-vaardigheid in de huidige repository te installeren in plaats van in je gebruikersprofiel, voeg je `--project` toe:

```bash
graphify install --project
graphify install --project --platform codex
```

Project-scoped installaties schrijven onder de huidige map, bijvoorbeeld
`.claude/skills/graphify/SKILL.md` of `.agents/skills/graphify/SKILL.md` (plus een
`references/`-sidecar die de vaardigheid on demand laadt), en
tonen een `git add`-hint voor bestanden die gecommit kunnen worden.
Per-platform-commando's die project-scoped installaties ondersteunen, accepteren dezelfde vlag,
bijvoorbeeld `graphify claude install --project` of `graphify codex install --project`.

> **PowerShell-opmerking:** Gebruik `graphify .` niet `/graphify .` — het leidende schuine streepje is een padscheidingsteken in PowerShell.

> **`graphify: command not found`?** `uv tool install` / `pipx install` plaatsen het `graphify`-commando in hun tool-bin-map (`~/.local/bin`). Als je shell het commando er direct na installatie niet kan vinden — gebruikelijk bij een verse macOS + zsh-opzet — staat die map nog niet op je `PATH`: draai `uv tool update-shell` (of `pipx ensurepath`), en open dan een nieuwe terminal. Voeg bij gewone `pip` `~/.local/bin` (Linux) of `~/Library/Python/3.x/bin` (Mac) toe aan je PATH, of draai `python -m graphify`.

> **Draai je met `uvx` / `uv tool run` in plaats van te installeren?** Noem het pakket, niet het commando: `uvx --from graphifyy graphify install`. Gewoon `uvx graphify …` mislukt (`No solution found … no versions of graphify`) omdat `uv tool run` het eerste woord als een *pakket* leest, en het pakket is `graphifyy` — het `graphify`-commando zit erin.

> **Vermijd `pip install` op Mac/Windows** indien mogelijk. De vaardigheid herleidt Python tijdens runtime vanuit `graphify-out/.graphify_python`; als dat naar een andere omgeving wijst dan waar `pip` het pakket heeft geïnstalleerd, krijg je `ModuleNotFoundError: No module named 'graphify'`. `uv tool install` en `pipx install` isoleren het pakket in hun eigen omgeving en vermijden dit volledig.

> **Git-hooks en uv tool / pipx:** `graphify hook install` bakt het pad van de huidige interpreter direct in de hookscripts in tijdens installatie, zodat de post-commit-hook correct afgaat, zelfs in grafische git-clients en CI-runners waar `~/.local/bin` niet op PATH staat. Als je graphify opnieuw installeert of upgradet, draai dan opnieuw `graphify hook install` om het ingebakken pad te vernieuwen.

> **Strict mode (Claude Code):** `graphify install --project --strict` zorgt dat de assistent de graaf ook daadwerkelijk gebruikt. De standaardinstallatie *duwt* hem in de richting om `graphify query` te draaien voordat hij bestanden leest; strict mode *blokkeert* de eerste ruwe broncodeleesactie van een sessie en stuurt die om naar de graaf, en valt daarna terug op de zachte duw (zodat dit maximaal één keer per sessie gebeurt en nooit vast blijft zitten). Schakel dit tijdens runtime met `GRAPHIFY_HOOK_STRICT=1`/`0`; de standaardinstallatie blijft ongewijzigd (zachte duw).

<details>
<summary><b>Kies je platform</b> (20+ assistenten, klik om uit te klappen)</summary>

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

Codex-gebruikers hebben ook `multi_agent = true` onder `[features]` in `~/.codex/config.toml` nodig voor parallelle extractie. CodeBuddy gebruikt hetzelfde Agent-tool- en PreToolUse-hookmechanisme als Claude Code. Factory Droid gebruikt de `Task`-tool voor het parallel starten van subagenten. OpenClaw en Aider gebruiken sequentiële extractie (ondersteuning voor parallelle agenten is op die platformen nog vroeg in ontwikkeling). Trae gebruikt de Agent-tool voor het parallel starten van subagenten en ondersteunt **geen** `PreToolUse`-hooks, dus AGENTS.md is daar het altijd-actieve mechanisme.

`--platform agents` (alias `--platform skills`) richt zich op de generieke, cross-framework [Agent-Skills](https://github.com/anthropics/skills)-locaties: de spec-brede, gebruikersglobale `~/.agents/skills/` (gelezen door `npx skills` en spec-conforme frameworks) voor een globale installatie, en `./.agents/skills/` voor een project- (`--project`) installatie. Het kale `graphify install` blijft bewust single-platform (Claude Code) — gebruik het benoemde `agents`-platform wanneer je wilt dat de vaardigheid vindbaar is voor elk framework dat `.agents/skills` leest.

> Codex gebruikt `$graphify` in plaats van `/graphify`.

</details>

<details>
<summary><b>Optionele extra's</b> (installeer alleen wat je nodig hebt)</summary>

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

## Zorg dat je assistent de graaf altijd gebruikt

Draai dit één keer in je project nadat je een graaf hebt gebouwd:

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

Dit schrijft een klein configuratiebestand dat je assistent vertelt om de kennisgraaf te raadplegen bij vragen over de codebase, met een voorkeur voor afgebakende queries zoals `graphify query "<vraag>"` boven het lezen van het volledige rapport of het grepen van ruwe bestanden.

- **Hook-platformen** (Claude Code, Gemini CLI): een hook gaat automatisch af vóór zoekachtige tool-aanroepen (en, op Claude Code, vóór het één-voor-één lezen van broncodebestanden via de Read/Glob-tools) en duwt je assistent richting het graaf-pad.
- **Instructiebestand-platformen** (Codex, OpenCode, Cursor, enz.): permanente instructiebestanden (`AGENTS.md`, `.cursor/rules/`, enz.) bieden dezelfde query-eerst-begeleiding.

`GRAPH_REPORT.md` blijft beschikbaar voor een brede architectuurbeoordeling.

**CodeBuddy** doet dezelfde twee dingen als Claude Code: schrijft een `CODEBUDDY.md`-sectie die CodeBuddy vertelt om `graphify-out/GRAPH_REPORT.md` te lezen voordat het architectuurvragen beantwoordt, en installeert `PreToolUse`-hooks (`.codebuddy/settings.json`) die afgaan vóór Bash-zoekcommando's en bestandsleesacties, en die richting `graphify query` duwen.

**Codex** schrijft naar `AGENTS.md`, wat op dit platform de daadwerkelijke drager is van de altijd-actieve graaf-begeleiding. `graphify codex install` registreert ook een `PreToolUse`-hook in `.codex/hooks.json` (`graphify hook-check`), maar die entry is bewust een **no-op**: Codex Desktop wijst `hookSpecificOutput.additionalContext` op `PreToolUse` af, dus het uitzenden van een duw daar zou Bash-tool-aanroepen breken. Anders dan bij Claude Code, waar de hook (`graphify hook-guard`) de duw geeft, gaat de hook op Codex wel af maar doet bewust niets, en is `AGENTS.md` het altijd-actieve mechanisme.

**Kilo Code** installeert de Graphify-vaardigheid naar `~/.config/kilo/skills/graphify/SKILL.md` en een native `/graphify`-commando naar `~/.config/kilo/command/graphify.md`. `graphify kilo install` schrijft ook `AGENTS.md` plus een native `tool.execute.before`-plugin (`.kilo/plugins/graphify.js` + `.kilo/kilo.json`- of `.kilo/kilo.jsonc`-registratie), zodat Kilo hetzelfde altijd-actieve graaf-herinneringsgedrag krijgt via native `.kilo`-configuratie.

**Cursor** schrijft `.cursor/rules/graphify.mdc` met `alwaysApply: true`, zodat Cursor het automatisch in elk gesprek opneemt, zonder dat er een hook nodig is.

Om graphify van alle platformen tegelijk te verwijderen: `graphify uninstall` (voeg `--purge` toe om ook `graphify-out/` te verwijderen). Of gebruik het per-platform-commando (bijvoorbeeld `graphify claude uninstall`).

---

## Wat er in het rapport staat

- **Godknooppunten** — de meest verbonden concepten in je project. Alles loopt hierdoorheen.
- **Verrassende verbindingen** — koppelingen tussen dingen die in verschillende bestanden of modules leven. Gerangschikt op hoe onverwacht ze zijn.
- **Het "waarom"** — inline commentaar (`# NOTE:`, `# WHY:`, `# HACK:`), docstrings en ontwerprationale uit documenten worden geëxtraheerd als losse knooppunten, gekoppeld aan de code die ze verklaren.
- **Voorgestelde vragen** — 4–5 vragen die de graaf bij uitstek kan beantwoorden.
- **Betrouwbaarheidslabels** — elke afgeleide relatie is gelabeld als `EXTRACTED`, `INFERRED`, of `AMBIGUOUS`. Je weet altijd wat er gevonden versus geraden is.

---

## Welke bestanden het verwerkt

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

Code wordt **lokaal geëxtraheerd zonder API-aanroepen** (AST via tree-sitter). Al het andere gaat via de model-API van je AI-assistent.

Google Drive for desktop `.gdoc`-, `.gsheet`- en `.gslides`-bestanden zijn snelkoppelingen,
geen documentinhoud. Om native Google Docs, Sheets en Slides op te nemen
in een headless extractie, installeer en authenticeer je de
[`gws`-CLI](https://github.com/googleworkspace/cli), en draai je dan:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

Je kunt ook `GRAPHIFY_GOOGLE_WORKSPACE=1` instellen. Graphify exporteert snelkoppelingen naar
`graphify-out/converted/` als Markdown-sidecars, en extraheert vervolgens die bestanden.

---

## Veelgebruikte commando's

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

Zie [Decouple: risicogescoorde Extract-Class-kandidaten](#decouple-risicogescoorde-extract-class-kandidaten) hierboven, of de [volledige opdrachtenreferentie](#volledige-opdrachtenreferentie) hieronder.

---

## Bestanden negeren

Maak een `.graphifyignore` in je projectroot — dezelfde syntax als `.gitignore`, inclusief `!`-negatie.

**`.gitignore` wordt automatisch gerespecteerd.** graphify leest de `.gitignore` in elke map. Als er ook een `.graphifyignore` aanwezig is, worden de twee **samengevoegd** — `.graphifyignore`-patronen worden als laatste geëvalueerd, dus zij winnen bij conflicten (inclusief `!`-negaties). Het toevoegen van een `.graphifyignore` sluit alleen ooit méér uit; het neemt nooit een bestand opnieuw op dat je `.gitignore` al uitsloot. Scoping van submappen werkt op dezelfde manier als bij git — een ignore-bestand beïnvloedt alleen zijn eigen subtree.

Geef `--no-gitignore` mee aan `graphify extract` wanneer git-genegeerde gegenereerde of getranspileerde code in de graaf thuishoort. Dit schakelt `.gitignore` en `.git/info/exclude` uit; `.graphifyignore` blijft van toepassing.

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

## Team-opzet

`graphify-out/` is bedoeld om naar git te worden gecommit, zodat iedereen in het team met een kaart begint.

**Aanbevolen toevoegingen aan `.gitignore`:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` is nu portable — sleutels worden opgeslagen als relatieve paden en opnieuw verankerd bij het laden, dus committen is veilig en voorkomt een volledige rebuild bij de eerste checkout.

**Workflow:**
1. Eén persoon draait `/graphify .` en commit `graphify-out/`.
2. Iedereen pullt — hun assistent leest de graaf meteen.
3. Draai `graphify hook install` om na elke commit automatisch te herbouwen (alleen AST, geen API-kosten). Dit zet ook een git-merge-driver op zodat `graph.json` nooit met conflictmarkers achterblijft — twee ontwikkelaars die parallel committen krijgen hun grafen automatisch samengevoegd.
4. Wanneer documenten of papers veranderen, draai je `/graphify --update` om die knooppunten te vernieuwen.

---

## De graaf direct gebruiken

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

De MCP-server geeft je assistent gestructureerde toegang: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Gedeelde HTTP-server

`--transport stdio` (de standaard) start één lokale server per ontwikkelaar. `--transport http` levert dezelfde tools via de MCP Streamable HTTP-transport, zodat één gedeeld proces de graaf voor het hele team kan bedienen — clients richten hun IDE-MCP-configuratie op `http://<host>:8080/mcp` in plaats van graphify lokaal te draaien.

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

De standaard `127.0.0.1`-binding is alleen loopback. Zet `--host 0.0.0.0` **en** `--api-key` samen wanneer je op een gedeelde host publiceert. Draai het in een container:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **WSL/Linux-opmerking:** Ubuntu levert `python3`, geen `python`. Gebruik een venv om conflicten te vermijden:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## Omgevingsvariabelen

Deze zijn alleen nodig voor **headless/CI-extractie** (`graphify extract`). Bij gebruik via de `/graphify`-vaardigheid in je IDE wordt de model-API geleverd door je IDE-sessie — geen extra sleutels nodig.

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

## Privacy

- **Codebestanden** — lokaal verwerkt via tree-sitter. Niets verlaat je machine. Een corpus met alleen code heeft geen API-sleutel nodig — `graphify extract` draait volledig offline. Voeg bij een gemengde repository `--code-only` toe om alleen de code te indexeren en de documenten/PDF's/afbeeldingen over te slaan die anders een LLM nodig zouden hebben.
- **Video/audio** — lokaal getranscribeerd met faster-whisper. Niets verlaat je machine.
- **Documenten, PDF's, afbeeldingen** — verzonden naar je AI-assistent voor semantische extractie (via de `/graphify`-vaardigheid, met welk model je IDE-sessie ook draait). Headless `graphify extract` vereist `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), een draaiende Ollama-instantie (`OLLAMA_BASE_URL`), AWS-credentials via de standaard providerketen (Bedrock — geen API-sleutel nodig, gebruikt IAM), of de `claude`-CLI-binary (Claude Code — geen API-sleutel nodig, gebruikt je Claude-abonnement). De `--dedup-llm`-vlag gebruikt dezelfde sleutel.
- **Dataresidentie** — `graphify extract` detecteert automatisch welke provider te gebruiken op basis van welke API-sleutel is ingesteld (prioriteit: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). Voor code met dataresidentie-vereisten gebruik je `--backend ollama` (volledig lokaal) of geef je een expliciete `--backend`-vlag mee. Kimi (`MOONSHOT_API_KEY`) routeert naar Moonshot AI-servers in China.
- **Geen telemetrie**, geen gebruikstracking, geen analytics.
- **Query-logging** — elke `graphify query`-, `graphify path`-, `graphify explain`- en MCP-`query_graph`-aanroep wordt gelogd naar `~/.cache/graphify-queries.log` in JSON Lines-formaat (tijdstempel, vraag, corpus, teruggegeven knooppunten, duur). Volledige subgraaf-responses worden **niet** standaard opgeslagen. Zet `GRAPHIFY_QUERY_LOG_DISABLE=1` om je af te melden, of `GRAPHIFY_QUERY_LOG=/dev/null` om te dempen zonder het codepad uit te schakelen.

---

## Beperkingen en grenzen

Wat graphify bewust **niet** doet, en waar de dekking ophoudt:

- **Geen semantische/vector-zoekmachine.** De graaf is structureel — knooppunten en getypeerde edges herleid uit de bron, geen embeddings. `graphify query`/`path`/`explain` doorlopen die structuur; ze kunnen geen verbinding tonen die niet als edge is gerepresenteerd, zelfs als die "semantisch" gerelateerd is. Er is geen fallback op basis van similarity/nearest-neighbor.
- **Documenten, PDF's, afbeeldingen en headless video/URL-extractie zijn niet volledig lokaal.** Alleen code (tree-sitter AST) en audio/video-transcriptie (faster-whisper) draaien volledig offline. Het extraheren van documenten/PDF's/afbeeldingen roept altijd een LLM aan — het model van je AI-assistent via de `/graphify`-vaardigheid, of een geconfigureerde backend-API-sleutel voor headless `graphify extract`. Zie [Privacy](#privacy) hierboven voor precies welke vlag of sleutel elk pad nodig heeft.
- **De state-sharing-controle van decouple dekt niet elke taal.** C heeft geen betrouwbaar `self`/`this`-signaal zonder volledige type-inferentie, dus is uitgesloten (zie de [taaldekkingstabel](#decouple-risicogescoorde-extract-class-kandidaten) hierboven). Een god-knooppunt in een niet-ondersteunde taal, of waarvan de bron niet gelezen kan worden, valt terug op scoring op basis van alleen de aanroepgraaf (`state_analysis: "skipped"`) in plaats van een geverifieerde state-controle.
- **De 3D-dataflow-vloer is een naamheuristiek, geen dataflow/taint-analyse.** De I/O-grensdetectie van `data_floor` (parsers, loaders, readers, writers, DB/HTTP-clients) matcht op naamconventies (`boundary_reason`); een grensknooppunt met een onconventionele naam kan gemist worden, waardoor onderschat wordt hoe diep de rest van de graaf zit.
- **Betrouwbaarheidslabels zijn graphify's eigen resolutie-vertrouwen, geen absolute waarheid.** `INFERRED`- en `AMBIGUOUS`-edges zijn best-effort-resoluties en kunnen nog steeds fout zijn, vooral bij sterk dynamische idiomen (reflectie, runtime-dispatch, metaprogrammering) die geen enkele statische AST-pass volledig kan oplossen.
- **HTML-visualisatie en graafgrootte hebben allebei een plafond.** `graph.html` / `DECOUPLE.html` slaan generatie standaard over boven 5.000 knooppunten (`MAX_NODES_FOR_VIZ`, te verhogen via `GRAPHIFY_VIZ_NODE_LIMIT`); `graph.json` zelf is begrensd op 512 MiB (`GRAPHIFY_MAX_GRAPH_BYTES` om dit te overschrijven). Gebruik `--no-viz` samen met `query`/`path`/`explain` voor corpora die een van beide limieten overschrijden.
- **Cross-project-bewustzijn is opt-in, niet automatisch.** `graphify query` ziet alleen de ene graaf waar je naar wijst. Vragen over meerdere repositories vereisen dat je eerst elk project expliciet registreert in de gedeelde graaf (`graphify global add`, begrensd op `GRAPHIFY_MAX_CONTEXTS` niet-standaard contexten per MCP-server) — graphify scant nooit uit zichzelf je machine op andere repositories.
- **Parallelle multi-agent-extractie hangt af van het platform.** Het vereist ondersteuning aan de kant van de assistent voor het starten van subagenten (`multi_agent = true` onder `~/.codex/config.toml` voor Codex, de Agent/Task-tool op Claude Code/CodeBuddy/Factory Droid/Trae). OpenClaw en Aider extraheren momenteel alleen sequentieel.
- **De gedeelde MCP-HTTP-server bindt standaard alleen aan loopback.** Om hem vanaf een andere machine te bereiken heb je expliciet `--host 0.0.0.0` **en** `--api-key` nodig; graphify beheert geen TLS of enige andere authenticatie dan dat ene bearer-token.
- **PowerShell interpreteert een leidend `/` als padscheidingsteken.** `/graphify .` mislukt daardoor op Windows PowerShell — dat is geen bug in graphify — gebruik in plaats daarvan `graphify .`.

---

## Probleemoplossing

**`graphify: command not found` na installatie**
De CLI is geïnstalleerd, maar zijn bin-map staat niet op de `PATH` van je shell. Kies de oplossing voor hoe je hebt geïnstalleerd:
- **uv** (`uv tool install graphifyy`): het commando komt terecht in de tool-bin-map van uv (`~/.local/bin`), die op een verse macOS/zsh-opzet vaak nog niet op `PATH` staat. Draai `uv tool update-shell`, en open dan een nieuwe terminal. (Vind de map met `uv tool dir --bin`.)
- **pipx** (`pipx install graphifyy`): draai `pipx ensurepath`, en open dan een nieuwe terminal.
- **pip** (`pip install graphifyy`): pip installeert scripts naar een gebruikers-bin-map die mogelijk niet op `PATH` staat — voeg `~/Library/Python/3.x/bin` (macOS) of `~/.local/bin` (Linux) toe aan je `PATH` in `~/.zshrc`/`~/.bashrc`, of draai gewoon `python -m graphify`.

**`uvx graphify …` of `uv tool run graphify …` slaagt er niet in `graphify` te herleiden**
Het PyPI-pakket is `graphifyy`; `graphify` is alleen het commando dat het levert. `uv tool run` behandelt het eerste woord als een *pakketnaam*, dus het zoekt naar een pakket genaamd `graphify` en meldt `No solution found … no versions of graphify`. Noem het pakket expliciet: `uvx --from graphifyy graphify install` (hetzelfde als `uv tool run --from graphifyy graphify install`). Of installeer eenmalig `uv tool install graphifyy` en roep daarna `graphify` direct aan.

**`uv run --with graphifyy python -m graphify` draait stilletjes een oudere installatie**
`uv run` gebruikt je *systeem*-Python, dus als er ook een oudere `graphifyy` op je systeem staat (bijvoorbeeld van een eerdere `pip install graphifyy`), kan Python die kopie eerder vinden op `sys.path` en overschrijft `--with graphifyy` deze niet. Het draait zonder foutmelding, maar je krijgt het gedrag van de *oude* versie — bijvoorbeeld env-overrides zoals `OPENAI_BASE_URL` worden stilzwijgend genegeerd, waardoor verzoeken het standaard-endpoint raken en falen met een 401 die op een verkeerde sleutel lijkt. Het herkenningsteken is een regel `warning: skill is from graphify <newer>, package is <older>` — dat betekent dat er een andere installatie is geladen, niet slechts een verouderd vaardigheidsbestand. Controleer welke kopie daadwerkelijk is geladen:
```bash
python -c "import graphify; print(graphify.__file__)"
```
Draai daarna het geïnstalleerde commando direct (dat gebruikt de door uv beheerde kopie), of verwijder de verouderde systeemkopie:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` werkt maar het `graphify`-commando niet**
De `PATH` van je shell bevat de bin-map niet waar het commando naartoe is geïnstalleerd. Geef de voorkeur aan `uv tool install` / `pipx install` boven gewone `pip`, draai dan `uv tool update-shell` / `pipx ensurepath` en open een nieuwe terminal (zie de installatienotities hierboven).

**`/graphify .` veroorzaakt "path not recognized" in PowerShell**
PowerShell behandelt een leidende `/` als padscheidingsteken. Gebruik `graphify .` (zonder schuine streep) op Windows.

**Graaf heeft minder knooppunten na `--update` of rebuild**
Als een refactor bestanden heeft verwijderd, blijven de oude knooppunten hangen. Geef `--force` mee (of zet `GRAPHIFY_FORCE=1`) om te overschrijven, zelfs wanneer de rebuild minder knooppunten heeft.

**`extract` stopt met "extraction was incomplete ... refusing to overwrite"**
Wanneer een extractiepass crasht of een walk het corpus niet volledig kan lezen, zou de run kleiner zijn dan een volledige, dus weigert `graphify extract` een grotere bestaande graaf te overschrijven met het gedeeltelijke resultaat (ter bescherming van je `graph.json`). Los het onderliggende probleem op en draai opnieuw, of geef `--allow-partial` mee om toch te overschrijven.

**Graaf heeft dubbele knooppunten voor dezelfde entiteit (spookduplicaten)**
Spookduplicaten (hetzelfde symbool dat twee keer voorkomt — één keer uit AST-extractie met een bronlocatie, één keer uit semantische extractie zonder) worden nu automatisch samengevoegd tijdens het bouwen. Als je dit ziet in een graaf die vóór v0.8.33 is gebouwd, draai dan een volledige heropbouw om op te ruimen:
```bash
graphify extract . --force
```

**Ollama loopt uit VRAM / context window exceeded**
Het KV-cache-venster wordt automatisch geschaald, maar kan te groot zijn voor je GPU. Verklein het:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**`LLM returned invalid JSON` / `Unterminated string`-waarschuwingen**
De response van het model raakte zijn output-tokenlimiet en werd midden in een string afgekapt. graphify herstelt hier automatisch van (het splitst de chunk en extraheert de helften opnieuw, en een te groot enkel document wordt eerst gesneden op kop/paragraafgrenzen, zodat het hele bestand toch gedekt blijft), dus deze waarschuwingen zijn ruis, geen dataverlies. Om de ruis te verminderen, verhoog je de output-cap of verklein je de output per chunk:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
Geef bij een cloud-gateway zoals OpenRouter de voorkeur aan `--backend openai` (zet `OPENAI_BASE_URL`) boven de Ollama-shim — dat is een schoner OpenAI-compatibel pad. Als het model zijn eigen max-outputplafond heeft, is het verlagen van `--token-budget` de betrouwbare hendel.

**Graph HTML is te groot om in een browser te openen (>5000 knooppunten)**
Sla HTML-generatie over en gebruik de JSON direct:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**`graph.json` heeft conflictmarkers nadat twee ontwikkelaars tegelijk committen**
Draai `graphify hook install` — dat zet een git-merge-driver op die `graph.json` automatisch union-merged, zodat conflicten nooit voorkomen.

**Extractie geeft lege knooppunten/edges terug voor documenten of PDF's**
Documenten, PDF's en afbeeldingen vereisen een LLM-aanroep — corpora met alleen code hebben geen sleutel nodig. Controleer of je API-sleutel is ingesteld en de backend correct is:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**Vaardigheidsversie-mismatchwaarschuwing in je IDE**
Je geïnstalleerde graphify-versie verschilt van het vaardigheidsbestand. Update:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**Claude Code prompt cache geïnvalideerd na elke `graphify extract`**
Graphify schrijft outputbestanden (`graph.json`, `graphify-out/`) naar de werkruimte. Als die paden niet genegeerd worden, invalideert elke schrijfactie de prompt cache van Claude Code, wat op de volgende beurt een volledige heruploads tegen cache-write-tarieven afdwingt. Voeg ze toe aan `.claudeignore`:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## Volledige opdrachtenreferentie

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

> **Namen van gemeenschappen:** binnen een agent (Claude Code, Gemini CLI) noemt de agent de gemeenschappen zelf. Wanneer je de kale CLI draait, geeft `cluster-only` ze automatisch namen met de geconfigureerde backend (ingebouwd of een aangepaste OpenAI-compatibele provider) — geef `--no-label` mee om `Community N` te behouden, of draai `graphify label` om op aanvraag namen te (her)genereren.

---

## Meer informatie

- [Hoe het werkt](../how-it-works.md) — de extractiepijplijn, community detection, betrouwbaarheidsscoring, benchmarks
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — moduleopbouw, hoe je een taal toevoegt
- [Optionele integraties](../docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — het boek over de ideeën achter graphify, de architectuur van begin tot eind

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) is de altijd-actieve laag bovenop graphify — het past dezelfde graafbenadering toe op je hele werkcontext: meetings, bestanden, documenten en code, continu bijgewerkt op de achtergrond.

Gebouwd voor mensen en teams wier werk zich afspeelt over honderden gesprekken en documenten die ze nooit volledig kunnen reconstrueren.

**[Meld je aan voor de wachtlijst op graphify.com](https://graphify.com).** Gratis proefversie lanceert binnenkort.

---

<details>
<summary>Bijdragen</summary>

### Ontwikkelomgeving opzetten

Het project gebruikt [uv](https://docs.astral.sh/uv/) voor de ontwikkelworkflow. Installeer het eenmalig, en dan:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

Controleer de editable install:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### Tests uitvoeren

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> macOS-opmerking: de testsuite bevat zowel `sample.f90`- als `sample.F90`-fixtures. Deze botsen op hoofdletterongevoelige HFS+/APFS-bestandssystemen. Draai op Linux of in een Docker-container als je beide Fortran-varianten tegelijk moet testen.

### Git-workflow

- Actieve ontwikkeling vindt plaats op de `v8`-branch.
- Commitstijl: `fix: <description>` / `feat: <description>` / `docs: <description>`
- Draai voordat je een PR opent `uv run pytest tests/ -q` en bevestig dat deze slaagt.
- Voeg voor elke nieuwe taalextractor een fixture-bestand toe aan `tests/fixtures/` en tests aan `tests/test_languages.py`.

### Waaraan je kunt bijdragen

**Uitgewerkte voorbeelden** zijn de nuttigste bijdrage. Draai `/graphify` op een echt corpus, sla de output op in `worked/{slug}/`, schrijf een eerlijke `review.md` die beschrijft wat de graaf goed en fout had, en open een PR.

**Extractiebugs** — open een issue met het invoerbestand, de cache-entry (`graphify-out/cache/`), en wat er gemist of fout was.

Zie [ARCHITECTURE.md](../../ARCHITECTURE.md) voor moduleverantwoordelijkheden en hoe je een taal toevoegt.

</details>
