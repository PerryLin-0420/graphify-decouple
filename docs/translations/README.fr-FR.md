<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>Un fork de <a href="https://github.com/Graphify-Labs/graphify">graphify</a> qui ajoute <code>graphify decouple</code></b> — 0-LLM, candidats Extract-Class notés par risque pour les god objects, revérifiés par rapport au code source réel (et non pas seulement le graphe d'appels) avant toute recommandation. Voir <a href="#decouple-candidats-extract-class-notés-par-risque">Decouple : candidats Extract-Class notés par risque</a> ci-dessous.
</p>

<div align="center">
<details><summary><b>Lire ceci dans d'autres langues</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>L'accès anticipé à la plateforme graphify est ouvert avant le lancement public de la v1 : <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

Tapez `/graphify` dans votre assistant de codage IA et il cartographie l'ensemble de votre projet (code, docs, PDF, images, vidéos) sous forme de **graphe de connaissances** que vous pouvez **interroger au lieu de faire des recherches (grep)** dans les fichiers.

- **Cartographie du code gratuite, entièrement locale.** Le code est analysé avec l'AST tree-sitter : déterministe, sans LLM, rien ne quitte votre machine. (Les docs, PDF, images et vidéos utilisent le modèle de votre assistant, ou une clé API configurée, pour une passe sémantique.)
- **Chaque lien est expliqué.** Chaque connexion est étiquetée `EXTRACTED` (explicite dans le code source) ou `INFERRED` (résolue par graphify), afin que vous puissiez distinguer ce qui a été lu directement de ce qui a été déduit.
- **Ce n'est pas un index vectoriel.** Pas d'embeddings, pas de base vectorielle : un vrai graphe que vous parcourez. Posez une question, tracez le chemin entre deux éléments, ou expliquez un concept.

> Vous voulez que cela tourne en permanence, en se mettant à jour en arrière-plan sur votre code, vos docs et vos réunions plutôt que seulement à la demande ? C'est ce que nous construisons chez **[graphify.com](https://graphify.com)**, et l'accès anticipé est ouvert dès maintenant sur **[app.graphify.com](https://app.graphify.com/login)**.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="Le graph.html interactif de graphify montrant le codebase FastAPI sous forme de graphe de connaissances à disposition dirigée par les forces, avec une légende des communautés détectées" width="900">
</p>
<p align="center">
  <em>Le codebase de FastAPI cartographié par graphify. Chaque nœud est un concept, les couleurs sont les communautés détectées, et l'ensemble est cliquable dans graph.html.</em>
</p>

**Pour démarrer** (30 secondes) :

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

Ensuite, dans votre assistant IA :

```
/graphify .
```

C'est tout. Vous obtenez **trois fichiers** :

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**Fonctionne avec** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, et 15+ autres — [choisissez votre plateforme](#installation).

---

## Voir en action

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="Requête de chemin graphify : un terminal demande le plus court chemin entre FastAPI et ModelField, et la réponse s'illumine saut par saut à travers le graphe de connaissances" width="900">
</p>

Une fois le graphe construit, vous l'interrogez au lieu de lire des fichiers. Sortie réelle, graphify exécuté sur le codebase FastAPI montré ci-dessus :

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

Chaque lien porte une **étiquette de confiance** (`EXTRACTED` = explicite dans le code source, `INFERRED` = dérivée par résolution), afin que vous puissiez distinguer ce qui a été lu directement de ce qui a été déduit. `graphify query "<question>"` renvoie un sous-graphe ciblé pour une question en langage naturel, et `graphify path A B` retrace comment deux éléments quelconques sont reliés.

---

## Decouple : candidats Extract-Class notés par risque

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple : le god node MainWindow se divisant en classes candidates notées par risque, avec un avertissement d'état partagé entre deux d'entre elles" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html : les 5 classes proposées pour MainWindow, panneau Node Info ouvert sur Main Window Axis and Range Controls montrant un chevauchement d'état de 0.608 avec Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>DECOUPLE.html sur une exécution réelle — cliquer sur une classe proposée montre exactement avec quelle autre classe elle partage de l'état, et ce qui est précisément partagé.</em>
</p>

La même page rend également la division elle-même. Basculer **Preview decoupled view** remplace les méthodes propres de la god class par les classes proposées et réachemine les arêtes sur place — le changement de câblage, pas un diagramme redessiné :

| Avant — la god class aujourd'hui | Après — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html avant la bascule : un unique nœud pivot MainWindow avec ses propres méthodes déployées autour de lui" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html après la bascule : le même nœud réduit à 5 classes proposées en losange, des arêtes vertes en pointillés montrant quelles méthodes ont été extraites dans chacune, des arêtes rouges montrant l'état d'instance partagé entre deux d'entre elles" width="440"> |
| Un nœud contenant 47 de ses propres méthodes, chacune accessible uniquement à travers la classe. | Les classes proposées. Vert pointillé = ce qui a été extrait dans chacune ; rouge = l'état d'instance que deux d'entre elles partagent encore, ce qui décide précisément entre `split` et `keep_as_is`. Seuls les candidats qui franchissent le seuil de risque sont dessinés — ici 5 sur 6, d'où une méthode sans losange où atterrir. |

`graphify decouple` repère les god objects et vous dit si les diviser en vaut réellement la peine — pas seulement s'ils sont gros.

Le mode d'échec que cet outil cherche à repérer : une classe de 47 méthodes que le clustering par graphe d'appels divise joyeusement en 5 groupes d'apparence bien nette, qui continuent tous à lire et écrire exactement le même état d'instance `self._chart_style` / `self._crosshair` en dessous. Livrez cette division et vous n'avez rien découplé du tout — vous avez déplacé des méthodes dans de nouveaux fichiers qui ne peuvent toujours pas être testés, modifiés ou raisonnés indépendamment, parce qu'ils ont tous encore besoin du même état partagé qui leur est repassé. Un outil qui ne regarde que le graphe d'appels ne peut absolument pas voir cela ; il doit revenir au code source réel.

**Deux vérifications, toutes deux 0-LLM, toutes deux déterministes :**

1. **S'agit-il seulement d'un God Object ?** Un nœud à haut degré peut être un véritable God Object (beaucoup de ses PROPRES méthodes, réparties sur des responsabilités sans rapport — Extract Class s'applique) ou un hub/modèle de données sur-référencé (peu de méthodes propres, surtout des références *entrantes* — diviser son corps ne sert à rien ; la solution est de restreindre son interface, pas d'extraire une classe). `classify_god_node` distingue les deux via le `member_ratio`, pas via le degré brut — c'est cette différence qui évite à `TraceSource` (84 arêtes, mais seulement 6 de ses propres méthodes) de recevoir une suggestion de division fallacieuse, alors que `MainWindow` (88 arêtes, 47 de ses propres méthodes) la reçoit à juste titre.
2. **La division réduirait-elle réellement le couplage ?** `risk_before` (la taille/le couplage/la fragmentation actuels du god node) est comparé à `risk_after` — le NOUVEAU risque que la division elle-même introduirait : des appels inter-groupes qui étaient des arêtes intra-classe invisibles et qui deviennent des dépendances inter-classes explicites, des appelants qui devraient désormais dépendre de plus d'une nouvelle classe, et — la vérification qu'un graphe d'appels ne peut structurellement pas faire — la quantité d'état d'instance `self`/`this` (lectures, écritures et appels de méthodes d'aide partagées, pondérés séparément : une **écriture** partagée est notée plus haut qu'une lecture partagée) que les groupes proposés ont réellement en commun. Cette vérification réanalyse directement le fichier source du god node lui-même avec tree-sitter ; elle ne repose pas sur le graphe déjà extrait par graphify, qui n'enregistre jamais l'accès aux champs pour aucun langage. Ce n'est que lorsque `risk_after` passe sous un seuil par rapport à `risk_before` que le plan recommande `split` — sinon c'est `marginal` ou `keep_as_is`, et un candidat déconseillé est rapporté comme un nombre, jamais dessiné comme une forme que vous devriez remettre en question à l'œil nu.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

Produit trois fichiers à côté de `graph.json` :

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

**Couverture linguistique pour la vérification de partage d'état** (la classification basée uniquement sur le graphe d'appels ci-dessus fonctionne pour tous les langages que graphify extrait ; ce tableau concerne spécifiquement la réanalyse du code source qui vérifie le chevauchement d'état `self`/`this`) :

| Langage | Pris en charge | Remarques |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` est son propre nœud AST, pas un accès de champ enveloppé — géré explicitement |
| C# | ✅ | |
| Rust | ✅ | `self.x` via les blocs `impl` |
| Ruby | ✅ | `@x` (l'idiome dominant) + les appels `self.foo` |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | résolution du récepteur par méthode — Go n'a pas de mot-clé `self`/`this`, donc le nom du récepteur (`f` dans `func (f *Foo) M()`) est résolu à nouveau pour chaque méthode |
| C | ❌ | un paramètre pointeur de struct n'a aucun marqueur syntaxique le distinguant d'un autre paramètre — aucun signal fiable sans inférence de type complète |

Un god node dans un langage non pris en charge, ou dont le code source ne peut pas être lu, est marqué `state_analysis: "skipped"` — la classification et le score du graphe d'appels s'exécutent quand même, mais la recommandation repose uniquement sur le graphe d'appels plutôt que de supposer silencieusement que la vérification d'état a réussi.

---

## Ce que fait l'outil

Ce que vous obtenez d'entrée de jeu :

| Capacité | Ce que vous obtenez |
|---|---|
| **God nodes** | Les concepts les plus connectés, pour voir ce à travers quoi tout transite |
| **Communautés** | Le graphe divisé en sous-systèmes (Leiden), avec des étiquettes sans LLM |
| **Liens inter-fichiers** | `calls` / `imports` / `inherits` / `mixes_in` résolus à travers ~40 langages via l'AST tree-sitter |
| **Query, path, explain** | Posez une question, tracez le chemin entre deux éléments, ou expliquez un concept, le tout contre `graph.json` |
| **Justification + références de docs** | Les commentaires `# NOTE:` / `# WHY:` et les citations ADR/RFC deviennent des nœuds de première classe reliés au code |
| **Au-delà du code** | Les docs, PDF, images et vidéo/audio se cartographient tous dans le même graphe |
| **Priorité au local** | Le code est analysé localement avec tree-sitter (pas de LLM, rien ne quitte votre machine) ; seule la passe sémantique sur les docs/médias appelle un backend, et seulement si vous en configurez un |

---

## Benchmarks

| Benchmark | Métrique | graphify | Concurrence |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | Précision QA | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | Précision QA | **76%** | à égalité avec dense RAG |
| Construction du graphe | Crédits LLM | **0** | par jeton pour la plupart des systèmes |

Chaque système a tourné sur le même harnais, avec le même modèle et les mêmes budgets, noté par un juge validé à l'aveugle contre un second juge (90,6 % d'accord, kappa de Cohen 0,81). Tableaux complets par système, résultat sur l'intelligence de code, et commandes de reproduction : **[BENCHMARKS.md](../../BENCHMARKS.md)**.

---

## Prérequis

| Prérequis | Minimum | Vérifier | Installer |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(recommandé)* | n'importe laquelle | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(alternative)* | n'importe laquelle | `pipx --version` | `pip install pipx` |

**Installation rapide macOS (Homebrew) :**
```bash
brew install python@3.12 uv
```

**Installation rapide Windows :**
```powershell
winget install astral-sh.uv
```

**Ubuntu/Debian :**
```bash
sudo apt install python3.12 python3-pip pipx
# or install uv:
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## Installation

> **Paquet officiel :** Le paquet PyPI est `graphifyy` (double y). Les autres paquets `graphify*` sur PyPI ne sont pas affiliés. La commande CLI reste `graphify`.

**Étape 1 — installer le paquet :**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**Étape 2 — enregistrer la skill auprès de votre assistant IA :**

```bash
graphify install
```

C'est tout. Ouvrez votre assistant IA et tapez `/graphify .`

Pour installer la skill de l'assistant dans le dépôt courant plutôt que dans votre
profil utilisateur, ajoutez `--project` :

```bash
graphify install --project
graphify install --project --platform codex
```

Les installations à portée de projet écrivent dans le répertoire courant, par exemple
`.claude/skills/graphify/SKILL.md` ou `.agents/skills/graphify/SKILL.md` (plus un
sidecar `references/` que la skill charge à la demande), et
affichent une suggestion `git add` pour les fichiers qui peuvent être committés.
Les commandes par plateforme qui prennent en charge les installations à portée de projet
acceptent la même option, par exemple `graphify claude install --project` ou `graphify codex install --project`.

> **Remarque PowerShell :** Utilisez `graphify .` et non `/graphify .` — la barre oblique de tête est un séparateur de chemin dans PowerShell.

> **`graphify: command not found` ?** `uv tool install` / `pipx install` placent la commande `graphify` dans leur répertoire bin d'outils (`~/.local/bin`). Si votre shell ne la trouve pas juste après l'installation — fréquent sur une installation macOS + zsh toute fraîche — ce répertoire n'est pas encore dans votre `PATH` : lancez `uv tool update-shell` (ou `pipx ensurepath`), puis ouvrez un nouveau terminal. Avec `pip` seul, ajoutez `~/.local/bin` (Linux) ou `~/Library/Python/3.x/bin` (Mac) à votre PATH, ou lancez `python -m graphify`.

> **Vous utilisez `uvx` / `uv tool run` au lieu d'installer ?** Nommez le paquet, pas la commande : `uvx --from graphifyy graphify install`. Le simple `uvx graphify …` échoue (`No solution found … no versions of graphify`) parce que `uv tool run` lit le premier mot comme un *paquet*, et le paquet est `graphifyy` — la commande `graphify` vit à l'intérieur.

> **Évitez `pip install` sur Mac/Windows** si possible. La skill résout Python au moment de l'exécution à partir de `graphify-out/.graphify_python` ; si celui-ci pointe vers un environnement différent de celui où `pip` a installé le paquet, vous obtiendrez `ModuleNotFoundError: No module named 'graphify'`. `uv tool install` et `pipx install` isolent le paquet dans leur propre environnement et évitent complètement ce problème.

> **Git hooks et uv tool / pipx :** `graphify hook install` intègre le chemin de l'interpréteur courant directement dans les scripts de hook au moment de l'installation, afin que le hook post-commit se déclenche correctement même dans les clients git graphiques et les runners CI où `~/.local/bin` n'est pas dans le PATH. Si vous réinstallez ou mettez à niveau graphify, relancez `graphify hook install` pour rafraîchir le chemin intégré.

> **Mode strict (Claude Code) :** `graphify install --project --strict` fait en sorte que l'assistant utilise réellement le graphe. L'installation par défaut *incite* l'assistant à lancer `graphify query` avant de lire des fichiers ; le mode strict *bloque* la première lecture brute de fichier source d'une session et la redirige vers le graphe, puis revient à l'incitation (de sorte qu'il se déclenche au plus une fois par session et ne reste jamais bloqué). Basculez à l'exécution avec `GRAPHIFY_HOOK_STRICT=1`/`0` ; l'installation par défaut reste inchangée (incitation douce).

<details>
<summary><b>Choisissez votre plateforme</b> (20+ assistants, cliquez pour développer)</summary>

| Plateforme | Commande d'installation |
|----------|----------------|
| Claude Code (Linux/Mac) | `graphify install` |
| Claude Code (Windows) | `graphify install` (détection automatique) ou `graphify install --platform windows` |
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

Les utilisateurs de Codex ont aussi besoin de `multi_agent = true` sous `[features]` dans `~/.codex/config.toml` pour l'extraction parallèle. CodeBuddy utilise le même outil Agent et le même mécanisme de hook PreToolUse que Claude Code. Factory Droid utilise l'outil `Task` pour la répartition parallèle des sous-agents. OpenClaw et Aider utilisent l'extraction séquentielle (le support des agents parallèles est encore récent sur ces plateformes). Trae utilise l'outil Agent pour la répartition parallèle des sous-agents et ne prend **pas** en charge les hooks `PreToolUse`, donc AGENTS.md est le mécanisme toujours actif.

`--platform agents` (alias `--platform skills`) cible les emplacements génériques multi-framework [Agent-Skills](https://github.com/anthropics/skills) : le `~/.agents/skills/` global de l'utilisateur défini par la spec (lu par `npx skills` et les frameworks conformes à la spec) pour une installation globale, et `./.agents/skills/` pour une installation de projet (`--project`). Le simple `graphify install` reste mono-plateforme (Claude Code) par conception — utilisez la plateforme nommée `agents` quand vous voulez que la skill soit détectable par n'importe quel framework qui lit `.agents/skills`.

> Codex utilise `$graphify` au lieu de `/graphify`.

</details>

<details>
<summary><b>Extras optionnels</b> (installez seulement ce dont vous avez besoin)</summary>

| Extra | Ce que ça ajoute | Installer |
|---|---|---|
| `pdf` | Extraction PDF | `uv tool install "graphifyy[pdf]"` |
| `office` | Support `.docx` et `.xlsx` | `uv tool install "graphifyy[office]"` |
| `google` | Rendu Google Sheets | `uv tool install "graphifyy[google]"` |
| `video` | Transcription vidéo/audio (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | Serveur MCP stdio | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Support d'export Neo4j | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | Support d'export FalkorDB | `uv tool install "graphifyy[falkordb]"` |
| `svg` | Export du graphe en SVG | `uv tool install "graphifyy[svg]"` |
| `leiden` | Détection de communautés Leiden (Python < 3.13 uniquement) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Inférence locale Ollama | `uv tool install "graphifyy[ollama]"` |
| `openai` | API OpenAI / compatibles OpenAI | `uv tool install "graphifyy[openai]"` |
| `gemini` | API Google Gemini | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | API Anthropic Claude (`--backend claude`, utilise `ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (utilise IAM, pas de clé API) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, utilise `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "graphifyy[openai]"` |
| `sql` | Extraction de schéma SQL | `uv tool install "graphifyy[sql]"` |
| `postgres` | Introspection PostgreSQL en direct (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | Extraction AST BYOND DreamMaker `.dm`/`.dme` (peut nécessiter un compilateur C + `python3-dev` si aucune wheel ne correspond à votre plateforme) | `uv tool install "graphifyy[dm]"` |
| `terraform` | Extraction AST Terraform / HCL `.tf`/`.tfvars`/`.hcl` | `uv tool install "graphifyy[terraform]"` |
| `pascal` | Extraction AST Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` (arêtes `calls`/`inherits` plus précises ; retombe sur un extracteur regex en son absence) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | Segmentation de requêtes en chinois (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | Tout ce qui précède | `uv tool install "graphifyy[all]"` |

</details>

---

## Faire en sorte que votre assistant utilise toujours le graphe

Lancez ceci une fois dans votre projet après avoir construit un graphe :

| Plateforme | Commande |
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

Ceci écrit un petit fichier de configuration qui indique à votre assistant de consulter le graphe de connaissances pour les questions sur le codebase, en préférant des requêtes ciblées comme `graphify query "<question>"` plutôt que de lire le rapport complet ou de faire des recherches (grep) dans les fichiers bruts.

- **Plateformes à hook** (Claude Code, Gemini CLI) : un hook se déclenche automatiquement avant les appels d'outils de type recherche (et, sur Claude Code, avant de lire les fichiers source un par un via les outils Read/Glob) et incite votre assistant à emprunter le chemin du graphe.
- **Plateformes à fichier d'instructions** (Codex, OpenCode, Cursor, etc.) : des fichiers d'instructions persistants (`AGENTS.md`, `.cursor/rules/`, etc.) fournissent le même conseil de requête d'abord.

`GRAPH_REPORT.md` reste disponible pour une revue d'architecture large.

**CodeBuddy** fait les deux mêmes choses que Claude Code : il écrit une section `CODEBUDDY.md` indiquant à CodeBuddy de lire `graphify-out/GRAPH_REPORT.md` avant de répondre aux questions d'architecture, et installe des hooks `PreToolUse` (`.codebuddy/settings.json`) qui se déclenchent avant les commandes de recherche Bash et les lectures de fichiers, incitant à utiliser `graphify query` à la place.

**Codex** écrit dans `AGENTS.md`, qui est ce qui porte réellement le conseil toujours actif sur le graphe sur cette plateforme. `graphify codex install` enregistre aussi un hook `PreToolUse` dans `.codex/hooks.json` (`graphify hook-check`), mais cette entrée est délibérément un **no-op** : Codex Desktop rejette `hookSpecificOutput.additionalContext` sur `PreToolUse`, donc émettre une incitation à cet endroit casserait les appels d'outil Bash. Contrairement à Claude Code, où le hook (`graphify hook-guard`) fait l'incitation, sur Codex le hook se déclenche et ne fait volontairement rien, et `AGENTS.md` est le mécanisme toujours actif.

**Kilo Code** installe la skill Graphify dans `~/.config/kilo/skills/graphify/SKILL.md` et une commande native `/graphify` dans `~/.config/kilo/command/graphify.md`. `graphify kilo install` écrit aussi `AGENTS.md` plus un plugin natif `tool.execute.before` (`.kilo/plugins/graphify.js` + enregistrement dans `.kilo/kilo.json` ou `.kilo/kilo.jsonc`) afin que Kilo bénéficie du même rappel de graphe toujours actif via la configuration native `.kilo`.

**Cursor** écrit `.cursor/rules/graphify.mdc` avec `alwaysApply: true`, donc Cursor l'inclut automatiquement dans chaque conversation, sans hook nécessaire.

Pour retirer graphify de toutes les plateformes en une fois : `graphify uninstall` (ajoutez `--purge` pour aussi supprimer `graphify-out/`). Ou utilisez la commande par plateforme (par exemple `graphify claude uninstall`).

---

## Ce que contient le rapport

- **God nodes** — les concepts les plus connectés de votre projet. Tout transite par eux.
- **Connexions surprenantes** — des liens entre des éléments qui vivent dans des fichiers ou modules différents. Classés selon leur degré d'inattendu.
- **Le « pourquoi »** — les commentaires en ligne (`# NOTE:`, `# WHY:`, `# HACK:`), les docstrings et la justification de conception issue des docs sont extraits comme des nœuds distincts reliés au code qu'ils expliquent.
- **Questions suggérées** — 4 à 5 questions auxquelles le graphe est particulièrement bien placé pour répondre.
- **Étiquettes de confiance** — chaque relation déduite est marquée `EXTRACTED`, `INFERRED`, ou `AMBIGUOUS`. Vous savez toujours ce qui a été trouvé par rapport à ce qui a été deviné.

---

## Quels fichiers sont pris en charge

| Type | Extensions |
|------|-----------|
| Code (36 grammaires tree-sitter) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme` nécessite `uv tool install graphifyy[dm]` ; `.mts`/`.cts` réutilisent la grammaire TypeScript, `.cc`/`.cxx` ainsi que CUDA `.cu`/`.cuh` et Metal `.metal` réutilisent la grammaire C++) |
| Salesforce Apex | `.cls .trigger` (basé sur des regex ; classes, interfaces, enums, méthodes, triggers, arêtes SOQL/DML) |
| Terraform / HCL | `.tf .tfvars .hcl` (nécessite `uv tool install graphifyy[terraform]`) |
| Configurations MCP | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — extrait les nœuds de serveur, les références de paquets, les exigences de variables d'environnement |
| Manifestes de paquets | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — un nœud de paquet canonique par paquet (par nom) plus des arêtes `depends_on`, de sorte qu'un paquet référencé depuis plusieurs manifestes reste un hub unique |
| Docs | `.md .mdx .qmd .html .txt .rst .yaml .yml` (les liens markdown `[text](./other.md)` et les `[[wikilinks]]` deviennent des arêtes `references` entre les docs) |
| Office | `.docx .xlsx` (nécessite `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (opt-in ; nécessite l'authentification `gws` et `--google-workspace` ; Sheets nécessite `uv tool install graphifyy[google]`) |
| PDF | `.pdf` |
| Images | `.png .jpg .webp .gif` |
| Vidéo / Audio | `.mp4 .mov .mp3 .wav` et plus (nécessite `uv tool install graphifyy[video]`) |
| YouTube / URL | n'importe quelle URL vidéo (nécessite `uv tool install graphifyy[video]`) |

Le code est extrait **localement sans aucun appel API** (AST via tree-sitter). Tout le reste passe par l'API du modèle de votre assistant IA.

Les fichiers `.gdoc`, `.gsheet` et `.gslides` de Google Drive pour ordinateur sont des
pointeurs de raccourci, pas le contenu du document. Pour inclure les Google Docs, Sheets et Slides natifs
dans une extraction headless, installez et authentifiez le
[CLI `gws`](https://github.com/googleworkspace/cli), puis lancez :

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

Vous pouvez aussi définir `GRAPHIFY_GOOGLE_WORKSPACE=1`. Graphify exporte les raccourcis dans
`graphify-out/converted/` sous forme de fichiers Markdown annexes, puis extrait ces fichiers.

---

## Commandes courantes

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

Voir [Decouple : candidats Extract-Class notés par risque](#decouple-candidats-extract-class-notés-par-risque) ci-dessus, ou la [référence complète des commandes](#référence-complète-des-commandes) ci-dessous.

---

## Ignorer des fichiers

Créez un `.graphifyignore` à la racine de votre projet — même syntaxe que `.gitignore`, y compris la négation `!`.

**`.gitignore` est respecté automatiquement.** graphify lit le `.gitignore` de chaque répertoire. Si un `.graphifyignore` est également présent, les deux sont **fusionnés** — les motifs de `.graphifyignore` sont évalués en dernier, donc ils l'emportent en cas de conflit (y compris les négations `!`). Ajouter un `.graphifyignore` ne fait jamais qu'exclure davantage ; il ne réinclut jamais un fichier déjà exclu par votre `.gitignore`. La portée par sous-répertoire fonctionne comme avec git — un fichier d'exclusion n'affecte que sa propre sous-arborescence.

Passez `--no-gitignore` à `graphify extract` lorsque du code généré ou transpilé ignoré par git doit figurer dans le graphe. Cela désactive `.gitignore` et `.git/info/exclude` ; `.graphifyignore` s'applique toujours.

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

## Configuration en équipe

`graphify-out/` est destiné à être committé dans git afin que toute l'équipe démarre avec une carte.

**Ajouts recommandés au `.gitignore` :**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` est désormais portable — les clés sont stockées sous forme de chemins relatifs et réancrées au chargement, donc le committer est sûr et évite une reconstruction complète au premier checkout.

**Flux de travail :**
1. Une personne lance `/graphify .` et committe `graphify-out/`.
2. Tout le monde tire (pull) — leur assistant lit le graphe immédiatement.
3. Lancez `graphify hook install` pour reconstruire automatiquement après chaque commit (AST uniquement, aucun coût d'API). Cela configure aussi un driver de fusion git afin que `graph.json` ne se retrouve jamais avec des marqueurs de conflit : deux développeurs qui committent en parallèle voient leurs graphes fusionnés automatiquement (union).
4. Quand des docs ou des papers changent, lancez `/graphify --update` pour rafraîchir ces nœuds.

---

## Utiliser le graphe directement

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

Le serveur MCP donne à votre assistant un accès structuré : `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Serveur HTTP partagé

`--transport stdio` (par défaut) lance un serveur local par développeur. `--transport http` sert les mêmes outils via le transport MCP Streamable HTTP, de sorte qu'un unique processus partagé peut servir le graphe pour toute l'équipe — les clients pointent la configuration MCP de leur IDE vers `http://<host>:8080/mcp` plutôt que de lancer graphify localement.

| Option | Par défaut | Objectif |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Transport sur lequel servir |
| `--host` | `127.0.0.1` | Hôte de liaison HTTP (utilisez `0.0.0.0` pour exposer au-delà de localhost) |
| `--port` | `8080` | Port de liaison HTTP |
| `--api-key` | env `GRAPHIFY_API_KEY` | Exiger `Authorization: Bearer <key>` (ou `X-API-Key`) |
| `--path` | `/mcp` | Chemin de montage HTTP |
| `--json-response` | désactivé | Renvoyer du JSON brut au lieu de flux SSE |
| `--stateless` | désactivé | Aucun état par session (pour les déploiements à répartition de charge / CI) |
| `--session-timeout` | `3600` | Récupérer les sessions avec état inactives après N secondes (`0` désactive) |

La liaison par défaut `127.0.0.1` est en boucle locale uniquement. Définissez `--host 0.0.0.0` **et** `--api-key` ensemble lors d'une exposition sur un hôte partagé. Lancez-le dans un conteneur :

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **Remarque WSL / Linux :** Ubuntu fournit `python3`, pas `python`. Utilisez un venv pour éviter les conflits :
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## Variables d'environnement

Celles-ci ne sont nécessaires que pour l'**extraction headless / CI** (`graphify extract`). Lors de l'exécution via la skill `/graphify` dans votre IDE, l'API du modèle est fournie par votre session IDE — aucune clé supplémentaire n'est nécessaire.

| Variable | Utilisée pour | Quand requise |
|---|---|---|
| `ANTHROPIC_API_KEY` | Backend Claude (Anthropic) | `--backend claude` |
| `ANTHROPIC_BASE_URL` | URL de point de terminaison compatible Anthropic (proxy LiteLLM, gateways, ...) | `--backend claude` (par défaut : `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Nom du modèle pour le backend Claude — pour les points de terminaison personnalisés, utilisez le nom/alias de modèle exposé par votre serveur | `--backend claude` (par défaut : `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` ou `GOOGLE_API_KEY` | Backend Google Gemini | `--backend gemini` |
| `OPENAI_API_KEY` | API OpenAI ou compatibles OpenAI | `--backend openai` (les serveurs locaux acceptent n'importe quelle valeur non vide) |
| `OPENAI_BASE_URL` | URL de serveur compatible OpenAI (llama.cpp, vLLM, LM Studio, ...) | `--backend openai` (par défaut : `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | Nom du modèle pour le backend OpenAI — pour les serveurs auto-hébergés, utilisez le nom/alias de modèle exposé par votre serveur (vérifiez son endpoint `/v1/models`), par ex. `LFM2.5-8B-A1B-UD-Q4_K_XL` pour llama.cpp | `--backend openai` (par défaut : `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | Backend DeepSeek | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Backend Kimi Code | `--backend kimi` |
| `OLLAMA_BASE_URL` | URL d'inférence locale Ollama | `--backend ollama` (par défaut : `http://localhost:11434`) |
| `OLLAMA_MODEL` | Nom du modèle Ollama | `--backend ollama` (par défaut : détection automatique) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Remplace la taille de la fenêtre de cache KV d'Ollama | optionnel — dimensionné automatiquement par défaut |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Minutes pendant lesquelles garder le modèle Ollama chargé | optionnel — définir `0` pour décharger après chaque bloc |
| `AZURE_OPENAI_API_KEY` | Backend Azure OpenAI Service | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | URL de point de terminaison de la ressource Azure | `--backend azure` (requis avec la clé API) |
| `AZURE_OPENAI_API_VERSION` | Remplace la version d'API Azure | optionnel — par défaut `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` ou `GRAPHIFY_AZURE_MODEL` | Nom du déploiement Azure | optionnel — par défaut `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — chaîne d'identifiants standard | `--backend bedrock` (pas de clé API, utilise IAM) |
| `GRAPHIFY_MAX_WORKERS` | Nombre de threads de parallélisme pour l'AST | optionnel — aussi l'option `--max-workers` |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Augmente le plafond de sortie pour les corpus denses | optionnel — par ex. `32768` pour les gros fichiers |
| `GRAPHIFY_API_TIMEOUT` | Délai d'expiration par appel en secondes pour les backends HTTP, claude-cli, SDK Anthropic et Bedrock (par défaut : 600) | optionnel — aussi l'option `--api-timeout` |
| `GRAPHIFY_MAX_RETRIES` | Combien de fois réessayer une requête limitée en débit (429) avant d'abandonner (par défaut : 6 ; respecte `Retry-After`) | optionnel — augmentez pour les limites strictes par organisation (par ex. kimi) ; `0` désactive |
| `GRAPHIFY_FORCE` | Force la reconstruction du graphe même avec moins de nœuds | optionnel — aussi l'option `--force` |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Active automatiquement l'export Google Workspace | optionnel — définir sur `1` |
| `GRAPHIFY_TRIAGE_BACKEND` | Backend pour `graphify prs --triage` | optionnel — détecté automatiquement selon les clés disponibles |
| `GRAPHIFY_TRIAGE_MODEL` | Remplace le modèle pour le triage | optionnel — par ex. `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | Définir sur `1` pour activer le journal de requêtes local dans `~/.cache/graphify-queries.log` (enregistre chaque question query/path/explain + chemin du corpus). Désactivé par défaut — rien n'est écrit sans opt-in (#1797) | optionnel |
| `GRAPHIFY_QUERY_LOG` | Active le journal de requêtes et l'écrit à cet emplacement au lieu de celui par défaut | optionnel — désactivé sauf si celui-ci ou `_ENABLE` est défini |
| `GRAPHIFY_QUERY_LOG_DISABLE` | Définir sur `1` pour forcer la désactivation du journal de requêtes (l'emporte sur les variables d'activation) | optionnel |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | Quand le journal est actif, enregistre aussi les réponses complètes de sous-graphe (désactivé par défaut) | optionnel |
| `GRAPHIFY_MAX_GRAPH_BYTES` | Remplace le plafond de taille de 512 Mio pour graph.json — par ex. `700MB`, `2GB`, ou en octets bruts | optionnel — utile pour les très gros corpus |
| `GRAPHIFY_MAX_CONTEXTS` | Nombre maximal de graphes de projet non par défaut conservés par un serveur MCP multi-projets | optionnel — par défaut : `8` ; les valeurs invalides utilisent `8`, et les valeurs inférieures à `1` utilisent `1` |
| `GRAPHIFY_LLM_TEMPERATURE` | Remplace la température du LLM pour l'extraction sémantique — par ex. `0.7`, ou `none` pour l'omettre | optionnel — omis automatiquement pour les modèles de raisonnement o1/o3/o4/gpt-5 |

---

## Confidentialité

- **Fichiers de code** — traités localement via tree-sitter. Rien ne quitte votre machine. Un corpus uniquement composé de code ne nécessite aucune clé API — `graphify extract` fonctionne entièrement hors ligne. Sur un dépôt mixte, ajoutez `--code-only` pour n'indexer que le code et ignorer les docs/PDF/images qui nécessiteraient sinon un LLM.
- **Vidéo / audio** — transcrits localement avec faster-whisper. Rien ne quitte votre machine.
- **Docs, PDF, images** — envoyés à votre assistant IA pour extraction sémantique (via la skill `/graphify`, en utilisant le modèle que fait tourner votre session IDE). `graphify extract` en mode headless nécessite `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), une instance Ollama en cours d'exécution (`OLLAMA_BASE_URL`), des identifiants AWS via la chaîne de fournisseurs standard (Bedrock — pas de clé API nécessaire, utilise IAM), ou le binaire CLI `claude` (Claude Code — pas de clé API nécessaire, utilise votre abonnement Claude). L'option `--dedup-llm` utilise la même clé.
- **Résidence des données** — `graphify extract` détecte automatiquement quel fournisseur utiliser selon la clé API définie (priorité : Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). Pour du code avec des exigences de résidence des données, utilisez `--backend ollama` (entièrement local) ou passez une option `--backend` explicite. Kimi (`MOONSHOT_API_KEY`) route vers les serveurs Moonshot AI en Chine.
- **Aucune télémétrie**, aucun suivi d'usage, aucune analytique.
- **Journalisation des requêtes** — chaque appel `graphify query`, `graphify path`, `graphify explain`, et MCP `query_graph` est journalisé dans `~/.cache/graphify-queries.log` au format JSON Lines (horodatage, question, corpus, nœuds renvoyés, durée). Les réponses complètes de sous-graphe ne sont **pas** stockées par défaut. Définissez `GRAPHIFY_QUERY_LOG_DISABLE=1` pour vous désinscrire, ou `GRAPHIFY_QUERY_LOG=/dev/null` pour faire taire le journal sans désactiver le chemin de code.

---

## Dépannage

**`graphify: command not found` après l'installation**
La CLI est installée mais son répertoire bin n'est pas dans le `PATH` de votre shell. Choisissez la solution selon votre méthode d'installation :
- **uv** (`uv tool install graphifyy`) : la commande atterrit dans le répertoire bin d'outils d'uv (`~/.local/bin`), souvent absent du `PATH` sur une installation macOS/zsh toute fraîche. Lancez `uv tool update-shell`, puis ouvrez un nouveau terminal. (Trouvez le répertoire avec `uv tool dir --bin`.)
- **pipx** (`pipx install graphifyy`) : lancez `pipx ensurepath`, puis ouvrez un nouveau terminal.
- **pip** (`pip install graphifyy`) : pip installe les scripts dans un répertoire bin utilisateur qui peut ne pas être dans le `PATH` — ajoutez `~/Library/Python/3.x/bin` (macOS) ou `~/.local/bin` (Linux) à votre `PATH` dans `~/.zshrc`/`~/.bashrc`, ou lancez simplement `python -m graphify`.

**`uvx graphify …` ou `uv tool run graphify …` échoue à résoudre `graphify`**
Le paquet PyPI est `graphifyy` ; `graphify` n'est que la commande qu'il fournit. `uv tool run` traite le premier mot comme un *nom de paquet*, donc il cherche un paquet appelé `graphify` et rapporte `No solution found … no versions of graphify`. Nommez le paquet explicitement : `uvx --from graphifyy graphify install` (identique à `uv tool run --from graphifyy graphify install`). Ou installez une fois `uv tool install graphifyy` puis appelez `graphify` directement.

**`uv run --with graphifyy python -m graphify` exécute silencieusement une installation plus ancienne**
`uv run` utilise votre Python *système*, donc si une ancienne version de `graphifyy` s'y trouve aussi (par ex. un ancien `pip install graphifyy`), Python peut trouver cette copie en premier dans `sys.path` et `--with graphifyy` ne la remplacera pas. Cela s'exécute sans erreur, mais vous obtenez le comportement de l'*ancienne* version — par ex. des surcharges d'environnement comme `OPENAI_BASE_URL` sont silencieusement ignorées, donc les requêtes atteignent le point de terminaison par défaut et échouent avec un 401 qui ressemble à une mauvaise clé. L'empreinte est une ligne `warning: skill is from graphify <plus récent>, package is <plus ancien>` — cela signifie qu'une installation différente a été chargée, pas seulement une skill obsolète. Vérifiez quelle copie a réellement été chargée :
```bash
python -c "import graphify; print(graphify.__file__)"
```
Puis lancez directement la commande installée (elle utilise la copie gérée par uv), ou supprimez la copie système obsolète :
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` fonctionne mais pas la commande `graphify`**
Le `PATH` de votre shell n'inclut pas le répertoire bin où la commande a été installée. Préférez `uv tool install` / `pipx install` à `pip` seul, puis lancez `uv tool update-shell` / `pipx ensurepath` et ouvrez un nouveau terminal (voir les notes d'installation ci-dessus).

**`/graphify .` provoque « path not recognized » dans PowerShell**
PowerShell traite un `/` de tête comme un séparateur de chemin. Utilisez `graphify .` (sans barre oblique) sur Windows.

**Le graphe a moins de nœuds après `--update` ou une reconstruction**
Si un refactoring a supprimé des fichiers, les anciens nœuds persistent. Passez `--force` (ou définissez `GRAPHIFY_FORCE=1`) pour écraser même quand la reconstruction a moins de nœuds.

**`extract` se termine avec « extraction was incomplete ... refusing to overwrite »**
Quand une passe d'extraction plante ou qu'un parcours ne peut pas lire entièrement le corpus, l'exécution serait plus petite qu'une exécution complète, donc `graphify extract` refuse d'écraser un `graph.json` existant plus grand avec le résultat partiel (ce qui protège votre `graph.json`). Corrigez l'échec sous-jacent et relancez, ou passez `--allow-partial` pour écraser quand même.

**Le graphe a des nœuds en double pour la même entité (doublons fantômes)**
Les doublons fantômes (le même symbole apparaissant deux fois — une fois depuis l'extraction AST avec un emplacement source, une fois depuis l'extraction sémantique sans) sont désormais fusionnés automatiquement au moment de la construction. Si vous voyez cela dans un graphe construit avant la v0.8.33, lancez une réextraction complète pour nettoyer :
```bash
graphify extract . --force
```

**Ollama manque de VRAM / dépassement de la fenêtre de contexte**
La fenêtre de cache KV est dimensionnée automatiquement mais peut être trop grande pour votre GPU. Réduisez-la :
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**Avertissements `LLM returned invalid JSON` / `Unterminated string`**
La réponse JSON du modèle a atteint sa limite de jetons de sortie et a été coupée en plein milieu d'une chaîne. graphify se rétablit automatiquement (il divise le bloc et réextrait les deux moitiés, et un document unique surdimensionné est d'abord tranché aux frontières de titres/paragraphes afin que tout le fichier reste couvert), donc ces avertissements sont bruyants mais ne causent pas de perte de données. Pour réduire ce bruit, augmentez le plafond de sortie ou réduisez la sortie de chaque bloc :
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
Avec une passerelle cloud comme OpenRouter, préférez `--backend openai` (en définissant `OPENAI_BASE_URL`) au shim Ollama — c'est un chemin compatible OpenAI plus propre. Si le modèle a son propre plafond de sortie maximal, réduire `--token-budget` est le levier fiable.

**Le HTML du graphe est trop volumineux pour s'ouvrir dans un navigateur (>5000 nœuds)**
Ignorez la génération HTML et utilisez le JSON directement :
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**`graph.json` a des marqueurs de conflit après que deux développeurs committent en même temps**
Lancez `graphify hook install` — cela configure un driver de fusion git qui fusionne automatiquement `graph.json` (union) afin que les conflits ne se produisent jamais.

**L'extraction renvoie des nœuds/arêtes vides pour les docs ou PDF**
Les docs, PDF et images nécessitent un appel LLM — les corpus uniquement composés de code ne nécessitent aucune clé. Vérifiez que votre clé API est définie et que le backend est correct :
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**Avertissement de version de skill non concordante dans votre IDE**
Votre version installée de graphify diffère du fichier de skill. Mettez à jour :
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**Le cache de prompt de Claude Code est invalidé après chaque `graphify extract`**
Graphify écrit des fichiers de sortie (`graph.json`, `graphify-out/`) dans l'espace de travail. Si ces chemins ne sont pas ignorés, chaque écriture invalide le cache de prompt de Claude Code, forçant un réenvoi complet au tarif d'écriture de cache au tour suivant. Ajoutez-les à `.claudeignore` :
```text
# .claudeignore
graph.json
graphify-out/
```

---

## Référence complète des commandes

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

> **Noms de communautés :** à l'intérieur d'un agent (Claude Code, Gemini CLI), l'agent nomme lui-même les communautés. Quand vous lancez la CLI seule, `cluster-only` les nomme automatiquement avec le backend configuré (intégré ou fournisseur compatible OpenAI personnalisé) — passez `--no-label` pour garder `Community N`, ou lancez `graphify label` pour (re)générer des noms à la demande.

---

## En savoir plus

- [Comment ça marche](../how-it-works.md) — le pipeline d'extraction, la détection de communautés, le score de confiance, les benchmarks
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — répartition des modules, comment ajouter un langage
- [Intégrations optionnelles](../docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — le livre sur les idées derrière graphify, l'architecture de bout en bout

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) est la couche toujours active construite au-dessus de graphify — elle applique la même approche de graphe à l'ensemble de votre contexte de travail : réunions, fichiers, docs et code, avec une mise à jour continue en arrière-plan.

Conçu pour les personnes et les équipes dont le travail s'étend sur des centaines de conversations et de documents qu'elles ne peuvent jamais entièrement reconstituer.

**[Rejoignez la liste d'attente sur graphify.com](https://graphify.com).** Essai gratuit à venir prochainement.

---

<details>
<summary>Contribuer</summary>

### Configuration de l'environnement de développement

Le projet utilise [uv](https://docs.astral.sh/uv/) pour le workflow de développement. Installez-le une fois, puis :

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

Vérifiez l'installation en mode éditable :
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### Exécuter les tests

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> Remarque macOS : la suite de tests inclut à la fois les fixtures `sample.f90` et `sample.F90`. Elles entrent en collision sur les systèmes de fichiers HFS+ / APFS insensibles à la casse. Exécutez sur Linux ou dans un conteneur Docker si vous devez tester les deux variantes Fortran simultanément.

### Flux de travail Git

- Le développement actif se déroule sur la branche `v8`.
- Style de commit : `fix: <description>` / `feat: <description>` / `docs: <description>`
- Avant d'ouvrir une PR, lancez `uv run pytest tests/ -q` et vérifiez que ça passe.
- Ajoutez un fichier de fixture dans `tests/fixtures/` et des tests dans `tests/test_languages.py` pour tout nouvel extracteur de langage.

### Contributions attendues

**Les exemples travaillés** sont la contribution la plus utile. Lancez `/graphify` sur un corpus réel, enregistrez la sortie dans `worked/{slug}/`, écrivez un `review.md` honnête couvrant ce que le graphe a bien et mal saisi, et ouvrez une PR.

**Bugs d'extraction** — ouvrez une issue avec le fichier d'entrée, l'entrée de cache (`graphify-out/cache/`), et ce qui a été manqué ou incorrect.

Voir [ARCHITECTURE.md](../../ARCHITECTURE.md) pour les responsabilités des modules et comment ajouter un langage.

</details>
