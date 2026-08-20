<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>Форк <a href="https://github.com/Graphify-Labs/graphify">graphify</a>, добавляющий <code>graphify decouple</code></b> — 0-LLM кандидаты на Extract Class с оценкой риска для god object'ов, повторно проверенные по реальному исходному коду (а не только по графу вызовов), прежде чем что-либо рекомендовать. См. раздел <a href="#decouple-кандидаты-на-extract-class-с-оценкой-риска">Decouple: кандидаты на Extract Class с оценкой риска</a> ниже.
</p>

<div align="center">
<details><summary><b>Читать на других языках</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>Ранний доступ к платформе graphify открыт ещё до публичного релиза v1: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

Введите `/graphify` в вашем AI-ассистенте для написания кода, и он отобразит весь ваш проект (код, документацию, PDF, изображения, видео) в виде **графа знаний**, который можно **запрашивать вместо grep** по файлам.

- **Карты кода — бесплатно и полностью локально.** Код разбирается через AST tree-sitter: детерминированно, без LLM, ничего не уходит с вашей машины. (Документы, PDF, изображения и видео используют модель вашего ассистента или настроенный API-ключ для семантического прохода.)
- **Каждое ребро объяснено.** Каждая связь помечена как `EXTRACTED` (явно присутствует в источнике) или `INFERRED` (выведена graphify), поэтому всегда видно, что было прочитано напрямую, а что — выведено.
- **Это не векторный индекс.** Никаких эмбеддингов, никакого векторного хранилища — настоящий граф, по которому можно перемещаться. Задайте вопрос, проследите путь между двумя объектами или объясните одно понятие.

