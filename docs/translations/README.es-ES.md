<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>Un fork de <a href="https://github.com/Graphify-Labs/graphify">graphify</a> que añade <code>graphify decouple</code></b> — candidatos de Extract Class con puntuación de riesgo, sin LLM, reverificados contra el código fuente real (no solo contra el grafo de llamadas) antes de recomendar nada. Consulta <a href="#decouple-candidatos-a-extract-class-con-puntuación-de-riesgo">Decouple: candidatos a Extract Class con puntuación de riesgo</a> más abajo.
</p>

<div align="center">
<details><summary><b>Lee esto en otros idiomas</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>El acceso anticipado a la plataforma graphify está abierto antes del lanzamiento público de v1: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

Escribe `/graphify` en tu asistente de código con IA y este mapea todo tu proyecto (código, documentación, PDF, imágenes, vídeos) en un **grafo de conocimiento** que puedes **consultar en lugar de bucear con grep** entre archivos.

- **Mapas de código gratis y totalmente locales.** El código se analiza con un AST de tree-sitter: determinista, sin LLM, nada sale de tu máquina. (Los documentos, PDF, imágenes y vídeo usan el modelo de tu asistente, o una clave de API configurada, para una pasada semántica.)
- **Cada arista está explicada.** Cada conexión se etiqueta como `EXTRACTED` (explícita en el código fuente) o `INFERRED` (resuelta por graphify), para que sepas qué se leyó directamente y qué se infirió.
- **No es un índice vectorial.** Sin embeddings, sin almacén vectorial: un grafo real que se recorre. Haz una pregunta, traza el camino entre dos elementos, o explica un concepto.

