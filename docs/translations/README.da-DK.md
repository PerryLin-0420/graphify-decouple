<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>En fork af <a href="https://github.com/Graphify-Labs/graphify">graphify</a>, der tilføjer <code>graphify decouple</code></b> — 0-LLM, risikoscorede Extract-Class-kandidater til God Objects, genverificeret mod den faktiske kildekode (ikke kun kaldgrafen), før noget bliver anbefalet. Se <a href="#decouple-risikoscorede-extract-class-kandidater">Decouple: risikoscorede Extract-Class-kandidater</a> nedenfor.
</p>

<div align="center">
<details><summary><b>Læs dette på andre sprog</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>Tidlig adgang til graphify-platformen er åben før den offentlige v1-lancering: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

Skriv `/graphify` i din AI-kodeassistent, og den kortlægger hele dit projekt (kode, dokumenter, PDF'er, billeder, video) til en **vidensgraf**, du kan **forespørge i stedet for at grep'e** dig gennem filer.

- **Kodekort er gratis og fuldt lokale.** Kode parses med tree-sitter AST: deterministisk, uden LLM, intet forlader din maskine. (Dokumenter, PDF'er, billeder og video bruger din assistents model, eller en konfigureret API-nøgle, til et semantisk gennemløb.)
- **Hver kant er forklaret.** Hver forbindelse er mærket `EXTRACTED` (eksplicit i kilden) eller `INFERRED` (udledt af graphify), så du altid kan se, hvad der er læst direkte, og hvad der er udledt.
- **Ikke et vektorindeks.** Ingen embeddings, intet vektorlager: en reel graf, du kan gennemtraversere. Stil et spørgsmål, følg stien mellem to ting, eller forklar et enkelt begreb.

> Vil du have dette altid kørende og opdateret i baggrunden på tværs af din kode, dine dokumenter og dine møder i stedet for kun on demand? Det er det, vi bygger hos **[graphify.com](https://graphify.com)**, og tidlig adgang er åben nu på **[app.graphify.com](https://app.graphify.com/login)**.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="graphifys interaktive graph.html, der viser FastAPI-kodebasen som en kraftbaseret vidensgraf med en signaturforklaring over registrerede communities" width="900">
</p>
<p align="center">
  <em>FastAPI-kodebasen kortlagt af graphify. Hver node er et begreb, farverne er registrerede communities, og det hele kan klikkes på i graph.html.</em>
</p>

**Kom godt i gang** (30 sekunder):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

Derefter, i din AI-assistent:

```
/graphify .
```

Det er det. Du får **tre filer**:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**Virker i** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot og 15+ flere — [vælg din platform](#installation).

---

## Se det i praksis

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="graphify-stiforespørgsel: en terminal spørger om den korteste vej mellem FastAPI og ModelField, og svaret lyser op hop for hop hen over vidensgrafen" width="900">
</p>

Når grafen er bygget, forespørger du i den i stedet for at læse filer. Reelt output fra graphify kørt på FastAPI-kodebasen vist ovenfor:

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

Hver kant har en **konfidensmærkat** (`EXTRACTED` = eksplicit i kilden, `INFERRED` = udledt via resolution), så du altid kan se, hvad der er læst direkte, og hvad der er udledt. `graphify query "<question>"` returnerer en afgrænset delgraf for et spørgsmål i almindeligt sprog, og `graphify path A B` følger, hvordan to ting hænger sammen.

---

## Decouple: risikoscorede Extract-Class-kandidater

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: god-noden MainWindow splittes op i risikoscorede kandidatklasser, med en advarsel om delt tilstand mellem to af dem" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: MainWindows 5 foreslåede klasser, med Node Info-panelet åbent på Main Window Axis and Range Controls, der viser en tilstandsoverlapning på 0,608 med Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>DECOUPLE.html fra en reel kørsel — et klik på en foreslået klasse viser præcis, hvilken anden klasse den deler tilstand med, og hvad der konkret deles.</em>
</p>

Den samme side rendrer også selve opdelingen. Slår du **Preview decoupled view** til, bytter den god-klassens egne metoder ud med de foreslåede klasser og omlægger kanterne på stedet — selve ledningsændringen, ikke et gentegnet diagram:

| Før — god-klassen i dag | Efter — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html før toggle: en enkelt MainWindow-hubknude med sine egne metoder spredt rundt om sig" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html efter toggle: den samme knude reduceret til 5 rudeformede foreslåede klasser, grønne stiplede kanter der viser hvilke metoder der blev udtrukket til hver, og røde kanter der viser den delte instanstilstand mellem to af dem" width="440"> |
| Én knude med 47 af sine egne metoder, som hver især kun kan nås gennem klassen. | De foreslåede klasser. Grøn stiplet = hvad der blev udtrukket til hver; rød = den instanstilstand, som to af dem stadig deler, hvilket er præcis det, der afgør `split` kontra `keep_as_is`. Kun kandidater, der klarer risikotærsklen, tegnes — her 5 ud af 6, og derfor har én metode ingen rude at lande på. |

`graphify decouple` finder God Objects og fortæller dig, om det rent faktisk er værd at splitte dem op — ikke bare at de er store.

Den fejltype, dette findes for at fange: en klasse med 47 metoder, som kaldgraf-klyngedannelse med glæde splitter op i 5 pænt udseende grupper, som alle stadig læser og skriver til nøjagtig samme `self._chart_style` / `self._crosshair`-instanstilstand under overfladen. Udgiver du det split, har du ikke frikoblet noget — du har flyttet metoder over i nye filer, som stadig ikke kan testes, ændres eller forstås uafhængigt af hinanden, fordi de alle stadig skal have den samme delte tilstand givet tilbage. Et værktøj, der kun kigger på kaldgrafen, kan slet ikke se dette; det er nødvendigt at gå tilbage til den faktiske kildekode.

**To kontroller, begge 0-LLM, begge deterministiske:**

1. **Er dette overhovedet et God Object?** En node med høj grad (degree) kan enten være et ægte God Object (mange af sine EGNE metoder, spredt over urelaterede ansvarsområder — Extract Class er relevant) eller en overrefereret hub/datamodel (få egne metoder, mest *indgående* referencer — at splitte selve kroppen op gør ingenting; løsningen er at gøre interfacet smallere, ikke at udtrække en klasse). `classify_god_node` skelner mellem de to ved hjælp af `member_ratio`, ikke rå grad — den forskel, der forhindrer `TraceSource` (84 kanter, men kun 6 af sine egne metoder) i at få et falsk splitforslag, som `MainWindow` (88 kanter, 47 af sine egne metoder) korrekt får.
2. **Ville splittet rent faktisk reducere koblingen?** `risk_before` (god-nodens nuværende størrelse/kobling/fragmentering) sammenlignes med `risk_after` — den NYE risiko, som selve splittet ville introducere: tværgruppekald, der før var usynlige kanter inde i klassen, og som bliver til eksplicitte afhængigheder mellem klasser; kaldere, der nu ville skulle afhænge af mere end én ny klasse; og — den kontrol, en kaldgraf strukturelt ikke kan udføre — hvor meget `self`/`this`-instanstilstand (læsninger, skrivninger og delte hjælpemetodekald, vægtet separat: en delt **skrivning** scores højere end en delt læsning) de foreslåede grupper faktisk har til fælles. Dette genparser direkte god-nodens egen kildefil med tree-sitter; det er ikke afhængigt af graphifys eget udtrukne graf, som aldrig registrerer feltniveau-adgang for noget sprog. Kun når `risk_after` kommer under en tærskel i forhold til `risk_before`, anbefaler planen `split` — ellers er det `marginal` eller `keep_as_is`, og en frarådet kandidat rapporteres altid som et tal, aldrig tegnet som en figur, du selv skal vurdere med øjet.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

Skriver tre filer ud ved siden af `graph.json`:

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

**Sprogunderstøttelse for tilstandsdelings-kontrollen** (den rene kaldgraf-klassificering ovenfor fungerer for alle sprog, graphify kan udtrække; denne tabel handler specifikt om kildekode-genparsningen, der verificerer `self`/`this`-tilstandsoverlapning):

| Sprog | Understøttet | Noter |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` er sin egen AST-node, ikke en indpakket feltadgang — håndteres explicit |
| C# | ✅ | |
| Rust | ✅ | `self.x` via `impl`-blokke |
| Ruby | ✅ | `@x` (det dominerende idiom) + `self.foo`-kald |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | receiver-opløsning pr. metode — Go har intet `self`/`this`-nøgleord, så receiver-navnet (`f` i `func (f *Foo) M()`) opløses på ny for hver metode |
| C | ❌ | en struct-pointer-parameter har ingen syntaktisk markør, der skelner den fra enhver anden parameter — intet pålideligt signal uden fuld typeinferens |

En god-node i et ikke-understøttet sprog, eller en hvis kildekode ikke kan læses, markeres som `state_analysis: "skipped"` — klassificeringen og kaldgraf-scoren køres stadig, men anbefalingen bygger udelukkende på kaldgrafen i stedet for stiltiende at antage, at tilstandskontrollen bestod.

---

## Hvad det gør

Det, du får ud af boksen:

| Egenskab | Hvad du får |
|---|---|
| **God nodes** | De mest forbundne begreber, så du kan se, hvad alt strømmer igennem |
| **Communities** | Grafen opdelt i undersystemer (Leiden), med LLM-frie labels |
| **Tværfil-forbindelser** | `calls` / `imports` / `inherits` / `mixes_in` opløst på tværs af ~40 sprog via tree-sitter AST |
| **Query, path, explain** | Stil et spørgsmål, følg stien mellem to ting, eller forklar et enkelt begreb — alt sammen mod `graph.json` |
| **Begrundelse + dokumentreferencer** | `# NOTE:` / `# WHY:`-kommentarer samt ADR-/RFC-citater bliver til førsteklasses noder linket til koden |
| **Mere end kode** | Dokumenter, PDF'er, billeder og video/lyd kortlægges alle ind i den samme graf |
| **Lokal-først** | Kode parses lokalt med tree-sitter (ingen LLM, intet forlader din maskine); kun det semantiske gennemløb over dokumenter/medier kalder en backend, og kun hvis du konfigurerer én |

---

## Benchmarks

| Benchmark | Metrik | graphify | Feltet |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | QA-nøjagtighed | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | QA-nøjagtighed | **76%** | uafgjort med dense RAG |
| Grafopbygning | LLM-credits | **0** | pr. token for de fleste systemer |

Alle systemer blev kørt på den samme testrig med samme model og samme budgetter, bedømt af en dommer, der er blindvalideret mod en anden dommer (90,6 % overensstemmelse, Cohens kappa 0,81). Fulde tabeller pr. system, resultatet for kodeintelligens, og kommandoer til reproduktion: **[BENCHMARKS.md](../../BENCHMARKS.md)**.

---

## Forudsætninger

| Krav | Minimum | Tjek | Installer |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(anbefalet)* | enhver | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(alternativ)* | enhver | `pipx --version` | `pip install pipx` |

**Hurtig installation på macOS (Homebrew):**
```bash
brew install python@3.12 uv
```

**Hurtig installation på Windows:**
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

> **Officiel pakke:** PyPI-pakken hedder `graphifyy` (dobbelt-y). Andre `graphify*`-pakker på PyPI er ikke tilknyttet projektet. CLI-kommandoen er stadig `graphify`.

**Trin 1 — installer pakken:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**Trin 2 — registrer skillet hos din AI-assistent:**

```bash
graphify install
```

Det er det. Åbn din AI-assistent, og skriv `/graphify .`

For at installere assistent-skillet i det nuværende repository i stedet for din brugerprofil, tilføj `--project`:

```bash
graphify install --project
graphify install --project --platform codex
```

Projektafgrænsede installationer skriver under den nuværende mappe, for eksempel
`.claude/skills/graphify/SKILL.md` eller `.agents/skills/graphify/SKILL.md` (plus en
`references/`-sidefil, som skillet indlæser efter behov), og
udskriver et `git add`-tip for filer, der kan committes.
Platformspecifikke kommandoer, der understøtter projektafgrænsede installationer, accepterer det samme flag,
for eksempel `graphify claude install --project` eller `graphify codex install --project`.

> **PowerShell-bemærkning:** Brug `graphify .`, ikke `/graphify .` — den ledende skråstreg er en stiseparator i PowerShell.

> **`graphify: command not found`?** `uv tool install` / `pipx install` lægger `graphify`-kommandoen i deres eget værktøjs bin-mappe (`~/.local/bin`). Hvis din shell ikke kan finde den lige efter installationen — almindeligt på en frisk macOS + zsh-opsætning — er den mappe endnu ikke på din `PATH`: kør `uv tool update-shell` (eller `pipx ensurepath`), og åbn derefter en ny terminal. Med almindelig `pip` skal du tilføje `~/.local/bin` (Linux) eller `~/Library/Python/3.x/bin` (Mac) til din PATH, eller køre `python -m graphify`.

> **Kører du med `uvx` / `uv tool run` i stedet for at installere?** Angiv pakkenavnet, ikke kommandoen: `uvx --from graphifyy graphify install`. Almindelig `uvx graphify …` fejler (`No solution found … no versions of graphify`), fordi `uv tool run` læser det første ord som en *pakke*, og pakken hedder `graphifyy` — kommandoen `graphify` bor inde i den.

> **Undgå `pip install` på Mac/Windows**, hvis muligt. Skillet finder Python ved runtime fra `graphify-out/.graphify_python`; hvis den peger på et andet miljø end det, `pip` installerede pakken i, får du `ModuleNotFoundError: No module named 'graphify'`. `uv tool install` og `pipx install` isolerer pakken i deres eget miljø og undgår helt dette.

> **Git hooks og uv tool / pipx:** `graphify hook install` indlejrer den nuværende interpreter-sti direkte i hook-scripts ved installationstidspunktet, så post-commit-hooket udløses korrekt selv i GUI-git-klienter og CI-runnere, hvor `~/.local/bin` ikke er på PATH. Geninstallerer eller opgraderer du graphify, skal du køre `graphify hook install` igen for at opdatere den indlejrede sti.

> **Strict-tilstand (Claude Code):** `graphify install --project --strict` gør, at assistenten rent faktisk bruger grafen. Standardinstallationen *tilskynder* den til at køre `graphify query`, før den læser filer; strict-tilstand *blokerer* i stedet sessionens første rå læsning af kildekode og omdirigerer den til grafen, hvorefter den falder tilbage til den bløde tilskyndelse (så den udløses højst én gang pr. session og aldrig sætter sig fast). Skift ved runtime med `GRAPHIFY_HOOK_STRICT=1`/`0`; standardinstallationen er uændret (blød tilskyndelse).

<details>
<summary><b>Vælg din platform</b> (20+ assistenter, klik for at udvide)</summary>

| Platform | Installationskommando |
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

Codex-brugere skal desuden have `multi_agent = true` under `[features]` i `~/.codex/config.toml` for parallel udtrækning. CodeBuddy bruger samme Agent-værktøj og PreToolUse-hook-mekanisme som Claude Code. Factory Droid bruger `Task`-værktøjet til parallel afsendelse til subagenter. OpenClaw og Aider bruger sekventiel udtrækning (understøttelse af parallelle agenter er stadig tidligt på disse platforme). Trae bruger Agent-værktøjet til parallel afsendelse til subagenter og understøtter **ikke** `PreToolUse`-hooks, så AGENTS.md er den altid-aktive mekanisme.

`--platform agents` (alias `--platform skills`) retter sig mod de generiske cross-framework-placeringer for [Agent-Skills](https://github.com/anthropics/skills): specifikationens brugerglobale `~/.agents/skills/` (læst af `npx skills` og specifikationskompatible frameworks) til en global installation, og `./.agents/skills/` til en projektinstallation (`--project`). Den bare `graphify install` forbliver med vilje single-platform (Claude Code) — brug den navngivne `agents`-platform, når du vil have skillet synligt for ethvert framework, der læser `.agents/skills`.

> Codex bruger `$graphify` i stedet for `/graphify`.

</details>

<details>
<summary><b>Valgfrie tilføjelser</b> (installer kun det, du har brug for)</summary>

| Tilføjelse | Hvad den giver | Installer |
|---|---|---|
| `pdf` | PDF-udtrækning | `uv tool install "graphifyy[pdf]"` |
| `office` | Understøttelse af `.docx` og `.xlsx` | `uv tool install "graphifyy[office]"` |
| `google` | Rendering af Google Sheets | `uv tool install "graphifyy[google]"` |
| `video` | Video-/lydtranskription (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | MCP stdio-server | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Understøttelse af Neo4j-push | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | Understøttelse af FalkorDB-push | `uv tool install "graphifyy[falkordb]"` |
| `svg` | SVG-grafeksport | `uv tool install "graphifyy[svg]"` |
| `leiden` | Leiden community-detektion (kun Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Lokal Ollama-inferens | `uv tool install "graphifyy[ollama]"` |
| `openai` | OpenAI / OpenAI-kompatible API'er | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic Claude API (`--backend claude`, bruger `ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (bruger IAM, ingen API-nøgle) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, bruger `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "graphifyy[openai]"` |
| `sql` | SQL-skemaudtrækning | `uv tool install "graphifyy[sql]"` |
| `postgres` | Live PostgreSQL-introspektion (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | BYOND DreamMaker `.dm`/`.dme` AST-udtrækning (kan kræve en C-compiler + `python3-dev`, hvis der ikke findes et wheel til din platform) | `uv tool install "graphifyy[dm]"` |
| `terraform` | Terraform / HCL `.tf`/`.tfvars`/`.hcl` AST-udtrækning | `uv tool install "graphifyy[terraform]"` |
| `pascal` | Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` AST-udtrækning (mere præcise `calls`/`inherits`-kanter; falder tilbage til en regex-udtrækker, når den ikke er installeret) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | Kinesisk forespørgselssegmentering (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | Alt ovenstående | `uv tool install "graphifyy[all]"` |

</details>

---

## Få din assistent til altid at bruge grafen

Kør dette én gang i dit projekt, efter du har bygget en graf:

| Platform | Kommando |
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

Dette skriver en lille konfigurationsfil, der fortæller din assistent, at den skal konsultere vidensgrafen ved spørgsmål om kodebasen, og foretrække afgrænsede forespørgsler som `graphify query "<question>"` frem for at læse hele rapporten eller grep'e rå filer.

- **Hook-platforme** (Claude Code, Gemini CLI): et hook udløses automatisk før søgnings-lignende værktøjskald (og på Claude Code, før læsning af kildefiler én for én via Read-/Glob-værktøjerne) og tilskynder din assistent til at bruge grafens sti.
- **Instruktionsfil-platforme** (Codex, OpenCode, Cursor osv.): vedvarende instruktionsfiler (`AGENTS.md`, `.cursor/rules/` osv.) giver samme forespørgsel-først-vejledning.

`GRAPH_REPORT.md` er stadig tilgængelig til bred arkitekturgennemgang.

**CodeBuddy** gør samme to ting som Claude Code: skriver en `CODEBUDDY.md`-sektion, der fortæller CodeBuddy, at den skal læse `graphify-out/GRAPH_REPORT.md`, før den besvarer arkitekturspørgsmål, og installerer `PreToolUse`-hooks (`.codebuddy/settings.json`), der udløses før Bash-søgekommandoer og filhentninger, og tilskynder til at bruge `graphify query` i stedet.

**Codex** skriver til `AGENTS.md`, som er det, der faktisk bærer den altid-aktive graf-vejledning på denne platform. `graphify codex install` registrerer også et `PreToolUse`-hook i `.codex/hooks.json` (`graphify hook-check`), men den indgang er med vilje en **no-op**: Codex Desktop afviser `hookSpecificOutput.additionalContext` på `PreToolUse`, så at udsende en tilskyndelse dér ville ødelægge Bash-værktøjskald. I modsætning til Claude Code, hvor hooket (`graphify hook-guard`) faktisk tilskynder, udløses hooket på Codex, men gør med vilje ingenting, og `AGENTS.md` er den altid-aktive mekanisme.

**Kilo Code** installerer Graphify-skillet til `~/.config/kilo/skills/graphify/SKILL.md` og en indbygget `/graphify`-kommando til `~/.config/kilo/command/graphify.md`. `graphify kilo install` skriver også `AGENTS.md` plus et indbygget `tool.execute.before`-plugin (`.kilo/plugins/graphify.js` + registrering i `.kilo/kilo.json` eller `.kilo/kilo.jsonc`), så Kilo får samme altid-aktive graf-påmindelse gennem native `.kilo`-konfiguration.

**Cursor** skriver `.cursor/rules/graphify.mdc` med `alwaysApply: true`, så Cursor automatisk inkluderer den i hver samtale, uden at der er brug for et hook.

For at fjerne graphify fra alle platforme på én gang: `graphify uninstall` (tilføj `--purge` for også at slette `graphify-out/`). Eller brug den platformspecifikke kommando (f.eks. `graphify claude uninstall`).

---

## Hvad rapporten indeholder

- **Gudknuder** — de mest forbundne begreber i dit projekt. Alt strømmer igennem disse.
- **Overraskende forbindelser** — links mellem ting, der ligger i forskellige filer eller moduler. Rangeret efter, hvor uventede de er.
- **"Hvorfor'et"** — inline-kommentarer (`# NOTE:`, `# WHY:`, `# HACK:`), docstrings og designbegrundelse fra dokumenter udtrækkes som separate noder, linket til den kode, de forklarer.
- **Foreslåede spørgsmål** — 4-5 spørgsmål, som grafen er unikt positioneret til at besvare.
- **Konfidensmærkater** — hver udledt relation er mærket `EXTRACTED`, `INFERRED` eller `AMBIGUOUS`. Du ved altid, hvad der er fundet, og hvad der er gættet.

---

## Hvilke filer den håndterer

| Type | Filtyper |
|------|-----------|
| Kode (36 tree-sitter-grammatikker) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme` kræver `uv tool install graphifyy[dm]`; `.mts`/`.cts` genbruger TypeScript-grammatikken, `.cc`/`.cxx` samt CUDA `.cu`/`.cuh` og Metal `.metal` genbruger C++-grammatikken) |
| Salesforce Apex | `.cls .trigger` (regex-baseret; klasser, interfaces, enums, metoder, triggers, SOQL-/DML-kanter) |
| Terraform / HCL | `.tf .tfvars .hcl` (kræver `uv tool install graphifyy[terraform]`) |
| MCP-konfigurationer | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — udtrækker server-noder, pakkereferencer, krav til miljøvariabler |
| Pakkemanifester | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — én kanonisk pakke-node pr. pakke (efter navn) plus `depends_on`-kanter, så en pakke, der refereres fra mange manifester, er én samlet hub |
| Dokumenter | `.md .mdx .qmd .html .txt .rst .yaml .yml` (markdown-links `[text](./other.md)` og `[[wikilinks]]` bliver til `references`-kanter mellem dokumenter) |
| Office | `.docx .xlsx` (kræver `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (valgfrit; kræver `gws`-godkendelse og `--google-workspace`; Sheets kræver `uv tool install graphifyy[google]`) |
| PDF'er | `.pdf` |
| Billeder | `.png .jpg .webp .gif` |
| Video/lyd | `.mp4 .mov .mp3 .wav` og flere (kræver `uv tool install graphifyy[video]`) |
| YouTube/URL'er | enhver video-URL (kræver `uv tool install graphifyy[video]`) |

Kode udtrækkes **lokalt uden API-kald** (AST via tree-sitter). Alt andet går gennem din AI-assistents model-API.

Google Drive for desktops `.gdoc`-, `.gsheet`- og `.gslides`-filer er genvejspointere, ikke selve dokumentindholdet. For at inkludere native Google Docs, Sheets og Slides
i en headless udtrækning skal du installere og godkende
[`gws`-CLI'en](https://github.com/googleworkspace/cli) og derefter køre:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

Du kan også sætte `GRAPHIFY_GOOGLE_WORKSPACE=1`. Graphify eksporterer genveje til
`graphify-out/converted/` som Markdown-sidefiler og udtrækker derefter disse filer.

---

## Almindelige kommandoer

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
graphify prs 42                     # deep dive on PR #42 with graph impact
graphify prs --triage              # AI ranks your review queue (uses whatever backend is configured)
graphify prs --conflicts           # PRs sharing graph communities — merge-order risk

graphify decouple --project-root .   # risk-scored Extract-Class candidates for god objects
```

Se [Decouple: risikoscorede Extract-Class-kandidater](#decouple-risikoscorede-extract-class-kandidater) ovenfor, eller [den fulde kommandoreference](#fuld-kommandoreference) nedenfor.

---

## Ignorering af filer

Opret en `.graphifyignore` i roden af dit projekt — samme syntaks som `.gitignore`, inklusive `!`-negation.

**`.gitignore` respekteres automatisk.** graphify læser `.gitignore` i hver mappe. Findes der også en `.graphifyignore`, bliver de to **flettet sammen** — mønstre fra `.graphifyignore` evalueres sidst, så de vinder ved konflikter (inklusive `!`-negationer). At tilføje en `.graphifyignore` udelukker altid kun mere; den genindsætter aldrig en fil, din `.gitignore` allerede har udelukket. Afgrænsning til undermapper fungerer på samme måde som i git — en ignore-fil påvirker kun sit eget undertræ.

Send `--no-gitignore` til `graphify extract`, når git-ignoreret genereret eller transpileret kode hører til i grafen. Dette deaktiverer `.gitignore` og `.git/info/exclude`; `.graphifyignore` gælder stadig.

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

## Opsætning for teams

`graphify-out/` er tænkt til at blive committet til git, så alle på teamet starter med et kort.

**Anbefalede tilføjelser til `.gitignore`:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` er nu portabel — nøgler gemmes som relative stier og genankres ved indlæsning, så det er sikkert at committe filen, og det undgår en fuld genopbygning ved første checkout.

**Arbejdsgang:**
1. Én person kører `/graphify .` og committer `graphify-out/`.
2. Alle andre puller — deres assistent læser grafen med det samme.
3. Kør `graphify hook install` for at genopbygge automatisk efter hver commit (kun AST, ingen API-omkostning). Dette sætter også en git-merge-driver op, så `graph.json` aldrig efterlades med konfliktmarkører — to udviklere, der committer parallelt, får deres grafer union-flettet automatisk.
4. Når dokumenter eller artikler ændrer sig, kør `/graphify --update` for at opdatere de noder.

---

## Brug grafen direkte

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

MCP-serveren giver din assistent struktureret adgang: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Delt HTTP-server

`--transport stdio` (standard) starter én lokal server pr. udvikler. `--transport http` serverer de samme værktøjer over MCP Streamable HTTP-transporten, så én enkelt delt proces kan betjene grafen for hele teamet — klienter peger deres IDE's MCP-konfiguration på `http://<host>:8080/mcp` i stedet for at køre graphify lokalt.

| Flag | Standard | Formål |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Transport, der skal serveres over |
| `--host` | `127.0.0.1` | HTTP bind-host (brug `0.0.0.0` for at eksponere uden for localhost) |
| `--port` | `8080` | HTTP bind-port |
| `--api-key` | env `GRAPHIFY_API_KEY` | Kræv `Authorization: Bearer <key>` (eller `X-API-Key`) |
| `--path` | `/mcp` | HTTP-monteringssti |
| `--json-response` | fra | Returner ren JSON i stedet for SSE-streams |
| `--stateless` | fra | Ingen tilstand pr. session (til load-balancerede/CI-udrulninger) |
| `--session-timeout` | `3600` | Ryd inaktive stateful sessioner efter N sekunder (`0` deaktiverer) |

Standardbindingen `127.0.0.1` er kun loopback. Sæt `--host 0.0.0.0` **og** `--api-key` sammen, når den eksponeres på en delt host. Kør den i en container:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **WSL/Linux-bemærkning:** Ubuntu leveres med `python3`, ikke `python`. Brug et venv for at undgå konflikter:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## Miljøvariabler

Disse er kun nødvendige til **headless/CI-udtrækning** (`graphify extract`). Når du kører via `/graphify`-skillet i dit IDE, leveres model-API'en af din IDE-session — ingen ekstra nøgler nødvendige.

| Variabel | Bruges til | Hvornår krævet |
|---|---|---|
| `ANTHROPIC_API_KEY` | Claude (Anthropic)-backend | `--backend claude` |
| `ANTHROPIC_BASE_URL` | Anthropic-kompatibel endpoint-URL (LiteLLM-proxy, gateways, ...) | `--backend claude` (standard: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Modelnavn til Claude-backenden — brug det modelnavn/alias, din server eksponerer, til custom endpoints | `--backend claude` (standard: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` eller `GOOGLE_API_KEY` | Google Gemini-backend | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI eller OpenAI-kompatible API'er | `--backend openai` (lokale servere accepterer enhver ikke-tom værdi) |
| `OPENAI_BASE_URL` | OpenAI-kompatibel server-URL (llama.cpp, vLLM, LM Studio, ...) | `--backend openai` (standard: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | Modelnavn til OpenAI-backenden — brug det modelnavn/alias, din selv-hostede server eksponerer (tjek dens `/v1/models`-endpoint), til self-hosted servere, f.eks. `LFM2.5-8B-A1B-UD-Q4_K_XL` til llama.cpp | `--backend openai` (standard: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | DeepSeek-backend | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Kimi Code-backend | `--backend kimi` |
| `OLLAMA_BASE_URL` | URL til lokal Ollama-inferens | `--backend ollama` (standard: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Ollama-modelnavn | `--backend ollama` (standard: auto-detect) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Overstyr størrelsen på Ollamas KV-cache-vindue | valgfrit — auto-tilpasset som standard |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Minutter, Ollama-modellen skal forblive indlæst | valgfrit — sæt `0` for at aflæsse efter hver chunk |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI Service-backend | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | Azure-ressource-endpoint-URL | `--backend azure` (krævet sammen med API-nøglen) |
| `AZURE_OPENAI_API_VERSION` | Overstyring af Azure API-version | valgfrit — standard `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` eller `GRAPHIFY_AZURE_MODEL` | Azure-deploymentnavn | valgfrit — standard `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — standard credential-kæde | `--backend bedrock` (ingen API-nøgle, bruger IAM) |
| `GRAPHIFY_MAX_WORKERS` | Antal tråde til AST-parallelisme | valgfrit — også flaget `--max-workers` |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Hæv output-loftet for tætte korpora | valgfrit — f.eks. `32768` til store filer |
| `GRAPHIFY_API_TIMEOUT` | Timeout pr. kald i sekunder for HTTP-, claude-cli-, Anthropic SDK- og Bedrock-backends (standard: 600) | valgfrit — også flaget `--api-timeout` |
| `GRAPHIFY_MAX_RETRIES` | Hvor mange gange en rate-limitet (429) request skal forsøges igen, før der gives op (standard: 6; respekterer `Retry-After`) | valgfrit — hæv for strikse per-org-grænser (f.eks. kimi); `0` deaktiverer |
| `GRAPHIFY_FORCE` | Gennemtving genopbygning af grafen selv med færre noder | valgfrit — også flaget `--force` |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Aktivér automatisk Google Workspace-eksport | valgfrit — sæt til `1` |
| `GRAPHIFY_TRIAGE_BACKEND` | Backend til `graphify prs --triage` | valgfrit — auto-detekteret fra tilgængelige nøgler |
| `GRAPHIFY_TRIAGE_MODEL` | Modeloverstyring til triage | valgfrit — f.eks. `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | Sæt til `1` for at aktivere den lokale forespørgselslog på `~/.cache/graphify-queries.log` (registrerer hvert query-/path-/explain-spørgsmål + korpus-sti). Fra som standard — der skrives intet, før du selv aktiverer det (#1797) | valgfrit |
| `GRAPHIFY_QUERY_LOG` | Aktivér forespørgselsloggen, og skriv den til denne sti i stedet for standardstien | valgfrit — fra, med mindre denne eller `_ENABLE` er sat |
| `GRAPHIFY_QUERY_LOG_DISABLE` | Sæt til `1` for at tvangsdeaktivere forespørgselsloggen (vinder over enable-variablerne) | valgfrit |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | Registrer også fulde delgraf-svar, når loggen er aktiveret (fra som standard) | valgfrit |
| `GRAPHIFY_MAX_GRAPH_BYTES` | Overstyr loftet på 512 MiB for graph.json-størrelse — f.eks. `700MB`, `2GB` eller rene bytes | valgfrit — nyttigt til meget store korpora |
| `GRAPHIFY_MAX_CONTEXTS` | Maksimalt antal ikke-standard projektgrafer, som én multi-projekt MCP-server bevarer | valgfrit — standard: `8`; ugyldige værdier bruger `8`, og værdier under `1` bruger `1` |
| `GRAPHIFY_LLM_TEMPERATURE` | Overstyr LLM-temperatur til semantisk udtrækning — f.eks. `0.7`, eller `none` for at udelade den | valgfrit — udelades automatisk for o1/o3/o4/gpt-5-ræsonneringsmodeller |

---

## Privatliv

- **Kodefiler** — behandles lokalt via tree-sitter. Intet forlader din maskine. Et rent kode-korpus kræver ingen API-nøgle — `graphify extract` køres fuldt offline. På et blandet repository kan du tilføje `--code-only` for kun at indeksere koden og springe de dokumenter/PDF'er/billeder over, der ellers ville kræve en LLM.
- **Video/lyd** — transskriberes lokalt med faster-whisper. Intet forlader din maskine.
- **Dokumenter, PDF'er, billeder** — sendes til din AI-assistent til semantisk udtrækning (via `/graphify`-skillet, med den model, din IDE-session kører). Headless `graphify extract` kræver `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), en kørende Ollama-instans (`OLLAMA_BASE_URL`), AWS-credentials via standard provider-kæden (Bedrock — ingen API-nøgle nødvendig, bruger IAM), eller `claude`-CLI-binæren (Claude Code — ingen API-nøgle nødvendig, bruger dit Claude-abonnement). Flaget `--dedup-llm` bruger samme nøgle.
- **Datalokation** — `graphify extract` auto-detekterer, hvilken udbyder der skal bruges, baseret på hvilken API-nøgle der er sat (prioritet: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). Til kode med krav om datalokation, brug `--backend ollama` (fuldt lokal) eller angiv et eksplicit `--backend`-flag. Kimi (`MOONSHOT_API_KEY`) routes til Moonshot AI's servere i Kina.
- **Ingen telemetri**, ingen brugssporing, ingen analytics.
- **Forespørgselslogning** — hvert kald til `graphify query`, `graphify path`, `graphify explain` og MCP'ens `query_graph` logges til `~/.cache/graphify-queries.log` i JSON Lines-format (tidsstempel, spørgsmål, korpus, antal returnerede noder, varighed). Fulde delgraf-svar gemmes **ikke** som standard. Sæt `GRAPHIFY_QUERY_LOG_DISABLE=1` for at framelde dig, eller `GRAPHIFY_QUERY_LOG=/dev/null` for at gøre den tavs uden at deaktivere selve kodestien.

---

## Begrænsninger og grænser

Det, graphify bevidst **ikke** gør, og hvor dens dækning stopper:

- **Ikke en semantisk/vektor-søgemaskine.** Grafen er strukturel — noder og typede kanter udledt fra kilden, ikke embeddings. `graphify query`/`path`/`explain` gennemtraverserer den struktur; de kan ikke vise en forbindelse, der ikke er repræsenteret som en kant, selvom den er "semantisk" beslægtet. Der findes ingen similarity-/nærmeste-nabo-fallback.
- **Dokumenter, PDF'er, billeder og headless video-/URL-udtrækning er ikke rent lokale.** Kun kode (tree-sitter AST) og video-/lydtranskription (faster-whisper) kører helt offline. Udtrækning af dokumenter/PDF'er/billeder kalder altid en LLM — din AI-assistents model via `/graphify`-skillet, eller en konfigureret backend-API-nøgle til headless `graphify extract`. Se [Privatliv](#privatliv) ovenfor for præcis, hvilket flag eller hvilken nøgle hver vej kræver.
- **Decouples kontrol af delt tilstand dækker ikke alle sprog.** C har intet pålideligt `self`/`this`-signal uden fuld typeinferens, så det er udelukket (se [sprogunderstøttelsestabellen](#decouple-risikoscorede-extract-class-kandidater) ovenfor). En god-node i et ikke-understøttet sprog, eller en hvis kildekode ikke kan læses, falder tilbage på en scoring, der udelukkende bygger på kaldgrafen (`state_analysis: "skipped"`), i stedet for en verificeret tilstandskontrol.
- **3D-dataflow-gulvet er en navneheuristik, ikke dataflow-/taint-analyse.** `data_floor`s detektion af I/O-grænser (parsere, loaders, læsere, skrivere, DB-/HTTP-klienter) matcher på navnekonventioner (`boundary_reason`); en grænse-node med et ukonventionelt navn kan overses, hvilket underdriver, hvor dybt resten af grafen ligger.
- **Konfidensmærkater er graphifys egen resolution-konfidens, ikke absolut sandhed.** `INFERRED`- og `AMBIGUOUS`-kanter er best-effort-resolutions og kan stadig være forkerte, især for stærkt dynamiske idiomer (refleksion, runtime-dispatch, metaprogrammering), som ingen statisk AST-gennemgang kan løse fuldstændigt.
- **HTML-visualisering og grafstørrelse har begge et loft.** `graph.html` / `DECOUPLE.html` springer generering over ved mere end 5.000 noder som standard (`MAX_NODES_FOR_VIZ`, kan hæves via `GRAPHIFY_VIZ_NODE_LIMIT`); `graph.json` selv er begrænset til 512 MiB (`GRAPHIFY_MAX_GRAPH_BYTES` til at overstyre). Brug `--no-viz` sammen med `query`/`path`/`explain` til korpora, der overstiger en af grænserne.
- **Bevidsthed på tværs af projekter er opt-in, ikke automatisk.** `graphify query` ser kun den ene graf, du peger den mod. Spørgsmål på tværs af flere repositories kræver, at du først eksplicit registrerer hvert projekt i den delte graf (`graphify global add`, begrænset til `GRAPHIFY_MAX_CONTEXTS` ikke-standard-kontekster pr. MCP-server) — graphify scanner aldrig selv din maskine for andre repositories.
- **Parallel multi-agent-udtrækning afhænger af platformen.** Det kræver assistent-side understøttelse af at starte subagenter (`multi_agent = true` under `~/.codex/config.toml` til Codex, Agent-/Task-værktøjet på Claude Code/CodeBuddy/Factory Droid/Trae). OpenClaw og Aider udtrækker i øjeblikket kun sekventielt.
- **Den delte MCP-HTTP-server binder som standard kun til loopback.** At nå den fra en anden maskine kræver eksplicit `--host 0.0.0.0` **og** `--api-key`; graphify håndterer hverken TLS eller anden autentificering end den ene bearer-token.
- **PowerShell fortolker en ledende `/` som en stiseparator.** `/graphify .` fejler derfor på Windows PowerShell, ikke på grund af en fejl i graphify — brug `graphify .` i stedet.

---

## Fejlfinding

**`graphify: command not found` efter installation**
CLI'en er installeret, men dens bin-mappe er ikke på din shells `PATH`. Vælg fixet ud fra, hvordan du installerede:
- **uv** (`uv tool install graphifyy`): kommandoen lander i uv's værktøjs bin-mappe (`~/.local/bin`), som en frisk macOS/zsh-opsætning ofte ikke har på `PATH`. Kør `uv tool update-shell`, og åbn så en ny terminal. (Find mappen med `uv tool dir --bin`.)
- **pipx** (`pipx install graphifyy`): kør `pipx ensurepath`, og åbn så en ny terminal.
- **pip** (`pip install graphifyy`): pip installerer scripts til en bruger-bin-mappe, der måske ikke er på `PATH` — tilføj `~/Library/Python/3.x/bin` (macOS) eller `~/.local/bin` (Linux) til din `PATH` i `~/.zshrc`/`~/.bashrc`, eller kør bare `python -m graphify`.

**`uvx graphify …` eller `uv tool run graphify …` fejler med at opløse `graphify`**
PyPI-pakken hedder `graphifyy`; `graphify` er kun den kommando, den leverer. `uv tool run` behandler det første ord som et *pakkenavn*, så den leder efter en pakke, der hedder `graphify`, og rapporterer `No solution found … no versions of graphify`. Angiv pakken eksplicit: `uvx --from graphifyy graphify install` (samme som `uv tool run --from graphifyy graphify install`). Eller kør `uv tool install graphifyy` én gang og kald derefter `graphify` direkte.

**`uv run --with graphifyy python -m graphify` kører i stilhed en ældre installation**
`uv run` bruger din *system*-Python, så hvis en ældre `graphifyy` også findes der (f.eks. fra en tidligere `pip install graphifyy`), kan Python finde den kopi først på `sys.path`, og `--with graphifyy` overstyrer den ikke. Den kører uden fejl, men du får den *gamle* versions opførsel — f.eks. bliver miljøoverstyringer som `OPENAI_BASE_URL` stille ignoreret, så requests rammer standard-endpointet og fejler med en 401, der ligner en forkert nøgle. Fingeraftrykket er en linje som `warning: skill is from graphify <newer>, package is <older>` — det betyder, at en anden installation blev indlæst, ikke bare et forældet skill. Tjek, hvilken kopi der faktisk blev indlæst:
```bash
python -c "import graphify; print(graphify.__file__)"
```
Kør derefter den installerede kommando direkte (den bruger den uv-managede kopi), eller fjern den forældede systemkopi:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` virker, men kommandoen `graphify` gør ikke**
Din shells `PATH` inkluderer ikke den bin-mappe, kommandoen blev installeret til. Foretræk `uv tool install` / `pipx install` frem for almindelig `pip`, kør så `uv tool update-shell` / `pipx ensurepath`, og åbn en ny terminal (se installationsnoterne ovenfor).

**`/graphify .` giver "path not recognized" i PowerShell**
PowerShell behandler en ledende `/` som en stiseparator. Brug `graphify .` (uden skråstreg) på Windows.

**Grafen har færre noder efter `--update` eller genopbygning**
Hvis en refaktorering slettede filer, hænger de gamle noder i. Send `--force` (eller sæt `GRAPHIFY_FORCE=1`) for at overskrive, selv når genopbygningen har færre noder.

**`extract` afsluttes med "extraction was incomplete ... refusing to overwrite"**
Når et udtrækningsforløb crasher, eller en gennemgang ikke kan læse hele korpusset, vil kørslen blive mindre end en komplet én, så `graphify extract` afviser at overskrive en eksisterende, større graf med det delvise resultat (dette beskytter din `graph.json`). Ret den underliggende fejl, og kør igen, eller send `--allow-partial` for at overskrive alligevel.

**Grafen har duplikerede noder for samme entitet (spøgelsesduplikater)**
Spøgelsesduplikater (samme symbol optræder to gange — én gang fra AST-udtrækning med en kildeplacering, én gang fra semantisk udtrækning uden) merges nu automatisk ved opbygning. Ser du dette i en graf bygget før v0.8.33, så kør en fuld genudtrækning for at rydde op:
```bash
graphify extract . --force
```

**Ollama løber tør for VRAM/overskrider context-vinduet**
KV-cache-vinduet auto-tilpasses, men kan være for stort til din GPU. Reducer det:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**Advarsler om `LLM returned invalid JSON` / `Unterminated string`**
Modellens JSON-svar ramte sit output-token-loft og blev afskåret midt i en streng. graphify gendanner automatisk (den splitter chunken og genudtrækker de to halvdele, og et for stort enkeltdokument bliver først skåret op ved overskrifts-/afsnitsgrænser, så hele filen stadig dækkes), så disse advarsler er støjende, men ikke datatab. For at reducere støjen, hæv output-loftet, eller gør hver chunks output mindre:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
Med en cloud-gateway som OpenRouter er `--backend openai` (sæt `OPENAI_BASE_URL`) at foretrække frem for Ollama-shimmet — det er en renere OpenAI-kompatibel vej. Har modellen sit eget max-output-loft, er det at sænke `--token-budget` det mest pålidelige greb.

**Graf-HTML er for stor til at åbne i en browser (>5000 noder)**
Spring HTML-generering over, og brug JSON direkte:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**`graph.json` har konfliktmarkører, efter to udviklere har committet på samme tid**
Kør `graphify hook install` — den sætter en git-merge-driver op, som union-fletter `graph.json` automatisk, så konflikter aldrig sker.

**Udtrækning returnerer tomme noder/kanter for dokumenter eller PDF'er**
Dokumenter, PDF'er og billeder kræver et LLM-kald — kode-only-korpora kræver ingen nøgle. Tjek, at din API-nøgle er sat, og at backenden er korrekt:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**Advarsel om skill-versionsmismatch i dit IDE**
Din installerede graphify-version er forskellig fra skill-filen. Opdater:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**Claude Codes prompt-cache invalideres efter hver `graphify extract`**
Graphify skriver output-filer (`graph.json`, `graphify-out/`) ind i workspacet. Er disse stier ikke ignoreret, invaliderer hver skrivning Claude Codes prompt-cache og gennemtvinger en fuld genupload til cache-skrivehastigheder i den næste tur. Tilføj dem til `.claudeignore`:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## Fuld kommandoreference

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

> **Community-navne:** inde i en agent (Claude Code, Gemini CLI) navngiver agenten selv communities. Når du kører den bare CLI, navngiver `cluster-only` dem automatisk med den konfigurerede backend (indbygget eller custom OpenAI-kompatibel udbyder) — send `--no-label` for at bevare `Community N`, eller kør `graphify label` for at (gen)generere navne on demand.

---

## Lær mere

- [Sådan fungerer det](../how-it-works.md) — udtrækningspipelinen, community-detektion, konfidensscoring, benchmarks
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — modulopdeling, hvordan man tilføjer et sprog
- [Valgfrie integrationer](../docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — bogen om ideerne bag graphify, arkitekturen fra ende til anden

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) er det altid-aktive lag bygget oven på graphify — det anvender den samme graf-tilgang på hele din arbejdskontekst: møder, filer, dokumenter og kode, med løbende opdatering i baggrunden.

Bygget til mennesker og teams, hvis arbejde lever spredt over hundreder af samtaler og dokumenter, de aldrig fuldt ud kan rekonstruere.

**[Tilmeld dig ventelisten på graphify.com](https://graphify.com).** Gratis prøveperiode lanceres snart.

---

<details>
<summary>Bidrag</summary>

### Udviklingsopsætning

Projektet bruger [uv](https://docs.astral.sh/uv/) til udviklingsworkflowet. Installer det én gang, og kør derefter:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

Verificer den editable installation:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### Kørsel af tests

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> macOS-bemærkning: testsuiten indeholder både `sample.f90`- og `sample.F90`-fixtures. Disse kolliderer på filsystemer, der ikke skelner mellem store og små bogstaver, som HFS+/APFS. Kør på Linux eller i en Docker-container, hvis du skal teste begge Fortran-varianter samtidig.

### Git-workflow

- Aktiv udvikling sker på `v8`-branchen.
- Commit-stil: `fix: <description>` / `feat: <description>` / `docs: <description>`
- Kør `uv run pytest tests/ -q`, og bekræft, at den passerer, før du åbner en PR.
- Tilføj en fixture-fil til `tests/fixtures/` og tests til `tests/test_languages.py` for enhver ny sprog-udtrækker.

### Hvad du kan bidrage med

**Worked examples** er det mest nyttige bidrag. Kør `/graphify` på et reelt korpus, gem outputtet i `worked/{slug}/`, skriv en ærlig `review.md`, der dækker, hvad grafen fik rigtigt og forkert, og åbn en PR.

**Fejl i udtrækningen** — åbn et issue med inputfilen, cache-elementet (`graphify-out/cache/`) og hvad der blev overset eller var forkert.

Se [ARCHITECTURE.md](../../ARCHITECTURE.md) for modulansvar og hvordan man tilføjer et sprog.

</details>
