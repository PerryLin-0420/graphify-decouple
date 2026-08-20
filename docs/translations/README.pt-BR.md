<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>Um fork do <a href="https://github.com/Graphify-Labs/graphify">graphify</a> que adiciona o <code>graphify decouple</code></b> — candidatos a Extract-Class para god objects, com pontuação de risco, 0-LLM, reverificados contra o código-fonte real (não apenas contra o grafo de chamadas) antes de recomendar qualquer coisa. Veja <a href="#decouple-candidatos-a-extract-class-com-pontuação-de-risco">Decouple: candidatos a Extract-Class com pontuação de risco</a> abaixo.
</p>

<div align="center">
<details><summary><b>Leia isto em outros idiomas</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>O acesso antecipado à plataforma graphify está aberto antes do lançamento público da v1: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

Digite `/graphify` no seu assistente de código com IA e ele mapeia todo o seu projeto (código, docs, PDFs, imagens, vídeos) em um **grafo de conhecimento** que você pode **consultar em vez de fazer grep** nos arquivos.

- **Mapas de código de graça, totalmente locais.** O código é analisado com AST via tree-sitter: determinístico, sem LLM, nada sai da sua máquina. (Docs, PDFs, imagens e vídeo usam o modelo do seu assistente, ou uma chave de API configurada, para uma passagem semântica.)
- **Toda aresta é explicada.** Cada conexão é marcada como `EXTRACTED` (explícita no código-fonte) ou `INFERRED` (resolvida pelo graphify), para que você saiba o que foi lido diretamente do que foi inferido.
- **Não é um índice vetorial.** Sem embeddings, sem vector store: um grafo de verdade que você percorre. Faça uma pergunta, trace o caminho entre duas coisas, ou explique um conceito.

