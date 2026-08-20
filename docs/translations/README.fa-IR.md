<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>یک فورک از <a href="https://github.com/Graphify-Labs/graphify">graphify</a> که <code>graphify decouple</code> را اضافه می‌کند</b> — کاندیدهای Extract-Class با امتیاز ریسک برای god objectها، بدون LLM، که پیش از پیشنهاد هر کاری دوباره در برابر کد منبع واقعی (نه فقط گراف فراخوانی) تأیید می‌شوند. به <a href="#decouple-risk-scored-extract-class-candidates">Decouple: کاندیدهای Extract-Class با امتیاز ریسک</a> در پایین مراجعه کنید.
</p>

<div align="center">
<details><summary><b>این را به زبان‌های دیگر بخوانید</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>دسترسی زودهنگام به پلتفرم graphify پیش از عرضه‌ی عمومی v1 باز است: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

`/graphify` را در دستیار کدنویسی هوش مصنوعی خود تایپ کنید تا کل پروژه‌ی شما (کد، اسناد، PDFها، تصاویر، ویدیوها) را به یک **گراف دانش** نگاشت کند که می‌توانید به‌جای grep کردن فایل‌ها، آن را **کوئری** بزنید.

- **نگاشت کد رایگان، کاملاً محلی.** کد با tree-sitter AST تجزیه می‌شود: قطعی، بدون LLM، هیچ‌چیز از دستگاه شما خارج نمی‌شود. (اسناد، PDFها، تصاویر و ویدیو از مدل دستیار شما یا یک کلید API پیکربندی‌شده برای یک گذر معنایی استفاده می‌کنند.)
- **هر یال توضیح داده می‌شود.** هر اتصال با `EXTRACTED` (صریح در منبع) یا `INFERRED` (استنتاج‌شده توسط graphify) برچسب می‌خورد، تا بدانید چه چیزی مستقیم خوانده شده و چه چیزی استنتاج شده.
- **این یک ایندکس برداری نیست.** بدون embeddings، بدون vector store: یک گراف واقعی که پیمایش می‌کنید. سؤالی بپرسید، مسیر بین دو چیز را دنبال کنید، یا یک مفهوم را توضیح دهید.

