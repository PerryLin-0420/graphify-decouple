<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>نسخة مُشتقة (fork) من <a href="https://github.com/Graphify-Labs/graphify">graphify</a> تضيف <code>graphify decouple</code></b> — مرشحات Extract-Class مصنفة حسب المخاطر بدون أي LLM (0-LLM) لكائنات God Object، يُعاد التحقق منها في مقابل الشيفرة المصدرية الفعلية (لا رسم بياني الاستدعاءات فقط) قبل أن توصي بأي شيء. راجع <a href="#decouple-مرشحات-extract-class-مصنفة-حسب-المخاطر">Decouple: مرشحات Extract-Class مصنفة حسب المخاطر</a> أدناه.
</p>

<div align="center">
<details><summary><b>اقرأ هذا بلغات أخرى</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>الوصول المبكر إلى منصة graphify متاح الآن قبل إطلاق الإصدار v1 العام: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

اكتب `/graphify` في مساعد البرمجة بالذكاء الاصطناعي الخاص بك، فيقوم بتحويل مشروعك بالكامل (الكود، المستندات، ملفات PDF، الصور، الفيديوهات) إلى **رسم بياني معرفي (knowledge graph)** يمكنك **الاستعلام عنه بدلاً من البحث بـ grep** في الملفات.

- **رسم خرائط الكود مجاناً، ومحلياً بالكامل.** يتم تحليل الكود عبر AST من tree-sitter: حتمي، بدون LLM، ولا شيء يخرج من جهازك. (المستندات وملفات PDF والصور والفيديو تستخدم نموذج مساعدك، أو مفتاح API مُهيأ، لتمريرة دلالية.)
- **كل حافة (edge) لها تفسير.** كل صلة تُصنَّف بأنها `EXTRACTED` (موجودة صريحاً في المصدر) أو `INFERRED` (استنتجها graphify)، لذا تستطيع معرفة ما قُرئ مباشرة من ما استُنتج.
- **ليس فهرساً متجهياً (vector index).** بلا تضمينات (embeddings) وبلا مخزن متجهي: رسم بياني حقيقي تتنقل خلاله. اطرح سؤالاً، أو تتبّع المسار بين شيئين، أو فسّر مفهوماً واحداً.

