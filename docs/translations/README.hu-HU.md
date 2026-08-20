<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>A <a href="https://github.com/Graphify-Labs/graphify">graphify</a> forkja, amely hozzáadja a <code>graphify decouple</code> parancsot</b> — 0-LLM, kockázatra pontozott Extract-Class jelöltek god objectekhez, amelyeket a tényleges forráskód (nem csak a call graph) ellen újra ellenőriz, mielőtt bármit is javasolna. Lásd a lenti <a href="#decouple-kockázatra-pontozott-extract-class-jelöltek">Decouple: kockázatra pontozott Extract-Class jelöltek</a> részt.
</p>

<div align="center">
<details><summary><b>Olvasd más nyelveken</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>A graphify platform korai hozzáférése nyitva áll a nyilvános v1 indulás előtt: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

Írd be a `/graphify` parancsot az AI kódolóasszisztensedbe, és az a teljes projektedet (kód, dokumentumok, PDF-ek, képek, videók) egy **tudásgráffá** képezi le, amelyet **lekérdezhetsz ahelyett, hogy fájlokban grepelnél**.

- **Ingyenes kódtérképek, teljesen lokálisan.** A kódot tree-sitter AST elemzi: determinisztikus, LLM nélkül, semmi nem hagyja el a gépedet. (A dokumentumok, PDF-ek, képek és videók a szemantikus futáshoz az asszisztensed modelljét vagy egy beállított API-kulcsot használnak.)
- **Minden él meg van magyarázva.** Minden kapcsolat `EXTRACTED` (kifejezetten szerepel a forrásban) vagy `INFERRED` (a graphify oldotta fel) címkét kap, így megkülönbözteted a közvetlenül kiolvasottat a következtetettől.
- **Nem vektorindex.** Nincsenek embeddingek, nincs vektortár: egy valódi gráf, amelyet bejársz. Tegyél fel egy kérdést, kövesd az útvonalat két dolog között, vagy magyaráztass el egy fogalmat.

