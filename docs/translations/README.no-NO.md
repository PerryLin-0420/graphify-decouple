<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>En fork av <a href="https://github.com/Graphify-Labs/graphify">graphify</a> som legger til <code>graphify decouple</code></b> — 0-LLM, risikoscorede Extract-Class-kandidater for gudobjekter, verifisert på nytt mot selve kildekoden (ikke bare kallgrafen) før den anbefaler noe som helst. Se <a href="#decouple-risikoscorede-extract-class-kandidater">Decouple: risikoscorede Extract-Class-kandidater</a> nedenfor.
</p>

<div align="center">
<details><summary><b>Les dette på andre språk</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>Tidlig tilgang til graphify-plattformen er åpen før den offentlige v1-lanseringen: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

Skriv `/graphify` i AI-kodeassistenten din, og den kartlegger hele prosjektet ditt (kode, dokumenter, PDF-er, bilder, video) til en **kunnskapsgraf** du kan **spørre i stedet for å grepe** deg gjennom filer.

- **Kodekart gratis, helt lokalt.** Kode analyseres med tree-sitter AST: deterministisk, ingen LLM, ingenting forlater maskinen din. (Dokumenter, PDF-er, bilder og video bruker assistentens modell, eller en konfigurert API-nøkkel, for en semantisk gjennomgang.)
- **Hver kant er forklart.** Hver forbindelse er merket `EXTRACTED` (eksplisitt i kilden) eller `INFERRED` (utledet av graphify), slik at du kan se hva som ble lest direkte og hva som ble utledet.
- **Ikke en vektorindeks.** Ingen embeddings, ingen vektorlager: en ordentlig graf du kan navigere i. Still et spørsmål, spor stien mellom to ting, eller forklar ett konsept.

