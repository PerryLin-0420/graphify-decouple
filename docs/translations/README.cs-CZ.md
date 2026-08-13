<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>Fork projektu <a href="https://github.com/Graphify-Labs/graphify">graphify</a>, který přidává <code>graphify decouple</code></b> — 0-LLM kandidáti na Extract Class pro god objects s hodnocením rizika, znovu ověření proti skutečnému zdrojovému kódu (ne jen proti call grafu), než cokoli doporučí. Viz <a href="#decouple-kandidáti-na-extract-class-s-hodnocením-rizika">Decouple: kandidáti na Extract Class s hodnocením rizika</a> níže.
</p>

<div align="center">
<details><summary><b>Číst v jiných jazycích</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>Předběžný přístup k platformě graphify je otevřený ještě před veřejným spuštěním v1: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

Napiš `/graphify` do svého AI programátorského asistenta a on zmapuje celý tvůj projekt (kód, dokumentaci, PDF, obrázky, videa) do **znalostního grafu**, který můžeš **dotazovat místo grepování** souborů.

- **Mapy kódu zdarma a plně lokálně.** Kód se parsuje pomocí tree-sitter AST: deterministicky, bez LLM, nic neopustí tvůj počítač. (Dokumentace, PDF, obrázky a video používají pro sémantický průchod model tvého asistenta nebo nakonfigurovaný API klíč.)
- **Každá hrana je vysvětlená.** Každé spojení je označené jako `EXTRACTED` (explicitní ve zdroji) nebo `INFERRED` (odvozené nástrojem graphify), takže poznáš, co bylo přečteno přímo a co odvozeno.
- **Není to vektorový index.** Žádné embeddingy, žádné vektorové úložiště: skutečný graf, kterým procházíš. Polož otázku, vystopuj cestu mezi dvěma věcmi nebo si nech vysvětlit jeden koncept.

