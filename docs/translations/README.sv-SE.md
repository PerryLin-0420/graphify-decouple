<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>En fork av <a href="https://github.com/Graphify-Labs/graphify">graphify</a> som lägger till <code>graphify decouple</code></b> — 0-LLM, riskbedömda Extract-Class-kandidater för god objects, återverifierade mot den faktiska källkoden (inte bara anropsgrafen) innan något rekommenderas. Se <a href="#decouple-riskbedömda-extract-class-kandidater">Decouple: riskbedömda Extract-Class-kandidater</a> nedan.
</p>

<div align="center">
<details><summary><b>Läs detta på andra språk</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>Tidig tillgång till graphify-plattformen är öppen innan den publika v1-lanseringen: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

Skriv `/graphify` i din AI-kodassistent och den mappar hela ditt projekt (kod, dokument, PDF-filer, bilder, video) till en **kunskapsgraf** som du kan **fråga istället för att grepa** igenom filer.

- **Kodkartor gratis, helt lokalt.** Koden parsas med tree-sitter AST: deterministiskt, ingen LLM, ingenting lämnar din maskin. (Dokument, PDF-filer, bilder och video använder din assistents modell, eller en konfigurerad API-nyckel, för en semantisk genomgång.)
- **Varje kant har en förklaring.** Varje koppling märks `EXTRACTED` (explicit i källan) eller `INFERRED` (löst av graphify), så du kan se vad som lästs direkt från vad som härletts.
- **Inte ett vektorindex.** Inga embeddings, ingen vektordatabas: en verklig graf du kan navigera i. Ställ en fråga, spåra vägen mellan två saker, eller förklara ett koncept.