> Vil du ha dette alltid på, oppdatert i bakgrunnen tvers over koden, dokumentene og møtene dine, i stedet for bare på forespørsel? Det er det vi bygger hos **[graphify.com](https://graphify.com)**, og tidlig tilgang er åpen nå på **[app.graphify.com](https://app.graphify.com/login)**.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="graphifys interaktive graph.html som viser FastAPI-kodebasen som en kraftbasert kunnskapsgraf med en forklaring av oppdagede fellesskap" width="900">
</p>
<p align="center">
  <em>FastAPI-kodebasen kartlagt av graphify. Hver node er et konsept, fargene er oppdagede fellesskap, og hele greia er klikkbar i graph.html.</em>
</p>

**Kom i gang** (30 sekunder):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

Deretter, i AI-assistenten din:

```
/graphify .
```

Det er alt. Du får **tre filer**:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**Fungerer i** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot og 15+ til — [velg plattformen din](#installasjon).

---

## Se det i aksjon

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="graphify path-forespørsel: en terminal spør etter den korteste stien mellom FastAPI og ModelField, og svaret lyser opp hopp for hopp gjennom kunnskapsgrafen" width="900">
</p>

Når grafen er bygget, spør du den i stedet for å lese filer. Faktisk output, graphify kjørt på FastAPI-kodebasen vist ovenfor:

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

Hver kant har en **konfidensmerking** (`EXTRACTED` = eksplisitt i kilden, `INFERRED` = utledet av graphify), slik at du kan se hva som ble lest direkte og hva som ble utledet. `graphify query "<question>"` returnerer en avgrenset delgraf for et spørsmål på vanlig språk, og `graphify path A B` sporer hvordan to ting er koblet sammen.

---

## Decouple: risikoscorede Extract-Class-kandidater

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: MainWindow-gudnode splittes i risikoscorede kandidatklasser, med en advarsel om delt tilstand mellom to av dem" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: MainWindows 5 foreslåtte klasser, Node Info-panelet åpent for Main Window Axis and Range Controls, og viser et 0,608 tilstandsoverlapp med Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>DECOUPLE.html fra en reell kjøring (AutoCheck/Touchstone Explorer) — å klikke på en foreslått klasse viser nøyaktig hvilken annen klasse den deler tilstand med, og hva som konkret er delt.</em>
</p>

`graphify decouple` finner gudobjekter og forteller deg om det faktisk er verdt å splitte dem — ikke bare at de er store.

Feilmodusen dette skal fange opp: en klasse med 47 metoder som kallgraf-klustring gladelig splitter i 5 ryddig utseende grupper, som alle fortsatt leser og skriver akkurat samme `self._chart_style` / `self._crosshair`-instanstilstand under overflaten. Skip den splitten, og du har ikke frikoblet noe som helst — du har flyttet metoder inn i nye filer som fortsatt ikke kan testes, endres eller resonneres om uavhengig, fordi de alle fortsatt trenger den samme delte tilstanden gitt tilbake til seg. Et verktøy som bare ser på kallgrafen kan ikke se dette i det hele tatt; det må gå tilbake til selve kildekoden.

**To kontroller, begge 0-LLM, begge deterministiske:**

1. **Er dette faktisk et gudobjekt?** En node med høy grad kan være et ekte gudobjekt (mange av sine EGNE metoder, spredt over urelaterte ansvarsområder — Extract Class gjelder) eller en overrefererrt hub/datamodell (få egne metoder, mest *innkommende* referanser — å splitte kroppen gjør ingenting; løsningen er å smalne inn grensesnittet, ikke å trekke ut en klasse). `classify_god_node` skiller de to ved `member_ratio`, ikke rå grad — forskjellen som hindrer `TraceSource` (84 kanter, men bare 6 av sine egne metoder) fra å få et falskt splittforslag, mens `MainWindow` (88 kanter, 47 av sine egne metoder) korrekt får ett.
2. **Ville splitten faktisk redusere koblingen?** `risk_before` (gudnodens nåværende størrelse/kobling/fragmentering) sammenlignes med `risk_after` — den NYE risikoen splitten selv ville innføre: kryssgruppe-kall som var usynlige intra-klasse-kanter og blir eksplisitte inter-klasse-avhengigheter, kallere som nå må avhenge av mer enn én ny klasse, og — kontrollen en kallgraf strukturelt ikke kan gjøre — hvor mye `self`/`this`-instanstilstand (lesing, skriving og delte hjelpemetodekall, vektet separat: en delt **skriving** scores høyere enn en delt lesing) de foreslåtte gruppene faktisk har til felles. Dette re-parser gudnodens egen kildefil direkte med tree-sitter; det er ikke avhengig av graphifys egen ekstraherte graf, som aldri registrerer feltnivå-tilgang for noe språk. Bare når `risk_after` kommer under en terskel i forhold til `risk_before`, anbefaler planen `split` — ellers er det `marginal` eller `keep_as_is`, og en frarådet kandidat rapporteres som et tall, aldri tegnet som en form du må stille spørsmål ved med øyet.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

Skriver ut tre filer ved siden av `graph.json`:

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

**Språkdekning for tilstandsdelings-kontrollen** (den kallgraf-baserte klassifiseringen ovenfor fungerer for alle språk graphify ekstraherer; denne tabellen gjelder spesifikt kildekode-re-parsingen som verifiserer `self`/`this`-tilstandsoverlapp):

| Språk | Støttet | Merknader |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` er sin egen AST-node, ikke en innpakket feltaksess — håndtert eksplisitt |
| C# | ✅ | |
| Rust | ✅ | `self.x` via `impl`-blokker |
| Ruby | ✅ | `@x` (den dominerende idiomen) + `self.foo`-kall |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | per-metode mottaker-oppløsning — Go har ikke noe `self`/`this`-nøkkelord, så mottakernavnet (`f` i `func (f *Foo) M()`) løses opp på nytt for hver metode |
| C | ❌ | en struct-peker-parameter har ingen syntaktisk markør som skiller den fra noen annen parameter — ingen pålitelig signal uten full typeinferens |

En gudnode på et ustøttet språk, eller en hvis kildekode ikke kan leses, merkes `state_analysis: "skipped"` — klassifiseringen og kallgraf-scoren kjører fortsatt, men anbefalingen bygger da bare på kallgrafen i stedet for stilltiende å anta at tilstandskontrollen gikk gjennom.

---

## Hva den gjør

Det du får ut av boksen:

| Kapabilitet | Hva du får |
|---|---|
| **Gudnoder** | De mest tilkoblede konseptene, slik at du ser hva alt flyter gjennom |
| **Fellesskap** | Grafen delt inn i undersystemer (Leiden), med LLM-frie etiketter |
| **Kryssfil-lenker** | `calls` / `imports` / `inherits` / `mixes_in` løst opp over ~40 språk via tree-sitter AST |
| **Query, path, explain** | Still et spørsmål, spor stien mellom to ting, eller forklar ett konsept, alt mot `graph.json` |
| **Begrunnelse + dokumentreferanser** | `# NOTE:` / `# WHY:`-kommentarer og ADR/RFC-sitater blir førsteklasses noder lenket til koden |
| **Utover kode** | Dokumenter, PDF-er, bilder og video/lyd kartlegges alle inn i samme graf |
| **Lokal-først** | Kode analyseres lokalt med tree-sitter (ingen LLM, ingenting forlater maskinen din); bare den semantiske gjennomgangen av dokumenter/media kaller en backend, og bare hvis du konfigurerer én |

---

## Benchmarker

| Benchmark | Metrikk | graphify | Feltet |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | QA-nøyaktighet | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | QA-nøyaktighet | **76%** | likt med dense RAG |
| Grafbygging | LLM-kreditter | **0** | per token for de fleste systemer |

Alle systemene kjørte på samme rammeverk med samme modell og budsjetter, scoret av en dommer blindvalidert mot en annen dommer (90,6 % samsvar, Cohens kappa 0,81). Fullstendige per-system-tabeller, resultatet for kode-intelligens, og reproduksjonskommandoer: **[BENCHMARKS.md](../../BENCHMARKS.md)**.

---

## Forutsetninger

| Krav | Minimum | Kontroller | Installer |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(anbefalt)* | hvilken som helst | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(alternativ)* | hvilken som helst | `pipx --version` | `pip install pipx` |

**Rask installasjon på macOS (Homebrew):**
```bash
brew install python@3.12 uv
```

**Rask installasjon på Windows:**
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

## Installasjon

> **Offisiell pakke:** PyPI-pakken heter `graphifyy` (dobbel y). Andre `graphify*`-pakker på PyPI er ikke tilknyttet. CLI-kommandoen er fortsatt `graphify`.

**Steg 1 — installer pakken:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**Steg 2 — registrer ferdigheten hos AI-assistenten din:**

```bash
graphify install
```

Det er alt. Åpne AI-assistenten din og skriv `/graphify .`

For å installere assistent-ferdigheten i det nåværende repositoriet i stedet for brukerprofilen din, legger du til `--project`:

```bash
graphify install --project
graphify install --project --platform codex
```

Prosjektomfattede installasjoner skriver under den nåværende katalogen, for eksempel
`.claude/skills/graphify/SKILL.md` eller `.agents/skills/graphify/SKILL.md` (pluss en
`references/`-sidefil som ferdigheten laster ved behov), og
skriver ut et `git add`-hint for filer som kan committes.
Plattformspesifikke kommandoer som støtter prosjektomfattede installasjoner tar samme flagg,
for eksempel `graphify claude install --project` eller `graphify codex install --project`.

> **PowerShell-notat:** Bruk `graphify .` ikke `/graphify .` — den ledende skråstreken er et stiskilletegn i PowerShell.

> **`graphify: command not found`?** `uv tool install` / `pipx install` legger `graphify`-kommandoen i sin egen verktøy-bin-katalog (`~/.local/bin`). Hvis skallet ditt ikke finner den rett etter installasjon — vanlig på et nytt macOS + zsh-oppsett — er den katalogen ikke på `PATH` din enda: kjør `uv tool update-shell` (eller `pipx ensurepath`), og åpne deretter en ny terminal. Med vanlig `pip`, legg til `~/.local/bin` (Linux) eller `~/Library/Python/3.x/bin` (Mac) i `PATH`, eller kjør `python -m graphify`.

> **Kjører du med `uvx` / `uv tool run` i stedet for å installere?** Angi pakken, ikke kommandoen: `uvx --from graphifyy graphify install`. Vanlig `uvx graphify …` feiler (`No solution found … no versions of graphify`) fordi `uv tool run` leser det første ordet som en *pakke*, og pakken er `graphifyy` — kommandoen `graphify` lever inne i den.

> **Unngå `pip install` på Mac/Windows** hvis mulig. Ferdigheten løser opp Python ved kjøretid fra `graphify-out/.graphify_python`; hvis den peker på et annet miljø enn der `pip` installerte pakken, får du `ModuleNotFoundError: No module named 'graphify'`. `uv tool install` og `pipx install` isolerer pakken i sitt eget miljø og unngår dette fullstendig.

> **Git-hooks og uv tool / pipx:** `graphify hook install` bygger den nåværende tolkerens sti direkte inn i hook-skriptene ved installasjonstidspunktet, slik at post-commit-hooken utløses korrekt selv i GUI-git-klienter og CI-løpere der `~/.local/bin` ikke er på PATH. Hvis du reinstallerer eller oppgraderer graphify, kjør `graphify hook install` på nytt for å oppdatere den innebygde stien.

> **Strict-modus (Claude Code):** `graphify install --project --strict` gjør at assistenten faktisk bruker grafen. Standardinstallasjonen *oppfordrer* den bare til å kjøre `graphify query` før den leser filer; strict-modus *blokkerer* den første rå kildelesingen i en sesjon og omdirigerer den til grafen, og går deretter tilbake til den vanlige oppfordringen (så den utløses maks én gang per sesjon og setter seg aldri fast). Slå om ved kjøretid med `GRAPHIFY_HOOK_STRICT=1`/`0`; standardinstallasjonen er uendret (mild oppfordring).

<details>
<summary><b>Velg plattformen din</b> (20+ assistenter, klikk for å utvide)</summary>

| Plattform | Installasjonskommando |
|----------|----------------|
| Claude Code (Linux/Mac) | `graphify install` |
| Claude Code (Windows) | `graphify install` (oppdages automatisk) eller `graphify install --platform windows` |
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
| Agent Skills (tverrgående rammeverk) | `graphify install --platform agents` (alias `--platform skills`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify install --platform pi` |
| Cursor | `graphify cursor install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

Codex-brukere trenger også `multi_agent = true` under `[features]` i `~/.codex/config.toml` for parallell ekstraksjon. CodeBuddy bruker samme Agent-verktøy og PreToolUse-hook-mekanisme som Claude Code. Factory Droid bruker `Task`-verktøyet for parallell underagent-utsendelse. OpenClaw og Aider bruker sekvensiell ekstraksjon (støtte for parallelle agenter er fortsatt tidlig på disse plattformene). Trae bruker Agent-verktøyet for parallell underagent-utsendelse og støtter **ikke** `PreToolUse`-hooks, så AGENTS.md er den alltid-på-mekanismen.

`--platform agents` (alias `--platform skills`) retter seg mot de generiske, tverrgående [Agent-Skills](https://github.com/anthropics/skills)-plasseringene: spesifikasjonens brukerglobale `~/.agents/skills/` (lest av `npx skills` og spesifikasjons-kompatible rammeverk) for en global installasjon, og `./.agents/skills/` for en prosjektinstallasjon (`--project`). Den enkle `graphify install` forblir enkelt-plattform (Claude Code) med hensikt — bruk den navngitte `agents`-plattformen når du vil at ferdigheten skal kunne oppdages av et hvilket som helst rammeverk som leser `.agents/skills`.

> Codex bruker `$graphify` i stedet for `/graphify`.

</details>

<details>
<summary><b>Valgfrie tillegg</b> (installer bare det du trenger)</summary>

| Tillegg | Hva det legger til | Installer |
|---|---|---|
| `pdf` | PDF-ekstraksjon | `uv tool install "graphifyy[pdf]"` |
| `office` | Støtte for `.docx` og `.xlsx` | `uv tool install "graphifyy[office]"` |
| `google` | Rendering av Google Sheets | `uv tool install "graphifyy[google]"` |
| `video` | Video-/lydtranskripsjon (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | MCP stdio-server | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Støtte for Neo4j-push | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | Støtte for FalkorDB-push | `uv tool install "graphifyy[falkordb]"` |
| `svg` | SVG-grafeksport | `uv tool install "graphifyy[svg]"` |
| `leiden` | Leiden-fellesskapsoppdagelse (bare Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Lokal Ollama-inferens | `uv tool install "graphifyy[ollama]"` |
| `openai` | OpenAI / OpenAI-kompatible API-er | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic Claude API (`--backend claude`, bruker `ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (bruker IAM, ingen API-nøkkel) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, bruker `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "graphifyy[openai]"` |
| `sql` | SQL-skjemaekstraksjon | `uv tool install "graphifyy[sql]"` |
| `postgres` | Live PostgreSQL-introspeksjon (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | BYOND DreamMaker `.dm`/`.dme` AST-ekstraksjon (kan kreve en C-kompilator + `python3-dev` hvis ingen wheel matcher plattformen din) | `uv tool install "graphifyy[dm]"` |
| `terraform` | Terraform / HCL `.tf`/`.tfvars`/`.hcl` AST-ekstraksjon | `uv tool install "graphifyy[terraform]"` |
| `pascal` | Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` AST-ekstraksjon (mer nøyaktige `calls`/`inherits`-kanter; faller tilbake til en regex-ekstraktor når den ikke er tilgjengelig) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | Kinesisk spørringssegmentering (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | Alt ovenfor | `uv tool install "graphifyy[all]"` |

</details>

---

## Få assistenten din til alltid å bruke grafen

Kjør dette én gang i prosjektet ditt etter å ha bygget en graf:

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
| Agent Skills (tverrgående rammeverk) | `graphify agents install` (alias `graphify skills install`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify pi install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

Dette skriver en liten konfigurasjonsfil som forteller assistenten din å konsultere kunnskapsgrafen for spørsmål om kodebasen, og foretrekke avgrensede forespørsler som `graphify query "<question>"` over å lese hele rapporten eller grepe rå filer.

- **Hook-plattformer** (Claude Code, Gemini CLI): en hook utløses automatisk før søkelignende verktøykall (og, på Claude Code, før kildefiler leses én etter én via Read/Glob-verktøyene) og oppfordrer assistenten din mot grafstien.
- **Instruksjonsfil-plattformer** (Codex, OpenCode, Cursor osv.): vedvarende instruksjonsfiler (`AGENTS.md`, `.cursor/rules/` osv.) gir samme spørring-først-veiledning.

`GRAPH_REPORT.md` er fortsatt tilgjengelig for bred arkitekturgjennomgang.

**CodeBuddy** gjør de samme to tingene som Claude Code: skriver en `CODEBUDDY.md`-seksjon som forteller CodeBuddy å lese `graphify-out/GRAPH_REPORT.md` før den svarer på arkitekturspørsmål, og installerer `PreToolUse`-hooks (`.codebuddy/settings.json`) som utløses før Bash-søkekommandoer og filesing, og oppfordrer til `graphify query` i stedet.

**Codex** skriver til `AGENTS.md`, som er det som faktisk bærer den alltid-på-grafveiledningen på denne plattformen. `graphify codex install` registrerer også en `PreToolUse`-hook i `.codex/hooks.json` (`graphify hook-check`), men denne oppføringen er bevisst en **no-op**: Codex Desktop avviser `hookSpecificOutput.additionalContext` på `PreToolUse`, så å sende en oppfordring der ville ødelagt Bash-verktøykall. I motsetning til Claude Code, der hooken (`graphify hook-guard`) faktisk gjør oppfordringen, utløses hooken på Codex og gjør bevisst ingenting, og `AGENTS.md` er den alltid-på-mekanismen.

**Kilo Code** installerer Graphify-ferdigheten til `~/.config/kilo/skills/graphify/SKILL.md` og en native `/graphify`-kommando til `~/.config/kilo/command/graphify.md`. `graphify kilo install` skriver også `AGENTS.md` pluss en native `tool.execute.before`-plugin (`.kilo/plugins/graphify.js` + registrering i `.kilo/kilo.json` eller `.kilo/kilo.jsonc`), slik at Kilo får samme alltid-på-graf-påminnelse gjennom native `.kilo`-konfigurasjon.

**Cursor** skriver `.cursor/rules/graphify.mdc` med `alwaysApply: true`, slik at Cursor inkluderer det i hver samtale automatisk, uten behov for en hook.

For å fjerne graphify fra alle plattformer på én gang: `graphify uninstall` (legg til `--purge` for også å slette `graphify-out/`). Eller bruk den plattformspesifikke kommandoen (f.eks. `graphify claude uninstall`).

---

## Hva rapporten inneholder

- **Gudnoder** — de mest tilkoblede konseptene i prosjektet ditt. Alt flyter gjennom disse.
- **Overraskende forbindelser** — lenker mellom ting som lever i forskjellige filer eller moduler. Rangert etter hvor uventede de er.
- **«Hvorfor»** — innebygde kommentarer (`# NOTE:`, `# WHY:`, `# HACK:`), docstrings og designbegrunnelse fra dokumenter blir ekstrahert som separate noder lenket til koden de forklarer.
- **Foreslåtte spørsmål** — 4–5 spørsmål grafen er unikt posisjonert til å besvare.
- **Konfidensmerker** — hvert utledet forhold er merket `EXTRACTED`, `INFERRED` eller `AMBIGUOUS`. Du vet alltid hva som ble funnet versus gjettet.

---

## Hvilke filer den håndterer

| Type | Filtyper |
|------|-----------|
| Kode (36 tree-sitter-grammatikker) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme` krever `uv tool install graphifyy[dm]`; `.mts`/`.cts` gjenbruker TypeScript-grammatikken, `.cc`/`.cxx` og CUDA `.cu`/`.cuh` og Metal `.metal` gjenbruker C++-grammatikken) |
| Salesforce Apex | `.cls .trigger` (regex-basert; klasser, grensesnitt, enumer, metoder, triggere, SOQL/DML-kanter) |
| Terraform / HCL | `.tf .tfvars .hcl` (krever `uv tool install graphifyy[terraform]`) |
| MCP-konfigurasjoner | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — ekstraherer servernoder, pakkereferanser, krav til miljøvariabler |
| Pakkemanifester | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — én kanonisk pakkenode per pakke (etter navn) pluss `depends_on`-kanter, slik at en pakke referert fra mange manifester blir én enkelt hub |
| Dokumenter | `.md .mdx .qmd .html .txt .rst .yaml .yml` (markdown `[text](./other.md)`-lenker og `[[wikilinks]]` blir `references`-kanter mellom dokumenter) |
| Office | `.docx .xlsx` (krever `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (opt-in; krever `gws`-autentisering og `--google-workspace`; Sheets krever `uv tool install graphifyy[google]`) |
| PDF-er | `.pdf` |
| Bilder | `.png .jpg .webp .gif` |
| Video / lyd | `.mp4 .mov .mp3 .wav` og flere (krever `uv tool install graphifyy[video]`) |
| YouTube / URL-er | hvilken som helst video-URL (krever `uv tool install graphifyy[video]`) |

Kode ekstraheres **lokalt uten API-kall** (AST via tree-sitter). Alt annet går gjennom AI-assistentens modell-API.

Google Drive for desktop-filer med `.gdoc`, `.gsheet` og `.gslides` er snarveispekere,
ikke selve dokumentinnholdet. For å inkludere native Google Docs, Sheets og Slides
i en hodeløs ekstraksjon, installer og autentiser
[`gws`-CLI-et](https://github.com/googleworkspace/cli), og kjør deretter:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

Du kan også sette `GRAPHIFY_GOOGLE_WORKSPACE=1`. Graphify eksporterer snarveier til
`graphify-out/converted/` som Markdown-sidefiler, og ekstraherer deretter disse filene.

---

## Vanlige kommandoer

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

Se [Decouple: risikoscorede Extract-Class-kandidater](#decouple-risikoscorede-extract-class-kandidater) ovenfor, eller [full kommandoreferanse](#full-kommandoreferanse) nedenfor.

---

## Ignorere filer

Lag en `.graphifyignore` i prosjektroten din — samme syntaks som `.gitignore`, inkludert `!`-negasjon.

**`.gitignore` respekteres automatisk.** graphify leser `.gitignore` i hver katalog. Hvis en `.graphifyignore` også finnes, blir de to **slått sammen** — `.graphifyignore`-mønstre evalueres sist, så de vinner ved konflikter (inkludert `!`-negasjoner). Å legge til en `.graphifyignore` utelukker bare mer; den inkluderer aldri på nytt en fil `.gitignore` allerede har utelatt. Underkatalogomfang fungerer på samme måte som i git — en ignore-fil påvirker bare sitt eget undertre.

Send `--no-gitignore` til `graphify extract` når git-ignorert generert eller transpilert kode skal være med i grafen. Dette deaktiverer `.gitignore` og `.git/info/exclude`; `.graphifyignore` gjelder fortsatt.

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

## Team-oppsett

`graphify-out/` er ment å committes til git, slik at alle i teamet starter med et kart.

**Anbefalte tillegg til `.gitignore`:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` er nå portabel — nøkler lagres som relative stier og forankres på nytt ved lasting, så det er trygt å committe den, og det unngår en full ombygging ved første checkout.

**Arbeidsflyt:**
1. Én person kjører `/graphify .` og committer `graphify-out/`.
2. Alle andre puller — assistenten deres leser grafen umiddelbart.
3. Kjør `graphify hook install` for automatisk ombygging etter hver commit (bare AST, ingen API-kostnad). Dette setter også opp en git-mergedriver, slik at `graph.json` aldri blir liggende med konfliktmarkører — to utviklere som committer parallelt får grafene sine union-sammenslått automatisk.
4. Når dokumenter eller artikler endres, kjør `/graphify --update` for å oppdatere disse nodene.

---

## Bruke grafen direkte

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

MCP-serveren gir assistenten din strukturert tilgang: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Delt HTTP-server

`--transport stdio` (standard) starter én lokal server per utvikler. `--transport http` tilbyr de samme verktøyene over MCP Streamable HTTP-transporten, slik at én delt prosess kan betjene grafen for hele teamet — klienter peker IDE-ens MCP-konfigurasjon mot `http://<host>:8080/mcp` i stedet for å kjøre graphify lokalt.

| Flagg | Standard | Formål |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Transport som skal betjenes på |
| `--host` | `127.0.0.1` | HTTP-bindevert (bruk `0.0.0.0` for å eksponere utover localhost) |
| `--port` | `8080` | HTTP-bindeport |
| `--api-key` | env `GRAPHIFY_API_KEY` | Krev `Authorization: Bearer <key>` (eller `X-API-Key`) |
| `--path` | `/mcp` | HTTP-monteringssti |
| `--json-response` | av | Returner ren JSON i stedet for SSE-strømmer |
| `--stateless` | av | Ingen sesjonstilstand (for lastbalanserte / CI-utrullinger) |
| `--session-timeout` | `3600` | Fjern inaktive tilstandsfulle sesjoner etter N sekunder (`0` deaktiverer) |

Standardbindingen `127.0.0.1` er kun loopback. Sett `--host 0.0.0.0` **og** `--api-key` sammen når du eksponerer på en delt vert. Kjør den i en container:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **WSL / Linux-notat:** Ubuntu leverer `python3`, ikke `python`. Bruk et venv for å unngå konflikter:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## Miljøvariabler

Disse er bare nødvendige for **hodeløs / CI-ekstraksjon** (`graphify extract`). Når du kjører via `/graphify`-ferdigheten inne i IDE-en din, blir modell-API-et levert av IDE-sesjonen din — ingen ekstra nøkler nødvendig.

| Variabel | Brukt til | Når nødvendig |
|---|---|---|
| `ANTHROPIC_API_KEY` | Claude (Anthropic)-backend | `--backend claude` |
| `ANTHROPIC_BASE_URL` | Anthropic-kompatibel endepunkt-URL (LiteLLM-proxy, gatewayer, ...) | `--backend claude` (standard: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Modellnavn for Claude-backend — for egendefinerte endepunkter, bruk modellnavnet/aliaset serveren din eksponerer | `--backend claude` (standard: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` eller `GOOGLE_API_KEY` | Google Gemini-backend | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI eller OpenAI-kompatible API-er | `--backend openai` (lokale servere aksepterer hvilken som helst ikke-tom verdi) |
| `OPENAI_BASE_URL` | OpenAI-kompatibel server-URL (llama.cpp, vLLM, LM Studio, ...) | `--backend openai` (standard: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | Modellnavn for OpenAI-backend — for selvhostede servere, bruk modellnavnet/aliaset serveren din eksponerer (sjekk `/v1/models`-endepunktet), f.eks. `LFM2.5-8B-A1B-UD-Q4_K_XL` for llama.cpp | `--backend openai` (standard: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | DeepSeek-backend | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Kimi Code-backend | `--backend kimi` |
| `OLLAMA_BASE_URL` | URL for lokal Ollama-inferens | `--backend ollama` (standard: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Ollama-modellnavn | `--backend ollama` (standard: automatisk oppdaging) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Overstyr Ollama KV-cache-vindusstørrelse | valgfritt — automatisk størrelse som standard |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Minutter Ollama-modellen skal holdes lastet | valgfritt — sett `0` for å losse etter hver chunk |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI Service-backend | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | Azure-ressursens endepunkt-URL | `--backend azure` (nødvendig sammen med API-nøkkel) |
| `AZURE_OPENAI_API_VERSION` | Overstyring av Azure API-versjon | valgfritt — standard `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` eller `GRAPHIFY_AZURE_MODEL` | Azure-utrullingsnavn | valgfritt — standard `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — standard credential-kjede | `--backend bedrock` (ingen API-nøkkel, bruker IAM) |
| `GRAPHIFY_MAX_WORKERS` | Antall AST-parallellitetstråder | valgfritt — også `--max-workers`-flagget |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Øk output-taket for tette korpus | valgfritt — f.eks. `32768` for store filer |
| `GRAPHIFY_API_TIMEOUT` | Timeout per kall i sekunder for HTTP-, claude-cli-, Anthropic SDK- og Bedrock-backender (standard: 600) | valgfritt — også `--api-timeout`-flagget |
| `GRAPHIFY_MAX_RETRIES` | Hvor mange ganger en rate-limitet (429) forespørsel skal gjentas før den gir opp (standard: 6; respekterer `Retry-After`) | valgfritt — øk for strenge per-org-grenser (f.eks. kimi); `0` deaktiverer |
| `GRAPHIFY_FORCE` | Tvungen grafombygging selv med færre noder | valgfritt — også `--force`-flagget |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Aktiver Google Workspace-eksport automatisk | valgfritt — sett til `1` |
| `GRAPHIFY_TRIAGE_BACKEND` | Backend for `graphify prs --triage` | valgfritt — automatisk oppdaget fra tilgjengelige nøkler |
| `GRAPHIFY_TRIAGE_MODEL` | Modelloverstyring for triage | valgfritt — f.eks. `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | Sett til `1` for å aktivere den lokale spørringsloggen på `~/.cache/graphify-queries.log` (registrerer hvert query/path/explain-spørsmål + korpussti). Av som standard — ingenting skrives med mindre du velger det aktivt (#1797) | valgfritt |
| `GRAPHIFY_QUERY_LOG` | Aktiver spørringsloggen og skriv den til denne stien i stedet for standarden | valgfritt — av med mindre denne eller `_ENABLE` er satt |
| `GRAPHIFY_QUERY_LOG_DISABLE` | Sett til `1` for å tvinge spørringsloggen av (vinner over enable-variablene) | valgfritt |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | Når loggen er aktivert, registrer også fullstendige delgraf-responser (av som standard) | valgfritt |
| `GRAPHIFY_MAX_GRAPH_BYTES` | Overstyr 512 MiB-grensen for graph.json-størrelse — f.eks. `700MB`, `2GB`, eller rene bytes | valgfritt — nyttig for svært store korpus |
| `GRAPHIFY_MAX_CONTEXTS` | Maksimalt antall ikke-standard prosjektgrafer som beholdes av én multi-prosjekt MCP-server | valgfritt — standard: `8`; ugyldige verdier bruker `8`, og verdier under `1` bruker `1` |
| `GRAPHIFY_LLM_TEMPERATURE` | Overstyr LLM-temperatur for semantisk ekstraksjon — f.eks. `0.7`, eller `none` for å utelate | valgfritt — utelates automatisk for o1/o3/o4/gpt-5-resonneringsmodeller |

---

## Personvern

- **Kodefiler** — behandlet lokalt via tree-sitter. Ingenting forlater maskinen din. Et rent kode-korpus krever ingen API-nøkkel — `graphify extract` kjører helt frakoblet. På et blandet repositorium, legg til `--code-only` for å bare indeksere koden og hoppe over dokumenter/PDF-er/bilder som ellers ville krevd en LLM.
- **Video / lyd** — transkribert lokalt med faster-whisper. Ingenting forlater maskinen din.
- **Dokumenter, PDF-er, bilder** — sendt til AI-assistenten din for semantisk ekstraksjon (via `/graphify`-ferdigheten, ved bruk av hvilken modell IDE-sesjonen din kjører). Hodeløs `graphify extract` krever `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), en kjørende Ollama-instans (`OLLAMA_BASE_URL`), AWS-legitimasjon via standard leverandørkjede (Bedrock — ingen API-nøkkel nødvendig, bruker IAM), eller `claude`-CLI-binæren (Claude Code — ingen API-nøkkel nødvendig, bruker Claude-abonnementet ditt). `--dedup-llm`-flagget bruker samme nøkkel.
- **Datalokasjon** — `graphify extract` oppdager automatisk hvilken leverandør som skal brukes basert på hvilken API-nøkkel som er satt (prioritet: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). For kode med krav til datalokasjon, bruk `--backend ollama` (helt lokalt) eller angi et eksplisitt `--backend`-flagg. Kimi (`MOONSHOT_API_KEY`) ruter til Moonshot AI-servere i Kina.
- **Ingen telemetri**, ingen bruksovervåking, ingen analyse.
- **Spørringslogging** — hvert `graphify query`-, `graphify path`-, `graphify explain`- og MCP `query_graph`-kall logges til `~/.cache/graphify-queries.log` i JSON Lines-format (tidsstempel, spørsmål, korpus, antall returnerte noder, varighet). Fullstendige delgraf-responser lagres **ikke** som standard. Sett `GRAPHIFY_QUERY_LOG_DISABLE=1` for å velge deg ut, eller `GRAPHIFY_QUERY_LOG=/dev/null` for å dempe uten å deaktivere kodestien.

---

## Feilsøking

**`graphify: command not found` etter installasjon**
CLI-et er installert, men bin-katalogen er ikke på skallets `PATH`. Velg fiksen for hvordan du installerte:
- **uv** (`uv tool install graphifyy`): kommandoen lander i uvs verktøy-bin-katalog (`~/.local/bin`), som et nytt macOS/zsh-oppsett ofte ikke har på `PATH`. Kjør `uv tool update-shell`, og åpne deretter en ny terminal. (Finn katalogen med `uv tool dir --bin`.)
- **pipx** (`pipx install graphifyy`): kjør `pipx ensurepath`, og åpne deretter en ny terminal.
- **pip** (`pip install graphifyy`): pip installerer skript til en bruker-bin-katalog som kanskje ikke er på `PATH` — legg til `~/Library/Python/3.x/bin` (macOS) eller `~/.local/bin` (Linux) til `PATH` din i `~/.zshrc`/`~/.bashrc`, eller bare kjør `python -m graphify`.

**`uvx graphify …` eller `uv tool run graphify …` klarer ikke å løse opp `graphify`**
PyPI-pakken heter `graphifyy`; `graphify` er bare kommandoen den tilbyr. `uv tool run` behandler det første ordet som et *pakkenavn*, så den ser etter en pakke kalt `graphify` og rapporterer `No solution found … no versions of graphify`. Angi pakken eksplisitt: `uvx --from graphifyy graphify install` (samme som `uv tool run --from graphifyy graphify install`). Eller kjør `uv tool install graphifyy` én gang og kall deretter `graphify` direkte.

**`uv run --with graphifyy python -m graphify` kjører stille en eldre installasjon**
`uv run` bruker *system*-Python-en din, så hvis en eldre `graphifyy` også ligger der (f.eks. en tidligere `pip install graphifyy`), kan Python finne den kopien først på `sys.path`, og `--with graphifyy` overstyrer den ikke. Den kjører uten feil, men du får den *gamle* versjonens oppførsel — f.eks. blir miljøoverstyringer som `OPENAI_BASE_URL` stille ignorert, slik at forespørsler treffer standardendepunktet og feiler med en 401 som ser ut som en dårlig nøkkel. Fingeravtrykket er en linje som `warning: skill is from graphify <newer>, package is <older>` — det betyr at en annen installasjon ble lastet, ikke bare en utdatert ferdighet. Sjekk hvilken kopi som faktisk ble lastet:
```bash
python -c "import graphify; print(graphify.__file__)"
```
Kjør deretter den installerte kommandoen direkte (den bruker den uv-administrerte kopien), eller fjern den utdaterte systemkopien:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` fungerer, men `graphify`-kommandoen gjør ikke det**
Skallets `PATH` inkluderer ikke bin-katalogen kommandoen ble installert til. Foretrekk `uv tool install` / `pipx install` over vanlig `pip`, kjør deretter `uv tool update-shell` / `pipx ensurepath` og åpne en ny terminal (se installasjonsnotatene ovenfor).

**`/graphify .` gir "path not recognized" i PowerShell**
PowerShell behandler en ledende `/` som et stiskilletegn. Bruk `graphify .` (uten skråstrek) på Windows.

**Grafen har færre noder etter `--update` eller ombygging**
Hvis en refaktorering slettet filer, blir de gamle nodene liggende. Send `--force` (eller sett `GRAPHIFY_FORCE=1`) for å overskrive selv når ombyggingen har færre noder.

**`extract` avsluttes med "extraction was incomplete ... refusing to overwrite"**
Når en ekstraksjonspassering krasjer eller en gjennomgang ikke kan lese hele korpuset fullt ut, blir kjøringen mindre enn en komplett en, så `graphify extract` nekter å overskrive en større eksisterende graf med det delvise resultatet (for å beskytte `graph.json` din). Fiks den underliggende feilen og kjør på nytt, eller send `--allow-partial` for å overskrive uansett.

**Grafen har dupliserte noder for samme entitet (spøkelsesdupliseringer)**
Spøkelsesdupliseringer (samme symbol som dukker opp to ganger — én gang fra AST-ekstraksjon med en kildeplassering, én gang fra semantisk ekstraksjon uten) slås nå automatisk sammen ved byggetidspunktet. Hvis du ser dette i en graf bygget før v0.8.33, kjør en full re-ekstraksjon for å rydde opp:
```bash
graphify extract . --force
```

**Ollama får tomt for VRAM / kontekstvinduet overskrides**
KV-cache-vinduet har automatisk størrelse, men kan være for stort for GPU-en din. Reduser det:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**`LLM returned invalid JSON` / `Unterminated string`-advarsler**
Modellens JSON-respons traff output-token-grensen og ble avkuttet midt i en streng. graphify gjenoppretter automatisk (den deler chunken og re-ekstraherer halvdelene, og et altfor stort enkeltdokument deles først opp ved overskrift-/avsnittsgrenser slik at hele filen fortsatt dekkes), så disse advarslene er støyende, men ikke datatap. For å redusere støyen, øk output-taket eller krymp hver chunks output:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
Med en skygateway som OpenRouter, foretrekk `--backend openai` (sett `OPENAI_BASE_URL`) over Ollama-shimmen — det er en renere OpenAI-kompatibel vei. Hvis modellen har sitt eget maks-output-tak, er å senke `--token-budget` det pålitelige virkemiddelet.

**Graf-HTML er for stor til å åpne i en nettleser (>5000 noder)**
Hopp over HTML-generering og bruk JSON-en direkte:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**`graph.json` har konfliktmarkører etter at to utviklere committer samtidig**
Kjør `graphify hook install` — det setter opp en git-mergedriver som union-sammenslår `graph.json` automatisk, slik at konflikter aldri oppstår.

**Ekstraksjon returnerer tomme noder/kanter for dokumenter eller PDF-er**
Dokumenter, PDF-er og bilder krever et LLM-kall — kode-bare korpus krever ingen nøkkel. Kontroller at API-nøkkelen din er satt og at backenden er riktig:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**Advarsel om ferdighetsversjonsmismatch i IDE-en din**
Den installerte graphify-versjonen din er forskjellig fra ferdighetsfilen. Oppdater:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**Claude Code sin prompt-cache blir ugyldiggjort etter hver `graphify extract`**
Graphify skriver output-filer (`graph.json`, `graphify-out/`) inn i arbeidsområdet. Hvis disse stiene ikke er ignorert, ugyldiggjør hver skriving Claude Codes prompt-cache, og tvinger en full re-opplasting ved cache-skrive-rater på neste tur. Legg dem til i `.claudeignore`:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## Full kommandoreferanse

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

> **Fellesskapsnavn:** inne i en agent (Claude Code, Gemini CLI) navngir agenten selv fellesskapene. Når du kjører det rene CLI-et, navngir `cluster-only` dem automatisk med den konfigurerte backenden (innebygd eller egendefinert OpenAI-kompatibel leverandør) — send `--no-label` for å beholde `Community N`, eller kjør `graphify label` for å (re)generere navn på forespørsel.

---

## Lær mer

- [Hvordan det fungerer](../how-it-works.md) — ekstraksjonspipelinen, fellesskapsoppdagelse, konfidensscoring, benchmarker
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — modulnedbryting, hvordan legge til et språk
- [Valgfrie integrasjoner](../docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — boken om ideene bak graphify, arkitekturen fra ende til ende

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) er alltid-på-laget bygget på toppen av graphify — det anvender samme grafbaserte tilnærming på hele arbeidskonteksten din: møter, filer, dokumenter og kode, oppdatert kontinuerlig i bakgrunnen.

Bygget for enkeltpersoner og team hvis arbeid lever over hundrevis av samtaler og dokumenter de aldri fullt ut kan rekonstruere.

**[Bli med på ventelisten på graphify.com](https://graphify.com).** Gratis prøveperiode lanseres snart.

---

<details>
<summary>Bidra</summary>

### Oppsett for utvikling

Prosjektet bruker [uv](https://docs.astral.sh/uv/) for utviklingsarbeidsflyten. Installer det én gang, og kjør deretter:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

Verifiser den redigerbare installasjonen (editable install):
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### Kjøre tester

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> macOS-notat: testsuiten inkluderer både `sample.f90`- og `sample.F90`-fixturer. Disse kolliderer på filsystemer som ikke skiller mellom store og små bokstaver, som HFS+ / APFS. Kjør på Linux eller i en Docker-container hvis du trenger å teste begge Fortran-variantene samtidig.

### Git-arbeidsflyt

- Aktiv utvikling skjer på `v8`-grenen.
- Commit-stil: `fix: <description>` / `feat: <description>` / `docs: <description>`
- Før du åpner en PR, kjør `uv run pytest tests/ -q` og bekreft at den passerer.
- Legg til en fixture-fil i `tests/fixtures/` og tester i `tests/test_languages.py` for hver ny språkekstraktor.

### Hva du kan bidra med

**Utarbeidede eksempler (worked examples)** er det mest nyttige bidraget. Kjør `/graphify` på et reelt korpus, lagre outputen til `worked/{slug}/`, skriv en ærlig `review.md` som dekker hva grafen fikk rett og hva den fikk feil, og åpne en PR.

**Ekstraksjonsfeil** — åpne en issue med inndatafilen, cache-oppføringen (`graphify-out/cache/`), og hva som ble oversett eller var feil.

Se [ARCHITECTURE.md](../../ARCHITECTURE.md) for modulansvar og hvordan legge til et språk.

</details>