> می‌خواهید این همیشه فعال باشد، در پس‌زمینه در کد، اسناد و جلسات شما به‌روزرسانی شود، نه فقط در صورت درخواست؟ این چیزی است که ما در **[graphify.com](https://graphify.com)** می‌سازیم، و دسترسی زودهنگام هم‌اکنون در **[app.graphify.com](https://app.graphify.com/login)** باز است.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="graphify's interactive graph.html showing the FastAPI codebase as a force-directed knowledge graph with a legend of detected communities" width="900">
</p>
<p align="center">
  <em>کد منبع FastAPI که توسط graphify نگاشت شده. هر گره یک مفهوم است، رنگ‌ها جوامع شناسایی‌شده هستند، و کل آن در graph.html قابل کلیک است.</em>
</p>

**شروع کنید** (۳۰ ثانیه):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

سپس، در دستیار هوش مصنوعی خود:

```
/graphify .
```

همین. شما **سه فایل** دریافت می‌کنید:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**در این‌ها کار می‌کند:** Claude Code، Cursor، Codex، Gemini CLI، GitHub Copilot، و بیش از ۱۵ مورد دیگر — [پلتفرم خود را انتخاب کنید](#install).

---

## آن را در عمل ببینید

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="graphify path query: a terminal asks for the shortest path between FastAPI and ModelField, and the answer lights up hop by hop across the knowledge graph" width="900">
</p>

پس از ساخته شدن گراف، به‌جای خواندن فایل‌ها آن را کوئری می‌زنید. خروجی واقعی، graphify اجرا شده روی کد منبع FastAPI که در بالا نشان داده شد:

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

هر یال یک **برچسب اطمینان** حمل می‌کند (`EXTRACTED` = صریح در منبع، `INFERRED` = استنتاج‌شده از طریق حل‌وفصل)، تا بدانید چه چیزی مستقیم خوانده شده و چه چیزی استنتاج شده. `graphify query "<question>"` برای یک سؤال به زبان ساده یک زیرگراف محدود برمی‌گرداند، و `graphify path A B` نشان می‌دهد چگونه هر دو چیز به هم متصل‌اند.

---

## Decouple: کاندیدهای Extract-Class با امتیاز ریسک

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: MainWindow god node splitting into risk-scored candidate classes, with a shared-state warning between two of them" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: MainWindow's 5 proposed classes, Node Info panel open on Main Window Axis and Range Controls showing a 0.608 state overlap with Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>DECOUPLE.html روی یک اجرای واقعی — کلیک روی یک کلاس پیشنهادی دقیقاً نشان می‌دهد با کدام کلاس دیگر state به اشتراک می‌گذارد، و دقیقاً چه چیزی به اشتراک گذاشته می‌شود.</em>
</p>

همین صفحه خود تقسیم را نیز رندر می‌کند. فعال کردن **Preview decoupled view** متدهای خود god کلاس را با کلاس‌های پیشنهادی جابه‌جا می‌کند و یال‌ها را در همان جا مسیریابی مجدد می‌کند — تغییر سیم‌کشی، نه یک نمودار دوباره‌رسم‌شده:

| قبل — god کلاس امروز | بعد — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html before the toggle: a single MainWindow hub node with its own methods fanned out around it" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html after the toggle: the same node reduced to 5 diamond-shaped proposed classes, green dashed edges showing which methods were extracted into each, red edges showing shared instance state between two of them" width="440"> |
| یک گره که ۴۷ متد خودش را نگه می‌دارد، هرکدام فقط از طریق کلاس قابل دسترسی. | کلاس‌های پیشنهادی. خط‌چین سبز = چه چیزی به کدام استخراج شده؛ قرمز = state نمونه‌ای که دو تا از آن‌ها هنوز به اشتراک می‌گذارند، که دقیقاً همان چیزی است که بین `split` و `keep_as_is` تصمیم می‌گیرد. فقط کاندیدهایی که از آستانه‌ی ریسک عبور می‌کنند رسم می‌شوند — اینجا ۵ از ۶، به همین دلیل یک متد لوزی‌ای برای فرود ندارد. |

`graphify decouple` god objectها را پیدا می‌کند و به شما می‌گوید آیا تقسیم کردن آن‌ها واقعاً ارزشش را دارد — نه فقط اینکه بزرگ‌اند.

حالت شکستی که این برای گرفتن آن ساخته شده: کلاسی با ۴۷ متد که خوشه‌بندی مبتنی بر گراف فراخوانی با خوشحالی آن را به ۵ گروه مرتب به‌نظررسنده تقسیم می‌کند، که همه‌ی آن‌ها هنوز دقیقاً همان state نمونه‌ای `self._chart_style` / `self._crosshair` را در زیر می‌خوانند و می‌نویسند. اگر آن تقسیم را ارسال کنید، هیچ‌چیزی را decouple نکرده‌اید — فقط متدها را به فایل‌های جدیدی منتقل کرده‌اید که هنوز نمی‌توانند مستقل تست، تغییر یا درک شوند، چون همه‌شان هنوز به همان state مشترک نیاز دارند که به آن‌ها بازگردانده شود. ابزاری که فقط به گراف فراخوانی نگاه می‌کند اصلاً نمی‌تواند این را ببیند؛ باید به منبع واقعی برگردد.

**دو بررسی، هر دو بدون LLM، هر دو قطعی:**

1. **آیا این اصلاً یک God Object است؟** یک گره با درجه‌ی بالا می‌تواند یک God Object واقعی باشد (متدهای زیاد از آنِ خودش، پخش‌شده در مسئولیت‌های نامرتبط — Extract Class اعمال می‌شود) یا یک hub/مدل داده با ارجاع بیش‌ازحد (متدهای کم از آنِ خودش، بیشتر ارجاعات *ورودی* — تقسیم بدنه‌ی آن هیچ کاری نمی‌کند؛ راه‌حل باریک کردن رابط آن است، نه استخراج یک کلاس). `classify_god_node` این‌ها را با `member_ratio` تشخیص می‌دهد، نه درجه‌ی خام — تفاوتی که مانع می‌شود `TraceSource` (۸۴ یال، اما فقط ۶ متد از آنِ خودش) پیشنهاد تقسیم نادرستی بگیرد که `MainWindow` (۸۸ یال، ۴۷ متد از آنِ خودش) به‌درستی می‌گیرد.
2. **آیا تقسیم واقعاً coupling را کاهش می‌دهد؟** `risk_before` (اندازه/coupling/تکه‌تکه‌شدگی فعلی گره god) با `risk_after` مقایسه می‌شود — ریسک جدیدی که خود تقسیم معرفی می‌کند: فراخوانی‌های بین‌گروهی که یال‌های نامرئی درون‌کلاسی بودند و به وابستگی‌های صریح بین‌کلاسی تبدیل می‌شوند، فراخوانندگانی که اکنون باید به بیش از یک کلاس جدید وابسته باشند، و — بررسی‌ای که یک گراف فراخوانی از نظر ساختاری نمی‌تواند انجام دهد — گروه‌های پیشنهادی واقعاً چقدر state نمونه‌ای `self`/`this` (خواندن‌ها، نوشتن‌ها، و فراخوانی‌های متد کمکی مشترک، با وزن‌دهی جداگانه: یک **نوشتن** مشترک امتیاز بالاتری نسبت به یک خواندن مشترک می‌گیرد) مشترک دارند. این کار فایل منبع خودِ گره god را مستقیماً با tree-sitter دوباره تجزیه می‌کند؛ به گراف استخراج‌شده‌ی خودِ graphify متکی نیست، که هرگز دسترسی سطح فیلد را برای هیچ زبانی ثبت نمی‌کند. فقط زمانی که `risk_after` از آستانه‌ای پایین‌تر از `risk_before` عبور کند، برنامه `split` را توصیه می‌کند — در غیر این صورت `marginal` یا `keep_as_is` است، و یک کاندید دلسردکننده به‌صورت یک عدد گزارش می‌شود، هرگز به‌صورت شکلی که مجبور باشید با چشم حدس بزنید رسم نمی‌شود.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

سه فایل کنار `graph.json` تولید می‌کند:

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

**پوشش زبان برای بررسی اشتراک state** (طبقه‌بندی فقط-گراف-فراخوانی بالا برای هر زبانی که graphify استخراج می‌کند کار می‌کند؛ این جدول به‌طور خاص درباره‌ی تجزیه‌ی مجدد منبع است که همپوشانی state `self`/`this` را تأیید می‌کند):

| زبان | پشتیبانی‌شده | یادداشت‌ها |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` گره AST خودش است، نه دسترسی فیلد بسته‌بندی‌شده — به‌صراحت مدیریت می‌شود |
| C# | ✅ | |
| Rust | ✅ | `self.x` از طریق بلوک‌های `impl` |
| Ruby | ✅ | `@x` (اصطلاح غالب) + فراخوانی‌های `self.foo` |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | حل‌وفصل receiver به‌ازای هر متد — Go کلمه‌ی کلیدی `self`/`this` ندارد، پس نام receiver (`f` در `func (f *Foo) M()`) برای هر متد دوباره حل می‌شود |
| C | ❌ | یک پارامتر اشاره‌گر struct هیچ نشانه‌ی نحوی‌ای ندارد که آن را از هر پارامتر دیگری متمایز کند — بدون استنتاج کامل نوع، سیگنال قابل‌اعتمادی وجود ندارد |

یک گره god در یک زبان پشتیبانی‌نشده، یا یکی که منبعش قابل خواندن نیست، به‌عنوان `state_analysis: "skipped"` علامت‌گذاری می‌شود — طبقه‌بندی و امتیاز گراف فراخوانی همچنان اجرا می‌شوند، اما توصیه فقط بر گراف فراخوانی تکیه می‌کند نه اینکه بی‌صدا فرض کند بررسی state موفق شده.

---

## این چه کاری انجام می‌دهد

آنچه از ابتدا دریافت می‌کنید:

| قابلیت | چه چیزی دریافت می‌کنید |
|---|---|
| **گره‌های God** | متصل‌ترین مفاهیم، پس می‌بینید همه‌چیز از کجا عبور می‌کند |
| **جوامع** | گراف تقسیم‌شده به زیرسیستم‌ها (Leiden)، با برچسب‌های بدون LLM |
| **پیوندهای بین‌فایلی** | `calls` / `imports` / `inherits` / `mixes_in` حل‌شده در ~۴۰ زبان از طریق tree-sitter AST |
| **کوئری، مسیر، توضیح** | سؤالی بپرسید، مسیر بین دو چیز را دنبال کنید، یا یک مفهوم را توضیح دهید، همه در برابر `graph.json` |
| **دلیل + ارجاعات سند** | کامنت‌های `# NOTE:` / `# WHY:` و ارجاعات ADR/RFC به گره‌های درجه‌یک تبدیل می‌شوند که به کد متصل‌اند |
| **فراتر از کد** | اسناد، PDFها، تصاویر، و ویدیو/صدا همه در همان گراف نگاشت می‌شوند |
| **محلی‌محور** | کد به‌صورت محلی با tree-sitter تجزیه می‌شود (بدون LLM، هیچ‌چیز از دستگاه شما خارج نمی‌شود)؛ فقط گذر معنایی روی اسناد/رسانه یک backend را فراخوانی می‌کند، و فقط اگر آن را پیکربندی کنید |

---

## معیارهای سنجش (Benchmarks)

| معیار | متریک | graphify | حوزه |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | دقت QA | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | دقت QA | **76%** | برابر با dense RAG |
| ساخت گراف | اعتبار LLM | **0** | به‌ازای توکن برای بیشتر سیستم‌ها |

هر سیستم روی همان زیرساخت با همان مدل و بودجه اجرا شد، توسط داوری امتیازدهی شد که در برابر داور دوم به‌صورت کور اعتبارسنجی شده بود (۹۰.۶٪ توافق، کاپای کوهن ۰.۸۱). جداول کامل هر سیستم، نتیجه‌ی هوش کد، و دستورات بازتولید: **[BENCHMARKS.md](./BENCHMARKS.md)**.

---

## پیش‌نیازها

| نیازمندی | حداقل | بررسی | نصب |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(توصیه‌شده)* | هر نسخه | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(جایگزین)* | هر نسخه | `pipx --version` | `pip install pipx` |

**نصب سریع macOS (Homebrew):**
```bash
brew install python@3.12 uv
```

**نصب سریع Windows:**
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

## نصب

> **بسته‌ی رسمی:** بسته‌ی PyPI به‌صورت `graphifyy` است (دو تا y). بسته‌های دیگر `graphify*` در PyPI وابسته نیستند. دستور CLI همچنان `graphify` است.

**قدم ۱ — نصب بسته:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**قدم ۲ — ثبت skill با دستیار هوش مصنوعی شما:**

```bash
graphify install
```

همین. دستیار هوش مصنوعی خود را باز کنید و `/graphify .` را تایپ کنید.

برای نصب skill دستیار در مخزن فعلی به‌جای پروفایل کاربری خود، `--project` اضافه کنید:

```bash
graphify install --project
graphify install --project --platform codex
```

نصب‌های با محدوده‌ی پروژه در دایرکتوری فعلی می‌نویسند، برای مثال `.claude/skills/graphify/SKILL.md` یا `.agents/skills/graphify/SKILL.md` (به‌علاوه یک `references/` جانبی که skill آن را در صورت نیاز بارگذاری می‌کند)، و یک راهنمای `git add` برای فایل‌هایی که می‌توان کامیت کرد چاپ می‌کنند. دستورات به‌ازای هر پلتفرم که از نصب‌های با محدوده‌ی پروژه پشتیبانی می‌کنند همان فلگ را می‌پذیرند، برای مثال `graphify claude install --project` یا `graphify codex install --project`.

> **یادداشت PowerShell:** از `graphify .` استفاده کنید نه `/graphify .` — اسلش ابتدایی در PowerShell یک جداکننده‌ی مسیر است.

> **`graphify: command not found`؟** `uv tool install` / `pipx install` دستور `graphify` را در دایرکتوری bin ابزارهای خودشان (`~/.local/bin`) قرار می‌دهند. اگر شل شما بلافاصله بعد از نصب آن را پیدا نکند — رایج در یک نصب تازه‌ی macOS + zsh — آن دایرکتوری هنوز در `PATH` شما نیست: `uv tool update-shell` (یا `pipx ensurepath`) را اجرا کنید، سپس یک ترمینال جدید باز کنید. با `pip` ساده، `~/.local/bin` (Linux) یا `~/Library/Python/3.x/bin` (Mac) را به PATH خود اضافه کنید، یا `python -m graphify` را اجرا کنید.

> **اجرا با `uvx` / `uv tool run` به‌جای نصب؟** بسته را نام‌گذاری کنید، نه دستور را: `uvx --from graphifyy graphify install`. `uvx graphify …` ساده شکست می‌خورد (`No solution found … no versions of graphify`) چون `uv tool run` کلمه‌ی اول را به‌عنوان یک *بسته* می‌خواند، و بسته `graphifyy` است — دستور `graphify` درون آن زندگی می‌کند.

> **از `pip install` روی Mac/Windows پرهیز کنید** اگر ممکن است. skill در زمان اجرا Python را از `graphify-out/.graphify_python` حل می‌کند؛ اگر آن به محیطی متفاوت از جایی که `pip` بسته را نصب کرده اشاره کند، شما `ModuleNotFoundError: No module named 'graphify'` دریافت خواهید کرد. `uv tool install` و `pipx install` بسته را در محیط خودشان جدا می‌کنند و کاملاً از این جلوگیری می‌کنند.

> **Git hooks و uv tool / pipx:** `graphify hook install` مسیر مفسر فعلی را مستقیماً در اسکریپت‌های hook در زمان نصب جاسازی می‌کند، پس hook پس از commit حتی در کلاینت‌های گرافیکی git و اجراکننده‌های CI که `~/.local/bin` در PATH نیست به‌درستی فعال می‌شود. اگر graphify را دوباره نصب یا ارتقا دهید، `graphify hook install` را دوباره اجرا کنید تا مسیر جاسازی‌شده تازه شود.

> **حالت سخت‌گیرانه (Claude Code):** `graphify install --project --strict` باعث می‌شود دستیار واقعاً از گراف استفاده کند. نصب پیش‌فرض *تشویق* می‌کند که پیش از خواندن فایل‌ها `graphify query` اجرا شود؛ حالت سخت‌گیرانه اولین خواندن خام منبع در یک نشست را *مسدود* می‌کند و آن را به گراف هدایت مجدد می‌کند، سپس به تشویق بازمی‌گردد (پس حداکثر یک‌بار در هر نشست فعال می‌شود و هرگز گیر نمی‌کند). در زمان اجرا با `GRAPHIFY_HOOK_STRICT=1`/`0` جابه‌جا کنید؛ نصب پیش‌فرض بدون تغییر باقی می‌ماند (تشویق نرم).

<details>
<summary><b>پلتفرم خود را انتخاب کنید</b> (بیش از ۲۰ دستیار، برای گسترش کلیک کنید)</summary>

| پلتفرم | دستور نصب |
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

کاربران Codex همچنین برای استخراج موازی به `multi_agent = true` زیر `[features]` در `~/.codex/config.toml` نیاز دارند. CodeBuddy از همان مکانیزم Agent tool و PreToolUse hook مانند Claude Code استفاده می‌کند. Factory Droid از ابزار `Task` برای ارسال موازی subagent استفاده می‌کند. OpenClaw و Aider از استخراج ترتیبی استفاده می‌کنند (پشتیبانی از agent موازی هنوز در این پلتفرم‌ها ابتدایی است). Trae از ابزار Agent برای ارسال موازی subagent استفاده می‌کند و از hookهای `PreToolUse` پشتیبانی **نمی‌کند**، پس AGENTS.md مکانیزم همیشه-فعال است.

`--platform agents` (نام مستعار `--platform skills`) مکان‌های عمومی و cross-framework [Agent-Skills](https://github.com/anthropics/skills) را هدف می‌گیرد: `~/.agents/skills/` کاربر-سراسری مشخصات (که توسط `npx skills` و فریمورک‌های سازگار خوانده می‌شود) برای یک نصب سراسری، و `./.agents/skills/` برای یک نصب پروژه (`--project`). `graphify install` ساده طبق طراحی تک‌پلتفرمی (Claude Code) باقی می‌ماند — از پلتفرم نام‌گذاری‌شده‌ی `agents` استفاده کنید وقتی می‌خواهید skill توسط هر فریمورکی که `.agents/skills` را می‌خواند قابل کشف باشد.

> Codex از `$graphify` به‌جای `/graphify` استفاده می‌کند.

</details>

<details>
<summary><b>افزونه‌های اختیاری</b> (فقط آنچه نیاز دارید نصب کنید)</summary>

| افزونه | چه چیزی اضافه می‌کند | نصب |
|---|---|---|
| `pdf` | استخراج PDF | `uv tool install "graphifyy[pdf]"` |
| `office` | پشتیبانی از `.docx` و `.xlsx` | `uv tool install "graphifyy[office]"` |
| `google` | رندر Google Sheets | `uv tool install "graphifyy[google]"` |
| `video` | رونویسی ویدیو/صدا (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | سرور MCP stdio | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | پشتیبانی push از Neo4j | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | پشتیبانی push از FalkorDB | `uv tool install "graphifyy[falkordb]"` |
| `svg` | خروجی گراف SVG | `uv tool install "graphifyy[svg]"` |
| `leiden` | تشخیص جامعه‌ی Leiden (فقط Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | استنتاج محلی Ollama | `uv tool install "graphifyy[ollama]"` |
| `openai` | OpenAI / APIهای سازگار با OpenAI | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic Claude API (`--backend claude`، از `ANTHROPIC_API_KEY` استفاده می‌کند) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (از IAM استفاده می‌کند، بدون کلید API) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`، از `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT` استفاده می‌کند) | `uv tool install "graphifyy[openai]"` |
| `sql` | استخراج شمای SQL | `uv tool install "graphifyy[sql]"` |
| `postgres` | بازرسی زنده‌ی PostgreSQL (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | استخراج AST برای BYOND DreamMaker `.dm`/`.dme` (ممکن است به کامپایلر C + `python3-dev` نیاز داشته باشد اگر هیچ wheelی با پلتفرم شما مطابقت نداشته باشد) | `uv tool install "graphifyy[dm]"` |
| `terraform` | استخراج AST برای Terraform / HCL `.tf`/`.tfvars`/`.hcl` | `uv tool install "graphifyy[terraform]"` |
| `pascal` | استخراج AST برای Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` (یال‌های `calls`/`inherits` دقیق‌تر؛ در نبود آن به یک استخراج‌کننده‌ی regex بازمی‌گردد) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | تقسیم‌بندی کوئری چینی (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | همه‌ی موارد بالا | `uv tool install "graphifyy[all]"` |

</details>

---

## دستیار خود را وادار کنید همیشه از گراف استفاده کند

این را یک‌بار در پروژه‌ی خود پس از ساخت یک گراف اجرا کنید:

| پلتفرم | دستور |
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

این یک فایل پیکربندی کوچک می‌نویسد که به دستیار شما می‌گوید برای سؤالات مربوط به کدبیس با گراف دانش مشورت کند، و کوئری‌های محدود مانند `graphify query "<question>"` را به خواندن کل گزارش یا grep کردن فایل‌های خام ترجیح دهد.

- **پلتفرم‌های hook** (Claude Code، Gemini CLI): یک hook به‌طور خودکار پیش از فراخوانی‌های ابزار به‌سبک جست‌وجو فعال می‌شود (و، در Claude Code، پیش از خواندن فایل‌های منبع یکی‌یکی از طریق ابزارهای Read/Glob) و دستیار شما را به‌سمت مسیر گراف سوق می‌دهد.
- **پلتفرم‌های فایل دستورالعمل** (Codex، OpenCode، Cursor، و غیره): فایل‌های دستورالعمل دائمی (`AGENTS.md`، `.cursor/rules/`، و غیره) همان راهنمایی کوئری-اول را ارائه می‌دهند.

`GRAPH_REPORT.md` همچنان برای بازبینی گسترده‌ی معماری در دسترس است.

**CodeBuddy** همان دو کار Claude Code را انجام می‌دهد: یک بخش `CODEBUDDY.md` می‌نویسد که به CodeBuddy می‌گوید پیش از پاسخ به سؤالات معماری `graphify-out/GRAPH_REPORT.md` را بخواند، و hookهای `PreToolUse` (`.codebuddy/settings.json`) نصب می‌کند که پیش از دستورات جست‌وجوی Bash و خواندن فایل فعال می‌شوند، و به‌سمت `graphify query` سوق می‌دهند.

**Codex** به `AGENTS.md` می‌نویسد، که در این پلتفرم واقعاً راهنمایی همیشه-فعال گراف را حمل می‌کند. `graphify codex install` همچنین یک hook `PreToolUse` در `.codex/hooks.json` (`graphify hook-check`) ثبت می‌کند، اما آن ورودی عمداً **no-op** است: Codex Desktop `hookSpecificOutput.additionalContext` را روی `PreToolUse` رد می‌کند، پس ارسال یک تشویق آنجا فراخوانی‌های ابزار Bash را خراب می‌کرد. برخلاف Claude Code، جایی که hook (`graphify hook-guard`) تشویق می‌کند، در Codex hook فعال می‌شود و عمداً هیچ کاری نمی‌کند، و `AGENTS.md` مکانیزم همیشه-فعال است.

**Kilo Code** skill Graphify را در `~/.config/kilo/skills/graphify/SKILL.md` و یک دستور بومی `/graphify` را در `~/.config/kilo/command/graphify.md` نصب می‌کند. `graphify kilo install` همچنین `AGENTS.md` به‌علاوه یک افزونه‌ی بومی `tool.execute.before` (`.kilo/plugins/graphify.js` + ثبت `.kilo/kilo.json` یا `.kilo/kilo.jsonc`) می‌نویسد تا Kilo همان رفتار یادآوری گراف همیشه-فعال را از طریق پیکربندی بومی `.kilo` دریافت کند.

**Cursor** فایل `.cursor/rules/graphify.mdc` را با `alwaysApply: true` می‌نویسد، پس Cursor آن را به‌طور خودکار در هر مکالمه‌ای شامل می‌کند، بدون نیاز به hook.

برای حذف graphify از همه‌ی پلتفرم‌ها یک‌جا: `graphify uninstall` (برای حذف `graphify-out/` نیز `--purge` اضافه کنید). یا از دستور به‌ازای هر پلتفرم استفاده کنید (مثلاً `graphify claude uninstall`).

---

## در گزارش چه چیزی هست

- **گره‌های God** — متصل‌ترین مفاهیم در پروژه‌ی شما. همه‌چیز از این‌ها عبور می‌کند.
- **اتصالات شگفت‌انگیز** — پیوندهایی بین چیزهایی که در فایل‌ها یا ماژول‌های مختلف زندگی می‌کنند. رتبه‌بندی‌شده بر اساس میزان غیرمنتظره بودنشان.
- **"چرا"** — کامنت‌های درون‌خطی (`# NOTE:`، `# WHY:`، `# HACK:`)، docstringها، و دلیل طراحی از اسناد به‌عنوان گره‌های جداگانه‌ای استخراج می‌شوند که به کدی که توضیح می‌دهند متصل‌اند.
- **سؤالات پیشنهادی** — ۴ تا ۵ سؤال که گراف به‌طور منحصربه‌فرد برای پاسخ‌دهی به آن‌ها موقعیت دارد.
- **برچسب‌های اطمینان** — هر رابطه‌ی استنتاج‌شده با `EXTRACTED`، `INFERRED`، یا `AMBIGUOUS` علامت‌گذاری می‌شود. همیشه می‌دانید چه چیزی پیدا شده در برابر چه چیزی حدس زده شده.

---

## این چه فایل‌هایی را مدیریت می‌کند

| نوع | پسوندها |
|------|-----------|
| کد (۳۶ گرامر tree-sitter) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme` نیازمند `uv tool install graphifyy[dm]`؛ `.mts`/`.cts` گرامر TypeScript را دوباره استفاده می‌کنند، `.cc`/`.cxx` و CUDA `.cu`/`.cuh` و Metal `.metal` گرامر C++ را دوباره استفاده می‌کنند) |
| Salesforce Apex | `.cls .trigger` (مبتنی بر regex؛ کلاس‌ها، رابط‌ها، enumها، متدها، triggerها، یال‌های SOQL/DML) |
| Terraform / HCL | `.tf .tfvars .hcl` (نیازمند `uv tool install graphifyy[terraform]`) |
| پیکربندی‌های MCP | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — گره‌های سرور، ارجاعات بسته، نیازمندی‌های متغیر محیطی را استخراج می‌کند |
| مانیفست‌های بسته | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — یک گره‌ی بسته‌ی متعارف به‌ازای هر بسته (بر اساس نام) به‌علاوه یال‌های `depends_on`، پس بسته‌ای که از مانیفست‌های زیادی ارجاع داده شده یک hub واحد است |
| اسناد | `.md .mdx .qmd .html .txt .rst .yaml .yml` (لینک‌های markdown `[text](./other.md)` و `[[wikilinks]]` به یال‌های `references` بین اسناد تبدیل می‌شوند) |
| Office | `.docx .xlsx` (نیازمند `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (اختیاری؛ نیازمند احراز هویت `gws` و `--google-workspace`؛ Sheets به `uv tool install graphifyy[google]` نیاز دارد) |
| PDFها | `.pdf` |
| تصاویر | `.png .jpg .webp .gif` |
| ویدیو / صدا | `.mp4 .mov .mp3 .wav` و بیشتر (نیازمند `uv tool install graphifyy[video]`) |
| YouTube / URLها | هر URL ویدیویی (نیازمند `uv tool install graphifyy[video]`) |

کد **به‌صورت محلی بدون فراخوانی API** استخراج می‌شود (AST از طریق tree-sitter). همه‌چیز دیگر از طریق API مدل دستیار هوش مصنوعی شما عبور می‌کند.

فایل‌های `.gdoc`، `.gsheet`، و `.gslides` مربوط به Google Drive for desktop اشاره‌گرهای میان‌بر هستند، نه محتوای سند. برای شامل کردن Google Docs، Sheets، و Slides بومی در یک استخراج headless، [`gws` CLI](https://github.com/googleworkspace/cli) را نصب و احراز هویت کنید، سپس اجرا کنید:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

می‌توانید `GRAPHIFY_GOOGLE_WORKSPACE=1` را نیز تنظیم کنید. Graphify میان‌برها را به‌صورت Markdown جانبی در `graphify-out/converted/` صادر می‌کند، سپس آن فایل‌ها را استخراج می‌کند.

---

## دستورات رایج

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

به [Decouple: کاندیدهای Extract-Class با امتیاز ریسک](#decouple-risk-scored-extract-class-candidates) در بالا، یا [مرجع کامل دستورات](#full-command-reference) در پایین مراجعه کنید.

---

## نادیده گرفتن فایل‌ها

یک `.graphifyignore` در ریشه‌ی پروژه‌ی خود ایجاد کنید — همان نحو `.gitignore`، شامل نفی `!`.

**`.gitignore` به‌طور خودکار رعایت می‌شود.** graphify در هر دایرکتوری `.gitignore` را می‌خواند. اگر یک `.graphifyignore` نیز وجود داشته باشد، این دو **ادغام** می‌شوند — الگوهای `.graphifyignore` آخر ارزیابی می‌شوند، پس در تعارضات برنده می‌شوند (شامل نفی‌های `!`). افزودن یک `.graphifyignore` فقط بیشتر مستثنی می‌کند؛ هرگز فایلی را که `.gitignore` شما قبلاً مستثنی کرده دوباره شامل نمی‌کند. محدوده‌بندی زیردایرکتوری دقیقاً مانند git کار می‌کند — یک فایل ignore فقط زیردرخت خودش را تحت تأثیر قرار می‌دهد.

`--no-gitignore` را به `graphify extract` بدهید وقتی کد git-ignored شده‌ی تولیدشده یا transpile‌شده باید در گراف باشد. این `.gitignore` و `.git/info/exclude` را غیرفعال می‌کند؛ `.graphifyignore` همچنان اعمال می‌شود.

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

## راه‌اندازی تیم

`graphify-out/` قرار است در git کامیت شود تا همه‌ی اعضای تیم با یک نقشه شروع کنند.

**افزودنی‌های پیشنهادی به `.gitignore`:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` اکنون قابل‌حمل است — کلیدها به‌صورت مسیرهای نسبی ذخیره می‌شوند و در بارگذاری دوباره لنگر می‌شوند، پس کامیت کردن آن امن است و از بازسازی کامل در اولین checkout جلوگیری می‌کند.

**گردش کار:**
۱. یک نفر `/graphify .` را اجرا می‌کند و `graphify-out/` را کامیت می‌کند.
۲. همه pull می‌کنند — دستیار آن‌ها بلافاصله گراف را می‌خواند.
۳. `graphify hook install` را برای بازسازی خودکار پس از هر کامیت اجرا کنید (فقط AST، بدون هزینه‌ی API). این همچنین یک git merge driver راه‌اندازی می‌کند تا `graph.json` هرگز با نشانگرهای تعارض باقی نماند — دو توسعه‌دهنده که به‌صورت موازی کامیت می‌کنند گراف‌های خود را به‌طور خودکار union-merge شده دریافت می‌کنند.
۴. وقتی اسناد یا مقالات تغییر می‌کنند، `/graphify --update` را اجرا کنید تا آن گره‌ها تازه شوند.

---

## استفاده‌ی مستقیم از گراف

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

سرور MCP به دستیار شما دسترسی ساختاریافته می‌دهد: `query_graph`، `get_node`، `get_neighbors`، `shortest_path`، `list_prs`، `get_pr_impact`، `triage_prs`.

### سرور HTTP مشترک

`--transport stdio` (پیش‌فرض) یک سرور محلی به‌ازای هر توسعه‌دهنده اجرا می‌کند. `--transport http` همان ابزارها را روی transport MCP Streamable HTTP سرو می‌کند، پس یک فرآیند مشترک واحد می‌تواند گراف را برای کل تیم سرو کند — کلاینت‌ها پیکربندی MCP IDE خود را به‌جای اجرای محلی graphify به سمت `http://<host>:8080/mcp` اشاره می‌دهند.

| فلگ | پیش‌فرض | هدف |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Transport برای سرو کردن |
| `--host` | `127.0.0.1` | میزبان bind شونده‌ی HTTP (از `0.0.0.0` برای در معرض قرار دادن فراتر از localhost استفاده کنید) |
| `--port` | `8080` | پورت bind شونده‌ی HTTP |
| `--api-key` | env `GRAPHIFY_API_KEY` | نیازمند `Authorization: Bearer <key>` (یا `X-API-Key`) |
| `--path` | `/mcp` | مسیر mount شونده‌ی HTTP |
| `--json-response` | خاموش | به‌جای جریان‌های SSE، JSON ساده برمی‌گرداند |
| `--stateless` | خاموش | بدون state به‌ازای هر نشست (برای استقرارهای load-balanced / CI) |
| `--session-timeout` | `3600` | نشست‌های stateful غیرفعال را پس از N ثانیه پاک می‌کند (`0` غیرفعال می‌کند) |

اتصال پیش‌فرض `127.0.0.1` فقط loopback است. هنگام در معرض قرار دادن روی یک میزبان مشترک، `--host 0.0.0.0` **و** `--api-key` را با هم تنظیم کنید. آن را در یک کانتینر اجرا کنید:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **یادداشت WSL / Linux:** Ubuntu `python3` را ارائه می‌دهد، نه `python`. برای اجتناب از تعارضات از یک venv استفاده کنید:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## متغیرهای محیطی

این‌ها فقط برای استخراج **headless / CI** (`graphify extract`) لازم‌اند. وقتی از طریق skill `/graphify` درون IDE خود اجرا می‌شود، API مدل توسط نشست IDE شما فراهم می‌شود — کلید اضافی لازم نیست.

| متغیر | برای چه استفاده می‌شود | چه زمانی لازم است |
|---|---|---|
| `ANTHROPIC_API_KEY` | backend Claude (Anthropic) | `--backend claude` |
| `ANTHROPIC_BASE_URL` | URL نقطه‌پایانی سازگار با Anthropic (پروکسی LiteLLM، gatewayها، ...) | `--backend claude` (پیش‌فرض: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | نام مدل برای backend Claude — برای نقطه‌پایانی‌های سفارشی، از نام/نام‌مستعار مدلی که سرور شما ارائه می‌دهد استفاده کنید | `--backend claude` (پیش‌فرض: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` یا `GOOGLE_API_KEY` | backend Google Gemini | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI یا APIهای سازگار با OpenAI | `--backend openai` (سرورهای محلی هر مقدار غیرخالی را می‌پذیرند) |
| `OPENAI_BASE_URL` | URL سرور سازگار با OpenAI (llama.cpp، vLLM، LM Studio، ...) | `--backend openai` (پیش‌فرض: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | نام مدل برای backend OpenAI — برای سرورهای self-hosted، از نام/نام‌مستعار مدلی که سرور شما ارائه می‌دهد استفاده کنید (نقطه‌پایانی `/v1/models` آن را بررسی کنید)، مثلاً `LFM2.5-8B-A1B-UD-Q4_K_XL` برای llama.cpp | `--backend openai` (پیش‌فرض: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | backend DeepSeek | `--backend deepseek` |
| `MOONSHOT_API_KEY` | backend Kimi Code | `--backend kimi` |
| `OLLAMA_BASE_URL` | URL استنتاج محلی Ollama | `--backend ollama` (پیش‌فرض: `http://localhost:11434`) |
| `OLLAMA_MODEL` | نام مدل Ollama | `--backend ollama` (پیش‌فرض: تشخیص خودکار) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | اندازه‌ی پنجره‌ی KV-cache Ollama را بازنویسی می‌کند | اختیاری — به‌طور پیش‌فرض به‌صورت خودکار اندازه‌دهی می‌شود |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | دقایقی که مدل Ollama بارگذاری‌شده باقی می‌ماند | اختیاری — برای تخلیه پس از هر تکه `0` تنظیم کنید |
| `AZURE_OPENAI_API_KEY` | backend Azure OpenAI Service | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | URL نقطه‌پایانی منبع Azure | `--backend azure` (همراه با کلید API لازم است) |
| `AZURE_OPENAI_API_VERSION` | بازنویسی نسخه‌ی API Azure | اختیاری — پیش‌فرض `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` یا `GRAPHIFY_AZURE_MODEL` | نام deployment Azure | اختیاری — پیش‌فرض `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — زنجیره‌ی استاندارد گواهی | `--backend bedrock` (بدون کلید API، از IAM استفاده می‌کند) |
| `GRAPHIFY_MAX_WORKERS` | تعداد thread موازی‌سازی AST | اختیاری — همچنین فلگ `--max-workers` |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | سقف خروجی را برای پیکره‌های متراکم افزایش دهید | اختیاری — مثلاً `32768` برای فایل‌های بزرگ |
| `GRAPHIFY_API_TIMEOUT` | مهلت زمانی به‌ازای هر فراخوانی به ثانیه برای backendهای HTTP، claude-cli، Anthropic SDK، و Bedrock (پیش‌فرض: 600) | اختیاری — همچنین فلگ `--api-timeout` |
| `GRAPHIFY_MAX_RETRIES` | چند بار یک درخواست rate-limited (429) را پیش از تسلیم شدن دوباره امتحان کند (پیش‌فرض: 6؛ به `Retry-After` احترام می‌گذارد) | اختیاری — برای محدودیت‌های سخت‌گیرانه‌ی هر سازمان افزایش دهید (مثلاً kimi)؛ `0` غیرفعال می‌کند |
| `GRAPHIFY_FORCE` | بازسازی گراف را حتی با گره‌های کمتر مجبور کنید | اختیاری — همچنین فلگ `--force` |
| `GRAPHIFY_GOOGLE_WORKSPACE` | صادرات Google Workspace را به‌طور خودکار فعال کنید | اختیاری — روی `1` تنظیم کنید |
| `GRAPHIFY_TRIAGE_BACKEND` | backend برای `graphify prs --triage` | اختیاری — از کلیدهای موجود به‌طور خودکار تشخیص داده می‌شود |
| `GRAPHIFY_TRIAGE_MODEL` | بازنویسی مدل برای triage | اختیاری — مثلاً `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | روی `1` تنظیم کنید تا لاگ محلی کوئری در `~/.cache/graphify-queries.log` روشن شود (هر سؤال query/path/explain + مسیر پیکره را ثبت می‌کند). پیش‌فرض خاموش — تا زمانی که opt in نکنید چیزی نوشته نمی‌شود (#1797) | اختیاری |
| `GRAPHIFY_QUERY_LOG` | لاگ کوئری را فعال می‌کند و به‌جای پیش‌فرض در این مسیر می‌نویسد | اختیاری — خاموش مگر اینکه این یا `_ENABLE` تنظیم شود |
| `GRAPHIFY_QUERY_LOG_DISABLE` | روی `1` تنظیم کنید تا لاگ کوئری اجباراً خاموش شود (بر متغیرهای enable غالب می‌شود) | اختیاری |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | وقتی لاگ روشن است، پاسخ‌های کامل زیرگراف را نیز ثبت می‌کند (پیش‌فرض خاموش) | اختیاری |
| `GRAPHIFY_MAX_GRAPH_BYTES` | سقف اندازه‌ی ۵۱۲ MiB برای graph.json را بازنویسی کنید — مثلاً `700MB`، `2GB`، یا بایت‌های ساده | اختیاری — برای پیکره‌های بسیار بزرگ مفید |
| `GRAPHIFY_MAX_CONTEXTS` | حداکثر تعداد گراف‌های پروژه‌ی غیرپیش‌فرض که یک سرور MCP چندپروژه‌ای نگه می‌دارد | اختیاری — پیش‌فرض: `8`؛ مقادیر نامعتبر از `8` استفاده می‌کنند، و مقادیر زیر `1` از `1` استفاده می‌کنند |
| `GRAPHIFY_LLM_TEMPERATURE` | دمای LLM را برای استخراج معنایی بازنویسی کنید — مثلاً `0.7`، یا `none` برای حذف | اختیاری — برای مدل‌های استدلال o1/o3/o4/gpt-5 به‌طور خودکار حذف می‌شود |

---

## حریم خصوصی

- **فایل‌های کد** — به‌صورت محلی از طریق tree-sitter پردازش می‌شوند. هیچ‌چیز از دستگاه شما خارج نمی‌شود. یک پیکره‌ی فقط-کد به هیچ کلید APIای نیاز ندارد — `graphify extract` کاملاً آفلاین اجرا می‌شود. در یک مخزن مختلط، `--code-only` را اضافه کنید تا فقط کد را ایندکس کنید و اسناد/PDFها/تصاویری را که در غیر این صورت به LLM نیاز داشتند رد شوید.
- **ویدیو / صدا** — به‌صورت محلی با faster-whisper رونویسی می‌شوند. هیچ‌چیز از دستگاه شما خارج نمی‌شود.
- **اسناد، PDFها، تصاویر** — برای استخراج معنایی به دستیار هوش مصنوعی شما ارسال می‌شوند (از طریق skill `/graphify`، با استفاده از هر مدلی که نشست IDE شما اجرا می‌کند). `graphify extract` به‌صورت headless به `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini)، `MOONSHOT_API_KEY` (Kimi)، `ANTHROPIC_API_KEY` (Claude)، `OPENAI_API_KEY` (OpenAI)، `DEEPSEEK_API_KEY` (DeepSeek)، یک نمونه‌ی در حال اجرای Ollama (`OLLAMA_BASE_URL`)، گواهی‌های AWS از طریق زنجیره‌ی استاندارد ارائه‌دهنده (Bedrock - بدون نیاز به کلید API، از IAM استفاده می‌کند)، یا باینری CLI `claude` (Claude Code - بدون نیاز به کلید API، از اشتراک Claude شما استفاده می‌کند) نیاز دارد. فلگ `--dedup-llm` از همان کلید استفاده می‌کند.
- **محل نگهداری داده** — `graphify extract` به‌طور خودکار بر اساس اینکه کدام کلید API تنظیم شده تشخیص می‌دهد از کدام ارائه‌دهنده استفاده کند (اولویت: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). برای کدی با نیازمندی‌های محل نگهداری داده، از `--backend ollama` (کاملاً محلی) استفاده کنید یا یک فلگ `--backend` صریح بدهید. Kimi (`MOONSHOT_API_KEY`) به سرورهای Moonshot AI در چین مسیریابی می‌کند.
- **بدون تله‌متری**، بدون ردیابی استفاده، بدون تحلیل.
- **لاگ‌گیری کوئری** — هر فراخوانی `graphify query`، `graphify path`، `graphify explain`، و MCP `query_graph` در قالب JSON Lines در `~/.cache/graphify-queries.log` ثبت می‌شود (زمان، سؤال، پیکره، گره‌های بازگردانده‌شده، مدت). پاسخ‌های کامل زیرگراف به‌طور پیش‌فرض ذخیره **نمی‌شوند**. برای انصراف `GRAPHIFY_QUERY_LOG_DISABLE=1` را تنظیم کنید، یا برای خاموش کردن بدون غیرفعال کردن مسیر کد `GRAPHIFY_QUERY_LOG=/dev/null` را تنظیم کنید.

---

## محدودیت‌ها و مرزها

آنچه graphify عمداً انجام **نمی‌دهد**، و جایی که پوشش آن متوقف می‌شود:

- **یک موتور جستجوی معنایی/برداری (vector) نیست.** گراف ساختاری است — گره‌ها و یال‌های تایپ‌شده‌ای که از منبع حل‌وفصل شده‌اند، نه embedding. `graphify query`/`path`/`explain` این ساختار را پیمایش می‌کنند؛ آن‌ها نمی‌توانند اتصالی را که به‌صورت یال نمایش داده نشده آشکار کنند، حتی اگر «از نظر معنایی» مرتبط باشد. هیچ راه‌حل جایگزین بر پایه‌ی شباهت/نزدیک‌ترین همسایه وجود ندارد.
- **اسناد، PDFها، تصاویر، و استخراج ویدیو/URL به‌صورت headless، صرفاً محلی نیستند.** فقط کد (tree-sitter AST) و رونویسی صدا/ویدیو (faster-whisper) کاملاً آفلاین اجرا می‌شوند. استخراج اسناد/PDFها/تصاویر همیشه یک LLM را فرا می‌خواند — مدل دستیار هوش مصنوعی شما از طریق skill `/graphify`، یا یک کلید API بک‌اند پیکربندی‌شده برای `graphify extract` به‌صورت headless. برای اینکه دقیقاً بدانید هر مسیر به کدام فلگ یا کلید نیاز دارد، به [حریم خصوصی](#حریم-خصوصی) در بالا مراجعه کنید.
- **بررسی اشتراک‌گذاری state در decouple همه‌ی زبان‌ها را پوشش نمی‌دهد.** زبان C بدون استنتاج کامل نوع، سیگنال `self`/`this` قابل‌اعتمادی ندارد، بنابراین مستثنا شده است (به [جدول پوشش زبان‌ها](#decouple-risk-scored-extract-class-candidates) در بالا مراجعه کنید). یک گره god در یک زبان پشتیبانی‌نشده، یا یکی که منبعش قابل خواندن نیست، به‌جای بررسی state تأییدشده، به امتیازدهی فقط بر پایه‌ی گراف فراخوانی برمی‌گردد (`state_analysis: "skipped"`).
- **سطح جریان داده‌ی سه‌بعدی یک اکتشاف مبتنی بر نام است، نه تحلیل جریان داده/taint.** تشخیص مرز I/O در `data_floor` (parserها، loaderها، readerها، writerها، کلاینت‌های DB/HTTP) بر اساس تطبیق قراردادهای نام‌گذاری (`boundary_reason`) است؛ ممکن است یک گره‌ی مرزی با نامی غیرمتعارف نادیده گرفته شود، که عمق واقعی باقی گراف را کمتر از حد نشان می‌دهد.
- **برچسب‌های اطمینان، اطمینان تفسیر خود graphify هستند، نه حقیقت مطلق.** یال‌های `INFERRED` و `AMBIGUOUS` راه‌حل‌های بهترین‌تلاش هستند و همچنان می‌توانند اشتباه باشند، به‌خصوص برای الگوهای بسیار پویا (reflection، dispatch در زمان اجرا، متاپروگرمینگ) که هیچ پاس AST ایستایی نمی‌تواند آن‌ها را کاملاً حل کند.
- **تجسم HTML و اندازه‌ی گراف هر دو سقف دارند.** `graph.html` / `DECOUPLE.html` به‌طور پیش‌فرض تولید را بالای ۵۰۰۰ گره رد می‌کنند (`MAX_NODES_FOR_VIZ`، از طریق `GRAPHIFY_VIZ_NODE_LIMIT` افزایش دهید)؛ خود `graph.json` به ۵۱۲ مگابایت محدود شده است (`GRAPHIFY_MAX_GRAPH_BYTES` برای لغو). برای پیکره‌هایی فراتر از هر یک از این محدودیت‌ها، از `--no-viz` به‌همراه `query`/`path`/`explain` استفاده کنید.
- **آگاهی بین‌پروژه‌ای اختیاری (opt-in) است، نه خودکار.** `graphify query` فقط همان یک گرافی را می‌بیند که شما به آن اشاره می‌کنید. سؤالات چندمخزنی ابتدا نیاز به ثبت صریح هر پروژه در گراف مشترک دارند (`graphify global add`، با سقف `GRAPHIFY_MAX_CONTEXTS` پیکره‌ی غیرپیش‌فرض به‌ازای هر سرور MCP) — graphify هرگز به‌خودی‌خود دستگاه شما را برای مخزن‌های دیگر اسکن نمی‌کند.
- **استخراج موازی چندعامله به پلتفرم بستگی دارد.** این کار به پشتیبانی دستیار برای ایجاد ساب‌ایجنت نیاز دارد (`multi_agent = true` در `~/.codex/config.toml` برای Codex، ابزار Agent/Task در Claude Code/CodeBuddy/Factory Droid/Trae). OpenClaw و Aider در حال حاضر فقط به‌صورت ترتیبی استخراج می‌کنند.
- **سرور مشترک MCP HTTP به‌طور پیش‌فرض فقط loopback است.** دسترسی به آن از دستگاهی دیگر به تنظیم صریح `--host 0.0.0.0` **و** `--api-key` نیاز دارد؛ graphify نه TLS را مدیریت می‌کند و نه هیچ احراز هویتی فراتر از همان یک bearer token.
- **PowerShell علامت `/` ابتدایی را به‌عنوان جداکننده‌ی مسیر تفسیر می‌کند.** به همین دلیل `/graphify .` در Windows PowerShell شکست می‌خورد، نه به‌خاطر باگی در graphify — در عوض از `graphify .` استفاده کنید.

---

## عیب‌یابی

**`graphify: command not found` پس از نصب**
CLI نصب شده اما دایرکتوری bin آن در `PATH` شل شما نیست. اصلاح متناسب با نحوه‌ی نصب خود را انتخاب کنید:
- **uv** (`uv tool install graphifyy`): دستور به دایرکتوری bin ابزارهای uv (`~/.local/bin`) می‌رود، که یک نصب تازه‌ی macOS/zsh اغلب آن را در `PATH` ندارد. `uv tool update-shell` را اجرا کنید، سپس یک ترمینال جدید باز کنید. (دایرکتوری را با `uv tool dir --bin` پیدا کنید.)
- **pipx** (`pipx install graphifyy`): `pipx ensurepath` را اجرا کنید، سپس یک ترمینال جدید باز کنید.
- **pip** (`pip install graphifyy`): pip اسکریپت‌ها را در دایرکتوری bin کاربر نصب می‌کند که ممکن است در `PATH` نباشد — `~/Library/Python/3.x/bin` (macOS) یا `~/.local/bin` (Linux) را در `~/.zshrc`/`~/.bashrc` به `PATH` خود اضافه کنید، یا فقط `python -m graphify` را اجرا کنید.

**`uvx graphify …` یا `uv tool run graphify …` نمی‌تواند `graphify` را حل کند**
بسته‌ی PyPI `graphifyy` است؛ `graphify` فقط دستوری است که ارائه می‌دهد. `uv tool run` کلمه‌ی اول را به‌عنوان یک *نام بسته* در نظر می‌گیرد، پس به‌دنبال بسته‌ای با نام `graphify` می‌گردد و گزارش می‌دهد `No solution found … no versions of graphify`. بسته را صریحاً نام‌گذاری کنید: `uvx --from graphifyy graphify install` (مانند `uv tool run --from graphifyy graphify install`). یا `uv tool install graphifyy` را یک‌بار انجام دهید و سپس مستقیماً `graphify` را فراخوانی کنید.

**`uv run --with graphifyy python -m graphify` بی‌صدا یک نصب قدیمی‌تر را اجرا می‌کند**
`uv run` از Python *سیستم* شما استفاده می‌کند، پس اگر یک `graphifyy` قدیمی‌تر نیز آنجا زندگی کند (مثلاً یک `pip install graphifyy` قبلی)، Python ممکن است ابتدا آن نسخه را در `sys.path` پیدا کند و `--with graphifyy` آن را بازنویسی نکند. بدون خطا اجرا می‌شود، اما رفتار نسخه‌ی *قدیمی* را دریافت می‌کنید — مثلاً بازنویسی‌های محیطی مانند `OPENAI_BASE_URL` بی‌صدا نادیده گرفته می‌شوند، پس درخواست‌ها به نقطه‌پایانی پیش‌فرض می‌خورند و با 401 که شبیه یک کلید بد است شکست می‌خورند. اثر انگشت یک خط `warning: skill is from graphify <newer>, package is <older>` است — این یعنی نصب متفاوتی بارگذاری شده، نه فقط یک skill قدیمی. بررسی کنید کدام نسخه واقعاً بارگذاری شده:
```bash
python -c "import graphify; print(graphify.__file__)"
```
سپس دستور نصب‌شده را مستقیماً اجرا کنید (از نسخه‌ی مدیریت‌شده توسط uv استفاده می‌کند)، یا نسخه‌ی قدیمی سیستم را حذف کنید:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` کار می‌کند اما دستور `graphify` نه**
`PATH` شل شما شامل دایرکتوری binی که دستور در آن نصب شده نیست. به‌جای `pip` ساده، `uv tool install` / `pipx install` را ترجیح دهید، سپس `uv tool update-shell` / `pipx ensurepath` را اجرا کنید و یک ترمینال جدید باز کنید (یادداشت‌های نصب بالا را ببینید).

**`/graphify .` در PowerShell باعث "path not recognized" می‌شود**
PowerShell اسلش ابتدایی را به‌عنوان یک جداکننده‌ی مسیر در نظر می‌گیرد. روی Windows از `graphify .` (بدون اسلش) استفاده کنید.

**پس از `--update` یا بازسازی، گراف گره‌های کمتری دارد**
اگر یک بازآرایی فایل‌هایی را حذف کرده باشد، گره‌های قدیمی باقی می‌مانند. `--force` (یا `GRAPHIFY_FORCE=1` را تنظیم کنید) بدهید تا حتی وقتی بازسازی گره‌های کمتری دارد بازنویسی شود.

**`extract` با "extraction was incomplete ... refusing to overwrite" خارج می‌شود**
وقتی یک مرحله‌ی استخراج خراب می‌شود یا یک پیمایش نمی‌تواند پیکره را کاملاً بخواند، اجرا کوچک‌تر از یک اجرای کامل خواهد بود، پس `graphify extract` از بازنویسی یک گراف بزرگ‌تر موجود با نتیجه‌ی جزئی خودداری می‌کند (از `graph.json` شما محافظت می‌کند). خرابی زیربنایی را برطرف کنید و دوباره اجرا کنید، یا برای بازنویسی به‌هرحال `--allow-partial` بدهید.

**گراف کپی‌های تکراری برای همان موجودیت دارد (کپی‌های شبح)**
کپی‌های شبح (همان نماد دو بار ظاهر می‌شود — یک‌بار از استخراج AST با موقعیت منبع، یک‌بار از استخراج معنایی بدون آن) اکنون به‌طور خودکار در زمان ساخت ادغام می‌شوند. اگر این را در گرافی که پیش از v0.8.33 ساخته شده می‌بینید، برای پاک‌سازی یک استخراج مجدد کامل اجرا کنید:
```bash
graphify extract . --force
```

**Ollama از VRAM تمام می‌شود / پنجره‌ی context عبور می‌کند**
پنجره‌ی KV-cache به‌طور خودکار اندازه‌دهی می‌شود اما ممکن است برای GPU شما خیلی بزرگ باشد. آن را کاهش دهید:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**هشدارهای `LLM returned invalid JSON` / `Unterminated string`**
پاسخ JSON مدل به سقف توکن خروجی رسیده و در وسط رشته قطع شده. graphify به‌طور خودکار بازیابی می‌کند (تکه را تقسیم می‌کند و نیمه‌ها را دوباره استخراج می‌کند، و یک سند تک بیش‌ازحد بزرگ ابتدا در مرزهای تیتر/پاراگراف تکه‌تکه می‌شود تا کل فایل همچنان پوشش داده شود)، پس این هشدارها پرسروصدا اما نه از دست رفتن داده هستند. برای کاهش سروصدا، سقف خروجی را افزایش دهید یا خروجی هر تکه را کاهش دهید:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
با یک gateway ابری مانند OpenRouter، `--backend openai` (تنظیم `OPENAI_BASE_URL`) را به shim Ollama ترجیح دهید — یک مسیر تمیزتر و سازگار با OpenAI است. اگر مدل سقف max-output خودش را دارد، کاهش `--token-budget` یک اهرم قابل‌اعتماد است.

**Graph HTML برای باز کردن در مرورگر خیلی بزرگ است (بیش از ۵۰۰۰ گره)**
از تولید HTML صرف‌نظر کنید و مستقیماً از JSON استفاده کنید:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**پس از کامیت هم‌زمان دو توسعه‌دهنده، `graph.json` نشانگرهای تعارض دارد**
`graphify hook install` را اجرا کنید — یک git merge driver راه‌اندازی می‌کند که `graph.json` را به‌طور خودکار union-merge می‌کند تا تعارض‌ها هرگز رخ ندهند.

**استخراج برای اسناد یا PDFها گره‌ها/یال‌های خالی برمی‌گرداند**
اسناد، PDFها، و تصاویر به یک فراخوانی LLM نیاز دارند — پیکره‌های فقط-کد به کلیدی نیاز ندارند. بررسی کنید کلید API شما تنظیم شده و backend درست است:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**هشدار عدم تطابق نسخه‌ی skill در IDE شما**
نسخه‌ی نصب‌شده‌ی graphify شما با فایل skill متفاوت است. به‌روزرسانی کنید:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**کش prompt در Claude Code پس از هر `graphify extract` باطل می‌شود**
Graphify فایل‌های خروجی (`graph.json`، `graphify-out/`) را در فضای کاری می‌نویسد. اگر آن مسیرها ignore نشده باشند، هر نوشتاری کش prompt در Claude Code را باطل می‌کند، و در نوبت بعدی با نرخ‌های نوشتن کش یک آپلود مجدد کامل را مجبور می‌کند. آن‌ها را به `.claudeignore` اضافه کنید:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## مرجع کامل دستورات

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

> **نام‌های جامعه:** درون یک agent (Claude Code، Gemini CLI) خودِ agent جوامع را نام‌گذاری می‌کند. وقتی CLI خام را اجرا می‌کنید، `cluster-only` آن‌ها را به‌طور خودکار با backend پیکربندی‌شده (داخلی یا ارائه‌دهنده‌ی سفارشی سازگار با OpenAI) نام‌گذاری می‌کند — برای حفظ `Community N` `--no-label` بدهید، یا برای تولید (مجدد) نام‌ها در صورت تقاضا `graphify label` را اجرا کنید.

---

## بیشتر بدانید

- [چگونه کار می‌کند](docs/how-it-works.md) — خط لوله‌ی استخراج، تشخیص جامعه، امتیازدهی اطمینان، معیارها
- [ARCHITECTURE.md](ARCHITECTURE.md) — تجزیه‌ی ماژول، چگونه یک زبان اضافه کنیم
- [یکپارچه‌سازی‌های اختیاری](docs/docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — کتاب درباره‌ی ایده‌های پشت graphify، معماری از ابتدا تا انتها

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) لایه‌ی همیشه-فعالی است که روی graphify ساخته شده — همان رویکرد گراف را روی کل زمینه‌ی کاری شما اعمال می‌کند: جلسات، فایل‌ها، اسناد، و کد، با به‌روزرسانی مداوم در پس‌زمینه.

ساخته‌شده برای افراد و تیم‌هایی که کارشان در صدها مکالمه و سندی زندگی می‌کند که هرگز نمی‌توانند به‌طور کامل بازسازی کنند.

**[به لیست انتظار در graphify.com بپیوندید](https://graphify.com).** آزمایش رایگان به‌زودی راه‌اندازی می‌شود.

---

<details>
<summary>مشارکت</summary>

### راه‌اندازی محیط توسعه

پروژه از [uv](https://docs.astral.sh/uv/) برای گردش کار توسعه استفاده می‌کند. یک‌بار آن را نصب کنید، سپس:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

نصب editable را تأیید کنید:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### اجرای تست‌ها

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> یادداشت macOS: مجموعه‌ی تست شامل هر دو fixture `sample.f90` و `sample.F90` است. این‌ها روی سیستم‌های فایل حساس‌نبودن به بزرگی-کوچکی مانند HFS+ / APFS تصادم می‌کنند. اگر نیاز به تست همزمان هر دو نوع Fortran دارید، روی Linux یا در یک کانتینر Docker اجرا کنید.

### گردش کار Git

- توسعه‌ی فعال روی شاخه‌ی `v8` انجام می‌شود.
- سبک کامیت: `fix: <description>` / `feat: <description>` / `docs: <description>`
- پیش از باز کردن یک PR، `uv run pytest tests/ -q` را اجرا کنید و تأیید کنید که موفق می‌شود.
- برای هر استخراج‌کننده‌ی زبان جدید، یک فایل fixture به `tests/fixtures/` و تست‌ها به `tests/test_languages.py` اضافه کنید.

### چه چیزی مشارکت دهیم

**مثال‌های کارشده** مفیدترین مشارکت هستند. `/graphify` را روی یک پیکره‌ی واقعی اجرا کنید، خروجی را در `worked/{slug}/` ذخیره کنید، یک `review.md` صادقانه بنویسید که پوشش می‌دهد گراف چه چیزی را درست و چه چیزی را غلط انجام داد، و یک PR باز کنید.

**باگ‌های استخراج** — با فایل ورودی، ورودی کش (`graphify-out/cache/`)، و آنچه از دست رفته یا اشتباه بود یک issue باز کنید.

برای مسئولیت‌های ماژول و چگونگی افزودن یک زبان، [ARCHITECTURE.md](ARCHITECTURE.md) را ببینید.

</details>
