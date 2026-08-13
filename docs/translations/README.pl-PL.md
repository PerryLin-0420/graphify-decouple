<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>Fork <a href="https://github.com/Graphify-Labs/graphify">graphify</a> dodający <code>graphify decouple</code></b> — kandydaci do Extract-Class ocenieni pod kątem ryzyka dla god objects, bez LLM, ponownie zweryfikowani względem rzeczywistego kodu źródłowego (nie tylko grafu wywołań), zanim cokolwiek zostanie zasugerowane. Zobacz <a href="#decouple-risk-scored-extract-class-candidates">Decouple: kandydaci Extract-Class z oceną ryzyka</a> poniżej.
</p>

<div align="center">
<details><summary><b>Przeczytaj to w innych językach</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>Wczesny dostęp do platformy graphify jest otwarty przed publiczną premierą v1: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

Wpisz `/graphify` w swoim asystencie AI, a zmapuje cały twój projekt (kod, dokumenty, PDF-y, obrazy, wideo) w **graf wiedzy**, który możesz **przeszukiwać zapytaniami zamiast grepować** pliki.

- **Mapowanie kodu za darmo, w pełni lokalnie.** Kod jest parsowany za pomocą tree-sitter AST: deterministycznie, bez LLM, nic nie opuszcza twojej maszyny. (Dokumenty, PDF-y, obrazy i wideo używają modelu twojego asystenta lub skonfigurowanego klucza API do przebiegu semantycznego.)
- **Każda krawędź jest wyjaśniona.** Każde połączenie jest oznaczone jako `EXTRACTED` (jawnie obecne w źródle) lub `INFERRED` (wywnioskowane przez graphify), więc wiesz, co zostało odczytane bezpośrednio, a co wywnioskowane.
- **To nie jest indeks wektorowy.** Bez embeddings, bez vector store: prawdziwy graf, który przemierzasz. Zadaj pytanie, prześledź ścieżkę między dwiema rzeczami, albo poproś o wyjaśnienie jednej koncepcji.