> Quer isso sempre ativo, atualizando em segundo plano ao longo do seu código, docs e reuniões, em vez de só sob demanda? É isso que estamos construindo na **[graphify.com](https://graphify.com)**, e o acesso antecipado está aberto agora em **[app.graphify.com](https://app.graphify.com/login)**.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="o graph.html interativo do graphify mostrando a base de código do FastAPI como um grafo de conhecimento de layout por força, com uma legenda das comunidades detectadas" width="900">
</p>
<p align="center">
  <em>A base de código do FastAPI mapeada pelo graphify. Cada nó é um conceito, as cores são comunidades detectadas, e tudo é clicável no graph.html.</em>
</p>

**Comece agora** (30 segundos):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

Depois, no seu assistente de IA:

```
/graphify .
```

Pronto. Você recebe **três arquivos**:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**Funciona em** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, e mais de 15 outros — [escolha sua plataforma](#instalação).

---

## Veja em ação

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="consulta de caminho do graphify: um terminal pede o caminho mais curto entre FastAPI e ModelField, e a resposta acende salto a salto ao longo do grafo de conhecimento" width="900">
</p>

Depois que o grafo é construído, você o consulta em vez de ler arquivos. Saída real, graphify rodado na base de código do FastAPI mostrada acima:

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

Toda aresta carrega uma **etiqueta de confiança** (`EXTRACTED` = explícita no código-fonte, `INFERRED` = derivada por resolução), para que você saiba o que foi lido diretamente do que foi inferido. `graphify query "<pergunta>"` retorna um subgrafo delimitado para uma pergunta em linguagem natural, e `graphify path A B` traça como duas coisas quaisquer se conectam.

---

## Decouple: candidatos a Extract-Class com pontuação de risco

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: o god node MainWindow se dividindo em classes candidatas com pontuação de risco, com um aviso de estado compartilhado entre duas delas" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: as 5 classes propostas de MainWindow, painel Node Info aberto em Main Window Axis and Range Controls mostrando uma sobreposição de estado de 0,608 com Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>DECOUPLE.html em uma execução real — clicar em uma classe proposta mostra exatamente com qual outra classe ela compartilha estado, e o que especificamente é compartilhado.</em>
</p>

A mesma página também renderiza a divisão em si. Alternar **Preview decoupled view** troca os métodos próprios da god class pelas classes propostas e re-roteia as arestas no lugar — a mudança de ligação, não um diagrama redesenhado:

| Antes — a god class hoje | Depois — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html antes do toggle: um único nó central MainWindow com seus próprios métodos espalhados ao redor" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html depois do toggle: o mesmo nó reduzido a 5 classes propostas em forma de losango, arestas verdes tracejadas mostrando quais métodos foram extraídos para cada uma, e arestas vermelhas mostrando o estado de instância compartilhado entre duas delas" width="440"> |
| Um nó contendo 47 de seus próprios métodos, cada um alcançável apenas através da classe. | As classes propostas. Verde tracejado = o que foi extraído para cada uma; vermelho = o estado de instância que duas delas ainda compartilham, que é exatamente o que decide entre `split` e `keep_as_is`. Só são desenhados os candidatos que passam do limiar de risco — aqui 5 de 6, e por isso um método fica sem losango onde pousar. |

O `graphify decouple` encontra god objects e diz se dividi-los realmente vale a pena — não apenas que eles são grandes.

O modo de falha que ele existe para capturar: uma classe com 47 métodos que o agrupamento por grafo de chamadas divide alegremente em 5 grupos de aparência organizada, todos os quais ainda leem e escrevem exatamente o mesmo estado de instância `self._chart_style` / `self._crosshair` por baixo dos panos. Fazer esse split não desacopla nada — você só moveu métodos para novos arquivos que ainda não podem ser testados, alterados ou raciocinados de forma independente, porque todos ainda precisam do mesmo estado compartilhado passado de volta. Uma ferramenta que só olha o grafo de chamadas não consegue enxergar isso de jeito nenhum; ela precisa voltar ao código-fonte real.

**Duas verificações, ambas 0-LLM, ambas determinísticas:**

1. **Isso é mesmo um God Object?** Um nó com grau alto pode ser um verdadeiro God Object (muitos métodos PRÓPRIOS, espalhados por responsabilidades não relacionadas — o Extract Class se aplica) ou um hub/modelo de dados sobrerreferenciado (poucos métodos próprios, majoritariamente referências *de entrada* — dividir seu corpo não faz nada; a correção é estreitar sua interface, não extrair uma classe). `classify_god_node` diferencia os dois pelo `member_ratio`, não pelo grau bruto — a diferença que impede que `TraceSource` (84 arestas, mas só 6 métodos próprios) receba uma sugestão de split espúria que `MainWindow` (88 arestas, 47 métodos próprios) recebe corretamente.
2. **O split realmente reduziria o acoplamento?** O `risk_before` (o tamanho/acoplamento/fragmentação atual do god node) é comparado com o `risk_after` — o NOVO risco que o próprio split introduziria: chamadas entre grupos que eram arestas intraclasse invisíveis e passam a ser dependências interclasse explícitas, chamadores que passariam a depender de mais de uma classe nova e — a verificação que um grafo de chamadas estruturalmente não consegue fazer — quanto estado de instância `self`/`this` (leituras, escritas e chamadas a métodos auxiliares compartilhados, ponderadas separadamente: uma **escrita** compartilhada pontua mais alto que uma leitura compartilhada) os grupos propostos realmente têm em comum. Isso reanalisa diretamente o arquivo-fonte do próprio god node com tree-sitter; não depende do grafo já extraído pelo graphify, que nunca registra acesso a campos em nenhuma linguagem. Só quando o `risk_after` fica abaixo de um limiar em relação ao `risk_before` é que o plano recomenda `split` — caso contrário é `marginal` ou `keep_as_is`, e um candidato desencorajado é reportado como um número, nunca desenhado como uma forma que você precisa questionar a olho nu.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

Gera três arquivos ao lado do `graph.json`:

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

**Cobertura de linguagens para a verificação de compartilhamento de estado** (a classificação baseada só no grafo de chamadas acima funciona para toda linguagem que o graphify extrai; esta tabela é especificamente sobre a reanálise do código-fonte que verifica a sobreposição de estado `self`/`this`):

| Language | Supported | Notes |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` é seu próprio nó de AST, não um acesso a campo encapsulado — tratado explicitamente |
| C# | ✅ | |
| Rust | ✅ | `self.x` via blocos `impl` |
| Ruby | ✅ | `@x` (o idioma dominante) + chamadas `self.foo` |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | resolução de receiver por método — Go não tem palavra-chave `self`/`this`, então o nome do receiver (`f` em `func (f *Foo) M()`) é resolvido novamente para cada método |
| C | ❌ | um parâmetro ponteiro para struct não tem nenhum marcador sintático que o distinga de qualquer outro parâmetro — sem sinal confiável sem inferência de tipos completa |

Um god node em uma linguagem não suportada, ou cujo código-fonte não pode ser lido, é marcado como `state_analysis: "skipped"` — a classificação e a pontuação do grafo de chamadas ainda são executadas, mas a recomendação passa a depender só do grafo de chamadas, em vez de simplesmente assumir silenciosamente que a verificação de estado passou.

---

## O que ele faz

O que você recebe pronto para uso:

| Capability | What you get |
|---|---|
| **God nodes** | Os conceitos mais conectados, para você ver por onde tudo passa |
| **Comunidades** | O grafo dividido em subsistemas (Leiden), com rótulos sem LLM |
| **Links entre arquivos** | `calls` / `imports` / `inherits` / `mixes_in` resolvidos entre ~40 linguagens via AST tree-sitter |
| **Query, path, explain** | Faça uma pergunta, trace o caminho entre duas coisas, ou explique um conceito, tudo contra o `graph.json` |
| **Justificativa + referências a docs** | Comentários `# NOTE:` / `# WHY:` e citações de ADR/RFC viram nós de primeira classe ligados ao código |
| **Além do código** | Docs, PDFs, imagens e vídeo/áudio são todos mapeados no mesmo grafo |
| **Local-first** | O código é analisado localmente com tree-sitter (sem LLM, nada sai da sua máquina); só a passagem semântica sobre docs/mídia chama um backend, e só se você configurar um |

---

## Benchmarks

| Benchmark | Metric | graphify | Field |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | QA accuracy | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | QA accuracy | **76%** | empatado com dense RAG |
| Graph build | LLM credits | **0** | por token na maioria dos sistemas |

Todos os sistemas rodaram no mesmo ambiente de teste, com o mesmo modelo e os mesmos orçamentos, avaliados por um juiz validado às cegas contra um segundo juiz (90,6% de concordância, kappa de Cohen 0,81). Tabelas completas por sistema, o resultado de inteligência de código e comandos de reprodução: **[BENCHMARKS.md](../../BENCHMARKS.md)**.

---

## Pré-requisitos

| Requirement | Minimum | Check | Install |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(recomendado)* | qualquer | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(alternativa)* | qualquer | `pipx --version` | `pip install pipx` |

**Instalação rápida no macOS (Homebrew):**
```bash
brew install python@3.12 uv
```

**Instalação rápida no Windows:**
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

## Instalação

> **Pacote oficial:** O pacote no PyPI é `graphifyy` (dois "y"). Outros pacotes `graphify*` no PyPI não têm afiliação com este projeto. O comando de CLI continua sendo `graphify`.

**Passo 1 — instale o pacote:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**Passo 2 — registre a skill no seu assistente de IA:**

```bash
graphify install
```

Pronto. Abra seu assistente de IA e digite `/graphify .`

Para instalar a skill do assistente no repositório atual em vez de no seu
perfil de usuário, adicione `--project`:

```bash
graphify install --project
graphify install --project --platform codex
```

Instalações com escopo de projeto gravam dentro do diretório atual, por exemplo
`.claude/skills/graphify/SKILL.md` ou `.agents/skills/graphify/SKILL.md` (mais um
sidecar `references/` que a skill carrega sob demanda), e
imprimem uma dica de `git add` para os arquivos que podem ser commitados.
Os comandos por plataforma que suportam instalações com escopo de projeto aceitam a mesma flag,
por exemplo `graphify claude install --project` ou `graphify codex install --project`.

> **Nota sobre PowerShell:** Use `graphify .` e não `/graphify .` — a barra inicial é um separador de caminho no PowerShell.

> **`graphify: command not found`?** `uv tool install` / `pipx install` colocam o comando `graphify` no diretório bin da própria ferramenta (`~/.local/bin`). Se o seu shell não encontrar o comando logo após a instalação — comum em uma configuração recém-instalada de macOS + zsh — esse diretório ainda não está no seu `PATH`: rode `uv tool update-shell` (ou `pipx ensurepath`), depois abra um novo terminal. Com o `pip` puro, adicione `~/.local/bin` (Linux) ou `~/Library/Python/3.x/bin` (Mac) ao seu PATH, ou rode `python -m graphify`.

> **Rodando com `uvx` / `uv tool run` em vez de instalar?** Informe o pacote, não o comando: `uvx --from graphifyy graphify install`. O simples `uvx graphify …` falha (`No solution found … no versions of graphify`) porque o `uv tool run` lê a primeira palavra como um *pacote*, e o pacote é `graphifyy` — o comando `graphify` vive dentro dele.

> **Evite `pip install` no Mac/Windows** se possível. A skill resolve o Python em tempo de execução a partir de `graphify-out/.graphify_python`; se isso apontar para um ambiente diferente daquele em que o `pip` instalou o pacote, você vai receber `ModuleNotFoundError: No module named 'graphify'`. `uv tool install` e `pipx install` isolam o pacote no próprio ambiente e evitam isso por completo.

> **Git hooks e uv tool / pipx:** `graphify hook install` embute o caminho do interpretador atual diretamente nos scripts de hook no momento da instalação, para que o hook post-commit dispare corretamente até mesmo em clientes git com GUI e executores de CI onde `~/.local/bin` não está no PATH. Se você reinstalar ou atualizar o graphify, rode `graphify hook install` novamente para atualizar o caminho embutido.

> **Modo estrito (Claude Code):** `graphify install --project --strict` faz o assistente realmente usar o grafo. A instalação padrão *incentiva* o assistente a rodar `graphify query` antes de ler arquivos; o modo estrito *bloqueia* a primeira leitura bruta de código-fonte da sessão e a redireciona para o grafo, depois volta ao incentivo (então dispara no máximo uma vez por sessão e nunca trava). Alterne em tempo de execução com `GRAPHIFY_HOOK_STRICT=1`/`0`; a instalação padrão permanece inalterada (incentivo leve).

<details>
<summary><b>Escolha sua plataforma</b> (mais de 20 assistentes, clique para expandir)</summary>

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

Usuários do Codex também precisam de `multi_agent = true` sob `[features]` em `~/.codex/config.toml` para extração paralela. O CodeBuddy usa o mesmo mecanismo de Agent tool e hook PreToolUse que o Claude Code. O Factory Droid usa a ferramenta `Task` para despacho paralelo de subagentes. OpenClaw e Aider usam extração sequencial (o suporte a agentes paralelos ainda é recente nessas plataformas). O Trae usa a Agent tool para despacho paralelo de subagentes e **não** suporta hooks `PreToolUse`, então o AGENTS.md é o mecanismo sempre ativo.

`--platform agents` (alias `--platform skills`) direciona para os locais genéricos e multi-framework do [Agent-Skills](https://github.com/anthropics/skills): o diretório global do usuário definido pela especificação, `~/.agents/skills/` (lido pelo `npx skills` e por frameworks compatíveis com a especificação), para uma instalação global, e `./.agents/skills/` para uma instalação de projeto (`--project`). O `graphify install` simples permanece de propósito restrito a uma única plataforma (Claude Code) — use a plataforma nomeada `agents` quando quiser que a skill seja descoberta por qualquer framework que leia `.agents/skills`.

> O Codex usa `$graphify` em vez de `/graphify`.

</details>

<details>
<summary><b>Extras opcionais</b> (instale só o que você precisa)</summary>

| Extra | What it adds | Install |
|---|---|---|
| `pdf` | Extração de PDF | `uv tool install "graphifyy[pdf]"` |
| `office` | Suporte a `.docx` e `.xlsx` | `uv tool install "graphifyy[office]"` |
| `google` | Renderização do Google Sheets | `uv tool install "graphifyy[google]"` |
| `video` | Transcrição de vídeo/áudio (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | Servidor MCP stdio | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Suporte a push para Neo4j | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | Suporte a push para FalkorDB | `uv tool install "graphifyy[falkordb]"` |
| `svg` | Exportação de grafo em SVG | `uv tool install "graphifyy[svg]"` |
| `leiden` | Detecção de comunidades Leiden (somente Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Inferência local com Ollama | `uv tool install "graphifyy[ollama]"` |
| `openai` | APIs OpenAI / compatíveis com OpenAI | `uv tool install "graphifyy[openai]"` |
| `gemini` | API do Google Gemini | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | API Claude da Anthropic (`--backend claude`, usa `ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (usa IAM, sem chave de API) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, usa `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "graphifyy[openai]"` |
| `sql` | Extração de esquema SQL | `uv tool install "graphifyy[sql]"` |
| `postgres` | Introspecção ao vivo de PostgreSQL (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | Extração de AST de BYOND DreamMaker `.dm`/`.dme` (pode precisar de um compilador C + `python3-dev` se nenhum wheel corresponder à sua plataforma) | `uv tool install "graphifyy[dm]"` |
| `terraform` | Extração de AST de Terraform / HCL `.tf`/`.tfvars`/`.hcl` | `uv tool install "graphifyy[terraform]"` |
| `pascal` | Extração de AST de Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` (arestas `calls`/`inherits` mais precisas; recai para um extrator baseado em regex quando ausente) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | Segmentação de consultas em chinês (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | Tudo acima | `uv tool install "graphifyy[all]"` |

</details>

---

## Faça seu assistente sempre usar o grafo

Rode isto uma vez no seu projeto depois de construir um grafo:

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

Isso grava um pequeno arquivo de configuração que diz ao seu assistente para consultar o grafo de conhecimento em perguntas sobre a base de código, preferindo consultas delimitadas como `graphify query "<pergunta>"` em vez de ler o relatório completo ou fazer grep nos arquivos brutos.

- **Plataformas com hook** (Claude Code, Gemini CLI): um hook dispara automaticamente antes de chamadas de ferramenta do tipo busca (e, no Claude Code, antes de ler arquivos-fonte um a um via as ferramentas Read/Glob) e incentiva o assistente a seguir o caminho do grafo.
- **Plataformas com arquivo de instruções** (Codex, OpenCode, Cursor, etc.): arquivos de instrução persistentes (`AGENTS.md`, `.cursor/rules/`, etc.) fornecem a mesma orientação de consulta prioritária.

O `GRAPH_REPORT.md` continua disponível para uma revisão ampla de arquitetura.

O **CodeBuddy** faz as mesmas duas coisas que o Claude Code: grava uma seção no `CODEBUDDY.md` dizendo ao CodeBuddy para ler o `graphify-out/GRAPH_REPORT.md` antes de responder perguntas de arquitetura, e instala hooks `PreToolUse` (`.codebuddy/settings.json`) que disparam antes de comandos de busca no Bash e leituras de arquivo, incentivando o uso do `graphify query` em vez disso.

O **Codex** grava no `AGENTS.md`, que é o que de fato carrega a orientação sempre ativa do grafo nessa plataforma. O `graphify codex install` também registra um hook `PreToolUse` em `.codex/hooks.json` (`graphify hook-check`), mas essa entrada é deliberadamente um **no-op**: o Codex Desktop rejeita `hookSpecificOutput.additionalContext` em `PreToolUse`, então emitir um incentivo ali quebraria as chamadas da ferramenta Bash. Diferente do Claude Code, onde o hook (`graphify hook-guard`) faz o incentivo, no Codex o hook dispara e intencionalmente não faz nada, e o `AGENTS.md` é o mecanismo sempre ativo.

O **Kilo Code** instala a skill Graphify em `~/.config/kilo/skills/graphify/SKILL.md` e um comando nativo `/graphify` em `~/.config/kilo/command/graphify.md`. O `graphify kilo install` também grava `AGENTS.md` mais um plugin nativo `tool.execute.before` (`.kilo/plugins/graphify.js` + registro em `.kilo/kilo.json` ou `.kilo/kilo.jsonc`), para que o Kilo tenha o mesmo comportamento de lembrete sempre ativo do grafo por meio da configuração nativa `.kilo`.

O **Cursor** grava `.cursor/rules/graphify.mdc` com `alwaysApply: true`, então o Cursor o inclui automaticamente em toda conversa, sem precisar de hook.

Para remover o graphify de todas as plataformas de uma vez: `graphify uninstall` (adicione `--purge` para também apagar `graphify-out/`). Ou use o comando específico da plataforma (por exemplo, `graphify claude uninstall`).

---

## O que tem no relatório

- **God nodes** — os conceitos mais conectados do seu projeto. Tudo passa por eles.
- **Conexões surpreendentes** — links entre coisas que vivem em arquivos ou módulos diferentes. Ranqueadas por quão inesperadas são.
- **O "porquê"** — comentários inline (`# NOTE:`, `# WHY:`, `# HACK:`), docstrings e justificativas de design vindas de docs são extraídos como nós separados, ligados ao código que explicam.
- **Perguntas sugeridas** — 4–5 perguntas que o grafo está unicamente posicionado para responder.
- **Etiquetas de confiança** — toda relação inferida é marcada como `EXTRACTED`, `INFERRED` ou `AMBIGUOUS`. Você sempre sabe o que foi encontrado versus o que foi um palpite.

---

## Quais arquivos ele processa

| Type | Extensions |
|------|-----------|
| Código (36 gramáticas tree-sitter) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme` requer `uv tool install graphifyy[dm]`; `.mts`/`.cts` reaproveitam a gramática do TypeScript, `.cc`/`.cxx` e CUDA `.cu`/`.cuh` e Metal `.metal` reaproveitam a gramática do C++) |
| Salesforce Apex | `.cls .trigger` (baseado em regex; classes, interfaces, enums, métodos, triggers, arestas SOQL/DML) |
| Terraform / HCL | `.tf .tfvars .hcl` (requer `uv tool install graphifyy[terraform]`) |
| Configs MCP | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — extrai nós de servidor, referências de pacote, requisitos de variável de ambiente |
| Manifestos de pacote | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — um nó de pacote canônico por pacote (por nome) mais arestas `depends_on`, de modo que um pacote referenciado em muitos manifestos é um único hub |
| Docs | `.md .mdx .qmd .html .txt .rst .yaml .yml` (links markdown `[text](./other.md)` e `[[wikilinks]]` viram arestas `references` entre docs) |
| Office | `.docx .xlsx` (requer `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (opcional; requer autenticação `gws` e `--google-workspace`; Sheets precisa de `uv tool install graphifyy[google]`) |
| PDFs | `.pdf` |
| Imagens | `.png .jpg .webp .gif` |
| Vídeo / Áudio | `.mp4 .mov .mp3 .wav` e mais (requer `uv tool install graphifyy[video]`) |
| YouTube / URLs | qualquer URL de vídeo (requer `uv tool install graphifyy[video]`) |

O código é extraído **localmente, sem chamadas de API** (AST via tree-sitter). Tudo o mais passa pela API do modelo do seu assistente de IA.

Arquivos `.gdoc`, `.gsheet` e `.gslides` do Google Drive para desktop são
atalhos apontadores, não o conteúdo do documento. Para incluir Google Docs, Sheets
e Slides nativos em uma extração headless, instale e autentique a
[CLI `gws`](https://github.com/googleworkspace/cli), depois rode:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

Você também pode definir `GRAPHIFY_GOOGLE_WORKSPACE=1`. O Graphify exporta os atalhos para
`graphify-out/converted/` como sidecars em Markdown, e então extrai esses arquivos.

---

## Comandos comuns

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

Veja [Decouple: candidatos a Extract-Class com pontuação de risco](#decouple-candidatos-a-extract-class-com-pontuação-de-risco) acima, ou a [referência completa de comandos](#referência-completa-de-comandos) abaixo.

---

## Ignorando arquivos

Crie um `.graphifyignore` na raiz do seu projeto — mesma sintaxe do `.gitignore`, incluindo negação com `!`.

**O `.gitignore` é respeitado automaticamente.** O graphify lê o `.gitignore` de cada diretório. Se um `.graphifyignore` também estiver presente, os dois são **mesclados** — os padrões do `.graphifyignore` são avaliados por último, então eles ganham em caso de conflito (incluindo negações com `!`). Adicionar um `.graphifyignore` só exclui mais; ele nunca reinclui um arquivo que seu `.gitignore` já excluía. O escopo de subdiretórios funciona do mesmo jeito que no git — um arquivo de ignore só afeta sua própria subárvore.

Passe `--no-gitignore` para o `graphify extract` quando código gerado ou transpilado ignorado pelo git deveria entrar no grafo. Isso desativa o `.gitignore` e o `.git/info/exclude`; o `.graphifyignore` continua se aplicando.

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

## Configuração para equipes

O `graphify-out/` deve ser commitado no git para que todo mundo no time comece com um mapa.

**Adições recomendadas ao `.gitignore`:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> O `manifest.json` agora é portável — as chaves são armazenadas como caminhos relativos e reancoradas ao carregar, então commitá-lo é seguro e evita um rebuild completo no primeiro checkout.

**Fluxo de trabalho:**
1. Uma pessoa roda `/graphify .` e commita `graphify-out/`.
2. Todos fazem pull — o assistente deles lê o grafo imediatamente.
3. Rode `graphify hook install` para reconstruir automaticamente depois de cada commit (só AST, sem custo de API). Isso também configura um merge driver do git para que o `graph.json` nunca fique com marcadores de conflito — dois devs commitando em paralelo têm seus grafos mesclados por união automaticamente.
4. Quando docs ou papers mudarem, rode `/graphify --update` para atualizar esses nós.

---

## Usando o grafo diretamente

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

O servidor MCP dá ao seu assistente acesso estruturado: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Servidor HTTP compartilhado

`--transport stdio` (o padrão) inicia um servidor local por desenvolvedor. `--transport http` serve as mesmas ferramentas pelo transporte MCP Streamable HTTP, para que um único processo compartilhado possa servir o grafo para todo o time — os clientes apontam a configuração MCP da IDE para `http://<host>:8080/mcp` em vez de rodar o graphify localmente.

| Flag | Default | Purpose |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Transporte a ser usado |
| `--host` | `127.0.0.1` | Host de bind do HTTP (use `0.0.0.0` para expor além do localhost) |
| `--port` | `8080` | Porta de bind do HTTP |
| `--api-key` | env `GRAPHIFY_API_KEY` | Exige `Authorization: Bearer <key>` (ou `X-API-Key`) |
| `--path` | `/mcp` | Caminho de montagem HTTP |
| `--json-response` | desligado | Retorna JSON simples em vez de streams SSE |
| `--stateless` | desligado | Sem estado por sessão (para deploys com load balancing / CI) |
| `--session-timeout` | `3600` | Encerra sessões com estado ociosas após N segundos (`0` desativa) |

O bind padrão em `127.0.0.1` é somente loopback. Defina `--host 0.0.0.0` **e** `--api-key` juntos ao expor em um host compartilhado. Rode em um container:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **Nota WSL / Linux:** o Ubuntu vem com `python3`, não `python`. Use um venv para evitar conflitos:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## Variáveis de ambiente

Estas só são necessárias para **extração headless / CI** (`graphify extract`). Ao rodar via a skill `/graphify` dentro da sua IDE, a API do modelo é fornecida pela sua sessão de IDE — nenhuma chave extra é necessária.

| Variable | Used for | When required |
|---|---|---|
| `ANTHROPIC_API_KEY` | Backend Claude (Anthropic) | `--backend claude` |
| `ANTHROPIC_BASE_URL` | URL de endpoint compatível com Anthropic (proxy LiteLLM, gateways, ...) | `--backend claude` (padrão: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Nome do modelo para o backend Claude — para endpoints personalizados, use o nome/alias de modelo que seu servidor expõe | `--backend claude` (padrão: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` or `GOOGLE_API_KEY` | Backend Google Gemini | `--backend gemini` |
| `OPENAI_API_KEY` | APIs OpenAI ou compatíveis com OpenAI | `--backend openai` (servidores locais aceitam qualquer valor não vazio) |
| `OPENAI_BASE_URL` | URL de servidor compatível com OpenAI (llama.cpp, vLLM, LM Studio, ...) | `--backend openai` (padrão: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | Nome do modelo para o backend OpenAI — para servidores auto-hospedados, use o nome/alias de modelo que seu servidor expõe (confira o endpoint `/v1/models` dele), por exemplo `LFM2.5-8B-A1B-UD-Q4_K_XL` para llama.cpp | `--backend openai` (padrão: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | Backend DeepSeek | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Backend Kimi Code | `--backend kimi` |
| `OLLAMA_BASE_URL` | URL de inferência local do Ollama | `--backend ollama` (padrão: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Nome do modelo do Ollama | `--backend ollama` (padrão: detecção automática) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Sobrescreve o tamanho da janela de KV-cache do Ollama | opcional — dimensionado automaticamente por padrão |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Minutos para manter o modelo do Ollama carregado | opcional — defina `0` para descarregar depois de cada chunk |
| `AZURE_OPENAI_API_KEY` | Backend Azure OpenAI Service | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | URL de endpoint do recurso Azure | `--backend azure` (obrigatório junto com a chave de API) |
| `AZURE_OPENAI_API_VERSION` | Sobrescreve a versão da API do Azure | opcional — padrão `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` or `GRAPHIFY_AZURE_MODEL` | Nome do deployment no Azure | opcional — padrão `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — cadeia de credenciais padrão | `--backend bedrock` (sem chave de API, usa IAM) |
| `GRAPHIFY_MAX_WORKERS` | Contagem de threads de paralelismo da AST | opcional — também a flag `--max-workers` |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Aumenta o limite de saída para corpora densos | opcional — por exemplo `32768` para arquivos grandes |
| `GRAPHIFY_API_TIMEOUT` | Timeout por chamada, em segundos, para os backends HTTP, claude-cli, Anthropic SDK e Bedrock (padrão: 600) | opcional — também a flag `--api-timeout` |
| `GRAPHIFY_MAX_RETRIES` | Quantas vezes tentar novamente uma requisição limitada por taxa (429) antes de desistir (padrão: 6; respeita `Retry-After`) | opcional — aumente para limites estritos por organização (por exemplo, kimi); `0` desativa |
| `GRAPHIFY_FORCE` | Força a reconstrução do grafo mesmo com menos nós | opcional — também a flag `--force` |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Ativa automaticamente a exportação do Google Workspace | opcional — defina como `1` |
| `GRAPHIFY_TRIAGE_BACKEND` | Backend para `graphify prs --triage` | opcional — autodetectado a partir das chaves disponíveis |
| `GRAPHIFY_TRIAGE_MODEL` | Sobrescreve o modelo usado na triagem | opcional — por exemplo `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | Defina como `1` para ativar o log de consultas local em `~/.cache/graphify-queries.log` (registra cada pergunta de query/path/explain + o caminho do corpus). Desligado por padrão — nada é gravado a menos que você opte por isso (#1797) | opcional |
| `GRAPHIFY_QUERY_LOG` | Ativa o log de consultas e grava nesse caminho em vez do padrão | opcional — desligado a menos que esta ou `_ENABLE` esteja definida |
| `GRAPHIFY_QUERY_LOG_DISABLE` | Defina como `1` para forçar o log de consultas a ficar desligado (tem prioridade sobre as variáveis de ativação) | opcional |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | Quando o log está ativado, também registra as respostas completas de subgrafo (desligado por padrão) | opcional |
| `GRAPHIFY_MAX_GRAPH_BYTES` | Sobrescreve o limite de tamanho de 512 MiB do graph.json — por exemplo `700MB`, `2GB`, ou bytes simples | opcional — útil para corpora muito grandes |
| `GRAPHIFY_MAX_CONTEXTS` | Número máximo de grafos de projeto não padrão mantidos por um servidor MCP multi-projeto | opcional — padrão: `8`; valores inválidos usam `8`, e valores abaixo de `1` usam `1` |
| `GRAPHIFY_LLM_TEMPERATURE` | Sobrescreve a temperatura do LLM para extração semântica — por exemplo `0.7`, ou `none` para omitir | opcional — omitido automaticamente para modelos de raciocínio o1/o3/o4/gpt-5 |

---

## Privacidade

- **Arquivos de código** — processados localmente via tree-sitter. Nada sai da sua máquina. Um corpus só de código não requer nenhuma chave de API — o `graphify extract` roda totalmente offline. Em um repositório misto, adicione `--code-only` para indexar só o código e pular docs/PDFs/imagens que de outra forma precisariam de um LLM.
- **Vídeo / áudio** — transcritos localmente com faster-whisper. Nada sai da sua máquina.
- **Docs, PDFs, imagens** — enviados ao seu assistente de IA para extração semântica (via a skill `/graphify`, usando qualquer modelo que sua sessão de IDE rode). O `graphify extract` headless requer `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), uma instância do Ollama em execução (`OLLAMA_BASE_URL`), credenciais AWS via a cadeia de provedores padrão (Bedrock — sem chave de API, usa IAM), ou o binário da CLI `claude` (Claude Code — sem chave de API, usa sua assinatura Claude). A flag `--dedup-llm` usa a mesma chave.
- **Residência de dados** — o `graphify extract` detecta automaticamente qual provedor usar com base em qual chave de API está definida (prioridade: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). Para código com requisitos de residência de dados, use `--backend ollama` (totalmente local) ou passe uma flag `--backend` explícita. O Kimi (`MOONSHOT_API_KEY`) roteia para servidores da Moonshot AI na China.
- **Sem telemetria**, sem rastreamento de uso, sem analytics.
- **Log de consultas** — toda chamada `graphify query`, `graphify path`, `graphify explain` e `query_graph` via MCP é registrada em `~/.cache/graphify-queries.log` no formato JSON Lines (timestamp, pergunta, corpus, nós retornados, duração). As respostas completas de subgrafo **não** são armazenadas por padrão. Defina `GRAPHIFY_QUERY_LOG_DISABLE=1` para desativar, ou `GRAPHIFY_QUERY_LOG=/dev/null` para silenciar sem desativar o caminho de código.

---

## Limitações e limites

O que o graphify deliberadamente **não** faz, e onde sua cobertura termina:

- **Não é um motor de busca semântica/vetorial.** O grafo é estrutural — nós e arestas tipadas resolvidas a partir do código-fonte, não embeddings. `graphify query`/`path`/`explain` percorrem essa estrutura; eles não conseguem revelar uma conexão que não esteja representada como uma aresta, mesmo que ela seja "semanticamente" relacionada. Não existe nenhum fallback por similaridade/vizinho mais próximo.
- **Docs, PDFs, imagens e a extração headless de vídeo/URL não são só locais.** Somente o código (AST do tree-sitter) e a transcrição de áudio/vídeo (faster-whisper) rodam totalmente offline. Extrair docs/PDFs/imagens sempre chama um LLM — o modelo do seu assistente de IA via a skill `/graphify`, ou uma chave de API de backend configurada para o `graphify extract` headless. Veja [Privacidade](#privacidade) acima para saber exatamente qual flag ou chave cada caminho precisa.
- **A verificação de compartilhamento de estado do decouple não cobre todas as linguagens.** C não tem um sinal confiável de `self`/`this` sem inferência de tipo completa, então é excluído (veja a [tabela de cobertura de linguagens](#decouple-candidatos-a-extract-class-com-pontuação-de-risco) acima). Um god node em uma linguagem não suportada, ou cujo código-fonte não pode ser lido, recai em uma pontuação baseada só no grafo de chamadas (`state_analysis: "skipped"`) em vez de uma verificação de estado verificada.
- **O data-flow floor 3D é uma heurística de nomes, não uma análise de dataflow/taint.** A detecção de fronteiras de E/S do `data_floor` (parsers, loaders, readers, writers, clientes de BD/HTTP) usa convenções de nomenclatura (`boundary_reason`); um nó de fronteira com um nome fora do padrão pode passar despercebido, subestimando quão profundo o restante do grafo realmente está.
- **As tags de confiança são a confiança de resolução do próprio graphify, não uma verdade absoluta.** As arestas `INFERRED` e `AMBIGUOUS` são resoluções de melhor esforço e ainda assim podem estar erradas, especialmente para idiomas altamente dinâmicos (reflexão, dispatch em tempo de execução, metaprogramação) que nenhuma passagem estática de AST consegue resolver por completo.
- **A visualização HTML e o tamanho do grafo têm, ambos, um teto.** `graph.html` / `DECOUPLE.html` pulam a geração acima de 5.000 nós por padrão (`MAX_NODES_FOR_VIZ`, ajustável via `GRAPHIFY_VIZ_NODE_LIMIT`); o próprio `graph.json` é limitado a 512 MiB (`GRAPHIFY_MAX_GRAPH_BYTES` para sobrepor). Use `--no-viz` junto com `query`/`path`/`explain` para corpora que ultrapassem qualquer um dos dois limites.
- **A consciência entre projetos é opcional, não automática.** `graphify query` só enxerga o único grafo que você aponta. Perguntas multi-repositório exigem registrar explicitamente cada projeto no grafo compartilhado primeiro (`graphify global add`, limitado a `GRAPHIFY_MAX_CONTEXTS` contextos não padrão por servidor MCP) — o graphify nunca varre sua máquina em busca de outros repositórios por conta própria.
- **A extração paralela multiagente depende da plataforma.** Ela precisa de suporte do lado do assistente para gerar subagentes (`multi_agent = true` em `~/.codex/config.toml` para o Codex, a ferramenta Agent/Task no Claude Code/CodeBuddy/Factory Droid/Trae). OpenClaw e Aider atualmente só extraem de forma sequencial.
- **O servidor MCP HTTP compartilhado se vincula só a loopback por padrão.** Alcançá-lo de outra máquina exige um `--host 0.0.0.0` **e** um `--api-key` explícitos; o graphify não gerencia TLS nem nenhuma autenticação além desse único token bearer.
- **O PowerShell interpreta uma `/` inicial como separador de caminho.** Por isso o `/graphify .` falha no Windows PowerShell, e não é um bug do graphify — use `graphify .` em vez disso.

---

## Solução de problemas

**`graphify: command not found` depois de instalar**
A CLI está instalada, mas o diretório bin dela não está no `PATH` do seu shell. Escolha a correção conforme como você instalou:
- **uv** (`uv tool install graphifyy`): o comando vai para o diretório bin de ferramentas do uv (`~/.local/bin`), que uma configuração recém-instalada de macOS/zsh muitas vezes não tem no `PATH`. Rode `uv tool update-shell`, depois abra um novo terminal. (Encontre o diretório com `uv tool dir --bin`.)
- **pipx** (`pipx install graphifyy`): rode `pipx ensurepath`, depois abra um novo terminal.
- **pip** (`pip install graphifyy`): o pip instala scripts em um diretório bin de usuário que pode não estar no `PATH` — adicione `~/Library/Python/3.x/bin` (macOS) ou `~/.local/bin` (Linux) ao seu `PATH` em `~/.zshrc`/`~/.bashrc`, ou simplesmente rode `python -m graphify`.

**`uvx graphify …` ou `uv tool run graphify …` falha ao resolver `graphify`**
O pacote no PyPI é `graphifyy`; `graphify` é só o comando que ele fornece. O `uv tool run` trata a primeira palavra como um *nome de pacote*, então ele procura um pacote chamado `graphify` e reporta `No solution found … no versions of graphify`. Nomeie o pacote explicitamente: `uvx --from graphifyy graphify install` (o mesmo que `uv tool run --from graphifyy graphify install`). Ou rode `uv tool install graphifyy` uma vez e depois chame `graphify` diretamente.

**`uv run --with graphifyy python -m graphify` roda silenciosamente uma instalação mais antiga**
O `uv run` usa o Python do *sistema*, então se uma versão mais antiga do `graphifyy` também mora lá (por exemplo, um `pip install graphifyy` anterior), o Python pode encontrar essa cópia primeiro no `sys.path`, e o `--with graphifyy` não vai sobrescrevê-la. Ele roda sem erro, mas você recebe o comportamento da versão *antiga* — por exemplo, sobrescritas de ambiente como `OPENAI_BASE_URL` são ignoradas silenciosamente, então as requisições atingem o endpoint padrão e falham com um 401 que parece uma chave inválida. A impressão digital é uma linha `warning: skill is from graphify <newer>, package is <older>` — isso significa que uma instalação diferente foi carregada, não apenas uma skill desatualizada. Verifique qual cópia foi realmente carregada:
```bash
python -c "import graphify; print(graphify.__file__)"
```
Depois rode o comando instalado diretamente (ele usa a cópia gerenciada pelo uv), ou remova a cópia antiga do sistema:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` funciona, mas o comando `graphify` não**
O `PATH` do seu shell não inclui o diretório bin onde o comando foi instalado. Prefira `uv tool install` / `pipx install` em vez do `pip` puro, depois rode `uv tool update-shell` / `pipx ensurepath` e abra um novo terminal (veja as notas de instalação acima).

**`/graphify .` causa "path not recognized" no PowerShell**
O PowerShell trata uma `/` inicial como separador de caminho. Use `graphify .` (sem barra) no Windows.

**O grafo tem menos nós depois de `--update` ou rebuild**
Se uma refatoração apagou arquivos, os nós antigos permanecem. Passe `--force` (ou defina `GRAPHIFY_FORCE=1`) para sobrescrever mesmo quando o rebuild tiver menos nós.

**`extract` termina com "extraction was incomplete ... refusing to overwrite"**
Quando uma passagem de extração trava ou uma varredura não consegue ler todo o corpus, a execução ficaria menor que uma completa, então o `graphify extract` se recusa a sobrescrever um grafo existente maior com o resultado parcial (protegendo seu `graph.json`). Corrija a falha subjacente e rode novamente, ou passe `--allow-partial` para sobrescrever mesmo assim.

**O grafo tem nós duplicados para a mesma entidade (duplicatas fantasma)**
Duplicatas fantasma (o mesmo símbolo aparecendo duas vezes — uma vez pela extração de AST com localização no código-fonte, outra pela extração semântica sem ela) agora são mescladas automaticamente no momento da construção. Se você ver isso em um grafo construído antes da v0.8.33, rode uma reextração completa para limpar:
```bash
graphify extract . --force
```

**Ollama fica sem VRAM / janela de contexto excedida**
A janela de KV-cache é dimensionada automaticamente, mas pode ser grande demais para sua GPU. Reduza-a:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**Avisos `LLM returned invalid JSON` / `Unterminated string`**
A resposta JSON do modelo atingiu o limite de tokens de saída e foi cortada no meio de uma string. O graphify se recupera automaticamente (ele divide o chunk e reextrai as metades, e um documento único grande demais é primeiro fatiado em limites de título/parágrafo para que o arquivo inteiro continue coberto), então esses avisos são ruído, não perda de dados. Para reduzir a agitação, aumente o limite de saída ou diminua a saída de cada chunk:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
Com um gateway em nuvem como o OpenRouter, prefira `--backend openai` (defina `OPENAI_BASE_URL`) em vez do shim do Ollama — é um caminho compatível com OpenAI mais limpo. Se o modelo tiver seu próprio teto de saída máxima, reduzir `--token-budget` é a alavanca mais confiável.

**O HTML do grafo é grande demais para abrir em um navegador (>5000 nós)**
Pule a geração de HTML e use o JSON diretamente:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**`graph.json` tem marcadores de conflito depois que dois devs commitam ao mesmo tempo**
Rode `graphify hook install` — isso configura um merge driver do git que mescla o `graph.json` por união automaticamente, para que conflitos nunca aconteçam.

**A extração retorna nós/arestas vazios para docs ou PDFs**
Docs, PDFs e imagens exigem uma chamada de LLM — corpora só de código não precisam de nenhuma chave. Verifique se sua chave de API está definida e se o backend está correto:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**Aviso de incompatibilidade de versão da skill na sua IDE**
Sua versão instalada do graphify é diferente do arquivo da skill. Atualize:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**O cache de prompt do Claude Code é invalidado depois de cada `graphify extract`**
O Graphify grava arquivos de saída (`graph.json`, `graphify-out/`) dentro do workspace. Se esses caminhos não forem ignorados, cada gravação invalida o cache de prompt do Claude Code, forçando um novo upload completo em taxas de escrita de cache no próximo turno. Adicione-os ao `.claudeignore`:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## Referência completa de comandos

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

> **Nomes das comunidades:** dentro de um agente (Claude Code, Gemini CLI) o próprio agente nomeia as comunidades. Ao rodar a CLI pura, o `cluster-only` as nomeia automaticamente com o backend configurado (embutido ou provedor personalizado compatível com OpenAI) — passe `--no-label` para manter `Community N`, ou rode `graphify label` para (re)gerar nomes sob demanda.

---

## Saiba mais

- [Como funciona](../how-it-works.md) — o pipeline de extração, detecção de comunidades, pontuação de confiança, benchmarks
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — divisão dos módulos, como adicionar uma linguagem
- [Integrações opcionais](../docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — o livro sobre as ideias por trás do graphify, a arquitetura de ponta a ponta

---

## graphify Enterprise

O [**graphify Enterprise**](https://graphify.com) é a camada sempre ativa construída sobre o graphify — ele aplica a mesma abordagem de grafo a todo o seu contexto de trabalho: reuniões, arquivos, docs e código, atualizando continuamente em segundo plano.

Feito para pessoas e times cujo trabalho vive em centenas de conversas e documentos que eles nunca conseguem reconstruir por completo.

**[Entre na lista de espera em graphify.com](https://graphify.com).** Teste gratuito lançando em breve.

---

<details>
<summary>Contribuindo</summary>

### Configuração de desenvolvimento

O projeto usa o [uv](https://docs.astral.sh/uv/) para o fluxo de trabalho de desenvolvimento. Instale-o uma vez e depois:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

Verifique a instalação editável:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### Executando os testes

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> Nota macOS: o conjunto de testes inclui os fixtures `sample.f90` e `sample.F90`. Eles colidem em sistemas de arquivos HFS+ / APFS que não diferenciam maiúsculas de minúsculas. Rode em Linux ou em um container Docker se precisar testar as duas variantes de Fortran simultaneamente.

### Fluxo de trabalho com Git

- O desenvolvimento ativo acontece no branch `v8`.
- Estilo de commit: `fix: <description>` / `feat: <description>` / `docs: <description>`
- Antes de abrir um PR, rode `uv run pytest tests/ -q` e confirme que passa.
- Adicione um arquivo de fixture em `tests/fixtures/` e testes em `tests/test_languages.py` para qualquer novo extrator de linguagem.

### O que contribuir

**Exemplos trabalhados** são a contribuição mais útil. Rode `/graphify` em um corpus real, salve a saída em `worked/{slug}/`, escreva um `review.md` honesto cobrindo o que o grafo acertou e errou, e abra um PR.

**Bugs de extração** — abra uma issue com o arquivo de entrada, a entrada de cache (`graphify-out/cache/`) e o que estava faltando ou errado.

Veja [ARCHITECTURE.md](../../ARCHITECTURE.md) para responsabilidades dos módulos e como adicionar uma linguagem.

</details>