> Хотите, чтобы это работало постоянно, обновляясь в фоне по вашему коду, документации и встречам, а не только по запросу? Именно это мы строим на **[graphify.com](https://graphify.com)**, и ранний доступ уже открыт на **[app.graphify.com](https://app.graphify.com/login)**.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="Интерактивный graph.html graphify показывает кодовую базу FastAPI в виде силового графа знаний с легендой обнаруженных сообществ" width="900">
</p>
<p align="center">
  <em>Кодовая база FastAPI, отображённая graphify. Каждый узел — это понятие, цвета — обнаруженные сообщества, и всё это можно кликать в graph.html.</em>
</p>

**Начало работы** (30 секунд):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

Затем в вашем AI-ассистенте:

```
/graphify .
```

Вот и всё. Вы получаете **три файла**:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**Работает в** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot и ещё 15+ ассистентах — [выберите свою платформу](#установка).

---

## Демонстрация

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="Запрос пути в graphify: терминал спрашивает про самый короткий путь между FastAPI и ModelField, и ответ загорается хоп за хопом по графу знаний" width="900">
</p>

Когда граф построен, вы запрашиваете его вместо чтения файлов. Реальный вывод graphify, запущенного на кодовой базе FastAPI, показанной выше:

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

Каждое ребро несёт **тег уверенности** (`EXTRACTED` = явно присутствует в источнике, `INFERRED` = выведено при разрешении связей), поэтому всегда видно, что было прочитано напрямую, а что — выведено. `graphify query "<question>"` возвращает подграф, ограниченный вопросом на естественном языке, а `graphify path A B` прослеживает, как связаны между собой любые два объекта.

---

## Decouple: кандидаты на Extract Class с оценкой риска

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: god node MainWindow разбивается на кандидатные классы с оценкой риска, с предупреждением об общем состоянии между двумя из них" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: 5 предложенных классов для MainWindow, открыта панель Node Info для Main Window Axis and Range Controls, показывающая перекрытие состояния 0.608 с Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>DECOUPLE.html на реальном запуске — клик по предложенному классу показывает, с каким именно другим классом он делит состояние и что конкретно является общим.</em>
</p>

Та же страница рисует и саму разбивку. Переключатель **Preview decoupled view** заменяет собственные методы god-класса предложенными классами и перепрокладывает рёбра на месте — это изменение проводки, а не перерисованная диаграмма:

| До — god-класс сегодня | После — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html до переключения: один узел-хаб MainWindow с расходящимися вокруг него собственными методами" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html после переключения: тот же узел сведён к 5 предложенным классам в виде ромбов, зелёные пунктирные рёбра показывают, какие методы извлечены в каждый, красные — общее состояние экземпляра между двумя из них" width="440"> |
| Один узел с 47 собственными методами, каждый из которых доступен только через этот класс. | Предложенные классы. Зелёный пунктир = что извлечено в каждый; красный = состояние экземпляра, которое два из них по-прежнему делят, — именно это решает `split` или `keep_as_is`. Рисуются только кандидаты, прошедшие порог риска, — здесь 5 из 6, поэтому одному методу не достаётся ромба. |

`graphify decouple` находит god object'ы и говорит, действительно ли стоит их разбивать — а не просто что они большие.

Ошибка, которую это призвано отловить: класс с 47 методами, который кластеризация по графу вызовов охотно разбивает на 5 аккуратных на вид групп — все из которых по-прежнему читают и пишут одно и то же состояние экземпляра `self._chart_style` / `self._crosshair`. Если выпустить такое разбиение, вы ничего не разъединили — вы просто перенесли методы в новые файлы, которые всё так же невозможно тестировать, менять или анализировать по отдельности, потому что им всем всё равно нужно одно и то же общее состояние, передаваемое обратно. Инструмент, который смотрит только на граф вызовов, вообще не может это увидеть; ему нужно вернуться к реальному исходному коду.

**Две проверки, обе 0-LLM, обе детерминированные:**

1. **Это вообще God Object?** Узел с высокой степенью может быть настоящим God Object (множество СОБСТВЕННЫХ методов, разбросанных по несвязанным зонам ответственности — Extract Class применим) либо избыточно referenced хабом/моделью данных (мало собственных методов, в основном *входящие* ссылки — разбиение его тела ничего не даст; решение — сузить интерфейс, а не выделять класс). `classify_god_node` различает их по `member_ratio`, а не по «сырой» степени — именно это отличие не даёт `TraceSource` (84 ребра, но только 6 собственных методов) получить ложное предложение разбиения, которое `MainWindow` (88 рёбер, 47 собственных методов) корректно получает.
2. **Действительно ли разбиение снизит связанность?** `risk_before` (текущий размер/связанность/фрагментация god node) сравнивается с `risk_after` — НОВЫМ риском, который само разбиение внесёт: межгрупповые вызовы, которые были невидимыми внутриклассовыми рёбрами и становятся явными межклассовыми зависимостями, вызывающий код, которому теперь придётся зависеть от более чем одного нового класса, и — проверка, которую граф вызовов структурно не способен выполнить, — насколько предложенные группы на самом деле имеют общего состояния `self`/`this` (чтения, записи и вызовы общих вспомогательных методов, взвешенные по отдельности: общая **запись** оценивается выше, чем общее чтение). Это заново разбирает исходный файл самого god node напрямую через tree-sitter; оно не опирается на собственный извлечённый граф graphify, который никогда не фиксирует доступ на уровне полей для какого-либо языка. Только когда `risk_after` опускается ниже `risk_before` больше некоторого порога, план рекомендует `split` — иначе это `marginal` или `keep_as_is`, и не рекомендуемый кандидат всегда отражается как число, а не как фигура, которую нужно перепроверять на глаз.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

Выводит три файла рядом с `graph.json`:

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

**Языковая поддержка для проверки общего состояния** (классификация только по графу вызовов, описанная выше, работает для любого языка, который извлекает graphify; эта таблица — именно о повторном разборе исходного кода, который проверяет пересечение состояния `self`/`this`):

| Язык | Поддержка | Примечания |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` — отдельный узел AST, а не обёрнутый доступ к полю, обрабатывается явно |
| C# | ✅ | |
| Rust | ✅ | `self.x` через блоки `impl` |
| Ruby | ✅ | `@x` (доминирующая идиома) + вызовы `self.foo` |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | разрешение ресивера для каждого метода — в Go нет ключевого слова `self`/`this`, поэтому имя ресивера (`f` в `func (f *Foo) M()`) разрешается заново для каждого метода |
| C | ❌ | у параметра-указателя на структуру нет синтаксического маркера, отличающего его от любого другого параметра — без полного вывода типов надёжного сигнала нет |

God node на неподдерживаемом языке или тот, чей исходный код невозможно прочитать, помечается как `state_analysis: "skipped"` — классификация и оценка по графу вызовов всё равно выполняются, но рекомендация опирается только на граф вызовов, а не молча предполагает, что проверка состояния прошла успешно.

---

## Что это делает

Что вы получаете «из коробки»:

| Возможность | Что вы получаете |
|---|---|
| **God nodes** | Наиболее связанные понятия, чтобы видеть, через что всё проходит |
| **Сообщества** | Граф, разбитый на подсистемы (Leiden), с метками без LLM |
| **Связи между файлами** | `calls` / `imports` / `inherits` / `mixes_in`, разрешённые для ~40 языков через AST tree-sitter |
| **Query, path, explain** | Задайте вопрос, проследите путь между двумя объектами или объясните одно понятие — всё это по `graph.json` |
| **Обоснование и ссылки на документы** | Комментарии `# NOTE:` / `# WHY:` и ссылки на ADR/RFC становятся полноценными узлами, связанными с кодом |
| **Не только код** | Документы, PDF, изображения и видео/аудио — всё отображается в тот же граф |
| **Локально по умолчанию** | Код разбирается локально через tree-sitter (без LLM, ничего не уходит с вашей машины); backend вызывается только для семантического прохода по документам/медиа, и только если вы его настроили |

---

## Бенчмарки

| Бенчмарк | Метрика | graphify | Отрасль |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | Точность QA | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | Точность QA | **76%** | на уровне dense RAG |
| Построение графа | Кредиты LLM | **0** | у большинства систем — за токен |

Все системы запускались на одном и том же харнессе, с той же моделью и теми же бюджетами; оценка выставлялась судьёй, слепо верифицированным против второго судьи (согласие 90.6%, каппа Коэна 0.81). Полные таблицы по каждой системе, результат по коду и команды для воспроизведения: **[BENCHMARKS.md](../../BENCHMARKS.md)**.

---

## Требования

| Требование | Минимум | Проверка | Установка |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(рекомендуется)* | любая версия | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(альтернатива)* | любая версия | `pipx --version` | `pip install pipx` |

**Быстрая установка на macOS (Homebrew):**
```bash
brew install python@3.12 uv
```

**Быстрая установка на Windows:**
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

## Установка

> **Официальный пакет:** пакет PyPI называется `graphifyy` (с двумя «y»). Другие пакеты `graphify*` на PyPI не связаны с этим проектом. Команда CLI всё равно называется `graphify`.

**Шаг 1 — установите пакет:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**Шаг 2 — зарегистрируйте навык в вашем AI-ассистенте:**

```bash
graphify install
```

Вот и всё. Откройте вашего AI-ассистента и введите `/graphify .`

Чтобы установить навык ассистента в текущий репозиторий, а не в профиль пользователя, добавьте `--project`:

```bash
graphify install --project
graphify install --project --platform codex
```

Установка с привязкой к проекту записывает файлы в текущий каталог, например
`.claude/skills/graphify/SKILL.md` или `.agents/skills/graphify/SKILL.md` (плюс сопутствующий каталог
`references/`, который навык подгружает по требованию), и
выводит подсказку `git add` для файлов, которые можно закоммитить.
Команды для отдельных платформ, поддерживающих установку с привязкой к проекту, принимают тот же флаг,
например `graphify claude install --project` или `graphify codex install --project`.

> **Заметка про PowerShell:** используйте `graphify .`, а не `/graphify .` — в PowerShell ведущий слэш является разделителем пути.

> **`graphify: command not found`?** `uv tool install` / `pipx install` помещают команду `graphify` в bin-каталог своего инструмента (`~/.local/bin`). Если сразу после установки шелл не находит команду — что часто случается на свежей установке macOS + zsh — этот каталог ещё не в вашем `PATH`: выполните `uv tool update-shell` (или `pipx ensurepath`), затем откройте новый терминал. При использовании обычного `pip` добавьте `~/.local/bin` (Linux) или `~/Library/Python/3.x/bin` (Mac) в `PATH` либо запустите `python -m graphify`.

> **Запускаете через `uvx` / `uv tool run` вместо установки?** Указывайте имя пакета, а не команды: `uvx --from graphifyy graphify install`. Просто `uvx graphify …` не сработает (`No solution found … no versions of graphify`), потому что `uv tool run` читает первое слово как имя *пакета*, а пакет называется `graphifyy` — команда `graphify` находится внутри него.

> **Старайтесь избегать `pip install` на Mac/Windows**, если возможно. Навык определяет Python во время выполнения из `graphify-out/.graphify_python`; если он указывает на другое окружение, отличное от того, куда `pip` установил пакет, вы получите `ModuleNotFoundError: No module named 'graphify'`. `uv tool install` и `pipx install` изолируют пакет в собственном окружении и полностью избегают этой проблемы.

> **Git-хуки и uv tool / pipx:** `graphify hook install` встраивает путь к текущему интерпретатору прямо в скрипты хука во время установки, поэтому post-commit хук срабатывает корректно даже в GUI git-клиентах и CI-раннерах, где `~/.local/bin` не в `PATH`. Если вы переустанавливаете или обновляете graphify, повторно запустите `graphify hook install`, чтобы обновить встроенный путь.

> **Строгий режим (Claude Code):** `graphify install --project --strict` заставляет ассистента действительно использовать граф. Установка по умолчанию лишь *подталкивает* его выполнить `graphify query` перед чтением файлов; строгий режим *блокирует* первое чтение исходного кода «напрямую» за сессию и перенаправляет его на граф, а затем возвращается к обычному подталкиванию (так что срабатывает не более одного раза за сессию и никогда не застревает). Переключается во время выполнения через `GRAPHIFY_HOOK_STRICT=1`/`0`; поведение установки по умолчанию (мягкое подталкивание) не меняется.

<details>
<summary><b>Выберите свою платформу</b> (20+ ассистентов, нажмите, чтобы развернуть)</summary>

| Платформа | Команда установки |
|----------|----------------|
| Claude Code (Linux/Mac) | `graphify install` |
| Claude Code (Windows) | `graphify install` (автоопределяется) или `graphify install --platform windows` |
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
| Agent Skills (межплатформенно) | `graphify install --platform agents` (алиас `--platform skills`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify install --platform pi` |
| Cursor | `graphify cursor install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

Пользователям Codex также нужно установить `multi_agent = true` в секции `[features]` файла `~/.codex/config.toml` для параллельного извлечения. CodeBuddy использует тот же механизм Agent tool и хука PreToolUse, что и Claude Code. Factory Droid использует инструмент `Task` для параллельного запуска сабагентов. OpenClaw и Aider используют последовательное извлечение (поддержка параллельных агентов на этих платформах пока на раннем этапе). Trae использует Agent tool для параллельного запуска сабагентов и **не** поддерживает хуки `PreToolUse`, поэтому AGENTS.md — это постоянно работающий механизм.

`--platform agents` (алиас `--platform skills`) предназначен для универсальных межплатформенных расположений [Agent-Skills](https://github.com/anthropics/skills): пользовательский глобальный `~/.agents/skills/` из спецификации (читается `npx skills` и фреймворками, соответствующими спецификации) — для глобальной установки, и `./.agents/skills/` — для установки в проект (`--project`). Обычная команда `graphify install` намеренно остаётся однoплатформенной (Claude Code) — используйте именованную платформу `agents`, когда хотите, чтобы навык был доступен для обнаружения любым фреймворком, читающим `.agents/skills`.

> В Codex используется `$graphify` вместо `/graphify`.

</details>

<details>
<summary><b>Дополнительные модули</b> (устанавливайте только то, что нужно)</summary>

| Модуль | Что добавляет | Установка |
|---|---|---|
| `pdf` | Извлечение из PDF | `uv tool install "graphifyy[pdf]"` |
| `office` | Поддержка `.docx` и `.xlsx` | `uv tool install "graphifyy[office]"` |
| `google` | Отрисовка Google Sheets | `uv tool install "graphifyy[google]"` |
| `video` | Транскрипция видео/аудио (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | MCP stdio-сервер | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Поддержка выгрузки в Neo4j | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | Поддержка выгрузки в FalkorDB | `uv tool install "graphifyy[falkordb]"` |
| `svg` | Экспорт графа в SVG | `uv tool install "graphifyy[svg]"` |
| `leiden` | Определение сообществ Leiden (только Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Локальный инференс через Ollama | `uv tool install "graphifyy[ollama]"` |
| `openai` | OpenAI / совместимые с OpenAI API | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic Claude API (`--backend claude`, использует `ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (использует IAM, без API-ключа) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, использует `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "graphifyy[openai]"` |
| `sql` | Извлечение схемы SQL | `uv tool install "graphifyy[sql]"` |
| `postgres` | Живая интроспекция PostgreSQL (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | Извлечение AST BYOND DreamMaker `.dm`/`.dme` (может потребоваться C-компилятор + `python3-dev`, если под вашу платформу нет готового wheel) | `uv tool install "graphifyy[dm]"` |
| `terraform` | Извлечение AST Terraform / HCL `.tf`/`.tfvars`/`.hcl` | `uv tool install "graphifyy[terraform]"` |
| `pascal` | Извлечение AST Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` (более точные рёбра `calls`/`inherits`; при отсутствии используется регекс-экстрактор) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | Сегментация запросов на китайском (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | Всё вышеперечисленное | `uv tool install "graphifyy[all]"` |

</details>

---

## Чтобы ассистент всегда использовал граф

Выполните это один раз в вашем проекте после построения графа:

| Платформа | Команда |
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
| Agent Skills (межплатформенно) | `graphify agents install` (алиас `graphify skills install`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify pi install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

Это записывает небольшой конфигурационный файл, который указывает вашему ассистенту обращаться к графу знаний по вопросам о кодовой базе, предпочитая точечные запросы вроде `graphify query "<question>"` чтению полного отчёта или grep по исходным файлам.

- **Платформы с хуками** (Claude Code, Gemini CLI): хук автоматически срабатывает перед вызовами инструментов поиска (а в Claude Code — также перед чтением исходных файлов по одному через инструменты Read/Glob) и подталкивает вашего ассистента к пути через граф.
- **Платформы с файлами инструкций** (Codex, OpenCode, Cursor и др.): постоянные файлы инструкций (`AGENTS.md`, `.cursor/rules/` и т. п.) дают ту же рекомендацию — сначала запрос к графу.

`GRAPH_REPORT.md` остаётся доступным для широкого обзора архитектуры.

**CodeBuddy** делает то же, что и Claude Code: записывает секцию в `CODEBUDDY.md`, указывающую CodeBuddy читать `graphify-out/GRAPH_REPORT.md` перед ответом на архитектурные вопросы, и устанавливает хуки `PreToolUse` (`.codebuddy/settings.json`), которые срабатывают перед bash-командами поиска и чтением файлов, подталкивая к `graphify query`.

**Codex** записывает в `AGENTS.md`, который на этой платформе фактически несёт постоянно действующую рекомендацию по графу. `graphify codex install` также регистрирует хук `PreToolUse` в `.codex/hooks.json` (`graphify hook-check`), но эта запись намеренно является **no-op**: Codex Desktop отвергает `hookSpecificOutput.additionalContext` в `PreToolUse`, поэтому подталкивание там сломало бы вызовы bash-инструмента. В отличие от Claude Code, где подталкивание делает хук (`graphify hook-guard`), в Codex хук срабатывает и намеренно ничего не делает, а `AGENTS.md` — постоянно действующий механизм.

**Kilo Code** устанавливает навык Graphify в `~/.config/kilo/skills/graphify/SKILL.md` и нативную команду `/graphify` в `~/.config/kilo/command/graphify.md`. `graphify kilo install` также записывает `AGENTS.md` плюс нативный плагин `tool.execute.before` (`.kilo/plugins/graphify.js` + регистрация в `.kilo/kilo.json` или `.kilo/kilo.jsonc`), так что Kilo получает такое же постоянное напоминание о графе через нативную конфигурацию `.kilo`.

**Cursor** записывает `.cursor/rules/graphify.mdc` с `alwaysApply: true`, поэтому Cursor автоматически включает его в каждый разговор без хука.

Чтобы удалить graphify со всех платформ сразу: `graphify uninstall` (добавьте `--purge`, чтобы также удалить `graphify-out/`). Либо используйте команду для конкретной платформы (например, `graphify claude uninstall`).

---

## Что входит в отчёт

- **God nodes** — самые связанные понятия в вашем проекте. Всё проходит через них.
- **Неожиданные связи** — связи между вещами, живущими в разных файлах или модулях. Отранжированы по степени неожиданности.
- **«Почему»** — встроенные комментарии (`# NOTE:`, `# WHY:`, `# HACK:`), docstring'и и обоснование дизайна из документации извлекаются как отдельные узлы, связанные с кодом, который они объясняют.
- **Предлагаемые вопросы** — 4–5 вопросов, на которые граф способен ответить уникальным образом.
- **Теги уверенности** — каждая выведенная связь помечена как `EXTRACTED`, `INFERRED` или `AMBIGUOUS`. Вы всегда знаете, что было найдено, а что — предположено.

---

## Какие файлы поддерживаются

| Тип | Расширения |
|------|-----------|
| Код (36 грамматик tree-sitter) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme` требует `uv tool install graphifyy[dm]`; `.mts`/`.cts` используют грамматику TypeScript, `.cc`/`.cxx`, а также CUDA `.cu`/`.cuh` и Metal `.metal` используют грамматику C++) |
| Salesforce Apex | `.cls .trigger` (на основе регулярных выражений; классы, интерфейсы, перечисления, методы, триггеры, рёбра SOQL/DML) |
| Terraform / HCL | `.tf .tfvars .hcl` (требует `uv tool install graphifyy[terraform]`) |
| Конфигурации MCP | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — извлекает узлы серверов, ссылки на пакеты, требования к переменным окружения |
| Манифесты пакетов | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — один канонический узел пакета на пакет (по имени) плюс рёбра `depends_on`, так что пакет, на который ссылаются из многих манифестов, — это единый хаб |
| Документы | `.md .mdx .qmd .html .txt .rst .yaml .yml` (markdown-ссылки `[text](./other.md)` и `[[wikilinks]]` становятся рёбрами `references` между документами) |
| Office | `.docx .xlsx` (требует `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (по желанию; требует авторизации `gws` и `--google-workspace`; для Sheets нужен `uv tool install graphifyy[google]`) |
| PDF | `.pdf` |
| Изображения | `.png .jpg .webp .gif` |
| Видео / Аудио | `.mp4 .mov .mp3 .wav` и другие (требует `uv tool install graphifyy[video]`) |
| YouTube / URL | любой URL видео (требует `uv tool install graphifyy[video]`) |

Код извлекается **локально, без вызовов API** (AST через tree-sitter). Всё остальное проходит через API модели вашего AI-ассистента.

Файлы `.gdoc`, `.gsheet` и `.gslides` из Google Drive для компьютеров — это ярлыки-указатели, а не содержимое документа. Чтобы включить нативные Google Документы, Таблицы и Презентации
в headless-извлечение, установите и авторизуйте
[`gws` CLI](https://github.com/googleworkspace/cli), затем выполните:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

Также можно установить `GRAPHIFY_GOOGLE_WORKSPACE=1`. Graphify экспортирует ярлыки в
`graphify-out/converted/` в виде Markdown-сайдкаров, а затем извлекает эти файлы.

---

## Часто используемые команды

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

См. раздел [Decouple: кандидаты на Extract Class с оценкой риска](#decouple-кандидаты-на-extract-class-с-оценкой-риска) выше или [полный список команд](#полный-список-команд) ниже.

---

## Игнорирование файлов

Создайте `.graphifyignore` в корне проекта — синтаксис такой же, как у `.gitignore`, включая отрицание `!`.

**`.gitignore` учитывается автоматически.** graphify читает `.gitignore` в каждом каталоге. Если также присутствует `.graphifyignore`, они **объединяются** — паттерны `.graphifyignore` применяются последними, поэтому при конфликте (включая отрицания `!`) побеждают они. Добавление `.graphifyignore` может только увеличить число исключений; оно никогда не включит обратно файл, который уже исключён вашим `.gitignore`. Область действия для подкаталогов работает так же, как в git — файл игнорирования влияет только на своё собственное поддерево.

Передайте `--no-gitignore` команде `graphify extract`, если сгенерированный или транспилированный код, игнорируемый git, должен быть в графе. Это отключает `.gitignore` и `.git/info/exclude`; `.graphifyignore` продолжает применяться.

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

## Настройка для командной работы

`graphify-out/` предполагается коммитить в git, чтобы у всей команды с самого начала была карта проекта.

**Рекомендуемые добавления в `.gitignore`:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` теперь переносим — ключи хранятся как относительные пути и перепривязываются при загрузке, поэтому коммитить его безопасно, и это избавляет от полной пересборки при первом чекауте.

**Процесс:**
1. Один человек запускает `/graphify .` и коммитит `graphify-out/`.
2. Все остальные делают pull — их ассистент сразу же читает граф.
3. Запустите `graphify hook install`, чтобы автоматически пересобирать граф после каждого коммита (только AST, без затрат на API). Это также настраивает git merge driver, поэтому `graph.json` никогда не остаётся с маркерами конфликта — если два разработчика коммитят параллельно, их графы автоматически объединяются через union-merge.
4. Когда документация или статьи меняются, запустите `/graphify --update`, чтобы обновить эти узлы.

---

## Прямое использование графа

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

MCP-сервер даёт вашему ассистенту структурированный доступ: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Общий HTTP-сервер

`--transport stdio` (по умолчанию) запускает по одному локальному серверу на каждого разработчика. `--transport http` предоставляет те же инструменты через транспорт MCP Streamable HTTP, так что единый общий процесс может обслуживать граф для всей команды — клиенты указывают в конфигурации MCP своей IDE адрес `http://<host>:8080/mcp` вместо локального запуска graphify.

| Флаг | По умолчанию | Назначение |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Транспорт для обслуживания |
| `--host` | `127.0.0.1` | Хост привязки HTTP (используйте `0.0.0.0`, чтобы открыть доступ за пределы localhost) |
| `--port` | `8080` | Порт привязки HTTP |
| `--api-key` | переменная окружения `GRAPHIFY_API_KEY` | Требовать `Authorization: Bearer <key>` (или `X-API-Key`) |
| `--path` | `/mcp` | Путь монтирования HTTP |
| `--json-response` | выкл | Возвращать обычный JSON вместо потоков SSE |
| `--stateless` | выкл | Без состояния на сессию (для балансировки нагрузки / CI) |
| `--session-timeout` | `3600` | Удалять неактивные сессии с состоянием после N секунд (`0` отключает) |

Привязка по умолчанию к `127.0.0.1` — только для loopback. Устанавливайте `--host 0.0.0.0` **и** `--api-key` одновременно при публикации на общем хосте. Запуск в контейнере:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **Заметка про WSL / Linux:** Ubuntu поставляется с `python3`, а не с `python`. Используйте venv, чтобы избежать конфликтов:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## Переменные окружения

Они нужны только для **headless-извлечения / извлечения в CI** (`graphify extract`). При запуске через навык `/graphify` внутри вашей IDE API модели предоставляется сессией IDE — дополнительные ключи не нужны.

| Переменная | Используется для | Когда требуется |
|---|---|---|
| `ANTHROPIC_API_KEY` | Backend Claude (Anthropic) | `--backend claude` |
| `ANTHROPIC_BASE_URL` | URL эндпоинта, совместимого с Anthropic (proxy LiteLLM, гейтвеи, ...) | `--backend claude` (по умолчанию: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Имя модели для backend'а Claude — для кастомных эндпоинтов используйте имя/алиас модели, который предоставляет ваш сервер | `--backend claude` (по умолчанию: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` или `GOOGLE_API_KEY` | Backend Google Gemini | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI или совместимые с OpenAI API | `--backend openai` (локальные серверы принимают любое непустое значение) |
| `OPENAI_BASE_URL` | URL сервера, совместимого с OpenAI (llama.cpp, vLLM, LM Studio, ...) | `--backend openai` (по умолчанию: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | Имя модели для backend'а OpenAI — для self-hosted серверов используйте имя/алиас модели, который предоставляет ваш сервер (проверьте его эндпоинт `/v1/models`), например `LFM2.5-8B-A1B-UD-Q4_K_XL` для llama.cpp | `--backend openai` (по умолчанию: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | Backend DeepSeek | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Backend Kimi Code | `--backend kimi` |
| `OLLAMA_BASE_URL` | URL локального инференса Ollama | `--backend ollama` (по умолчанию: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Имя модели Ollama | `--backend ollama` (по умолчанию: автоопределение) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Переопределить размер окна KV-кэша Ollama | опционально — по умолчанию подбирается автоматически |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Сколько минут держать модель Ollama загруженной | опционально — установите `0`, чтобы выгружать после каждого чанка |
| `AZURE_OPENAI_API_KEY` | Backend Azure OpenAI Service | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | URL эндпоинта ресурса Azure | `--backend azure` (требуется вместе с API-ключом) |
| `AZURE_OPENAI_API_VERSION` | Переопределение версии API Azure | опционально — по умолчанию `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` или `GRAPHIFY_AZURE_MODEL` | Имя деплоймента Azure | опционально — по умолчанию `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — стандартная цепочка учётных данных | `--backend bedrock` (без API-ключа, использует IAM) |
| `GRAPHIFY_MAX_WORKERS` | Количество потоков для параллелизма AST | опционально — также флаг `--max-workers` |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Поднять лимит вывода для плотных корпусов | опционально — например `32768` для больших файлов |
| `GRAPHIFY_API_TIMEOUT` | Таймаут на вызов в секундах для backend'ов HTTP, claude-cli, Anthropic SDK и Bedrock (по умолчанию: 600) | опционально — также флаг `--api-timeout` |
| `GRAPHIFY_MAX_RETRIES` | Сколько раз повторять запрос с ограничением скорости (429), прежде чем сдаться (по умолчанию: 6; учитывает `Retry-After`) | опционально — увеличивайте для строгих лимитов по организации (например, kimi); `0` отключает |
| `GRAPHIFY_FORCE` | Принудительно пересобрать граф даже с меньшим числом узлов | опционально — также флаг `--force` |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Автоматически включить экспорт Google Workspace | опционально — установите `1` |
| `GRAPHIFY_TRIAGE_BACKEND` | Backend для `graphify prs --triage` | опционально — автоопределяется по доступным ключам |
| `GRAPHIFY_TRIAGE_MODEL` | Переопределение модели для triage | опционально — например `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | Установите `1`, чтобы включить локальный лог запросов в `~/.cache/graphify-queries.log` (фиксирует каждый вопрос query/path/explain + путь к корпусу). По умолчанию выключено — ничего не записывается, если вы не включили это явно (#1797) | опционально |
| `GRAPHIFY_QUERY_LOG` | Включить лог запросов и записывать его по этому пути вместо стандартного | опционально — выключено, если не задано это или `_ENABLE` |
| `GRAPHIFY_QUERY_LOG_DISABLE` | Установите `1`, чтобы принудительно выключить лог запросов (приоритетнее переменных включения) | опционально |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | Когда лог включён, также записывать полные ответы подграфов (по умолчанию выключено) | опционально |
| `GRAPHIFY_MAX_GRAPH_BYTES` | Переопределить лимит размера graph.json в 512 МиБ — например `700MB`, `2GB` или просто байты | опционально — полезно для очень больших корпусов |
| `GRAPHIFY_MAX_CONTEXTS` | Максимальное число неосновных графов проектов, которые хранит один multi-project MCP-сервер | опционально — по умолчанию: `8`; неверные значения используют `8`, значения меньше `1` используют `1` |
| `GRAPHIFY_LLM_TEMPERATURE` | Переопределить температуру LLM для семантического извлечения — например `0.7`, или `none`, чтобы не задавать | опционально — автоматически не задаётся для reasoning-моделей o1/o3/o4/gpt-5 |

---

## Конфиденциальность

- **Файлы кода** — обрабатываются локально через tree-sitter. Ничего не уходит с вашей машины. Корпус, состоящий только из кода, не требует API-ключа — `graphify extract` работает полностью офлайн. В смешанном репозитории добавьте `--code-only`, чтобы индексировать только код и пропустить документы/PDF/изображения, для которых иначе понадобился бы LLM.
- **Видео / аудио** — транскрибируются локально с помощью faster-whisper. Ничего не уходит с вашей машины.
- **Документы, PDF, изображения** — отправляются вашему AI-ассистенту для семантического извлечения (через навык `/graphify`, с использованием той модели, которую запускает ваша сессия IDE). Headless-режим `graphify extract` требует `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), запущенный экземпляр Ollama (`OLLAMA_BASE_URL`), учётные данные AWS через стандартную цепочку провайдеров (Bedrock — API-ключ не нужен, использует IAM) либо бинарник CLI `claude` (Claude Code — API-ключ не нужен, использует вашу подписку Claude). Флаг `--dedup-llm` использует тот же ключ.
- **Резидентность данных** — `graphify extract` автоматически определяет, какого провайдера использовать, по тому, какой API-ключ задан (приоритет: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). Для кода с требованиями к резидентности данных используйте `--backend ollama` (полностью локально) либо укажите явный флаг `--backend`. Kimi (`MOONSHOT_API_KEY`) направляет запросы на серверы Moonshot AI в Китае.
- **Без телеметрии**, без отслеживания использования, без аналитики.
- **Логирование запросов** — каждый вызов `graphify query`, `graphify path`, `graphify explain` и MCP `query_graph` записывается в `~/.cache/graphify-queries.log` в формате JSON Lines (метка времени, вопрос, корпус, число возвращённых узлов, длительность). Полные ответы подграфов по умолчанию **не** сохраняются. Установите `GRAPHIFY_QUERY_LOG_DISABLE=1`, чтобы отказаться, либо `GRAPHIFY_QUERY_LOG=/dev/null`, чтобы заглушить лог без отключения самого кода.

---

## Ограничения и границы применимости

Что graphify намеренно **не** делает и где заканчивается его покрытие:

- **Это не семантический/векторный поисковый движок.** Граф структурный — узлы и типизированные рёбра, полученные из исходного кода, а не эмбеддинги. `graphify query`/`path`/`explain` обходят эту структуру; они не могут показать связь, которая не представлена как ребро, даже если она «семантически» связана. Резервного механизма поиска по схожести/ближайшим соседям нет.
- **Документы, PDF, изображения и headless-извлечение видео/URL работают не только локально.** Полностью офлайн работают только код (AST через tree-sitter) и транскрипция аудио/видео (faster-whisper). Извлечение документов/PDF/изображений всегда вызывает LLM — модель вашего AI-ассистента через навык `/graphify`, либо настроенный API-ключ бэкенда для headless-режима `graphify extract`. Точный список того, какой флаг или ключ нужен для каждого пути, см. в разделе [Конфиденциальность](#конфиденциальность) выше.
- **Проверка совместного использования состояния в decouple охватывает не все языки.** У C нет надёжного сигнала `self`/`this` без полного вывода типов, поэтому он исключён (см. [таблицу покрытия языков](#decouple-кандидаты-на-extract-class-с-оценкой-риска) выше). God-узел на неподдерживаемом языке или тот, чей исходный код не удаётся прочитать, откатывается к оценке только по графу вызовов (`state_analysis: "skipped"`), а не к проверенной проверке состояния.
- **3D-показатель глубины потока данных (data-flow floor) — это эвристика по именам, а не анализ потока данных/taint-анализ.** Определение границ ввода-вывода в `data_floor` (парсеры, загрузчики, читатели, писатели, клиенты БД/HTTP) основано на соглашениях об именовании (`boundary_reason`); граничный узел с нестандартным именем может быть пропущен, из-за чего глубина остальной части графа занижается.
- **Теги уверенности — это собственная уверенность graphify в разрешении связи, а не абсолютная истина.** Рёбра `INFERRED` и `AMBIGUOUS` — это разрешения по принципу «лучшее из возможного», и они всё ещё могут быть ошибочными, особенно для сильно динамических идиом (рефлексия, диспетчеризация во время выполнения, метапрограммирование), которые ни один статический AST-проход не может разрешить полностью.
- **И HTML-визуализация, и размер графа имеют потолок.** `graph.html` / `DECOUPLE.html` по умолчанию пропускают генерацию при более чем 5000 узлов (`MAX_NODES_FOR_VIZ`, повышается через `GRAPHIFY_VIZ_NODE_LIMIT`); сам `graph.json` ограничен 512 МиБ (переопределяется через `GRAPHIFY_MAX_GRAPH_BYTES`). Для корпусов, превышающих любой из этих пределов, используйте `--no-viz` вместе с `query`/`path`/`explain`.
- **Осведомлённость о нескольких проектах включается вручную, а не автоматически.** `graphify query` видит только тот единственный граф, на который вы указали. Вопросы, охватывающие несколько репозиториев, требуют явной регистрации каждого проекта в общем графе (`graphify global add`, не более `GRAPHIFY_MAX_CONTEXTS` нестандартных контекстов на MCP-сервер) — graphify никогда не сканирует вашу машину в поисках других репозиториев самостоятельно.
- **Параллельное извлечение несколькими агентами зависит от платформы.** Для этого нужна поддержка запуска субагентов на стороне ассистента (`multi_agent = true` в `~/.codex/config.toml` для Codex, инструмент Agent/Task в Claude Code/CodeBuddy/Factory Droid/Trae). OpenClaw и Aider пока извлекают только последовательно.
- **Общий MCP HTTP-сервер по умолчанию слушает только loopback.** Чтобы обратиться к нему с другой машины, требуется явно указать `--host 0.0.0.0` **и** `--api-key`; graphify не управляет TLS и какой-либо аутентификацией, кроме этого единственного bearer-токена.
- **PowerShell воспринимает ведущий `/` как разделитель пути.** Поэтому `/graphify .` не работает в Windows PowerShell — это не баг graphify — вместо этого используйте `graphify .`.

---

## Устранение неполадок

**После установки `graphify: command not found`**
CLI установлен, но его bin-каталог не в `PATH` вашего шелла. Выберите решение по способу установки:
- **uv** (`uv tool install graphifyy`): команда попадает в bin-каталог инструментов uv (`~/.local/bin`), которого часто нет в `PATH` на свежей установке macOS/zsh. Выполните `uv tool update-shell`, затем откройте новый терминал. (Найти каталог можно через `uv tool dir --bin`.)
- **pipx** (`pipx install graphifyy`): выполните `pipx ensurepath`, затем откройте новый терминал.
- **pip** (`pip install graphifyy`): pip устанавливает скрипты в пользовательский bin-каталог, который может быть не в `PATH` — добавьте `~/Library/Python/3.x/bin` (macOS) или `~/.local/bin` (Linux) в `PATH` в `~/.zshrc`/`~/.bashrc`, либо просто запустите `python -m graphify`.

**`uvx graphify …` или `uv tool run graphify …` не может разрешить `graphify`**
Пакет PyPI называется `graphifyy`; `graphify` — лишь команда, которую он предоставляет. `uv tool run` трактует первое слово как *имя пакета*, поэтому ищет пакет с именем `graphify` и выдаёт `No solution found … no versions of graphify`. Укажите имя пакета явно: `uvx --from graphifyy graphify install` (то же, что `uv tool run --from graphifyy graphify install`). Либо один раз выполните `uv tool install graphifyy`, а затем вызывайте `graphify` напрямую.

**`uv run --with graphifyy python -m graphify` молча запускает более старую установку**
`uv run` использует *системный* Python, поэтому если там же живёт более старая `graphifyy` (например, из прошлого `pip install graphifyy`), Python может найти именно её первой в `sys.path`, и `--with graphifyy` не сможет её переопределить. Запуск проходит без ошибок, но вы получаете поведение *старой* версии — например, переопределения через переменные окружения, такие как `OPENAI_BASE_URL`, молча игнорируются, поэтому запросы идут на эндпоинт по умолчанию и падают с 401, похожей на неверный ключ. Характерный признак — строка `warning: skill is from graphify <newer>, package is <older>` — это значит, что загрузилась другая установка, а не просто устаревший навык. Проверьте, какая копия загрузилась на самом деле:
```bash
python -c "import graphify; print(graphify.__file__)"
```
Затем запускайте установленную команду напрямую (она использует копию, управляемую uv), либо удалите устаревшую системную копию:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` работает, а команда `graphify` — нет**
`PATH` вашего шелла не включает bin-каталог, куда была установлена команда. Предпочитайте `uv tool install` / `pipx install` обычному `pip`, затем выполните `uv tool update-shell` / `pipx ensurepath` и откройте новый терминал (см. заметки об установке выше).

**`/graphify .` вызывает "path not recognized" в PowerShell**
PowerShell трактует ведущий `/` как разделитель пути. На Windows используйте `graphify .` (без слэша).

**После `--update` или пересборки в графе меньше узлов**
Если рефакторинг удалил файлы, старые узлы остаются. Передайте `--force` (или установите `GRAPHIFY_FORCE=1`), чтобы перезаписать граф даже когда пересборка даёт меньше узлов.

**`extract` завершается с "extraction was incomplete ... refusing to overwrite"**
Когда проход извлечения аварийно завершается или обход не может полностью прочитать корпус, результат оказывается меньше полного, поэтому `graphify extract` отказывается перезаписывать больший существующий граф частичным результатом (это защищает ваш `graph.json`). Устраните причину сбоя и запустите заново, либо передайте `--allow-partial`, чтобы перезаписать в любом случае.

**В графе есть дублирующиеся узлы для одной и той же сущности (призрачные дубликаты)**
Призрачные дубликаты (один и тот же символ появляется дважды — один раз из AST-извлечения с расположением в исходнике, второй раз из семантического извлечения без него) теперь автоматически объединяются во время сборки. Если вы видите это в графе, собранном до v0.8.33, выполните полное повторное извлечение, чтобы всё почистить:
```bash
graphify extract . --force
```

**У Ollama не хватает VRAM / превышено окно контекста**
Окно KV-кэша подбирается автоматически, но может быть слишком большим для вашего GPU. Уменьшите его:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**Предупреждения `LLM returned invalid JSON` / `Unterminated string`**
Ответ модели в формате JSON достиг лимита выходных токенов и был обрезан посреди строки. graphify восстанавливается автоматически (он разбивает чанк и повторно извлекает обе половины, а слишком большой единый документ сначала разрезается по границам заголовков/абзацев, чтобы весь файл всё равно был покрыт), так что эти предупреждения — шум, но не потеря данных. Чтобы уменьшить количество таких случаев, поднимите лимит вывода или уменьшите вывод для каждого чанка:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
С облачным гейтвеем вроде OpenRouter предпочитайте `--backend openai` (установив `OPENAI_BASE_URL`) вместо прокладки через Ollama — это более чистый путь, совместимый с OpenAI. Если у модели есть собственный потолок максимального вывода, снижение `--token-budget` — надёжный рычаг.

**HTML графа слишком большой, чтобы открыть в браузере (>5000 узлов)**
Пропустите генерацию HTML и используйте JSON напрямую:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**В `graph.json` появляются маркеры конфликта, когда два разработчика коммитят одновременно**
Запустите `graphify hook install` — он настраивает git merge driver, который автоматически объединяет `graph.json` через union-merge, так что конфликтов не возникает вовсе.

**Извлечение возвращает пустые узлы/рёбра для документов или PDF**
Документы, PDF и изображения требуют вызова LLM — корпусам, состоящим только из кода, ключ не нужен. Проверьте, что API-ключ задан и backend указан верно:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**Предупреждение о несовпадении версий навыка в вашей IDE**
Установленная версия graphify отличается от версии файла навыка. Обновите:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**Кэш промптов Claude Code сбрасывается после каждого `graphify extract`**
Graphify записывает выходные файлы (`graph.json`, `graphify-out/`) в рабочее пространство. Если эти пути не игнорируются, каждая запись сбрасывает кэш промптов Claude Code, вынуждая полную повторную загрузку по ставкам записи в кэш на следующем ходе. Добавьте их в `.claudeignore`:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## Полный список команд

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

> **Имена сообществ:** внутри агента (Claude Code, Gemini CLI) сам агент называет сообщества. При запуске обычного CLI `cluster-only` автоматически называет их с помощью настроенного backend'а (встроенного или кастомного провайдера, совместимого с OpenAI) — передайте `--no-label`, чтобы оставить `Community N`, либо запустите `graphify label`, чтобы (пере)сгенерировать имена по требованию.

---

## Узнать больше

- [Как это работает](../how-it-works.md) — конвейер извлечения, определение сообществ, оценка уверенности, бенчмарки
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — разбивка по модулям, как добавить язык
- [Дополнительные интеграции](../docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — книга об идеях, стоящих за graphify, и архитектуре от начала до конца

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) — это постоянно работающий слой, построенный над graphify: он применяет тот же подход на основе графа ко всему вашему рабочему контексту — встречам, файлам, документам и коду, непрерывно обновляясь в фоне.

Создан для людей и команд, чья работа охватывает сотни разговоров и документов, которые они никогда не смогут полностью восстановить в памяти.

**[Присоединяйтесь к списку ожидания на graphify.com](https://graphify.com).** Бесплатный пробный период скоро запускается.

---

<details>
<summary>Вклад в проект</summary>

### Настройка окружения разработки

Проект использует [uv](https://docs.astral.sh/uv/) для рабочего процесса разработки. Установите его один раз, затем:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

Проверьте editable-установку:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### Запуск тестов

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> Заметка про macOS: набор тестов включает и фикстуру `sample.f90`, и фикстуру `sample.F90`. Они конфликтуют на файловых системах HFS+ / APFS без учёта регистра. Если нужно одновременно протестировать оба варианта Fortran, запускайте на Linux или в Docker-контейнере.

### Процесс работы с Git

- Активная разработка ведётся в ветке `v8`.
- Стиль коммитов: `fix: <description>` / `feat: <description>` / `docs: <description>`
- Перед открытием PR запустите `uv run pytest tests/ -q` и убедитесь, что тесты проходят.
- Добавьте файл фикстуры в `tests/fixtures/` и тесты в `tests/test_languages.py` для любого нового экстрактора языка.

### Что можно предложить

**Разобранные примеры (worked examples)** — самый полезный вклад. Запустите `/graphify` на реальном корпусе, сохраните вывод в `worked/{slug}/`, напишите честный `review.md`, описывающий, что граф понял правильно, а что — неправильно, и откройте PR.

**Ошибки извлечения** — откройте issue с входным файлом, записью кэша (`graphify-out/cache/`) и тем, что было упущено или неверно.

См. [ARCHITECTURE.md](../../ARCHITECTURE.md) о зонах ответственности модулей и о том, как добавить язык.

</details>