> Szeretnéd, hogy ez folyamatosan működjön, a háttérben frissülve a kódod, dokumentumaid és meetingjeid felett, ne csak igény szerint? Pontosan ezt építjük a **[graphify.com](https://graphify.com)** oldalon, és a korai hozzáférés már nyitva van itt: **[app.graphify.com](https://app.graphify.com/login)**.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="a graphify interaktív graph.html oldala, amely a FastAPI kódbázist erővezérelt tudásgráfként mutatja, az észlelt közösségek jelmagyarázatával" width="900">
</p>
<p align="center">
  <em>A graphify által feltérképezett FastAPI kódbázis. Minden csomópont egy fogalom, a színek az észlelt közösségek, és az egész kattintható a graph.html-ben.</em>
</p>

**Kezdés** (30 másodperc):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

Ezután az AI-asszisztensedben:

```
/graphify .
```

Ennyi. **Három fájlt** kapsz:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**Működik ezekkel:** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot és további 15+ — [válaszd ki a platformodat](#telepítés).

---

## Működés közben

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="graphify path lekérdezés: egy terminál a FastAPI és a ModelField közötti legrövidebb útvonalat kéri, és a válasz ugrásról ugrásra világít fel a tudásgráfon" width="900">
</p>

Ha a gráf felépült, lekérdezed ahelyett, hogy fájlokat olvasnál. Valódi kimenet, a graphify a fent bemutatott FastAPI kódbázison futtatva:

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

Minden él **megbízhatósági címkét** hordoz (`EXTRACTED` = kifejezetten szerepel a forrásban, `INFERRED` = feloldásból származtatva), így megkülönbözteted a közvetlenül kiolvasottat a következtetettől. A `graphify query "<question>"` egy hétköznapi nyelven feltett kérdésre szűkített részgráfot ad vissza, a `graphify path A B` pedig felderíti, hogyan kapcsolódik össze bármely két dolog.

---

## Decouple: kockázatra pontozott Extract-Class jelöltek

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: a MainWindow god node kockázatra pontozott jelöltosztályokra bomlik, két osztály között megosztott state figyelmeztetéssel" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: a MainWindow 5 javasolt osztálya, a Node Info panel a Main Window Axis and Range Controls elemre nyitva, 0,608 state-átfedést mutatva a Main Window Controller Core felé" width="900">
</p>
<p align="center">
  <em>A DECOUPLE.html egy valódi futáson — egy javasolt osztályra kattintva pontosan látod, melyik másik osztállyal oszt meg state-et, és konkrétan mit oszt meg.</em>
</p>

Ugyanez az oldal a felbontást magát is megjeleníti. A **Preview decoupled view** kapcsoló a god osztály saját metódusait a javasolt osztályokra cseréli, és helyben átvezeti az éleket — a bekötés változása, nem egy újrarajzolt diagram:

| Előtte — a god osztály ma | Utána — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html a kapcsoló előtt: egyetlen MainWindow hub csomópont, körülötte legyezőszerűen elrendezett saját metódusaival" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html a kapcsoló után: ugyanaz a csomópont 5 rombusz alakú javasolt osztályra redukálva, zöld szaggatott élek mutatják, mely metódusok kerültek melyikbe, piros élek a kettejük között megosztott példányállapotot" width="440"> |
| Egyetlen csomópont, amely 47 saját metódust tart, és mindegyik csak az osztályon keresztül érhető el. | A javasolt osztályok. Zöld szaggatott = mi került ki melyikbe; piros = a példányállapot, amelyet kettejük továbbra is megoszt — pontosan ez dönti el a `split` és a `keep_as_is` közötti választást. Csak azok a jelöltek kerülnek kirajzolásra, amelyek átmennek a kockázati küszöbön — itt 6-ból 5, ezért van egy metódus, amelynek nincs rombusza, ahová leszállhatna. |

A `graphify decouple` megtalálja a god objecteket, és megmondja, hogy a felbontásuk valóban megéri-e — nem csak azt, hogy nagyok.

A hibajelenség, amelynek elkapására létezik: egy 47 metódusos osztály, amelyet a call graph alapú klaszterezés készségesen 5 rendezettnek tűnő csoportra bont, de mindegyik továbbra is pontosan ugyanazt a `self._chart_style` / `self._crosshair` példányállapotot olvassa és írja alatta. Ha kiszállítod ezt a felbontást, semmit nem csatoltál szét — csak metódusokat mozgattál új fájlokba, amelyeket továbbra sem lehet függetlenül tesztelni, módosítani vagy átgondolni, mert mindnek ugyanarra a megosztott state-re van szüksége visszaadva. Egy eszköz, amely csak a call graphot nézi, ezt egyáltalán nem látja; ehhez vissza kell mennie a tényleges forráshoz.

**Két ellenőrzés, mindkettő 0-LLM, mindkettő determinisztikus:**

1. **Ez egyáltalán God Object?** Egy magas fokszámú csomópont lehet valódi God Object (sok SAJÁT metódus, egymással össze nem függő felelősségek között szétszórva — az Extract Class alkalmazható), vagy egy túlhivatkozott hub/adatmodell (kevés saját metódus, többnyire *bejövő* hivatkozások — a törzsének felbontása semmit nem ér; a megoldás az interfész szűkítése, nem az osztálykiemelés). A `classify_god_node` a `member_ratio` alapján különbözteti meg ezeket, nem a nyers fokszám alapján — ez a különbség óvja meg a `TraceSource`-t (84 él, de csak 6 saját metódus) attól a hamis split-javaslattól, amelyet a `MainWindow` (88 él, 47 saját metódus) jogosan kap meg.
2. **Valóban csökkentené a csatolást a felbontás?** A `risk_before` (a god node jelenlegi mérete/csatoltsága/fragmentáltsága) összevetésre kerül a `risk_after` értékkel — azzal az ÚJ kockázattal, amelyet maga a felbontás vezetne be: csoportok közötti hívások, amelyek korábban láthatatlan osztályon belüli élek voltak, és most explicit osztályok közötti függőségekké válnak; hívók, amelyeknek ezután egynél több új osztálytól kellene függeniük; és — az az ellenőrzés, amelyet egy call graph szerkezetileg nem tud elvégezni — mennyi `self`/`this` példányállapot (olvasások, írások és megosztott segédmetódus-hívások, külön súlyozva: egy megosztott **írás** magasabb pontot kap, mint egy megosztott olvasás) közös valójában a javasolt csoportokban. Ehhez a god node saját forrásfájlját közvetlenül újraparse-olja tree-sitterrel; nem támaszkodik a graphify saját kinyert gráfjára, amely egyetlen nyelvre sem rögzít mezőszintű hozzáférést. A terv csak akkor javasol `split`-et, ha a `risk_after` egy `risk_before` alatti küszöböt is átlép — egyébként `marginal` vagy `keep_as_is` az eredmény, és egy nem javasolt jelölt számként jelenik meg, sosem olyan alakzatként, amelyet szemre kellene megkérdőjelezned.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

Három fájlt hoz létre a `graph.json` mellé:

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

**Nyelvi lefedettség a state-megosztás ellenőrzéséhez** (a fenti, csak call graph alapú besorolás minden olyan nyelvre működik, amelyet a graphify kinyer; ez a táblázat kifejezetten a forrás újraparse-olására vonatkozik, amely a `self`/`this` state-átfedést ellenőrzi):

| Nyelv | Támogatott | Megjegyzések |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | a `this.foo()` saját AST-csomópont, nem becsomagolt mezőhozzáférés — külön kezelve |
| C# | ✅ | |
| Rust | ✅ | `self.x` az `impl` blokkokon keresztül |
| Ruby | ✅ | `@x` (az uralkodó idióma) + `self.foo` hívások |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | metódusonkénti receiver-feloldás — a Go-ban nincs `self`/`this` kulcsszó, ezért a receiver nevét (`f` a `func (f *Foo) M()` esetén) minden metódusnál újra feloldja |
| C | ❌ | egy struct-pointer paraméternek nincs szintaktikai jelölése, amely megkülönböztetné bármely más paramétertől — teljes típuskikövetkeztetés nélkül nincs megbízható jel |

Egy nem támogatott nyelvű god node, vagy olyan, amelynek forrása nem olvasható, `state_analysis: "skipped"` jelölést kap — a besorolás és a call graph pontszám ekkor is lefut, de az ajánlás egyedül a call graphra támaszkodik ahelyett, hogy hallgatólagosan feltételezné a state-ellenőrzés sikerét.

---

## Mit csinál

Amit alapból kapsz:

| Képesség | Amit kapsz |
|---|---|
| **God node-ok** | A legtöbb kapcsolattal rendelkező fogalmak, hogy lásd, min megy át minden |
| **Közösségek** | A gráf alrendszerekre bontva (Leiden), LLM-mentes címkékkel |
| **Fájlok közötti linkek** | `calls` / `imports` / `inherits` / `mixes_in` feloldva ~40 nyelven tree-sitter AST-vel |
| **Query, path, explain** | Tegyél fel egy kérdést, kövesd két dolog közötti útvonalat, vagy magyaráztass el egy fogalmat — mindezt a `graph.json` ellen |
| **Indoklás + dokumentumhivatkozások** | A `# NOTE:` / `# WHY:` megjegyzések és az ADR/RFC hivatkozások elsőrangú csomópontokká válnak, a kódhoz kapcsolva |
| **A kódon túl** | Dokumentumok, PDF-ek, képek és videó/hang mind ugyanabba a gráfba kerülnek |
| **Local-first** | A kód lokálisan, tree-sitterrel elemződik (nincs LLM, semmi nem hagyja el a gépedet); csak a dokumentumok/média szemantikus futása hív backendet, és csak ha beállítasz egyet |

---

## Benchmarkok

| Benchmark | Metrika | graphify | Mezőny |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | QA accuracy | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | QA accuracy | **76%** | holtverseny a dense RAG-gel |
| Gráfépítés | LLM-kreditek | **0** | a legtöbb rendszernél tokenenként |

Minden rendszer ugyanazon a harness-en futott, ugyanazzal a modellel és budgettel, egy olyan judge pontozásával, amelyet vakon validáltak egy második judge ellen (90,6% egyetértés, Cohen-féle kappa 0,81). A teljes, rendszerenkénti táblázatok, a code-intelligence eredmény és a reprodukciós parancsok: **[BENCHMARKS.md](../../BENCHMARKS.md)**.

---

## Előfeltételek

| Követelmény | Minimum | Ellenőrzés | Telepítés |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(ajánlott)* | bármelyik | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(alternatíva)* | bármelyik | `pipx --version` | `pip install pipx` |

**Gyors telepítés macOS-en (Homebrew):**
```bash
brew install python@3.12 uv
```

**Gyors telepítés Windowson:**
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

## Telepítés

> **Hivatalos csomag:** a PyPI-csomag neve `graphifyy` (dupla y-nal). A PyPI-n található többi `graphify*` csomag nem kapcsolódik hozzá. A CLI-parancs továbbra is `graphify`.

**1. lépés — telepítsd a csomagot:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**2. lépés — regisztráld a skillt az AI-asszisztensednél:**

```bash
graphify install
```

Ennyi. Nyisd meg az AI-asszisztensedet, és írd be: `/graphify .`

Ha az asszisztens-skillt a felhasználói profilod helyett az aktuális repositoryba
szeretnéd telepíteni, add hozzá a `--project` kapcsolót:

```bash
graphify install --project
graphify install --project --platform codex
```

A projekt hatókörű telepítések az aktuális könyvtárba írnak, például
`.claude/skills/graphify/SKILL.md` vagy `.agents/skills/graphify/SKILL.md` (plusz egy
`references/` sidecar, amelyet a skill igény szerint tölt be), és
kiírnak egy `git add` javaslatot azokhoz a fájlokhoz, amelyeket commitolni lehet.
Azok a platformspecifikus parancsok, amelyek támogatják a projekt hatókörű telepítést, ugyanezt a kapcsolót fogadják el,
például `graphify claude install --project` vagy `graphify codex install --project`.

> **PowerShell megjegyzés:** használd a `graphify .` alakot a `/graphify .` helyett — a kezdő perjel a PowerShellben útvonal-elválasztó.

> **`graphify: command not found`?** Az `uv tool install` / `pipx install` a `graphify` parancsot a saját tool bin könyvtárába teszi (`~/.local/bin`). Ha a shelled közvetlenül a telepítés után nem találja — ez gyakori friss macOS + zsh beállításnál —, az a könyvtár még nincs a `PATH`-odon: futtasd az `uv tool update-shell` (vagy `pipx ensurepath`) parancsot, majd nyiss új terminált. Sima `pip` esetén add hozzá a `~/.local/bin` (Linux) vagy `~/Library/Python/3.x/bin` (Mac) könyvtárat a PATH-hoz, vagy futtasd a `python -m graphify` parancsot.

> **Telepítés helyett `uvx` / `uv tool run` használata?** A csomagot nevezd meg, ne a parancsot: `uvx --from graphifyy graphify install`. A sima `uvx graphify …` elbukik (`No solution found … no versions of graphify`), mert az `uv tool run` az első szót *csomagként* olvassa, a csomag neve pedig `graphifyy` — a `graphify` parancs benne lakik.

> **Kerüld a `pip install` használatát Macen/Windowson**, ha lehet. A skill futásidőben oldja fel a Pythont a `graphify-out/.graphify_python` alapján; ha az más környezetre mutat, mint ahová a `pip` telepítette a csomagot, `ModuleNotFoundError: No module named 'graphify'` hibát kapsz. Az `uv tool install` és a `pipx install` saját környezetébe izolálja a csomagot, és ezt teljesen elkerüli.

> **Git hookok és uv tool / pipx:** a `graphify hook install` telepítéskor közvetlenül beágyazza az aktuális interpreter útvonalát a hook-szkriptekbe, így a post-commit hook grafikus git kliensekben és CI runnereken is helyesen fut, ahol a `~/.local/bin` nincs a PATH-on. Ha újratelepíted vagy frissíted a graphify-t, futtasd újra a `graphify hook install` parancsot a beágyazott útvonal frissítéséhez.

> **Strict mód (Claude Code):** a `graphify install --project --strict` gondoskodik arról, hogy az asszisztens ténylegesen használja a gráfot. Az alapértelmezett telepítés csak *noszogatja*, hogy fájlolvasás előtt futtasson `graphify query`-t; a strict mód *blokkolja* a munkamenet első nyers forrásolvasását, és a gráf felé irányítja, majd visszaáll a noszogatásra (így munkamenetenként legfeljebb egyszer aktiválódik, és sosem akad be). Futásidőben a `GRAPHIFY_HOOK_STRICT=1`/`0` kapcsolja; az alapértelmezett telepítés változatlan (lágy noszogatás).

<details>
<summary><b>Válaszd ki a platformodat</b> (20+ asszisztens, kattints a kibontáshoz)</summary>

| Platform | Telepítőparancs |
|----------|----------------|
| Claude Code (Linux/Mac) | `graphify install` |
| Claude Code (Windows) | `graphify install` (automatikusan felismerve) vagy `graphify install --platform windows` |
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
| Agent Skills (keretrendszer-független) | `graphify install --platform agents` (alias: `--platform skills`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify install --platform pi` |
| Cursor | `graphify cursor install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

A Codex felhasználóinak a párhuzamos kinyeréshez a `~/.codex/config.toml` fájl `[features]` szakaszában `multi_agent = true` is kell. A CodeBuddy ugyanazt az Agent tool és PreToolUse hook mechanizmust használja, mint a Claude Code. A Factory Droid a `Task` toolt használja a párhuzamos subagent-diszpécsereléshez. Az OpenClaw és az Aider szekvenciális kinyerést használ (a párhuzamos agent-támogatás ezeken a platformokon még korai fázisban van). A Trae az Agent toolt használja párhuzamos subagent-diszpécsereléshez, és **nem** támogatja a `PreToolUse` hookokat, ezért az AGENTS.md a folyamatosan aktív mechanizmus.

A `--platform agents` (alias: `--platform skills`) az általános, keretrendszer-független [Agent-Skills](https://github.com/anthropics/skills) helyeket célozza: a specifikáció szerinti, felhasználói szintű `~/.agents/skills/` könyvtárat (ezt olvassa az `npx skills` és a specifikációkövető keretrendszerek) globális telepítéshez, valamint a `./.agents/skills/` könyvtárat projekt (`--project`) telepítéshez. A csupasz `graphify install` szándékosan egyplatformos marad (Claude Code) — használd a megnevezett `agents` platformot, ha azt szeretnéd, hogy a skillt bármely, `.agents/skills` könyvtárat olvasó keretrendszer megtalálja.

> A Codex a `/graphify` helyett a `$graphify` alakot használja.

</details>

<details>
<summary><b>Opcionális extrák</b> (csak azt telepítsd, amire szükséged van)</summary>

| Extra | Mit ad hozzá | Telepítés |
|---|---|---|
| `pdf` | PDF-kinyerés | `uv tool install "graphifyy[pdf]"` |
| `office` | `.docx` és `.xlsx` támogatás | `uv tool install "graphifyy[office]"` |
| `google` | Google Sheets megjelenítés | `uv tool install "graphifyy[google]"` |
| `video` | Videó-/hangátirat (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | MCP stdio szerver | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Neo4j push támogatás | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | FalkorDB push támogatás | `uv tool install "graphifyy[falkordb]"` |
| `svg` | SVG gráfexport | `uv tool install "graphifyy[svg]"` |
| `leiden` | Leiden közösségdetektálás (csak Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Ollama lokális inferencia | `uv tool install "graphifyy[ollama]"` |
| `openai` | OpenAI / OpenAI-kompatibilis API-k | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic Claude API (`--backend claude`, `ANTHROPIC_API_KEY`-t használ) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (IAM-et használ, nem kell API-kulcs) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT` kell) | `uv tool install "graphifyy[openai]"` |
| `sql` | SQL-séma kinyerés | `uv tool install "graphifyy[sql]"` |
| `postgres` | Élő PostgreSQL introspekció (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | BYOND DreamMaker `.dm`/`.dme` AST-kinyerés (C fordító + `python3-dev` kellhet, ha nincs a platformodhoz illő wheel) | `uv tool install "graphifyy[dm]"` |
| `terraform` | Terraform / HCL `.tf`/`.tfvars`/`.hcl` AST-kinyerés | `uv tool install "graphifyy[terraform]"` |
| `pascal` | Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` AST-kinyerés (pontosabb `calls`/`inherits` élek; hiányában regex-alapú extraktorra esik vissza) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | Kínai lekérdezés-szegmentálás (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | Minden fenti | `uv tool install "graphifyy[all]"` |

</details>

---

## Hogy az asszisztensed mindig a gráfot használja

Futtasd ezt egyszer a projektedben, miután felépítettél egy gráfot:

| Platform | Parancs |
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
| Agent Skills (keretrendszer-független) | `graphify agents install` (alias: `graphify skills install`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify pi install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

Ez egy kis konfigurációs fájlt ír ki, amely arra utasítja az asszisztensedet, hogy kódbázissal kapcsolatos kérdéseknél a tudásgráfot használja, és a szűkített lekérdezéseket — mint a `graphify query "<question>"` — részesítse előnyben a teljes jelentés elolvasásával vagy a nyers fájlok grepelésével szemben.

- **Hook-platformok** (Claude Code, Gemini CLI): egy hook automatikusan lefut a keresés jellegű tool-hívások előtt (Claude Code-on pedig a forrásfájlok egyenkénti, Read/Glob toolokkal történő olvasása előtt is), és a gráf felé tereli az asszisztensedet.
- **Utasításfájl-platformok** (Codex, OpenCode, Cursor stb.): állandó utasításfájlok (`AGENTS.md`, `.cursor/rules/` stb.) adják ugyanezt a query-first útmutatást.

A `GRAPH_REPORT.md` továbbra is rendelkezésre áll széles körű architektúra-áttekintéshez.

A **CodeBuddy** ugyanazt a két dolgot teszi, mint a Claude Code: kiír egy `CODEBUDDY.md` szakaszt, amely arra utasítja a CodeBuddyt, hogy architektúra-kérdések megválaszolása előtt olvassa el a `graphify-out/GRAPH_REPORT.md` fájlt, és telepít `PreToolUse` hookokat (`.codebuddy/settings.json`), amelyek a Bash keresőparancsok és fájlolvasások előtt futnak le, és inkább a `graphify query` felé terelnek.

A **Codex** az `AGENTS.md` fájlba ír, és ezen a platformon valójában ez hordozza a folyamatosan aktív gráf-útmutatást. A `graphify codex install` regisztrál egy `PreToolUse` hookot is a `.codex/hooks.json` fájlban (`graphify hook-check`), de ez a bejegyzés szándékosan **no-op**: a Codex Desktop elutasítja a `hookSpecificOutput.additionalContext` mezőt `PreToolUse` esetén, így egy ottani noszogatás elrontaná a Bash tool-hívásokat. A Claude Code-dal ellentétben, ahol a hook (`graphify hook-guard`) végzi a noszogatást, a Codexen a hook lefut és szándékosan nem csinál semmit — az `AGENTS.md` itt a folyamatosan aktív mechanizmus.

A **Kilo Code** a Graphify skillt a `~/.config/kilo/skills/graphify/SKILL.md` helyre, egy natív `/graphify` parancsot pedig a `~/.config/kilo/command/graphify.md` helyre telepít. A `graphify kilo install` emellett kiírja az `AGENTS.md` fájlt, plusz egy natív `tool.execute.before` plugint (`.kilo/plugins/graphify.js` + regisztráció a `.kilo/kilo.json` vagy `.kilo/kilo.jsonc` fájlban), így a Kilo a natív `.kilo` konfiguráción keresztül ugyanazt a folyamatosan aktív gráf-emlékeztető viselkedést kapja.

A **Cursor** a `.cursor/rules/graphify.mdc` fájlt írja ki `alwaysApply: true` beállítással, így a Cursor automatikusan minden beszélgetésbe beemeli — nincs szükség hookra.

A graphify eltávolítása az összes platformról egy lépésben: `graphify uninstall` (add hozzá a `--purge` kapcsolót a `graphify-out/` törléséhez is). Vagy használd a platformspecifikus parancsot (pl. `graphify claude uninstall`).

---

## Mi van a jelentésben

- **God node-ok** — a projekted legtöbb kapcsolattal rendelkező fogalmai. Minden ezeken keresztül megy át.
- **Meglepő kapcsolatok** — linkek olyan dolgok között, amelyek különböző fájlokban vagy modulokban élnek. Aszerint rangsorolva, mennyire váratlanok.
- **A „miért"** — a beágyazott megjegyzések (`# NOTE:`, `# WHY:`, `# HACK:`), docstringek és a dokumentumokból származó tervezési indoklások külön csomópontokként kerülnek kinyerésre, az általuk magyarázott kódhoz kapcsolva.
- **Javasolt kérdések** — 4–5 kérdés, amelyek megválaszolására a gráf különösen alkalmas.
- **Megbízhatósági címkék** — minden következtetett kapcsolat `EXTRACTED`, `INFERRED` vagy `AMBIGUOUS` jelölést kap. Mindig tudod, mi volt megtalálva és mi kitalálva.

---

## Milyen fájlokat kezel

| Típus | Kiterjesztések |
|------|-----------|
| Kód (36 tree-sitter nyelvtan) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (a `.dm`/`.dme` `uv tool install graphifyy[dm]` telepítést igényel; a `.mts`/`.cts` a TypeScript nyelvtant használja újra, a `.cc`/`.cxx`, valamint a CUDA `.cu`/`.cuh` és a Metal `.metal` a C++ nyelvtant) |
| Salesforce Apex | `.cls .trigger` (regex-alapú; classok, interfészek, enumok, metódusok, triggerek, SOQL/DML élek) |
| Terraform / HCL | `.tf .tfvars .hcl` (`uv tool install graphifyy[terraform]` szükséges) |
| MCP konfigurációk | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — szerver-csomópontokat, csomaghivatkozásokat és környezetiváltozó-igényeket nyer ki |
| Csomagmanifesztek | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — csomagonként egy kanonikus csomag-csomópont (név szerint), plusz `depends_on` élek, így a több manifesztből hivatkozott csomag egyetlen hub |
| Dokumentumok | `.md .mdx .qmd .html .txt .rst .yaml .yml` (a markdown `[text](./other.md)` linkek és a `[[wikilinkek]]` `references` élekké válnak a dokumentumok között) |
| Office | `.docx .xlsx` (`uv tool install graphifyy[office]` szükséges) |
| Google Workspace | `.gdoc .gsheet .gslides` (opt-in; `gws` hitelesítést és `--google-workspace` kapcsolót igényel; a Sheets `uv tool install graphifyy[google]` telepítést kér) |
| PDF-ek | `.pdf` |
| Képek | `.png .jpg .webp .gif` |
| Videó / hang | `.mp4 .mov .mp3 .wav` és továbbiak (`uv tool install graphifyy[video]` szükséges) |
| YouTube / URL-ek | bármely videó-URL (`uv tool install graphifyy[video]` szükséges) |

A kód **lokálisan, API-hívások nélkül** kerül kinyerésre (AST tree-sitterrel). Minden más az AI-asszisztensed modell-API-ján keresztül megy.

A Google Drive for desktop `.gdoc`, `.gsheet` és `.gslides` fájljai
parancsikon-mutatók, nem dokumentumtartalom. Ha natív Google Docs, Sheets és Slides
tartalmat is be szeretnél vonni egy headless kinyerésbe, telepítsd és hitelesítsd a
[`gws` CLI-t](https://github.com/googleworkspace/cli), majd futtasd:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

Beállíthatod a `GRAPHIFY_GOOGLE_WORKSPACE=1` értéket is. A Graphify a parancsikonokat
Markdown sidecar fájlként exportálja a `graphify-out/converted/` könyvtárba, majd azokat a fájlokat nyeri ki.

---

## Gyakori parancsok

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

Lásd fent a [Decouple: kockázatra pontozott Extract-Class jelöltek](#decouple-kockázatra-pontozott-extract-class-jelöltek) részt, vagy lent a [teljes parancsreferenciát](#teljes-parancsreferencia).

---

## Fájlok kizárása

Hozz létre egy `.graphifyignore` fájlt a projekted gyökerében — ugyanaz a szintaxis, mint a `.gitignore` esetén, beleértve a `!` negációt is.

**A `.gitignore` automatikusan érvényesül.** A graphify minden könyvtárban beolvassa a `.gitignore` fájlt. Ha egy `.graphifyignore` is jelen van, a kettő **összefésülődik** — a `.graphifyignore` mintái értékelődnek ki utoljára, így ütközés esetén ezek nyernek (a `!` negációkat is beleértve). Egy `.graphifyignore` hozzáadása mindig csak többet zár ki; sosem vesz vissza olyan fájlt, amelyet a `.gitignore` már kizárt. Az alkönyvtárakra vonatkozó hatókör ugyanúgy működik, mint a gitnél — egy ignore fájl csak a saját részfájára hat.

Add át a `--no-gitignore` kapcsolót a `graphify extract` parancsnak, ha a git által kizárt generált vagy transzpilált kód is a gráfba tartozik. Ez kikapcsolja a `.gitignore` és a `.git/info/exclude` fájlokat; a `.graphifyignore` továbbra is érvényes.

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

## Csapatbeállítás

A `graphify-out/` könyvtár arra való, hogy gitbe kerüljön, így a csapat minden tagja térképpel indul.

**Ajánlott `.gitignore` kiegészítések:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> A `manifest.json` mostantól hordozható — a kulcsok relatív útvonalként tárolódnak és betöltéskor újrahorgonyzódnak, így a commitolása biztonságos, és elkerüli a teljes újraépítést az első checkoutnál.

**Munkafolyamat:**
1. Egy ember lefuttatja a `/graphify .` parancsot, és commitolja a `graphify-out/` könyvtárat.
2. Mindenki más pullol — az asszisztensük azonnal olvassa a gráfot.
3. Futtasd a `graphify hook install` parancsot, hogy minden commit után automatikusan újraépüljön (csak AST, nincs API-költség). Ez egy git merge drivert is beállít, így a `graph.json` sosem marad konfliktusjelölőkkel — ha két fejlesztő párhuzamosan commitol, a gráfjaik automatikusan unió szerint egyesülnek.
4. Ha dokumentumok vagy tanulmányok változnak, futtasd a `/graphify --update` parancsot azoknak a csomópontoknak a frissítéséhez.

---

## A gráf közvetlen használata

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

Az MCP-szerver strukturált hozzáférést ad az asszisztensednek: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Megosztott HTTP-szerver

A `--transport stdio` (az alapértelmezés) fejlesztőnként egy lokális szervert indít. A `--transport http` ugyanezeket a toolokat az MCP Streamable HTTP transporton szolgálja ki, így egyetlen megosztott folyamat kiszolgálhatja a gráfot az egész csapatnak — a kliensek az IDE MCP-konfigurációjukat a `http://<host>:8080/mcp` címre irányítják ahelyett, hogy lokálisan futtatnák a graphify-t.

| Kapcsoló | Alapérték | Cél |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | A használandó transport |
| `--host` | `127.0.0.1` | HTTP bind host (használd a `0.0.0.0` értéket a localhoston túli elérhetőséghez) |
| `--port` | `8080` | HTTP bind port |
| `--api-key` | env `GRAPHIFY_API_KEY` | `Authorization: Bearer <key>` (vagy `X-API-Key`) megkövetelése |
| `--path` | `/mcp` | HTTP mount útvonal |
| `--json-response` | ki | Sima JSON visszaadása SSE streamek helyett |
| `--stateless` | ki | Nincs munkamenetenkénti állapot (terheléselosztott / CI deploymentekhez) |
| `--session-timeout` | `3600` | Az inaktív, állapottal rendelkező munkamenetek felszámolása N másodperc után (`0` kikapcsolja) |

Az alapértelmezett `127.0.0.1` bind csak loopbackon érhető el. Állítsd be a `--host 0.0.0.0` **és** az `--api-key` kapcsolót együtt, ha megosztott hoston teszed elérhetővé. Futtatás konténerben:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **WSL / Linux megjegyzés:** az Ubuntu `python3`-at szállít, nem `python`-t. Használj venv-et a konfliktusok elkerülésére:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## Környezeti változók

Ezekre csak a **headless / CI kinyeréshez** (`graphify extract`) van szükség. Ha a `/graphify` skillen keresztül futtatod az IDE-den belül, a modell-API-t az IDE-munkameneted biztosítja — nem kellenek extra kulcsok.

| Változó | Mire szolgál | Mikor szükséges |
|---|---|---|
| `ANTHROPIC_API_KEY` | Claude (Anthropic) backend | `--backend claude` |
| `ANTHROPIC_BASE_URL` | Anthropic-kompatibilis endpoint URL (LiteLLM proxy, gateway-ek, …) | `--backend claude` (alapérték: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Modellnév a Claude backendhez — egyedi endpointoknál azt a modellnevet/aliast használd, amelyet a szervered közzétesz | `--backend claude` (alapérték: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` vagy `GOOGLE_API_KEY` | Google Gemini backend | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI vagy OpenAI-kompatibilis API-k | `--backend openai` (a lokális szerverek bármilyen nem üres értéket elfogadnak) |
| `OPENAI_BASE_URL` | OpenAI-kompatibilis szerver URL (llama.cpp, vLLM, LM Studio, …) | `--backend openai` (alapérték: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | Modellnév az OpenAI backendhez — saját üzemeltetésű szervereknél azt a modellnevet/aliast használd, amelyet a szervered közzétesz (nézd meg a `/v1/models` endpointját), pl. `LFM2.5-8B-A1B-UD-Q4_K_XL` a llama.cpp esetén | `--backend openai` (alapérték: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | DeepSeek backend | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Kimi Code backend | `--backend kimi` |
| `OLLAMA_BASE_URL` | Ollama lokális inferencia URL | `--backend ollama` (alapérték: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Ollama modellnév | `--backend ollama` (alapérték: automatikus felismerés) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Az Ollama KV-cache ablakméretének felülírása | opcionális — alapból automatikusan méretezett |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Hány percig maradjon betöltve az Ollama modell | opcionális — állítsd `0`-ra, hogy minden chunk után kirakódjon |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI Service backend | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | Azure erőforrás endpoint URL | `--backend azure` (az API-kulcs mellett kötelező) |
| `AZURE_OPENAI_API_VERSION` | Azure API-verzió felülírása | opcionális — alapérték `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` vagy `GRAPHIFY_AZURE_MODEL` | Azure deployment neve | opcionális — alapérték `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — szabványos credential chain | `--backend bedrock` (nincs API-kulcs, IAM-et használ) |
| `GRAPHIFY_MAX_WORKERS` | AST-párhuzamosság szálszáma | opcionális — `--max-workers` kapcsolóként is |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Kimeneti korlát emelése sűrű korpuszokhoz | opcionális — pl. `32768` nagy fájlokhoz |
| `GRAPHIFY_API_TIMEOUT` | Hívásonkénti időkorlát másodpercben a HTTP, claude-cli, Anthropic SDK és Bedrock backendekhez (alapérték: 600) | opcionális — `--api-timeout` kapcsolóként is |
| `GRAPHIFY_MAX_RETRIES` | Hányszor próbálkozzon újra egy rate-limitelt (429) kéréssel, mielőtt feladja (alapérték: 6; figyelembe veszi a `Retry-After` fejlécet) | opcionális — emeld szigorú szervezeti limiteknél (pl. kimi); `0` kikapcsolja |
| `GRAPHIFY_FORCE` | Gráf-újraépítés kikényszerítése kevesebb csomópont esetén is | opcionális — `--force` kapcsolóként is |
| `GRAPHIFY_GOOGLE_WORKSPACE` | A Google Workspace export automatikus bekapcsolása | opcionális — állítsd `1`-re |
| `GRAPHIFY_TRIAGE_BACKEND` | Backend a `graphify prs --triage` parancshoz | opcionális — automatikusan felismeri az elérhető kulcsokból |
| `GRAPHIFY_TRIAGE_MODEL` | Modell-felülírás a triage-hoz | opcionális — pl. `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | Állítsd `1`-re a lokális lekérdezésnapló bekapcsolásához a `~/.cache/graphify-queries.log` útvonalon (minden query/path/explain kérdést + korpuszútvonalat rögzít). Alapból kikapcsolva — semmi nem íródik, hacsak nem kéred (#1797) | opcionális |
| `GRAPHIFY_QUERY_LOG` | Bekapcsolja a lekérdezésnaplót, és az alapértelmezett helyett erre az útvonalra írja | opcionális — kikapcsolva, hacsak ez vagy a `_ENABLE` nincs beállítva |
| `GRAPHIFY_QUERY_LOG_DISABLE` | Állítsd `1`-re a lekérdezésnapló kényszerített kikapcsolásához (felülírja a bekapcsoló változókat) | opcionális |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | Ha a napló be van kapcsolva, a teljes részgráf-válaszokat is rögzíti (alapból ki) | opcionális |
| `GRAPHIFY_MAX_GRAPH_BYTES` | A graph.json 512 MiB-os méretkorlátjának felülírása — pl. `700MB`, `2GB` vagy nyers bájtszám | opcionális — nagyon nagy korpuszokhoz hasznos |
| `GRAPHIFY_MAX_CONTEXTS` | Hány nem alapértelmezett projektgráfot tart meg egy több projektet kiszolgáló MCP-szerver | opcionális — alapérték: `8`; érvénytelen értékek esetén `8`, `1` alatti értékek esetén `1` |
| `GRAPHIFY_LLM_TEMPERATURE` | Az LLM hőmérsékletének felülírása a szemantikus kinyeréshez — pl. `0.7`, vagy `none` a kihagyáshoz | opcionális — o1/o3/o4/gpt-5 reasoning modelleknél automatikusan kimarad |

---

## Adatvédelem

- **Kódfájlok** — lokálisan, tree-sitterrel dolgozódnak fel. Semmi nem hagyja el a gépedet. Egy csak kódot tartalmazó korpuszhoz nem kell API-kulcs — a `graphify extract` teljesen offline fut. Vegyes repónál add hozzá a `--code-only` kapcsolót, hogy csak a kódot indexeld, és kihagyd a dokumentumokat/PDF-eket/képeket, amelyekhez különben LLM kellene.
- **Videó / hang** — lokálisan, faster-whisperrel készül az átirat. Semmi nem hagyja el a gépedet.
- **Dokumentumok, PDF-ek, képek** — szemantikus kinyerésre az AI-asszisztensednek küldve (a `/graphify` skillen keresztül, azzal a modellel, amelyet az IDE-munkameneted futtat). A headless `graphify extract` a következők valamelyikét igényli: `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), egy futó Ollama példány (`OLLAMA_BASE_URL`), AWS credentialök a szabványos provider chainen keresztül (Bedrock — nem kell API-kulcs, IAM-et használ), vagy a `claude` CLI bináris (Claude Code — nem kell API-kulcs, a Claude-előfizetésedet használja). A `--dedup-llm` kapcsoló ugyanazt a kulcsot használja.
- **Adatrezidencia** — a `graphify extract` automatikusan felismeri, melyik szolgáltatót használja, aszerint, hogy melyik API-kulcs van beállítva (prioritás: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). Adatrezidencia-követelményekkel bíró kódnál használd a `--backend ollama` (teljesen lokális) beállítást, vagy adj meg explicit `--backend` kapcsolót. A Kimi (`MOONSHOT_API_KEY`) a Moonshot AI kínai szervereire irányít.
- **Nincs telemetria**, nincs használatkövetés, nincs analitika.
- **Lekérdezésnaplózás** — minden `graphify query`, `graphify path`, `graphify explain` és MCP `query_graph` hívás naplózásra kerül a `~/.cache/graphify-queries.log` fájlba JSON Lines formátumban (időbélyeg, kérdés, korpusz, visszaadott csomópontok, időtartam). A teljes részgráf-válaszok alapból **nem** tárolódnak. Állítsd be a `GRAPHIFY_QUERY_LOG_DISABLE=1` értéket a kilépéshez, vagy a `GRAPHIFY_QUERY_LOG=/dev/null` értéket az elnémításhoz a kódútvonal kikapcsolása nélkül.

---

## Korlátok és határok

Amit a graphify szándékosan **nem** csinál, és ahol véget ér a lefedettsége:

- **Nem szemantikus/vektoros keresőmotor.** A gráf strukturális — a forrásból feloldott csomópontok és típusos élek, nem embeddingek. A `graphify query`/`path`/`explain` ezt a struktúrát járja be; nem tudnak felszínre hozni olyan kapcsolatot, amely nincs élként reprezentálva, még akkor sem, ha az "szemantikailag" összefügg. Nincs hasonlóság-/legközelebbi szomszéd alapú tartalék mechanizmus.
- **A dokumentumok, PDF-ek, képek és a headless videó-/URL-kinyerés nem kizárólag helyi.** Csak a kód (tree-sitter AST) és a hang-/videóátirat (faster-whisper) fut teljesen offline. A dokumentumok/PDF-ek/képek kinyerése mindig LLM-hívást igényel — az AI-asszisztensed modelljét a `/graphify` skillen keresztül, vagy egy beállított backend API-kulcsot a headless `graphify extract` esetén. Nézd meg fent az [Adatvédelem](#adatvédelem) részt, hogy pontosan melyik útvonalhoz melyik kapcsoló vagy kulcs kell.
- **A decouple állapotmegosztás-ellenőrzés nem fed le minden nyelvet.** A C-nek nincs megbízható `self`/`this` jele teljes típuskövetkeztetés nélkül, ezért ki van zárva (lásd fent a [nyelvi lefedettségi táblázatot](#decouple-kockázatra-pontozott-extract-class-jelöltek)). Egy nem támogatott nyelvű, vagy olyan god node, amelynek forráskódja nem olvasható be, csak a call graph alapú pontozásra esik vissza (`state_analysis: "skipped"`), nem egy ellenőrzött állapotvizsgálatra.
- **A 3D adatfolyam-szint (data-flow floor) egy névheurisztika, nem adatfolyam-/taint-elemzés.** A `data_floor` I/O-határ-felismerése (parserek, betöltők, olvasók, írók, DB-/HTTP-kliensek) elnevezési konvenciók alapján illeszkedik (`boundary_reason`); egy szokatlan nevű határ-csomópont kimaradhat, ami alábecsüli, milyen mélyen helyezkedik el a gráf többi része.
- **A megbízhatósági címkék a graphify saját feloldási bizonyossága, nem az objektív igazság.** Az `INFERRED` és `AMBIGUOUS` élek legjobb-erőfeszítés alapú feloldások, és még mindig tévesek lehetnek, különösen a rendkívül dinamikus idiómáknál (reflexió, futásidejű diszpécselés, metaprogramozás), amelyeket egyetlen statikus AST-feldolgozás sem tud teljesen feloldani.
- **A HTML-vizualizációnak és a gráf méretének is van felső korlátja.** A `graph.html` / `DECOUPLE.html` alapértelmezetten kihagyja a generálást 5000 csomópont felett (`MAX_NODES_FOR_VIZ`, a `GRAPHIFY_VIZ_NODE_LIMIT` segítségével emelhető); maga a `graph.json` 512 MiB-ra van korlátozva (felülírható a `GRAPHIFY_MAX_GRAPH_BYTES` értékkel). Ha egy korpusz bármelyik korlátot túllépi, használd a `--no-viz` kapcsolót a `query`/`path`/`explain` paranccsal együtt.
- **A projektek közötti tudatosság opt-in, nem automatikus.** A `graphify query` csak azt az egy gráfot látja, amelyre rámutatsz. A több repót érintő kérdésekhez előbb explicit módon regisztrálni kell minden projektet a megosztott gráfba (`graphify global add`, MCP szerverenként legfeljebb `GRAPHIFY_MAX_CONTEXTS` nem alapértelmezett kontextussal) — a graphify soha nem pásztázza át magától a gépedet más repók után kutatva.
- **A párhuzamos, több ágenses kinyerés a platformtól függ.** Ehhez az asszisztens oldalán szükséges a subagentek indításának támogatása (`multi_agent = true` a `~/.codex/config.toml` fájlban Codexhez, illetve az Agent/Task eszköz Claude Code/CodeBuddy/Factory Droid/Trae esetén). Az OpenClaw és az Aider jelenleg csak szekvenciálisan tud kinyerni.
- **A megosztott MCP HTTP-szerver alapból csak loopbackre kötődik.** Egy másik gépről való eléréséhez explicit `--host 0.0.0.0` **és** `--api-key` szükséges; a graphify nem kezel TLS-t, sem semmilyen hitelesítést ezen az egyetlen bearer tokenen túl.
- **A PowerShell a kezdő `/` jelet elérési út-elválasztóként értelmezi.** Emiatt a `/graphify .` parancs Windows PowerShellben elhasal — ez nem graphify-hiba —, használd inkább a `graphify .` parancsot.

---

## Hibaelhárítás

**`graphify: command not found` telepítés után**
A CLI telepítve van, de a bin könyvtára nincs a shelled `PATH`-ján. Válaszd a telepítési módodhoz illő megoldást:
- **uv** (`uv tool install graphifyy`): a parancs az uv tool bin könyvtárába kerül (`~/.local/bin`), amely egy friss macOS/zsh beállításban gyakran nincs a `PATH`-on. Futtasd az `uv tool update-shell` parancsot, majd nyiss új terminált. (A könyvtárat az `uv tool dir --bin` paranccsal találod meg.)
- **pipx** (`pipx install graphifyy`): futtasd a `pipx ensurepath` parancsot, majd nyiss új terminált.
- **pip** (`pip install graphifyy`): a pip egy felhasználói bin könyvtárba telepíti a szkripteket, amely lehet, hogy nincs a `PATH`-on — add hozzá a `~/Library/Python/3.x/bin` (macOS) vagy `~/.local/bin` (Linux) könyvtárat a `PATH`-hoz a `~/.zshrc`/`~/.bashrc` fájlban, vagy egyszerűen futtasd a `python -m graphify` parancsot.

**Az `uvx graphify …` vagy `uv tool run graphify …` nem tudja feloldani a `graphify`-t**
A PyPI-csomag neve `graphifyy`; a `graphify` csak az általa nyújtott parancs. Az `uv tool run` az első szót *csomagnévként* kezeli, tehát egy `graphify` nevű csomagot keres, és `No solution found … no versions of graphify` hibát jelent. Nevezd meg explicit módon a csomagot: `uvx --from graphifyy graphify install` (ugyanaz, mint az `uv tool run --from graphifyy graphify install`). Vagy futtasd egyszer az `uv tool install graphifyy` parancsot, és utána hívd közvetlenül a `graphify`-t.

**Az `uv run --with graphifyy python -m graphify` csendben egy régebbi telepítést futtat**
Az `uv run` a *rendszer* Pythonját használja, így ha ott is él egy régebbi `graphifyy` (pl. egy korábbi `pip install graphifyy` nyomán), a Python előbb találhatja meg azt a másolatot a `sys.path`-on, és a `--with graphifyy` nem írja felül. Hiba nélkül fut, de a *régi* verzió viselkedését kapod — pl. az olyan env-felülírások, mint az `OPENAI_BASE_URL`, csendben figyelmen kívül maradnak, így a kérések az alapértelmezett endpointra mennek, és egy 401-gyel bukik el, ami rossz kulcsnak látszik. A felismerhető jel egy `warning: skill is from graphify <newer>, package is <older>` sor — ez azt jelenti, hogy egy másik telepítés töltődött be, nem csupán egy elavult skill. Ellenőrizd, melyik másolat töltődött be valójában:
```bash
python -c "import graphify; print(graphify.__file__)"
```
Ezután futtasd közvetlenül a telepített parancsot (az az uv által kezelt másolatot használja), vagy távolítsd el az elavult rendszerszintű másolatot:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**A `python -m graphify` működik, de a `graphify` parancs nem**
A shelled `PATH`-ja nem tartalmazza azt a bin könyvtárat, ahová a parancs települt. Részesítsd előnyben az `uv tool install` / `pipx install` megoldást a sima `pip`-pel szemben, majd futtasd az `uv tool update-shell` / `pipx ensurepath` parancsot, és nyiss új terminált (lásd a fenti telepítési megjegyzéseket).

**A `/graphify .` „path not recognized" hibát okoz PowerShellben**
A PowerShell a kezdő `/` jelet útvonal-elválasztóként kezeli. Windowson használd a `graphify .` alakot (perjel nélkül).

**A gráfnak kevesebb csomópontja van `--update` vagy újraépítés után**
Ha egy refaktor fájlokat törölt, a régi csomópontok bennmaradnak. Add át a `--force` kapcsolót (vagy állítsd be a `GRAPHIFY_FORCE=1` értéket), hogy akkor is felülírja, ha az újraépítésnek kevesebb csomópontja van.

**Az `extract` „extraction was incomplete ... refusing to overwrite" hibával lép ki**
Ha egy kinyerési menet összeomlik, vagy egy bejárás nem tudja teljesen beolvasni a korpuszt, a futás kisebb lenne egy teljesnél, ezért a `graphify extract` nem hajlandó egy nagyobb, meglévő gráfot részeredménnyel felülírni (megvédve a `graph.json` fájlodat). Javítsd a mögöttes hibát és futtasd újra, vagy add át az `--allow-partial` kapcsolót a felülíráshoz.

**A gráfban duplikált csomópontok vannak ugyanarra az entitásra (ghost duplikátumok)**
A ghost duplikátumok (ugyanaz a szimbólum kétszer szerepel — egyszer az AST-kinyerésből, forráshellyel, egyszer a szemantikus kinyerésből, anélkül) mostantól automatikusan összefésülődnek build időben. Ha ezt egy v0.8.33 előtt épített gráfban látod, futtass teljes újrakinyerést a takarításhoz:
```bash
graphify extract . --force
```

**Az Ollamának elfogy a VRAM-ja / túllépi a kontextusablakot**
A KV-cache ablak automatikusan méretezett, de lehet, hogy túl nagy a GPU-dnak. Csökkentsd:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**`LLM returned invalid JSON` / `Unterminated string` figyelmeztetések**
A modell JSON-válasza elérte a kimeneti tokenkorlátot, és egy sztring közepén elvágódott. A graphify automatikusan helyreáll (kettévágja a chunkot és újra kinyeri a feleket, egy túlméretes önálló dokumentumot pedig előbb címsor-/bekezdéshatárokon szeletel, hogy az egész fájl így is lefedett legyen), tehát ezek a figyelmeztetések zajosak, de nem jelentenek adatvesztést. A hullámzás csökkentéséhez emeld a kimeneti korlátot, vagy zsugorítsd az egyes chunkok kimenetét:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
Egy felhős gateway, például az OpenRouter esetén részesítsd előnyben a `--backend openai` beállítást (állítsd be az `OPENAI_BASE_URL` értéket) az Ollama shimmel szemben — ez tisztább, OpenAI-kompatibilis út. Ha a modellnek saját maximális kimeneti plafonja van, a `--token-budget` csökkentése a megbízható eszköz.

**A gráf HTML-je túl nagy ahhoz, hogy böngészőben megnyíljon (>5000 csomópont)**
Hagyd ki a HTML-generálást, és használd közvetlenül a JSON-t:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**A `graph.json` konfliktusjelölőket tartalmaz, miután két fejlesztő egyszerre commitolt**
Futtasd a `graphify hook install` parancsot — ez beállít egy git merge drivert, amely automatikusan unió szerint fésüli össze a `graph.json` fájlt, így konfliktusok nem keletkeznek.

**A kinyerés üres csomópontokat/éleket ad vissza dokumentumokra vagy PDF-ekre**
A dokumentumok, PDF-ek és képek LLM-hívást igényelnek — a csak kódot tartalmazó korpuszokhoz nem kell kulcs. Ellenőrizd, hogy az API-kulcsod be van-e állítva, és hogy a backend helyes-e:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**Skill-verzióeltérési figyelmeztetés az IDE-dben**
A telepített graphify verziód eltér a skill fájltól. Frissítsd:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**A Claude Code prompt cache érvénytelenné válik minden `graphify extract` után**
A Graphify kimeneti fájlokat (`graph.json`, `graphify-out/`) ír a workspace-be. Ha ezek az útvonalak nincsenek kizárva, minden írás érvényteleníti a Claude Code prompt cache-ét, ami a következő körben teljes újrafeltöltést kényszerít ki cache-write árazáson. Add hozzá őket a `.claudeignore` fájlhoz:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## Teljes parancsreferencia

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

> **Közösségnevek:** egy agenten belül (Claude Code, Gemini CLI) maga az agent nevezi el a közösségeket. Ha a csupasz CLI-t futtatod, a `cluster-only` automatikusan elnevezi őket a beállított backenddel (beépített vagy egyedi OpenAI-kompatibilis szolgáltató) — add át a `--no-label` kapcsolót a `Community N` megtartásához, vagy futtasd a `graphify label` parancsot a nevek igény szerinti (újra)generálásához.

---

## További információ

- [Hogyan működik](../how-it-works.md) — a kinyerési pipeline, közösségdetektálás, megbízhatósági pontozás, benchmarkok
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — modulbontás, hogyan adj hozzá egy nyelvet
- [Opcionális integrációk](../docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — a könyv a graphify mögötti gondolatokról, az architektúráról elejétől a végéig

---

## graphify Enterprise

A [**graphify Enterprise**](https://graphify.com) az a folyamatosan aktív réteg, amely a graphify-ra épül — ugyanazt a gráfszemléletet alkalmazza a teljes munkakontextusodra: meetingekre, fájlokra, dokumentumokra és kódra, a háttérben folyamatosan frissülve.

Azoknak az embereknek és csapatoknak készült, akiknek a munkája több száz beszélgetésben és dokumentumban él, amelyeket sosem tudnak teljesen rekonstruálni.

**[Iratkozz fel a várólistára a graphify.com oldalon](https://graphify.com).** Az ingyenes próbaverzió hamarosan indul.

---

<details>
<summary>Közreműködés</summary>

### Fejlesztői környezet beállítása

A projekt az [uv](https://docs.astral.sh/uv/) eszközt használja a fejlesztői munkafolyamathoz. Telepítsd egyszer, majd:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

Ellenőrizd az editable telepítést:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### Tesztek futtatása

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> macOS megjegyzés: a tesztkészlet `sample.f90` és `sample.F90` fixture-t is tartalmaz. Ezek ütköznek a kis- és nagybetűket nem megkülönböztető HFS+ / APFS fájlrendszereken. Futtasd Linuxon vagy Docker konténerben, ha mindkét Fortran variánst egyszerre kell tesztelned.

### Git-munkafolyamat

- Az aktív fejlesztés a `v8` branchen zajlik.
- Commit-stílus: `fix: <description>` / `feat: <description>` / `docs: <description>`
- PR nyitása előtt futtasd az `uv run pytest tests/ -q` parancsot, és győződj meg róla, hogy sikeres.
- Minden új nyelvi extraktorhoz adj egy fixture fájlt a `tests/fixtures/` könyvtárba és teszteket a `tests/test_languages.py` fájlba.

### Mivel érdemes hozzájárulni

A **kidolgozott példák** a leghasznosabb hozzájárulás. Futtasd a `/graphify` parancsot egy valódi korpuszon, mentsd a kimenetet a `worked/{slug}/` könyvtárba, írj egy őszinte `review.md` fájlt arról, mit talált el a gráf jól és mit rosszul, és nyiss egy PR-t.

**Kinyerési hibák** — nyiss egy issue-t a bemeneti fájllal, a cache-bejegyzéssel (`graphify-out/cache/`), és azzal, hogy mi maradt ki vagy lett hibás.

A modulfelelősségekhez és egy nyelv hozzáadásának módjához lásd az [ARCHITECTURE.md](../../ARCHITECTURE.md) fájlt.

</details>
