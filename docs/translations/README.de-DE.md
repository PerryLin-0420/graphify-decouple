<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>Ein Fork von <a href="https://github.com/Graphify-Labs/graphify">graphify</a>, der <code>graphify decouple</code> hinzufügt</b> — 0-LLM, risikobewertete Extract-Class-Kandidaten für God Objects, die vor jeder Empfehlung gegen den tatsächlichen Quellcode (nicht nur den Call-Graph) erneut verifiziert werden. Siehe <a href="#decouple-risikobewertete-extract-class-kandidaten">Decouple: risikobewertete Extract-Class-Kandidaten</a> unten.
</p>

<div align="center">
<details><summary><b>In anderen Sprachen lesen</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>Der frühzeitige Zugang zur graphify-Plattform ist vor dem öffentlichen v1-Launch geöffnet: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

Gib `/graphify` in deinem KI-Coding-Assistenten ein, und er bildet dein gesamtes Projekt (Code, Dokumente, PDFs, Bilder, Videos) auf einen **Wissensgraphen** ab, den du **abfragen kannst, statt Dateien zu durchsuchen (grep)**.

- **Code-Maps kostenlos und vollständig lokal.** Code wird mit einem tree-sitter-AST geparst: deterministisch, ohne LLM, nichts verlässt deinen Rechner. (Dokumente, PDFs, Bilder und Videos nutzen für den semantischen Durchlauf das Modell deines Assistenten oder einen konfigurierten API-Key.)
- **Jede Kante ist erklärt.** Jede Verbindung ist mit `EXTRACTED` (explizit in der Quelle) oder `INFERRED` (von graphify aufgelöst) markiert, sodass du erkennst, was direkt gelesen und was hergeleitet wurde.
- **Kein Vektorindex.** Keine Embeddings, kein Vektorspeicher: ein echter Graph, den du durchläufst. Stelle eine Frage, verfolge den Pfad zwischen zwei Dingen, oder lass dir ein Konzept erklären.