> تريد شيئاً يعمل دائماً، ويتحدث في الخلفية عبر الكود والمستندات والاجتماعات، بدلاً من عند الطلب فقط؟ هذا بالضبط ما نبنيه في **[graphify.com](https://graphify.com)**، والوصول المبكر متاح الآن على **[app.graphify.com](https://app.graphify.com/login)**.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="واجهة graph.html التفاعلية من graphify تعرض قاعدة كود FastAPI كرسم بياني معرفي موجّه بالقوى، مع مفتاح للمجتمعات المكتشفة" width="900">
</p>
<p align="center">
  <em>قاعدة كود FastAPI بعد رسمها بواسطة graphify. كل عقدة هي مفهوم، والألوان هي مجتمعات مكتشفة، والكل قابل للنقر داخل graph.html.</em>
</p>

**البدء** (30 ثانية):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

بعد ذلك، داخل مساعدك بالذكاء الاصطناعي:

```
/graphify .
```

هذا كل ما تحتاجه. ستحصل على **ثلاثة ملفات**:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**يعمل مع** Claude Code وCursor وCodex وGemini CLI وGitHub Copilot وأكثر من 15 أداة أخرى — [اختر منصتك](#التثبيت).

---

## شاهده عملياً

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="استعلام مسار في graphify: طرفية تطلب أقصر مسار بين FastAPI وModelField، والإجابة تتوهج قفزة بقفزة عبر الرسم البياني المعرفي" width="900">
</p>

بعد بناء الرسم البياني، تستعلم عنه بدلاً من قراءة الملفات. مخرجات حقيقية من تشغيل graphify على قاعدة كود FastAPI الموضحة أعلاه:

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

كل حافة (edge) تحمل **علامة ثقة** (`EXTRACTED` = صريحة في المصدر، `INFERRED` = مستمدة عبر الاستنتاج)، لذا تستطيع معرفة ما قُرئ مباشرة من ما استُنتج. `graphify query "<question>"` يُرجع رسماً بيانياً فرعياً محدود النطاق لسؤال بلغة عادية، و`graphify path A B` يتتبّع كيف يرتبط أي شيئين ببعضهما.

---

## Decouple: مرشحات Extract-Class مصنفة حسب المخاطر

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: عقدة God Node بعنوان MainWindow تنقسم إلى فئات مرشحة مصنفة حسب المخاطر، مع تحذير من مشاركة الحالة (state) بين اثنتين منها" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: خمس فئات مقترحة لـ MainWindow، ولوحة معلومات العقدة مفتوحة على Main Window Axis and Range Controls تُظهر تداخل حالة (state overlap) بقيمة 0.608 مع Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>DECOUPLE.html في تشغيل حقيقي (AutoCheck/Touchstone Explorer) — النقر على فئة مقترحة يُظهر بالتحديد أي فئة أخرى تشاركها الحالة، وما هو المُشترك بالضبط.</em>
</p>

`graphify decouple` يعثر على كائنات God Object ويخبرك إن كان تقسيمها يستحق العناء فعلاً — لا فقط أنها كبيرة.

نمط الفشل الذي صُمم هذا لرصده: فئة بها 47 دالة يقسمها التجميع القائم على رسم بياني الاستدعاءات بسعادة إلى 5 مجموعات تبدو منظمة، وكلها لا تزال تحت السطح تقرأ وتكتب في نفس حالة النسخة (instance state) الخاصة بـ `self._chart_style` / `self._crosshair`. إذا شحنت هذا التقسيم فأنت لم تفصل شيئاً حقاً — لقد نقلت الدوال إلى ملفات جديدة لا يزال يتعذر اختبارها أو تغييرها أو فهمها بشكل مستقل، لأنها جميعاً لا تزال تحتاج إلى تمرير نفس الحالة المشتركة مرة أخرى. أداة تنظر فقط إلى رسم بياني الاستدعاءات لا يمكنها رؤية هذا على الإطلاق؛ يجب أن تعود إلى الشيفرة المصدرية الفعلية.

**فحصان، كلاهما بدون LLM (0-LLM) وكلاهما حتمي:**

1. **هل هذه أصلاً God Object؟** عقدة ذات درجة (degree) عالية قد تكون God Object حقيقية (كثير من دوالها الخاصة، موزعة على مسؤوليات غير مرتبطة — عندها ينطبق Extract Class) أو مركزاً (hub) أو نموذج بيانات مُشار إليه بكثرة (دوال خاصة قليلة، وأغلب المراجع *واردة*) — تقسيم جسمها لا يفعل شيئاً؛ الحل هو تضييق واجهته، لا استخراج فئة. تُميّز `classify_god_node` بين الحالتين عبر `member_ratio`، لا الدرجة الخام — وهو الفرق الذي يمنع `TraceSource` (84 حافة، لكن فقط 6 من دوالها الخاصة) من الحصول على اقتراح تقسيم زائف، بينما يحصل `MainWindow` (88 حافة، و47 من دوالها الخاصة) على الاقتراح بشكل صحيح.
2. **هل سيقلل التقسيم الترابط (coupling) فعلاً؟** تُقارَن `risk_before` (حجم God Node الحالي وترابطه وتشتته) بـ `risk_after` — المخاطر الجديدة التي سيُدخلها التقسيم نفسه: استدعاءات بين المجموعات كانت حوافاً غير مرئية داخل الفئة وتصبح تبعيات صريحة بين الفئات، ومستدعون سيحتاجون الآن للاعتماد على أكثر من فئة جديدة، و — وهو الفحص الذي لا يمكن لرسم بياني الاستدعاءات إجراءه بنيوياً — مقدار ما تتشاركه المجموعات المقترحة فعلاً من حالة نسخة (instance state) عبر `self`/`this` (قراءات وكتابات واستدعاءات دوال مساعدة مشتركة، تُقيَّم كل منها بوزن مستقل: **كتابة** مشتركة تُحسب بدرجة أعلى من قراءة مشتركة). هذا يُعيد تحليل ملف مصدر God Node نفسه مباشرة باستخدام tree-sitter؛ ولا يعتمد على الرسم البياني المُستخرج من graphify نفسه، الذي لا يسجّل أبداً الوصول على مستوى الحقول (field-level) لأي لغة. فقط عندما تنخفض `risk_after` عن `risk_before` بمقدار يتجاوز عتبة معينة، توصي الخطة بـ `split` — وإلا فهي `marginal` أو `keep_as_is`، والمرشح غير المُشجَّع عليه يُبلَّغ عنه كرقم، لا كشكل عليك التشكيك فيه بالعين.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

يُخرج ثلاثة ملفات إلى جانب `graph.json`:

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

**تغطية اللغات لفحص مشاركة الحالة** (التصنيف القائم فقط على رسم بياني الاستدعاءات أعلاه يعمل مع كل لغة يستخرجها graphify؛ هذا الجدول خاص بإعادة تحليل المصدر التي تتحقق من تداخل حالة `self`/`this`):

| اللغة | مدعومة | ملاحظات |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` عقدة AST مستقلة بذاتها، لا مجرد استدعاء ملفوف لحقل — تُعامَل بشكل صريح |
| C# | ✅ | |
| Rust | ✅ | `self.x` عبر كتل `impl` |
| Ruby | ✅ | `@x` (الصيغة السائدة) + استدعاءات `self.foo` |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | تحليل المُستقبِل (receiver) لكل دالة — لا توجد في Go كلمة مفتاحية `self`/`this`، فيُحلَّل اسم المُستقبِل (`f` في `func (f *Foo) M()`) من جديد لكل دالة |
| C | ❌ | معامل من نوع مؤشر-بنية (struct-pointer) لا يحمل أي علامة نحوية تميّزه عن أي معامل آخر — لا توجد إشارة موثوقة بدون استدلال كامل للأنواع |

عقدة God Node بلغة غير مدعومة، أو لا يمكن قراءة مصدرها، تُوسم بـ `state_analysis: "skipped"` — التصنيف وتقييم رسم بياني الاستدعاءات يستمران بالتشغيل، لكن التوصية تعتمد على رسم بياني الاستدعاءات وحده بدلاً من افتراض ضمني بأن فحص الحالة قد نجح.

---

## ما الذي يقدمه

ما تحصل عليه جاهزاً:

| القدرة (Capability) | ما تحصل عليه |
|---|---|
| **God nodes** | المفاهيم الأكثر ارتباطاً، لترى ما يتدفق عبره كل شيء |
| **المجتمعات (Communities)** | الرسم البياني مُقسَّم إلى أنظمة فرعية (Leiden)، بتسميات دون LLM |
| **الروابط بين الملفات** | `calls` / `imports` / `inherits` / `mixes_in` مُحلَّلة عبر نحو 40 لغة باستخدام AST من tree-sitter |
| **الاستعلام والمسار والتفسير** | اطرح سؤالاً، أو تتبّع المسار بين شيئين، أو فسّر مفهوماً واحداً، كل ذلك مقابل `graph.json` |
| **الأسباب المنطقية ومراجع التوثيق** | تعليقات `# NOTE:` / `# WHY:` واستشهادات ADR/RFC تصبح عقداً من الدرجة الأولى مرتبطة بالكود |
| **ما وراء الكود** | المستندات وملفات PDF والصور والفيديو/الصوت، كل ذلك يُرسَم في نفس الرسم البياني |
| **أولوية للمحلي (Local-first)** | الكود يُحلَّل محلياً باستخدام tree-sitter (بدون LLM، ولا شيء يخرج من جهازك)؛ فقط التمريرة الدلالية على المستندات/الوسائط تستدعي واجهة خلفية (backend)، وذلك فقط إذا هيّأت واحدة |

---

## المقاييس المرجعية

| المقياس المرجعي | المؤشر | graphify | المجال |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | دقة الإجابة على الأسئلة (QA accuracy) | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | دقة الإجابة على الأسئلة (QA accuracy) | **76%** | متعادل مع dense RAG |
| بناء الرسم البياني | أرصدة LLM | **0** | لكل رمز (token) في أغلب الأنظمة الأخرى |

كل نظام عمل على نفس بنية الاختبار (harness) بنفس النموذج ونفس الموازنة، وقُيِّم بواسطة حكم (judge) تم التحقق من صحته بشكل معزول (blind-validated) مقابل حكم ثانٍ (نسبة اتفاق 90.6%، معامل كابا لكوهين 0.81). الجداول الكاملة لكل نظام، ونتيجة ذكاء الكود، وأوامر إعادة إنتاج التجربة: **[BENCHMARKS.md](../../BENCHMARKS.md)**.

---

## المتطلبات الأساسية

| المتطلب | الحد الأدنى | التحقق | التثبيت |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(مُوصى به)* | أي إصدار | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(بديل)* | أي إصدار | `pipx --version` | `pip install pipx` |

**تثبيت سريع على macOS (Homebrew):**
```bash
brew install python@3.12 uv
```

**تثبيت سريع على Windows:**
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

## التثبيت

> **الحزمة الرسمية:** حزمة PyPI هي `graphifyy` (بحرفي y). الحزم الأخرى التي تبدأ بـ `graphify*` على PyPI غير تابعة لهذا المشروع. أمر CLI يبقى `graphify`.

**الخطوة 1 — تثبيت الحزمة:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**الخطوة 2 — تسجيل المهارة (skill) مع مساعدك بالذكاء الاصطناعي:**

```bash
graphify install
```

هذا كل ما تحتاجه. افتح مساعدك بالذكاء الاصطناعي واكتب `/graphify .`

لتثبيت مهارة المساعد داخل المستودع الحالي بدلاً من ملف تعريفك (profile)، أضف `--project`:

```bash
graphify install --project
graphify install --project --platform codex
```

عمليات التثبيت المحددة النطاق للمشروع تكتب داخل الدليل الحالي، مثل
`.claude/skills/graphify/SKILL.md` أو `.agents/skills/graphify/SKILL.md` (مع ملف مرافق
`references/` تُحمّله المهارة عند الحاجة)، وتطبع
تلميحاً بأمر `git add` للملفات القابلة للـ commit.
الأوامر الخاصة بكل منصة والتي تدعم التثبيت المحدد النطاق للمشروع تقبل نفس الخيار،
مثل `graphify claude install --project` أو `graphify codex install --project`.

> **ملاحظة PowerShell:** استخدم `graphify .` وليس `/graphify .` — الشرطة المائلة في البداية هي فاصل مسار (path separator) في PowerShell.

> **يظهر لك `graphify: command not found`؟** يضع `uv tool install` / `pipx install` أمر `graphify` في دليل bin الخاص بأداتهما (`~/.local/bin`). إن كانت الصدفة (shell) لا تجد الأمر بعد التثبيت مباشرة — وهو أمر شائع على تثبيت macOS + zsh جديد — فإن هذا الدليل ليس بعد على `PATH`: نفّذ `uv tool update-shell` (أو `pipx ensurepath`)، ثم افتح طرفية جديدة. مع `pip` العادي، أضف `~/.local/bin` (Linux) أو `~/Library/Python/3.x/bin` (Mac) إلى `PATH`، أو نفّذ `python -m graphify`.

> **تُشغّل باستخدام `uvx` / `uv tool run` بدلاً من التثبيت؟** اذكر اسم الحزمة، لا الأمر: `uvx --from graphifyy graphify install`. الأمر العادي `uvx graphify …` يفشل (`No solution found … no versions of graphify`) لأن `uv tool run` يقرأ الكلمة الأولى كاسم *حزمة*، والحزمة هي `graphifyy` — أمر `graphify` موجود داخلها.

> **تجنّب `pip install` على Mac/Windows** إن أمكن. تحلّ المهارة مسار Python وقت التشغيل من `graphify-out/.graphify_python`؛ فإن أشار إلى بيئة مختلفة عن التي ثبّت `pip` الحزمة فيها، ستحصل على `ModuleNotFoundError: No module named 'graphify'`. يعزل `uv tool install` و`pipx install` الحزمة في بيئتهما الخاصة ويتجنبان هذا تماماً.

> **خطاطات (hooks) git وuv tool / pipx:** يضمّن `graphify hook install` مسار المُفسِّر (interpreter) الحالي مباشرة داخل نصوص الخطاطات وقت التثبيت، لذا يعمل خطاط post-commit بشكل صحيح حتى في عملاء git ذوي الواجهة الرسومية وفي أدوات CI حيث لا يكون `~/.local/bin` على PATH. إن أعدت تثبيت graphify أو رقّيته، أعد تشغيل `graphify hook install` لتحديث المسار المُضمَّن.

> **النمط الصارم (Claude Code):** `graphify install --project --strict` يجعل المساعد يستخدم الرسم البياني فعلاً. التثبيت الافتراضي *يحثّ* المساعد على تشغيل `graphify query` قبل قراءة الملفات؛ أما النمط الصارم فهو *يحجب* أول قراءة خام للمصدر في الجلسة ويوجّهها إلى الرسم البياني، ثم يعود إلى الحثّ العادي (فيُفعَّل مرة واحدة على الأكثر في كل جلسة ولا يتعطل أبداً). بدّل وقت التشغيل عبر `GRAPHIFY_HOOK_STRICT=1`/`0`؛ التثبيت الافتراضي (الحثّ اللطيف) يبقى دون تغيير.

<details>
<summary><b>اختر منصتك</b> (أكثر من 20 مساعداً، انقر للتوسيع)</summary>

| المنصة | أمر التثبيت |
|----------|----------------|
| Claude Code (Linux/Mac) | `graphify install` |
| Claude Code (Windows) | `graphify install` (يُكتشف تلقائياً) أو `graphify install --platform windows` |
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
| Agent Skills (عبر الأطر المختلفة) | `graphify install --platform agents` (اسم بديل `--platform skills`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify install --platform pi` |
| Cursor | `graphify cursor install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

يحتاج مستخدمو Codex أيضاً إلى `multi_agent = true` تحت `[features]` في `~/.codex/config.toml` للاستخراج المتوازي. يستخدم CodeBuddy نفس أداة Agent وآلية خطاط PreToolUse المستخدمة في Claude Code. يستخدم Factory Droid أداة `Task` لتوزيع العوامل الفرعية بالتوازي. يستخدم OpenClaw وAider استخراجاً متتابعاً (دعم العوامل المتوازية لا يزال في مراحله الأولى على هاتين المنصتين). يستخدم Trae أداة Agent لتوزيع العوامل الفرعية بالتوازي و **لا** يدعم خطاطات `PreToolUse`، لذا فإن AGENTS.md هي الآلية الدائمة العمل.

`--platform agents` (اسم بديل `--platform skills`) يستهدف مواقع [Agent-Skills](https://github.com/anthropics/skills) العامة عبر الأطر المختلفة: الموقع العام للمستخدم بحسب المواصفة `~/.agents/skills/` (تقرأه `npx skills` والأطر المتوافقة مع المواصفة) للتثبيت العام، و`./.agents/skills/` للتثبيت الخاص بمشروع (`--project`). أمر `graphify install` العادي يبقى، بحسب التصميم، خاصاً بمنصة واحدة (Claude Code) — استخدم منصة `agents` المسمّاة عندما تريد أن تكون المهارة قابلة للاكتشاف من أي إطار يقرأ `.agents/skills`.

> يستخدم Codex `$graphify` بدلاً من `/graphify`.

</details>

<details>
<summary><b>إضافات اختيارية</b> (ثبّت فقط ما تحتاجه)</summary>

| الإضافة | ما تضيفه | التثبيت |
|---|---|---|
| `pdf` | استخراج PDF | `uv tool install "graphifyy[pdf]"` |
| `office` | دعم `.docx` و`.xlsx` | `uv tool install "graphifyy[office]"` |
| `google` | عرض Google Sheets | `uv tool install "graphifyy[google]"` |
| `video` | تفريغ صوتي للفيديو/الصوت (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | خادم MCP بواسطة stdio | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | دعم الدفع (push) إلى Neo4j | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | دعم الدفع (push) إلى FalkorDB | `uv tool install "graphifyy[falkordb]"` |
| `svg` | تصدير الرسم البياني بصيغة SVG | `uv tool install "graphifyy[svg]"` |
| `leiden` | اكتشاف المجتمعات بخوارزمية Leiden (فقط لإصدارات Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | استدلال محلي عبر Ollama | `uv tool install "graphifyy[ollama]"` |
| `openai` | واجهات OpenAI أو المتوافقة معها | `uv tool install "graphifyy[openai]"` |
| `gemini` | واجهة Google Gemini | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | واجهة Anthropic Claude (`--backend claude`، تستخدم `ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (يستخدم IAM، بدون مفتاح API) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`، تستخدم `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "graphifyy[openai]"` |
| `sql` | استخراج مخطط SQL | `uv tool install "graphifyy[sql]"` |
| `postgres` | استبطان PostgreSQL مباشرة (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | استخراج AST لملفات BYOND DreamMaker `.dm`/`.dme` (قد تحتاج مترجم C + `python3-dev` إن لم توجد عجلة (wheel) مطابقة لمنصتك) | `uv tool install "graphifyy[dm]"` |
| `terraform` | استخراج AST لملفات Terraform / HCL `.tf`/`.tfvars`/`.hcl` | `uv tool install "graphifyy[terraform]"` |
| `pascal` | استخراج AST لملفات Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` (حواف `calls`/`inherits` أكثر دقة؛ يرجع إلى مستخرج قائم على التعابير النمطية عند غيابها) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | تجزيء استعلامات باللغة الصينية (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | كل ما سبق | `uv tool install "graphifyy[all]"` |

</details>

---

## جعل مساعدك يستخدم الرسم البياني دائماً

نفّذ هذا مرة واحدة في مشروعك بعد بناء رسم بياني:

| المنصة | الأمر |
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
| Agent Skills (عبر الأطر المختلفة) | `graphify agents install` (اسم بديل `graphify skills install`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify pi install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

هذا يكتب ملف تهيئة صغيراً يخبر مساعدك بمراجعة الرسم البياني المعرفي لأسئلة قاعدة الكود، مُفضِّلاً استعلامات محددة النطاق مثل `graphify query "<question>"` على قراءة التقرير الكامل أو البحث بـ grep في الملفات الخام.

- **منصات الخطاطات (hooks)** (Claude Code، Gemini CLI): يُفعَّل خطاط تلقائياً قبل استدعاءات الأدوات الشبيهة بالبحث (وعلى Claude Code، قبل قراءة ملفات المصدر واحداً تلو الآخر عبر أدوات Read/Glob) ويحثّ مساعدك على مسار الرسم البياني.
- **منصات ملفات التعليمات** (Codex، OpenCode، Cursor، إلخ): ملفات تعليمات دائمة (`AGENTS.md`، `.cursor/rules/`، إلخ) تقدّم نفس التوجيه القائم على الاستعلام أولاً.

يبقى `GRAPH_REPORT.md` متاحاً لمراجعة معمارية واسعة.

**CodeBuddy** يفعل الشيء نفسه الذي يفعله Claude Code: يكتب قسماً في `CODEBUDDY.md` يطلب من CodeBuddy قراءة `graphify-out/GRAPH_REPORT.md` قبل الإجابة عن أسئلة معمارية، ويُثبِّت خطاطات `PreToolUse` (`.codebuddy/settings.json`) تُفعَّل قبل أوامر بحث Bash وقراءات الملفات، حاثّةً على استخدام `graphify query` بدلاً من ذلك.

**Codex** يكتب إلى `AGENTS.md`، وهو ما يحمل فعلياً توجيه الرسم البياني الدائم على هذه المنصة. يُسجِّل `graphify codex install` أيضاً خطاط `PreToolUse` في `.codex/hooks.json` (`graphify hook-check`)، لكن هذا الإدخال مُتعمَّد أن يكون **بلا فعل (no-op)**: يرفض Codex Desktop قيمة `hookSpecificOutput.additionalContext` على `PreToolUse`، فإصدار حثّ هناك سيُعطِّل استدعاءات أداة Bash. بخلاف Claude Code، حيث يقوم الخطاط (`graphify hook-guard`) بالحثّ فعلاً، على Codex يُفعَّل الخطاط ولا يفعل شيئاً عمداً، و`AGENTS.md` هي الآلية الدائمة العمل.

**Kilo Code** يُثبِّت مهارة Graphify في `~/.config/kilo/skills/graphify/SKILL.md` وأمراً أصلياً `/graphify` في `~/.config/kilo/command/graphify.md`. يكتب `graphify kilo install` أيضاً `AGENTS.md` بالإضافة إلى مُلحق (plugin) أصلي من نوع `tool.execute.before` (`.kilo/plugins/graphify.js` + تسجيل في `.kilo/kilo.json` أو `.kilo/kilo.jsonc`) لذا يحصل Kilo على نفس سلوك تذكير الرسم البياني الدائم عبر تهيئة `.kilo` الأصلية.

**Cursor** يكتب `.cursor/rules/graphify.mdc` بخيار `alwaysApply: true`، لذا يُدرِجه Cursor في كل محادثة تلقائياً، دون الحاجة إلى خطاط.

لإزالة graphify من كل المنصات دفعة واحدة: `graphify uninstall` (أضف `--purge` لحذف `graphify-out/` أيضاً). أو استخدم الأمر الخاص بكل منصة (مثل `graphify claude uninstall`).

---

## محتوى التقرير

- **God nodes** — المفاهيم الأكثر ارتباطاً في مشروعك. كل شيء يتدفق عبرها.
- **الروابط المفاجئة** — صلات بين أشياء تعيش في ملفات أو وحدات مختلفة. مُرتَّبة بحسب مدى كونها غير متوقعة.
- **"السبب" (the why)** — التعليقات المضمّنة (`# NOTE:`، `# WHY:`، `# HACK:`) وdocstrings ومنطق التصميم من المستندات تُستخرج كعقد مستقلة مرتبطة بالكود التي تفسّره.
- **أسئلة مقترحة** — من 4 إلى 5 أسئلة يُعد الرسم البياني في موضع فريد للإجابة عنها.
- **علامات الثقة** — كل علاقة مُستنتَجة تُوسَم بـ `EXTRACTED` أو `INFERRED` أو `AMBIGUOUS`. تعرف دائماً ما وُجد فعلاً وما جرى تخمينه.

---

## الملفات التي يدعمها

| النوع | الامتدادات |
|------|-----------|
| الكود (36 قواعد نحوية لـ tree-sitter) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (يتطلب `.dm`/`.dme` تنفيذ `uv tool install graphifyy[dm]`؛ يعيد `.mts`/`.cts` استخدام قواعد TypeScript، ويعيد `.cc`/`.cxx` وCUDA `.cu`/`.cuh` وMetal `.metal` استخدام قواعد C++) |
| Salesforce Apex | `.cls .trigger` (قائم على التعابير النمطية؛ الفئات والواجهات والتعدادات والدوال والمُشغِّلات وحواف SOQL/DML) |
| Terraform / HCL | `.tf .tfvars .hcl` (يتطلب تنفيذ `uv tool install graphifyy[terraform]`) |
| تهيئات MCP | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — يستخرج عقد الخوادم، ومراجع الحزم، ومتطلبات متغيرات البيئة |
| بيانات الحزم (manifests) | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — عقدة حزمة معيارية واحدة لكل حزمة (بحسب الاسم) بالإضافة إلى حواف `depends_on`، لذا فإن الحزمة المُشار إليها من عدة بيانات تكون مركزاً (hub) واحداً |
| المستندات | `.md .mdx .qmd .html .txt .rst .yaml .yml` (روابط markdown من نوع `[text](./other.md)` والـ `[[wikilinks]]` تصبح حواف `references` بين المستندات) |
| Office | `.docx .xlsx` (يتطلب تنفيذ `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (اختياري؛ يتطلب مصادقة `gws` وخيار `--google-workspace`؛ يحتاج Sheets إلى `uv tool install graphifyy[google]`) |
| ملفات PDF | `.pdf` |
| الصور | `.png .jpg .webp .gif` |
| الفيديو / الصوت | `.mp4 .mov .mp3 .wav` وأكثر (يتطلب تنفيذ `uv tool install graphifyy[video]`) |
| YouTube / الروابط | أي رابط فيديو (يتطلب تنفيذ `uv tool install graphifyy[video]`) |

يُستخرَج الكود **محلياً بدون أي استدعاءات API** (AST عبر tree-sitter). كل ما عداه يمر عبر واجهة برمجة نموذج مساعدك بالذكاء الاصطناعي.

ملفات `.gdoc` و`.gsheet` و`.gslides` في تطبيق Google Drive لسطح المكتب هي مؤشرات اختصار (shortcuts)، لا محتوى المستند نفسه. لتضمين مستندات وجداول بيانات وعروض تقديمية أصلية من Google Docs وSheets وSlides في استخراج بلا واجهة (headless)، ثبّت
[أداة `gws` CLI](https://github.com/googleworkspace/cli) وصادق عبرها، ثم نفّذ:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

يمكنك أيضاً تعيين `GRAPHIFY_GOOGLE_WORKSPACE=1`. يُصدِّر Graphify الاختصارات إلى
`graphify-out/converted/` كملفات Markdown مرافقة، ثم يستخرج تلك الملفات.

---

## الأوامر الشائعة

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

راجع [Decouple: مرشحات Extract-Class مصنفة حسب المخاطر](#decouple-مرشحات-extract-class-مصنفة-حسب-المخاطر) أعلاه، أو [مرجع الأوامر الكامل](#مرجع-الأوامر-الكامل) أدناه.

---

## تجاهل الملفات

أنشئ ملف `.graphifyignore` في جذر مشروعك — بنفس صيغة `.gitignore`، بما فيها نفي `!`.

**يُحتَرم `.gitignore` تلقائياً.** يقرأ graphify ملف `.gitignore` في كل دليل. إن وُجد `.graphifyignore` أيضاً، فإن الاثنين **يُدمجان** — تُقيَّم أنماط `.graphifyignore` أخيراً، فتفوز عند التعارض (بما فيها نفي `!`). إضافة `.graphifyignore` لا تزيد إلا في الاستبعاد؛ فهي لا تُعيد إدراج ملف استبعده `.gitignore` أصلاً أبداً. نطاق الأدلة الفرعية يعمل بنفس طريقة git — ملف التجاهل يؤثر فقط على شجرته الفرعية الخاصة.

مرّر `--no-gitignore` إلى `graphify extract` عندما يكون الكود المُولَّد أو المُحوَّل (transpiled) المُتجاهَل من git ينتمي إلى الرسم البياني. هذا يُعطِّل `.gitignore` و`.git/info/exclude`؛ ويبقى `.graphifyignore` مُطبَّقاً.

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

## إعداد الفريق

يُقصد بـ `graphify-out/` أن يُودَع في git ليبدأ كل من في الفريق بخريطة.

**إضافات مُوصى بها إلى `.gitignore`:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` صار الآن قابلاً للنقل (portable) — تُخزَّن المفاتيح كمسارات نسبية وتُعاد تثبيتها عند التحميل، لذا فإن حفظه في commit أمر آمن ويتجنّب إعادة بناء كاملة عند أول سحب (checkout).

**سير العمل:**
1. يُنفِّذ شخص واحد `/graphify .` ويحفظ `graphify-out/` في commit.
2. يسحب الجميع — يقرأ مساعدهم الرسم البياني فوراً.
3. نفِّذ `graphify hook install` لإعادة البناء تلقائياً بعد كل commit (AST فقط، بلا تكلفة API). هذا يُهيِّئ أيضاً مُشغِّل دمج (merge driver) لـ git بحيث لا يُترك `graph.json` أبداً بعلامات تعارض — فحين يُنفِّذ مطوران commit بالتوازي، تُدمَج رسومهما البيانية تلقائياً بطريقة اتحادية (union-merge).
4. عندما تتغير المستندات أو الأوراق البحثية، نفِّذ `/graphify --update` لتحديث تلك العقد.

---

## استخدام الرسم البياني مباشرة

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

يمنح خادم MCP مساعدك وصولاً منظَّماً: `query_graph`، `get_node`، `get_neighbors`، `shortest_path`، `list_prs`، `get_pr_impact`، `triage_prs`.

### خادم HTTP مشترك

`--transport stdio` (الافتراضي) يُشغِّل خادماً محلياً واحداً لكل مطوِّر. `--transport http` يُقدِّم نفس الأدوات عبر نقل MCP Streamable HTTP، لذا تستطيع عملية مشتركة واحدة تقديم الرسم البياني للفريق بأكمله — يوجِّه العملاء تهيئة MCP في بيئة التطوير الخاصة بهم إلى `http://<host>:8080/mcp` بدلاً من تشغيل graphify محلياً.

| الخيار (Flag) | الافتراضي | الغرض |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | بروتوكول النقل الذي يُقدَّم عبره |
| `--host` | `127.0.0.1` | مضيف ربط HTTP (استخدم `0.0.0.0` للكشف خارج localhost) |
| `--port` | `8080` | منفذ ربط HTTP |
| `--api-key` | متغير البيئة `GRAPHIFY_API_KEY` | يتطلب `Authorization: Bearer <key>` (أو `X-API-Key`) |
| `--path` | `/mcp` | مسار تركيب HTTP |
| `--json-response` | معطّل | إرجاع JSON عادي بدلاً من تدفقات SSE |
| `--stateless` | معطّل | بلا حالة لكل جلسة (لعمليات التوزيع بموازنة الحمل / CI) |
| `--session-timeout` | `3600` | إنهاء الجلسات ذات الحالة الخاملة بعد N ثانية (`0` يُعطِّل ذلك) |

ربط `127.0.0.1` الافتراضي مخصص لـ loopback فقط. عيّن `--host 0.0.0.0` **و** `--api-key` معاً عند الكشف على مضيف مشترك. شغِّله في حاوية (container):

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **ملاحظة WSL / Linux:** يُضمِّن Ubuntu أمر `python3`، لا `python`. استخدم بيئة افتراضية (venv) لتجنب التعارضات:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## متغيرات البيئة

هذه مطلوبة فقط لـ **الاستخراج بلا واجهة / في CI** (`graphify extract`). عند التشغيل عبر مهارة `/graphify` داخل بيئة التطوير الخاصة بك، تُوفِّر جلسة IDE واجهة برمجة النموذج — دون الحاجة إلى مفاتيح إضافية.

| المتغير | يُستخدم لـ | متى يكون مطلوباً |
|---|---|---|
| `ANTHROPIC_API_KEY` | واجهة Claude (Anthropic) | `--backend claude` |
| `ANTHROPIC_BASE_URL` | رابط نقطة نهاية متوافقة مع Anthropic (وكيل LiteLLM، بوابات، ...) | `--backend claude` (الافتراضي: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | اسم النموذج لواجهة Claude — للنقاط النهائية المخصصة، استخدم اسم/لقب النموذج الذي يعرضه خادمك | `--backend claude` (الافتراضي: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` أو `GOOGLE_API_KEY` | واجهة Google Gemini | `--backend gemini` |
| `OPENAI_API_KEY` | واجهات OpenAI أو المتوافقة معها | `--backend openai` (الخوادم المحلية تقبل أي قيمة غير فارغة) |
| `OPENAI_BASE_URL` | رابط خادم متوافق مع OpenAI (llama.cpp، vLLM، LM Studio، ...) | `--backend openai` (الافتراضي: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | اسم النموذج لواجهة OpenAI — للخوادم ذاتية الاستضافة، استخدم اسم/لقب النموذج الذي يعرضه خادمك (راجع نقطة النهاية `/v1/models`)، مثل `LFM2.5-8B-A1B-UD-Q4_K_XL` لـ llama.cpp | `--backend openai` (الافتراضي: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | واجهة DeepSeek | `--backend deepseek` |
| `MOONSHOT_API_KEY` | واجهة Kimi Code | `--backend kimi` |
| `OLLAMA_BASE_URL` | رابط الاستدلال المحلي لـ Ollama | `--backend ollama` (الافتراضي: `http://localhost:11434`) |
| `OLLAMA_MODEL` | اسم نموذج Ollama | `--backend ollama` (الافتراضي: كشف تلقائي) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | تجاوز حجم نافذة ذاكرة التخزين المؤقت KV لـ Ollama | اختياري — يُحدَّد حجمه تلقائياً بشكل افتراضي |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | عدد الدقائق للاحتفاظ بنموذج Ollama محمَّلاً | اختياري — عيّن `0` لإلغاء التحميل بعد كل قطعة (chunk) |
| `AZURE_OPENAI_API_KEY` | واجهة Azure OpenAI Service | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | رابط نقطة نهاية مورد Azure | `--backend azure` (مطلوب إلى جانب مفتاح API) |
| `AZURE_OPENAI_API_VERSION` | تجاوز إصدار Azure API | اختياري — الافتراضي `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` أو `GRAPHIFY_AZURE_MODEL` | اسم نشر Azure | اختياري — الافتراضي `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — سلسلة بيانات الاعتماد المعيارية | `--backend bedrock` (بلا مفتاح API، يستخدم IAM) |
| `GRAPHIFY_MAX_WORKERS` | عدد خيوط التوازي لـ AST | اختياري — أيضاً خيار `--max-workers` |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | رفع سقف المخرجات للمجموعات الكثيفة | اختياري — مثلاً `32768` للملفات الكبيرة |
| `GRAPHIFY_API_TIMEOUT` | مهلة كل استدعاء بالثواني لواجهات HTTP وclaude-cli وAnthropic SDK وBedrock (الافتراضي: 600) | اختياري — أيضاً خيار `--api-timeout` |
| `GRAPHIFY_MAX_RETRIES` | عدد مرات إعادة محاولة طلب مُقيَّد المعدل (429) قبل الاستسلام (الافتراضي: 6؛ يحترم `Retry-After`) | اختياري — ارفعه لحدود صارمة لكل منظمة (مثل kimi)؛ `0` يُعطِّل ذلك |
| `GRAPHIFY_FORCE` | فرض إعادة بناء الرسم البياني حتى مع عقد أقل | اختياري — أيضاً خيار `--force` |
| `GRAPHIFY_GOOGLE_WORKSPACE` | تفعيل تصدير Google Workspace تلقائياً | اختياري — عيّنه إلى `1` |
| `GRAPHIFY_TRIAGE_BACKEND` | الواجهة الخلفية لـ `graphify prs --triage` | اختياري — يُكتشف تلقائياً من المفاتيح المتوفرة |
| `GRAPHIFY_TRIAGE_MODEL` | تجاوز النموذج للفرز (triage) | اختياري — مثلاً `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | عيّنه إلى `1` لتفعيل سجل الاستعلامات المحلي في `~/.cache/graphify-queries.log` (يسجل كل سؤال query/path/explain + مسار المجموعة). معطّل افتراضياً — لا يُكتب شيء إلا إذا اختًرت ذلك (#1797) | اختياري |
| `GRAPHIFY_QUERY_LOG` | تفعيل سجل الاستعلامات وكتابته في هذا المسار بدلاً من الافتراضي | اختياري — معطّل إلا إذا عُيِّن هذا أو `_ENABLE` |
| `GRAPHIFY_QUERY_LOG_DISABLE` | عيّنه إلى `1` لفرض تعطيل سجل الاستعلامات (يفوز على متغيرات التفعيل) | اختياري |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | عند تفعيل السجل، يسجل أيضاً استجابات الرسم البياني الفرعي كاملة (معطّل افتراضياً) | اختياري |
| `GRAPHIFY_MAX_GRAPH_BYTES` | تجاوز سقف حجم `graph.json` البالغ 512 MiB — مثلاً `700MB`، `2GB`، أو بايتات مباشرة | اختياري — مفيد للمجموعات الكبيرة جداً |
| `GRAPHIFY_MAX_CONTEXTS` | العدد الأقصى للرسوم البيانية غير الافتراضية للمشاريع التي يحتفظ بها خادم MCP واحد متعدد المشاريع | اختياري — الافتراضي: `8`؛ القيم غير الصالحة تستخدم `8`، والقيم الأقل من `1` تستخدم `1` |
| `GRAPHIFY_LLM_TEMPERATURE` | تجاوز درجة حرارة (temperature) LLM للاستخراج الدلالي — مثلاً `0.7`، أو `none` لحذفها | اختياري — تُحذَف تلقائياً لنماذج الاستدلال o1/o3/o4/gpt-5 |

---

## الخصوصية

- **ملفات الكود** — تُعالَج محلياً عبر tree-sitter. لا شيء يخرج من جهازك. مجموعة كود فقط لا تحتاج إلى مفتاح API — يعمل `graphify extract` بلا اتصال تماماً. في مستودع مختلط، أضف `--code-only` لفهرسة الكود فقط وتخطي المستندات/ملفات PDF/الصور التي تحتاج إلى LLM.
- **الفيديو / الصوت** — يُفرَّغ صوتياً محلياً باستخدام faster-whisper. لا شيء يخرج من جهازك.
- **المستندات وملفات PDF والصور** — تُرسَل إلى مساعدك بالذكاء الاصطناعي لاستخراج دلالي (عبر مهارة `/graphify`، باستخدام أي نموذج تُشغِّله جلسة IDE الخاصة بك). يتطلب `graphify extract` بلا واجهة أحد المفاتيح: `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini)، `MOONSHOT_API_KEY` (Kimi)، `ANTHROPIC_API_KEY` (Claude)، `OPENAI_API_KEY` (OpenAI)، `DEEPSEEK_API_KEY` (DeepSeek)، مثيل Ollama قيد التشغيل (`OLLAMA_BASE_URL`)، بيانات اعتماد AWS عبر سلسلة المزوّد المعيارية (Bedrock - بلا مفتاح API، يستخدم IAM)، أو ملف تنفيذي `claude` CLI (Claude Code - بلا مفتاح API، يستخدم اشتراك Claude الخاص بك). يستخدم خيار `--dedup-llm` نفس المفتاح.
- **إقامة البيانات (data residency)** — يكتشف `graphify extract` تلقائياً أي مزوّد يُستخدم بحسب أي مفتاح API مُعيَّن (الأولوية: Gemini ← Kimi ← Claude ← OpenAI ← DeepSeek ← Azure ← Bedrock ← Ollama). للكود ذي متطلبات إقامة بيانات، استخدم `--backend ollama` (محلي بالكامل) أو مرّر خيار `--backend` صريحاً. Kimi (`MOONSHOT_API_KEY`) يوجَّه إلى خوادم Moonshot AI في الصين.
- **بلا تِلِمتري (telemetry)**، بلا تتبع للاستخدام، بلا تحليلات.
- **تسجيل الاستعلامات** — كل استدعاء لـ `graphify query` و`graphify path` و`graphify explain` وMCP `query_graph` يُسجَّل في `~/.cache/graphify-queries.log` بصيغة JSON Lines (الطابع الزمني، السؤال، المجموعة، عدد العقد المُرجَعة، المدة). استجابات الرسم البياني الفرعي الكاملة **لا** تُخزَّن افتراضياً. عيّن `GRAPHIFY_QUERY_LOG_DISABLE=1` لإلغاء التسجيل، أو `GRAPHIFY_QUERY_LOG=/dev/null` لإسكاته دون تعطيل مسار الكود.

---

## استكشاف الأخطاء وإصلاحها

**`graphify: command not found` بعد التثبيت**
تم تثبيت CLI لكن دليل bin الخاص به ليس على `PATH` صدفتك (shell). اختر الحل بحسب طريقة تثبيتك:
- **uv** (`uv tool install graphifyy`): يُوضَع الأمر في دليل bin الخاص بأداة uv (`~/.local/bin`)، وهو ما لا يكون غالباً على `PATH` في تثبيت macOS/zsh جديد. نفّذ `uv tool update-shell`، ثم افتح طرفية جديدة. (اعثر على الدليل باستخدام `uv tool dir --bin`.)
- **pipx** (`pipx install graphifyy`): نفّذ `pipx ensurepath`، ثم افتح طرفية جديدة.
- **pip** (`pip install graphifyy`): يُثبِّت pip النصوص في دليل bin للمستخدم قد لا يكون على `PATH` — أضف `~/Library/Python/3.x/bin` (macOS) أو `~/.local/bin` (Linux) إلى `PATH` في `~/.zshrc`/`~/.bashrc`، أو فقط نفّذ `python -m graphify`.

**`uvx graphify …` أو `uv tool run graphify …` يفشل في حل `graphify`**
حزمة PyPI هي `graphifyy`؛ `graphify` هو فقط الأمر الذي تُقدِّمه. تُعامل `uv tool run` الكلمة الأولى كـ *اسم حزمة*، فتبحث عن حزمة باسم `graphify` وتُظهر `No solution found … no versions of graphify`. اذكر اسم الحزمة صريحاً: `uvx --from graphifyy graphify install` (نفس `uv tool run --from graphifyy graphify install`). أو نفّذ `uv tool install graphifyy` مرة واحدة ثم استدعِ `graphify` مباشرة.

**`uv run --with graphifyy python -m graphify` يُشغِّل بصمت تثبيتاً أقدم**
يستخدم `uv run` بايثون *النظام*، فإن كانت نسخة أقدم من `graphifyy` موجودة فيه أيضاً (مثلاً من `pip install graphifyy` سابق)، يجد بايثون تلك النسخة أولاً في `sys.path` ولا يستطيع `--with graphifyy` تجاوزها. يُنفَّذ دون خطأ، لكنك تحصل على سلوك النسخة *القديمة* — مثلاً تُتجاهل بصمت تجاوزات المتغيرات مثل `OPENAI_BASE_URL`، فتصل الطلبات إلى نقطة النهاية الافتراضية وتفشل بخطأ 401 يبدو كمفتاح خاطئ. العلامة المميزة لذلك هي سطر `warning: skill is from graphify <newer>, package is <older>` — وهذا يعني أن تثبيتاً مختلفاً هو ما جرى تحميله، لا فقط مهارة قديمة. تحقّق من أي نسخة جرى تحميلها فعلاً:
```bash
python -c "import graphify; print(graphify.__file__)"
```
ثم نفّذ الأمر المُثبَّت مباشرة (يستخدم النسخة المُدارة عبر uv)، أو تخلَّص من نسخة النظام القديمة:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` يعمل لكن أمر `graphify` لا يعمل**
لا يتضمن `PATH` الخاص بصدفتك دليل bin الذي ثُبِّت الأمر فيه. فضِّل `uv tool install` / `pipx install` على `pip` العادي، ثم نفّذ `uv tool update-shell` / `pipx ensurepath` وافتح طرفية جديدة (راجع ملاحظات التثبيت أعلاه).

**`/graphify .` يتسبب في "path not recognized" في PowerShell**
تُعامل PowerShell الشرطة المائلة `/` في البداية كفاصل مسار. استخدم `graphify .` (بلا شرطة) على Windows.

**عدد عقد الرسم البياني أقل بعد `--update` أو إعادة البناء**
إن حذفت عملية إعادة هيكلة (refactor) ملفات، تبقى العقد القديمة عالقة. مرّر `--force` (أو عيّن `GRAPHIFY_FORCE=1`) للاستبدال حتى إن كانت إعادة البناء تحتوي عقداً أقل.

**تخرج `extract` برسالة "extraction was incomplete ... refusing to overwrite"**
عندما تتعطل مرحلة استخراج أو يتعذر على عملية مسح (walk) قراءة المجموعة كاملة، يكون التشغيل أصغر من تشغيل كامل، فيرفض `graphify extract` استبدال رسم بياني موجود أكبر بنتيجة جزئية (حماية لـ `graph.json`). أصلِح الخلل الأساسي وأعد التشغيل، أو مرّر `--allow-partial` للاستبدال بأي حال.

**عقد مكررة لنفس الكيان في الرسم البياني (تكرارات شبحية)**
التكرارات الشبحية (نفس الرمز يظهر مرتين — مرة من استخراج AST بموقع مصدري، ومرة من استخراج دلالي دون موقع) تُدمَج تلقائياً الآن وقت البناء. إن رأيت هذا في رسم بياني بُني قبل v0.8.33، نفِّذ إعادة استخراج كاملة للتنظيف:
```bash
graphify extract . --force
```

**Ollama يستهلك كل ذاكرة VRAM / يتجاوز نافذة السياق**
تُحدَّد نافذة ذاكرة التخزين المؤقت KV تلقائياً لكنها قد تكون كبيرة جداً على وحدة معالجة الرسوميات (GPU) الخاصة بك. صغِّرها:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**تحذيرات `LLM returned invalid JSON` / `Unterminated string`**
بلغت استجابة JSON من النموذج سقف رموز المخرجات وانقُطعت وسط سلسلة نصية. يتعافى graphify تلقائياً (يُقسِّم القطعة (chunk) ويُعيد استخراج النصفين، ويُقسَّم أي مستند واحد أكبر من المعتاد أولاً عند حدود العناوين/الفقرات لضمان تغطية الملف كاملاً)، فهذه التحذيرات مُشوِّشة لكنها لا تعني فقدان بيانات. للتخفيف من هذا التذبذب، ارفع سقف المخرجات أو صغِّر مخرجات كل قطعة:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
مع بوابة سحابية مثل OpenRouter، فضِّل `--backend openai` (عيّن `OPENAI_BASE_URL`) على وسيط (shim) Ollama — فهو مسار أنظف متوافق مع OpenAI. إن كان للنموذج سقف مخرجات أقصى خاص به، فتقليل `--token-budget` هو الأداة الأكثر موثوقية.

**HTML الرسم البياني كبير جداً على أن يُفتح في متصفح (أكثر من 5000 عقدة)**
تخطَّ توليد HTML واستخدم JSON مباشرة:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**علامات تعارض في `graph.json` بعد أن يُنفِّذ مطوران commit في وقت واحد**
نفِّذ `graphify hook install` — يُهيِّئ مُشغِّل دمج (merge driver) لـ git يدمج `graph.json` تلقائياً بطريقة اتحادية (union-merge) حتى لا تحدث التعارضات مطلقاً.

**يُعيد الاستخراج عقداً/حوافاً فارغة للمستندات أو ملفات PDF**
تحتاج المستندات وملفات PDF والصور إلى استدعاء LLM — مجموعات الكود فقط لا تحتاج إلى مفتاح. تحقّق من تعيين مفتاح API وصحة الواجهة الخلفية:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**تحذير عدم تطابق إصدار المهارة في بيئة التطوير الخاصة بك**
إصدار graphify المُثبَّت مختلف عن ملف المهارة. حدِّثه:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**تُبطَل ذاكرة التخزين المؤقت لمطالبات Claude Code بعد كل `graphify extract`**
يكتب Graphify ملفات مخرجات (`graph.json`، `graphify-out/`) داخل مساحة العمل. إن لم تكن هذه المسارات مُتجاهَلة، فإن كل كتابة تُبطِل ذاكرة التخزين المؤقت لمطالبات Claude Code، مما يفرض إعادة تحميل كاملة بمعدلات كتابة الذاكرة المؤقتة في الدورة التالية. أضفها إلى `.claudeignore`:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## مرجع الأوامر الكامل

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

> **أسماء المجتمعات:** داخل عامل (agent) (Claude Code، Gemini CLI) يُسمّي العامل نفسه المجتمعات. عندما تُشغِّل CLI الخام مباشرة، تُسمّيها `cluster-only` تلقائياً باستخدام الواجهة الخلفية المُهيَّأة (مُدمَجة أو مزوّد مخصص متوافق مع OpenAI) — مرّر `--no-label` للاحتفاظ بـ `Community N`، أو نفّذ `graphify label` لتوليد الأسماء (من جديد) عند الحاجة.

---

## لمزيد من المعلومات

- [كيف يعمل](../how-it-works.md) — خط أنابيب الاستخراج، اكتشاف المجتمعات، تقييم الثقة، المقاييس المرجعية
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — تفصيل الوحدات، كيفية إضافة لغة
- [عمليات التكامل الاختيارية](../docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — الكتاب الذي يشرح الأفكار التي يقوم عليها graphify، والمعمارية من طرف إلى طرف

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) هي الطبقة الدائمة العمل المبنية فوق graphify — تُطبِّق نفس نهج الرسم البياني على سياق عملك بأكمله: الاجتماعات والملفات والمستندات والكود، وتُحدِّثه باستمرار في الخلفية.

مصمَّمة للأفراد والفرق الذين تمتد أعمالهم عبر مئات المحادثات والمستندات التي لا يمكنهم إعادة تجميعها كاملة أبداً.

**[انضم إلى قائمة الانتظار في graphify.com](https://graphify.com).** التجربة المجانية تنطلق قريباً.

---

<details>
<summary>المساهمة</summary>

### إعداد بيئة التطوير

يستخدم المشروع [uv](https://docs.astral.sh/uv/) لسير عمل التطوير. ثبِّته مرة واحدة، ثم:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

تحقّق من تثبيت وضع editable:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### تشغيل الاختبارات

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> ملاحظة macOS: تتضمن حزمة الاختبارات كلاً من ملفَي `sample.f90` و`sample.F90`. يتعارض هذان الملفان على أنظمة ملفات HFS+ / APFS التي لا تُفرِّق بين حالة الأحرف. شغِّل على Linux أو داخل حاوية Docker إن احتجت اختبار كلا نسختي Fortran في وقت واحد.

### سير عمل Git

- التطوير النشط يجري على فرع `v8`.
- أسلوب الـ commit: `fix: <description>` / `feat: <description>` / `docs: <description>`
- قبل فتح طلب سحب (PR)، نفِّذ `uv run pytest tests/ -q` وتأكّد من نجاحه.
- أضف ملف تجهيزات (fixture) إلى `tests/fixtures/` واختبارات إلى `tests/test_languages.py` لأي مُستخرِج لغة جديد.

### ما الذي يمكنك المساهمة به

**الأمثلة المُنفَّذة (worked examples)** هي أكثر المساهمات فائدة. شغِّل `/graphify` على مجموعة حقيقية، احفظ المخرجات في `worked/{slug}/`، اكتب `review.md` صادقاً يغطي ما أصاب فيه الرسم البياني وما أخطأ، وافتح طلب سحب (PR).

**أخطاء الاستخراج** — افتح Issue مع ملف الإدخال، وإدخال ذاكرة التخزين المؤقت (`graphify-out/cache/`)، وما الذي كان مفقوداً أو خاطئاً.

راجع [ARCHITECTURE.md](../../ARCHITECTURE.md) لمسؤوليات الوحدات وكيفية إضافة لغة.

</details>
