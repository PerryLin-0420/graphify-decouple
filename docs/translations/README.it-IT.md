<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>Un fork di <a href="https://github.com/Graphify-Labs/graphify">graphify</a> che aggiunge <code>graphify decouple</code></b> — candidati Extract-Class con punteggio di rischio a 0 LLM per i god object, riverificati contro il codice sorgente reale (non solo il call graph) prima di raccomandare qualsiasi cosa. Vedi <a href="#decouple-candidati-extract-class-con-punteggio-di-rischio">Decouple: candidati Extract-Class con punteggio di rischio</a> più sotto.
</p>

<div align="center">
<details><summary><b>Leggi questo in altre lingue</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>L'accesso anticipato alla piattaforma graphify è aperto prima del lancio pubblico della v1: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

Digita `/graphify` nel tuo assistente di codice IA e mapperà l'intero progetto (codice, documenti, PDF, immagini, video) in un **grafo della conoscenza** che puoi **interrogare invece di fare grep** nei file.

- **Mappe del codice gratuite, completamente locali.** Il codice viene analizzato con l'AST di tree-sitter: deterministico, senza LLM, niente lascia la tua macchina. (Documenti, PDF, immagini e video usano il modello del tuo assistente, o una chiave API configurata, per un passaggio semantico.)
- **Ogni collegamento è spiegato.** Ogni connessione è etichettata `EXTRACTED` (esplicita nel codice sorgente) o `INFERRED` (risolta da graphify), così sai distinguere cosa è stato letto direttamente da cosa è stato dedotto.
- **Non è un indice vettoriale.** Nessun embedding, nessun vector store: un grafo reale che puoi attraversare. Fai una domanda, traccia il percorso tra due elementi, oppure spiega un concetto.