> Möchtest du das lieber dauerhaft aktiv, im Hintergrund aktualisiert über Code, Dokumente und Meetings hinweg, statt nur auf Abruf? Genau das bauen wir gerade bei **[graphify.com](https://graphify.com)**, und der frühzeitige Zugang ist jetzt unter **[app.graphify.com](https://app.graphify.com/login)** geöffnet.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="graphifys interaktive graph.html zeigt die FastAPI-Codebasis als kraftbasierten Wissensgraphen mit einer Legende der erkannten Communities" width="900">
</p>
<p align="center">
  <em>Die von graphify abgebildete FastAPI-Codebasis. Jeder Knoten ist ein Konzept, Farben stehen für erkannte Communities, und das Ganze ist in graph.html klickbar.</em>
</p>

**Los geht's** (30 Sekunden):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

Dann in deinem KI-Assistenten:

```
/graphify .
```

Das ist alles. Du bekommst **drei Dateien**:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**Funktioniert mit** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot und 15+ weiteren — [wähle deine Plattform](#installation).

---

## In Aktion sehen

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="graphify-Pfadabfrage: Ein Terminal fragt nach dem kürzesten Pfad zwischen FastAPI und ModelField, und die Antwort leuchtet Schritt für Schritt über den Wissensgraphen auf" width="900">
</p>

Sobald der Graph aufgebaut ist, fragst du ihn ab, statt Dateien zu lesen. Echte Ausgabe, graphify ausgeführt auf der oben gezeigten FastAPI-Codebasis:

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

Jede Kante trägt ein **Konfidenz-Tag** (`EXTRACTED` = explizit in der Quelle, `INFERRED` = durch Auflösung abgeleitet), sodass du erkennst, was direkt gelesen und was hergeleitet wurde. `graphify query "<question>"` liefert für eine Frage in normaler Sprache einen begrenzten Teilgraphen, und `graphify path A B` verfolgt, wie zwei beliebige Dinge zusammenhängen.

---

## Decouple: risikobewertete Extract-Class-Kandidaten

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: Der God-Node MainWindow teilt sich in risikobewertete Kandidatenklassen auf, mit einer Warnung zu geteiltem State zwischen zwei von ihnen" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: Die 5 vorgeschlagenen Klassen von MainWindow, das Node-Info-Panel ist für Main Window Axis and Range Controls geöffnet und zeigt eine State-Überlappung von 0,608 mit Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>DECOUPLE.html bei einem echten Lauf — ein Klick auf eine vorgeschlagene Klasse zeigt genau, mit welcher anderen Klasse sie sich State teilt und was konkret geteilt wird.</em>
</p>

Dieselbe Seite rendert auch die Aufteilung selbst. Der Schalter **Preview decoupled view** ersetzt die eigenen Methoden der God-Klasse durch die vorgeschlagenen Klassen und verlegt die Kanten an Ort und Stelle — die Verdrahtungsänderung, kein neu gezeichnetes Diagramm:

| Vorher — die God-Klasse heute | Nachher — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html vor dem Umschalten: ein einzelner MainWindow-Hub-Knoten, um den herum seine eigenen Methoden aufgefächert sind" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html nach dem Umschalten: derselbe Knoten reduziert auf 5 rautenförmige vorgeschlagene Klassen, grün gestrichelte Kanten zeigen, welche Methoden in welche Klasse extrahiert wurden, rote Kanten den geteilten Instanz-State zwischen zweien davon" width="440"> |
| Ein Knoten mit 47 eigenen Methoden, von denen jede einzelne nur über die Klasse erreichbar ist. | Die vorgeschlagenen Klassen. Grün gestrichelt = was in welche extrahiert wurde; rot = der Instanz-State, den zwei davon weiterhin teilen — genau das entscheidet zwischen `split` und `keep_as_is`. Gezeichnet werden nur Kandidaten, die den Risikoschwellwert bestehen — hier 5 von 6, weshalb eine Methode keine Raute hat, auf der sie landen könnte. |

`graphify decouple` findet God Objects und sagt dir, ob sich eine Aufteilung tatsächlich lohnt — nicht nur, dass sie groß sind.

Das Fehlerbild, das damit erkannt werden soll: eine Klasse mit 47 Methoden, die ein Call-Graph-Clustering bereitwillig in 5 ordentlich aussehende Gruppen aufteilt, die darunter aber alle exakt denselben Instance-State `self._chart_style` / `self._crosshair` lesen und schreiben. Lieferst du diese Aufteilung aus, hast du nichts entkoppelt — du hast nur Methoden in neue Dateien verschoben, die weiterhin nicht unabhängig getestet, geändert oder verstanden werden können, weil sie alle denselben geteilten State zurückgereicht brauchen. Ein Tool, das nur auf den Call-Graph schaut, kann das überhaupt nicht erkennen; es muss dafür auf den tatsächlichen Quellcode zurückgreifen.

**Zwei Prüfungen, beide 0-LLM, beide deterministisch:**

1. **Ist das überhaupt ein God Object?** Ein Knoten mit hohem Grad kann ein echtes God Object sein (viele EIGENE Methoden, verteilt über nicht zusammenhängende Verantwortlichkeiten — Extract Class ist angebracht) oder ein überreferenzierter Hub/Datenmodell (wenige eigene Methoden, überwiegend *eingehende* Referenzen — eine Aufteilung des Bodys bringt nichts; die Lösung ist eine schlankere Schnittstelle, keine Extract-Class). `classify_god_node` unterscheidet das anhand von `member_ratio`, nicht anhand des reinen Grades — der Unterschied, der verhindert, dass `TraceSource` (84 Kanten, aber nur 6 eigene Methoden) einen unsinnigen Split-Vorschlag bekommt, den `MainWindow` (88 Kanten, 47 eigene Methoden) zu Recht erhält.
2. **Würde die Aufteilung die Kopplung wirklich verringern?** `risk_before` (die aktuelle Größe/Kopplung/Fragmentierung des God Nodes) wird mit `risk_after` verglichen — dem NEUEN Risiko, das die Aufteilung selbst einführen würde: gruppenübergreifende Aufrufe, die zuvor unsichtbare klasseninterne Kanten waren und zu expliziten Abhängigkeiten zwischen Klassen werden, Aufrufer, die künftig von mehr als einer neuen Klasse abhängen müssten, und — die Prüfung, die ein Call-Graph strukturell nicht leisten kann — wie viel `self`/`this`-Instance-State (Lesezugriffe, Schreibzugriffe und gemeinsame Aufrufe von Hilfsmethoden, separat gewichtet: ein gemeinsamer **Schreibzugriff** wird höher bewertet als ein gemeinsamer Lesezugriff) die vorgeschlagenen Gruppen tatsächlich gemeinsam haben. Dafür wird die Quelldatei des God Nodes direkt erneut mit tree-sitter geparst; es wird nicht auf graphifys eigenen extrahierten Graphen zurückgegriffen, der für keine Sprache Field-Level-Zugriffe erfasst. Nur wenn `risk_after` einen Schwellenwert unterhalb von `risk_before` unterschreitet, empfiehlt der Plan `split` — andernfalls lautet er `marginal` oder `keep_as_is`, und ein abgelehnter Kandidat wird als Zahl ausgewiesen, niemals als Form gezeichnet, die du optisch anzweifeln müsstest.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

Erzeugt drei Dateien neben `graph.json`:

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

**Sprachabdeckung für die State-Sharing-Prüfung** (die reine Call-Graph-Klassifizierung oben funktioniert für jede von graphify extrahierte Sprache; diese Tabelle betrifft speziell das erneute Parsen der Quelle, das die `self`/`this`-State-Überlappung verifiziert):

| Sprache | Unterstützt | Hinweise |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` ist ein eigener AST-Knoten, kein verpackter Field-Access — wird explizit behandelt |
| C# | ✅ | |
| Rust | ✅ | `self.x` über `impl`-Blöcke |
| Ruby | ✅ | `@x` (das dominante Idiom) + `self.foo`-Aufrufe |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | Receiver-Auflösung pro Methode — Go hat kein `self`/`this`-Schlüsselwort, daher wird der Receiver-Name (`f` in `func (f *Foo) M()`) für jede Methode neu aufgelöst |
| C | ❌ | ein Struct-Pointer-Parameter hat kein syntaktisches Merkmal, das ihn von jedem anderen Parameter unterscheidet — ohne vollständige Typinferenz kein verlässliches Signal |

Ein God Node in einer nicht unterstützten Sprache, oder einer, dessen Quelle nicht gelesen werden kann, wird mit `state_analysis: "skipped"` markiert — Klassifizierung und Call-Graph-Score laufen trotzdem, aber die Empfehlung stützt sich dann allein auf den Call-Graph, statt stillschweigend anzunehmen, dass die State-Prüfung bestanden wurde.

---

## Was es leistet

Was du direkt bekommst:

| Fähigkeit | Was du bekommst |
|---|---|
| **God Nodes** | Die am stärksten vernetzten Konzepte, damit du siehst, wodurch alles läuft |
| **Communities** | Der Graph aufgeteilt in Subsysteme (Leiden), mit LLM-freien Bezeichnungen |
| **Dateiübergreifende Links** | `calls` / `imports` / `inherits` / `mixes_in`, aufgelöst über ~40 Sprachen per tree-sitter-AST |
| **Query, Path, Explain** | Stelle eine Frage, verfolge den Pfad zwischen zwei Dingen, oder lass dir ein Konzept erklären — alles gegen `graph.json` |
| **Begründungen + Doc-Referenzen** | `# NOTE:` / `# WHY:`-Kommentare und ADR/RFC-Zitate werden zu vollwertigen Knoten, die mit dem Code verlinkt sind |
| **Über Code hinaus** | Dokumente, PDFs, Bilder und Video/Audio werden alle in denselben Graphen abgebildet |
| **Local-First** | Code wird lokal mit tree-sitter geparst (kein LLM, nichts verlässt deinen Rechner); nur der semantische Durchlauf über Dokumente/Medien ruft ein Backend auf, und nur wenn du eines konfigurierst |

---

## Benchmarks

| Benchmark | Metrik | graphify | Feld |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | QA accuracy | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | QA accuracy | **76%** | gleichauf mit dense RAG |
| Graph-Aufbau | LLM-Credits | **0** | bei den meisten Systemen pro Token |

Jedes System lief auf demselben Testharness mit demselben Modell und denselben Budgets, bewertet von einem Judge, der blind gegen einen zweiten Judge validiert wurde (90,6 % Übereinstimmung, Cohens Kappa 0,81). Vollständige Tabellen pro System, das Code-Intelligence-Ergebnis und Reproduktionsbefehle: **[BENCHMARKS.md](../../BENCHMARKS.md)**.

---

## Voraussetzungen

| Anforderung | Minimum | Prüfen | Installieren |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(empfohlen)* | beliebig | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(Alternative)* | beliebig | `pipx --version` | `pip install pipx` |

**Schnellinstallation für macOS (Homebrew):**
```bash
brew install python@3.12 uv
```

**Schnellinstallation für Windows:**
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

> **Offizielles Paket:** Das PyPI-Paket heißt `graphifyy` (doppeltes y). Andere `graphify*`-Pakete auf PyPI stehen in keiner Verbindung dazu. Der CLI-Befehl bleibt `graphify`.

**Schritt 1 — Paket installieren:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**Schritt 2 — die Skill bei deinem KI-Assistenten registrieren:**

```bash
graphify install
```

Das ist alles. Öffne deinen KI-Assistenten und gib `/graphify .` ein.

Um die Assistenten-Skill im aktuellen Repository statt in deinem Benutzerprofil zu installieren, füge `--project` hinzu:

```bash
graphify install --project
graphify install --project --platform codex
```

Projektbezogene Installationen schreiben in das aktuelle Verzeichnis, zum Beispiel nach
`.claude/skills/graphify/SKILL.md` oder `.agents/skills/graphify/SKILL.md` (plus einer
`references/`-Sidecar-Datei, die die Skill bei Bedarf lädt), und
geben einen `git add`-Hinweis für Dateien aus, die committet werden können.
Plattformspezifische Befehle, die projektbezogene Installationen unterstützen, akzeptieren dasselbe Flag,
zum Beispiel `graphify claude install --project` oder `graphify codex install --project`.

> **Hinweis zu PowerShell:** Verwende `graphify .` statt `/graphify .` — der führende Schrägstrich ist in PowerShell ein Pfadtrenner.

> **`graphify: command not found`?** `uv tool install` / `pipx install` legen den Befehl `graphify` in ihr Tool-bin-Verzeichnis (`~/.local/bin`). Wenn deine Shell ihn direkt nach der Installation nicht findet — häufig bei einem frischen macOS+zsh-Setup — steht dieses Verzeichnis noch nicht in deinem `PATH`: führe `uv tool update-shell` (oder `pipx ensurepath`) aus und öffne dann ein neues Terminal. Bei reinem `pip` füge `~/.local/bin` (Linux) oder `~/Library/Python/3.x/bin` (Mac) zu deinem PATH hinzu, oder führe `python -m graphify` aus.

> **Läuft es stattdessen über `uvx` / `uv tool run` statt einer Installation?** Nenne das Paket, nicht den Befehl: `uvx --from graphifyy graphify install`. Ein einfaches `uvx graphify …` schlägt fehl (`No solution found … no versions of graphify`), weil `uv tool run` das erste Wort als *Paketnamen* liest, und das Paket heißt `graphifyy` — der Befehl `graphify` steckt darin.

> **Vermeide `pip install` auf Mac/Windows**, wenn möglich. Die Skill löst Python zur Laufzeit über `graphify-out/.graphify_python` auf; zeigt das auf eine andere Umgebung als die, in der `pip` das Paket installiert hat, bekommst du `ModuleNotFoundError: No module named 'graphify'`. `uv tool install` und `pipx install` isolieren das Paket in ihrer eigenen Umgebung und vermeiden das komplett.

> **Git-Hooks und uv tool / pipx:** `graphify hook install` bettet den aktuellen Interpreter-Pfad zur Installationszeit direkt in die Hook-Skripte ein, sodass der post-commit-Hook auch in grafischen Git-Clients und CI-Runnern korrekt ausgelöst wird, wo `~/.local/bin` nicht im PATH steht. Wenn du graphify neu installierst oder aktualisierst, führe `graphify hook install` erneut aus, um den eingebetteten Pfad zu aktualisieren.

> **Strict-Modus (Claude Code):** `graphify install --project --strict` sorgt dafür, dass der Assistent den Graphen tatsächlich nutzt. Die Standardinstallation *stupst* ihn nur an, vor dem Lesen von Dateien `graphify query` auszuführen; der Strict-Modus *blockiert* das erste rohe Quelldateien-Lesen einer Sitzung und leitet es auf den Graphen um, danach kehrt er zum sanften Stups zurück (er greift also höchstens einmal pro Sitzung und bleibt nie hängen). Zur Laufzeit umschaltbar mit `GRAPHIFY_HOOK_STRICT=1`/`0`; die Standardinstallation bleibt unverändert (sanfter Stups).

<details>
<summary><b>Wähle deine Plattform</b> (20+ Assistenten, zum Ausklappen anklicken)</summary>

| Plattform | Installationsbefehl |
|----------|----------------|
| Claude Code (Linux/Mac) | `graphify install` |
| Claude Code (Windows) | `graphify install` (automatisch erkannt) oder `graphify install --platform windows` |
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
| Agent Skills (framework-übergreifend) | `graphify install --platform agents` (Alias `--platform skills`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify install --platform pi` |
| Cursor | `graphify cursor install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

Codex-Nutzer benötigen für die parallele Extraktion außerdem `multi_agent = true` unter `[features]` in `~/.codex/config.toml`. CodeBuddy verwendet denselben Agent-Tool- und PreToolUse-Hook-Mechanismus wie Claude Code. Factory Droid nutzt das `Task`-Tool für den parallelen Subagenten-Dispatch. OpenClaw und Aider verwenden sequenzielle Extraktion (paralleler Agent-Support ist auf diesen Plattformen noch früh). Trae nutzt das Agent-Tool für parallelen Subagenten-Dispatch und unterstützt `PreToolUse`-Hooks **nicht**, daher ist AGENTS.md der dauerhaft aktive Mechanismus.

`--platform agents` (Alias `--platform skills`) zielt auf die generischen, framework-übergreifenden [Agent-Skills](https://github.com/anthropics/skills)-Speicherorte: das spezifikationsgemäße, benutzerglobale `~/.agents/skills/` (gelesen von `npx skills` und spezifikationskonformen Frameworks) für eine globale Installation, und `./.agents/skills/` für eine Projektinstallation (`--project`). Das bloße `graphify install` bleibt bewusst plattformspezifisch (Claude Code) — nutze die benannte Plattform `agents`, wenn die Skill von jedem Framework auffindbar sein soll, das `.agents/skills` liest.

> Codex verwendet `$graphify` statt `/graphify`.

</details>

<details>
<summary><b>Optionale Extras</b> (installiere nur, was du brauchst)</summary>

| Extra | Was es hinzufügt | Installieren |
|---|---|---|
| `pdf` | PDF-Extraktion | `uv tool install "graphifyy[pdf]"` |
| `office` | Unterstützung für `.docx` und `.xlsx` | `uv tool install "graphifyy[office]"` |
| `google` | Rendering von Google Sheets | `uv tool install "graphifyy[google]"` |
| `video` | Video-/Audio-Transkription (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | MCP-stdio-Server | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Neo4j-Push-Unterstützung | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | FalkorDB-Push-Unterstützung | `uv tool install "graphifyy[falkordb]"` |
| `svg` | SVG-Graph-Export | `uv tool install "graphifyy[svg]"` |
| `leiden` | Leiden-Community-Erkennung (nur Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Lokale Inferenz mit Ollama | `uv tool install "graphifyy[ollama]"` |
| `openai` | OpenAI- / OpenAI-kompatible APIs | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic-Claude-API (`--backend claude`, nutzt `ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (nutzt IAM, kein API-Key) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, nutzt `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "graphifyy[openai]"` |
| `sql` | SQL-Schema-Extraktion | `uv tool install "graphifyy[sql]"` |
| `postgres` | Live-Introspektion von PostgreSQL (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | BYOND-DreamMaker-`.dm`/`.dme`-AST-Extraktion (benötigt ggf. einen C-Compiler + `python3-dev`, wenn kein Wheel zu deiner Plattform passt) | `uv tool install "graphifyy[dm]"` |
| `terraform` | Terraform-/HCL-`.tf`/`.tfvars`/`.hcl`-AST-Extraktion | `uv tool install "graphifyy[terraform]"` |
| `pascal` | Pascal-/Delphi-`.pas`/`.dpr`/`.dpk`/`.inc`-AST-Extraktion (genauere `calls`/`inherits`-Kanten; ohne Extra Fallback auf einen Regex-Extraktor) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | Chinesische Query-Segmentierung (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | Alles oben Genannte | `uv tool install "graphifyy[all]"` |

</details>

---

## Deinen Assistenten dauerhaft den Graphen nutzen lassen

Führe dies einmal in deinem Projekt aus, nachdem ein Graph erstellt wurde:

| Plattform | Befehl |
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
| Agent Skills (framework-übergreifend) | `graphify agents install` (Alias `graphify skills install`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify pi install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

Dies schreibt eine kleine Konfigurationsdatei, die deinem Assistenten sagt, bei Fragen zur Codebasis den Wissensgraphen zu konsultieren, wobei begrenzte Abfragen wie `graphify query "<question>"` gegenüber dem Lesen des vollständigen Reports oder dem Durchsuchen roher Dateien bevorzugt werden.

- **Hook-Plattformen** (Claude Code, Gemini CLI): Ein Hook wird automatisch vor Tool-Aufrufen im Suchstil ausgelöst (und, bei Claude Code, vor dem einzelnen Lesen von Quelldateien über die Read/Glob-Tools) und lenkt deinen Assistenten in Richtung des Graph-Pfads.
- **Instruktionsdatei-Plattformen** (Codex, OpenCode, Cursor usw.): dauerhafte Instruktionsdateien (`AGENTS.md`, `.cursor/rules/` usw.) liefern dieselbe Query-first-Anleitung.

`GRAPH_REPORT.md` steht weiterhin für eine breite Architekturübersicht zur Verfügung.

**CodeBuddy** macht dieselben zwei Dinge wie Claude Code: Es schreibt einen `CODEBUDDY.md`-Abschnitt, der CodeBuddy anweist, vor der Beantwortung von Architekturfragen `graphify-out/GRAPH_REPORT.md` zu lesen, und installiert `PreToolUse`-Hooks (`.codebuddy/settings.json`), die vor Bash-Suchbefehlen und Dateizugriffen ausgelöst werden und stattdessen zu `graphify query` hinlenken.

**Codex** schreibt nach `AGENTS.md`, was auf dieser Plattform tatsächlich die dauerhafte Graph-Anleitung trägt. `graphify codex install` registriert außerdem einen `PreToolUse`-Hook in `.codex/hooks.json` (`graphify hook-check`), aber dieser Eintrag ist bewusst ein **No-op**: Codex Desktop lehnt `hookSpecificOutput.additionalContext` bei `PreToolUse` ab, sodass ein Stups dort Bash-Tool-Aufrufe kaputt machen würde. Anders als bei Claude Code, wo der Hook (`graphify hook-guard`) den Stups liefert, löst der Hook bei Codex aus und tut absichtlich nichts — `AGENTS.md` ist hier der dauerhaft aktive Mechanismus.

**Kilo Code** installiert die Graphify-Skill nach `~/.config/kilo/skills/graphify/SKILL.md` und einen nativen `/graphify`-Befehl nach `~/.config/kilo/command/graphify.md`. `graphify kilo install` schreibt außerdem `AGENTS.md` plus ein natives `tool.execute.before`-Plugin (`.kilo/plugins/graphify.js` + Registrierung in `.kilo/kilo.json` oder `.kilo/kilo.jsonc`), sodass Kilo über die native `.kilo`-Konfiguration dasselbe dauerhaft aktive Graph-Erinnerungsverhalten erhält.

**Cursor** schreibt `.cursor/rules/graphify.mdc` mit `alwaysApply: true`, sodass Cursor es automatisch in jede Konversation einbezieht — kein Hook nötig.

Um graphify von allen Plattformen gleichzeitig zu entfernen: `graphify uninstall` (füge `--purge` hinzu, um auch `graphify-out/` zu löschen). Oder nutze den plattformspezifischen Befehl (z. B. `graphify claude uninstall`).

---

## Was im Report steht

- **God Nodes** — die am stärksten vernetzten Konzepte in deinem Projekt. Alles läuft durch sie.
- **Überraschende Verbindungen** — Links zwischen Dingen, die in unterschiedlichen Dateien oder Modulen liegen. Sortiert danach, wie unerwartet sie sind.
- **Das „Warum"** — Inline-Kommentare (`# NOTE:`, `# WHY:`, `# HACK:`), Docstrings und Design-Begründungen aus Dokumenten werden als eigene Knoten extrahiert, die mit dem Code verlinkt sind, den sie erklären.
- **Vorgeschlagene Fragen** — 4–5 Fragen, die der Graph besonders gut beantworten kann.
- **Konfidenz-Tags** — jede hergeleitete Beziehung ist mit `EXTRACTED`, `INFERRED` oder `AMBIGUOUS` markiert. Du weißt immer, was gefunden und was erraten wurde.

---

## Welche Dateien es verarbeitet

| Typ | Endungen |
|------|-----------|
| Code (36 tree-sitter-Grammatiken) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme` erfordert `uv tool install graphifyy[dm]`; `.mts`/`.cts` verwenden dieselbe TypeScript-Grammatik, `.cc`/`.cxx` sowie CUDA `.cu`/`.cuh` und Metal `.metal` verwenden dieselbe C++-Grammatik) |
| Salesforce Apex | `.cls .trigger` (regex-basiert; Classes, Interfaces, Enums, Methods, Triggers, SOQL/DML-Kanten) |
| Terraform / HCL | `.tf .tfvars .hcl` (erfordert `uv tool install graphifyy[terraform]`) |
| MCP-Konfigurationen | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — extrahiert Server-Knoten, Paket-Referenzen, Anforderungen an Umgebungsvariablen |
| Paket-Manifeste | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — ein kanonischer Paket-Knoten pro Paket (nach Name) plus `depends_on`-Kanten, sodass ein aus vielen Manifesten referenziertes Paket ein einziger Hub ist |
| Dokumente | `.md .mdx .qmd .html .txt .rst .yaml .yml` (Markdown-Links `[text](./other.md)` und `[[Wikilinks]]` werden zu `references`-Kanten zwischen Dokumenten) |
| Office | `.docx .xlsx` (erfordert `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (Opt-in; erfordert `gws`-Auth und `--google-workspace`; Sheets benötigen `uv tool install graphifyy[google]`) |
| PDFs | `.pdf` |
| Bilder | `.png .jpg .webp .gif` |
| Video / Audio | `.mp4 .mov .mp3 .wav` und weitere (erfordert `uv tool install graphifyy[video]`) |
| YouTube / URLs | jede Video-URL (erfordert `uv tool install graphifyy[video]`) |

Code wird **lokal ohne API-Aufrufe** extrahiert (AST via tree-sitter). Alles andere läuft über die Modell-API deines KI-Assistenten.

Die `.gdoc`-, `.gsheet`- und `.gslides`-Dateien von Google Drive for Desktop sind
Verknüpfungen (Shortcut-Zeiger), kein Dokumentinhalt. Um native Google Docs, Sheets und Slides
bei einer Headless-Extraktion einzubeziehen, installiere und authentifiziere die
[`gws`-CLI](https://github.com/googleworkspace/cli), und führe dann aus:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

Du kannst auch `GRAPHIFY_GOOGLE_WORKSPACE=1` setzen. Graphify exportiert Shortcuts als
Markdown-Sidecar-Dateien nach `graphify-out/converted/` und extrahiert anschließend diese Dateien.

---

## Häufige Befehle

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

Siehe [Decouple: risikobewertete Extract-Class-Kandidaten](#decouple-risikobewertete-extract-class-kandidaten) oben, oder die [vollständige Befehlsreferenz](#vollständige-befehlsreferenz) unten.

---

## Dateien ignorieren

Erstelle eine `.graphifyignore` im Wurzelverzeichnis deines Projekts — dieselbe Syntax wie `.gitignore`, einschließlich `!`-Negation.

**`.gitignore` wird automatisch berücksichtigt.** graphify liest die `.gitignore` in jedem Verzeichnis. Ist zusätzlich eine `.graphifyignore` vorhanden, werden beide **zusammengeführt** — `.graphifyignore`-Muster werden zuletzt ausgewertet und gewinnen daher bei Konflikten (einschließlich `!`-Negationen). Eine `.graphifyignore` schließt immer nur zusätzlich aus; sie nimmt niemals eine Datei wieder auf, die deine `.gitignore` bereits ausgeschlossen hat. Die Verzeichnisgeltung funktioniert wie bei git — eine Ignore-Datei wirkt sich nur auf ihren eigenen Teilbaum aus.

Übergib `--no-gitignore` an `graphify extract`, wenn git-ignorierter generierter oder transpilierter Code in den Graphen gehört. Das deaktiviert `.gitignore` und `.git/info/exclude`; `.graphifyignore` gilt weiterhin.

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

## Team-Setup

`graphify-out/` ist dafür gedacht, in git committet zu werden, damit jeder im Team mit einer Map startet.

**Empfohlene Ergänzungen für `.gitignore`:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` ist jetzt portabel — Keys werden als relative Pfade gespeichert und beim Laden neu verankert, daher ist das Committen unbedenklich und vermeidet einen vollständigen Neuaufbau beim ersten Checkout.

**Workflow:**
1. Eine Person führt `/graphify .` aus und committet `graphify-out/`.
2. Alle anderen pullen — ihr Assistent liest den Graphen sofort.
3. Führe `graphify hook install` aus, um nach jedem Commit automatisch neu zu bauen (nur AST, keine API-Kosten). Das richtet außerdem einen git-Merge-Driver ein, sodass `graph.json` nie mit Konfliktmarkierungen zurückbleibt — committen zwei Entwickler parallel, werden ihre Graphen automatisch per Union zusammengeführt.
4. Wenn sich Dokumente oder Papers ändern, führe `/graphify --update` aus, um diese Knoten zu aktualisieren.

---

## Den Graphen direkt nutzen

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

Der MCP-Server gibt deinem Assistenten strukturierten Zugriff: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Gemeinsam genutzter HTTP-Server

`--transport stdio` (die Standardeinstellung) startet einen lokalen Server pro Entwickler. `--transport http` stellt dieselben Tools über den MCP-Streamable-HTTP-Transport bereit, sodass ein einziger gemeinsamer Prozess den Graphen für das gesamte Team bedienen kann — Clients richten ihre IDE-MCP-Konfiguration auf `http://<host>:8080/mcp`, statt graphify lokal auszuführen.

| Flag | Standard | Zweck |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Zu verwendender Transport |
| `--host` | `127.0.0.1` | HTTP-Bind-Host (nutze `0.0.0.0`, um über localhost hinaus verfügbar zu sein) |
| `--port` | `8080` | HTTP-Bind-Port |
| `--api-key` | Env `GRAPHIFY_API_KEY` | Erfordert `Authorization: Bearer <key>` (oder `X-API-Key`) |
| `--path` | `/mcp` | HTTP-Mount-Pfad |
| `--json-response` | aus | Gibt reines JSON statt SSE-Streams zurück |
| `--stateless` | aus | Kein Session-State (für lastverteilte / CI-Deployments) |
| `--session-timeout` | `3600` | Räumt inaktive zustandsbehaftete Sessions nach N Sekunden ab (`0` deaktiviert) |

Die Standardbindung `127.0.0.1` ist nur per Loopback erreichbar. Setze `--host 0.0.0.0` **und** `--api-key` zusammen, wenn du es auf einem gemeinsam genutzten Host bereitstellst. Ausführen in einem Container:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **Hinweis zu WSL / Linux:** Ubuntu liefert `python3` aus, nicht `python`. Nutze ein venv, um Konflikte zu vermeiden:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## Umgebungsvariablen

Diese werden nur für die **Headless-/CI-Extraktion** (`graphify extract`) benötigt. Beim Ausführen über die `/graphify`-Skill in deiner IDE wird die Modell-API von deiner IDE-Sitzung bereitgestellt — keine zusätzlichen Keys nötig.

| Variable | Verwendet für | Wann erforderlich |
|---|---|---|
| `ANTHROPIC_API_KEY` | Claude-(Anthropic-)Backend | `--backend claude` |
| `ANTHROPIC_BASE_URL` | Anthropic-kompatible Endpoint-URL (LiteLLM-Proxy, Gateways, …) | `--backend claude` (Standard: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Modellname für das Claude-Backend — bei eigenen Endpoints den Modellnamen/Alias verwenden, den dein Server bereitstellt | `--backend claude` (Standard: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` oder `GOOGLE_API_KEY` | Google-Gemini-Backend | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI oder OpenAI-kompatible APIs | `--backend openai` (lokale Server akzeptieren jeden nicht leeren Wert) |
| `OPENAI_BASE_URL` | OpenAI-kompatible Server-URL (llama.cpp, vLLM, LM Studio, …) | `--backend openai` (Standard: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | Modellname für das OpenAI-Backend — bei selbst gehosteten Servern den Modellnamen/Alias verwenden, den dein Server bereitstellt (siehe dessen `/v1/models`-Endpoint), z. B. `LFM2.5-8B-A1B-UD-Q4_K_XL` für llama.cpp | `--backend openai` (Standard: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | DeepSeek-Backend | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Kimi-Code-Backend | `--backend kimi` |
| `OLLAMA_BASE_URL` | URL für lokale Ollama-Inferenz | `--backend ollama` (Standard: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Ollama-Modellname | `--backend ollama` (Standard: automatische Erkennung) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Überschreibt die Größe des Ollama-KV-Cache-Fensters | optional — standardmäßig automatisch dimensioniert |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Minuten, für die das Ollama-Modell geladen bleibt | optional — setze `0`, um es nach jedem Chunk zu entladen |
| `AZURE_OPENAI_API_KEY` | Azure-OpenAI-Service-Backend | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | Azure-Ressourcen-Endpoint-URL | `--backend azure` (zusätzlich zum API-Key erforderlich) |
| `AZURE_OPENAI_API_VERSION` | Überschreibt die Azure-API-Version | optional — Standard `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` oder `GRAPHIFY_AZURE_MODEL` | Azure-Deployment-Name | optional — Standard `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — Standard-Credential-Chain | `--backend bedrock` (kein API-Key, nutzt IAM) |
| `GRAPHIFY_MAX_WORKERS` | Anzahl der Threads für AST-Parallelität | optional — auch als Flag `--max-workers` |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Erhöht die Output-Obergrenze für dichte Korpora | optional — z. B. `32768` für große Dateien |
| `GRAPHIFY_API_TIMEOUT` | Timeout pro Aufruf in Sekunden für HTTP-, claude-cli-, Anthropic-SDK- und Bedrock-Backends (Standard: 600) | optional — auch als Flag `--api-timeout` |
| `GRAPHIFY_MAX_RETRIES` | Wie oft eine ratenlimitierte (429) Anfrage wiederholt wird, bevor aufgegeben wird (Standard: 6; berücksichtigt `Retry-After`) | optional — erhöhen bei strikten Org-Limits (z. B. kimi); `0` deaktiviert |
| `GRAPHIFY_FORCE` | Erzwingt einen Graph-Rebuild auch bei weniger Knoten | optional — auch als Flag `--force` |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Aktiviert den Google-Workspace-Export automatisch | optional — auf `1` setzen |
| `GRAPHIFY_TRIAGE_BACKEND` | Backend für `graphify prs --triage` | optional — wird automatisch aus verfügbaren Keys erkannt |
| `GRAPHIFY_TRIAGE_MODEL` | Modell-Override für die Triage | optional — z. B. `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | Auf `1` setzen, um das lokale Query-Log unter `~/.cache/graphify-queries.log` zu aktivieren (erfasst jede query/path/explain-Frage + Corpus-Pfad). Standardmäßig aus — es wird nichts geschrieben, außer du aktivierst es (#1797) | optional |
| `GRAPHIFY_QUERY_LOG` | Aktiviert das Query-Log und schreibt es an diesen Pfad statt an den Standardpfad | optional — aus, solange nicht dies oder `_ENABLE` gesetzt ist |
| `GRAPHIFY_QUERY_LOG_DISABLE` | Auf `1` setzen, um das Query-Log zwangsweise auszuschalten (gewinnt gegenüber den Enable-Variablen) | optional |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | Zeichnet bei aktiviertem Log zusätzlich vollständige Subgraph-Antworten auf (standardmäßig aus) | optional |
| `GRAPHIFY_MAX_GRAPH_BYTES` | Überschreibt die 512-MiB-Größenobergrenze für graph.json — z. B. `700MB`, `2GB` oder reine Bytes | optional — nützlich für sehr große Korpora |
| `GRAPHIFY_MAX_CONTEXTS` | Maximale Anzahl an Nicht-Standard-Projektgraphen, die ein Multi-Projekt-MCP-Server vorhält | optional — Standard: `8`; ungültige Werte verwenden `8`, Werte unter `1` verwenden `1` |
| `GRAPHIFY_LLM_TEMPERATURE` | Überschreibt die LLM-Temperatur für die semantische Extraktion — z. B. `0.7`, oder `none` zum Weglassen | optional — bei o1/o3/o4/gpt-5-Reasoning-Modellen automatisch weggelassen |

---

## Datenschutz

- **Code-Dateien** — werden lokal per tree-sitter verarbeitet. Nichts verlässt deinen Rechner. Ein reiner Code-Korpus benötigt keinen API-Key — `graphify extract` läuft vollständig offline. Bei einem gemischten Repo füge `--code-only` hinzu, um nur den Code zu indizieren und Dokumente/PDFs/Bilder zu überspringen, die sonst ein LLM benötigen würden.
- **Video / Audio** — wird lokal mit faster-whisper transkribiert. Nichts verlässt deinen Rechner.
- **Dokumente, PDFs, Bilder** — werden zur semantischen Extraktion an deinen KI-Assistenten gesendet (über die `/graphify`-Skill, mit dem Modell, das deine IDE-Sitzung ausführt). Headless `graphify extract` benötigt `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), eine laufende Ollama-Instanz (`OLLAMA_BASE_URL`), AWS-Credentials über die Standard-Provider-Chain (Bedrock — kein API-Key nötig, nutzt IAM) oder die `claude`-CLI-Binary (Claude Code — kein API-Key nötig, nutzt dein Claude-Abo). Das Flag `--dedup-llm` nutzt denselben Key.
- **Datenresidenz** — `graphify extract` erkennt automatisch, welcher Provider genutzt wird, je nachdem, welcher API-Key gesetzt ist (Priorität: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). Bei Anforderungen an die Datenresidenz nutze `--backend ollama` (vollständig lokal) oder übergib ein explizites `--backend`-Flag. Kimi (`MOONSHOT_API_KEY`) leitet an Moonshot-AI-Server in China weiter.
- **Keine Telemetrie**, kein Nutzungstracking, keine Analytics.
- **Query-Logging** — jeder Aufruf von `graphify query`, `graphify path`, `graphify explain` und des MCP-`query_graph` wird im JSON-Lines-Format nach `~/.cache/graphify-queries.log` protokolliert (Timestamp, Frage, Corpus, zurückgegebene Knoten, Dauer). Vollständige Subgraph-Antworten werden standardmäßig **nicht** gespeichert. Setze `GRAPHIFY_QUERY_LOG_DISABLE=1`, um dich abzumelden, oder `GRAPHIFY_QUERY_LOG=/dev/null`, um es stillzulegen, ohne den Codepfad zu deaktivieren.

---

## Fehlerbehebung

**`graphify: command not found` nach der Installation**
Die CLI ist installiert, aber ihr bin-Verzeichnis steht nicht im `PATH` deiner Shell. Wähle die passende Lösung für deine Installationsart:
- **uv** (`uv tool install graphifyy`): Der Befehl landet im Tool-bin-Verzeichnis von uv (`~/.local/bin`), das bei einem frischen macOS/zsh-Setup oft nicht im `PATH` steht. Führe `uv tool update-shell` aus und öffne dann ein neues Terminal. (Das Verzeichnis findest du mit `uv tool dir --bin`.)
- **pipx** (`pipx install graphifyy`): führe `pipx ensurepath` aus und öffne dann ein neues Terminal.
- **pip** (`pip install graphifyy`): pip installiert Skripte in ein Benutzer-bin-Verzeichnis, das möglicherweise nicht im `PATH` steht — füge `~/Library/Python/3.x/bin` (macOS) oder `~/.local/bin` (Linux) in deiner `~/.zshrc`/`~/.bashrc` zu deinem `PATH` hinzu, oder führe einfach `python -m graphify` aus.

**`uvx graphify …` oder `uv tool run graphify …` kann `graphify` nicht auflösen**
Das PyPI-Paket heißt `graphifyy`; `graphify` ist nur der Befehl, den es bereitstellt. `uv tool run` behandelt das erste Wort als *Paketnamen*, sucht also nach einem Paket namens `graphify` und meldet `No solution found … no versions of graphify`. Nenne das Paket explizit: `uvx --from graphifyy graphify install` (dasselbe wie `uv tool run --from graphifyy graphify install`). Oder führe einmal `uv tool install graphifyy` aus und rufe danach `graphify` direkt auf.

**`uv run --with graphifyy python -m graphify` führt stillschweigend eine ältere Installation aus**
`uv run` nutzt dein *System*-Python. Lebt dort ebenfalls ein älteres `graphifyy` (z. B. von einem früheren `pip install graphifyy`), kann Python diese Kopie zuerst im `sys.path` finden, und `--with graphifyy` überschreibt sie nicht. Es läuft ohne Fehler, aber du bekommst das Verhalten der *alten* Version — z. B. werden Env-Overrides wie `OPENAI_BASE_URL` stillschweigend ignoriert, sodass Anfragen den Standard-Endpoint treffen und mit einem 401 fehlschlagen, der wie ein falscher Key aussieht. Das Erkennungsmerkmal ist eine Zeile `warning: skill is from graphify <newer>, package is <older>` — das bedeutet, dass eine andere Installation geladen wurde, nicht nur eine veraltete Skill. Prüfe, welche Kopie tatsächlich geladen wurde:
```bash
python -c "import graphify; print(graphify.__file__)"
```
Führe dann den installierten Befehl direkt aus (er nutzt die von uv verwaltete Kopie), oder entferne die veraltete Systemkopie:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` funktioniert, aber der Befehl `graphify` nicht**
Der `PATH` deiner Shell enthält nicht das bin-Verzeichnis, in das der Befehl installiert wurde. Bevorzuge `uv tool install` / `pipx install` gegenüber reinem `pip`, führe dann `uv tool update-shell` / `pipx ensurepath` aus und öffne ein neues Terminal (siehe die Installationshinweise oben).

**`/graphify .` verursacht „path not recognized" in PowerShell**
PowerShell behandelt ein führendes `/` als Pfadtrenner. Nutze unter Windows `graphify .` (ohne Schrägstrich).

**Graph hat nach `--update` oder Rebuild weniger Knoten**
Wenn ein Refactoring Dateien gelöscht hat, bleiben die alten Knoten bestehen. Übergib `--force` (oder setze `GRAPHIFY_FORCE=1`), um auch dann zu überschreiben, wenn der Rebuild weniger Knoten hat.

**`extract` bricht ab mit „extraction was incomplete ... refusing to overwrite"**
Wenn ein Extraktionsdurchlauf abstürzt oder ein Walk den Korpus nicht vollständig lesen kann, wäre der Lauf kleiner als ein vollständiger — deshalb verweigert `graphify extract`, einen größeren bestehenden Graphen mit dem Teilergebnis zu überschreiben (zum Schutz deiner `graph.json`). Behebe die zugrunde liegende Ursache und führe es erneut aus, oder übergib `--allow-partial`, um trotzdem zu überschreiben.

**Graph hat doppelte Knoten für dieselbe Entität (Ghost-Duplikate)**
Ghost-Duplikate (dasselbe Symbol taucht zweimal auf — einmal aus der AST-Extraktion mit Quellort, einmal aus der semantischen Extraktion ohne) werden inzwischen automatisch beim Build zusammengeführt. Siehst du das in einem Graphen, der vor v0.8.33 gebaut wurde, führe eine vollständige erneute Extraktion aus, um aufzuräumen:
```bash
graphify extract . --force
```

**Ollama läuft aus dem VRAM / Context-Window überschritten**
Das KV-Cache-Fenster wird automatisch dimensioniert, kann aber für deine GPU zu groß sein. Verkleinere es:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**Warnungen `LLM returned invalid JSON` / `Unterminated string`**
Die JSON-Antwort des Modells hat das Output-Token-Limit erreicht und wurde mitten in einem String abgeschnitten. graphify erholt sich automatisch (es teilt den Chunk und extrahiert die Hälften erneut, und ein zu großes Einzeldokument wird zunächst an Überschriften-/Absatzgrenzen zerschnitten, sodass die ganze Datei trotzdem abgedeckt wird), diese Warnungen sind also lästig, aber kein Datenverlust. Um das zu reduzieren, erhöhe die Output-Obergrenze oder verkleinere den Output pro Chunk:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
Bei einem Cloud-Gateway wie OpenRouter bevorzuge `--backend openai` (setze `OPENAI_BASE_URL`) gegenüber dem Ollama-Shim — das ist ein saubererer OpenAI-kompatibler Pfad. Hat das Modell eine eigene Max-Output-Obergrenze, ist das Absenken von `--token-budget` der verlässliche Hebel.

**Graph-HTML ist zu groß, um im Browser geöffnet zu werden (>5000 Knoten)**
Überspringe die HTML-Generierung und nutze das JSON direkt:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**`graph.json` hat Konfliktmarkierungen, nachdem zwei Entwickler gleichzeitig committet haben**
Führe `graphify hook install` aus — es richtet einen git-Merge-Driver ein, der `graph.json` automatisch per Union zusammenführt, sodass Konflikte gar nicht erst entstehen.

**Extraktion liefert leere Nodes/Edges für Dokumente oder PDFs**
Dokumente, PDFs und Bilder erfordern einen LLM-Aufruf — reine Code-Korpora benötigen keinen Key. Prüfe, ob dein API-Key gesetzt und das Backend korrekt ist:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**Warnung „Skill version mismatch" in deiner IDE**
Deine installierte graphify-Version unterscheidet sich von der Skill-Datei. Aktualisieren:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**Claude-Code-Prompt-Cache wird nach jedem `graphify extract` invalidiert**
Graphify schreibt Output-Dateien (`graph.json`, `graphify-out/`) in den Workspace. Sind diese Pfade nicht ignoriert, invalidiert jeder Schreibvorgang den Prompt-Cache von Claude Code und erzwingt beim nächsten Turn einen vollständigen Re-Upload zu Cache-Write-Raten. Füge sie zu `.claudeignore` hinzu:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## Vollständige Befehlsreferenz

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

> **Community-Namen:** Innerhalb eines Agenten (Claude Code, Gemini CLI) benennt der Agent die Communities selbst. Führst du die reine CLI aus, benennt `cluster-only` sie automatisch mit dem konfigurierten Backend (integriert oder ein eigener OpenAI-kompatibler Provider) — übergib `--no-label`, um `Community N` zu behalten, oder führe `graphify label` aus, um Namen bei Bedarf (neu) zu generieren.

---

## Mehr erfahren

- [So funktioniert es](../how-it-works.md) — die Extraktions-Pipeline, Community-Erkennung, Konfidenz-Scoring, Benchmarks
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — Modulaufteilung, wie man eine Sprache hinzufügt
- [Optionale Integrationen](../docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — das Buch über die Ideen hinter graphify, die Architektur von Anfang bis Ende

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) ist die dauerhaft aktive Schicht, die auf graphify aufbaut — sie wendet denselben Graph-Ansatz auf deinen gesamten Arbeitskontext an: Meetings, Dateien, Dokumente und Code, kontinuierlich im Hintergrund aktualisiert.

Gebaut für Menschen und Teams, deren Arbeit sich über Hunderte von Konversationen und Dokumenten verteilt, die sie nie vollständig rekonstruieren können.

**[Trage dich auf der Warteliste bei graphify.com ein](https://graphify.com).** Kostenlose Testphase startet in Kürze.

---

<details>
<summary>Mitwirken</summary>

### Entwicklungsumgebung einrichten

Das Projekt nutzt [uv](https://docs.astral.sh/uv/) für den Entwicklungsworkflow. Installiere es einmal, dann:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

Die editable Installation überprüfen:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### Tests ausführen

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> Hinweis für macOS: Die Testsuite enthält sowohl `sample.f90`- als auch `sample.F90`-Fixtures. Diese kollidieren auf case-insensitiven HFS+-/APFS-Dateisystemen. Führe die Tests auf Linux oder in einem Docker-Container aus, wenn du beide Fortran-Varianten gleichzeitig testen musst.

### Git-Workflow

- Die aktive Entwicklung findet auf dem `v8`-Branch statt.
- Commit-Stil: `fix: <description>` / `feat: <description>` / `docs: <description>`
- Bevor du einen PR öffnest, führe `uv run pytest tests/ -q` aus und stelle sicher, dass er erfolgreich durchläuft.
- Füge für jeden neuen Sprach-Extractor eine Fixture-Datei in `tests/fixtures/` und Tests in `tests/test_languages.py` hinzu.

### Was du beitragen kannst

**Ausgearbeitete Beispiele** sind der nützlichste Beitrag. Führe `/graphify` auf einem echten Korpus aus, speichere die Ausgabe unter `worked/{slug}/`, schreibe eine ehrliche `review.md`, die festhält, was der Graph richtig und falsch gemacht hat, und öffne einen PR.

**Extraktionsfehler** — öffne ein Issue mit der Eingabedatei, dem Cache-Eintrag (`graphify-out/cache/`) und dem, was fehlte oder falsch war.

Siehe [ARCHITECTURE.md](../../ARCHITECTURE.md) für Modulverantwortlichkeiten und wie man eine Sprache hinzufügt.

</details>