> Chcesz, żeby to działało zawsze, aktualizując się w tle w twoim kodzie, dokumentach i spotkaniach, zamiast tylko na żądanie? To właśnie budujemy w **[graphify.com](https://graphify.com)**, a wczesny dostęp jest już otwarty na **[app.graphify.com](https://app.graphify.com/login)**.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="graphify's interactive graph.html showing the FastAPI codebase as a force-directed knowledge graph with a legend of detected communities" width="900">
</p>
<p align="center">
  <em>Kod źródłowy FastAPI zmapowany przez graphify. Każdy węzeł to koncepcja, kolory to wykryte społeczności, a całość jest klikalna w graph.html.</em>
</p>

**Zacznij** (30 sekund):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

Następnie, w swoim asystencie AI:

```
/graphify .
```

To wszystko. Otrzymujesz **trzy pliki**:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**Działa w** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot i ponad 15 innych — [wybierz swoją platformę](#install).

---

## Zobacz to w akcji

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="graphify path query: a terminal asks for the shortest path between FastAPI and ModelField, and the answer lights up hop by hop across the knowledge graph" width="900">
</p>

Po zbudowaniu grafu odpytujesz go zamiast czytać pliki. Prawdziwe dane wyjściowe, graphify uruchomiony na pokazanym powyżej kodzie FastAPI:

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

Każda krawędź niesie **znacznik pewności** (`EXTRACTED` = jawny w źródle, `INFERRED` = wywnioskowany przez rozwiązanie), więc wiesz, co zostało odczytane bezpośrednio, a co wywnioskowane. `graphify query "<question>"` zwraca zawężony podgraf dla pytania w prostym języku, a `graphify path A B` śledzi, jak dwie rzeczy się łączą.

---

## Decouple: kandydaci Extract-Class z oceną ryzyka

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: MainWindow god node splitting into risk-scored candidate classes, with a shared-state warning between two of them" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: MainWindow's 5 proposed classes, Node Info panel open on Main Window Axis and Range Controls showing a 0.608 state overlap with Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>DECOUPLE.html z rzeczywistego uruchomienia — kliknięcie proponowanej klasy pokazuje dokładnie, z jaką inną klasą dzieli stan, i co dokładnie jest współdzielone.</em>
</p>

Ta sama strona renderuje też sam podział. Przełączenie **Preview decoupled view** zamienia własne metody klasy god na proponowane klasy i przekierowuje krawędzie w miejscu — zmianę okablowania, a nie odrysowany diagram:

| Przed — klasa god dzisiaj | Po — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html before the toggle: a single MainWindow hub node with its own methods fanned out around it" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html after the toggle: the same node reduced to 5 diamond-shaped proposed classes, green dashed edges showing which methods were extracted into each, red edges showing shared instance state between two of them" width="440"> |
| Jeden węzeł z 47 własnymi metodami, z których każda jest osiągalna tylko przez klasę. | Proponowane klasy. Zielona przerywana = co wyekstrahowano do każdej; czerwona = stan instancji, który dwie z nich nadal współdzielą, co dokładnie decyduje między `split` a `keep_as_is`. Rysowani są tylko kandydaci, którzy przekraczają próg ryzyka — tutaj 5 z 6, dlatego jedna metoda nie ma rombu, na którym mogłaby wylądować. |

`graphify decouple` znajduje god objects i mówi, czy ich podział rzeczywiście się opłaca — nie tylko, że są duże.

Tryb awarii, który to wychwytuje: klasa z 47 metodami, którą grupowanie oparte na grafie wywołań chętnie dzieli na 5 schludnie wyglądających grup, z których wszystkie nadal czytają i zapisują dokładnie ten sam stan instancji `self._chart_style` / `self._crosshair` pod spodem. Wysyłając taki podział, nie odsprzęgłeś niczego — po prostu przeniosłeś metody do nowych plików, które nadal nie mogą być testowane, zmieniane ani rozumiane niezależnie, ponieważ wszystkie nadal potrzebują tego samego współdzielonego stanu przekazywanego z powrotem. Narzędzie patrzące tylko na graf wywołań w ogóle tego nie widzi; musi wrócić do rzeczywistego źródła.

**Dwie kontrole, obie bez LLM, obie deterministyczne:**

1. **Czy to w ogóle God Object?** Węzeł o wysokim stopniu może być prawdziwym God Object (wiele WŁASNYCH metod, rozłożonych na niepowiązane odpowiedzialności — Extract Class ma zastosowanie) albo nadmiernie referencjonowanym hubem/modelem danych (mało własnych metod, głównie *przychodzące* referencje — podział jego ciała nic nie daje; naprawą jest zawężenie jego interfejsu, nie ekstrakcja klasy). `classify_god_node` odróżnia je za pomocą `member_ratio`, nie surowego stopnia — różnica, która chroni `TraceSource` (84 krawędzie, ale tylko 6 własnych metod) przed fałszywą sugestią podziału, którą `MainWindow` (88 krawędzi, 47 własnych metod) słusznie otrzymuje.
2. **Czy podział rzeczywiście zmniejszyłby sprzężenie?** `risk_before` (obecny rozmiar/sprzężenie/fragmentacja węzła god) jest porównywany z `risk_after` — NOWYM ryzykiem, które sam podział by wprowadził: wywołania między grupami, które były niewidocznymi krawędziami wewnątrzklasowymi, a stają się jawnymi zależnościami międzyklasowymi, wywołujący, którzy teraz musieliby zależeć od więcej niż jednej nowej klasy, oraz — kontrola, której graf wywołań strukturalnie nie może wykonać — ile stanu instancji `self`/`this` (odczyty, zapisy i współdzielone wywołania metod pomocniczych, ważone osobno: współdzielony **zapis** jest punktowany wyżej niż współdzielony odczyt) mają rzeczywiście wspólnego proponowane grupy. To ponownie parsuje własny plik źródłowy węzła god bezpośrednio za pomocą tree-sitter; nie polega na własnym wyekstrahowanym grafie graphify, który nigdy nie rejestruje dostępu na poziomie pola dla żadnego języka. Tylko gdy `risk_after` spada poniżej progu względem `risk_before`, plan rekomenduje `split` — w przeciwnym razie jest to `marginal` lub `keep_as_is`, a zniechęcony kandydat jest raportowany jako liczba, nigdy rysowany jako kształt, który musisz zgadywać na oko.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

Generuje trzy pliki obok `graph.json`:

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

**Pokrycie języków dla kontroli współdzielenia stanu** (powyższa klasyfikacja oparta tylko na grafie wywołań działa dla każdego języka, który graphify ekstrahuje; ta tabela dotyczy konkretnie ponownego parsowania źródła, które weryfikuje nakładanie się stanu `self`/`this`):

| Język | Wspierany | Uwagi |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` jest własnym węzłem AST, nie opakowanym dostępem do pola — obsługiwane jawnie |
| C# | ✅ | |
| Rust | ✅ | `self.x` przez bloki `impl` |
| Ruby | ✅ | `@x` (dominujący idiom) + wywołania `self.foo` |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | rozwiązywanie odbiornika per metoda — Go nie ma słowa kluczowego `self`/`this`, więc nazwa odbiornika (`f` w `func (f *Foo) M()`) jest rozwiązywana od nowa dla każdej metody |
| C | ❌ | parametr wskaźnika struktury nie ma znacznika składniowego odróżniającego go od jakiegokolwiek innego parametru — brak wiarygodnego sygnału bez pełnej inferencji typów |

Węzeł god w niewspieranym języku, lub taki, którego źródła nie da się odczytać, jest oznaczany jako `state_analysis: "skipped"` — klasyfikacja i wynik grafu wywołań nadal działają, ale rekomendacja opiera się wyłącznie na grafie wywołań zamiast cicho zakładać, że kontrola stanu przeszła.

---

## Co to robi

Co dostajesz od razu:

| Możliwość | Co dostajesz |
|---|---|
| **God nodes** | Najbardziej połączone koncepcje, więc widzisz, przez co wszystko przepływa |
| **Społeczności** | Graf podzielony na podsystemy (Leiden), z etykietami bez LLM |
| **Linki między plikami** | `calls` / `imports` / `inherits` / `mixes_in` rozwiązane w ~40 językach za pomocą tree-sitter AST |
| **Zapytanie, ścieżka, wyjaśnienie** | Zadaj pytanie, prześledź ścieżkę między dwiema rzeczami, lub wyjaśnij jedną koncepcję, wszystko na `graph.json` |
| **Uzasadnienie + odniesienia do dokumentów** | Komentarze `# NOTE:` / `# WHY:` i cytaty ADR/RFC stają się węzłami pierwszej klasy powiązanymi z kodem |
| **Poza kodem** | Dokumenty, PDF-y, obrazy i wideo/audio wszystkie mapują się do tego samego grafu |
| **Lokalnie przede wszystkim** | Kod jest parsowany lokalnie za pomocą tree-sitter (bez LLM, nic nie opuszcza twojej maszyny); tylko przebieg semantyczny nad dokumentami/mediami wywołuje backend, i tylko jeśli go skonfigurujesz |

---

## Testy porównawcze (Benchmarks)

| Benchmark | Metryka | graphify | Konkurencja |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | dokładność QA | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | dokładność QA | **76%** | remis z dense RAG |
| Budowanie grafu | kredyty LLM | **0** | za token dla większości systemów |

Każdy system działał na tej samej infrastrukturze z tym samym modelem i budżetami, oceniany przez sędziego zwalidowanego na ślepo względem drugiego sędziego (90.6% zgodności, kappa Cohena 0.81). Pełne tabele per system, wynik code-intelligence i komendy do reprodukcji: **[BENCHMARKS.md](./BENCHMARKS.md)**.

---

## Wymagania wstępne

| Wymaganie | Minimum | Sprawdzenie | Instalacja |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(zalecane)* | dowolna | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(alternatywa)* | dowolna | `pipx --version` | `pip install pipx` |

**Szybka instalacja macOS (Homebrew):**
```bash
brew install python@3.12 uv
```

**Szybka instalacja Windows:**
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

## Instalacja

> **Oficjalny pakiet:** Pakiet PyPI to `graphifyy` (podwójne y). Inne pakiety `graphify*` w PyPI nie są powiązane. Komenda CLI to nadal `graphify`.

**Krok 1 — zainstaluj pakiet:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**Krok 2 — zarejestruj skill w swoim asystencie AI:**

```bash
graphify install
```

To wszystko. Otwórz swojego asystenta AI i wpisz `/graphify .`

Aby zainstalować skill asystenta w bieżącym repozytorium zamiast w profilu użytkownika, dodaj `--project`:

```bash
graphify install --project
graphify install --project --platform codex
```

Instalacje w zakresie projektu zapisują pliki w bieżącym katalogu, na przykład `.claude/skills/graphify/SKILL.md` lub `.agents/skills/graphify/SKILL.md` (plus dodatek `references/`, który skill ładuje na żądanie), i wypisują wskazówkę `git add` dla plików, które można commitować. Komendy per platforma wspierające instalacje w zakresie projektu akceptują tę samą flagę, na przykład `graphify claude install --project` lub `graphify codex install --project`.

> **Uwaga PowerShell:** Użyj `graphify .` nie `/graphify .` — początkowy ukośnik jest separatorem ścieżki w PowerShell.

> **`graphify: command not found`?** `uv tool install` / `pipx install` umieszczają komendę `graphify` w katalogu bin swoich narzędzi (`~/.local/bin`). Jeśli twoja powłoka nie może jej znaleźć zaraz po instalacji — częste na świeżej instalacji macOS + zsh — ten katalog nie jest jeszcze w `PATH`: uruchom `uv tool update-shell` (lub `pipx ensurepath`), potem otwórz nowy terminal. Z prostym `pip`, dodaj `~/.local/bin` (Linux) lub `~/Library/Python/3.x/bin` (Mac) do PATH, lub uruchom `python -m graphify`.

> **Uruchamianie z `uvx` / `uv tool run` zamiast instalacji?** Nazwij pakiet, nie komendę: `uvx --from graphifyy graphify install`. Samo `uvx graphify …` zawodzi (`No solution found … no versions of graphify`), ponieważ `uv tool run` czyta pierwsze słowo jako *pakiet*, a pakiet to `graphifyy` — komenda `graphify` żyje wewnątrz niego.

> **Unikaj `pip install` na Mac/Windows** jeśli to możliwe. Skill rozwiązuje Pythona w czasie wykonania z `graphify-out/.graphify_python`; jeśli wskazuje na inne środowisko niż to, gdzie `pip` zainstalował pakiet, dostaniesz `ModuleNotFoundError: No module named 'graphify'`. `uv tool install` i `pipx install` izolują pakiet we własnym środowisku i całkowicie tego unikają.

> **Git hooks i uv tool / pipx:** `graphify hook install` osadza ścieżkę bieżącego interpretera bezpośrednio w skryptach hooka podczas instalacji, więc hook post-commit działa poprawnie nawet w graficznych klientach git i runnerach CI, gdzie `~/.local/bin` nie jest w PATH. Jeśli reinstalujesz lub aktualizujesz graphify, uruchom ponownie `graphify hook install`, aby odświeżyć osadzoną ścieżkę.

> **Tryb ścisły (Claude Code):** `graphify install --project --strict` sprawia, że asystent faktycznie używa grafu. Domyślna instalacja *zachęca* do uruchomienia `graphify query` przed czytaniem plików; tryb ścisły *blokuje* pierwszy surowy odczyt źródła w sesji i przekierowuje go do grafu, potem wraca do zachęty (więc uruchamia się co najwyżej raz na sesję i nigdy się nie zawiesza). Przełącz w czasie wykonania za pomocą `GRAPHIFY_HOOK_STRICT=1`/`0`; domyślna instalacja pozostaje niezmieniona (łagodna zachęta).

<details>
<summary><b>Wybierz swoją platformę</b> (20+ asystentów, kliknij, aby rozwinąć)</summary>

| Platforma | Komenda instalacji |
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

Użytkownicy Codex potrzebują też `multi_agent = true` pod `[features]` w `~/.codex/config.toml` dla równoległej ekstrakcji. CodeBuddy używa tego samego mechanizmu Agent tool i PreToolUse hook co Claude Code. Factory Droid używa narzędzia `Task` do równoległego dispatchu subagentów. OpenClaw i Aider używają sekwencyjnej ekstrakcji (wsparcie dla równoległych agentów jest wciąż wczesne na tych platformach). Trae używa Agent tool do równoległego dispatchu subagentów i **nie** wspiera hooków `PreToolUse`, więc AGENTS.md jest mechanizmem zawsze aktywnym.

`--platform agents` (alias `--platform skills`) celuje w ogólne, wieloframeworkowe lokalizacje [Agent-Skills](https://github.com/anthropics/skills): globalny dla użytkownika `~/.agents/skills/` ze specyfikacji (czytany przez `npx skills` i zgodne frameworki) dla instalacji globalnej, oraz `./.agents/skills/` dla instalacji projektu (`--project`). Samo `graphify install` pozostaje jednoplatformowe (Claude Code) z założenia — użyj nazwanej platformy `agents`, gdy chcesz, aby skill był wykrywalny przez dowolny framework czytający `.agents/skills`.

> Codex używa `$graphify` zamiast `/graphify`.

</details>

<details>
<summary><b>Opcjonalne dodatki</b> (zainstaluj tylko to, czego potrzebujesz)</summary>

| Dodatek | Co dodaje | Instalacja |
|---|---|---|
| `pdf` | Ekstrakcja PDF | `uv tool install "graphifyy[pdf]"` |
| `office` | Wsparcie `.docx` i `.xlsx` | `uv tool install "graphifyy[office]"` |
| `google` | Renderowanie Google Sheets | `uv tool install "graphifyy[google]"` |
| `video` | Transkrypcja wideo/audio (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | Serwer MCP stdio | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Wsparcie push do Neo4j | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | Wsparcie push do FalkorDB | `uv tool install "graphifyy[falkordb]"` |
| `svg` | Eksport grafu SVG | `uv tool install "graphifyy[svg]"` |
| `leiden` | Wykrywanie społeczności Leiden (tylko Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Lokalna inferencja Ollama | `uv tool install "graphifyy[ollama]"` |
| `openai` | OpenAI / API kompatybilne z OpenAI | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic Claude API (`--backend claude`, używa `ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (używa IAM, bez klucza API) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, używa `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "graphifyy[openai]"` |
| `sql` | Ekstrakcja schematu SQL | `uv tool install "graphifyy[sql]"` |
| `postgres` | Żywa introspekcja PostgreSQL (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | Ekstrakcja AST BYOND DreamMaker `.dm`/`.dme` (może wymagać kompilatora C + `python3-dev`, jeśli żaden wheel nie pasuje do twojej platformy) | `uv tool install "graphifyy[dm]"` |
| `terraform` | Ekstrakcja AST Terraform / HCL `.tf`/`.tfvars`/`.hcl` | `uv tool install "graphifyy[terraform]"` |
| `pascal` | Ekstrakcja AST Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` (dokładniejsze krawędzie `calls`/`inherits`; przechodzi na ekstraktor regex, gdy brak) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | Segmentacja zapytań chińskich (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | Wszystko powyżej | `uv tool install "graphifyy[all]"` |

</details>

---

## Spraw, żeby twój asystent zawsze używał grafu

Uruchom to raz w swoim projekcie po zbudowaniu grafu:

| Platforma | Komenda |
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

To zapisuje mały plik konfiguracyjny, który mówi twojemu asystentowi, żeby konsultował graf wiedzy w kwestiach dotyczących kodu, preferując zawężone zapytania jak `graphify query "<question>"` zamiast czytania pełnego raportu lub grepowania surowych plików.

- **Platformy z hookami** (Claude Code, Gemini CLI): hook uruchamia się automatycznie przed wywołaniami narzędzi typu wyszukiwanie (a na Claude Code, przed czytaniem plików źródłowych pojedynczo przez narzędzia Read/Glob) i zachęca asystenta w stronę ścieżki grafu.
- **Platformy z plikami instrukcji** (Codex, OpenCode, Cursor, itp.): trwałe pliki instrukcji (`AGENTS.md`, `.cursor/rules/`, itp.) dostarczają tę samą wskazówkę priorytetu zapytań.

`GRAPH_REPORT.md` nadal jest dostępny do szerokiego przeglądu architektury.

**CodeBuddy** robi te same dwie rzeczy co Claude Code: zapisuje sekcję `CODEBUDDY.md` mówiącą CodeBuddy, żeby czytał `graphify-out/GRAPH_REPORT.md` przed odpowiadaniem na pytania architektoniczne, i instaluje hooki `PreToolUse` (`.codebuddy/settings.json`), które uruchamiają się przed komendami wyszukiwania Bash i odczytami plików, zachęcając w stronę `graphify query`.

**Codex** zapisuje do `AGENTS.md`, co faktycznie niesie stałą wskazówkę grafu na tej platformie. `graphify codex install` rejestruje też hook `PreToolUse` w `.codex/hooks.json` (`graphify hook-check`), ale ten wpis jest celowo **no-op**: Codex Desktop odrzuca `hookSpecificOutput.additionalContext` na `PreToolUse`, więc wysłanie tam zachęty zepsułoby wywołania narzędzia Bash. W przeciwieństwie do Claude Code, gdzie hook (`graphify hook-guard`) robi zachętę, na Codex hook uruchamia się i celowo nic nie robi, a `AGENTS.md` jest mechanizmem zawsze aktywnym.

**Kilo Code** instaluje skill Graphify do `~/.config/kilo/skills/graphify/SKILL.md` i natywną komendę `/graphify` do `~/.config/kilo/command/graphify.md`. `graphify kilo install` zapisuje też `AGENTS.md` plus natywny plugin `tool.execute.before` (`.kilo/plugins/graphify.js` + rejestrację `.kilo/kilo.json` lub `.kilo/kilo.jsonc`), więc Kilo dostaje to samo zawsze aktywne przypomnienie o grafie przez natywną konfigurację `.kilo`.

**Cursor** zapisuje `.cursor/rules/graphify.mdc` z `alwaysApply: true`, więc Cursor włącza to do każdej konwersacji automatycznie, bez potrzeby hooka.

Aby usunąć graphify ze wszystkich platform naraz: `graphify uninstall` (dodaj `--purge`, żeby też usunąć `graphify-out/`). Albo użyj komendy per platforma (np. `graphify claude uninstall`).

---

## Co jest w raporcie

- **God nodes** — najbardziej połączone koncepcje w twoim projekcie. Wszystko przez nie przepływa.
- **Zaskakujące połączenia** — linki między rzeczami żyjącymi w różnych plikach lub modułach. Uszeregowane według tego, jak nieoczekiwane są.
- **"Dlaczego"** — komentarze w kodzie (`# NOTE:`, `# WHY:`, `# HACK:`), docstringi i uzasadnienie projektowe z dokumentów są ekstrahowane jako osobne węzły powiązane z kodem, który wyjaśniają.
- **Sugerowane pytania** — 4–5 pytań, na które graf jest wyjątkowo dobrze przygotowany odpowiedzieć.
- **Znaczniki pewności** — każda wywnioskowana relacja jest oznaczona `EXTRACTED`, `INFERRED`, lub `AMBIGUOUS`. Zawsze wiesz, co zostało znalezione, a co odgadnięte.

---

## Jakie pliki obsługuje

| Typ | Rozszerzenia |
|------|-----------|
| Kod (36 gramatyk tree-sitter) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme` wymaga `uv tool install graphifyy[dm]`; `.mts`/`.cts` ponownie używają gramatyki TypeScript, `.cc`/`.cxx` i CUDA `.cu`/`.cuh` oraz Metal `.metal` ponownie używają gramatyki C++) |
| Salesforce Apex | `.cls .trigger` (oparte na regex; klasy, interfejsy, enumy, metody, triggery, krawędzie SOQL/DML) |
| Terraform / HCL | `.tf .tfvars .hcl` (wymaga `uv tool install graphifyy[terraform]`) |
| Konfiguracje MCP | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — ekstrahuje węzły serwerów, referencje pakietów, wymagania zmiennych środowiskowych |
| Manifesty pakietów | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — jeden kanoniczny węzeł pakietu na pakiet (po nazwie) plus krawędzie `depends_on`, więc pakiet referencjonowany przez wiele manifestów to jeden hub |
| Dokumenty | `.md .mdx .qmd .html .txt .rst .yaml .yml` (linki markdown `[text](./other.md)` i `[[wikilinks]]` stają się krawędziami `references` między dokumentami) |
| Office | `.docx .xlsx` (wymaga `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (opt-in; wymaga autoryzacji `gws` i `--google-workspace`; Sheets wymagają `uv tool install graphifyy[google]`) |
| PDF-y | `.pdf` |
| Obrazy | `.png .jpg .webp .gif` |
| Wideo / Audio | `.mp4 .mov .mp3 .wav` i więcej (wymaga `uv tool install graphifyy[video]`) |
| YouTube / URL-e | dowolny URL wideo (wymaga `uv tool install graphifyy[video]`) |

Kod jest ekstrahowany **lokalnie bez wywołań API** (AST przez tree-sitter). Wszystko inne przechodzi przez API modelu twojego asystenta AI.

Pliki `.gdoc`, `.gsheet`, i `.gslides` z Google Drive na komputer to wskaźniki skrótów, nie zawartość dokumentu. Aby uwzględnić natywne Google Docs, Sheets i Slides w ekstrakcji headless, zainstaluj i uwierzytelnij [`gws` CLI](https://github.com/googleworkspace/cli), potem uruchom:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

Możesz też ustawić `GRAPHIFY_GOOGLE_WORKSPACE=1`. Graphify eksportuje skróty do `graphify-out/converted/` jako dodatki Markdown, potem ekstrahuje te pliki.

---

## Częste komendy

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

Zobacz [Decouple: kandydaci Extract-Class z oceną ryzyka](#decouple-risk-scored-extract-class-candidates) powyżej, lub [pełne odniesienie komend](#full-command-reference) poniżej.

---

## Ignorowanie plików

Utwórz `.graphifyignore` w katalogu głównym projektu — ta sama składnia co `.gitignore`, wraz z negacją `!`.

**`.gitignore` jest respektowany automatycznie.** graphify czyta `.gitignore` w każdym katalogu. Jeśli obecny jest też `.graphifyignore`, oba są **scalane** — wzorce `.graphifyignore` są oceniane jako ostatnie, więc wygrywają w konfliktach (włącznie z negacjami `!`). Dodanie `.graphifyignore` tylko wyklucza więcej; nigdy nie włącza ponownie pliku, który twój `.gitignore` już wykluczył. Zakres podkatalogu działa tak samo jak w git — plik ignorowania wpływa tylko na własne poddrzewo.

Przekaż `--no-gitignore` do `graphify extract`, gdy wygenerowany lub transpilowany kod ignorowany przez git powinien należeć do grafu. To wyłącza `.gitignore` i `.git/info/exclude`; `.graphifyignore` nadal obowiązuje.

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

## Konfiguracja zespołu

`graphify-out/` jest przeznaczony do commitowania do git, żeby każdy w zespole zaczynał z mapą.

**Zalecane dodatki do `.gitignore`:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` jest teraz przenośny — klucze są przechowywane jako ścieżki względne i przekotwiczane przy wczytywaniu, więc commitowanie go jest bezpieczne i pozwala uniknąć pełnej przebudowy przy pierwszym checkout.

**Przepływ pracy:**
1. Jedna osoba uruchamia `/graphify .` i commituje `graphify-out/`.
2. Wszyscy pullują — ich asystent od razu czyta graf.
3. Uruchom `graphify hook install`, żeby automatycznie przebudowywać po każdym commicie (tylko AST, bez kosztu API). To też ustawia git merge driver, więc `graph.json` nigdy nie zostaje z markerami konfliktu — dwóch deweloperów commitujących równolegle dostaje swoje grafy automatycznie scalone.
4. Kiedy zmieniają się dokumenty lub artykuły, uruchom `/graphify --update`, żeby odświeżyć te węzły.

---

## Bezpośrednie użycie grafu

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

Serwer MCP daje twojemu asystentowi ustrukturyzowany dostęp: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Współdzielony serwer HTTP

`--transport stdio` (domyślny) tworzy jeden lokalny serwer na dewelopera. `--transport http` serwuje te same narzędzia przez transport MCP Streamable HTTP, więc jeden współdzielony proces może serwować graf dla całego zespołu — klienci kierują konfigurację MCP swojego IDE na `http://<host>:8080/mcp` zamiast uruchamiać graphify lokalnie.

| Flaga | Domyślna | Cel |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Transport do serwowania |
| `--host` | `127.0.0.1` | Host bindowania HTTP (użyj `0.0.0.0`, żeby wystawić poza localhost) |
| `--port` | `8080` | Port bindowania HTTP |
| `--api-key` | env `GRAPHIFY_API_KEY` | Wymaga `Authorization: Bearer <key>` (lub `X-API-Key`) |
| `--path` | `/mcp` | Ścieżka montowania HTTP |
| `--json-response` | off | Zwraca zwykły JSON zamiast strumieni SSE |
| `--stateless` | off | Bez stanu per sesja (dla deploymentów load-balanced / CI) |
| `--session-timeout` | `3600` | Usuwa nieaktywne sesje stanowe po N sekundach (`0` wyłącza) |

Domyślne bindowanie `127.0.0.1` jest tylko loopback. Ustaw `--host 0.0.0.0` **i** `--api-key` razem przy wystawianiu na współdzielonym hoście. Uruchom w kontenerze:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **Uwaga WSL / Linux:** Ubuntu dostarcza `python3`, nie `python`. Użyj venv, żeby uniknąć konfliktów:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## Zmienne środowiskowe

Są potrzebne tylko do **ekstrakcji headless / CI** (`graphify extract`). Podczas uruchamiania przez skill `/graphify` wewnątrz IDE, API modelu jest dostarczane przez twoją sesję IDE — nie są potrzebne dodatkowe klucze.

| Zmienna | Do czego | Kiedy wymagana |
|---|---|---|
| `ANTHROPIC_API_KEY` | Backend Claude (Anthropic) | `--backend claude` |
| `ANTHROPIC_BASE_URL` | URL endpointu kompatybilnego z Anthropic (proxy LiteLLM, bramy, ...) | `--backend claude` (domyślnie: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Nazwa modelu dla backendu Claude — dla własnych endpointów, użyj nazwy/aliasu modelu, który wystawia twój serwer | `--backend claude` (domyślnie: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` lub `GOOGLE_API_KEY` | Backend Google Gemini | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI lub API kompatybilne z OpenAI | `--backend openai` (lokalne serwery akceptują dowolną niepustą wartość) |
| `OPENAI_BASE_URL` | URL serwera kompatybilnego z OpenAI (llama.cpp, vLLM, LM Studio, ...) | `--backend openai` (domyślnie: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | Nazwa modelu dla backendu OpenAI — dla serwerów self-hosted, użyj nazwy/aliasu modelu, który wystawia twój serwer (sprawdź jego endpoint `/v1/models`), np. `LFM2.5-8B-A1B-UD-Q4_K_XL` dla llama.cpp | `--backend openai` (domyślnie: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | Backend DeepSeek | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Backend Kimi Code | `--backend kimi` |
| `OLLAMA_BASE_URL` | URL lokalnej inferencji Ollama | `--backend ollama` (domyślnie: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Nazwa modelu Ollama | `--backend ollama` (domyślnie: auto-detekcja) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Nadpisanie rozmiaru okna KV-cache Ollama | opcjonalne — domyślnie auto-rozmiar |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Minuty utrzymania załadowanego modelu Ollama | opcjonalne — ustaw `0`, żeby zwalniać po każdym fragmencie |
| `AZURE_OPENAI_API_KEY` | Backend Azure OpenAI Service | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | URL endpointu zasobu Azure | `--backend azure` (wymagany razem z kluczem API) |
| `AZURE_OPENAI_API_VERSION` | Nadpisanie wersji API Azure | opcjonalne — domyślnie `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` lub `GRAPHIFY_AZURE_MODEL` | Nazwa deploymentu Azure | opcjonalne — domyślnie `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — standardowy łańcuch poświadczeń | `--backend bedrock` (bez klucza API, używa IAM) |
| `GRAPHIFY_MAX_WORKERS` | Liczba wątków równoległości AST | opcjonalne — też flaga `--max-workers` |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Podnieś limit wyjścia dla gęstych korpusów | opcjonalne — np. `32768` dla dużych plików |
| `GRAPHIFY_API_TIMEOUT` | Timeout per wywołanie w sekundach dla HTTP, claude-cli, Anthropic SDK i backendów Bedrock (domyślnie: 600) | opcjonalne — też flaga `--api-timeout` |
| `GRAPHIFY_MAX_RETRIES` | Ile razy ponowić żądanie rate-limited (429) przed poddaniem się (domyślnie: 6; respektuje `Retry-After`) | opcjonalne — podnieś dla ścisłych limitów per organizacja (np. kimi); `0` wyłącza |
| `GRAPHIFY_FORCE` | Wymuś przebudowę grafu nawet z mniejszą liczbą węzłów | opcjonalne — też flaga `--force` |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Auto-włącz eksport Google Workspace | opcjonalne — ustaw na `1` |
| `GRAPHIFY_TRIAGE_BACKEND` | Backend dla `graphify prs --triage` | opcjonalne — auto-wykrywany z dostępnych kluczy |
| `GRAPHIFY_TRIAGE_MODEL` | Nadpisanie modelu dla triage | opcjonalne — np. `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | Ustaw na `1`, żeby włączyć lokalny log zapytań w `~/.cache/graphify-queries.log` (rejestruje każde pytanie query/path/explain + korpus). Domyślnie wyłączony — nic nie jest zapisywane, chyba że dołączysz (#1797) | opcjonalne |
| `GRAPHIFY_QUERY_LOG` | Włącza log zapytań i zapisuje go w tej ścieżce zamiast domyślnej | opcjonalne — off, chyba że to lub `_ENABLE` jest ustawione |
| `GRAPHIFY_QUERY_LOG_DISABLE` | Ustaw na `1`, żeby wymusić wyłączenie logu zapytań (wygrywa nad zmiennymi enable) | opcjonalne |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | Kiedy log jest włączony, rejestruje też pełne odpowiedzi podgrafu (domyślnie off) | opcjonalne |
| `GRAPHIFY_MAX_GRAPH_BYTES` | Nadpisanie limitu rozmiaru graph.json 512 MiB — np. `700MB`, `2GB`, lub zwykłe bajty | opcjonalne — przydatne dla bardzo dużych korpusów |
| `GRAPHIFY_MAX_CONTEXTS` | Maksymalna liczba nie-domyślnych grafów projektów utrzymywanych przez jeden multi-project serwer MCP | opcjonalne — domyślnie: `8`; nieprawidłowe wartości używają `8`, a wartości poniżej `1` używają `1` |
| `GRAPHIFY_LLM_TEMPERATURE` | Nadpisanie temperatury LLM dla ekstrakcji semantycznej — np. `0.7`, lub `none`, żeby pominąć | opcjonalne — auto-pomijane dla modeli reasoning o1/o3/o4/gpt-5 |

---

## Prywatność

- **Pliki kodu** — przetwarzane lokalnie przez tree-sitter. Nic nie opuszcza twojej maszyny. Korpus tylko-kod nie wymaga klucza API — `graphify extract` działa całkowicie offline. Na mieszanym repozytorium, dodaj `--code-only`, żeby indeksować tylko kod i pominąć dokumenty/PDF-y/obrazy, które inaczej wymagałyby LLM.
- **Wideo / audio** — transkrybowane lokalnie za pomocą faster-whisper. Nic nie opuszcza twojej maszyny.
- **Dokumenty, PDF-y, obrazy** — wysyłane do twojego asystenta AI do ekstrakcji semantycznej (przez skill `/graphify`, używając dowolnego modelu, na którym działa twoja sesja IDE). Headless `graphify extract` wymaga `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), działającej instancji Ollama (`OLLAMA_BASE_URL`), poświadczeń AWS przez standardowy łańcuch dostawcy (Bedrock - bez klucza API, używa IAM), lub binarki CLI `claude` (Claude Code - bez klucza API, używa twojej subskrypcji Claude). Flaga `--dedup-llm` używa tego samego klucza.
- **Rezydencja danych** — `graphify extract` automatycznie wykrywa, którego dostawcę użyć na podstawie tego, który klucz API jest ustawiony (priorytet: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). Dla kodu z wymaganiami rezydencji danych, użyj `--backend ollama` (w pełni lokalny) lub przekaż jawną flagę `--backend`. Kimi (`MOONSHOT_API_KEY`) kieruje do serwerów Moonshot AI w Chinach.
- **Brak telemetrii**, brak śledzenia użycia, brak analityki.
- **Logowanie zapytań** — każde wywołanie `graphify query`, `graphify path`, `graphify explain` i MCP `query_graph` jest logowane do `~/.cache/graphify-queries.log` w formacie JSON Lines (znacznik czasu, pytanie, korpus, zwrócone węzły, czas trwania). Pełne odpowiedzi podgrafu **nie** są przechowywane domyślnie. Ustaw `GRAPHIFY_QUERY_LOG_DISABLE=1`, żeby zrezygnować, lub `GRAPHIFY_QUERY_LOG=/dev/null`, żeby wyciszyć bez wyłączania ścieżki kodu.

---

## Rozwiązywanie problemów

**`graphify: command not found` po instalacji**
CLI jest zainstalowane, ale jego katalog bin nie jest w `PATH` twojej powłoki. Wybierz naprawę odpowiednią do sposobu instalacji:
- **uv** (`uv tool install graphifyy`): komenda ląduje w katalogu bin narzędzi uv (`~/.local/bin`), którego świeża instalacja macOS/zsh często nie ma w `PATH`. Uruchom `uv tool update-shell`, potem otwórz nowy terminal. (Znajdź katalog za pomocą `uv tool dir --bin`.)
- **pipx** (`pipx install graphifyy`): uruchom `pipx ensurepath`, potem otwórz nowy terminal.
- **pip** (`pip install graphifyy`): pip instaluje skrypty do katalogu bin użytkownika, który może nie być w `PATH` — dodaj `~/Library/Python/3.x/bin` (macOS) lub `~/.local/bin` (Linux) do `PATH` w `~/.zshrc`/`~/.bashrc`, lub po prostu uruchom `python -m graphify`.

**`uvx graphify …` lub `uv tool run graphify …` nie rozwiązuje `graphify`**
Pakiet PyPI to `graphifyy`; `graphify` to tylko komenda, którą zapewnia. `uv tool run` traktuje pierwsze słowo jako *nazwę pakietu*, więc szuka pakietu o nazwie `graphify` i raportuje `No solution found … no versions of graphify`. Nazwij pakiet jawnie: `uvx --from graphifyy graphify install` (to samo co `uv tool run --from graphifyy graphify install`). Albo `uv tool install graphifyy` raz, a potem wywołaj `graphify` bezpośrednio.

**`uv run --with graphifyy python -m graphify` po cichu uruchamia starszą instalację**
`uv run` używa twojego *systemowego* Pythona, więc jeśli starsza `graphifyy` też tam żyje (np. wcześniejsze `pip install graphifyy`), Python może znaleźć tę kopię jako pierwszą na `sys.path`, a `--with graphifyy` jej nie nadpisze. Działa bez błędu, ale dostajesz zachowanie *starej* wersji — np. nadpisania środowiska jak `OPENAI_BASE_URL` są po cichu ignorowane, więc żądania trafiają w domyślny endpoint i zawodzą z 401, który wygląda jak zły klucz. Odciskiem palca jest linia `warning: skill is from graphify <newer>, package is <older>` — to znaczy, że załadowała się inna instalacja, nie tylko przestarzały skill. Sprawdź, która kopia faktycznie się załadowała:
```bash
python -c "import graphify; print(graphify.__file__)"
```
Potem uruchom zainstalowaną komendę bezpośrednio (używa kopii zarządzanej przez uv), albo usuń przestarzałą kopię systemową:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` działa, ale komenda `graphify` nie**
`PATH` twojej powłoki nie zawiera katalogu bin, do którego zainstalowano komendę. Preferuj `uv tool install` / `pipx install` zamiast zwykłego `pip`, potem uruchom `uv tool update-shell` / `pipx ensurepath` i otwórz nowy terminal (zobacz notatki instalacyjne powyżej).

**`/graphify .` powoduje "path not recognized" w PowerShell**
PowerShell traktuje początkowy `/` jako separator ścieżki. Użyj `graphify .` (bez ukośnika) na Windows.

**Graf ma mniej węzłów po `--update` lub przebudowie**
Jeśli refaktoryzacja usunęła pliki, stare węzły pozostają. Przekaż `--force` (lub ustaw `GRAPHIFY_FORCE=1`), żeby nadpisać, nawet gdy przebudowa ma mniej węzłów.

**`extract` kończy się z "extraction was incomplete ... refusing to overwrite"**
Kiedy przebieg ekstrakcji ulega awarii lub przejście nie może w pełni odczytać korpusu, uruchomienie byłoby mniejsze niż kompletne, więc `graphify extract` odmawia nadpisania większego istniejącego grafu częściowym wynikiem (chroniąc twój `graph.json`). Napraw leżącą u podstaw awarię i uruchom ponownie, lub przekaż `--allow-partial`, żeby nadpisać mimo to.

**Graf ma duplikaty węzłów dla tej samej encji (duchy-duplikaty)**
Duchy-duplikaty (ten sam symbol pojawiający się dwa razy — raz z ekstrakcji AST z lokalizacją źródłową, raz z ekstrakcji semantycznej bez) są teraz automatycznie scalane podczas budowania. Jeśli widzisz to w grafie zbudowanym przed v0.8.33, uruchom pełną reekstrakcję, żeby posprzątać:
```bash
graphify extract . --force
```

**Ollama wyczerpuje VRAM / przekroczone okno kontekstu**
Okno KV-cache ma automatyczny rozmiar, ale może być za duże dla twojego GPU. Zmniejsz je:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**Ostrzeżenia `LLM returned invalid JSON` / `Unterminated string`**
Odpowiedź JSON modelu osiągnęła limit tokenów wyjściowych i została ucięta w połowie stringa. graphify automatycznie się regeneruje (dzieli fragment i reekstrahuje połówki, a zbyt duży pojedynczy dokument jest najpierw krojony na granicach nagłówków/akapitów, żeby cały plik był nadal pokryty), więc te ostrzeżenia są hałaśliwe, ale nie oznaczają utraty danych. Żeby zmniejszyć hałas, podnieś limit wyjścia lub zmniejsz wyjście każdego fragmentu:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
Z bramą chmurową jak OpenRouter, preferuj `--backend openai` (ustaw `OPENAI_BASE_URL`) zamiast shimu Ollama — to czystsza ścieżka kompatybilna z OpenAI. Jeśli model ma własny sufit max-output, obniżenie `--token-budget` jest niezawodną dźwignią.

**Graph HTML jest zbyt duży, żeby otworzyć w przeglądarce (>5000 węzłów)**
Pomiń generowanie HTML i użyj JSON bezpośrednio:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**`graph.json` ma markery konfliktu po jednoczesnym commicie dwóch deweloperów**
Uruchom `graphify hook install` — ustawia git merge driver, który automatycznie scala `graph.json`, więc konflikty nigdy nie występują.

**Ekstrakcja zwraca puste węzły/krawędzie dla dokumentów lub PDF-ów**
Dokumenty, PDF-y i obrazy wymagają wywołania LLM — korpusy tylko-kod nie potrzebują klucza. Sprawdź, czy twój klucz API jest ustawiony, a backend poprawny:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**Ostrzeżenie o niezgodności wersji skilla w twoim IDE**
Twoja zainstalowana wersja graphify różni się od pliku skilla. Zaktualizuj:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**Cache promptów Claude Code unieważniana po każdym `graphify extract`**
Graphify zapisuje pliki wyjściowe (`graph.json`, `graphify-out/`) do przestrzeni roboczej. Jeśli te ścieżki nie są ignorowane, każdy zapis unieważnia cache promptów Claude Code, wymuszając pełny ponowny upload w tempie zapisu cache przy następnej turze. Dodaj je do `.claudeignore`:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## Pełne odniesienie komend

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

> **Nazwy społeczności:** wewnątrz agenta (Claude Code, Gemini CLI) agent sam nazywa społeczności. Kiedy uruchamiasz goły CLI, `cluster-only` automatycznie je nazywa skonfigurowanym backendem (wbudowanym lub własnym dostawcą kompatybilnym z OpenAI) — przekaż `--no-label`, żeby zachować `Community N`, lub uruchom `graphify label`, żeby (re)generować nazwy na żądanie.

---

## Dowiedz się więcej

- [Jak to działa](docs/how-it-works.md) — pipeline ekstrakcji, wykrywanie społeczności, punktacja pewności, benchmarki
- [ARCHITECTURE.md](ARCHITECTURE.md) — podział na moduły, jak dodać język
- [Opcjonalne integracje](docs/docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — książka o ideach stojących za graphify, architekturze od początku do końca

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) to zawsze aktywna warstwa zbudowana na graphify — stosuje to samo podejście grafowe do całego twojego kontekstu roboczego: spotkań, plików, dokumentów i kodu, aktualizując się w tle w sposób ciągły.

Zbudowane dla ludzi i zespołów, których praca żyje w setkach konwersacji i dokumentów, których nigdy nie da się w pełni zrekonstruować.

**[Dołącz do listy oczekujących na graphify.com](https://graphify.com).** Bezpłatny okres próbny wkrótce.

---

<details>
<summary>Współtworzenie</summary>

### Konfiguracja środowiska deweloperskiego

Projekt używa [uv](https://docs.astral.sh/uv/) do przepływu pracy deweloperskiej. Zainstaluj go raz, potem:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

Zweryfikuj instalację editable:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### Uruchamianie testów

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> Uwaga macOS: pakiet testów zawiera zarówno fixture `sample.f90`, jak i `sample.F90`. Kolidują one na systemach plików nierozróżniających wielkości liter, jak HFS+ / APFS. Uruchom na Linuxie lub w kontenerze Docker, jeśli musisz testować obie odmiany Fortranu jednocześnie.

### Przepływ pracy Git

- Aktywny rozwój odbywa się na gałęzi `v8`.
- Styl commitów: `fix: <description>` / `feat: <description>` / `docs: <description>`
- Przed otwarciem PR, uruchom `uv run pytest tests/ -q` i potwierdź, że przechodzi.
- Dodaj plik fixture do `tests/fixtures/` i testy do `tests/test_languages.py` dla każdego nowego ekstraktora języka.

### Co współtworzyć

**Przepracowane przykłady (worked examples)** są najbardziej użytecznym wkładem. Uruchom `/graphify` na prawdziwym korpusie, zapisz wynik do `worked/{slug}/`, napisz szczery `review.md` obejmujący, co graf zrobił dobrze, a co źle, i otwórz PR.

**Błędy ekstrakcji** — otwórz issue z plikiem wejściowym, wpisem cache (`graphify-out/cache/`), i tym, co zostało pominięte lub było błędne.

Zobacz [ARCHITECTURE.md](ARCHITECTURE.md) dla odpowiedzialności modułów i jak dodać język.

</details>