> Vuoi che questo sia sempre attivo, aggiornandosi in background su codice, documenti e riunioni invece che solo su richiesta? È quello che stiamo costruendo su **[graphify.com](https://graphify.com)**, e l'accesso anticipato è aperto ora su **[app.graphify.com](https://app.graphify.com/login)**.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="il graph.html interattivo di graphify che mostra la codebase di FastAPI come un grafo della conoscenza force-directed con una legenda delle community rilevate" width="900">
</p>
<p align="center">
  <em>La codebase di FastAPI mappata da graphify. Ogni nodo è un concetto, i colori sono le community rilevate, e il tutto è cliccabile in graph.html.</em>
</p>

**Per iniziare** (30 secondi):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

Poi, nel tuo assistente IA:

```
/graphify .
```

Tutto qui. Ottieni **tre file**:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**Funziona con** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, e altri 15+ — [scegli la tua piattaforma](#installazione).

---

## Guardalo in azione

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="query di percorso di graphify: un terminale chiede il percorso più breve tra FastAPI e ModelField, e la risposta si illumina un salto alla volta lungo il grafo della conoscenza" width="900">
</p>

Una volta costruito il grafo, lo interroghi invece di leggere i file. Output reale, graphify eseguito sulla codebase di FastAPI mostrata sopra:

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

Ogni collegamento porta un **tag di confidenza** (`EXTRACTED` = esplicito nel codice sorgente, `INFERRED` = derivato dalla risoluzione), così sai distinguere cosa è stato letto direttamente da cosa è stato dedotto. `graphify query "<question>"` restituisce un sottografo mirato per una domanda in linguaggio naturale, e `graphify path A B` traccia come due elementi qualsiasi sono connessi.

---

## Decouple: candidati Extract-Class con punteggio di rischio

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: il god node MainWindow che si divide in classi candidate con punteggio di rischio, con un avviso di stato condiviso tra due di esse" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: le 5 classi proposte per MainWindow, pannello Node Info aperto su Main Window Axis and Range Controls che mostra una sovrapposizione di stato di 0.608 con Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>DECOUPLE.html su un'esecuzione reale — cliccando su una classe proposta mostra esattamente con quale altra classe condivide stato, e cosa esattamente viene condiviso.</em>
</p>

La stessa pagina renderizza anche la divisione vera e propria. Attivare **Preview decoupled view** sostituisce i metodi propri della god class con le classi proposte e re-instrada gli archi sul posto — il cambio di cablaggio, non un diagramma ridisegnato:

| Prima — la god class oggi | Dopo — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html prima del toggle: un singolo nodo hub MainWindow con i suoi metodi disposti tutt'intorno" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html dopo il toggle: lo stesso nodo ridotto a 5 classi proposte a forma di rombo, archi verdi tratteggiati che mostrano quali metodi sono stati estratti in ciascuna, archi rossi che mostrano lo stato di istanza condiviso tra due di esse" width="440"> |
| Un nodo che contiene 47 dei suoi metodi, ognuno raggiungibile solo attraverso la classe. | Le classi proposte. Verde tratteggiato = cosa è stato estratto in ciascuna; rosso = lo stato di istanza che due di esse continuano a condividere, che è esattamente ciò che decide tra `split` e `keep_as_is`. Vengono disegnati solo i candidati che superano la soglia di rischio — qui 5 su 6, ed è per questo che un metodo resta senza rombo su cui atterrare. |

`graphify decouple` trova i god object e ti dice se dividerli vale davvero la pena — non solo che sono grandi.

Il modo di fallimento che questo strumento vuole intercettare: una classe con 47 metodi che il clustering basato sul call graph divide felicemente in 5 gruppi dall'aspetto ordinato, tutti i quali continuano a leggere e scrivere esattamente lo stesso stato di istanza `self._chart_style` / `self._crosshair` sotto il cofano. Se rilasci quella divisione non hai disaccoppiato nulla — hai solo spostato metodi in nuovi file che ancora non possono essere testati, modificati o ragionati in modo indipendente, perché tutti hanno ancora bisogno dello stesso stato condiviso passato indietro. Uno strumento che guarda solo il call graph non può vederlo affatto; deve tornare al codice sorgente reale.

**Due controlli, entrambi a 0 LLM, entrambi deterministici:**

1. **È davvero un God Object?** Un nodo con un grado alto può essere un vero God Object (molti dei SUOI PROPRI metodi, distribuiti su responsabilità non correlate — Extract Class si applica) oppure un hub/modello dati sovra-referenziato (pochi metodi propri, per lo più riferimenti *in entrata* — dividerne il corpo non serve a nulla; la correzione è restringere la sua interfaccia, non estrarre una classe). `classify_god_node` distingue i due casi in base a `member_ratio`, non al grado grezzo — la differenza che impedisce a `TraceSource` (84 archi, ma solo 6 dei suoi metodi propri) di ricevere un suggerimento di divisione fasullo che `MainWindow` (88 archi, 47 dei suoi metodi propri) riceve invece correttamente.
2. **La divisione ridurrebbe davvero l'accoppiamento?** `risk_before` (la dimensione/accoppiamento/frammentazione attuale del god node) viene confrontato con `risk_after` — il NUOVO rischio che la divisione stessa introdurrebbe: chiamate cross-gruppo che erano archi intra-classe invisibili e diventano dipendenze inter-classe esplicite, chiamanti che dovrebbero ora dipendere da più di una nuova classe e — il controllo che un call graph strutturalmente non può fare — quanto stato di istanza `self`/`this` (letture, scritture e chiamate a metodi helper condivisi, pesate separatamente: una **scrittura** condivisa vale più di una lettura condivisa) i gruppi proposti hanno effettivamente in comune. Questo ri-analizza direttamente il file sorgente del god node con tree-sitter; non si basa sul grafo già estratto da graphify, che non registra mai l'accesso ai campi a livello di dettaglio per nessun linguaggio. Solo quando `risk_after` scende sotto una soglia rispetto a `risk_before` il piano raccomanda `split` — altrimenti è `marginal` o `keep_as_is`, e un candidato scoraggiato viene riportato come un numero, mai disegnato come una forma che devi rimettere in dubbio a occhio.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

Genera tre file accanto a `graph.json`:

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

**Copertura linguistica per il controllo di condivisione dello stato** (la classificazione basata solo sul call graph descritta sopra funziona per ogni linguaggio che graphify estrae; questa tabella riguarda specificamente la ri-analisi del sorgente che verifica la sovrapposizione di stato `self`/`this`):

| Linguaggio | Supportato | Note |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` è un nodo AST a sé stante, non un accesso a campo avvolto — gestito esplicitamente |
| C# | ✅ | |
| Rust | ✅ | `self.x` tramite i blocchi `impl` |
| Ruby | ✅ | `@x` (l'idioma dominante) + chiamate `self.foo` |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | risoluzione del receiver per singolo metodo — Go non ha una keyword `self`/`this`, quindi il nome del receiver (`f` in `func (f *Foo) M()`) viene risolto di nuovo per ogni metodo |
| C | ❌ | un parametro puntatore-a-struct non ha alcun marcatore sintattico che lo distingua da qualsiasi altro parametro — nessun segnale affidabile senza una piena inferenza dei tipi |

Un god node in un linguaggio non supportato, o il cui sorgente non può essere letto, viene marcato `state_analysis: "skipped"` — la classificazione e il punteggio del call graph vengono comunque eseguiti, ma la raccomandazione si basa solo sul call graph invece di assumere silenziosamente che il controllo di stato sia passato.

---

## Cosa fa

Cosa ottieni pronto all'uso:

| Capacità | Cosa ottieni |
|---|---|
| **God nodes** | I concetti più connessi, così vedi da dove passa tutto |
| **Communities** | Il grafo suddiviso in sottosistemi (Leiden), con etichette senza LLM |
| **Cross-file links** | `calls` / `imports` / `inherits` / `mixes_in` risolti tra ~40 linguaggi tramite AST di tree-sitter |
| **Query, path, explain** | Fai una domanda, traccia il percorso tra due elementi, o spiega un concetto, tutto contro `graph.json` |
| **Rationale + doc refs** | I commenti `# NOTE:` / `# WHY:` e le citazioni ADR/RFC diventano nodi di prima classe collegati al codice |
| **Beyond code** | Documenti, PDF, immagini e video/audio mappano tutti nello stesso grafo |
| **Local-first** | Il codice viene analizzato localmente con tree-sitter (nessun LLM, niente lascia la tua macchina); solo il passaggio semantico su documenti/media chiama un backend, e solo se ne configuri uno |

---

## Benchmark

| Benchmark | Metrica | graphify | Settore |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | accuratezza QA | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | accuratezza QA | **76%** | a pari merito con dense RAG |
| Graph build | crediti LLM | **0** | a consumo per token per la maggior parte dei sistemi |

Ogni sistema è stato eseguito sullo stesso harness, con lo stesso modello e gli stessi budget, valutato da un giudice validato alla cieca contro un secondo giudice (90,6% di accordo, kappa di Cohen 0,81). Tabelle complete per singolo sistema, il risultato sulla code-intelligence e i comandi di riproduzione: **[BENCHMARKS.md](../../BENCHMARKS.md)**.

---

## Prerequisiti

| Requisito | Minimo | Verifica | Installazione |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(consigliato)* | qualsiasi | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(alternativa)* | qualsiasi | `pipx --version` | `pip install pipx` |

**Installazione rapida su macOS (Homebrew):**
```bash
brew install python@3.12 uv
```

**Installazione rapida su Windows:**
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

## Installazione

> **Pacchetto ufficiale:** il pacchetto PyPI è `graphifyy` (doppia y). Altri pacchetti `graphify*` su PyPI non sono affiliati. Il comando CLI resta `graphify`.

**Passo 1 — installa il pacchetto:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**Passo 2 — registra la skill con il tuo assistente IA:**

```bash
graphify install
```

Tutto qui. Apri il tuo assistente IA e digita `/graphify .`

Per installare la skill dell'assistente nel repository corrente invece che nel tuo profilo
utente, aggiungi `--project`:

```bash
graphify install --project
graphify install --project --platform codex
```

Le installazioni con ambito di progetto scrivono sotto la directory corrente, per esempio
`.claude/skills/graphify/SKILL.md` o `.agents/skills/graphify/SKILL.md` (più un
sidecar `references/` che la skill carica su richiesta), e
stampano un suggerimento `git add` per i file che possono essere committati.
I comandi per singola piattaforma che supportano installazioni con ambito di progetto accettano
lo stesso flag, ad esempio `graphify claude install --project` o `graphify codex install --project`.

> **Nota PowerShell:** usa `graphify .` e non `/graphify .` — lo slash iniziale è un separatore di percorso in PowerShell.

> **`graphify: command not found`?** `uv tool install` / `pipx install` mettono il comando `graphify` nella loro tool bin dir (`~/.local/bin`). Se la tua shell non lo trova subito dopo l'installazione — comune su un setup macOS + zsh appena fatto — quella directory non è ancora nel tuo `PATH`: esegui `uv tool update-shell` (o `pipx ensurepath`), poi apri un nuovo terminale. Con il semplice `pip`, aggiungi `~/.local/bin` (Linux) o `~/Library/Python/3.x/bin` (Mac) al tuo PATH, oppure esegui `python -m graphify`.

> **Esegui con `uvx` / `uv tool run` invece di installare?** Nomina il pacchetto, non il comando: `uvx --from graphifyy graphify install`. Il semplice `uvx graphify …` fallisce (`No solution found … no versions of graphify`) perché `uv tool run` legge la prima parola come *pacchetto*, e il pacchetto è `graphifyy` — il comando `graphify` vive al suo interno.

> **Evita `pip install` su Mac/Windows** se possibile. La skill risolve Python a runtime da `graphify-out/.graphify_python`; se questo punta a un ambiente diverso da quello in cui `pip` ha installato il pacchetto, otterrai `ModuleNotFoundError: No module named 'graphify'`. `uv tool install` e `pipx install` isolano il pacchetto nel proprio ambiente ed evitano completamente questo problema.

> **Git hook e uv tool / pipx:** `graphify hook install` incorpora direttamente il percorso dell'interprete corrente negli script hook al momento dell'installazione, così l'hook post-commit scatta correttamente anche nei client git GUI e nei runner CI dove `~/.local/bin` non è nel PATH. Se reinstalli o aggiorni graphify, riesegui `graphify hook install` per aggiornare il percorso incorporato.

> **Modalità strict (Claude Code):** `graphify install --project --strict` fa sì che l'assistente usi davvero il grafo. L'installazione predefinita lo *spinge* a eseguire `graphify query` prima di leggere i file; la modalità strict *blocca* la prima lettura grezza del sorgente in una sessione e la reindirizza verso il grafo, poi torna alla semplice spinta (così scatta al massimo una volta per sessione e non resta mai bloccata). Attivabile a runtime con `GRAPHIFY_HOOK_STRICT=1`/`0`; l'installazione predefinita resta invariata (spinta leggera).

<details>
<summary><b>Scegli la tua piattaforma</b> (20+ assistenti, clicca per espandere)</summary>

| Piattaforma | Comando di installazione |
|----------|----------------|
| Claude Code (Linux/Mac) | `graphify install` |
| Claude Code (Windows) | `graphify install` (rilevato automaticamente) o `graphify install --platform windows` |
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

Gli utenti Codex hanno anche bisogno di `multi_agent = true` sotto `[features]` in `~/.codex/config.toml` per l'estrazione parallela. CodeBuddy usa lo stesso meccanismo di Agent tool e hook PreToolUse di Claude Code. Factory Droid usa lo strumento `Task` per il dispatch parallelo dei subagent. OpenClaw e Aider usano l'estrazione sequenziale (il supporto per agenti paralleli è ancora agli inizi su quelle piattaforme). Trae usa l'Agent tool per il dispatch parallelo dei subagent e **non** supporta gli hook `PreToolUse`, quindi AGENTS.md è il meccanismo always-on.

`--platform agents` (alias `--platform skills`) mira alle posizioni generiche cross-framework di [Agent-Skills](https://github.com/anthropics/skills): la `~/.agents/skills/` user-global della spec (letta da `npx skills` e dai framework conformi alla spec) per un'installazione globale, e `./.agents/skills/` per un'installazione di progetto (`--project`). Il semplice `graphify install` resta single-platform (Claude Code) di proposito — usa la piattaforma denominata `agents` quando vuoi che la skill sia individuabile da qualsiasi framework che legge `.agents/skills`.

> Codex usa `$graphify` invece di `/graphify`.

</details>

<details>
<summary><b>Estensioni opzionali</b> (installa solo ciò che ti serve)</summary>

| Estensione | Cosa aggiunge | Installazione |
|---|---|---|
| `pdf` | Estrazione PDF | `uv tool install "graphifyy[pdf]"` |
| `office` | Supporto per `.docx` e `.xlsx` | `uv tool install "graphifyy[office]"` |
| `google` | Rendering di Google Sheets | `uv tool install "graphifyy[google]"` |
| `video` | Trascrizione video/audio (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | Server MCP stdio | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Supporto push verso Neo4j | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | Supporto push verso FalkorDB | `uv tool install "graphifyy[falkordb]"` |
| `svg` | Esportazione del grafo in SVG | `uv tool install "graphifyy[svg]"` |
| `leiden` | Rilevamento community Leiden (solo Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Inferenza locale Ollama | `uv tool install "graphifyy[ollama]"` |
| `openai` | API OpenAI / compatibili con OpenAI | `uv tool install "graphifyy[openai]"` |
| `gemini` | API Google Gemini | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | API Anthropic Claude (`--backend claude`, usa `ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (usa IAM, nessuna chiave API) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, usa `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "graphifyy[openai]"` |
| `sql` | Estrazione di schemi SQL | `uv tool install "graphifyy[sql]"` |
| `postgres` | Introspezione PostgreSQL live (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | Estrazione AST BYOND DreamMaker `.dm`/`.dme` (potrebbe richiedere un compilatore C + `python3-dev` se non è disponibile una wheel per la tua piattaforma) | `uv tool install "graphifyy[dm]"` |
| `terraform` | Estrazione AST Terraform / HCL `.tf`/`.tfvars`/`.hcl` | `uv tool install "graphifyy[terraform]"` |
| `pascal` | Estrazione AST Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` (archi `calls`/`inherits` più accurati; ricade su un estrattore basato su regex se assente) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | Segmentazione delle query in cinese (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | Tutto quanto sopra | `uv tool install "graphifyy[all]"` |

</details>

---

## Fai in modo che il tuo assistente usi sempre il grafo

Esegui questo comando una volta nel tuo progetto dopo aver costruito un grafo:

| Piattaforma | Comando |
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

Questo scrive un piccolo file di configurazione che dice al tuo assistente di consultare il grafo della conoscenza per le domande sulla codebase, preferendo query mirate come `graphify query "<question>"` invece di leggere il report completo o fare grep sui file grezzi.

- **Piattaforme con hook** (Claude Code, Gemini CLI): un hook scatta automaticamente prima delle chiamate a strumenti di tipo ricerca (e, su Claude Code, prima di leggere i file sorgente uno per uno tramite gli strumenti Read/Glob) e spinge il tuo assistente verso il percorso del grafo.
- **Piattaforme a file di istruzioni** (Codex, OpenCode, Cursor, ecc.): file di istruzioni persistenti (`AGENTS.md`, `.cursor/rules/`, ecc.) forniscono la stessa indicazione a favore delle query.

`GRAPH_REPORT.md` resta comunque disponibile per una revisione architetturale ad ampio raggio.

**CodeBuddy** fa le stesse due cose di Claude Code: scrive una sezione `CODEBUDDY.md` che dice a CodeBuddy di leggere `graphify-out/GRAPH_REPORT.md` prima di rispondere a domande architetturali, e installa hook `PreToolUse` (`.codebuddy/settings.json`) che scattano prima dei comandi di ricerca Bash e delle letture di file, spingendo invece verso `graphify query`.

**Codex** scrive su `AGENTS.md`, che è ciò che effettivamente porta l'indicazione always-on verso il grafo su questa piattaforma. `graphify codex install` registra anche un hook `PreToolUse` in `.codex/hooks.json` (`graphify hook-check`), ma quella voce è deliberatamente un **no-op**: Codex Desktop rifiuta `hookSpecificOutput.additionalContext` su `PreToolUse`, quindi emettere un suggerimento lì romperebbe le chiamate allo strumento Bash. A differenza di Claude Code, dove l'hook (`graphify hook-guard`) fa da spinta, su Codex l'hook scatta e intenzionalmente non fa nulla, e `AGENTS.md` è il meccanismo always-on.

**Kilo Code** installa la skill Graphify in `~/.config/kilo/skills/graphify/SKILL.md` e un comando nativo `/graphify` in `~/.config/kilo/command/graphify.md`. `graphify kilo install` scrive anche `AGENTS.md` più un plugin nativo `tool.execute.before` (`.kilo/plugins/graphify.js` + registrazione in `.kilo/kilo.json` o `.kilo/kilo.jsonc`) così Kilo ottiene lo stesso comportamento di promemoria always-on verso il grafo tramite la configurazione nativa `.kilo`.

**Cursor** scrive `.cursor/rules/graphify.mdc` con `alwaysApply: true`, così Cursor lo include automaticamente in ogni conversazione, senza bisogno di hook.

Per rimuovere graphify da tutte le piattaforme in una volta: `graphify uninstall` (aggiungi `--purge` per eliminare anche `graphify-out/`). Oppure usa il comando specifico per piattaforma (ad es. `graphify claude uninstall`).

---

## Cosa contiene il report

- **God nodes** — i concetti più connessi nel tuo progetto. Tutto passa attraverso questi.
- **Surprising connections** — collegamenti tra elementi che vivono in file o moduli diversi. Classificati in base a quanto sono inaspettati.
- **Il "perché"** — i commenti inline (`# NOTE:`, `# WHY:`, `# HACK:`), le docstring e le motivazioni di design provenienti dai documenti vengono estratti come nodi separati collegati al codice che spiegano.
- **Suggested questions** — 4-5 domande a cui il grafo è particolarmente adatto a rispondere.
- **Confidence tags** — ogni relazione dedotta è marcata `EXTRACTED`, `INFERRED` o `AMBIGUOUS`. Sai sempre cosa è stato trovato rispetto a cosa è stato ipotizzato.

---

## Quali file gestisce

| Tipo | Estensioni |
|------|-----------|
| Codice (36 grammatiche tree-sitter) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme` richiede `uv tool install graphifyy[dm]`; `.mts`/`.cts` riusano la grammatica TypeScript, `.cc`/`.cxx` e CUDA `.cu`/`.cuh` e Metal `.metal` riusano la grammatica C++) |
| Salesforce Apex | `.cls .trigger` (basato su regex; classi, interfacce, enum, metodi, trigger, archi SOQL/DML) |
| Terraform / HCL | `.tf .tfvars .hcl` (richiede `uv tool install graphifyy[terraform]`) |
| Configurazioni MCP | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — estrae nodi server, riferimenti a pacchetti, requisiti di variabili d'ambiente |
| Manifest dei pacchetti | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — un nodo pacchetto canonico per pacchetto (per nome) più archi `depends_on`, così un pacchetto referenziato da molti manifest è un unico hub |
| Documenti | `.md .mdx .qmd .html .txt .rst .yaml .yml` (i link markdown `[text](./other.md)` e i `[[wikilinks]]` diventano archi `references` tra documenti) |
| Office | `.docx .xlsx` (richiede `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (opzionale; richiede l'autenticazione `gws` e `--google-workspace`; i Fogli richiedono `uv tool install graphifyy[google]`) |
| PDF | `.pdf` |
| Immagini | `.png .jpg .webp .gif` |
| Video / Audio | `.mp4 .mov .mp3 .wav` e altri (richiede `uv tool install graphifyy[video]`) |
| YouTube / URL | qualsiasi URL video (richiede `uv tool install graphifyy[video]`) |

Il codice viene estratto **localmente senza chiamate API** (AST tramite tree-sitter). Tutto il resto passa attraverso l'API del modello del tuo assistente IA.

I file `.gdoc`, `.gsheet` e `.gslides` di Google Drive per desktop sono puntatori di scorciatoia, non il contenuto del documento. Per includere Google Docs, Sheets e Slides nativi in un'estrazione headless, installa e autentica la [`gws` CLI](https://github.com/googleworkspace/cli), poi esegui:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

Puoi anche impostare `GRAPHIFY_GOOGLE_WORKSPACE=1`. Graphify esporta le scorciatoie in
`graphify-out/converted/` come file collaterali Markdown, poi estrae quei file.

---

## Comandi comuni

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

Vedi [Decouple: candidati Extract-Class con punteggio di rischio](#decouple-candidati-extract-class-con-punteggio-di-rischio) più sopra, oppure il [riferimento completo dei comandi](#riferimento-completo-dei-comandi) più sotto.

---

## Ignorare i file

Crea un file `.graphifyignore` nella radice del progetto — stessa sintassi di `.gitignore`, inclusa la negazione con `!`.

**`.gitignore` viene rispettato automaticamente.** graphify legge il `.gitignore` presente in ogni directory. Se è presente anche un `.graphifyignore`, i due vengono **uniti** — i pattern di `.graphifyignore` sono valutati per ultimi, quindi vincono in caso di conflitto (incluse le negazioni con `!`). Aggiungere un `.graphifyignore` può solo escludere di più; non reintroduce mai un file che il tuo `.gitignore` aveva già escluso. L'ambito per sottodirectory funziona come in git — un file di ignore riguarda solo il proprio sottoalbero.

Passa `--no-gitignore` a `graphify extract` quando codice generato o transpilato ignorato da git deve comunque far parte del grafo. Questo disabilita `.gitignore` e `.git/info/exclude`; `.graphifyignore` continua ad applicarsi.

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

## Configurazione per il team

`graphify-out/` è pensato per essere committato in git, così tutti nel team partono con una mappa.

**Aggiunte consigliate a `.gitignore`:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` è ora portabile — le chiavi sono memorizzate come percorsi relativi e vengono riancorate al caricamento, quindi committarlo è sicuro ed evita una ricostruzione completa al primo checkout.

**Flusso di lavoro:**
1. Una persona esegue `/graphify .` e committa `graphify-out/`.
2. Tutti gli altri fanno pull — il loro assistente legge subito il grafo.
3. Esegui `graphify hook install` per ricostruire automaticamente dopo ogni commit (solo AST, nessun costo API). Questo imposta anche un merge driver git così `graph.json` non viene mai lasciato con marcatori di conflitto — due sviluppatori che committano in parallelo ottengono i loro grafi uniti automaticamente (union-merge).
4. Quando documenti o paper cambiano, esegui `/graphify --update` per aggiornare quei nodi.

---

## Usare il grafo direttamente

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

Il server MCP dà al tuo assistente un accesso strutturato: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Server HTTP condiviso

`--transport stdio` (predefinito) avvia un server locale per ogni sviluppatore. `--transport http` espone gli stessi strumenti tramite il trasporto MCP Streamable HTTP, così un singolo processo condiviso può servire il grafo per l'intero team — i client puntano la configurazione MCP del proprio IDE su `http://<host>:8080/mcp` invece di eseguire graphify localmente.

| Flag | Predefinito | Scopo |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Trasporto su cui servire |
| `--host` | `127.0.0.1` | Host di bind HTTP (usa `0.0.0.0` per esporre oltre localhost) |
| `--port` | `8080` | Porta di bind HTTP |
| `--api-key` | env `GRAPHIFY_API_KEY` | Richiede `Authorization: Bearer <key>` (o `X-API-Key`) |
| `--path` | `/mcp` | Percorso di mount HTTP |
| `--json-response` | off | Restituisce JSON semplice invece di stream SSE |
| `--stateless` | off | Nessuno stato per sessione (per deployment con load balancing / CI) |
| `--session-timeout` | `3600` | Termina le sessioni stateful inattive dopo N secondi (`0` disabilita) |

Il bind predefinito `127.0.0.1` è solo loopback. Imposta `--host 0.0.0.0` **e** `--api-key` insieme quando lo esponi su un host condiviso. Eseguilo in un container:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **Nota WSL / Linux:** Ubuntu fornisce `python3`, non `python`. Usa un venv per evitare conflitti:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## Variabili d'ambiente

Sono necessarie solo per l'**estrazione headless / CI** (`graphify extract`). Quando esegui tramite la skill `/graphify` all'interno del tuo IDE, l'API del modello è fornita dalla sessione del tuo IDE — non servono chiavi aggiuntive.

| Variabile | Utilizzo | Quando richiesta |
|---|---|---|
| `ANTHROPIC_API_KEY` | Backend Claude (Anthropic) | `--backend claude` |
| `ANTHROPIC_BASE_URL` | URL dell'endpoint compatibile con Anthropic (proxy LiteLLM, gateway, ...) | `--backend claude` (predefinito: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Nome del modello per il backend Claude — per endpoint personalizzati, usa il nome/alias del modello esposto dal tuo server | `--backend claude` (predefinito: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` o `GOOGLE_API_KEY` | Backend Google Gemini | `--backend gemini` |
| `OPENAI_API_KEY` | API OpenAI o compatibili con OpenAI | `--backend openai` (i server locali accettano qualsiasi valore non vuoto) |
| `OPENAI_BASE_URL` | URL del server compatibile con OpenAI (llama.cpp, vLLM, LM Studio, ...) | `--backend openai` (predefinito: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | Nome del modello per il backend OpenAI — per server self-hosted, usa il nome/alias esposto dal tuo server (controlla il suo endpoint `/v1/models`), ad es. `LFM2.5-8B-A1B-UD-Q4_K_XL` per llama.cpp | `--backend openai` (predefinito: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | Backend DeepSeek | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Backend Kimi Code | `--backend kimi` |
| `OLLAMA_BASE_URL` | URL di inferenza locale Ollama | `--backend ollama` (predefinito: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Nome del modello Ollama | `--backend ollama` (predefinito: rilevamento automatico) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Sovrascrive la dimensione della finestra KV-cache di Ollama | opzionale — dimensionata automaticamente per default |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Minuti per cui mantenere caricato il modello Ollama | opzionale — imposta `0` per scaricarlo dopo ogni chunk |
| `AZURE_OPENAI_API_KEY` | Backend Azure OpenAI Service | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | URL dell'endpoint della risorsa Azure | `--backend azure` (richiesto insieme alla chiave API) |
| `AZURE_OPENAI_API_VERSION` | Sovrascrive la versione dell'API Azure | opzionale — predefinito `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` o `GRAPHIFY_AZURE_MODEL` | Nome del deployment Azure | opzionale — predefinito `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — catena di credenziali standard | `--backend bedrock` (nessuna chiave API, usa IAM) |
| `GRAPHIFY_MAX_WORKERS` | Numero di thread per il parallelismo AST | opzionale — anche flag `--max-workers` |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Alza il limite di output per corpus densi | opzionale — ad es. `32768` per file grandi |
| `GRAPHIFY_API_TIMEOUT` | Timeout per chiamata in secondi per i backend HTTP, claude-cli, Anthropic SDK e Bedrock (predefinito: 600) | opzionale — anche flag `--api-timeout` |
| `GRAPHIFY_MAX_RETRIES` | Quante volte ritentare una richiesta con rate limit (429) prima di arrendersi (predefinito: 6; rispetta `Retry-After`) | opzionale — alza per limiti per-org rigidi (ad es. kimi); `0` disabilita |
| `GRAPHIFY_FORCE` | Forza la ricostruzione del grafo anche con meno nodi | opzionale — anche flag `--force` |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Abilita automaticamente l'esportazione Google Workspace | opzionale — imposta a `1` |
| `GRAPHIFY_TRIAGE_BACKEND` | Backend per `graphify prs --triage` | opzionale — rilevato automaticamente dalle chiavi disponibili |
| `GRAPHIFY_TRIAGE_MODEL` | Sovrascrive il modello per il triage | opzionale — ad es. `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | Imposta a `1` per attivare il log locale delle query in `~/.cache/graphify-queries.log` (registra ogni domanda query/path/explain + il percorso del corpus). Disattivato per default — nulla viene scritto a meno che tu non lo attivi (#1797) | opzionale |
| `GRAPHIFY_QUERY_LOG` | Attiva il log delle query e lo scrive in questo percorso invece di quello predefinito | opzionale — disattivato a meno che questa o `_ENABLE` non sia impostata |
| `GRAPHIFY_QUERY_LOG_DISABLE` | Imposta a `1` per forzare la disattivazione del log delle query (ha priorità sulle variabili di attivazione) | opzionale |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | Quando il log è attivo, registra anche le risposte complete dei sottografi (disattivato per default) | opzionale |
| `GRAPHIFY_MAX_GRAPH_BYTES` | Sovrascrive il limite di dimensione di 512 MiB per `graph.json` — ad es. `700MB`, `2GB`, o byte semplici | opzionale — utile per corpus molto grandi |
| `GRAPHIFY_MAX_CONTEXTS` | Numero massimo di grafi di progetto non predefiniti mantenuti da un server MCP multi-progetto | opzionale — predefinito: `8`; i valori non validi usano `8`, e i valori sotto `1` usano `1` |
| `GRAPHIFY_LLM_TEMPERATURE` | Sovrascrive la temperatura dell'LLM per l'estrazione semantica — ad es. `0.7`, o `none` per ometterla | opzionale — omessa automaticamente per i modelli di reasoning o1/o3/o4/gpt-5 |

---

## Privacy

- **File di codice** — elaborati localmente tramite tree-sitter. Niente lascia la tua macchina. Un corpus solo di codice non richiede alcuna chiave API — `graphify extract` funziona completamente offline. Su un repository misto, aggiungi `--code-only` per indicizzare solo il codice e saltare documenti/PDF/immagini che altrimenti richiederebbero un LLM.
- **Video / audio** — trascritti localmente con faster-whisper. Niente lascia la tua macchina.
- **Documenti, PDF, immagini** — inviati al tuo assistente IA per l'estrazione semantica (tramite la skill `/graphify`, usando qualunque modello esegua la tua sessione IDE). `graphify extract` headless richiede `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), un'istanza Ollama in esecuzione (`OLLAMA_BASE_URL`), credenziali AWS tramite la catena di provider standard (Bedrock — nessuna chiave API necessaria, usa IAM), oppure il binario CLI `claude` (Claude Code — nessuna chiave API necessaria, usa il tuo abbonamento Claude). Il flag `--dedup-llm` usa la stessa chiave.
- **Residenza dei dati** — `graphify extract` rileva automaticamente quale provider usare in base a quale chiave API è impostata (priorità: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). Per codice con requisiti di residenza dei dati, usa `--backend ollama` (completamente locale) oppure passa esplicitamente un flag `--backend`. Kimi (`MOONSHOT_API_KEY`) instrada verso i server Moonshot AI in Cina.
- **Nessuna telemetria**, nessun tracciamento dell'utilizzo, nessuna analitica.
- **Logging delle query** — ogni chiamata a `graphify query`, `graphify path`, `graphify explain` e alla MCP `query_graph` viene registrata in `~/.cache/graphify-queries.log` in formato JSON Lines (timestamp, domanda, corpus, nodi restituiti, durata). Le risposte complete dei sottografi **non** vengono salvate per default. Imposta `GRAPHIFY_QUERY_LOG_DISABLE=1` per disattivare, oppure `GRAPHIFY_QUERY_LOG=/dev/null` per silenziare senza disabilitare il percorso di codice.

---

## Limiti e confini

Ciò che graphify deliberatamente **non** fa, e dove si ferma la sua copertura:

- **Non è un motore di ricerca semantica/vettoriale.** Il grafo è strutturale — nodi e archi tipizzati risolti a partire dal sorgente, non embedding. `graphify query`/`path`/`explain` percorrono quella struttura; non possono far emergere una connessione che non sia rappresentata come un arco, anche se è "semanticamente" correlata. Non esiste alcun fallback per similarità/nearest-neighbor.
- **Documenti, PDF, immagini ed estrazione headless di video/URL non sono solo locali.** Solo il codice (AST tree-sitter) e la trascrizione audio/video (faster-whisper) girano completamente offline. L'estrazione di documenti/PDF/immagini chiama sempre un LLM — il modello del tuo assistente IA tramite la skill `/graphify`, oppure una chiave API di backend configurata per `graphify extract` headless. Vedi [Privacy](#privacy) più sopra per sapere esattamente quale flag o chiave serve per ciascun percorso.
- **Il controllo di condivisione dello stato di decouple non copre tutti i linguaggi.** C non ha un segnale `self`/`this` affidabile senza un'inferenza di tipo completa, quindi è escluso (vedi la [tabella di copertura dei linguaggi](#decouple-candidati-extract-class-con-punteggio-di-rischio) più sopra). Un god node in un linguaggio non supportato, o il cui sorgente non può essere letto, ricade su un punteggio basato solo sul call graph (`state_analysis: "skipped"`) invece che su un controllo di stato verificato.
- **Il data-flow floor 3D è un'euristica basata sui nomi, non un'analisi di dataflow/taint.** Il rilevamento dei confini I/O di `data_floor` (parser, loader, reader, writer, client DB/HTTP) si basa su convenzioni di denominazione (`boundary_reason`); un nodo di confine con un nome non convenzionale può essere mancato, sottostimando quanto in profondità si trovi in realtà il resto del grafo.
- **I tag di confidenza sono la confidenza di risoluzione propria di graphify, non una verità assoluta.** Gli archi `INFERRED` e `AMBIGUOUS` sono risoluzioni fatte al meglio delle possibilità e possono comunque essere sbagliati, specialmente per idiomi molto dinamici (reflection, dispatch a runtime, metaprogrammazione) che nessun passaggio AST statico può risolvere completamente.
- **La visualizzazione HTML e la dimensione del grafo hanno entrambe un tetto massimo.** `graph.html` / `DECOUPLE.html` saltano la generazione oltre i 5.000 nodi per default (`MAX_NODES_FOR_VIZ`, alzabile tramite `GRAPHIFY_VIZ_NODE_LIMIT`); `graph.json` stesso è limitato a 512 MiB (`GRAPHIFY_MAX_GRAPH_BYTES` per sovrascriverlo). Usa `--no-viz` insieme a `query`/`path`/`explain` per corpus che superano uno dei due limiti.
- **La consapevolezza cross-progetto è opt-in, non automatica.** `graphify query` vede solo l'unico grafo a cui punti. Le domande multi-repository richiedono di registrare esplicitamente prima ogni progetto nel grafo condiviso (`graphify global add`, limitato a `GRAPHIFY_MAX_CONTEXTS` contesti non predefiniti per server MCP) — graphify non esegue mai da solo la scansione della tua macchina alla ricerca di altri repository.
- **L'estrazione parallela multi-agente dipende dalla piattaforma.** Richiede supporto lato assistente per generare subagent (`multi_agent = true` in `~/.codex/config.toml` per Codex, lo strumento Agent/Task su Claude Code/CodeBuddy/Factory Droid/Trae). OpenClaw e Aider attualmente estraggono solo in modo sequenziale.
- **Il server MCP HTTP condiviso si lega solo a loopback per default.** Raggiungerlo da un'altra macchina richiede un `--host 0.0.0.0` **e** un `--api-key` espliciti; graphify non gestisce TLS né alcuna autenticazione oltre quel singolo token bearer.
- **PowerShell interpreta uno `/` iniziale come separatore di percorso.** `/graphify .` fallisce su Windows PowerShell per questo motivo, non è un bug di graphify — usa invece `graphify .`.

---

## Risoluzione dei problemi

**`graphify: command not found` dopo l'installazione**
La CLI è installata ma la sua directory bin non è nel `PATH` della tua shell. Scegli la correzione in base a come hai installato:
- **uv** (`uv tool install graphifyy`): il comando finisce nella tool bin dir di uv (`~/.local/bin`), che spesso un setup macOS/zsh appena fatto non ha nel `PATH`. Esegui `uv tool update-shell`, poi apri un nuovo terminale. (Trova la directory con `uv tool dir --bin`.)
- **pipx** (`pipx install graphifyy`): esegui `pipx ensurepath`, poi apri un nuovo terminale.
- **pip** (`pip install graphifyy`): pip installa gli script in una user bin dir che potrebbe non essere nel `PATH` — aggiungi `~/Library/Python/3.x/bin` (macOS) o `~/.local/bin` (Linux) al tuo `PATH` in `~/.zshrc`/`~/.bashrc`, oppure esegui semplicemente `python -m graphify`.

**`uvx graphify …` o `uv tool run graphify …` non riesce a risolvere `graphify`**
Il pacchetto PyPI è `graphifyy`; `graphify` è solo il comando che fornisce. `uv tool run` tratta la prima parola come *nome del pacchetto*, quindi cerca un pacchetto chiamato `graphify` e segnala `No solution found … no versions of graphify`. Nomina esplicitamente il pacchetto: `uvx --from graphifyy graphify install` (uguale a `uv tool run --from graphifyy graphify install`). Oppure esegui `uv tool install graphifyy` una volta e poi chiama `graphify` direttamente.

**`uv run --with graphifyy python -m graphify` esegue silenziosamente un'installazione più vecchia**
`uv run` usa il Python di *sistema*, quindi se una `graphifyy` più vecchia vive anche lì (ad es. un vecchio `pip install graphifyy`), Python può trovare prima quella copia su `sys.path` e `--with graphifyy` non la sovrascriverà. Viene eseguito senza errori, ma ottieni il comportamento della versione *vecchia* — ad es. gli override d'ambiente come `OPENAI_BASE_URL` vengono ignorati silenziosamente, quindi le richieste raggiungono l'endpoint predefinito e falliscono con un 401 che sembra una chiave sbagliata. L'indizio è una riga `warning: skill is from graphify <newer>, package is <older>` — significa che è stata caricata un'installazione diversa, non solo una skill obsoleta. Controlla quale copia è stata effettivamente caricata:
```bash
python -c "import graphify; print(graphify.__file__)"
```
Poi esegui direttamente il comando installato (usa la copia gestita da uv), oppure elimina la copia di sistema obsoleta:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` funziona ma il comando `graphify` no**
Il `PATH` della tua shell non include la directory bin in cui è stato installato il comando. Preferisci `uv tool install` / `pipx install` al semplice `pip`, poi esegui `uv tool update-shell` / `pipx ensurepath` e apri un nuovo terminale (vedi le note di installazione sopra).

**`/graphify .` causa "path not recognized" in PowerShell**
PowerShell tratta uno `/` iniziale come separatore di percorso. Usa `graphify .` (senza slash) su Windows.

**Il grafo ha meno nodi dopo `--update` o una ricostruzione**
Se un refactor ha eliminato dei file, i vecchi nodi restano. Passa `--force` (o imposta `GRAPHIFY_FORCE=1`) per sovrascrivere anche quando la ricostruzione ha meno nodi.

**`extract` termina con "extraction was incomplete ... refusing to overwrite"**
Quando un passaggio di estrazione va in crash o una scansione non riesce a leggere completamente il corpus, l'esecuzione risulterebbe più piccola di una completa, quindi `graphify extract` rifiuta di sovrascrivere un grafo esistente più grande con il risultato parziale (proteggendo il tuo `graph.json`). Risolvi il problema alla base e riesegui, oppure passa `--allow-partial` per sovrascrivere comunque.

**Il grafo ha nodi duplicati per la stessa entità (ghost duplicates)**
I ghost duplicate (lo stesso simbolo che appare due volte — una dall'estrazione AST con una posizione nel sorgente, una dall'estrazione semantica senza) vengono ora uniti automaticamente al momento della build. Se lo vedi in un grafo costruito prima della v0.8.33, esegui una ri-estrazione completa per ripulire:
```bash
graphify extract . --force
```

**Ollama esaurisce la VRAM / finestra di contesto superata**
La finestra KV-cache viene dimensionata automaticamente ma potrebbe essere troppo grande per la tua GPU. Riducila:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**Avvisi `LLM returned invalid JSON` / `Unterminated string`**
La risposta JSON del modello ha raggiunto il suo limite di token di output ed è stata troncata a metà stringa. graphify si autoripara (divide il chunk e ri-estrae le due metà, e un singolo documento troppo grande viene prima suddiviso ai confini di titolo/paragrafo così l'intero file resta comunque coperto), quindi questi avvisi sono rumorosi ma non causano perdita di dati. Per ridurre il fenomeno, alza il limite di output o riduci l'output di ogni chunk:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
Con un gateway cloud come OpenRouter, preferisci `--backend openai` (impostando `OPENAI_BASE_URL`) rispetto allo shim Ollama — è un percorso compatibile con OpenAI più pulito. Se il modello ha un proprio tetto massimo di output, abbassare `--token-budget` è la leva più affidabile.

**L'HTML del grafo è troppo grande per essere aperto in un browser (>5000 nodi)**
Salta la generazione dell'HTML e usa direttamente il JSON:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**`graph.json` ha marcatori di conflitto dopo che due sviluppatori committano contemporaneamente**
Esegui `graphify hook install` — imposta un merge driver git che unisce automaticamente `graph.json` (union-merge) così i conflitti non si verificano mai.

**L'estrazione restituisce nodi/archi vuoti per documenti o PDF**
Documenti, PDF e immagini richiedono una chiamata LLM — i corpus solo di codice non necessitano di alcuna chiave. Controlla che la tua chiave API sia impostata e che il backend sia corretto:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**Avviso di mismatch di versione della skill nel tuo IDE**
La versione di graphify installata è diversa dal file della skill. Aggiorna:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**La prompt cache di Claude Code viene invalidata dopo ogni `graphify extract`**
Graphify scrive i file di output (`graph.json`, `graphify-out/`) nel workspace. Se questi percorsi non sono ignorati, ogni scrittura invalida la prompt cache di Claude Code, forzando un ri-caricamento completo a tariffe di scrittura cache al turno successivo. Aggiungili a `.claudeignore`:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## Riferimento completo dei comandi

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

> **Nomi delle community:** dentro un agente (Claude Code, Gemini CLI) è l'agente stesso a nominare le community. Quando esegui la CLI da sola, `cluster-only` le nomina automaticamente con il backend configurato (provider integrato o compatibile con OpenAI personalizzato) — passa `--no-label` per mantenere `Community N`, oppure esegui `graphify label` per (ri)generare i nomi su richiesta.

---

## Per saperne di più

- [Come funziona](../how-it-works.md) — la pipeline di estrazione, il rilevamento delle community, il punteggio di confidenza, i benchmark
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — suddivisione dei moduli, come aggiungere un linguaggio
- [Integrazioni opzionali](../docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — il libro sulle idee dietro graphify, l'architettura end-to-end

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) è il livello always-on costruito sopra graphify — applica lo stesso approccio a grafo all'intero tuo contesto di lavoro: riunioni, file, documenti e codice, aggiornandosi continuamente in background.

Pensato per persone e team il cui lavoro vive attraverso centinaia di conversazioni e documenti che non potranno mai ricostruire del tutto.

**[Iscriviti alla waitlist su graphify.com](https://graphify.com).** La prova gratuita sarà presto disponibile.

---

<details>
<summary>Contribuire</summary>

### Configurazione per lo sviluppo

Il progetto usa [uv](https://docs.astral.sh/uv/) per il flusso di lavoro di sviluppo. Installalo una volta, poi:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

Verifica l'installazione in modalità editable:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### Esecuzione dei test

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> Nota macOS: la suite di test include sia il fixture `sample.f90` che `sample.F90`. Questi collidono su file system case-insensitive HFS+ / APFS. Esegui su Linux o in un container Docker se hai bisogno di testare entrambe le varianti Fortran contemporaneamente.

### Flusso di lavoro Git

- Lo sviluppo attivo avviene sul branch `v8`.
- Stile dei commit: `fix: <description>` / `feat: <description>` / `docs: <description>`
- Prima di aprire una PR, esegui `uv run pytest tests/ -q` e conferma che passi.
- Aggiungi un file fixture in `tests/fixtures/` e dei test in `tests/test_languages.py` per ogni nuovo estrattore di linguaggio.

### Cosa contribuire

I **worked example** (esempi lavorati) sono il contributo più utile. Esegui `/graphify` su un corpus reale, salva l'output in `worked/{slug}/`, scrivi un `review.md` onesto che copra cosa il grafo ha fatto bene e cosa ha sbagliato, e apri una PR.

**Bug di estrazione** — apri una issue con il file di input, la voce di cache (`graphify-out/cache/`), e cosa è stato tralasciato o sbagliato.

Vedi [ARCHITECTURE.md](../../ARCHITECTURE.md) per le responsabilità dei moduli e come aggiungere un linguaggio.

</details>