> ¿Quieres esto siempre activo, actualizándose en segundo plano en tu código, documentación y reuniones en lugar de solo bajo demanda? Eso es lo que estamos construyendo en **[graphify.com](https://graphify.com)**, y el acceso anticipado ya está abierto en **[app.graphify.com](https://app.graphify.com/login)**.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="El graph.html interactivo de graphify mostrando la base de código de FastAPI como un grafo de conocimiento dirigido por fuerzas, con una leyenda de las comunidades detectadas" width="900">
</p>
<p align="center">
  <em>La base de código de FastAPI mapeada por graphify. Cada nodo es un concepto, los colores son comunidades detectadas, y todo es interactivo en graph.html.</em>
</p>

**Empieza** (30 segundos):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

Luego, en tu asistente de IA:

```
/graphify .
```

Eso es todo. Obtienes **tres archivos**:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**Funciona en** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot y 15+ más — [elige tu plataforma](#instalación).

---

## Véalo en acción

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="Consulta de camino en graphify: una terminal pregunta por el camino más corto entre FastAPI y ModelField, y la respuesta se ilumina salto a salto a través del grafo de conocimiento" width="900">
</p>

Una vez construido el grafo, lo consultas en lugar de leer archivos. Salida real, graphify ejecutado sobre la base de código de FastAPI mostrada arriba:

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

Cada arista lleva una **etiqueta de confianza** (`EXTRACTED` = explícita en el código fuente, `INFERRED` = derivada por resolución), para que sepas qué se leyó directamente y qué se infirió. `graphify query "<pregunta>"` devuelve un subgrafo acotado para una pregunta en lenguaje natural, y `graphify path A B` traza cómo se conectan dos elementos cualesquiera.

---

## Decouple: candidatos a Extract Class con puntuación de riesgo

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: el nodo dios MainWindow dividiéndose en clases candidatas con puntuación de riesgo, con una advertencia de estado compartido entre dos de ellas" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: las 5 clases propuestas de MainWindow, con el panel Node Info abierto en Main Window Axis and Range Controls mostrando una superposición de estado de 0.608 con Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>DECOUPLE.html en una ejecución real — al hacer clic en una clase propuesta se muestra exactamente con qué otra clase comparte estado, y qué se comparte específicamente.</em>
</p>

La misma página también renderiza la división en sí. Alternar **Preview decoupled view** cambia los métodos propios de la god class por las clases propuestas y reencamina las aristas en el sitio: el cambio de cableado, no un diagrama redibujado:

| Antes — la god class hoy | Después — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html antes del cambio: un único nodo central MainWindow con sus propios métodos desplegados a su alrededor" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html después del cambio: el mismo nodo reducido a 5 clases propuestas con forma de rombo, aristas verdes discontinuas que muestran qué métodos se extrajeron a cada una, y aristas rojas que muestran el estado de instancia compartido entre dos de ellas" width="440"> |
| Un nodo que contiene 47 de sus propios métodos, cada uno accesible solo a través de la clase. | Las clases propuestas. Verde discontinuo = lo que se extrajo a cada una; rojo = el estado de instancia que dos de ellas siguen compartiendo, que es exactamente lo que decide entre `split` y `keep_as_is`. Solo se dibujan los candidatos que superan el umbral de riesgo: aquí 5 de 6, por eso un método se queda sin rombo donde aterrizar. |

`graphify decouple` encuentra objetos dios y te dice si dividirlos merece realmente la pena, no solo que son grandes.

El caso de fallo que esto existe para detectar: una clase con 47 métodos que el clustering basado en el grafo de llamadas divide alegremente en 5 grupos de aspecto ordenado, todos los cuales siguen leyendo y escribiendo el mismo estado de instancia `self._chart_style` / `self._crosshair` por debajo. Si publicas esa división no has desacoplado nada: has movido métodos a archivos nuevos que siguen sin poder probarse, cambiarse o razonarse de forma independiente, porque todos siguen necesitando que se les pase de vuelta el mismo estado compartido. Una herramienta que solo mira el grafo de llamadas no puede ver esto en absoluto; tiene que volver al código fuente real.

**Dos comprobaciones, ambas sin LLM, ambas deterministas:**

1. **¿Es esto siquiera un objeto dios?** Un nodo con un grado alto puede ser un verdadero objeto dios (muchos métodos PROPIOS, repartidos entre responsabilidades no relacionadas — aquí aplica Extract Class) o un hub/modelo de datos sobrerreferenciado (pocos métodos propios, mayormente referencias *entrantes* — dividir su cuerpo no sirve de nada; el arreglo es reducir su interfaz, no extraer una clase). `classify_god_node` distingue esto por `member_ratio`, no por el grado en bruto — la diferencia que evita que `TraceSource` (84 aristas, pero solo 6 métodos propios) reciba una sugerencia de división falsa que `MainWindow` (88 aristas, 47 métodos propios) sí recibe correctamente.
2. **¿La división reduciría realmente el acoplamiento?** `risk_before` (el tamaño/acoplamiento/fragmentación actual del nodo dios) se compara con `risk_after` — el NUEVO riesgo que la propia división introduciría: llamadas entre grupos que eran aristas intraclase invisibles y pasan a ser dependencias interclase explícitas, llamadores que ahora necesitarían depender de más de una clase nueva y —la comprobación que un grafo de llamadas no puede hacer estructuralmente— cuánto estado de instancia `self`/`this` (lecturas, escrituras y llamadas a métodos auxiliares compartidos, ponderadas por separado: una **escritura** compartida puntúa más alto que una lectura compartida) tienen en común realmente los grupos propuestos. Esto vuelve a analizar directamente con tree-sitter el propio archivo fuente del nodo dios; no depende del grafo ya extraído por graphify, que nunca registra el acceso a nivel de campo para ningún lenguaje. Solo cuando `risk_after` supera un umbral por debajo de `risk_before` el plan recomienda `split`; en caso contrario es `marginal` o `keep_as_is`, y un candidato desaconsejado se reporta como un número, nunca se dibuja como una forma que tengas que cuestionar a ojo.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

Genera tres archivos junto a `graph.json`:

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

**Cobertura de lenguajes para la comprobación de estado compartido** (la clasificación basada solo en el grafo de llamadas descrita arriba funciona para todos los lenguajes que graphify extrae; esta tabla es específicamente el reanálisis del código fuente que verifica la superposición de estado `self`/`this`):

| Language | Supported | Notes |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` es su propio nodo de AST, no un acceso a campo envuelto — se gestiona explícitamente |
| C# | ✅ | |
| Rust | ✅ | `self.x` a través de bloques `impl` |
| Ruby | ✅ | `@x` (el modismo dominante) + llamadas `self.foo` |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | resolución del receptor por método — Go no tiene palabra clave `self`/`this`, así que el nombre del receptor (`f` en `func (f *Foo) M()`) se resuelve de nuevo para cada método |
| C | ❌ | un parámetro de puntero a struct no tiene ningún marcador sintáctico que lo distinga de cualquier otro parámetro — no hay una señal fiable sin inferencia de tipos completa |

Un nodo dios en un lenguaje no compatible, o cuyo código fuente no se puede leer, se marca como `state_analysis: "skipped"` — la clasificación y la puntuación basada en el grafo de llamadas se siguen ejecutando, pero la recomendación se apoya únicamente en el grafo de llamadas en lugar de asumir en silencio que la comprobación de estado pasó.

---

## Qué hace

Lo que obtienes de fábrica:

| Capability | What you get |
|---|---|
| **Nodos dios** | Los conceptos más conectados, para que veas por dónde fluye todo |
| **Comunidades** | El grafo dividido en subsistemas (Leiden), con etiquetas sin LLM |
| **Enlaces entre archivos** | `calls` / `imports` / `inherits` / `mixes_in` resueltos en ~40 lenguajes mediante AST de tree-sitter |
| **Consulta, camino, explicación** | Haz una pregunta, traza el camino entre dos elementos, o explica un concepto, todo contra `graph.json` |
| **Justificación + referencias a documentación** | Los comentarios `# NOTE:` / `# WHY:` y las citas de ADR/RFC se convierten en nodos de primera clase vinculados al código |
| **Más allá del código** | Documentos, PDF, imágenes y vídeo/audio se mapean todos en el mismo grafo |
| **Local por defecto** | El código se analiza localmente con tree-sitter (sin LLM, nada sale de tu máquina); solo la pasada semántica sobre documentos/medios llama a un backend, y solo si configuras uno |

---

## Benchmarks

| Benchmark | Metric | graphify | Field |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | QA accuracy | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | QA accuracy | **76%** | empatado con dense RAG |
| Graph build | LLM credits | **0** | por token en la mayoría de sistemas |

Todos los sistemas se ejecutaron con el mismo arnés de pruebas, el mismo modelo y los mismos presupuestos, puntuados por un juez validado a ciegas contra un segundo juez (90,6% de acuerdo, kappa de Cohen 0,81). Tablas completas por sistema, el resultado de inteligencia de código y los comandos de reproducción: **[BENCHMARKS.md](../../BENCHMARKS.md)**.

---

## Requisitos previos

| Requirement | Minimum | Check | Install |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(recomendado)* | any | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(alternativa)* | any | `pipx --version` | `pip install pipx` |

**Instalación rápida en macOS (Homebrew):**
```bash
brew install python@3.12 uv
```

**Instalación rápida en Windows:**
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

## Instalación

> **Paquete oficial:** el paquete de PyPI es `graphifyy` (con doble «y»). Otros paquetes `graphify*` en PyPI no están afiliados. El comando de la CLI sigue siendo `graphify`.

**Paso 1 — instala el paquete:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**Paso 2 — registra la skill con tu asistente de IA:**

```bash
graphify install
```

Eso es todo. Abre tu asistente de IA y escribe `/graphify .`

Para instalar la skill del asistente en el repositorio actual en lugar de en tu
perfil de usuario, añade `--project`:

```bash
graphify install --project
graphify install --project --platform codex
```

Las instalaciones con ámbito de proyecto escriben dentro del directorio actual, por ejemplo
en `.claude/skills/graphify/SKILL.md` o `.agents/skills/graphify/SKILL.md` (más un
directorio auxiliar `references/` que la skill carga bajo demanda), y
muestran una pista de `git add` para los archivos que se pueden confirmar (commit).
Los comandos específicos de cada plataforma que admiten instalaciones con ámbito de proyecto aceptan el mismo flag,
por ejemplo `graphify claude install --project` o `graphify codex install --project`.

> **Nota para PowerShell:** usa `graphify .`, no `/graphify .` — la barra inicial es un separador de rutas en PowerShell.

> **¿`graphify: command not found`?** `uv tool install` / `pipx install` colocan el comando `graphify` en el directorio bin de sus herramientas (`~/.local/bin`). Si tu shell no lo encuentra justo después de instalar —algo habitual en una instalación nueva de macOS + zsh—, ese directorio aún no está en tu `PATH`: ejecuta `uv tool update-shell` (o `pipx ensurepath`) y abre una terminal nueva. Con `pip` normal, añade `~/.local/bin` (Linux) o `~/Library/Python/3.x/bin` (Mac) a tu PATH, o ejecuta `python -m graphify`.

> **¿Ejecutas con `uvx` / `uv tool run` en lugar de instalar?** Indica el paquete, no el comando: `uvx --from graphifyy graphify install`. El simple `uvx graphify …` falla (`No solution found … no versions of graphify`) porque `uv tool run` lee la primera palabra como un *paquete*, y el paquete es `graphifyy` — el comando `graphify` vive dentro de él.

> **Evita `pip install` en Mac/Windows** si es posible. La skill resuelve Python en tiempo de ejecución desde `graphify-out/.graphify_python`; si eso apunta a un entorno distinto de aquel donde `pip` instaló el paquete, obtendrás `ModuleNotFoundError: No module named 'graphify'`. `uv tool install` y `pipx install` aíslan el paquete en su propio entorno y evitan esto por completo.

> **Git hooks y uv tool / pipx:** `graphify hook install` incrusta la ruta del intérprete actual directamente en los scripts del hook en el momento de la instalación, para que el hook post-commit se dispare correctamente incluso en clientes git de escritorio y en ejecutores de CI donde `~/.local/bin` no está en el PATH. Si reinstalas o actualizas graphify, vuelve a ejecutar `graphify hook install` para refrescar la ruta incrustada.

> **Modo estricto (Claude Code):** `graphify install --project --strict` hace que el asistente realmente use el grafo. La instalación por defecto lo *empuja* a ejecutar `graphify query` antes de leer archivos; el modo estricto *bloquea* la primera lectura en bruto del código fuente en una sesión y la redirige al grafo, y luego vuelve al empujón suave (así se dispara como mucho una vez por sesión y nunca se queda bloqueado). Actívalo o desactívalo en tiempo de ejecución con `GRAPHIFY_HOOK_STRICT=1`/`0`; la instalación por defecto no cambia (empujón suave).

<details>
<summary><b>Elige tu plataforma</b> (20+ asistentes, haz clic para expandir)</summary>

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

Los usuarios de Codex también necesitan `multi_agent = true` bajo `[features]` en `~/.codex/config.toml` para la extracción en paralelo. CodeBuddy usa el mismo mecanismo de herramienta Agent y hook PreToolUse que Claude Code. Factory Droid usa la herramienta `Task` para el despacho de subagentes en paralelo. OpenClaw y Aider usan extracción secuencial (el soporte de agentes en paralelo aún es incipiente en esas plataformas). Trae usa la herramienta Agent para el despacho de subagentes en paralelo y **no** admite hooks `PreToolUse`, así que AGENTS.md es el mecanismo siempre activo.

`--platform agents` (alias `--platform skills`) apunta a las ubicaciones genéricas multi-framework de [Agent-Skills](https://github.com/anthropics/skills): la ubicación global de usuario de la especificación `~/.agents/skills/` (leída por `npx skills` y frameworks compatibles con la especificación) para una instalación global, y `./.agents/skills/` para una instalación de proyecto (`--project`). El simple `graphify install` se mantiene de una sola plataforma (Claude Code) a propósito — usa la plataforma con nombre `agents` cuando quieras que la skill sea descubrible por cualquier framework que lea `.agents/skills`.

> Codex usa `$graphify` en lugar de `/graphify`.

</details>

<details>
<summary><b>Extras opcionales</b> (instala solo lo que necesites)</summary>

| Extra | What it adds | Install |
|---|---|---|
| `pdf` | Extracción de PDF | `uv tool install "graphifyy[pdf]"` |
| `office` | Soporte de `.docx` y `.xlsx` | `uv tool install "graphifyy[office]"` |
| `google` | Renderizado de Google Sheets | `uv tool install "graphifyy[google]"` |
| `video` | Transcripción de vídeo/audio (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | Servidor MCP stdio | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Soporte de envío a Neo4j | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | Soporte de envío a FalkorDB | `uv tool install "graphifyy[falkordb]"` |
| `svg` | Exportación de grafo en SVG | `uv tool install "graphifyy[svg]"` |
| `leiden` | Detección de comunidades Leiden (solo Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Inferencia local con Ollama | `uv tool install "graphifyy[ollama]"` |
| `openai` | APIs de OpenAI o compatibles con OpenAI | `uv tool install "graphifyy[openai]"` |
| `gemini` | API de Google Gemini | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | API de Anthropic Claude (`--backend claude`, usa `ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (usa IAM, sin clave de API) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, usa `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "graphifyy[openai]"` |
| `sql` | Extracción de esquemas SQL | `uv tool install "graphifyy[sql]"` |
| `postgres` | Introspección en vivo de PostgreSQL (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | Extracción de AST de BYOND DreamMaker `.dm`/`.dme` (puede necesitar un compilador de C + `python3-dev` si no hay una wheel para tu plataforma) | `uv tool install "graphifyy[dm]"` |
| `terraform` | Extracción de AST de Terraform / HCL `.tf`/`.tfvars`/`.hcl` | `uv tool install "graphifyy[terraform]"` |
| `pascal` | Extracción de AST de Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` (aristas `calls`/`inherits` más precisas; si no está presente, recurre a un extractor basado en regex) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | Segmentación de consultas en chino (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | Todo lo anterior | `uv tool install "graphifyy[all]"` |

</details>

---

## Haz que tu asistente use siempre el grafo

Ejecuta esto una vez en tu proyecto después de construir un grafo:

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

Esto escribe un pequeño archivo de configuración que le dice a tu asistente que consulte el grafo de conocimiento para preguntas sobre la base de código, prefiriendo consultas acotadas como `graphify query "<pregunta>"` antes que leer el informe completo o hacer grep sobre los archivos en bruto.

- **Plataformas con hooks** (Claude Code, Gemini CLI): un hook se dispara automáticamente antes de las llamadas a herramientas de tipo búsqueda (y, en Claude Code, antes de leer archivos fuente uno a uno mediante las herramientas Read/Glob) y empuja a tu asistente hacia el camino del grafo.
- **Plataformas con archivos de instrucciones** (Codex, OpenCode, Cursor, etc.): archivos de instrucciones persistentes (`AGENTS.md`, `.cursor/rules/`, etc.) proporcionan la misma guía de «consulta primero».

`GRAPH_REPORT.md` sigue disponible para una revisión arquitectónica amplia.

**CodeBuddy** hace las mismas dos cosas que Claude Code: escribe una sección en `CODEBUDDY.md` diciéndole a CodeBuddy que lea `graphify-out/GRAPH_REPORT.md` antes de responder preguntas de arquitectura, e instala hooks `PreToolUse` (`.codebuddy/settings.json`) que se disparan antes de comandos de búsqueda de Bash y lecturas de archivos, empujando hacia `graphify query` en su lugar.

**Codex** escribe en `AGENTS.md`, que es lo que realmente lleva la guía del grafo siempre activo en esta plataforma. `graphify codex install` también registra un hook `PreToolUse` en `.codex/hooks.json` (`graphify hook-check`), pero esa entrada es deliberadamente un **no-op**: Codex Desktop rechaza `hookSpecificOutput.additionalContext` en `PreToolUse`, así que emitir un empujón ahí rompería las llamadas a la herramienta Bash. A diferencia de Claude Code, donde el hook (`graphify hook-guard`) es el que empuja, en Codex el hook se dispara y deliberadamente no hace nada, y `AGENTS.md` es el mecanismo siempre activo.

**Kilo Code** instala la skill de Graphify en `~/.config/kilo/skills/graphify/SKILL.md` y un comando nativo `/graphify` en `~/.config/kilo/command/graphify.md`. `graphify kilo install` también escribe `AGENTS.md` más un plugin nativo `tool.execute.before` (`.kilo/plugins/graphify.js` + registro en `.kilo/kilo.json` o `.kilo/kilo.jsonc`) para que Kilo tenga el mismo comportamiento de recordatorio del grafo siempre activo a través de la configuración nativa de `.kilo`.

**Cursor** escribe `.cursor/rules/graphify.mdc` con `alwaysApply: true`, así que Cursor lo incluye automáticamente en cada conversación, sin necesidad de hook.

Para eliminar graphify de todas las plataformas de una vez: `graphify uninstall` (añade `--purge` para borrar también `graphify-out/`). O usa el comando específico de cada plataforma (por ejemplo, `graphify claude uninstall`).

---

## Qué contiene el informe

- **Nodos dios** — los conceptos más conectados de tu proyecto. Todo fluye a través de estos.
- **Conexiones sorprendentes** — enlaces entre elementos que viven en archivos o módulos distintos. Ordenados por lo inesperados que son.
- **El «por qué»** — los comentarios en línea (`# NOTE:`, `# WHY:`, `# HACK:`), los docstrings y la justificación de diseño de la documentación se extraen como nodos independientes vinculados al código que explican.
- **Preguntas sugeridas** — 4–5 preguntas que el grafo está en una posición única para responder.
- **Etiquetas de confianza** — cada relación inferida se marca como `EXTRACTED`, `INFERRED` o `AMBIGUOUS`. Siempre sabes qué se encontró frente a qué se adivinó.

---

## Qué archivos admite

| Type | Extensions |
|------|-----------|
| Código (36 gramáticas de tree-sitter) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme` requiere `uv tool install graphifyy[dm]`; `.mts`/`.cts` reutilizan la gramática de TypeScript, `.cc`/`.cxx` y CUDA `.cu`/`.cuh` y Metal `.metal` reutilizan la gramática de C++) |
| Salesforce Apex | `.cls .trigger` (basado en regex; clases, interfaces, enums, métodos, triggers, aristas SOQL/DML) |
| Terraform / HCL | `.tf .tfvars .hcl` (requiere `uv tool install graphifyy[terraform]`) |
| Configuraciones MCP | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — extrae nodos de servidor, referencias de paquetes, requisitos de variables de entorno |
| Manifiestos de paquetes | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — un nodo de paquete canónico por paquete (por nombre) más aristas `depends_on`, de modo que un paquete referenciado desde muchos manifiestos es un único hub |
| Documentación | `.md .mdx .qmd .html .txt .rst .yaml .yml` (los enlaces markdown `[text](./other.md)` y los `[[wikilinks]]` se convierten en aristas `references` entre documentos) |
| Office | `.docx .xlsx` (requiere `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (opcional; requiere autenticación `gws` y `--google-workspace`; Sheets necesita `uv tool install graphifyy[google]`) |
| PDFs | `.pdf` |
| Imágenes | `.png .jpg .webp .gif` |
| Vídeo / Audio | `.mp4 .mov .mp3 .wav` y más (requiere `uv tool install graphifyy[video]`) |
| YouTube / URLs | cualquier URL de vídeo (requiere `uv tool install graphifyy[video]`) |

El código se extrae **localmente sin llamadas a API** (AST mediante tree-sitter). Todo lo demás pasa por la API del modelo de tu asistente de IA.

Los archivos `.gdoc`, `.gsheet` y `.gslides` de Google Drive para escritorio son
punteros de acceso directo, no el contenido del documento. Para incluir Google Docs,
Sheets y Slides nativos en una extracción headless, instala y autentica la
[CLI `gws`](https://github.com/googleworkspace/cli), y luego ejecuta:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

También puedes definir `GRAPHIFY_GOOGLE_WORKSPACE=1`. Graphify exporta los accesos directos a
`graphify-out/converted/` como archivos Markdown auxiliares, y luego extrae esos archivos.

---

## Comandos habituales

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

Consulta [Decouple: candidatos a Extract Class con puntuación de riesgo](#decouple-candidatos-a-extract-class-con-puntuación-de-riesgo) más arriba, o la [referencia completa de comandos](#referencia-completa-de-comandos) más abajo.

---

## Ignorar archivos

Crea un `.graphifyignore` en la raíz de tu proyecto — misma sintaxis que `.gitignore`, incluida la negación con `!`.

**`.gitignore` se respeta automáticamente.** graphify lee el `.gitignore` de cada directorio. Si también hay un `.graphifyignore` presente, ambos se **combinan** — los patrones de `.graphifyignore` se evalúan al final, así que ganan en caso de conflicto (incluidas las negaciones con `!`). Añadir un `.graphifyignore` solo puede excluir más; nunca vuelve a incluir un archivo que tu `.gitignore` ya excluía. El alcance por subdirectorio funciona igual que en git — un archivo de exclusión solo afecta a su propio subárbol.

Pasa `--no-gitignore` a `graphify extract` cuando el código generado o transpilado ignorado por git deba estar en el grafo. Esto desactiva `.gitignore` y `.git/info/exclude`; `.graphifyignore` se sigue aplicando.

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

## Configuración en equipo

`graphify-out/` está pensado para confirmarse (commit) en git, de modo que todo el equipo empiece con un mapa.

**Adiciones recomendadas a `.gitignore`:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` ahora es portable — las claves se almacenan como rutas relativas y se reanclan al cargar, así que confirmarlo es seguro y evita una reconstrucción completa en el primer checkout.

**Flujo de trabajo:**
1. Una persona ejecuta `/graphify .` y confirma `graphify-out/`.
2. Todos los demás hacen pull — su asistente lee el grafo inmediatamente.
3. Ejecuta `graphify hook install` para reconstruir automáticamente después de cada commit (solo AST, sin coste de API). Esto también configura un driver de fusión de git para que `graph.json` nunca se quede con marcadores de conflicto — dos desarrolladores que confirman en paralelo obtienen sus grafos fusionados automáticamente por unión.
4. Cuando cambien la documentación o los papers, ejecuta `/graphify --update` para refrescar esos nodos.

---

## Usar el grafo directamente

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

El servidor MCP le da a tu asistente acceso estructurado: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Servidor HTTP compartido

`--transport stdio` (el valor por defecto) lanza un servidor local por desarrollador. `--transport http` sirve las mismas herramientas sobre el transporte MCP Streamable HTTP, de modo que un único proceso compartido puede servir el grafo para todo el equipo — los clientes apuntan la configuración MCP de su IDE a `http://<host>:8080/mcp` en lugar de ejecutar graphify localmente.

| Flag | Default | Purpose |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Transporte en el que servir |
| `--host` | `127.0.0.1` | Host de enlace HTTP (usa `0.0.0.0` para exponer más allá de localhost) |
| `--port` | `8080` | Puerto de enlace HTTP |
| `--api-key` | env `GRAPHIFY_API_KEY` | Requiere `Authorization: Bearer <key>` (o `X-API-Key`) |
| `--path` | `/mcp` | Ruta de montaje HTTP |
| `--json-response` | off | Devuelve JSON plano en lugar de streams SSE |
| `--stateless` | off | Sin estado por sesión (para despliegues con balanceo de carga / CI) |
| `--session-timeout` | `3600` | Elimina las sesiones con estado inactivas tras N segundos (`0` lo desactiva) |

El enlace por defecto `127.0.0.1` es solo loopback. Define `--host 0.0.0.0` **y** `--api-key` juntos al exponerlo en un host compartido. Ejecútalo en un contenedor:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **Nota WSL / Linux:** Ubuntu incluye `python3`, no `python`. Usa un venv para evitar conflictos:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## Variables de entorno

Estas solo son necesarias para la **extracción headless / de CI** (`graphify extract`). Al ejecutarse a través de la skill `/graphify` dentro de tu IDE, la API del modelo la proporciona tu sesión del IDE — no se necesitan claves adicionales.

| Variable | Used for | When required |
|---|---|---|
| `ANTHROPIC_API_KEY` | Backend de Claude (Anthropic) | `--backend claude` |
| `ANTHROPIC_BASE_URL` | URL de endpoint compatible con Anthropic (proxy LiteLLM, gateways, ...) | `--backend claude` (por defecto: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Nombre del modelo para el backend de Claude — para endpoints personalizados, usa el nombre/alias de modelo que exponga tu servidor | `--backend claude` (por defecto: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` or `GOOGLE_API_KEY` | Backend de Google Gemini | `--backend gemini` |
| `OPENAI_API_KEY` | APIs de OpenAI o compatibles con OpenAI | `--backend openai` (los servidores locales aceptan cualquier valor no vacío) |
| `OPENAI_BASE_URL` | URL de servidor compatible con OpenAI (llama.cpp, vLLM, LM Studio, ...) | `--backend openai` (por defecto: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | Nombre del modelo para el backend de OpenAI — para servidores autoalojados, usa el nombre/alias de modelo que exponga tu servidor (comprueba su endpoint `/v1/models`), p. ej. `LFM2.5-8B-A1B-UD-Q4_K_XL` para llama.cpp | `--backend openai` (por defecto: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | Backend de DeepSeek | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Backend de Kimi Code | `--backend kimi` |
| `OLLAMA_BASE_URL` | URL de inferencia local de Ollama | `--backend ollama` (por defecto: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Nombre del modelo de Ollama | `--backend ollama` (por defecto: autodetección) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Anula el tamaño de la ventana de caché KV de Ollama | opcional — dimensionado automáticamente por defecto |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Minutos que se mantiene cargado el modelo de Ollama | opcional — define `0` para descargarlo después de cada fragmento |
| `AZURE_OPENAI_API_KEY` | Backend de Azure OpenAI Service | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | URL del endpoint del recurso de Azure | `--backend azure` (obligatorio junto con la clave de API) |
| `AZURE_OPENAI_API_VERSION` | Anulación de la versión de la API de Azure | opcional — por defecto `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` or `GRAPHIFY_AZURE_MODEL` | Nombre del despliegue de Azure | opcional — por defecto `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — cadena de credenciales estándar | `--backend bedrock` (sin clave de API, usa IAM) |
| `GRAPHIFY_MAX_WORKERS` | Número de hilos para el paralelismo del AST | opcional — también el flag `--max-workers` |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Eleva el límite de salida para corpus densos | opcional — p. ej. `32768` para archivos grandes |
| `GRAPHIFY_API_TIMEOUT` | Tiempo de espera por llamada en segundos para los backends HTTP, claude-cli, Anthropic SDK y Bedrock (por defecto: 600) | opcional — también el flag `--api-timeout` |
| `GRAPHIFY_MAX_RETRIES` | Cuántas veces reintentar una solicitud limitada por tasa (429) antes de desistir (por defecto: 6; respeta `Retry-After`) | opcional — auméntalo para límites estrictos por organización (p. ej. kimi); `0` lo desactiva |
| `GRAPHIFY_FORCE` | Fuerza la reconstrucción del grafo incluso con menos nodos | opcional — también el flag `--force` |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Activa automáticamente la exportación de Google Workspace | opcional — define en `1` |
| `GRAPHIFY_TRIAGE_BACKEND` | Backend para `graphify prs --triage` | opcional — autodetectado a partir de las claves disponibles |
| `GRAPHIFY_TRIAGE_MODEL` | Anulación del modelo para el triaje | opcional — p. ej. `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | Define en `1` para activar el registro local de consultas en `~/.cache/graphify-queries.log` (registra cada pregunta de query/path/explain + la ruta del corpus). Desactivado por defecto — no se escribe nada a menos que lo actives (#1797) | opcional |
| `GRAPHIFY_QUERY_LOG` | Activa el registro de consultas y lo escribe en esta ruta en lugar de la predeterminada | opcional — desactivado a menos que se defina esta o `_ENABLE` |
| `GRAPHIFY_QUERY_LOG_DISABLE` | Define en `1` para forzar la desactivación del registro de consultas (prevalece sobre las variables de activación) | opcional |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | Cuando el registro está activado, también graba las respuestas completas del subgrafo (desactivado por defecto) | opcional |
| `GRAPHIFY_MAX_GRAPH_BYTES` | Anula el límite de tamaño de 512 MiB de graph.json — p. ej. `700MB`, `2GB`, o bytes simples | opcional — útil para corpus muy grandes |
| `GRAPHIFY_MAX_CONTEXTS` | Número máximo de grafos de proyecto no predeterminados que retiene un servidor MCP multiproyecto | opcional — por defecto: `8`; los valores inválidos usan `8`, y los valores por debajo de `1` usan `1` |
| `GRAPHIFY_LLM_TEMPERATURE` | Anula la temperatura del LLM para la extracción semántica — p. ej. `0.7`, o `none` para omitirla | opcional — se omite automáticamente para modelos de razonamiento o1/o3/o4/gpt-5 |

---

## Privacidad

- **Archivos de código** — se procesan localmente mediante tree-sitter. Nada sale de tu máquina. Un corpus solo de código no requiere ninguna clave de API — `graphify extract` se ejecuta completamente sin conexión. En un repositorio mixto, añade `--code-only` para indexar solo el código y omitir la documentación/PDF/imágenes que de otro modo necesitarían un LLM.
- **Vídeo / audio** — se transcribe localmente con faster-whisper. Nada sale de tu máquina.
- **Documentos, PDF, imágenes** — se envían a tu asistente de IA para extracción semántica (a través de la skill `/graphify`, usando el modelo que ejecute tu sesión del IDE). `graphify extract` en modo headless requiere `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), una instancia de Ollama en ejecución (`OLLAMA_BASE_URL`), credenciales de AWS a través de la cadena de proveedores estándar (Bedrock — no necesita clave de API, usa IAM), o el binario de la CLI `claude` (Claude Code — no necesita clave de API, usa tu suscripción de Claude). El flag `--dedup-llm` usa la misma clave.
- **Residencia de datos** — `graphify extract` detecta automáticamente qué proveedor usar según qué clave de API esté definida (prioridad: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). Para código con requisitos de residencia de datos, usa `--backend ollama` (totalmente local) o pasa un flag `--backend` explícito. Kimi (`MOONSHOT_API_KEY`) enruta a servidores de Moonshot AI en China.
- **Sin telemetría**, sin seguimiento de uso, sin analítica.
- **Registro de consultas** — cada llamada a `graphify query`, `graphify path`, `graphify explain` y a `query_graph` de MCP se registra en `~/.cache/graphify-queries.log` en formato JSON Lines (marca de tiempo, pregunta, corpus, nodos devueltos, duración). Las respuestas completas del subgrafo **no** se almacenan por defecto. Define `GRAPHIFY_QUERY_LOG_DISABLE=1` para excluirte, o `GRAPHIFY_QUERY_LOG=/dev/null` para silenciarlo sin desactivar la ruta de código.

---

## Limitaciones y alcance

Lo que graphify deliberadamente **no** hace, y dónde termina su cobertura:

- **No es un motor de búsqueda semántica/vectorial.** El grafo es estructural — nodos y aristas tipadas resueltas a partir del código fuente, no embeddings. `graphify query`/`path`/`explain` recorren esa estructura; no pueden mostrar una conexión que no esté representada como una arista, aunque esté relacionada "semánticamente". No existe ningún mecanismo de respaldo por similitud/vecino más cercano.
- **Los documentos, PDF, imágenes y la extracción headless de vídeo/URL no son solo locales.** Solo el código (AST de tree-sitter) y la transcripción de audio/vídeo (faster-whisper) se ejecutan completamente sin conexión. Extraer documentos/PDF/imágenes siempre llama a un LLM — el modelo de tu asistente de IA a través de la skill `/graphify`, o una clave de API de backend configurada para `graphify extract` en modo headless. Consulta [Privacidad](#privacidad) más arriba para saber exactamente qué flag o clave necesita cada ruta.
- **La comprobación de estado compartido de decouple no cubre todos los lenguajes.** C no tiene una señal fiable de `self`/`this` sin inferencia de tipos completa, por lo que queda excluido (consulta la [tabla de cobertura de lenguajes](#decouple-candidatos-a-extract-class-con-puntuación-de-riesgo) más arriba). Un nodo dios en un lenguaje no soportado, o cuyo código fuente no se pueda leer, recae en una puntuación basada solo en el grafo de llamadas (`state_analysis: "skipped"`) en lugar de una comprobación de estado verificada.
- **El suelo de flujo de datos 3D es una heurística de nombres, no un análisis de dataflow/taint.** La detección de límites de E/S de `data_floor` (parsers, loaders, readers, writers, clientes de BD/HTTP) se basa en convenciones de nombres (`boundary_reason`); un nodo límite con un nombre poco convencional puede pasarse por alto, subestimando cuán profundo está realmente el resto del grafo.
- **Las etiquetas de confianza son la propia confianza de resolución de graphify, no una verdad absoluta.** Las aristas `INFERRED` y `AMBIGUOUS` son resoluciones hechas con el mejor esfuerzo y aun así pueden ser incorrectas, especialmente en modismos muy dinámicos (reflexión, despacho en tiempo de ejecución, metaprogramación) que ningún análisis estático de AST puede resolver por completo.
- **La visualización HTML y el tamaño del grafo tienen ambos un techo.** `graph.html` / `DECOUPLE.html` omiten su generación por defecto por encima de 5000 nodos (`MAX_NODES_FOR_VIZ`, ajustable mediante `GRAPHIFY_VIZ_NODE_LIMIT`); `graph.json` en sí está limitado a 512 MiB (`GRAPHIFY_MAX_GRAPH_BYTES` para anularlo). Usa `--no-viz` junto con `query`/`path`/`explain` para corpus que superen cualquiera de los dos límites.
- **La conciencia entre proyectos es opcional, no automática.** `graphify query` solo ve el único grafo al que apuntas. Las preguntas multi-repositorio requieren registrar explícitamente cada proyecto en el grafo compartido primero (`graphify global add`, limitado a `GRAPHIFY_MAX_CONTEXTS` contextos no predeterminados por servidor MCP) — graphify nunca escanea tu máquina en busca de otros repositorios por su cuenta.
- **La extracción paralela multiagente depende de la plataforma.** Necesita soporte por parte del asistente para lanzar subagentes (`multi_agent = true` en `~/.codex/config.toml` para Codex, la herramienta Agent/Task en Claude Code/CodeBuddy/Factory Droid/Trae). OpenClaw y Aider actualmente solo extraen de forma secuencial.
- **El servidor MCP HTTP compartido se vincula solo a loopback por defecto.** Alcanzarlo desde otra máquina requiere un `--host 0.0.0.0` **y** un `--api-key` explícitos; graphify no gestiona TLS ni ninguna autenticación más allá de ese único token bearer.
- **PowerShell interpreta una `/` inicial como separador de ruta.** Por eso `/graphify .` falla en Windows PowerShell, no es un fallo de graphify — usa `graphify .` en su lugar.

---

## Solución de problemas

**`graphify: command not found` después de instalar**
La CLI está instalada, pero su directorio bin no está en el `PATH` de tu shell. Elige el arreglo según cómo instalaste:
- **uv** (`uv tool install graphifyy`): el comando termina en el directorio bin de herramientas de uv (`~/.local/bin`), que una instalación nueva de macOS/zsh a menudo no tiene en `PATH`. Ejecuta `uv tool update-shell` y abre una terminal nueva. (Encuentra el directorio con `uv tool dir --bin`.)
- **pipx** (`pipx install graphifyy`): ejecuta `pipx ensurepath` y abre una terminal nueva.
- **pip** (`pip install graphifyy`): pip instala los scripts en un directorio bin de usuario que puede no estar en `PATH` — añade `~/Library/Python/3.x/bin` (macOS) o `~/.local/bin` (Linux) a tu `PATH` en `~/.zshrc`/`~/.bashrc`, o simplemente ejecuta `python -m graphify`.

**`uvx graphify …` o `uv tool run graphify …` no logra resolver `graphify`**
El paquete de PyPI es `graphifyy`; `graphify` es solo el comando que este proporciona. `uv tool run` trata la primera palabra como un *nombre de paquete*, así que busca un paquete llamado `graphify` e informa `No solution found … no versions of graphify`. Indica el paquete explícitamente: `uvx --from graphifyy graphify install` (igual que `uv tool run --from graphifyy graphify install`). O ejecuta `uv tool install graphifyy` una vez y luego llama a `graphify` directamente.

**`uv run --with graphifyy python -m graphify` ejecuta en silencio una instalación más antigua**
`uv run` usa tu Python del *sistema*, así que si otra `graphifyy` más antigua también vive ahí (p. ej. un `pip install graphifyy` anterior), Python puede encontrar esa copia primero en `sys.path` y `--with graphifyy` no la anulará. Se ejecuta sin error, pero obtienes el comportamiento de la versión *antigua* — p. ej. las anulaciones de entorno como `OPENAI_BASE_URL` se ignoran en silencio, así que las solicitudes llegan al endpoint por defecto y fallan con un 401 que parece una clave incorrecta. La huella distintiva es una línea `warning: skill is from graphify <newer>, package is <older>` — eso significa que se cargó una instalación distinta, no solo una skill desactualizada. Comprueba qué copia se cargó realmente:
```bash
python -c "import graphify; print(graphify.__file__)"
```
Luego ejecuta directamente el comando instalado (usa la copia gestionada por uv), o elimina la copia antigua del sistema:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` funciona pero el comando `graphify` no**
El `PATH` de tu shell no incluye el directorio bin donde se instaló el comando. Prefiere `uv tool install` / `pipx install` antes que `pip` a secas, luego ejecuta `uv tool update-shell` / `pipx ensurepath` y abre una terminal nueva (ver las notas de instalación de arriba).

**`/graphify .` provoca «path not recognized» en PowerShell**
PowerShell trata una `/` inicial como separador de rutas. Usa `graphify .` (sin barra) en Windows.

**El grafo tiene menos nodos después de `--update` o de una reconstrucción**
Si una refactorización eliminó archivos, los nodos antiguos persisten. Pasa `--force` (o define `GRAPHIFY_FORCE=1`) para sobrescribir incluso cuando la reconstrucción tenga menos nodos.

**`extract` termina con "extraction was incomplete ... refusing to overwrite"**
Cuando una pasada de extracción falla o un recorrido no puede leer el corpus por completo, la ejecución sería más pequeña que una completa, así que `graphify extract` se niega a sobrescribir un `graph.json` existente más grande con el resultado parcial (protegiendo tu `graph.json`). Arregla el fallo subyacente y vuelve a ejecutar, o pasa `--allow-partial` para sobrescribir de todas formas.

**El grafo tiene nodos duplicados para la misma entidad (duplicados fantasma)**
Los duplicados fantasma (el mismo símbolo apareciendo dos veces — una vez por extracción de AST con una ubicación de origen, otra por extracción semántica sin ella) ahora se fusionan automáticamente en tiempo de construcción. Si ves esto en un grafo construido antes de v0.8.33, ejecuta una reextracción completa para limpiarlo:
```bash
graphify extract . --force
```

**Ollama se queda sin VRAM / se excede la ventana de contexto**
La ventana de caché KV se dimensiona automáticamente, pero puede ser demasiado grande para tu GPU. Redúcela:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**Avisos de `LLM returned invalid JSON` / `Unterminated string`**
La respuesta JSON del modelo alcanzó su límite de tokens de salida y se cortó a mitad de una cadena. graphify se recupera automáticamente (divide el fragmento y reextrae las mitades, y un documento único sobredimensionado se corta primero en los límites de encabezado/párrafo para que todo el archivo siga cubierto), así que estos avisos son ruidosos pero no suponen pérdida de datos. Para reducir el ruido, eleva el límite de salida o reduce la salida de cada fragmento:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
Con un gateway en la nube como OpenRouter, prefiere `--backend openai` (definiendo `OPENAI_BASE_URL`) antes que el shim de Ollama — es una ruta más limpia y compatible con OpenAI. Si el modelo tiene su propio tope de salida máxima, reducir `--token-budget` es la palanca fiable.

**El HTML del grafo es demasiado grande para abrirse en un navegador (>5000 nodos)**
Omite la generación de HTML y usa el JSON directamente:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**`graph.json` tiene marcadores de conflicto después de que dos desarrolladores confirmen a la vez**
Ejecuta `graphify hook install` — configura un driver de fusión de git que fusiona `graph.json` por unión automáticamente para que los conflictos nunca ocurran.

**La extracción devuelve nodos/aristas vacíos para documentos o PDF**
Los documentos, PDF e imágenes requieren una llamada a un LLM — los corpus solo de código no necesitan ninguna clave. Comprueba que tu clave de API esté definida y que el backend sea el correcto:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**Aviso de discrepancia de versión de la skill en tu IDE**
Tu versión instalada de graphify es distinta del archivo de la skill. Actualiza:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**La caché de prompts de Claude Code se invalida después de cada `graphify extract`**
Graphify escribe archivos de salida (`graph.json`, `graphify-out/`) dentro del espacio de trabajo. Si esas rutas no están ignoradas, cada escritura invalida la caché de prompts de Claude Code, forzando una recarga completa a las tarifas de escritura de caché en el siguiente turno. Añádelas a `.claudeignore`:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## Referencia completa de comandos

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

> **Nombres de comunidad:** dentro de un agente (Claude Code, Gemini CLI) el propio agente nombra las comunidades. Cuando ejecutas la CLI a secas, `cluster-only` las nombra automáticamente con el backend configurado (integrado o un proveedor personalizado compatible con OpenAI) — pasa `--no-label` para mantener `Community N`, o ejecuta `graphify label` para (re)generar nombres a demanda.

---

## Más información

- [Cómo funciona](../how-it-works.md) — el pipeline de extracción, la detección de comunidades, la puntuación de confianza, los benchmarks
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — desglose de módulos, cómo añadir un lenguaje
- [Integraciones opcionales](../docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — el libro sobre las ideas detrás de graphify, la arquitectura de principio a fin

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) es la capa siempre activa construida sobre graphify — aplica el mismo enfoque de grafo a todo tu contexto de trabajo: reuniones, archivos, documentos y código, actualizándose de forma continua en segundo plano.

Construido para personas y equipos cuyo trabajo vive repartido en cientos de conversaciones y documentos que nunca podrían reconstruir por completo.

**[Únete a la lista de espera en graphify.com](https://graphify.com).** Prueba gratuita próximamente.

---

<details>
<summary>Contribuir</summary>

### Configuración del entorno de desarrollo

El proyecto usa [uv](https://docs.astral.sh/uv/) para el flujo de trabajo de desarrollo. Instálalo una vez, y luego:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

Verifica la instalación editable:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### Ejecutar las pruebas

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> Nota para macOS: la suite de pruebas incluye tanto los fixtures `sample.f90` como `sample.F90`. Estos colisionan en sistemas de archivos que no distinguen mayúsculas de minúsculas como HFS+ / APFS. Ejecuta en Linux o en un contenedor Docker si necesitas probar ambas variantes de Fortran simultáneamente.

### Flujo de trabajo con Git

- El desarrollo activo ocurre en la rama `v8`.
- Estilo de commit: `fix: <description>` / `feat: <description>` / `docs: <description>`
- Antes de abrir un PR, ejecuta `uv run pytest tests/ -q` y confirma que pasa.
- Añade un archivo de fixture a `tests/fixtures/` y pruebas a `tests/test_languages.py` para cualquier nuevo extractor de lenguaje.

### Qué contribuir

Los **ejemplos trabajados** son la contribución más útil. Ejecuta `/graphify` sobre un corpus real, guarda la salida en `worked/{slug}/`, escribe un `review.md` honesto que cubra lo que el grafo acertó y lo que falló, y abre un PR.

**Errores de extracción** — abre un issue con el archivo de entrada, la entrada de caché (`graphify-out/cache/`), y qué se omitió o salió mal.

Consulta [ARCHITECTURE.md](../../ARCHITECTURE.md) para las responsabilidades de los módulos y cómo añadir un lenguaje.

</details>
