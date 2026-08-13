<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>Форк <a href="https://github.com/Graphify-Labs/graphify">graphify</a>, який додає <code>graphify decouple</code></b> — 0-LLM, ризик-оцінені кандидати Extract-Class для god-об'єктів, повторно перевірені на основі фактичного вихідного коду (а не лише графа викликів), перш ніж щось рекомендувати. Див. <a href="#decouple-кандидати-extract-class-з-оцінкою-ризику">Decouple: кандидати Extract-Class з оцінкою ризику</a> нижче.
</p>

<div align="center">
<details><summary><b>Читати цією мовою</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>Ранній доступ до платформи graphify відкритий ще до публічного релізу v1: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

Введіть `/graphify` у своєму ШІ-асистенті для кодингу — і він нанесе весь ваш проєкт (код, документи, PDF, зображення, відео) на **граф знань**, який можна **запитувати замість того, щоб грепати** файли.

- **Карти коду безкоштовно і повністю локально.** Код розбирається через AST tree-sitter: детерміновано, без LLM, нічого не залишає вашу машину. (Документи, PDF, зображення та відео проходять семантичний аналіз через модель вашого асистента або налаштований API-ключ.)
- **Кожен зв'язок пояснено.** Кожне з'єднання позначене як `EXTRACTED` (явно присутнє в коді) або `INFERRED` (виведене graphify), тож завжди видно, що прочитано напряму, а що — виведено логічно.
- **Це не векторний індекс.** Без embeddings, без vector store: справжній граф, який можна обходити. Поставте запитання, простежте шлях між двома сутностями або поясніть одне поняття.