> Vill du ha detta alltid på, uppdaterande i bakgrunden över din kod, dokumentation och möten istället för bara på begäran? Det är vad vi bygger på **[graphify.com](https://graphify.com)**, och tidig tillgång är öppen nu på **[app.graphify.com](https://app.graphify.com/login)**.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="graphifys interaktiva graph.html som visar FastAPI-kodbasen som en kraftbaserad kunskapsgraf med en legend över upptäckta communities" width="900">
</p>
<p align="center">
  <em>FastAPI-kodbasen kartlagd av graphify. Varje nod är ett koncept, färgerna är upptäckta communities, och allt är klickbart i graph.html.</em>
</p>

**Kom igång** (30 sekunder):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

Sedan, i din AI-assistent:

```
/graphify .
```

Det är allt. Du får **tre filer**:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**Fungerar i** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot och 15+ till — [välj din plattform](#installation).

---

## Se det i praktiken

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="graphify path-fråga: en terminal frågar efter den kortaste vägen mellan FastAPI och ModelField, och svaret lyser upp hopp för hopp genom kunskapsgrafen" width="900">
</p>

När grafen är byggd frågar du den istället för att läsa filer. Verklig output, graphify körd på FastAPI-kodbasen som visas ovan:

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

Varje kant bär en **konfidensmärkning** (`EXTRACTED` = explicit i källan, `INFERRED` = härledd genom upplösning), så du kan se vad som lästs direkt från vad som härletts. `graphify query "<question>"` returnerar en avgränsad delgraf för en fråga i klarspråk, och `graphify path A B` spårar hur två saker hänger ihop.

---

## Decouple: riskbedömda Extract-Class-kandidater

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: MainWindow-god-noden delas upp i riskbedömda kandidatklasser, med en varning om delat state mellan två av dem" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: MainWindows 5 föreslagna klasser, Node Info-panelen öppen på Main Window Axis and Range Controls och visar 0.608 state-överlapp med Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>DECOUPLE.html i en verklig körning — att klicka på en föreslagen klass visar exakt vilken annan klass den delar state med, och vad som specifikt delas.</em>
</p>

Samma sida renderar också själva uppdelningen. Att slå på **Preview decoupled view** byter ut god-klassens egna metoder mot de föreslagna klasserna och drar om kanterna på plats — själva kopplingsändringen, inte ett omritat diagram:

| Före — god-klassen idag | Efter — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html före växlingen: en enda MainWindow-hubbnod med sina egna metoder utspridda runt omkring" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html efter växlingen: samma nod reducerad till 5 rombformade föreslagna klasser, gröna streckade kanter som visar vilka metoder som extraherades till var och en, och röda kanter som visar det delade instanstillståndet mellan två av dem" width="440"> |
| En nod med 47 av sina egna metoder, där varje enskild bara går att nå genom klassen. | De föreslagna klasserna. Grönt streckat = vad som extraherades till var och en; rött = det instanstillstånd två av dem fortfarande delar, vilket är precis det som avgör `split` mot `keep_as_is`. Bara kandidater som klarar rikströskeln ritas ut — här 5 av 6, och därför har en metod ingen romb att landa på. |

`graphify decouple` hittar god objects och talar om för dig om det faktiskt är värt att dela upp dem — inte bara att de är stora.

Felmönstret detta finns till för att fånga: en klass med 47 metoder som anropsgrafklustring gärna delar upp i 5 grupper som ser snygga och avgränsade ut, men där alla fortfarande läser och skriver exakt samma instansstate `self._chart_style` / `self._crosshair` under ytan. Skeppar du den uppdelningen har du inte frikopplat något — du har flyttat metoder till nya filer som fortfarande inte kan testas, ändras eller resoneras kring oberoende av varandra, eftersom de alla fortfarande behöver samma delade state skickat tillbaka. Ett verktyg som bara tittar på anropsgrafen kan inte se detta alls; det måste gå tillbaka till den faktiska källkoden.

**Två kontroller, båda 0-LLM, båda deterministiska:**

1. **Är detta överhuvudtaget ett God Object?** En nod med hög grad kan vara ett verkligt God Object (många av sina EGNA metoder, spridda över orelaterade ansvarsområden — Extract Class är lämpligt) eller en överreferensierad hub/datamodell (få egna metoder, mestadels *inkommande* referenser — att dela upp dess innehåll gör ingenting; lösningen är att smalna av gränssnittet, inte att extrahera en klass). `classify_god_node` skiljer dessa åt genom `member_ratio`, inte rå grad — skillnaden som hindrar `TraceSource` (84 kanter, men bara 6 egna metoder) från att få ett felaktigt uppdelningsförslag, medan `MainWindow` (88 kanter, 47 egna metoder) korrekt får ett.
2. **Skulle uppdelningen faktiskt minska kopplingen?** `risk_before` (god-nodens nuvarande storlek/koppling/fragmentering) jämförs med `risk_after` — den NYA risken som själva uppdelningen skulle introducera: anrop mellan grupper som tidigare var osynliga kanter inom klassen och som blir explicita beroenden mellan klasser, anropare som nu skulle behöva bero på fler än en ny klass, och — kontrollen en anropsgraf strukturellt inte kan göra — hur mycket `self`/`this`-instansstate (läsningar, skrivningar och delade hjälpmetodanrop, viktade separat: en delad **skrivning** poängsätts högre än en delad läsning) de föreslagna grupperna faktiskt har gemensamt. Detta parsar om god-nodens egen källfil direkt med tree-sitter; det förlitar sig inte på graphifys egen extraherade graf, som aldrig registrerar fältnivååtkomst för något språk. Bara när `risk_after` klarar ett tröskelvärde under `risk_before` rekommenderar planen `split` — annars är det `marginal` eller `keep_as_is`, och en avskräckt kandidat rapporteras alltid som ett tal, aldrig ritad som en form du måste ifrågasätta med ögat.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

Skriver ut tre filer bredvid `graph.json`:

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

**Språkstöd för state-delningskontrollen** (klassificeringen ovan som bara använder anropsgrafen fungerar för alla språk graphify extraherar; denna tabell gäller specifikt omparsningen av källkoden som verifierar `self`/`this`-state-överlapp):

| Language | Stöds | Anteckningar |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` är sin egen AST-nod, inte en inlindad fältåtkomst — hanteras explicit |
| C# | ✅ | |
| Rust | ✅ | `self.x` via `impl`-block |
| Ruby | ✅ | `@x` (det dominerande idiomet) + `self.foo`-anrop |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | upplösning av mottagare per metod — Go har inget `self`/`this`-nyckelord, så mottagarnamnet (`f` i `func (f *Foo) M()`) löses upp på nytt för varje metod |
| C | ❌ | en struct-pekarparameter har ingen syntaktisk markör som skiljer den från någon annan parameter — ingen tillförlitlig signal utan fullständig typinferens |

En god-nod på ett språk som inte stöds, eller en vars källkod inte kan läsas, markeras `state_analysis: "skipped"` — klassificeringen och anropsgrafpoängen körs fortfarande, men rekommendationen vilar enbart på anropsgrafen istället för att tyst anta att state-kontrollen godkändes.

---

## Vad det gör

Det du får direkt:

| Funktion | Vad du får |
|---|---|
| **God nodes** | De mest sammankopplade koncepten, så du ser vad allt flödar genom |
| **Communities** | Grafen uppdelad i undersystem (Leiden), med LLM-fria etiketter |
| **Länkar mellan filer** | `calls` / `imports` / `inherits` / `mixes_in` löst över ~40 språk via tree-sitter AST |
| **Query, path, explain** | Ställ en fråga, spåra vägen mellan två saker, eller förklara ett koncept, allt mot `graph.json` |
| **Motivering + dokumentreferenser** | `# NOTE:` / `# WHY:`-kommentarer och ADR/RFC-citeringar blir förstklassiga noder länkade till koden |
| **Bortom kod** | Dokument, PDF-filer, bilder och video/ljud mappas alla in i samma graf |
| **Lokalt först** | Koden parsas lokalt med tree-sitter (ingen LLM, ingenting lämnar din maskin); bara den semantiska genomgången av dokument/media anropar en backend, och bara om du konfigurerar en |

---

## Benchmarks

| Benchmark | Mätvärde | graphify | Fältet |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | QA-noggrannhet | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | QA-noggrannhet | **76%** | tied with dense RAG |
| Graf-byggning | LLM-krediter | **0** | per-token för de flesta system |

Alla system kördes på samma testrigg med samma modell och samma budgetar, poängsatta av en domare som blindvaliderades mot en andra domare (90,6 % överensstämmelse, Cohens kappa 0,81). Fullständiga per-system-tabeller, resultatet för kodintelligens och kommandon för att reproducera: **[BENCHMARKS.md](../../BENCHMARKS.md)**.

---

## Förutsättningar

| Krav | Minimum | Kontroll | Installation |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(rekommenderas)* | valfri | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(alternativ)* | valfri | `pipx --version` | `pip install pipx` |

**Snabbinstallation för macOS (Homebrew):**
```bash
brew install python@3.12 uv
```

**Snabbinstallation för Windows:**
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

## Installation

> **Officiellt paket:** PyPI-paketet är `graphifyy` (dubbel-y). Andra `graphify*`-paket på PyPI är inte anknutna. CLI-kommandot är fortfarande `graphify`.

**Steg 1 — installera paketet:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**Steg 2 — registrera skillen hos din AI-assistent:**

```bash
graphify install
```

Det är allt. Öppna din AI-assistent och skriv `/graphify .`

Om du vill installera assistent-skillen i det aktuella repot istället för din användarprofil, lägg till `--project`:

```bash
graphify install --project
graphify install --project --platform codex
```

Projektbegränsade installationer skriver under den aktuella katalogen, till exempel
`.claude/skills/graphify/SKILL.md` eller `.agents/skills/graphify/SKILL.md` (plus en
`references/`-sidecar som skillen laddar vid behov), och
skriver ut en `git add`-hint för filer som kan committas.
Plattformsspecifika kommandon som stöder projektbegränsade installationer accepterar samma flagga,
till exempel `graphify claude install --project` eller `graphify codex install --project`.

> **PowerShell-anmärkning:** Använd `graphify .` inte `/graphify .` — det inledande snedstrecket är en sökvägsseparator i PowerShell.

> **`graphify: command not found`?** `uv tool install` / `pipx install` placerar kommandot `graphify` i sin egen verktygs-bin-katalog (`~/.local/bin`). Om ditt skal inte hittar det direkt efter installationen — vanligt på en färsk macOS + zsh-installation — finns den katalogen ännu inte i din `PATH`: kör `uv tool update-shell` (eller `pipx ensurepath`), och öppna sedan en ny terminal. Med ren `pip`, lägg till `~/.local/bin` (Linux) eller `~/Library/Python/3.x/bin` (Mac) till din PATH, eller kör `python -m graphify`.

> **Kör med `uvx` / `uv tool run` istället för att installera?** Namnge paketet, inte kommandot: `uvx --from graphifyy graphify install`. Ren `uvx graphify …` misslyckas (`No solution found … no versions of graphify`) eftersom `uv tool run` läser det första ordet som ett *paket*, och paketet är `graphifyy` — kommandot `graphify` lever inuti det.

> **Undvik `pip install` på Mac/Windows** om möjligt. Skillen slår upp Python vid körningstillfället från `graphify-out/.graphify_python`; om den pekar mot en annan miljö än den där `pip` installerade paketet får du `ModuleNotFoundError: No module named 'graphify'`. `uv tool install` och `pipx install` isolerar paketet i sin egen miljö och undviker detta helt.

> **Git-hooks och uv tool / pipx:** `graphify hook install` bäddar in den nuvarande interpreterns sökväg direkt i hook-skripten vid installationstillfället, så att post-commit-hooken triggas korrekt även i grafiska git-klienter och CI-runners där `~/.local/bin` inte finns i PATH. Om du installerar om eller uppgraderar graphify, kör `graphify hook install` igen för att uppdatera den inbäddade sökvägen.

> **Strict-läge (Claude Code):** `graphify install --project --strict` gör att assistenten faktiskt använder grafen. Standardinstallationen *puttar* den bara mot att köra `graphify query` innan den läser filer; strict-läget *blockerar* den första råa källkodsläsningen i en session och dirigerar om den till grafen, och återgår sedan till den vanliga putten (så den triggas högst en gång per session och fastnar aldrig). Växla vid körning med `GRAPHIFY_HOOK_STRICT=1`/`0`; standardinstallationen förblir oförändrad (mjuk putt).

<details>
<summary><b>Välj din plattform</b> (20+ assistenter, klicka för att expandera)</summary>

| Plattform | Installationskommando |
|----------|----------------|
| Claude Code (Linux/Mac) | `graphify install` |
| Claude Code (Windows) | `graphify install` (upptäcks automatiskt) eller `graphify install --platform windows` |
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

Codex-användare behöver också `multi_agent = true` under `[features]` i `~/.codex/config.toml` för parallell extraktion. CodeBuddy använder samma Agent-verktyg och PreToolUse-hook-mekanism som Claude Code. Factory Droid använder `Task`-verktyget för parallell subagent-dispatch. OpenClaw och Aider använder sekventiell extraktion (stöd för parallella agenter är fortfarande tidigt på dessa plattformar). Trae använder Agent-verktyget för parallell subagent-dispatch och stöder **inte** `PreToolUse`-hooks, så AGENTS.md är den alltid-på-mekanismen.

`--platform agents` (alias `--platform skills`) riktar sig mot de generiska cross-framework-platserna för [Agent-Skills](https://github.com/anthropics/skills): specifikationens användarglobala `~/.agents/skills/` (läses av `npx skills` och specifikationskompatibla ramverk) för en global installation, och `./.agents/skills/` för en projektinstallation (`--project`). Ren `graphify install` förblir enplattforms (Claude Code) med avsikt — använd den namngivna `agents`-plattformen när du vill göra skillen upptäckbar för alla ramverk som läser `.agents/skills`.

> Codex använder `$graphify` istället för `/graphify`.

</details>

<details>
<summary><b>Valfria tillägg</b> (installera bara det du behöver)</summary>

| Tillägg | Vad det lägger till | Installation |
|---|---|---|
| `pdf` | PDF-extraktion | `uv tool install "graphifyy[pdf]"` |
| `office` | Stöd för `.docx` och `.xlsx` | `uv tool install "graphifyy[office]"` |
| `google` | Rendering av Google Sheets | `uv tool install "graphifyy[google]"` |
| `video` | Transkribering av video/ljud (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | MCP stdio-server | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Stöd för push till Neo4j | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | Stöd för push till FalkorDB | `uv tool install "graphifyy[falkordb]"` |
| `svg` | SVG-export av grafen | `uv tool install "graphifyy[svg]"` |
| `leiden` | Leiden-communitydetektering (endast Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Lokal inferens med Ollama | `uv tool install "graphifyy[ollama]"` |
| `openai` | OpenAI / OpenAI-kompatibla API:er | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic Claude API (`--backend claude`, använder `ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (använder IAM, ingen API-nyckel) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, använder `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "graphifyy[openai]"` |
| `sql` | SQL-schemaextraktion | `uv tool install "graphifyy[sql]"` |
| `postgres` | Direkt introspektion av live PostgreSQL (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | AST-extraktion för BYOND DreamMaker `.dm`/`.dme` (kan behöva en C-kompilator + `python3-dev` om inget hjul matchar din plattform) | `uv tool install "graphifyy[dm]"` |
| `terraform` | AST-extraktion för Terraform / HCL `.tf`/`.tfvars`/`.hcl` | `uv tool install "graphifyy[terraform]"` |
| `pascal` | AST-extraktion för Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` (mer exakta `calls`/`inherits`-kanter; faller tillbaka på en regex-extraktor om den saknas) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | Kinesisk frågesegmentering (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | Allt ovanstående | `uv tool install "graphifyy[all]"` |

</details>

---

## Få din assistent att alltid använda grafen

Kör detta en gång i ditt projekt efter att du har byggt en graf:

| Plattform | Kommando |
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

Detta skriver en liten konfigurationsfil som talar om för din assistent att konsultera kunskapsgrafen för frågor om kodbasen, och föredra avgränsade frågor som `graphify query "<question>"` framför att läsa hela rapporten eller grepa råa filer.

- **Hook-plattformar** (Claude Code, Gemini CLI): en hook triggas automatiskt innan sökliknande verktygsanrop (och, på Claude Code, innan källfiler läses en och en via Read/Glob-verktygen) och puttar din assistent mot grafvägen.
- **Instruktionsfilsplattformar** (Codex, OpenCode, Cursor, med flera): permanenta instruktionsfiler (`AGENTS.md`, `.cursor/rules/`, osv.) ger samma frågeförsta-vägledning.

`GRAPH_REPORT.md` finns fortfarande tillgänglig för bred arkitekturgranskning.

**CodeBuddy** gör samma två saker som Claude Code: skriver en `CODEBUDDY.md`-sektion som talar om för CodeBuddy att läsa `graphify-out/GRAPH_REPORT.md` innan den svarar på arkitekturfrågor, och installerar `PreToolUse`-hooks (`.codebuddy/settings.json`) som triggas innan Bash-sökkommandon och filläsningar, och puttar mot `graphify query` istället.

**Codex** skriver till `AGENTS.md`, vilket är det som faktiskt bär den alltid-på-grafvägledningen på den här plattformen. `graphify codex install` registrerar också en `PreToolUse`-hook i `.codex/hooks.json` (`graphify hook-check`), men den posten är medvetet en **no-op**: Codex Desktop avvisar `hookSpecificOutput.additionalContext` på `PreToolUse`, så att skicka en putt där skulle förstöra Bash-verktygsanrop. Till skillnad från Claude Code, där hooken (`graphify hook-guard`) gör puttandet, triggas hooken på Codex men gör medvetet ingenting, och `AGENTS.md` är den alltid-på-mekanismen.

**Kilo Code** installerar Graphify-skillen till `~/.config/kilo/skills/graphify/SKILL.md` och ett inbyggt `/graphify`-kommando till `~/.config/kilo/command/graphify.md`. `graphify kilo install` skriver också `AGENTS.md` plus en inbyggd `tool.execute.before`-plugin (`.kilo/plugins/graphify.js` + registrering i `.kilo/kilo.json` eller `.kilo/kilo.jsonc`) så att Kilo får samma alltid-på-grafpåminnelsebeteende genom inbyggd `.kilo`-konfiguration.

**Cursor** skriver `.cursor/rules/graphify.mdc` med `alwaysApply: true`, så Cursor inkluderar den i varje konversation automatiskt, ingen hook behövs.

För att ta bort graphify från alla plattformar på en gång: `graphify uninstall` (lägg till `--purge` för att även ta bort `graphify-out/`). Eller använd det plattformsspecifika kommandot (t.ex. `graphify claude uninstall`).

---

## Vad som finns i rapporten

- **God nodes** — de mest sammankopplade koncepten i ditt projekt. Allt flödar genom dessa.
- **Överraskande kopplingar** — länkar mellan saker som finns i olika filer eller moduler. Rankade efter hur oväntade de är.
- **"Varför"** — inline-kommentarer (`# NOTE:`, `# WHY:`, `# HACK:`), docstrings och designmotivering från dokument extraheras som separata noder länkade till koden de förklarar.
- **Föreslagna frågor** — 4–5 frågor som grafen är unikt positionerad att besvara.
- **Konfidensmärkningar** — varje härledd relation märks `EXTRACTED`, `INFERRED` eller `AMBIGUOUS`. Du vet alltid vad som hittades kontra vad som gissades.

---

## Vilka filer den hanterar

| Typ | Filändelser |
|------|-----------|
| Kod (36 tree-sitter-grammatiker) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme` kräver `uv tool install graphifyy[dm]`; `.mts`/`.cts` återanvänder TypeScript-grammatiken, `.cc`/`.cxx` samt CUDA `.cu`/`.cuh` och Metal `.metal` återanvänder C++-grammatiken) |
| Salesforce Apex | `.cls .trigger` (regelbaserad; klasser, interfaces, enums, metoder, triggers, SOQL/DML-kanter) |
| Terraform / HCL | `.tf .tfvars .hcl` (kräver `uv tool install graphifyy[terraform]`) |
| MCP-konfigurationer | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — extraherar servernoder, paketreferenser, krav på miljövariabler |
| Paketmanifest | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — en kanonisk paketnod per paket (efter namn) plus `depends_on`-kanter, så ett paket som refereras från många manifest blir en enda hub |
| Dokument | `.md .mdx .qmd .html .txt .rst .yaml .yml` (markdown-länkar `[text](./other.md)` och `[[wikilänkar]]` blir `references`-kanter mellan dokument) |
| Office | `.docx .xlsx` (kräver `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (frivilligt; kräver `gws`-autentisering och `--google-workspace`; Sheets kräver `uv tool install graphifyy[google]`) |
| PDF-filer | `.pdf` |
| Bilder | `.png .jpg .webp .gif` |
| Video/ljud | `.mp4 .mov .mp3 .wav` med mer (kräver `uv tool install graphifyy[video]`) |
| YouTube/URL:er | valfri video-URL (kräver `uv tool install graphifyy[video]`) |

Kod extraheras **lokalt utan API-anrop** (AST via tree-sitter). Allt annat går genom din AI-assistents modell-API.

Google Drive för desktop-filer av typen `.gdoc`, `.gsheet` och `.gslides` är genvägspekare, inte
dokumentinnehåll. För att inkludera riktiga Google Docs, Sheets och Slides
i en huvudlös extraktion, installera och autentisera
[`gws` CLI](https://github.com/googleworkspace/cli), och kör sedan:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

Du kan också sätta `GRAPHIFY_GOOGLE_WORKSPACE=1`. Graphify exporterar genvägar till
`graphify-out/converted/` som Markdown-sidecars, och extraherar sedan dessa filer.

---

## Vanliga kommandon

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

Se [Decouple: riskbedömda Extract-Class-kandidater](#decouple-riskbedömda-extract-class-kandidater) ovan, eller den [fullständiga kommandoreferensen](#fullständig-kommandoreferens) nedan.

---

## Ignorera filer

Skapa en `.graphifyignore` i din projektrot — samma syntax som `.gitignore`, inklusive `!`-negation.

**`.gitignore` respekteras automatiskt.** graphify läser `.gitignore` i varje katalog. Om en `.graphifyignore` också finns, **slås de samman** — `.graphifyignore`-mönster utvärderas sist, så de vinner vid konflikter (inklusive `!`-negationer). Att lägga till en `.graphifyignore` exkluderar bara mer; den återinkluderar aldrig en fil som din `.gitignore` redan exkluderat. Underkatalogers omfattning fungerar på samma sätt som i git — en ignore-fil påverkar bara sitt eget underträd.

Skicka `--no-gitignore` till `graphify extract` när git-ignorerad genererad eller transpilerad kod ska ingå i grafen. Detta inaktiverar `.gitignore` och `.git/info/exclude`; `.graphifyignore` gäller fortfarande.

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

## Teamkonfiguration

`graphify-out/` är avsett att committas till git så att alla i teamet startar med en karta.

**Rekommenderade tillägg till `.gitignore`:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` är nu portabel — nycklar lagras som relativa sökvägar och omankras vid inläsning, så det är säkert att committa den och det undviker en fullständig ombyggnad vid första utcheckningen.

**Arbetsflöde:**
1. En person kör `/graphify .` och committar `graphify-out/`.
2. Alla andra pullar — deras assistent läser grafen omedelbart.
3. Kör `graphify hook install` för att bygga om automatiskt efter varje commit (endast AST, ingen API-kostnad). Detta sätter också upp en git-mergedriver så att `graph.json` aldrig lämnas med konfliktmarkörer — två utvecklare som committar parallellt får sina grafer union-mergade automatiskt.
4. När dokument eller artiklar ändras, kör `/graphify --update` för att uppdatera dessa noder.

---

## Använda grafen direkt

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

MCP-servern ger din assistent strukturerad åtkomst: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Delad HTTP-server

`--transport stdio` (standard) startar en lokal server per utvecklare. `--transport http` serverar samma verktyg över MCP Streamable HTTP-transporten, så en enda delad process kan serva grafen för hela teamet — klienter pekar sin IDE:s MCP-konfiguration mot `http://<host>:8080/mcp` istället för att köra graphify lokalt.

| Flagga | Standard | Syfte |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Transport att servera på |
| `--host` | `127.0.0.1` | HTTP-bindningshost (använd `0.0.0.0` för att exponera bortom localhost) |
| `--port` | `8080` | HTTP-bindningsport |
| `--api-key` | env `GRAPHIFY_API_KEY` | Kräv `Authorization: Bearer <key>` (eller `X-API-Key`) |
| `--path` | `/mcp` | HTTP-monteringssökväg |
| `--json-response` | av | Returnera vanlig JSON istället för SSE-strömmar |
| `--stateless` | av | Ingen state per session (för lastbalanserade/CI-driftsättningar) |
| `--session-timeout` | `3600` | Städa bort inaktiva stateful sessioner efter N sekunder (`0` inaktiverar) |

Standardbindningen `127.0.0.1` är endast loopback. Sätt `--host 0.0.0.0` **och** `--api-key` tillsammans när du exponerar på en delad host. Kör den i en container:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **Anmärkning för WSL/Linux:** Ubuntu levereras med `python3`, inte `python`. Använd en venv för att undvika konflikter:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## Miljövariabler

Dessa behövs bara för **huvudlös/CI-extraktion** (`graphify extract`). När du kör via `/graphify`-skillen inuti din IDE tillhandahålls modell-API:et av din IDE-session — inga extra nycklar behövs.

| Variabel | Används för | När det krävs |
|---|---|---|
| `ANTHROPIC_API_KEY` | Claude (Anthropic)-backend | `--backend claude` |
| `ANTHROPIC_BASE_URL` | Anthropic-kompatibel endpoint-URL (LiteLLM-proxy, gateways, …) | `--backend claude` (standard: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Modellnamn för Claude-backend — för anpassade endpoints, använd modellnamnet/aliaset din server exponerar | `--backend claude` (standard: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` eller `GOOGLE_API_KEY` | Google Gemini-backend | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI eller OpenAI-kompatibla API:er | `--backend openai` (lokala servrar accepterar valfritt icke-tomt värde) |
| `OPENAI_BASE_URL` | OpenAI-kompatibel server-URL (llama.cpp, vLLM, LM Studio, …) | `--backend openai` (standard: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | Modellnamn för OpenAI-backend — för självhostade servrar, använd modellnamnet/aliaset din server exponerar (kontrollera dess `/v1/models`-endpoint), t.ex. `LFM2.5-8B-A1B-UD-Q4_K_XL` för llama.cpp | `--backend openai` (standard: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | DeepSeek-backend | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Kimi Code-backend | `--backend kimi` |
| `OLLAMA_BASE_URL` | URL för lokal Ollama-inferens | `--backend ollama` (standard: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Ollama-modellnamn | `--backend ollama` (standard: autodetektera) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Åsidosätt Ollamas KV-cache-fönsterstorlek | valfritt — autostorlek som standard |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Minuter att hålla Ollama-modellen laddad | valfritt — sätt `0` för att avlasta efter varje chunk |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI Service-backend | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | Azure-resursens endpoint-URL | `--backend azure` (krävs tillsammans med API-nyckel) |
| `AZURE_OPENAI_API_VERSION` | Åsidosättning av Azure API-version | valfritt — standard `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` eller `GRAPHIFY_AZURE_MODEL` | Azure-driftsättningsnamn | valfritt — standard `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — standard autentiseringskedja | `--backend bedrock` (ingen API-nyckel, använder IAM) |
| `GRAPHIFY_MAX_WORKERS` | Antal trådar för AST-parallellism | valfritt — även flaggan `--max-workers` |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Höj outputtaket för täta korpusar | valfritt — t.ex. `32768` för stora filer |
| `GRAPHIFY_API_TIMEOUT` | Timeout per anrop i sekunder för HTTP-, claude-cli-, Anthropic SDK- och Bedrock-backends (standard: 600) | valfritt — även flaggan `--api-timeout` |
| `GRAPHIFY_MAX_RETRIES` | Hur många gånger en rate-limitad (429) begäran görs om innan den ger upp (standard: 6; respekterar `Retry-After`) | valfritt — höj för strikta per-organisationsgränser (t.ex. kimi); `0` inaktiverar |
| `GRAPHIFY_FORCE` | Tvinga ombyggnad av grafen även med färre noder | valfritt — även flaggan `--force` |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Aktivera Google Workspace-export automatiskt | valfritt — sätt till `1` |
| `GRAPHIFY_TRIAGE_BACKEND` | Backend för `graphify prs --triage` | valfritt — autodetekteras från tillgängliga nycklar |
| `GRAPHIFY_TRIAGE_MODEL` | Åsidosättning av modell för triage | valfritt — t.ex. `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | Sätt till `1` för att slå på den lokala frågeloggen på `~/.cache/graphify-queries.log` (registrerar varje query/path/explain-fråga + korpussökväg). Avstängt som standard — inget skrivs om du inte aktivt väljer det (#1797) | valfritt |
| `GRAPHIFY_QUERY_LOG` | Aktivera frågeloggen och skriv den till denna sökväg istället för standardvägen | valfritt — avstängt om inte denna eller `_ENABLE` är satt |
| `GRAPHIFY_QUERY_LOG_DISABLE` | Sätt till `1` för att tvinga av frågeloggen (vinner över aktiveringsvariablerna) | valfritt |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | När loggen är aktiverad, registrera även fullständiga delgrafsvar (avstängt som standard) | valfritt |
| `GRAPHIFY_MAX_GRAPH_BYTES` | Åsidosätt storleksgränsen på 512 MiB för graph.json — t.ex. `700MB`, `2GB`, eller rena byte | valfritt — användbart för mycket stora korpusar |
| `GRAPHIFY_MAX_CONTEXTS` | Maximalt antal icke-standard projektgrafer som behålls av en multiprojekt-MCP-server | valfritt — standard: `8`; ogiltiga värden använder `8`, och värden under `1` använder `1` |
| `GRAPHIFY_LLM_TEMPERATURE` | Åsidosätt LLM-temperatur för semantisk extraktion — t.ex. `0.7`, eller `none` för att utesluta | valfritt — utesluts automatiskt för o1/o3/o4/gpt-5-resonemangsmodeller |

---

## Integritet

- **Kodfiler** — bearbetas lokalt via tree-sitter. Ingenting lämnar din maskin. En korpus med bara kod kräver ingen API-nyckel — `graphify extract` körs helt offline. I ett blandat repo, lägg till `--code-only` för att bara indexera koden och hoppa över dokument/PDF-filer/bilder som annars skulle behöva en LLM.
- **Video/ljud** — transkriberas lokalt med faster-whisper. Ingenting lämnar din maskin.
- **Dokument, PDF-filer, bilder** — skickas till din AI-assistent för semantisk extraktion (via `/graphify`-skillen, med vilken modell din IDE-session än kör). Huvudlös `graphify extract` kräver `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), en körande Ollama-instans (`OLLAMA_BASE_URL`), AWS-autentiseringsuppgifter via standardleverantörskedjan (Bedrock — ingen API-nyckel behövs, använder IAM), eller `claude` CLI-binären (Claude Code — ingen API-nyckel behövs, använder din Claude-prenumeration). Flaggan `--dedup-llm` använder samma nyckel.
- **Datalokalisering** — `graphify extract` autodetekterar vilken leverantör som ska användas baserat på vilken API-nyckel som är satt (prioritet: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). För kod med krav på datalokalisering, använd `--backend ollama` (helt lokalt) eller skicka en explicit `--backend`-flagga. Kimi (`MOONSHOT_API_KEY`) dirigeras till Moonshot AI-servrar i Kina.
- **Ingen telemetri**, ingen användningsspårning, ingen analys.
- **Frågeloggning** — varje anrop till `graphify query`, `graphify path`, `graphify explain` och MCP:s `query_graph` loggas till `~/.cache/graphify-queries.log` i JSON Lines-format (tidsstämpel, fråga, korpus, returnerade noder, varaktighet). Fullständiga delgrafsvar lagras **inte** som standard. Sätt `GRAPHIFY_QUERY_LOG_DISABLE=1` för att välja bort, eller `GRAPHIFY_QUERY_LOG=/dev/null` för att tysta utan att inaktivera kodvägen.

---

## Felsökning

**`graphify: command not found` efter installation**
CLI:et är installerat men dess bin-katalog finns inte i skalets `PATH`. Välj lösningen som matchar hur du installerade:
- **uv** (`uv tool install graphifyy`): kommandot hamnar i uv:s tool-bin-katalog (`~/.local/bin`), som en färsk macOS/zsh-installation ofta inte har i `PATH`. Kör `uv tool update-shell`, öppna sedan en ny terminal. (Hitta katalogen med `uv tool dir --bin`.)
- **pipx** (`pipx install graphifyy`): kör `pipx ensurepath`, öppna sedan en ny terminal.
- **pip** (`pip install graphifyy`): pip installerar skript till en användar-bin-katalog som kanske inte finns i `PATH` — lägg till `~/Library/Python/3.x/bin` (macOS) eller `~/.local/bin` (Linux) till din `PATH` i `~/.zshrc`/`~/.bashrc`, eller kör helt enkelt `python -m graphify`.

**`uvx graphify …` eller `uv tool run graphify …` misslyckas att slå upp `graphify`**
PyPI-paketet är `graphifyy`; `graphify` är bara kommandot det tillhandahåller. `uv tool run` behandlar det första ordet som ett *paketnamn*, så det letar efter ett paket som heter `graphify` och rapporterar `No solution found … no versions of graphify`. Namnge paketet explicit: `uvx --from graphifyy graphify install` (samma som `uv tool run --from graphifyy graphify install`). Eller kör `uv tool install graphifyy` en gång och anropa sedan `graphify` direkt.

**`uv run --with graphifyy python -m graphify` körs tyst mot en äldre installation**
`uv run` använder ditt *system*-Python, så om en äldre `graphifyy` också finns där (t.ex. en tidigare `pip install graphifyy`), kan Python hitta den kopian först på `sys.path`, och `--with graphifyy` åsidosätter den inte. Det körs utan fel, men du får den *gamla* versionens beteende — t.ex. ignoreras miljöåsidosättningar som `OPENAI_BASE_URL` tyst, så förfrågningar går till standard-endpointen och misslyckas med ett 401-fel som ser ut som en felaktig nyckel. Fingeravtrycket är en rad `warning: skill is from graphify <newer>, package is <older>` — det betyder att en annan installation laddades, inte bara en inaktuell skill. Kontrollera vilken kopia som faktiskt laddades:
```bash
python -c "import graphify; print(graphify.__file__)"
```
Kör sedan det installerade kommandot direkt (det använder den uv-hanterade kopian), eller släng den inaktuella systemkopian:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` fungerar men `graphify`-kommandot gör det inte**
Ditt skals `PATH` inkluderar inte bin-katalogen kommandot installerades till. Föredra `uv tool install` / `pipx install` framför ren `pip`, kör sedan `uv tool update-shell` / `pipx ensurepath` och öppna en ny terminal (se installationsanmärkningarna ovan).

**`/graphify .` orsakar "path not recognized" i PowerShell**
PowerShell behandlar ett inledande `/` som en sökvägsseparator. Använd `graphify .` (utan snedstreck) på Windows.

**Grafen har färre noder efter `--update` eller ombyggnad**
Om en refaktorering tog bort filer dröjer de gamla noderna kvar. Skicka `--force` (eller sätt `GRAPHIFY_FORCE=1`) för att skriva över även när ombyggnaden har färre noder.

**`extract` avslutas med "extraction was incomplete ... refusing to overwrite"**
När en extraktionspass kraschar eller en genomgång inte kan läsa hela korpusen, blir körningen mindre än en fullständig en, så `graphify extract` vägrar att skriva över en större befintlig graf med det partiella resultatet (för att skydda din `graph.json`). Åtgärda det underliggande felet och kör om, eller skicka `--allow-partial` för att skriva över ändå.

**Grafen har dubbletter av noder för samma entitet (spöke-dubbletter)**
Spöke-dubbletter (samma symbol som förekommer två gånger — en gång från AST-extraktion med en källplats, en gång från semantisk extraktion utan) sammanfogas nu automatiskt vid byggtillfället. Om du ser detta i en graf byggd före v0.8.33, kör en fullständig omextraktion för att städa upp:
```bash
graphify extract . --force
```

**Ollama får slut på VRAM / kontextfönstret överskrids**
KV-cache-fönstret storleksanpassas automatiskt men kan vara för stort för din GPU. Minska det:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**Varningarna `LLM returned invalid JSON` / `Unterminated string`**
Modellens JSON-svar nådde sin output-tokengräns och klipptes av mitt i en sträng. graphify återhämtar sig automatiskt (den delar upp chunken och extraherar om de två halvorna, och ett alltför stort enskilt dokument delas först upp vid rubrik-/styckegränser så att hela filen fortfarande täcks), så dessa varningar är brusiga men innebär ingen dataförlust. För att minska bruset, höj outputtaket eller minska varje chunks output:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
Med en molngateway som OpenRouter, föredra `--backend openai` (sätt `OPENAI_BASE_URL`) framför Ollama-shimmen — det är en renare OpenAI-kompatibel väg. Om modellen har sitt eget max-output-tak är det att sänka `--token-budget` den pålitliga spaken.

**Graf-HTML är för stor för att öppna i en webbläsare (>5000 noder)**
Hoppa över HTML-generering och använd JSON:en direkt:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**`graph.json` har konfliktmarkörer efter att två utvecklare committat samtidigt**
Kör `graphify hook install` — det sätter upp en git-mergedriver som union-mergar `graph.json` automatiskt så att konflikter aldrig uppstår.

**Extraktion returnerar tomma noder/kanter för dokument eller PDF-filer**
Dokument, PDF-filer och bilder kräver ett LLM-anrop — korpusar med bara kod behöver ingen nyckel. Kontrollera att din API-nyckel är satt och att backend är korrekt:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**Varning om skill-versionsmismatch i din IDE**
Din installerade graphify-version skiljer sig från skill-filen. Uppdatera:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**Claude Codes promptcache ogiltigförklaras efter varje `graphify extract`**
Graphify skriver utdatafiler (`graph.json`, `graphify-out/`) till arbetsytan. Om dessa sökvägar inte ignoreras ogiltigförklarar varje skrivning Claude Codes promptcache, vilket tvingar fram en fullständig omuppladdning i nästa tur till cache-skrivningspriser. Lägg till dem i `.claudeignore`:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## Fullständig kommandoreferens

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

> **Om community-namn:** inuti en agent (Claude Code, Gemini CLI) namnger agenten själv communities. När du kör det rena CLI:et namnger `cluster-only` dem automatiskt med den konfigurerade backend (inbyggd eller anpassad OpenAI-kompatibel leverantör) — skicka `--no-label` för att behålla `Community N`, eller kör `graphify label` för att (om)generera namn på begäran.

---

## Läs mer

- [Hur det fungerar](../how-it-works.md) — extraktionspipelinen, communitydetektering, konfidenspoängsättning, benchmarks
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — moduluppdelning, hur man lägger till ett språk
- [Valfria integrationer](../docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — boken om idéerna bakom graphify, arkitekturen från början till slut

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) är det alltid-på-lagret byggt ovanpå graphify — det tillämpar samma grafansats på hela din arbetskontext: möten, filer, dokument och kod, och uppdaterar kontinuerligt i bakgrunden.

Byggt för personer och team vars arbete lever utspritt över hundratals konversationer och dokument som de aldrig helt kan rekonstruera.

**[Gå med i väntelistan på graphify.com](https://graphify.com).** Gratis provperiod lanseras snart.

---

<details>
<summary>Bidra</summary>

### Utvecklingsmiljö

Projektet använder [uv](https://docs.astral.sh/uv/) för utvecklingsarbetsflödet. Installera det en gång, kör sedan:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

Verifiera den redigerbara installationen:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### Köra tester

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> Anmärkning för macOS: testsviten inkluderar både `sample.f90`- och `sample.F90`-fixturer. Dessa kolliderar på skiftlägesokänsliga HFS+/APFS-filsystem. Kör på Linux eller i en Docker-container om du behöver testa båda Fortran-varianterna samtidigt.

### Git-arbetsflöde

- Aktiv utveckling sker på grenen `v8`.
- Commit-stil: `fix: <description>` / `feat: <description>` / `docs: <description>`
- Innan du öppnar en PR, kör `uv run pytest tests/ -q` och bekräfta att den går igenom.
- Lägg till en fixturfil i `tests/fixtures/` och tester i `tests/test_languages.py` för varje ny språkextraktor.

### Vad man kan bidra med

**Genomarbetade exempel** är det mest användbara bidraget. Kör `/graphify` på en verklig korpus, spara utdatan till `worked/{slug}/`, skriv en ärlig `review.md` som täcker vad grafen fick rätt och fel, och öppna en PR.

**Extraktionsbuggar** — öppna ett issue med indatafilen, cache-posten (`graphify-out/cache/`), och vad som missades eller var fel.

Se [ARCHITECTURE.md](../../ARCHITECTURE.md) för modulansvar och hur man lägger till ett språk.

</details>