> Chceš to mít trvale zapnuté, aktualizované na pozadí napříč kódem, dokumentací a schůzkami, a ne jen na vyžádání? Přesně to stavíme na **[graphify.com](https://graphify.com)** a předběžný přístup je nyní otevřený na **[app.graphify.com](https://app.graphify.com/login)**.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="interaktivní graph.html od graphify zobrazující codebase FastAPI jako silově orientovaný znalostní graf s legendou detekovaných komunit" width="900">
</p>
<p align="center">
  <em>Codebase FastAPI zmapovaná nástrojem graphify. Každý uzel je koncept, barvy jsou detekované komunity a celé je to klikatelné v graph.html.</em>
</p>

**Začni** (30 sekund):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

Poté ve svém AI asistentovi:

```
/graphify .
```

To je vše. Dostaneš **tři soubory**:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**Funguje v** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot a 15+ dalších — [vyber si svou platformu](#instalace).

---

## Podívej se, jak to funguje

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="dotaz graphify path: terminál se ptá na nejkratší cestu mezi FastAPI a ModelField a odpověď se krok po kroku rozsvěcuje napříč znalostním grafem" width="900">
</p>

Jakmile je graf postavený, dotazuješ se ho místo čtení souborů. Skutečný výstup, graphify spuštěný na codebase FastAPI zobrazené výše:

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

Každá hrana nese **značku spolehlivosti** (`EXTRACTED` = explicitní ve zdroji, `INFERRED` = odvozené při rozlišování), takže poznáš, co bylo přečteno přímo a co odvozeno. `graphify query "<question>"` vrátí ohraničený podgraf pro otázku v běžném jazyce a `graphify path A B` vystopuje, jak spolu dvě libovolné věci souvisí.

---

## Decouple: kandidáti na Extract Class s hodnocením rizika

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: god uzel MainWindow se dělí na kandidátské třídy s hodnocením rizika, s varováním o sdíleném stavu mezi dvěma z nich" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: 5 navržených tříd pro MainWindow, panel Node Info otevřený na Main Window Axis and Range Controls a zobrazující překryv stavu 0,608 s Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>DECOUPLE.html při skutečném běhu — kliknutí na navrženou třídu ukáže přesně, se kterou další třídou sdílí stav a co konkrétně je sdíleno.</em>
</p>

Tatáž stránka vykreslí i samotné rozdělení. Přepínač **Preview decoupled view** vymění vlastní metody god třídy za navržené třídy a přesměruje hrany na místě — jde o změnu zapojení, ne o překreslený diagram:

| Před — god třída dnes | Po — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html před přepnutím: jediný hub uzel MainWindow s vlastními metodami rozvětvenými okolo" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html po přepnutí: tentýž uzel zredukovaný na 5 kosočtvercových navržených tříd, zelené čárkované hrany ukazují, které metody byly vyextrahovány do které, červené hrany sdílený instanční stav mezi dvěma z nich" width="440"> |
| Jeden uzel držící 47 vlastních metod, z nichž každá je dostupná jen skrz tuto třídu. | Navržené třídy. Zeleně čárkovaně = co bylo do které vyextrahováno; červeně = instanční stav, který dvě z nich stále sdílejí, což je přesně to, co rozhoduje mezi `split` a `keep_as_is`. Vykreslují se pouze kandidáti, kteří překonají práh rizika — zde 5 ze 6, proto jedna metoda nemá kosočtverec, na kterém by přistála. |

`graphify decouple` najde god objects a řekne ti, jestli se jejich rozdělení skutečně vyplatí — ne jen to, že jsou velké.

Selhání, které má tento nástroj odhalit: třída se 47 metodami, kterou clustering nad call grafem s radostí rozdělí do 5 úhledně vypadajících skupin, jenže všechny pod povrchem stále čtou a zapisují přesně tentýž instanční stav `self._chart_style` / `self._crosshair`. Když takové rozdělení nasadíš, nic jsi neoddělil — jen jsi přesunul metody do nových souborů, které pořád nejde nezávisle testovat, měnit ani samostatně chápat, protože všechny stále potřebují tentýž sdílený stav předaný zpět. Nástroj, který se dívá jen na call graf, tohle vůbec nemůže vidět; musí se vrátit ke skutečnému zdrojovému kódu.

**Dvě kontroly, obě 0-LLM, obě deterministické:**

1. **Je tohle vůbec God Object?** Uzel s vysokým stupněm může být skutečný God Object (mnoho VLASTNÍCH metod rozprostřených přes nesouvisející odpovědnosti — Extract Class dává smysl) nebo přereferencovaný hub / datový model (málo vlastních metod, převážně *příchozí* reference — rozdělení jeho těla nic nepřinese; řešením je zúžení rozhraní, ne extrakce třídy). `classify_god_node` je rozliší podle `member_ratio`, ne podle holého stupně — právě ten rozdíl brání tomu, aby `TraceSource` (84 hran, ale jen 6 vlastních metod) dostal nesmyslný návrh na rozdělení, který `MainWindow` (88 hran, 47 vlastních metod) dostane právem.
2. **Snížilo by rozdělení skutečně provázanost?** `risk_before` (aktuální velikost/provázanost/fragmentace god uzlu) se porovnává s `risk_after` — NOVÝM rizikem, které by samotné rozdělení zavedlo: volání napříč skupinami, která byla dosud neviditelnými hranami uvnitř třídy a stanou se z nich explicitní závislosti mezi třídami, volající, kteří by nově museli záviset na více než jedné nové třídě, a — kontrola, kterou call graf strukturálně nedokáže provést — kolik instančního stavu `self`/`this` (čtení, zápisy a sdílená volání pomocných metod, vážené zvlášť: sdílený **zápis** je hodnocen výše než sdílené čtení) mají navržené skupiny skutečně společného. Tato kontrola znovu parsuje vlastní zdrojový soubor god uzlu přímo pomocí tree-sitter; nespoléhá na vlastní vyextrahovaný graf nástroje graphify, který přístup na úrovni polí nezaznamenává pro žádný jazyk. Pouze když `risk_after` klesne pod práh nižší než `risk_before`, doporučí plán `split` — jinak je výsledek `marginal` nebo `keep_as_is` a nedoporučený kandidát je vykázán jako číslo, nikdy nakreslen jako tvar, který bys musel očima zpochybňovat.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

Vytvoří tři soubory vedle `graph.json`:

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

**Jazykové pokrytí kontroly sdílení stavu** (klasifikace pouze nad call grafem popsaná výše funguje pro každý jazyk, který graphify extrahuje; tato tabulka se týká konkrétně opětovného parsování zdroje, které ověřuje překryv stavu `self`/`this`):

| Jazyk | Podporováno | Poznámky |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` je samostatný AST uzel, ne zabalený přístup k poli — ošetřeno explicitně |
| C# | ✅ | |
| Rust | ✅ | `self.x` přes bloky `impl` |
| Ruby | ✅ | `@x` (dominantní idiom) + volání `self.foo` |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | rozlišení receiveru pro každou metodu — Go nemá klíčové slovo `self`/`this`, takže se jméno receiveru (`f` v `func (f *Foo) M()`) rozlišuje znovu pro každou metodu |
| C | ❌ | parametr typu ukazatel na strukturu nemá žádný syntaktický znak, který by ho odlišil od jakéhokoli jiného parametru — bez plné typové inference žádný spolehlivý signál |

God uzel v nepodporovaném jazyce nebo takový, jehož zdroj nelze přečíst, je označen `state_analysis: "skipped"` — klasifikace i skóre nad call grafem stále proběhnou, ale doporučení se opírá pouze o call graf, místo aby se mlčky předpokládalo, že kontrola stavu prošla.

---

## Co to dělá

Co dostaneš rovnou z krabice:

| Schopnost | Co dostaneš |
|---|---|
| **God uzly** | Nejvíce propojené koncepty, takže vidíš, čím všechno protéká |
| **Komunity** | Graf rozdělený na podsystémy (Leiden), s popisky bez LLM |
| **Odkazy napříč soubory** | `calls` / `imports` / `inherits` / `mixes_in` rozlišené napříč ~40 jazyky pomocí tree-sitter AST |
| **Query, path, explain** | Polož otázku, vystopuj cestu mezi dvěma věcmi nebo si nech vysvětlit jeden koncept, vše nad `graph.json` |
| **Zdůvodnění + odkazy na dokumentaci** | Komentáře `# NOTE:` / `# WHY:` a citace ADR/RFC se stávají plnohodnotnými uzly propojenými s kódem |
| **Za hranicemi kódu** | Dokumentace, PDF, obrázky a video/audio se mapují do téhož grafu |
| **Local-first** | Kód se parsuje lokálně pomocí tree-sitter (žádné LLM, nic neopustí tvůj počítač); jen sémantický průchod nad dokumentací/médii volá backend, a to jen když si nějaký nakonfiguruješ |

---

## Benchmarky

| Benchmark | Metrika | graphify | Pole |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | QA accuracy | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | QA accuracy | **76%** | na stejné úrovni jako dense RAG |
| Stavba grafu | LLM kredity | **0** | u většiny systémů se platí za token |

Každý systém běžel na stejném harnessu se stejným modelem a rozpočty, hodnocený soudcem slepě validovaným proti druhému soudci (90,6% shoda, Cohenovo kappa 0,81). Kompletní tabulky pro jednotlivé systémy, výsledek code-intelligence a příkazy pro reprodukci: **[BENCHMARKS.md](../../BENCHMARKS.md)**.

---

## Předpoklady

| Požadavek | Minimum | Ověření | Instalace |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(doporučeno)* | jakákoli | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(alternativa)* | jakákoli | `pipx --version` | `pip install pipx` |

**Rychlá instalace na macOS (Homebrew):**
```bash
brew install python@3.12 uv
```

**Rychlá instalace na Windows:**
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

## Instalace

> **Oficiální balíček:** Balíček na PyPI se jmenuje `graphifyy` (dvě y). Ostatní balíčky `graphify*` na PyPI s tímto projektem nesouvisejí. CLI příkaz je stále `graphify`.

**Krok 1 — nainstaluj balíček:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**Krok 2 — zaregistruj skill u svého AI asistenta:**

```bash
graphify install
```

To je vše. Otevři svého AI asistenta a napiš `/graphify .`

Pokud chceš skill nainstalovat do aktuálního repozitáře místo do svého uživatelského
profilu, přidej `--project`:

```bash
graphify install --project
graphify install --project --platform codex
```

Instalace v rámci projektu zapisují do aktuálního adresáře, například do
`.claude/skills/graphify/SKILL.md` nebo `.agents/skills/graphify/SKILL.md` (plus
adresář `references/`, který si skill načte na vyžádání), a
vypíšou nápovědu `git add` pro soubory, které lze commitnout.
Příkazy pro jednotlivé platformy, které podporují instalaci v rámci projektu, přijímají tentýž přepínač,
například `graphify claude install --project` nebo `graphify codex install --project`.

> **Poznámka k PowerShellu:** Použij `graphify .`, ne `/graphify .` — úvodní lomítko je v PowerShellu oddělovač cesty.

> **`graphify: command not found`?** `uv tool install` / `pipx install` umístí příkaz `graphify` do svého bin adresáře pro nástroje (`~/.local/bin`). Pokud ho tvůj shell hned po instalaci nenajde — časté na čerstvém macOS + zsh — tento adresář ještě není v tvé `PATH`: spusť `uv tool update-shell` (nebo `pipx ensurepath`) a otevři nový terminál. U čistého `pip` přidej do PATH `~/.local/bin` (Linux) nebo `~/Library/Python/3.x/bin` (Mac), případně spouštěj `python -m graphify`.

> **Spouštíš to přes `uvx` / `uv tool run` místo instalace?** Uveď balíček, ne příkaz: `uvx --from graphifyy graphify install`. Prosté `uvx graphify …` selže (`No solution found … no versions of graphify`), protože `uv tool run` čte první slovo jako *balíček* a balíček se jmenuje `graphifyy` — příkaz `graphify` je uvnitř něj.

> **Vyhni se `pip install` na Macu/Windows**, pokud to jde. Skill si Python rozlišuje za běhu z `graphify-out/.graphify_python`; pokud to ukazuje na jiné prostředí, než kam `pip` balíček nainstaloval, dostaneš `ModuleNotFoundError: No module named 'graphify'`. `uv tool install` a `pipx install` balíček izolují do vlastního prostředí a tomuhle se úplně vyhnou.

> **Git hooky a uv tool / pipx:** `graphify hook install` vloží aktuální cestu k interpretu přímo do skriptů hooku už při instalaci, takže post-commit hook se správně spustí i v grafických git klientech a CI runnerech, kde `~/.local/bin` není v PATH. Pokud graphify přeinstaluješ nebo aktualizuješ, spusť `graphify hook install` znovu, aby se vložená cesta obnovila.

> **Striktní režim (Claude Code):** `graphify install --project --strict` zajistí, že asistent graf skutečně používá. Výchozí instalace ho jen *pošťouchne*, aby před čtením souborů spustil `graphify query`; striktní režim první surové čtení zdrojového souboru v relaci *zablokuje* a přesměruje ho na graf, poté se vrátí k pošťouchnutí (spustí se tedy nejvýš jednou za relaci a nikdy se nezasekne). Za běhu přepínej pomocí `GRAPHIFY_HOOK_STRICT=1`/`0`; výchozí instalace zůstává beze změny (jemné pošťouchnutí).

<details>
<summary><b>Vyber si svou platformu</b> (20+ asistentů, rozbal kliknutím)</summary>

| Platforma | Instalační příkaz |
|----------|----------------|
| Claude Code (Linux/Mac) | `graphify install` |
| Claude Code (Windows) | `graphify install` (automatická detekce) nebo `graphify install --platform windows` |
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
| Agent Skills (napříč frameworky) | `graphify install --platform agents` (alias `--platform skills`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify install --platform pi` |
| Cursor | `graphify cursor install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

Uživatelé Codexu navíc potřebují `multi_agent = true` pod `[features]` v `~/.codex/config.toml` pro paralelní extrakci. CodeBuddy používá stejný mechanismus Agent toolu a PreToolUse hooku jako Claude Code. Factory Droid používá pro paralelní odesílání subagentů nástroj `Task`. OpenClaw a Aider používají sekvenční extrakci (podpora paralelních agentů je na těchto platformách zatím v raném stavu). Trae používá pro paralelní odesílání subagentů Agent tool a **nepodporuje** hooky `PreToolUse`, takže trvale aktivním mechanismem je AGENTS.md.

`--platform agents` (alias `--platform skills`) cílí na obecná umístění [Agent-Skills](https://github.com/anthropics/skills) napříč frameworky: uživatelsky globální `~/.agents/skills/` podle specifikace (čte ho `npx skills` a frameworky odpovídající specifikaci) pro globální instalaci a `./.agents/skills/` pro instalaci v rámci projektu (`--project`). Samotné `graphify install` zůstává záměrně jednoplatformní (Claude Code) — pojmenovanou platformu `agents` použij, když chceš, aby skill našel jakýkoli framework čtoucí `.agents/skills`.

> Codex používá `$graphify` místo `/graphify`.

</details>

<details>
<summary><b>Volitelné extras</b> (instaluj jen to, co potřebuješ)</summary>

| Extra | Co přidává | Instalace |
|---|---|---|
| `pdf` | Extrakce PDF | `uv tool install "graphifyy[pdf]"` |
| `office` | Podpora `.docx` a `.xlsx` | `uv tool install "graphifyy[office]"` |
| `google` | Vykreslování Google Sheets | `uv tool install "graphifyy[google]"` |
| `video` | Přepis videa/audia (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | MCP stdio server | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Podpora push do Neo4j | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | Podpora push do FalkorDB | `uv tool install "graphifyy[falkordb]"` |
| `svg` | Export grafu do SVG | `uv tool install "graphifyy[svg]"` |
| `leiden` | Detekce komunit Leiden (jen Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Lokální inference přes Ollama | `uv tool install "graphifyy[ollama]"` |
| `openai` | OpenAI / API kompatibilní s OpenAI | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic Claude API (`--backend claude`, používá `ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (používá IAM, bez API klíče) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, používá `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "graphifyy[openai]"` |
| `sql` | Extrakce SQL schématu | `uv tool install "graphifyy[sql]"` |
| `postgres` | Živá introspekce PostgreSQL (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | AST extrakce BYOND DreamMaker `.dm`/`.dme` (může vyžadovat C kompilátor + `python3-dev`, pokud pro tvou platformu není wheel) | `uv tool install "graphifyy[dm]"` |
| `terraform` | AST extrakce Terraform / HCL `.tf`/`.tfvars`/`.hcl` | `uv tool install "graphifyy[terraform]"` |
| `pascal` | AST extrakce Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` (přesnější hrany `calls`/`inherits`; bez tohoto extras se použije regexový extraktor) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | Segmentace čínských dotazů (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | Vše výše uvedené | `uv tool install "graphifyy[all]"` |

</details>

---

## Ať tvůj asistent používá graf pořád

Spusť tohle jednou ve svém projektu poté, co jsi postavil graf:

| Platforma | Příkaz |
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
| Agent Skills (napříč frameworky) | `graphify agents install` (alias `graphify skills install`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify pi install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

Zapíše to malý konfigurační soubor, který tvému asistentovi říká, aby při otázkách na codebase konzultoval znalostní graf a dával přednost ohraničeným dotazům jako `graphify query "<question>"` před čtením celého reportu nebo grepováním surových souborů.

- **Platformy s hooky** (Claude Code, Gemini CLI): hook se automaticky spustí před voláními nástrojů typu vyhledávání (a v Claude Code i před čtením zdrojových souborů jeden po druhém přes nástroje Read/Glob) a nasměruje tvého asistenta k cestě přes graf.
- **Platformy s instrukčními soubory** (Codex, OpenCode, Cursor atd.): trvalé instrukční soubory (`AGENTS.md`, `.cursor/rules/` atd.) poskytují stejné vedení ve stylu „nejdřív dotaz".

`GRAPH_REPORT.md` je stále k dispozici pro širší architektonický přehled.

**CodeBuddy** dělá tytéž dvě věci jako Claude Code: zapíše sekci do `CODEBUDDY.md`, která CodeBuddy říká, aby před odpovídáním na architektonické otázky přečetl `graphify-out/GRAPH_REPORT.md`, a nainstaluje hooky `PreToolUse` (`.codebuddy/settings.json`), které se spustí před bashovými vyhledávacími příkazy a čtením souborů a nasměrují k `graphify query`.

**Codex** zapisuje do `AGENTS.md`, což je na této platformě to, co skutečně nese trvale aktivní vedení ke grafu. `graphify codex install` také zaregistruje hook `PreToolUse` v `.codex/hooks.json` (`graphify hook-check`), ale ten záznam je záměrně **no-op**: Codex Desktop odmítá `hookSpecificOutput.additionalContext` u `PreToolUse`, takže vypsání pošťouchnutí by rozbilo volání Bash nástroje. Na rozdíl od Claude Code, kde pošťouchnutí zajišťuje hook (`graphify hook-guard`), v Codexu se hook spustí a záměrně neudělá nic — trvale aktivním mechanismem je `AGENTS.md`.

**Kilo Code** nainstaluje skill Graphify do `~/.config/kilo/skills/graphify/SKILL.md` a nativní příkaz `/graphify` do `~/.config/kilo/command/graphify.md`. `graphify kilo install` navíc zapíše `AGENTS.md` plus nativní plugin `tool.execute.before` (`.kilo/plugins/graphify.js` + registrace v `.kilo/kilo.json` nebo `.kilo/kilo.jsonc`), takže Kilo získá stejné trvale aktivní připomínání grafu přes nativní konfiguraci `.kilo`.

**Cursor** zapíše `.cursor/rules/graphify.mdc` s `alwaysApply: true`, takže to Cursor automaticky zahrne do každé konverzace, žádný hook není potřeba.

Odebrání graphify ze všech platforem najednou: `graphify uninstall` (přidej `--purge`, aby se smazal i `graphify-out/`). Nebo použij příkaz pro konkrétní platformu (např. `graphify claude uninstall`).

---

## Co je v reportu

- **God uzly** — nejvíce propojené koncepty v tvém projektu. Všechno protéká skrz ně.
- **Překvapivá spojení** — odkazy mezi věcmi, které žijí v různých souborech nebo modulech. Seřazené podle toho, jak jsou nečekané.
- **To „proč"** — inline komentáře (`# NOTE:`, `# WHY:`, `# HACK:`), docstringy a designové zdůvodnění z dokumentace se extrahují jako samostatné uzly propojené s kódem, který vysvětlují.
- **Navržené otázky** — 4–5 otázek, na které je graf schopen odpovědět jako nikdo jiný.
- **Značky spolehlivosti** — každý odvozený vztah je označen `EXTRACTED`, `INFERRED` nebo `AMBIGUOUS`. Vždy víš, co bylo nalezeno a co odhadnuto.

---

## Jaké soubory zvládá

| Typ | Přípony |
|------|-----------|
| Kód (36 tree-sitter gramatik) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme` vyžaduje `uv tool install graphifyy[dm]`; `.mts`/`.cts` využívají gramatiku TypeScriptu, `.cc`/`.cxx` a CUDA `.cu`/`.cuh` a Metal `.metal` využívají gramatiku C++) |
| Salesforce Apex | `.cls .trigger` (na bázi regexu; třídy, rozhraní, enumy, metody, triggery, hrany SOQL/DML) |
| Terraform / HCL | `.tf .tfvars .hcl` (vyžaduje `uv tool install graphifyy[terraform]`) |
| Konfigurace MCP | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — extrahuje uzly serverů, odkazy na balíčky, požadavky na proměnné prostředí |
| Manifesty balíčků | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — jeden kanonický uzel balíčku na balíček (podle jména) plus hrany `depends_on`, takže balíček odkazovaný z mnoha manifestů je jediný hub |
| Dokumentace | `.md .mdx .qmd .html .txt .rst .yaml .yml` (markdownové odkazy `[text](./other.md)` a `[[wikilinks]]` se stávají hranami `references` mezi dokumenty) |
| Office | `.docx .xlsx` (vyžaduje `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (opt-in; vyžaduje autentizaci `gws` a `--google-workspace`; Sheets vyžadují `uv tool install graphifyy[google]`) |
| PDF | `.pdf` |
| Obrázky | `.png .jpg .webp .gif` |
| Video / audio | `.mp4 .mov .mp3 .wav` a další (vyžaduje `uv tool install graphifyy[video]`) |
| YouTube / URL | jakákoli URL videa (vyžaduje `uv tool install graphifyy[video]`) |

Kód se extrahuje **lokálně bez API volání** (AST přes tree-sitter). Všechno ostatní jde přes model API tvého AI asistenta.

Soubory `.gdoc`, `.gsheet` a `.gslides` z Google Drive pro desktop jsou
zástupci (ukazatele), ne obsah dokumentu. Chceš-li do headless extrakce zahrnout
nativní Google Docs, Sheets a Slides, nainstaluj a autentizuj
[`gws` CLI](https://github.com/googleworkspace/cli) a pak spusť:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

Můžeš také nastavit `GRAPHIFY_GOOGLE_WORKSPACE=1`. Graphify vyexportuje zástupce do
`graphify-out/converted/` jako markdownové sidecar soubory a ty pak extrahuje.

---

## Časté příkazy

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

Viz [Decouple: kandidáti na Extract Class s hodnocením rizika](#decouple-kandidáti-na-extract-class-s-hodnocením-rizika) výše, nebo [úplný přehled příkazů](#úplný-přehled-příkazů) níže.

---

## Ignorování souborů

Vytvoř `.graphifyignore` v kořeni projektu — stejná syntaxe jako `.gitignore`, včetně negace `!`.

**`.gitignore` je respektován automaticky.** graphify čte `.gitignore` v každém adresáři. Pokud je přítomen i `.graphifyignore`, oba se **sloučí** — vzory z `.graphifyignore` se vyhodnocují jako poslední, takže při konfliktu vyhrávají (včetně negací `!`). Přidání `.graphifyignore` může jen přidat vyloučení; nikdy znovu nezahrne soubor, který už `.gitignore` vyloučil. Rozsah v podadresářích funguje stejně jako v gitu — ignore soubor ovlivňuje jen svůj vlastní podstrom.

Předej `--no-gitignore` příkazu `graphify extract`, když do grafu patří i vygenerovaný nebo transpilovaný kód ignorovaný gitem. Tím se vypne `.gitignore` a `.git/info/exclude`; `.graphifyignore` stále platí.

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

## Nastavení pro tým

`graphify-out/` je určen k tomu, aby byl commitnutý do gitu, takže každý v týmu začíná s mapou.

**Doporučené doplňky do `.gitignore`:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` je nyní přenositelný — klíče jsou uloženy jako relativní cesty a při načtení se znovu ukotví, takže jeho commitnutí je bezpečné a předejde plnému přestavění při prvním checkoutu.

**Workflow:**
1. Jeden člověk spustí `/graphify .` a commitne `graphify-out/`.
2. Všichni ostatní pullnou — jejich asistent graf hned přečte.
3. Spusť `graphify hook install` pro automatické přestavění po každém commitu (jen AST, žádné náklady na API). Nastaví to také git merge driver, takže `graph.json` nikdy nezůstane s konfliktními značkami — dva vývojáři commitující paralelně dostanou své grafy automaticky sloučené sjednocením.
4. Když se změní dokumentace nebo články, spusť `/graphify --update` pro obnovení těchto uzlů.

---

## Přímé použití grafu

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

MCP server dá tvému asistentovi strukturovaný přístup: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Sdílený HTTP server

`--transport stdio` (výchozí) spouští jeden lokální server na vývojáře. `--transport http` poskytuje tytéž nástroje přes MCP Streamable HTTP transport, takže jediný sdílený proces může obsluhovat graf pro celý tým — klienti nasměrují MCP konfiguraci svého IDE na `http://<host>:8080/mcp` místo aby spouštěli graphify lokálně.

| Přepínač | Výchozí | Účel |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Transport, na kterém se obsluhuje |
| `--host` | `127.0.0.1` | HTTP bind host (použij `0.0.0.0` pro zpřístupnění mimo localhost) |
| `--port` | `8080` | HTTP bind port |
| `--api-key` | env `GRAPHIFY_API_KEY` | Vyžaduje `Authorization: Bearer <key>` (nebo `X-API-Key`) |
| `--path` | `/mcp` | HTTP mount cesta |
| `--json-response` | vypnuto | Vrací prosté JSON místo SSE streamů |
| `--stateless` | vypnuto | Žádný stav na relaci (pro nasazení za load balancerem / v CI) |
| `--session-timeout` | `3600` | Uklidí nečinné stavové relace po N sekundách (`0` vypíná) |

Výchozí bind `127.0.0.1` je jen loopback. Při zpřístupnění na sdíleném hostu nastav `--host 0.0.0.0` **a** `--api-key` společně. Spuštění v kontejneru:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **Poznámka k WSL / Linuxu:** Ubuntu dodává `python3`, ne `python`. Použij venv, aby ses vyhnul konfliktům:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## Proměnné prostředí

Tyto jsou potřeba pouze pro **headless / CI extrakci** (`graphify extract`). Při spuštění přes skill `/graphify` uvnitř tvého IDE poskytuje model API tvá IDE relace — žádné další klíče nejsou potřeba.

| Proměnná | Použití | Kdy je vyžadována |
|---|---|---|
| `ANTHROPIC_API_KEY` | Backend Claude (Anthropic) | `--backend claude` |
| `ANTHROPIC_BASE_URL` | URL endpointu kompatibilního s Anthropic (LiteLLM proxy, brány, …) | `--backend claude` (výchozí: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Jméno modelu pro backend Claude — u vlastních endpointů použij jméno/alias modelu, který tvůj server nabízí | `--backend claude` (výchozí: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` nebo `GOOGLE_API_KEY` | Backend Google Gemini | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI nebo API kompatibilní s OpenAI | `--backend openai` (lokální servery přijmou jakoukoli neprázdnou hodnotu) |
| `OPENAI_BASE_URL` | URL serveru kompatibilního s OpenAI (llama.cpp, vLLM, LM Studio, …) | `--backend openai` (výchozí: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | Jméno modelu pro backend OpenAI — u vlastních serverů použij jméno/alias modelu, který tvůj server nabízí (zkontroluj jeho endpoint `/v1/models`), např. `LFM2.5-8B-A1B-UD-Q4_K_XL` pro llama.cpp | `--backend openai` (výchozí: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | Backend DeepSeek | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Backend Kimi Code | `--backend kimi` |
| `OLLAMA_BASE_URL` | URL lokální inference Ollama | `--backend ollama` (výchozí: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Jméno modelu Ollama | `--backend ollama` (výchozí: automatická detekce) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Přepíše velikost okna KV cache pro Ollama | volitelné — ve výchozím stavu se dimenzuje automaticky |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Počet minut, po které zůstane model Ollama načtený | volitelné — nastav `0` pro uvolnění po každém chunku |
| `AZURE_OPENAI_API_KEY` | Backend Azure OpenAI Service | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | URL endpointu Azure zdroje | `--backend azure` (vyžadováno spolu s API klíčem) |
| `AZURE_OPENAI_API_VERSION` | Přepis verze Azure API | volitelné — výchozí `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` nebo `GRAPHIFY_AZURE_MODEL` | Jméno Azure deploymentu | volitelné — výchozí `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — standardní řetězec pověření | `--backend bedrock` (bez API klíče, používá IAM) |
| `GRAPHIFY_MAX_WORKERS` | Počet vláken pro paralelismus AST | volitelné — také přepínač `--max-workers` |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Zvýší strop výstupu pro husté korpusy | volitelné — např. `32768` pro velké soubory |
| `GRAPHIFY_API_TIMEOUT` | Timeout na volání v sekundách pro backendy HTTP, claude-cli, Anthropic SDK a Bedrock (výchozí: 600) | volitelné — také přepínač `--api-timeout` |
| `GRAPHIFY_MAX_RETRIES` | Kolikrát zopakovat požadavek omezený rate limitem (429), než to vzdá (výchozí: 6; respektuje `Retry-After`) | volitelné — zvyš u přísných limitů na organizaci (např. kimi); `0` vypíná |
| `GRAPHIFY_FORCE` | Vynutí přestavění grafu i při menším počtu uzlů | volitelné — také přepínač `--force` |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Automaticky zapne export Google Workspace | volitelné — nastav na `1` |
| `GRAPHIFY_TRIAGE_BACKEND` | Backend pro `graphify prs --triage` | volitelné — automaticky detekován z dostupných klíčů |
| `GRAPHIFY_TRIAGE_MODEL` | Přepis modelu pro triage | volitelné — např. `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | Nastav na `1` pro zapnutí lokálního logu dotazů v `~/.cache/graphify-queries.log` (zaznamenává každou otázku query/path/explain + cestu ke korpusu). Ve výchozím stavu vypnuto — nic se nezapisuje, dokud to sám nezapneš (#1797) | volitelné |
| `GRAPHIFY_QUERY_LOG` | Zapne log dotazů a zapíše ho na tuto cestu místo výchozí | volitelné — vypnuto, dokud není nastaveno toto nebo `_ENABLE` |
| `GRAPHIFY_QUERY_LOG_DISABLE` | Nastav na `1` pro vynucené vypnutí logu dotazů (má přednost před zapínacími proměnnými) | volitelné |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | Když je log zapnutý, zaznamenává navíc i celé odpovědi podgrafů (výchozí vypnuto) | volitelné |
| `GRAPHIFY_MAX_GRAPH_BYTES` | Přepíše strop velikosti graph.json 512 MiB — např. `700MB`, `2GB` nebo prosté bajty | volitelné — užitečné pro velmi rozsáhlé korpusy |
| `GRAPHIFY_MAX_CONTEXTS` | Maximální počet nevýchozích projektových grafů udržovaných jedním multiprojektovým MCP serverem | volitelné — výchozí: `8`; neplatné hodnoty použijí `8`, hodnoty pod `1` použijí `1` |
| `GRAPHIFY_LLM_TEMPERATURE` | Přepíše teplotu LLM pro sémantickou extrakci — např. `0.7`, nebo `none` pro vynechání | volitelné — u reasoning modelů o1/o3/o4/gpt-5 se automaticky vynechává |

---

## Soukromí

- **Soubory s kódem** — zpracovávají se lokálně přes tree-sitter. Nic neopustí tvůj počítač. Korpus obsahující jen kód nevyžaduje API klíč — `graphify extract` běží plně offline. U smíšeného repozitáře přidej `--code-only` pro indexaci pouze kódu a přeskočení dokumentace/PDF/obrázků, které by jinak potřebovaly LLM.
- **Video / audio** — přepisuje se lokálně pomocí faster-whisper. Nic neopustí tvůj počítač.
- **Dokumentace, PDF, obrázky** — posílají se tvému AI asistentovi k sémantické extrakci (přes skill `/graphify`, s modelem, který běží v tvé IDE relaci). Headless `graphify extract` vyžaduje `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), běžící instanci Ollama (`OLLAMA_BASE_URL`), AWS pověření přes standardní řetězec poskytovatelů (Bedrock — API klíč není potřeba, používá IAM), nebo binárku CLI `claude` (Claude Code — API klíč není potřeba, používá tvé předplatné Claude). Přepínač `--dedup-llm` používá tentýž klíč.
- **Umístění dat** — `graphify extract` automaticky detekuje, kterého poskytovatele použít podle toho, který API klíč je nastaven (priorita: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). Pro kód s požadavky na umístění dat použij `--backend ollama` (plně lokální) nebo předej explicitní přepínač `--backend`. Kimi (`MOONSHOT_API_KEY`) směruje na servery Moonshot AI v Číně.
- **Žádná telemetrie**, žádné sledování používání, žádná analytika.
- **Logování dotazů** — každé volání `graphify query`, `graphify path`, `graphify explain` a MCP `query_graph` se loguje do `~/.cache/graphify-queries.log` ve formátu JSON Lines (časová značka, otázka, korpus, vrácené uzly, doba trvání). Celé odpovědi podgrafů se ve výchozím stavu **neukládají**. Nastav `GRAPHIFY_QUERY_LOG_DISABLE=1` pro odhlášení, nebo `GRAPHIFY_QUERY_LOG=/dev/null` pro utišení bez vypnutí kódové cesty.

---

## Řešení potíží

**`graphify: command not found` po instalaci**
CLI je nainstalované, ale jeho bin adresář není v `PATH` tvého shellu. Vyber řešení podle toho, jak jsi instaloval:
- **uv** (`uv tool install graphifyy`): příkaz skončí v bin adresáři nástrojů uv (`~/.local/bin`), který čerstvý setup macOS/zsh často v `PATH` nemá. Spusť `uv tool update-shell` a otevři nový terminál. (Adresář najdeš pomocí `uv tool dir --bin`.)
- **pipx** (`pipx install graphifyy`): spusť `pipx ensurepath` a otevři nový terminál.
- **pip** (`pip install graphifyy`): pip instaluje skripty do uživatelského bin adresáře, který nemusí být v `PATH` — přidej `~/Library/Python/3.x/bin` (macOS) nebo `~/.local/bin` (Linux) do své `PATH` v `~/.zshrc`/`~/.bashrc`, nebo prostě spouštěj `python -m graphify`.

**`uvx graphify …` nebo `uv tool run graphify …` nedokáže vyřešit `graphify`**
Balíček na PyPI se jmenuje `graphifyy`; `graphify` je jen příkaz, který poskytuje. `uv tool run` bere první slovo jako *jméno balíčku*, takže hledá balíček jménem `graphify` a hlásí `No solution found … no versions of graphify`. Uveď balíček explicitně: `uvx --from graphifyy graphify install` (totéž jako `uv tool run --from graphifyy graphify install`). Nebo jednou spusť `uv tool install graphifyy` a pak volej `graphify` přímo.

**`uv run --with graphifyy python -m graphify` tiše spouští starší instalaci**
`uv run` používá tvůj *systémový* Python, takže pokud tam žije i starší `graphifyy` (např. z dřívějšího `pip install graphifyy`), Python může tuto kopii najít na `sys.path` dřív a `--with graphifyy` ji nepřebije. Běží to bez chyby, ale dostaneš chování *staré* verze — např. přepisy z prostředí jako `OPENAI_BASE_URL` se tiše ignorují, takže požadavky míří na výchozí endpoint a selžou s 401, který vypadá jako špatný klíč. Poznávacím znamením je řádek `warning: skill is from graphify <newer>, package is <older>` — to znamená, že se načetla jiná instalace, ne jen zastaralý skill. Zkontroluj, která kopie se skutečně načetla:
```bash
python -c "import graphify; print(graphify.__file__)"
```
Pak spusť nainstalovaný příkaz přímo (použije kopii spravovanou uv), nebo zahoď zastaralou systémovou kopii:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` funguje, ale příkaz `graphify` ne**
`PATH` tvého shellu neobsahuje bin adresář, do kterého byl příkaz nainstalován. Dej přednost `uv tool install` / `pipx install` před prostým `pip`, pak spusť `uv tool update-shell` / `pipx ensurepath` a otevři nový terminál (viz poznámky k instalaci výše).

**`/graphify .` způsobuje „path not recognized" v PowerShellu**
PowerShell bere úvodní `/` jako oddělovač cesty. Na Windows použij `graphify .` (bez lomítka).

**Graf má po `--update` nebo přestavění méně uzlů**
Pokud refaktoring smazal soubory, staré uzly přetrvávají. Předej `--force` (nebo nastav `GRAPHIFY_FORCE=1`), aby se přepsalo i tehdy, když má přestavěný graf méně uzlů.

**`extract` končí s „extraction was incomplete ... refusing to overwrite"**
Když průchod extrakce spadne nebo procházení nedokáže přečíst celý korpus, běh by byl menší než kompletní, takže `graphify extract` odmítá přepsat větší existující graf částečným výsledkem (chrání tvůj `graph.json`). Oprav příčinu selhání a spusť to znovu, nebo předej `--allow-partial` pro přepsání i tak.

**Graf má duplicitní uzly pro tutéž entitu (ghost duplicates)**
Ghost duplicates (tentýž symbol se objeví dvakrát — jednou z AST extrakce s umístěním ve zdroji, jednou ze sémantické extrakce bez něj) se nyní automaticky slučují při buildu. Pokud to vidíš v grafu postaveném před v0.8.33, spusť plnou reextrakci pro úklid:
```bash
graphify extract . --force
```

**Ollamě dochází VRAM / překročeno kontextové okno**
Okno KV cache se dimenzuje automaticky, ale může být pro tvou GPU příliš velké. Zmenši ho:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**Varování `LLM returned invalid JSON` / `Unterminated string`**
Odpověď modelu ve formátu JSON narazila na limit výstupních tokenů a byla useknutá uprostřed řetězce. graphify se automaticky zotaví (rozdělí chunk a extrahuje obě poloviny znovu a nadměrně velký jednotlivý dokument se nejprve rozřeže na hranicích nadpisů/odstavců, takže je celý soubor stále pokrytý), takže tato varování jsou hlučná, ale nejde o ztrátu dat. Pro snížení té práce navíc zvyš strop výstupu nebo zmenši výstup každého chunku:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
U cloudové brány jako OpenRouter dej přednost `--backend openai` (nastav `OPENAI_BASE_URL`) před Ollama shimem — je to čistší cesta kompatibilní s OpenAI. Pokud má model vlastní strop maximálního výstupu, spolehlivou pákou je snížení `--token-budget`.

**HTML grafu je příliš velké na otevření v prohlížeči (>5000 uzlů)**
Přeskoč generování HTML a použij JSON přímo:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**`graph.json` má konfliktní značky poté, co dva vývojáři commitli najednou**
Spusť `graphify hook install` — nastaví git merge driver, který `graph.json` automaticky slučuje sjednocením, takže ke konfliktům vůbec nedochází.

**Extrakce vrací prázdné uzly/hrany pro dokumentaci nebo PDF**
Dokumentace, PDF a obrázky vyžadují volání LLM — korpusy obsahující jen kód žádný klíč nepotřebují. Zkontroluj, že máš nastavený API klíč a správný backend:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**Varování o neshodě verze skillu ve tvém IDE**
Tvoje nainstalovaná verze graphify se liší od souboru se skillem. Aktualizuj:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**Prompt cache v Claude Code se invaliduje po každém `graphify extract`**
Graphify zapisuje výstupní soubory (`graph.json`, `graphify-out/`) do workspace. Pokud tyto cesty nejsou ignorované, každý zápis invaliduje prompt cache Claude Code a vynutí v dalším tahu plný re-upload za sazby zápisu do cache. Přidej je do `.claudeignore`:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## Úplný přehled příkazů

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

> **Jména komunit:** uvnitř agenta (Claude Code, Gemini CLI) pojmenovává komunity sám agent. Když spustíš holé CLI, `cluster-only` je automaticky pojmenuje nakonfigurovaným backendem (vestavěným nebo vlastním poskytovatelem kompatibilním s OpenAI) — předej `--no-label` pro zachování `Community N`, nebo spusť `graphify label` pro (znovu)vygenerování jmen na vyžádání.

---

## Další informace

- [Jak to funguje](../how-it-works.md) — pipeline extrakce, detekce komunit, hodnocení spolehlivosti, benchmarky
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — rozdělení modulů, jak přidat jazyk
- [Volitelné integrace](../docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — kniha o myšlenkách za graphify a o architektuře od začátku do konce

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) je trvale zapnutá vrstva postavená nad graphify — aplikuje stejný grafový přístup na celý tvůj pracovní kontext: schůzky, soubory, dokumentaci a kód, průběžně aktualizovaný na pozadí.

Postaveno pro lidi a týmy, jejichž práce se rozprostírá přes stovky konverzací a dokumentů, které nikdy nedokážou plně zrekonstruovat.

**[Zapiš se na čekací listinu na graphify.com](https://graphify.com).** Bezplatná zkušební verze startuje brzy.

---

<details>
<summary>Jak přispět</summary>

### Nastavení vývojového prostředí

Projekt používá pro vývojový workflow [uv](https://docs.astral.sh/uv/). Nainstaluj ho jednou a pak:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

Ověř editovatelnou instalaci:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### Spouštění testů

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> Poznámka k macOS: testovací sada obsahuje fixtures `sample.f90` i `sample.F90`. Ty na souborových systémech HFS+ / APFS nerozlišujících velikost písmen kolidují. Pokud potřebuješ testovat obě fortranské varianty současně, spusť testy na Linuxu nebo v Docker kontejneru.

### Git workflow

- Aktivní vývoj probíhá na větvi `v8`.
- Styl commitů: `fix: <description>` / `feat: <description>` / `docs: <description>`
- Před otevřením PR spusť `uv run pytest tests/ -q` a ověř, že projde.
- Pro každý nový jazykový extraktor přidej fixture soubor do `tests/fixtures/` a testy do `tests/test_languages.py`.

### Čím přispět

**Vypracované příklady** jsou nejužitečnějším přínosem. Spusť `/graphify` na skutečném korpusu, ulož výstup do `worked/{slug}/`, napiš poctivý `review.md` popisující, co graf zachytil správně a co špatně, a otevři PR.

**Chyby v extrakci** — otevři issue se vstupním souborem, položkou cache (`graphify-out/cache/`) a tím, co chybělo nebo bylo špatně.

Viz [ARCHITECTURE.md](../../ARCHITECTURE.md) pro odpovědnosti modulů a návod, jak přidat jazyk.

</details>