> Хочете, щоб це працювало завжди — оновлюючись у фоні для коду, документів і зустрічей, а не лише за запитом? Саме це ми будуємо у **[graphify.com](https://graphify.com)**, і ранній доступ уже відкрито на **[app.graphify.com](https://app.graphify.com/login)**.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="Інтерактивний graph.html від graphify: кодову базу FastAPI показано як силовий граф знань із легендою виявлених спільнот" width="900">
</p>
<p align="center">
  <em>Кодова база FastAPI, нанесена на граф за допомогою graphify. Кожен вузол — це концепт, кольори — виявлені спільноти, і все це можна клікати в graph.html.</em>
</p>

**Початок роботи** (30 секунд):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

Далі, у своєму ШІ-асистенті:

```
/graphify .
```

Ось і все. Ви отримуєте **три файли**:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**Працює в** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot та ще 15+ середовищах — [оберіть свою платформу](#встановлення).

---

## Побачити в дії

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="Запит шляху в graphify: у терміналі запитують найкоротший шлях між FastAPI та ModelField, і відповідь підсвічується крок за кроком на графі знань" width="900">
</p>

Коли граф побудовано, ви запитуєте його замість того, щоб читати файли. Реальний вивід — graphify, запущений на кодовій базі FastAPI, показаній вище:

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

Кожен зв'язок несе **тег довіри** (`EXTRACTED` = явно присутній у коді, `INFERRED` = виведений через розв'язання зв'язків), тож завжди видно, що прочитано напряму, а що — виведено логічно. `graphify query "<question>"` повертає обмежений підграф для питання звичайною мовою, а `graphify path A B` простежує, як пов'язані будь-які дві сутності.

---

## Decouple: кандидати Extract-Class з оцінкою ризику

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: god-вузол MainWindow розбивається на кандидатів-класів з оцінкою ризику, з попередженням про спільний стан між двома з них" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: 5 запропонованих класів для MainWindow, відкрита панель Node Info на Main Window Axis and Range Controls показує перетин стану 0.608 з Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>DECOUPLE.html на реальному запуску (AutoCheck/Touchstone Explorer) — клік на запропонованому класі показує, з яким саме іншим класом він спільно використовує стан і що конкретно є спільним.</em>
</p>

`graphify decouple` знаходить god-об'єкти і каже, чи справді варто їх розбивати — а не просто те, що вони великі.

Помилка, яку це покликане відловити: клас із 47 методами, який кластеризація за графом викликів охоче розбиває на 5 охайних на вигляд груп, — але всі вони під капотом продовжують читати й писати той самий стан екземпляра `self._chart_style` / `self._crosshair`. Якщо випустити такий поділ у продакшн, ви нічого не роз'єднали — ви просто перенесли методи в нові файли, які досі неможливо тестувати, змінювати чи розуміти окремо, бо всім їм досі потрібен той самий спільний стан, переданий назад. Інструмент, який дивиться лише на граф викликів, узагалі не здатен це побачити — доводиться повертатися до фактичного вихідного коду.

**Дві перевірки, обидві 0-LLM, обидві детерміновані:**

1. **Це взагалі god-об'єкт?** Вузол із високим degree може бути справжнім god-об'єктом (багато ВЛАСНИХ методів, розкиданих по непов'язаних відповідальностях — Extract Class підходить) або надто активно референсованим хабом/моделлю даних (мало власних методів, переважно *вхідні* посилання — розбиття його тіла нічого не дає; виправлення полягає у звуженні інтерфейсу, а не у виокремленні класу). `classify_god_node` розрізняє їх за `member_ratio`, а не за сирим degree — саме ця відмінність не дає `TraceSource` (84 зв'язки, але лише 6 власних методів) отримати помилкову пропозицію розбиття, тоді як `MainWindow` (88 зв'язків, 47 власних методів) її отримує цілком справедливо.
2. **Чи справді розбиття зменшить зчеплення?** `risk_before` (поточний розмір/зчеплення/фрагментація god-вузла) порівнюється з `risk_after` — НОВИМ ризиком, який внесе саме розбиття: викликами між групами, які раніше були невидимими внутрішньокласовими зв'язками, а стануть явними міжкласовими залежностями; викликаючим кодом, якому тепер доведеться залежати від більш ніж одного нового класу; і — перевіркою, яку граф викликів структурно не здатен виконати — тим, скільки стану екземпляра `self`/`this` (читання, записи та спільні викликі допоміжних методів, зважені окремо: спільний **запис** оцінюється вище, ніж спільне читання) насправді мають спільного запропоновані групи. Це передбачає повторний прямий розбір вихідного файлу самого god-вузла за допомогою tree-sitter; він не покладається на власний видобутий граф graphify, який ніколи не фіксує доступ до полів на рівні жодної мови. Лише коли `risk_after` опускається нижче `risk_before` на величину, що перевищує порогове значення, план рекомендує `split` — інакше це `marginal` або `keep_as_is`, і небажаний кандидат подається як число, а не як фігура на графі, яку потрібно перевіряти оком.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

Виводить три файли поруч із `graph.json`:

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

**Підтримка мов для перевірки спільного стану** (наведена вище класифікація лише за графом викликів працює для будь-якої мови, яку видобуває graphify; ця таблиця стосується саме повторного розбору вихідного коду, що перевіряє перетин стану `self`/`this`):

| Мова | Підтримується | Примітки |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` — окремий вузол AST, а не обгорнутий доступ до поля — обробляється явно |
| C# | ✅ | |
| Rust | ✅ | `self.x` через блоки `impl` |
| Ruby | ✅ | `@x` (домінантна ідіома) + виклики `self.foo` |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | розв'язання ресивера для кожного методу окремо — у Go немає ключового слова `self`/`this`, тож ім'я ресивера (`f` у `func (f *Foo) M()`) розв'язується заново для кожного методу |
| C | ❌ | параметр-вказівник на структуру не має синтаксичного маркера, що відрізняв би його від будь-якого іншого параметра — без повного виведення типів надійного сигналу немає |

God-вузол мовою, яка не підтримується, або той, чий вихідний код неможливо прочитати, позначається як `state_analysis: "skipped"` — класифікація й оцінка за графом викликів усе одно виконуються, але рекомендація ґрунтується лише на графі викликів, а не мовчки припускає, що перевірка стану пройшла успішно.

---

## Що він робить

Що ви отримуєте одразу після встановлення:

| Можливість | Що ви отримуєте |
|---|---|
| **God nodes** | Найбільш пов'язані концепти — видно, через що проходить усе інше |
| **Спільноти** | Граф розбитий на підсистеми (Leiden), з назвами без участі LLM |
| **Міжфайлові зв'язки** | `calls` / `imports` / `inherits` / `mixes_in`, розпізнані у ~40 мовах через AST tree-sitter |
| **Query, path, explain** | Поставте запитання, простежте шлях між двома сутностями або поясніть одне поняття — усе на основі `graph.json` |
| **Обґрунтування + посилання на документи** | Коментарі `# NOTE:` / `# WHY:` та посилання на ADR/RFC стають повноцінними вузлами, пов'язаними з кодом |
| **Не лише код** | Документи, PDF, зображення та відео/аудіо — усе потрапляє в той самий граф |
| **Локально за замовчуванням** | Код розбирається локально через tree-sitter (без LLM, нічого не залишає вашу машину); лише семантичний прохід по документах/медіа звертається до бекенда, і лише якщо ви його налаштували |

---

## Бенчмарки

| Бенчмарк | Метрика | graphify | Інші рішення |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | точність QA | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | точність QA | **76%** | на рівні dense RAG |
| Побудова графа | кредити LLM | **0** | по токенах — у більшості систем |

Усі системи запускалися на одному й тому самому стенді, з однаковою моделлю та однаковими бюджетами, і оцінювалися суддею, чия оцінка була наосліп перевірена другим суддею (збіг 90.6%, каппа Коена 0.81). Повні таблиці по кожній системі, результат для code intelligence та команди для відтворення: **[BENCHMARKS.md](../../BENCHMARKS.md)**.

---

## Вимоги

| Вимога | Мінімум | Перевірка | Встановлення |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(рекомендовано)* | будь-яка версія | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(альтернатива)* | будь-яка версія | `pipx --version` | `pip install pipx` |

**Швидке встановлення на macOS (Homebrew):**
```bash
brew install python@3.12 uv
```

**Швидке встановлення на Windows:**
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

## Встановлення

> **Офіційний пакет:** пакет на PyPI називається `graphifyy` (з подвійним y). Інші пакети `graphify*` на PyPI не пов'язані з цим проєктом. Команда CLI залишається `graphify`.

**Крок 1 — встановити пакет:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**Крок 2 — зареєструвати скіл у вашому ШІ-асистенті:**

```bash
graphify install
```

Ось і все. Відкрийте свого ШІ-асистента і введіть `/graphify .`

Щоб встановити скіл асистента в поточний репозиторій замість профілю
користувача, додайте `--project`:

```bash
graphify install --project
graphify install --project --platform codex
```

Встановлення в межах проєкту записує файли в поточну директорію, наприклад
`.claude/skills/graphify/SKILL.md` або `.agents/skills/graphify/SKILL.md` (плюс
допоміжну папку `references/`, яку скіл підвантажує за потреби), і
виводить підказку `git add` для файлів, які можна закомітити.
Команди для окремих платформ, що підтримують встановлення в межах проєкту, приймають той самий флаг,
наприклад `graphify claude install --project` або `graphify codex install --project`.

> **Примітка щодо PowerShell:** використовуйте `graphify .`, а не `/graphify .` — у PowerShell похилий слеш на початку сприймається як роздільник шляху.

> **`graphify: command not found`?** `uv tool install` / `pipx install` розміщують команду `graphify` у власній bin-директорії інструменту (`~/.local/bin`). Якщо оболонка не знаходить її одразу після встановлення — типово для свіжого macOS + zsh — ця директорія ще не в `PATH`: виконайте `uv tool update-shell` (або `pipx ensurepath`), а потім відкрийте новий термінал. Зі звичайним `pip` додайте `~/.local/bin` (Linux) або `~/Library/Python/3.x/bin` (Mac) у ваш PATH, або запустіть `python -m graphify`.

> **Запускаєте через `uvx` / `uv tool run` замість встановлення?** Вказуйте назву пакета, а не команди: `uvx --from graphifyy graphify install`. Просте `uvx graphify …` не спрацює (`No solution found … no versions of graphify`), бо `uv tool run` читає перше слово як назву *пакета*, а пакет називається `graphifyy` — команда `graphify` живе всередині нього.

> **Уникайте `pip install` на Mac/Windows**, якщо можливо. Скіл визначає Python під час роботи з `graphify-out/.graphify_python`; якщо це вказує на інше середовище, ніж те, куди `pip` встановив пакет, ви отримаєте `ModuleNotFoundError: No module named 'graphify'`. `uv tool install` і `pipx install` ізолюють пакет у власному середовищі й повністю уникають цієї проблеми.

> **Git-хуки та uv tool / pipx:** `graphify hook install` вбудовує шлях до поточного інтерпретатора прямо в скрипти хуків під час встановлення, тож post-commit хук коректно спрацьовує навіть у GUI git-клієнтах і CI-раннерах, де `~/.local/bin` не в PATH. Якщо ви перевстановлюєте або оновлюєте graphify, повторно виконайте `graphify hook install`, щоб оновити вбудований шлях.

> **Строгий режим (Claude Code):** `graphify install --project --strict` змушує асистента дійсно користуватися графом. Стандартне встановлення лише *підштовхує* його виконати `graphify query` перед читанням файлів; строгий режим *блокує* перше пряме читання вихідного коду за сесію і перенаправляє його до графа, а потім повертається до звичайного підштовхування (тож це спрацьовує щонайбільше раз за сесію і ніколи не застрягає). Перемикайте це під час роботи через `GRAPHIFY_HOOK_STRICT=1`/`0`; стандартне встановлення лишається незмінним (м'яке підштовхування).

<details>
<summary><b>Оберіть свою платформу</b> (20+ асистентів, клікніть, щоб розгорнути)</summary>

| Платформа | Команда встановлення |
|----------|----------------|
| Claude Code (Linux/Mac) | `graphify install` |
| Claude Code (Windows) | `graphify install` (визначається автоматично) або `graphify install --platform windows` |
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
| Agent Skills (крос-фреймворкові) | `graphify install --platform agents` (альтернатива `--platform skills`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify install --platform pi` |
| Cursor | `graphify cursor install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

Користувачам Codex також потрібно встановити `multi_agent = true` у розділі `[features]` файлу `~/.codex/config.toml` для паралельного видобування. CodeBuddy використовує той самий інструмент Agent і механізм хука PreToolUse, що й Claude Code. Factory Droid використовує інструмент `Task` для паралельного диспетчеризування субагентів. OpenClaw і Aider використовують послідовне видобування (підтримка паралельних агентів на цих платформах ще на ранній стадії). Trae використовує інструмент Agent для паралельного диспетчеризування субагентів і **не** підтримує хуки `PreToolUse`, тож AGENTS.md є завжди активним механізмом.

`--platform agents` (альтернатива `--platform skills`) орієнтується на загальні крос-фреймворкові розташування [Agent-Skills](https://github.com/anthropics/skills): глобальний для користувача `~/.agents/skills/` за специфікацією (який читають `npx skills` та фреймворки, що відповідають специфікації) для глобального встановлення, і `./.agents/skills/` для встановлення в межах проєкту (`--project`). Просте `graphify install` залишається одноплатформовим (Claude Code) за задумом — використовуйте окрему платформу `agents`, коли потрібно, щоб скіл був доступний для будь-якого фреймворку, що читає `.agents/skills`.

> У Codex використовується `$graphify` замість `/graphify`.

</details>

<details>
<summary><b>Опційні додатки</b> (встановлюйте лише те, що потрібно)</summary>

| Додаток | Що додає | Встановлення |
|---|---|---|
| `pdf` | Видобування з PDF | `uv tool install "graphifyy[pdf]"` |
| `office` | Підтримка `.docx` та `.xlsx` | `uv tool install "graphifyy[office]"` |
| `google` | Рендеринг Google Sheets | `uv tool install "graphifyy[google]"` |
| `video` | Транскрибування відео/аудіо (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | MCP stdio-сервер | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Підтримка вивантаження в Neo4j | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | Підтримка вивантаження в FalkorDB | `uv tool install "graphifyy[falkordb]"` |
| `svg` | Експорт графа в SVG | `uv tool install "graphifyy[svg]"` |
| `leiden` | Виявлення спільнот за алгоритмом Leiden (лише Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Локальний inference через Ollama | `uv tool install "graphifyy[ollama]"` |
| `openai` | OpenAI та сумісні з OpenAI API | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic Claude API (`--backend claude`, використовує `ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (використовує IAM, без API-ключа) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, використовує `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "graphifyy[openai]"` |
| `sql` | Видобування схеми SQL | `uv tool install "graphifyy[sql]"` |
| `postgres` | Інспекція живої бази PostgreSQL (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | Видобування AST з BYOND DreamMaker `.dm`/`.dme` (може знадобитися компілятор C + `python3-dev`, якщо для вашої платформи немає готового wheel) | `uv tool install "graphifyy[dm]"` |
| `terraform` | Видобування AST з Terraform / HCL `.tf`/`.tfvars`/`.hcl` | `uv tool install "graphifyy[terraform]"` |
| `pascal` | Видобування AST з Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` (точніші зв'язки `calls`/`inherits`; за відсутності — резервний regex-екстрактор) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | Сегментація запитів китайською (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | Усе перелічене вище | `uv tool install "graphifyy[all]"` |

</details>

---

## Змусьте свого асистента завжди використовувати граф

Виконайте це один раз у своєму проєкті після побудови графа:

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
| Agent Skills (крос-фреймворкові) | `graphify agents install` (альтернатива `graphify skills install`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify pi install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

Це записує невеликий конфігураційний файл, який каже вашому асистенту звертатися до графа знань щодо питань про кодову базу, надаючи перевагу точковим запитам типу `graphify query "<question>"` над читанням повного звіту чи грепанням сирих файлів.

- **Платформи з хуками** (Claude Code, Gemini CLI): хук автоматично спрацьовує перед пошуковими викликами інструментів (а в Claude Code — і перед послідовним читанням вихідних файлів через інструменти Read/Glob) і підштовхує вашого асистента до шляху через граф.
- **Платформи з файлами інструкцій** (Codex, OpenCode, Cursor тощо): постійні файли інструкцій (`AGENTS.md`, `.cursor/rules/` тощо) дають ту саму рекомендацію "спершу запит".

`GRAPH_REPORT.md` і надалі доступний для широкого огляду архітектури.

**CodeBuddy** робить те саме, що й Claude Code: записує розділ у `CODEBUDDY.md`, який каже CodeBuddy читати `graphify-out/GRAPH_REPORT.md` перед відповіддю на архітектурні питання, і встановлює хуки `PreToolUse` (`.codebuddy/settings.json`), які спрацьовують перед пошуковими командами Bash і читанням файлів, підштовхуючи до `graphify query` замість цього.

**Codex** записує в `AGENTS.md`, який власне і несе завжди активну підказку про граф на цій платформі. `graphify codex install` також реєструє хук `PreToolUse` у `.codex/hooks.json` (`graphify hook-check`), але цей запис свідомо є **no-op**: Codex Desktop відхиляє `hookSpecificOutput.additionalContext` для `PreToolUse`, тож видача підказки там зламала б виклики інструмента Bash. На відміну від Claude Code, де підштовхує саме хук (`graphify hook-guard`), у Codex хук спрацьовує і свідомо нічого не робить, а `AGENTS.md` є завжди активним механізмом.

**Kilo Code** встановлює скіл Graphify у `~/.config/kilo/skills/graphify/SKILL.md` та рідну команду `/graphify` у `~/.config/kilo/command/graphify.md`. `graphify kilo install` також записує `AGENTS.md` плюс рідний плагін `tool.execute.before` (`.kilo/plugins/graphify.js` + реєстрація в `.kilo/kilo.json` чи `.kilo/kilo.jsonc`), щоб Kilo отримав ту саму завжди активну поведінку через рідну конфігурацію `.kilo`.

**Cursor** записує `.cursor/rules/graphify.mdc` із `alwaysApply: true`, тож Cursor автоматично включає це в кожну розмову, без хука.

Щоб видалити graphify з усіх платформ одразу: `graphify uninstall` (додайте `--purge`, щоб також видалити `graphify-out/`). Або скористайтеся командою для конкретної платформи (наприклад, `graphify claude uninstall`).

---

## Що міститься у звіті

- **God nodes** — найбільш пов'язані концепти у вашому проєкті. Через них проходить усе.
- **Несподівані зв'язки** — посилання між сутностями, що живуть у різних файлах чи модулях. Ранжовані за тим, наскільки вони несподівані.
- **"Чому"** — вбудовані коментарі (`# NOTE:`, `# WHY:`, `# HACK:`), докстрінги та проєктні обґрунтування з документів видобуваються як окремі вузли, пов'язані з кодом, який вони пояснюють.
- **Рекомендовані запитання** — 4–5 питань, на які граф здатен відповісти по-особливому влучно.
- **Теги довіри** — кожен виведений зв'язок позначено як `EXTRACTED`, `INFERRED` або `AMBIGUOUS`. Ви завжди знаєте, що знайдено, а що припущено.

---

## Які файли він підтримує

| Тип | Розширення |
|------|-----------|
| Код (36 граматик tree-sitter) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme` потребує `uv tool install graphifyy[dm]`; `.mts`/`.cts` використовують граматику TypeScript, `.cc`/`.cxx` та CUDA `.cu`/`.cuh` та Metal `.metal` використовують граматику C++) |
| Salesforce Apex | `.cls .trigger` (на основі regex; класи, інтерфейси, enum'и, методи, тригери, зв'язки SOQL/DML) |
| Terraform / HCL | `.tf .tfvars .hcl` (потребує `uv tool install graphifyy[terraform]`) |
| Конфігурації MCP | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — видобуває вузли серверів, посилання на пакети, вимоги до змінних середовища |
| Маніфести пакетів | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — один канонічний вузол пакета на кожен пакет (за назвою) плюс зв'язки `depends_on`, тож пакет, на який посилаються багато маніфестів, — це один хаб |
| Документи | `.md .mdx .qmd .html .txt .rst .yaml .yml` (посилання markdown `[text](./other.md)` та `[[wikilinks]]` стають зв'язками `references` між документами) |
| Office | `.docx .xlsx` (потребує `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (опційно; потребує авторизації `gws` та `--google-workspace`; для Sheets потрібен `uv tool install graphifyy[google]`) |
| PDF | `.pdf` |
| Зображення | `.png .jpg .webp .gif` |
| Відео / Аудіо | `.mp4 .mov .mp3 .wav` та інші (потребує `uv tool install graphifyy[video]`) |
| YouTube / URL-адреси | будь-яка URL-адреса відео (потребує `uv tool install graphifyy[video]`) |

Код видобувається **локально, без API-викликів** (AST через tree-sitter). Усе інше проходить через API моделі вашого ШІ-асистента.

Файли `.gdoc`, `.gsheet` та `.gslides` від Google Drive для десктопу — це ярлики-вказівники,
а не вміст документа. Щоб включити нативні Google Docs, Sheets і Slides
у безголове (headless) видобування, встановіть і авторизуйте
[CLI `gws`](https://github.com/googleworkspace/cli), потім виконайте:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

Можна також встановити `GRAPHIFY_GOOGLE_WORKSPACE=1`. Graphify експортує ярлики у
`graphify-out/converted/` як бічні файли Markdown, а потім видобуває вже їх.

---

## Поширені команди

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

Див. [Decouple: кандидати Extract-Class з оцінкою ризику](#decouple-кандидати-extract-class-з-оцінкою-ризику) вище, або [повний довідник команд](#повний-довідник-команд) нижче.

---

## Ігнорування файлів

Створіть `.graphifyignore` у корені свого проєкту — той самий синтаксис, що й `.gitignore`, включно з заперечнями через `!`.

**`.gitignore` враховується автоматично.** graphify читає `.gitignore` у кожній директорії. Якщо присутній ще й `.graphifyignore`, вони **об'єднуються** — шаблони `.graphifyignore` застосовуються останніми, тож вони перемагають у конфліктах (включно з запереченнями `!`). Додавання `.graphifyignore` може лише виключити більше файлів; воно ніколи не повертає файл, який уже виключив ваш `.gitignore`. Область дії для підкаталогів працює так само, як у git — файл ігнорування впливає лише на власне піддерево.

Передайте `--no-gitignore` команді `graphify extract`, якщо ігнорований git згенерований чи транспільований код має бути в графі. Це вимикає `.gitignore` та `.git/info/exclude`; `.graphifyignore` продовжує застосовуватися.

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

## Налаштування для команди

`graphify-out/` призначено для коміту в git, щоб усі в команді починали з однакової карти.

**Рекомендовані додавання до `.gitignore`:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` тепер портативний — ключі зберігаються як відносні шляхи й перепрів'язуються під час завантаження, тож комітити його безпечно, і це дозволяє уникнути повної перебудови під час першого checkout.

**Робочий процес:**
1. Одна людина запускає `/graphify .` і комітить `graphify-out/`.
2. Усі інші роблять pull — їхній асистент одразу читає граф.
3. Виконайте `graphify hook install`, щоб автоматично перебудовувати граф після кожного коміту (лише AST, без витрат на API). Це також налаштовує git merge driver, тож `graph.json` ніколи не лишається з маркерами конфлікту — коли двоє розробників комітять паралельно, їхні графи автоматично об'єднуються.
4. Коли змінюються документи чи статті, запустіть `/graphify --update`, щоб оновити ці вузли.

---

## Використання графа напряму

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

MCP-сервер надає вашому асистенту структурований доступ: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Спільний HTTP-сервер

`--transport stdio` (за замовчуванням) породжує один локальний сервер на кожного розробника. `--transport http` подає ті самі інструменти через транспорт MCP Streamable HTTP, тож один спільний процес може обслуговувати граф для всієї команди — клієнти вказують у конфігурації MCP свого IDE `http://<host>:8080/mcp` замість локального запуску graphify.

| Флаг | За замовчуванням | Призначення |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Транспорт для роботи сервера |
| `--host` | `127.0.0.1` | Хост для прив'язки HTTP (використовуйте `0.0.0.0`, щоб відкрити доступ за межі localhost) |
| `--port` | `8080` | Порт для прив'язки HTTP |
| `--api-key` | змінна середовища `GRAPHIFY_API_KEY` | Вимагати `Authorization: Bearer <key>` (або `X-API-Key`) |
| `--path` | `/mcp` | Шлях монтування HTTP |
| `--json-response` | вимкнено | Повертати звичайний JSON замість потоків SSE |
| `--stateless` | вимкнено | Без стану на сесію (для розгортань із балансуванням навантаження / CI) |
| `--session-timeout` | `3600` | Прибирати неактивні стани сесій через N секунд (`0` вимикає) |

Прив'язка за замовчуванням `127.0.0.1` — лише loopback. Встановлюйте `--host 0.0.0.0` **і** `--api-key` разом, коли розгортаєте на спільному хості. Запуск у контейнері:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **Примітка для WSL / Linux:** Ubuntu постачає `python3`, а не `python`. Використовуйте venv, щоб уникнути конфліктів:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## Змінні середовища

Вони потрібні лише для **безголового видобування / видобування в CI** (`graphify extract`). Під час роботи через скіл `/graphify` у вашому IDE API моделі надає сесія самого IDE — додаткові ключі не потрібні.

| Змінна | Призначення | Коли потрібна |
|---|---|---|
| `ANTHROPIC_API_KEY` | Бекенд Claude (Anthropic) | `--backend claude` |
| `ANTHROPIC_BASE_URL` | URL сумісної з Anthropic точки доступу (проксі LiteLLM, гейтвеї тощо) | `--backend claude` (за замовчуванням: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Назва моделі для бекенда Claude — для власних точок доступу вкажіть назву/псевдонім моделі, який надає ваш сервер | `--backend claude` (за замовчуванням: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` або `GOOGLE_API_KEY` | Бекенд Google Gemini | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI або сумісні з OpenAI API | `--backend openai` (локальні сервери приймають будь-яке непорожнє значення) |
| `OPENAI_BASE_URL` | URL сумісного з OpenAI сервера (llama.cpp, vLLM, LM Studio тощо) | `--backend openai` (за замовчуванням: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | Назва моделі для бекенда OpenAI — для власних серверів вкажіть назву/псевдонім моделі, який надає ваш сервер (перевірте його кінцеву точку `/v1/models`), напр. `LFM2.5-8B-A1B-UD-Q4_K_XL` для llama.cpp | `--backend openai` (за замовчуванням: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | Бекенд DeepSeek | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Бекенд Kimi Code | `--backend kimi` |
| `OLLAMA_BASE_URL` | URL локального inference Ollama | `--backend ollama` (за замовчуванням: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Назва моделі Ollama | `--backend ollama` (за замовчуванням: автовизначення) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Перевизначити розмір вікна KV-кешу Ollama | опційно — за замовчуванням розмір визначається автоматично |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Скільки хвилин тримати модель Ollama завантаженою | опційно — встановіть `0`, щоб вивантажувати після кожного чанка |
| `AZURE_OPENAI_API_KEY` | Бекенд Azure OpenAI Service | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | URL кінцевої точки ресурсу Azure | `--backend azure` (потрібен разом із API-ключем) |
| `AZURE_OPENAI_API_VERSION` | Перевизначення версії API Azure | опційно — за замовчуванням `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` або `GRAPHIFY_AZURE_MODEL` | Назва розгортання Azure | опційно — за замовчуванням `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — стандартний ланцюжок автентифікації | `--backend bedrock` (без API-ключа, використовує IAM) |
| `GRAPHIFY_MAX_WORKERS` | Кількість потоків для паралелізму AST | опційно — також флаг `--max-workers` |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Підвищити межу виводу для щільних корпусів | опційно — напр. `32768` для великих файлів |
| `GRAPHIFY_API_TIMEOUT` | Тайм-аут на виклик у секундах для бекендів HTTP, claude-cli, Anthropic SDK та Bedrock (за замовчуванням: 600) | опційно — також флаг `--api-timeout` |
| `GRAPHIFY_MAX_RETRIES` | Скільки разів повторювати запит, обмежений за швидкістю (429), перед тим як здатися (за замовчуванням: 6; враховує `Retry-After`) | опційно — підвищуйте для суворих лімітів на організацію (напр. kimi); `0` вимикає |
| `GRAPHIFY_FORCE` | Примусово перебудувати граф навіть із меншою кількістю вузлів | опційно — також флаг `--force` |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Автоматично увімкнути експорт Google Workspace | опційно — встановіть `1` |
| `GRAPHIFY_TRIAGE_BACKEND` | Бекенд для `graphify prs --triage` | опційно — визначається автоматично за наявними ключами |
| `GRAPHIFY_TRIAGE_MODEL` | Перевизначення моделі для triage | опційно — напр. `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | Встановіть `1`, щоб увімкнути локальний журнал запитів у `~/.cache/graphify-queries.log` (фіксує кожне питання query/path/explain + шлях до корпусу). Вимкнено за замовчуванням — нічого не записується, доки ви не увімкнете це самі (#1797) | опційно |
| `GRAPHIFY_QUERY_LOG` | Увімкнути журнал запитів і записувати його за цим шляхом замість стандартного | опційно — вимкнено, якщо не встановлено це або `_ENABLE` |
| `GRAPHIFY_QUERY_LOG_DISABLE` | Встановіть `1`, щоб примусово вимкнути журнал запитів (перемагає змінні увімкнення) | опційно |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | Коли журнал увімкнено, також записувати повні відповіді підграфів (вимкнено за замовчуванням) | опційно |
| `GRAPHIFY_MAX_GRAPH_BYTES` | Перевизначити межу розміру `graph.json` у 512 МіБ — напр. `700MB`, `2GB` або просто байти | опційно — корисно для дуже великих корпусів |
| `GRAPHIFY_MAX_CONTEXTS` | Максимальна кількість не-основних графів проєктів, які зберігає один багатопроєктний MCP-сервер | опційно — за замовчуванням: `8`; некоректні значення трактуються як `8`, значення нижче `1` — як `1` |
| `GRAPHIFY_LLM_TEMPERATURE` | Перевизначити температуру LLM для семантичного видобування — напр. `0.7`, або `none`, щоб пропустити | опційно — автоматично пропускається для моделей-міркувачів o1/o3/o4/gpt-5 |

---

## Конфіденційність

- **Файли коду** — обробляються локально через tree-sitter. Нічого не залишає вашу машину. Корпус лише з коду не потребує API-ключа — `graphify extract` працює повністю офлайн. У змішаному репозиторії додайте `--code-only`, щоб індексувати лише код і пропустити документи/PDF/зображення, для яких інакше знадобився б LLM.
- **Відео / аудіо** — транскрибується локально за допомогою faster-whisper. Нічого не залишає вашу машину.
- **Документи, PDF, зображення** — надсилаються вашому ШІ-асистенту для семантичного видобування (через скіл `/graphify`, з використанням тієї моделі, яку запускає ваша сесія IDE). Безголовий `graphify extract` потребує `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), запущений інстанс Ollama (`OLLAMA_BASE_URL`), облікові дані AWS через стандартний ланцюжок постачальників (Bedrock — без API-ключа, використовує IAM), або бінарник CLI `claude` (Claude Code — без API-ключа, використовує вашу підписку Claude). Флаг `--dedup-llm` використовує той самий ключ.
- **Резидентність даних** — `graphify extract` автоматично визначає постачальника на основі того, який API-ключ встановлено (пріоритет: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). Для коду з вимогами до резидентності даних використовуйте `--backend ollama` (повністю локально) або передайте явний флаг `--backend`. Kimi (`MOONSHOT_API_KEY`) маршрутизує на сервери Moonshot AI в Китаї.
- **Без телеметрії**, без відстеження використання, без аналітики.
- **Логування запитів** — кожен виклик `graphify query`, `graphify path`, `graphify explain` та MCP `query_graph` логується у `~/.cache/graphify-queries.log` у форматі JSON Lines (часова позначка, питання, корпус, кількість повернутих вузлів, тривалість). Повні відповіді підграфів **не** зберігаються за замовчуванням. Встановіть `GRAPHIFY_QUERY_LOG_DISABLE=1`, щоб відмовитися від цього, або `GRAPHIFY_QUERY_LOG=/dev/null`, щоб приглушити без вимкнення самого коду.

---

## Усунення несправностей

**`graphify: command not found` після встановлення**
CLI встановлено, але його bin-директорія не в `PATH` вашої оболонки. Оберіть виправлення відповідно до способу встановлення:
- **uv** (`uv tool install graphifyy`): команда потрапляє в bin-директорію інструментів uv (`~/.local/bin`), якої часто немає в `PATH` у свіжому середовищі macOS/zsh. Виконайте `uv tool update-shell`, потім відкрийте новий термінал. (Знайти директорію можна через `uv tool dir --bin`.)
- **pipx** (`pipx install graphifyy`): виконайте `pipx ensurepath`, потім відкрийте новий термінал.
- **pip** (`pip install graphifyy`): pip встановлює скрипти в user bin-директорію, яка може бути не в `PATH` — додайте `~/Library/Python/3.x/bin` (macOS) або `~/.local/bin` (Linux) у ваш `PATH` в `~/.zshrc`/`~/.bashrc`, або просто запустіть `python -m graphify`.

**`uvx graphify …` або `uv tool run graphify …` не може розв'язати `graphify`**
Пакет на PyPI називається `graphifyy`; `graphify` — це лише команда, яку він надає. `uv tool run` сприймає перше слово як *назву пакета*, тож шукає пакет із назвою `graphify` і повідомляє `No solution found … no versions of graphify`. Вказуйте пакет явно: `uvx --from graphifyy graphify install` (те саме, що `uv tool run --from graphifyy graphify install`). Або одноразово виконайте `uv tool install graphifyy`, а далі викликайте `graphify` напряму.

**`uv run --with graphifyy python -m graphify` мовчки запускає старіше встановлення**
`uv run` використовує *системний* Python, тож якщо старіший `graphifyy` теж живе там (наприклад, від минулого `pip install graphifyy`), Python може знайти саме цю копію раніше в `sys.path`, і `--with graphifyy` її не перевизначить. Запуск відбувається без помилки, але ви отримуєте поведінку *старої* версії — напр. перевизначення через змінні середовища, як `OPENAI_BASE_URL`, мовчки ігноруються, тож запити йдуть на стандартну кінцеву точку і повертають 401, схожий на неправильний ключ. Ознака — рядок `warning: skill is from graphify <newer>, package is <older>`: це означає, що завантажилося інше встановлення, а не просто застарілий скіл. Перевірте, яка копія завантажилася насправді:
```bash
python -c "import graphify; print(graphify.__file__)"
```
Потім запускайте встановлену команду напряму (вона використовує керовану uv копію) або видаліть застарілу системну копію:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` працює, а команда `graphify` — ні**
`PATH` вашої оболонки не включає bin-директорію, куди було встановлено команду. Надавайте перевагу `uv tool install` / `pipx install` над простим `pip`, потім виконайте `uv tool update-shell` / `pipx ensurepath` і відкрийте новий термінал (див. примітки щодо встановлення вище).

**`/graphify .` викликає "path not recognized" у PowerShell**
PowerShell сприймає похилий слеш на початку як роздільник шляху. Використовуйте `graphify .` (без слеша) на Windows.

**У графі менше вузлів після `--update` або перебудови**
Якщо рефакторинг видалив файли, старі вузли залишаються. Передайте `--force` (або встановіть `GRAPHIFY_FORCE=1`), щоб перезаписати граф навіть якщо в перебудові менше вузлів.

**`extract` завершується з "extraction was incomplete ... refusing to overwrite"**
Коли прохід видобування завершується збоєм або обхід не може повністю прочитати корпус, результат вийде меншим за повний, тож `graphify extract` відмовляється перезаписувати більший наявний граф частковим результатом (захищаючи ваш `graph.json`). Виправте причину збою й повторіть спробу, або передайте `--allow-partial`, щоб перезаписати попри все.

**У графі є дублікати вузлів для однієї сутності (вузли-двійники)**
Вузли-двійники (той самий символ з'являється двічі — раз через AST-видобування з розташуванням у джерелі, раз через семантичне видобування без нього) тепер автоматично об'єднуються під час побудови. Якщо ви бачите таке у графі, побудованому до v0.8.33, виконайте повне повторне видобування, щоб прибрати їх:
```bash
graphify extract . --force
```

**Ollama вичерпує VRAM / перевищено розмір контекстного вікна**
Розмір вікна KV-кешу підбирається автоматично, але може бути завеликим для вашого GPU. Зменшіть його:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**Попередження `LLM returned invalid JSON` / `Unterminated string`**
Відповідь моделі у форматі JSON досягла межі токенів виводу й обірвалася посередині рядка. graphify автоматично відновлюється (розбиває чанк і повторно видобуває обидві половини, а завеликий одиничний документ спершу розрізається за межами заголовків/абзаців, тож весь файл усе одно охоплюється), тож ці попередження шумні, але не означають втрату даних. Щоб зменшити цей шум, підвищте межу виводу або зменшіть вивід кожного чанка:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
Із хмарним гейтвеєм типу OpenRouter надавайте перевагу `--backend openai` (встановивши `OPENAI_BASE_URL`) над шимом Ollama — це чистіший, сумісний з OpenAI шлях. Якщо у моделі є власна межа максимального виводу, зниження `--token-budget` — найнадійніший важіль.

**HTML графа занадто великий, щоб відкрити в браузері (>5000 вузлів)**
Пропустіть генерацію HTML і використовуйте JSON напряму:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**У `graph.json` з'являються маркери конфлікту після одночасного коміту двох розробників**
Виконайте `graphify hook install` — це налаштовує git merge driver, який автоматично об'єднує `graph.json`, тож конфліктів узагалі не виникає.

**Видобування повертає порожні вузли/зв'язки для документів чи PDF**
Документи, PDF і зображення потребують викликів LLM — корпуси лише з коду не потребують ключа. Перевірте, що ваш API-ключ встановлено і бекенд коректний:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**Попередження про неузгодженість версій скіла у вашому IDE**
Встановлена версія graphify відрізняється від файлу скіла. Оновіть:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**Кеш промптів Claude Code скидається після кожного `graphify extract`**
Graphify записує вихідні файли (`graph.json`, `graphify-out/`) прямо в робочу область. Якщо ці шляхи не ігноруються, кожен запис скидає кеш промптів Claude Code, змушуючи повністю перезавантажувати контекст за тарифами запису кешу на наступному кроці. Додайте їх у `.claudeignore`:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## Повний довідник команд

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

> **Назви спільнот:** усередині агента (Claude Code, Gemini CLI) сам агент називає спільноти. Коли ви запускаєте голий CLI, `cluster-only` автоматично називає їх за допомогою налаштованого бекенда (вбудованого або кастомного OpenAI-сумісного постачальника) — передайте `--no-label`, щоб залишити `Community N`, або запустіть `graphify label`, щоб (пере)генерувати назви за потреби.

---

## Дізнатися більше

- [Як це працює](../how-it-works.md) — конвеєр видобування, виявлення спільнот, оцінка довіри, бенчмарки
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — розбиття на модулі, як додати мову
- [Опційні інтеграції](../docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — книга про ідеї, що стоять за graphify, і про архітектуру від початку до кінця

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) — це завжди активний шар, побудований на graphify: він застосовує той самий підхід із графами до всього вашого робочого контексту — зустрічей, файлів, документів і коду, — оновлюючись безперервно у фоні.

Створено для людей і команд, чия робота живе в сотнях розмов і документів, які вони ніколи не зможуть повністю відновити в пам'яті.

**[Приєднайтеся до списку очікування на graphify.com](https://graphify.com).** Безкоштовний тріал запускається незабаром.

---

<details>
<summary>Участь у розробці</summary>

### Налаштування середовища розробки

Проєкт використовує [uv](https://docs.astral.sh/uv/) для робочого процесу розробки. Встановіть його один раз, потім:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

Перевірте editable-встановлення:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### Запуск тестів

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> Примітка для macOS: набір тестів включає фікстури і `sample.f90`, і `sample.F90`. Вони конфліктують на файлових системах, не чутливих до регістру, як HFS+ / APFS. Запускайте на Linux або в контейнері Docker, якщо потрібно тестувати обидва варіанти Fortran одночасно.

### Git-процес

- Активна розробка триває у гілці `v8`.
- Стиль комітів: `fix: <description>` / `feat: <description>` / `docs: <description>`
- Перед відкриттям PR виконайте `uv run pytest tests/ -q` і переконайтеся, що тести проходять.
- Додайте файл-фікстуру в `tests/fixtures/` і тести в `tests/test_languages.py` для будь-якого нового екстрактора мови.

### Що можна внести

**Розроблені приклади (worked examples)** — найкорисніший внесок. Запустіть `/graphify` на реальному корпусі, збережіть результат у `worked/{slug}/`, напишіть чесний `review.md` про те, що граф вловив правильно, а що — ні, і відкрийте PR.

**Помилки видобування** — відкрийте issue з вхідним файлом, записом кешу (`graphify-out/cache/`) і тим, що було пропущено чи невірно.

Див. [ARCHITECTURE.md](../../ARCHITECTURE.md) щодо відповідальності модулів і того, як додати мову.

</details>
