<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>פיצול (fork) של <a href="https://github.com/Graphify-Labs/graphify">graphify</a> שמוסיף את <code>graphify decouple</code></b> — מועמדים ל-Extract Class עבור god objects, מדורגים לפי סיכון וללא שום LLM (0-LLM), שנבדקים מחדש מול קוד המקור עצמו (ולא רק מול ה-call graph) לפני שהכלי ממליץ על משהו. ראו <a href="#decouple-מועמדי-extract-class-מדורגי-סיכון">Decouple: מועמדי Extract-Class מדורגי סיכון</a> למטה.
</p>

<div align="center">
<details><summary><b>קראו זאת בשפות אחרות</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>הגישה המוקדמת לפלטפורמת graphify פתוחה עוד לפני השקת v1 הציבורית: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

הקלידו `/graphify` בעוזר הקוד מבוסס ה-AI שלכם, והוא ימפה את כל הפרויקט שלכם (קוד, מסמכים, קובצי PDF, תמונות, סרטונים) לתוך **גרף ידע (knowledge graph)** שאפשר **לתשאל במקום לרוץ עם grep** על הקבצים.

- **מיפוי קוד בחינם, ומקומי לחלוטין.** הקוד מנותח באמצעות tree-sitter AST: דטרמיניסטי, ללא LLM, ושום דבר לא יוצא מהמחשב שלכם. (מסמכים, קובצי PDF, תמונות וסרטונים משתמשים במודל של העוזר שלכם, או במפתח API מוגדר, עבור מעבר סמנטי.)
- **לכל קשת (edge) יש הסבר.** כל חיבור מתויג `EXTRACTED` (מפורש במקור) או `INFERRED` (נפתר על ידי graphify), כך שתדעו מה נקרא ישירות ומה הוסק.
- **זה לא אינדקס וקטורי.** בלי embeddings, בלי vector store: גרף אמיתי שאתם מטיילים בו. שאלו שאלה, עקבו אחר המסלול בין שני דברים, או בקשו הסבר על מושג אחד.

> רוצים שזה יפעל תמיד, ויתעדכן ברקע על פני הקוד, המסמכים והפגישות שלכם ולא רק לפי דרישה? זה בדיוק מה שאנחנו בונים ב-**[graphify.com](https://graphify.com)**, והגישה המוקדמת פתוחה כעת ב-**[app.graphify.com](https://app.graphify.com/login)**.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="graph.html האינטראקטיבי של graphify מציג את בסיס הקוד של FastAPI כגרף ידע מכוון-כוחות עם מקרא של הקהילות שזוהו" width="900">
</p>
<p align="center">
  <em>בסיס הקוד של FastAPI ממופה על ידי graphify. כל צומת הוא מושג, הצבעים הם קהילות שזוהו, והכול ניתן ללחיצה בתוך graph.html.</em>
</p>

**להתחיל** (30 שניות):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

לאחר מכן, בעוזר ה-AI שלכם:

```
/graphify .
```

זה הכול. אתם מקבלים **שלושה קבצים**:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**עובד עם** Claude Code, ‏Cursor, ‏Codex, ‏Gemini CLI, ‏GitHub Copilot ועוד 15+ — [בחרו את הפלטפורמה שלכם](#התקנה).

---

## לראות את זה בפעולה

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="שאילתת path של graphify: טרמינל מבקש את המסלול הקצר ביותר בין FastAPI ל-ModelField, והתשובה נדלקת קפיצה אחר קפיצה על פני גרף הידע" width="900">
</p>

לאחר שהגרף נבנה, אתם מתשאלים אותו במקום לקרוא קבצים. פלט אמיתי, graphify שהורץ על בסיס הקוד של FastAPI שמוצג למעלה:

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

כל קשת נושאת **תג ודאות** (`EXTRACTED` = מפורש במקור, `INFERRED` = נגזר בתהליך הפתירה), כך שתדעו מה נקרא ישירות ומה הוסק. הפקודה `graphify query "<question>"` מחזירה תת-גרף ממוקד עבור שאלה בשפה חופשית, ו-`graphify path A B` עוקבת אחר האופן שבו שני דברים כלשהם מתחברים.

---

## Decouple: מועמדי Extract-Class מדורגי סיכון

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: צומת ה-god בשם MainWindow מתפצל למחלקות מועמדות מדורגות סיכון, עם אזהרה על מצב (state) משותף בין שתיים מהן" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: חמש המחלקות המוצעות של MainWindow, חלונית Node Info פתוחה על Main Window Axis and Range Controls ומציגה חפיפת state של 0.608 עם Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>DECOUPLE.html בהרצה אמיתית — לחיצה על מחלקה מוצעת מראה בדיוק עם איזו מחלקה אחרת היא חולקת state, ומה בדיוק משותף.</em>
</p>

אותו עמוד גם מרנדר את הפיצול עצמו. הפעלת **Preview decoupled view** מחליפה את המתודות של מחלקת ה-god במחלקות המוצעות ומנתבת מחדש את הקשתות במקום — שינוי החיווט עצמו, ולא דיאגרמה שצוירה מחדש:

| לפני — מחלקת ה-god היום | אחרי — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html לפני ההחלפה: צומת מרכז MainWindow יחיד עם המתודות שלו פרושות סביבו" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html אחרי ההחלפה: אותו צומת מצטמצם ל-5 מחלקות מוצעות בצורת מעוין, קשתות ירוקות מקווקוות מראות אילו מתודות חולצו לכל אחת, וקשתות אדומות מראות מצב מופע משותף בין שתיים מהן" width="440"> |
| צומת אחד שמחזיק 47 מתודות משלו, וכל אחת מהן נגישה רק דרך המחלקה. | המחלקות המוצעות. ירוק מקווקו = מה חולץ לכל אחת; אדום = מצב המופע ששתיים מהן עדיין חולקות, וזה בדיוק מה שמכריע בין `split` לבין `keep_as_is`. מצוירים רק מועמדים שעוברים את סף הסיכון — כאן 5 מתוך 6, ולכן למתודה אחת אין מעוין לנחות עליו. |

הפקודה `graphify decouple` מאתרת god objects ואומרת לכם אם באמת שווה לפצל אותם — לא רק שהם גדולים.

מצב הכשל שהכלי נועד לתפוס: מחלקה עם 47 מתודות שאשכול מבוסס call graph מפצל בשמחה ל-5 קבוצות שנראות מסודרות, אבל כולן עדיין קוראות וכותבות בדיוק לאותו מצב מופע `self._chart_style` / `self._crosshair` מתחת לפני השטח. אם תשלחו פיצול כזה לייצור לא ניתקתם דבר — רק העברתם מתודות לקבצים חדשים שעדיין אי אפשר לבדוק, לשנות או להבין בנפרד, כי כולן עדיין זקוקות לאותו state משותף שיוזרם אליהן בחזרה. כלי שמסתכל רק על ה-call graph פשוט לא יכול לראות את זה; הוא חייב לחזור לקוד המקור עצמו.

**שתי בדיקות, שתיהן ללא LLM, שתיהן דטרמיניסטיות:**

1. **האם זה בכלל God Object?** צומת בעל דרגה גבוהה יכול להיות God Object אמיתי (הרבה מתודות משלו, פרושות על אחריות שאינה קשורה זו לזו — Extract Class רלוונטי כאן) או hub / מודל נתונים שמופנים אליו יותר מדי (מעט מתודות משלו, רוב ההפניות *נכנסות* — פיצול הגוף שלו לא עוזר; הפתרון הוא לצמצם את הממשק, לא לחלץ מחלקה). הפונקציה `classify_god_node` מבחינה בין השניים לפי `member_ratio`, ולא לפי הדרגה הגולמית — וזה ההבדל שמונע מ-`TraceSource` (84 קשתות, אך רק 6 מתודות משלו) לקבל הצעת פיצול שגויה, בעוד ש-`MainWindow` (88 קשתות, 47 מתודות משלו) מקבל אותה בצדק.
2. **האם הפיצול באמת יפחית צימוד?** הערך `risk_before` (הגודל/הצימוד/הפיצול הנוכחיים של צומת ה-god) מושווה ל-`risk_after` — הסיכון החדש שהפיצול עצמו יכניס: קריאות בין קבוצות שהיו קשתות פנימיות בלתי נראות בתוך המחלקה והופכות לתלויות מפורשות בין מחלקות, קוראים שיצטרכו כעת להיות תלויים ביותר ממחלקה חדשה אחת, ו — הבדיקה שגרף קריאות פשוט לא יכול לבצע מבנית — כמה מצב מופע של `self`/`this` (קריאות, כתיבות וקריאות משותפות למתודות עזר, כל אחת במשקל נפרד: **כתיבה** משותפת נספרת גבוה יותר מקריאה משותפת) הקבוצות המוצעות באמת חולקות ביניהן. לשם כך מנותח מחדש קובץ המקור של צומת ה-god ישירות עם tree-sitter; הכלי אינו מסתמך על הגרף שחולץ על ידי graphify עצמו, שאינו מתעד גישה ברמת השדה (field-level) בשום שפה. רק כאשר `risk_after` יורד מתחת ל-`risk_before` במרווח העובר סף מסוים, התוכנית ממליצה על `split` — אחרת ההמלצה היא `marginal` או `keep_as_is`, ומועמד שאינו מומלץ מדווח כמספר בלבד ולעולם לא מצויר כצורה שתצטרכו לפקפק בה בעין.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

מייצר שלושה קבצים לצד `graph.json`:

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

**כיסוי שפות עבור בדיקת שיתוף ה-state** (הסיווג מבוסס ה-call graph שלמעלה עובד לכל שפה ש-graphify מחלץ; הטבלה הזו נוגעת ספציפית לניתוח המקור מחדש שמאמת חפיפת `self`/`this`):

| שפה | נתמכת | הערות |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | ‏`this.foo()` הוא צומת AST עצמאי, ולא גישה לשדה עטופה — מטופל במפורש |
| C# | ✅ | |
| Rust | ✅ | ‏`self.x` דרך בלוקי `impl` |
| Ruby | ✅ | ‏`@x` (הניב הדומיננטי) + קריאות `self.foo` |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | פתירת receiver לכל מתודה — ל-Go אין מילת מפתח `self`/`this`, ולכן שם ה-receiver (‏`f` ב-`func (f *Foo) M()`) נפתר מחדש עבור כל מתודה |
| C | ❌ | לפרמטר מסוג מצביע ל-struct אין סימן תחבירי שמבדיל אותו מכל פרמטר אחר — אין אות אמין ללא הסקת טיפוסים מלאה |

צומת god בשפה שאינה נתמכת, או כזה שלא ניתן לקרוא את המקור שלו, מסומן `state_analysis: "skipped"` — הסיווג וציון ה-call graph עדיין רצים, אבל ההמלצה נשענת על ה-call graph בלבד במקום להניח בשקט שבדיקת ה-state עברה.

---

## מה זה עושה

מה מקבלים מהקופסה:

| יכולת | מה מקבלים |
|---|---|
| **God nodes** | המושגים המחוברים ביותר, כדי שתראו דרך מה הכול עובר |
| **קהילות** | הגרף מפוצל לתת-מערכות (Leiden), עם תוויות ללא LLM |
| **קישורים בין קבצים** | ‏`calls` / `imports` / `inherits` / `mixes_in` נפתרים על פני ~40 שפות באמצעות tree-sitter AST |
| **Query, path, explain** | שאלו שאלה, עקבו אחר המסלול בין שני דברים, או בקשו הסבר על מושג — הכול מול `graph.json` |
| **נימוקים + הפניות למסמכים** | הערות `# NOTE:` / `# WHY:` וציטוטי ADR/RFC הופכים לצמתים מן המניין המקושרים לקוד |
| **מעבר לקוד** | מסמכים, קובצי PDF, תמונות ווידאו/אודיו — כולם ממופים לאותו גרף |
| **Local-first** | הקוד מנותח מקומית עם tree-sitter (ללא LLM, שום דבר לא יוצא מהמחשב); רק המעבר הסמנטי על מסמכים/מדיה פונה ל-backend, ורק אם הגדרתם אחד |

---

## Benchmarks

| Benchmark | מדד | graphify | השדה |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | QA accuracy | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | QA accuracy | **76%** | שווה ל-dense RAG |
| בניית הגרף | קרדיטים של LLM | **0** | לפי טוקן ברוב המערכות |

כל מערכת רצה על אותו harness, עם אותו מודל ואותם תקציבים, ונוקדה על ידי judge שאומת בעיוורון מול judge שני (‏90.6% הסכמה, קאפא של כהן 0.81). טבלאות מלאות לכל מערכת, תוצאת ה-code intelligence ופקודות לשחזור: **[BENCHMARKS.md](../../BENCHMARKS.md)**.

---

## דרישות מוקדמות

| דרישה | מינימום | בדיקה | התקנה |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(מומלץ)* | כל גרסה | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(חלופה)* | כל גרסה | `pipx --version` | `pip install pipx` |

**התקנה מהירה ב-macOS (Homebrew):**
```bash
brew install python@3.12 uv
```

**התקנה מהירה ב-Windows:**
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

## התקנה

> **החבילה הרשמית:** חבילת ה-PyPI היא `graphifyy` (עם שני y). חבילות `graphify*` אחרות ב-PyPI אינן קשורות. פקודת ה-CLI עדיין `graphify`.

**שלב 1 — התקינו את החבילה:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**שלב 2 — רשמו את ה-skill אצל עוזר ה-AI שלכם:**

```bash
graphify install
```

זה הכול. פתחו את עוזר ה-AI והקלידו `/graphify .`

כדי להתקין את ה-skill במאגר הנוכחי במקום בפרופיל המשתמש שלכם,
הוסיפו `--project`:

```bash
graphify install --project
graphify install --project --platform codex
```

התקנות ברמת הפרויקט כותבות אל תוך התיקייה הנוכחית, למשל
`.claude/skills/graphify/SKILL.md` או `.agents/skills/graphify/SKILL.md` (יחד עם
תיקיית `references/` נלווית שה-skill טוען לפי הצורך), ומדפיסות
רמז `git add` עבור הקבצים שניתן לבצע להם commit.
פקודות ייעודיות לפלטפורמה שתומכות בהתקנה ברמת פרויקט מקבלות את אותו flag,
למשל `graphify claude install --project` או `graphify codex install --project`.

> **הערה ל-PowerShell:** השתמשו ב-`graphify .` ולא ב-`/graphify .` — הלוכסן הפותח הוא מפריד נתיבים ב-PowerShell.

> **‏`graphify: command not found`?** הפקודות `uv tool install` / `pipx install` שמות את הפקודה `graphify` בתיקיית ה-bin של הכלי שלהן (`~/.local/bin`). אם ה-shell לא מוצא אותה מיד אחרי ההתקנה — נפוץ בהתקנה טרייה של macOS + zsh — התיקייה עדיין לא נמצאת ב-`PATH` שלכם: הריצו `uv tool update-shell` (או `pipx ensurepath`), ואז פתחו טרמינל חדש. עם `pip` רגיל, הוסיפו את `~/.local/bin` (Linux) או `~/Library/Python/3.x/bin` (Mac) ל-PATH, או הריצו `python -m graphify`.

> **מריצים עם `uvx` / `uv tool run` במקום להתקין?** ציינו את שם החבילה, לא את הפקודה: `uvx --from graphifyy graphify install`. הפקודה `uvx graphify …` נכשלת (`No solution found … no versions of graphify`) כי `uv tool run` קורא את המילה הראשונה כשם *חבילה*, והחבילה היא `graphifyy` — הפקודה `graphify` נמצאת בתוכה.

> **הימנעו מ-`pip install` ב-Mac/Windows** אם אפשר. ה-skill פותר את Python בזמן ריצה מתוך `graphify-out/.graphify_python`; אם זה מצביע על סביבה אחרת מזו שבה `pip` התקין את החבילה, תקבלו `ModuleNotFoundError: No module named 'graphify'`. הפקודות `uv tool install` ו-`pipx install` מבודדות את החבילה בסביבה משלהן ומונעות את זה לגמרי.

> **git hooks ו-uv tool / pipx:** הפקודה `graphify hook install` מטמיעה את נתיב המפרש הנוכחי ישירות בתסריטי ה-hook בזמן ההתקנה, כך שה-hook של post-commit מופעל כראוי גם בלקוחות git גרפיים ובמריצי CI שבהם `~/.local/bin` אינו ב-PATH. אם התקנתם מחדש או שדרגתם את graphify, הריצו שוב `graphify hook install` כדי לרענן את הנתיב המוטמע.

> **מצב strict (Claude Code):** הפקודה `graphify install --project --strict` גורמת לעוזר באמת להשתמש בגרף. ההתקנה הרגילה רק *דוחפת* אותו להריץ `graphify query` לפני קריאת קבצים; מצב strict *חוסם* את הקריאה הגולמית הראשונה של קוד מקור בכל סשן ומפנה אותה לגרף, ואז חוזר לדחיפה הרכה (כך שהוא פועל לכל היותר פעם אחת בסשן ולעולם לא נתקע). ניתן להחליף בזמן ריצה עם `GRAPHIFY_HOOK_STRICT=1`/`0`; ההתקנה הרגילה נשארת ללא שינוי (דחיפה רכה).

<details>
<summary><b>בחרו את הפלטפורמה שלכם</b> (20+ עוזרים, לחצו להרחבה)</summary>

| פלטפורמה | פקודת התקנה |
|----------|----------------|
| Claude Code (Linux/Mac) | `graphify install` |
| Claude Code (Windows) | `graphify install` (מזוהה אוטומטית) או `graphify install --platform windows` |
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
| Agent Skills (חוצה-פריימוורקים) | `graphify install --platform agents` (כינוי `--platform skills`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify install --platform pi` |
| Cursor | `graphify cursor install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

משתמשי Codex זקוקים גם ל-`multi_agent = true` תחת `[features]` בקובץ `~/.codex/config.toml` עבור חילוץ מקבילי. ‏CodeBuddy משתמש באותו מנגנון Agent tool ו-PreToolUse hook כמו Claude Code. ‏Factory Droid משתמש בכלי `Task` לשיגור תת-סוכנים במקביל. ‏OpenClaw ו-Aider משתמשים בחילוץ סדרתי (התמיכה בסוכנים מקביליים עדיין בחיתוליה בפלטפורמות האלה). ‏Trae משתמש ב-Agent tool לשיגור תת-סוכנים במקביל ו**אינו** תומך ב-hooks מסוג `PreToolUse`, ולכן AGENTS.md הוא המנגנון הפעיל-תמיד.

הדגל `--platform agents` (כינוי `--platform skills`) מכוון למיקומי [Agent-Skills](https://github.com/anthropics/skills) הגנריים חוצי-הפריימוורקים: ‏`~/.agents/skills/` הגלובלי למשתמש לפי המפרט (נקרא על ידי `npx skills` ועל ידי פריימוורקים תואמי-מפרט) עבור התקנה גלובלית, ו-`./.agents/skills/` עבור התקנה ברמת פרויקט (`--project`). הפקודה `graphify install` החשופה נשארת חד-פלטפורמית (Claude Code) בכוונה — השתמשו בפלטפורמה `agents` כשאתם רוצים שה-skill יימצא על ידי כל פריימוורק שקורא `.agents/skills`.

> ‏Codex משתמש ב-`$graphify` במקום ב-`/graphify`.

</details>

<details>
<summary><b>תוספות אופציונליות</b> (התקינו רק את מה שצריך)</summary>

| תוספת | מה היא מוסיפה | התקנה |
|---|---|---|
| `pdf` | חילוץ PDF | `uv tool install "graphifyy[pdf]"` |
| `office` | תמיכה ב-`.docx` וב-`.xlsx` | `uv tool install "graphifyy[office]"` |
| `google` | רינדור של Google Sheets | `uv tool install "graphifyy[google]"` |
| `video` | תמלול וידאו/אודיו (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | שרת MCP stdio | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | תמיכת push ל-Neo4j | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | תמיכת push ל-FalkorDB | `uv tool install "graphifyy[falkordb]"` |
| `svg` | ייצוא גרף ל-SVG | `uv tool install "graphifyy[svg]"` |
| `leiden` | זיהוי קהילות Leiden (רק Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | הרצה מקומית עם Ollama | `uv tool install "graphifyy[ollama]"` |
| `openai` | ממשקי OpenAI / תואמי OpenAI | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic Claude API (‏`--backend claude`, משתמש ב-`ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (משתמש ב-IAM, ללא מפתח API) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (‏`--backend azure`, משתמש ב-`AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "graphifyy[openai]"` |
| `sql` | חילוץ סכמת SQL | `uv tool install "graphifyy[sql]"` |
| `postgres` | אינטרוספקציה חיה של PostgreSQL (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | חילוץ AST של BYOND DreamMaker ‏`.dm`/`.dme` (ייתכן שיידרש קומפיילר C + `python3-dev` אם אין wheel שמתאים לפלטפורמה שלכם) | `uv tool install "graphifyy[dm]"` |
| `terraform` | חילוץ AST של Terraform / HCL ‏`.tf`/`.tfvars`/`.hcl` | `uv tool install "graphifyy[terraform]"` |
| `pascal` | חילוץ AST של Pascal / Delphi ‏`.pas`/`.dpr`/`.dpk`/`.inc` (קשתות `calls`/`inherits` מדויקות יותר; בהיעדרו נופל חזרה למחלץ מבוסס regex) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | פילוח שאילתות בסינית (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | כל מה שלמעלה | `uv tool install "graphifyy[all]"` |

</details>

---

## לגרום לעוזר שלכם להשתמש בגרף תמיד

הריצו את זה פעם אחת בפרויקט שלכם אחרי בניית גרף:

| פלטפורמה | פקודה |
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
| Agent Skills (חוצה-פריימוורקים) | `graphify agents install` (כינוי `graphify skills install`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify pi install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

הפעולה כותבת קובץ הגדרות קטן שאומר לעוזר שלכם להיוועץ בגרף הידע עבור שאלות על בסיס הקוד, ולהעדיף שאילתות ממוקדות כמו `graphify query "<question>"` על פני קריאת הדוח המלא או grep על קבצים גולמיים.

- **פלטפורמות עם hooks** (Claude Code, Gemini CLI): ‏hook נורה אוטומטית לפני קריאות כלי מסוג חיפוש (וב-Claude Code, גם לפני קריאת קובצי מקור אחד-אחד דרך כלי ה-Read/Glob) ודוחף את העוזר לכיוון מסלול הגרף.
- **פלטפורמות עם קובצי הנחיות** (Codex, ‏OpenCode, ‏Cursor וכו'): קובצי הנחיות קבועים (`AGENTS.md`, ‏`.cursor/rules/` וכו') מספקים את אותה הנחיה של query-first.

הקובץ `GRAPH_REPORT.md` עדיין זמין לסקירה ארכיטקטונית רחבה.

**CodeBuddy** עושה את אותם שני דברים כמו Claude Code: כותב מקטע ב-`CODEBUDDY.md` שאומר ל-CodeBuddy לקרוא את `graphify-out/GRAPH_REPORT.md` לפני מענה על שאלות ארכיטקטורה, ומתקין hooks מסוג `PreToolUse` (‏`.codebuddy/settings.json`) שנורים לפני פקודות חיפוש ב-Bash ולפני קריאות קבצים, ודוחפים אל `graphify query` במקום.

**Codex** כותב אל `AGENTS.md`, וזה מה שבפועל נושא את ההנחיה הפעילה-תמיד לגרף בפלטפורמה הזו. הפקודה `graphify codex install` גם רושמת hook מסוג `PreToolUse` בקובץ `.codex/hooks.json` (`graphify hook-check`), אבל הרשומה הזו היא **no-op** בכוונה: ‏Codex Desktop דוחה `hookSpecificOutput.additionalContext` ב-`PreToolUse`, ולכן פליטת דחיפה שם הייתה שוברת קריאות לכלי Bash. בניגוד ל-Claude Code, שבו ה-hook (`graphify hook-guard`) מבצע את הדחיפה, ב-Codex ה-hook נורה ובמכוון לא עושה דבר, ו-`AGENTS.md` הוא המנגנון הפעיל-תמיד.

**Kilo Code** מתקין את ה-skill של Graphify אל `~/.config/kilo/skills/graphify/SKILL.md` ופקודת `/graphify` מקומית אל `~/.config/kilo/command/graphify.md`. הפקודה `graphify kilo install` גם כותבת `AGENTS.md` בתוספת תוסף `tool.execute.before` מקורי (`.kilo/plugins/graphify.js` + רישום ב-`.kilo/kilo.json` או `.kilo/kilo.jsonc`), כך ש-Kilo מקבל את אותה התנהגות תזכורת פעילה-תמיד לגרף דרך הגדרות `.kilo` המקוריות.

**Cursor** כותב `.cursor/rules/graphify.mdc` עם `alwaysApply: true`, כך ש-Cursor מכליל אותו אוטומטית בכל שיחה, ללא צורך ב-hook.

כדי להסיר את graphify מכל הפלטפורמות בבת אחת: `graphify uninstall` (הוסיפו `--purge` כדי למחוק גם את `graphify-out/`). לחלופין השתמשו בפקודה הייעודית לפלטפורמה (למשל `graphify claude uninstall`).

---

## מה יש בדוח

- **God nodes** — המושגים המחוברים ביותר בפרויקט שלכם. הכול עובר דרכם.
- **חיבורים מפתיעים** — קישורים בין דברים שנמצאים בקבצים או במודולים שונים. מדורגים לפי מידת ההפתעה.
- **ה"למה"** — הערות בשורה (`# NOTE:`, `# WHY:`, `# HACK:`), docstrings ונימוקי עיצוב ממסמכים מחולצים כצמתים נפרדים המקושרים לקוד שהם מסבירים.
- **שאלות מוצעות** — 4–5 שאלות שהגרף במיוחד מסוגל לענות עליהן.
- **תגי ודאות** — כל קשר מוסק מסומן `EXTRACTED`, ‏`INFERRED` או `AMBIGUOUS`. אתם תמיד יודעים מה נמצא ומה נוחש.

---

## אילו קבצים זה מטפל בהם

| סוג | סיומות |
|------|-----------|
| קוד (36 דקדוקי tree-sitter) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (‏`.dm`/`.dme` דורש `uv tool install graphifyy[dm]`; ‏`.mts`/`.cts` עושים שימוש חוזר בדקדוק TypeScript, ואילו `.cc`/`.cxx`, ‏CUDA ‏`.cu`/`.cuh` ו-Metal ‏`.metal` עושים שימוש חוזר בדקדוק C++) |
| Salesforce Apex | `.cls .trigger` (מבוסס regex; מחלקות, ממשקים, enums, מתודות, טריגרים, קשתות SOQL/DML) |
| Terraform / HCL | `.tf .tfvars .hcl` (דורש `uv tool install graphifyy[terraform]`) |
| הגדרות MCP | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — מחלץ צמתי שרת, הפניות לחבילות ודרישות למשתני סביבה |
| מניפסטים של חבילות | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — צומת חבילה קנוני אחד לכל חבילה (לפי שם) בתוספת קשתות `depends_on`, כך שחבילה שמופנית ממניפסטים רבים היא hub יחיד |
| מסמכים | `.md .mdx .qmd .html .txt .rst .yaml .yml` (קישורי markdown מסוג `[text](./other.md)` ו-`[[wikilinks]]` הופכים לקשתות `references` בין מסמכים) |
| Office | `.docx .xlsx` (דורש `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (בהצטרפות מרצון; דורש אימות `gws` ו-`--google-workspace`; ‏Sheets דורש `uv tool install graphifyy[google]`) |
| קובצי PDF | `.pdf` |
| תמונות | `.png .jpg .webp .gif` |
| וידאו / אודיו | `.mp4 .mov .mp3 .wav` ועוד (דורש `uv tool install graphifyy[video]`) |
| YouTube / כתובות URL | כל כתובת של סרטון (דורש `uv tool install graphifyy[video]`) |

הקוד מחולץ **מקומית וללא קריאות API** (‏AST באמצעות tree-sitter). כל השאר עובר דרך ה-API של המודל בעוזר ה-AI שלכם.

קובצי `.gdoc`, ‏`.gsheet` ו-`.gslides` של Google Drive לשולחן העבודה הם
מצביעי קיצור דרך, ולא תוכן המסמך. כדי לכלול Google Docs, ‏Sheets ו-Slides מקוריים
בחילוץ headless, התקינו ואמתו את
[‏`gws` CLI](https://github.com/googleworkspace/cli), ואז הריצו:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

אפשר גם להגדיר `GRAPHIFY_GOOGLE_WORKSPACE=1`. ‏Graphify מייצא קיצורי דרך אל
`graphify-out/converted/` כקובצי Markdown נלווים, ואז מחלץ את הקבצים האלה.

---

## פקודות נפוצות

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

ראו [Decouple: מועמדי Extract-Class מדורגי סיכון](#decouple-מועמדי-extract-class-מדורגי-סיכון) למעלה, או את [סימוכין מלא לפקודות](#סימוכין-מלא-לפקודות) למטה.

---

## התעלמות מקבצים

צרו קובץ `.graphifyignore` בשורש הפרויקט — אותו תחביר כמו `.gitignore`, כולל שלילה עם `!`.

**הקובץ `.gitignore` מכובד אוטומטית.** ‏graphify קורא את `.gitignore` בכל תיקייה. אם קיים גם `.graphifyignore`, השניים **ממוזגים** — התבניות של `.graphifyignore` נבדקות אחרונות, ולכן הן מנצחות בהתנגשויות (כולל שלילות `!`). הוספת `.graphifyignore` תמיד רק מרחיבה את ההחרגה; היא לעולם לא מחזירה קובץ ש-`.gitignore` שלכם כבר החריג. תיחום לתת-תיקיות עובד בדיוק כמו ב-git — קובץ ignore משפיע רק על תת-העץ שלו.

העבירו `--no-gitignore` ל-`graphify extract` כאשר קוד מיוצר או מתומלל ש-git מתעלם ממנו כן שייך לגרף. זה משבית את `.gitignore` ואת `.git/info/exclude`; ‏`.graphifyignore` עדיין חל.

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

## הקמה לצוות

התיקייה `graphify-out/` נועדה להיכנס ל-git כך שכל חברי הצוות מתחילים עם מפה.

**תוספות מומלצות ל-`.gitignore`:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> הקובץ `manifest.json` ניתן כעת להעברה — המפתחות נשמרים כנתיבים יחסיים ומעוגנים מחדש בטעינה, כך שביצוע commit לו בטוח וחוסך בנייה מלאה מחדש ב-checkout הראשון.

**זרימת עבודה:**
1. אדם אחד מריץ `/graphify .` ומבצע commit ל-`graphify-out/`.
2. כולם מושכים — העוזר שלהם קורא את הגרף מיד.
3. הריצו `graphify hook install` לבנייה אוטומטית מחדש אחרי כל commit (רק AST, ללא עלות API). זה גם מגדיר merge driver של git כך ש-`graph.json` לעולם לא נשאר עם סימני קונפליקט — שני מפתחים שמבצעים commit במקביל מקבלים מיזוג איחוד אוטומטי של הגרפים שלהם.
4. כשמסמכים או מאמרים משתנים, הריצו `/graphify --update` כדי לרענן את הצמתים האלה.

---

## שימוש ישיר בגרף

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

שרת ה-MCP מעניק לעוזר שלכם גישה מובנית: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### שרת HTTP משותף

הדגל `--transport stdio` (ברירת המחדל) מריץ שרת מקומי אחד לכל מפתח. הדגל `--transport http` מגיש את אותם הכלים דרך ה-MCP Streamable HTTP transport, כך שתהליך משותף יחיד יכול להגיש את הגרף לכל הצוות — הלקוחות מכוונים את הגדרות ה-MCP ב-IDE אל `http://<host>:8080/mcp` במקום להריץ graphify מקומית.

| דגל | ברירת מחדל | מטרה |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | סוג ה-transport שעליו מגישים |
| `--host` | `127.0.0.1` | כתובת ה-bind ל-HTTP (השתמשו ב-`0.0.0.0` כדי לחשוף מעבר ל-localhost) |
| `--port` | `8080` | פורט ה-bind ל-HTTP |
| `--api-key` | משתנה סביבה `GRAPHIFY_API_KEY` | דורש `Authorization: Bearer <key>` (או `X-API-Key`) |
| `--path` | `/mcp` | נתיב ה-mount ב-HTTP |
| `--json-response` | כבוי | מחזיר JSON רגיל במקום זרמי SSE |
| `--stateless` | כבוי | ללא מצב לכל סשן (עבור פריסות עם איזון עומסים / CI) |
| `--session-timeout` | `3600` | מנקה סשנים עם מצב שאינם פעילים אחרי N שניות (‏`0` מבטל) |

ברירת המחדל `127.0.0.1` היא loopback בלבד. הגדירו `--host 0.0.0.0` **וגם** `--api-key` יחד כשחושפים על מארח משותף. הרצה בקונטיינר:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **הערה ל-WSL / Linux:** ‏Ubuntu מגיע עם `python3`, לא `python`. השתמשו ב-venv כדי להימנע מהתנגשויות:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## משתני סביבה

אלה נחוצים רק עבור **חילוץ headless / CI** (`graphify extract`). כשמריצים דרך ה-skill ‏`/graphify` בתוך ה-IDE, ה-API של המודל מסופק על ידי סשן ה-IDE — אין צורך במפתחות נוספים.

| משתנה | משמש עבור | מתי נדרש |
|---|---|---|
| `ANTHROPIC_API_KEY` | ‏backend של Claude (Anthropic) | `--backend claude` |
| `ANTHROPIC_BASE_URL` | כתובת endpoint תואמת Anthropic (‏LiteLLM proxy, שערים, ...) | `--backend claude` (ברירת מחדל: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | שם המודל עבור ה-backend של Claude — עבור endpoints מותאמים, השתמשו בשם/כינוי המודל שהשרת שלכם חושף | `--backend claude` (ברירת מחדל: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` או `GOOGLE_API_KEY` | ‏backend של Google Gemini | `--backend gemini` |
| `OPENAI_API_KEY` | ‏OpenAI או ממשקים תואמי OpenAI | `--backend openai` (שרתים מקומיים מקבלים כל ערך שאינו ריק) |
| `OPENAI_BASE_URL` | כתובת שרת תואם OpenAI (‏llama.cpp, ‏vLLM, ‏LM Studio, ...) | `--backend openai` (ברירת מחדל: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | שם המודל עבור ה-backend של OpenAI — עבור שרתים באחסון עצמי, השתמשו בשם/כינוי המודל שהשרת חושף (בדקו את ה-endpoint ‏`/v1/models` שלו), למשל `LFM2.5-8B-A1B-UD-Q4_K_XL` עבור llama.cpp | `--backend openai` (ברירת מחדל: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | ‏backend של DeepSeek | `--backend deepseek` |
| `MOONSHOT_API_KEY` | ‏backend של Kimi Code | `--backend kimi` |
| `OLLAMA_BASE_URL` | כתובת הרצה מקומית של Ollama | `--backend ollama` (ברירת מחדל: `http://localhost:11434`) |
| `OLLAMA_MODEL` | שם המודל של Ollama | `--backend ollama` (ברירת מחדל: זיהוי אוטומטי) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | דריסת גודל חלון ה-KV-cache של Ollama | אופציונלי — נקבע אוטומטית כברירת מחדל |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | דקות להשארת מודל Ollama טעון | אופציונלי — הגדירו `0` כדי לפרוק אחרי כל chunk |
| `AZURE_OPENAI_API_KEY` | ‏backend של Azure OpenAI Service | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | כתובת ה-endpoint של משאב Azure | `--backend azure` (נדרש לצד מפתח ה-API) |
| `AZURE_OPENAI_API_VERSION` | דריסת גרסת ה-API של Azure | אופציונלי — ברירת מחדל `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` או `GRAPHIFY_AZURE_MODEL` | שם ה-deployment ב-Azure | אופציונלי — ברירת מחדל `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — שרשרת האישורים הסטנדרטית | `--backend bedrock` (ללא מפתח API, משתמש ב-IAM) |
| `GRAPHIFY_MAX_WORKERS` | מספר ה-threads למקביליות AST | אופציונלי — גם הדגל `--max-workers` |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | העלאת תקרת הפלט עבור קורפוסים צפופים | אופציונלי — למשל `32768` לקבצים גדולים |
| `GRAPHIFY_API_TIMEOUT` | timeout לכל קריאה בשניות עבור ה-backends של HTTP, ‏claude-cli, ‏Anthropic SDK ו-Bedrock (ברירת מחדל: 600) | אופציונלי — גם הדגל `--api-timeout` |
| `GRAPHIFY_MAX_RETRIES` | כמה פעמים לנסות שוב בקשה שנחסמה בהגבלת קצב (429) לפני ויתור (ברירת מחדל: 6; מכבד `Retry-After`) | אופציונלי — העלו עבור מגבלות ארגון נוקשות (למשל kimi); ‏`0` מבטל |
| `GRAPHIFY_FORCE` | כפיית בנייה מחדש של הגרף גם עם פחות צמתים | אופציונלי — גם הדגל `--force` |
| `GRAPHIFY_GOOGLE_WORKSPACE` | הפעלה אוטומטית של ייצוא Google Workspace | אופציונלי — הגדירו ל-`1` |
| `GRAPHIFY_TRIAGE_BACKEND` | ‏backend עבור `graphify prs --triage` | אופציונלי — מזוהה אוטומטית מהמפתחות הזמינים |
| `GRAPHIFY_TRIAGE_MODEL` | דריסת המודל עבור triage | אופציונלי — למשל `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | הגדירו ל-`1` כדי להפעיל את יומן השאילתות המקומי ב-`~/.cache/graphify-queries.log` (מתעד כל שאלת query/path/explain + נתיב הקורפוס). כבוי כברירת מחדל — שום דבר לא נכתב אלא אם בחרתם להצטרף (#1797) | אופציונלי |
| `GRAPHIFY_QUERY_LOG` | מפעיל את יומן השאילתות וכותב אותו לנתיב הזה במקום לברירת המחדל | אופציונלי — כבוי אלא אם זה או `_ENABLE` הוגדרו |
| `GRAPHIFY_QUERY_LOG_DISABLE` | הגדירו ל-`1` כדי לכבות בכוח את יומן השאילתות (מנצח את משתני ההפעלה) | אופציונלי |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | כשהיומן מופעל, מתעד גם תשובות תת-גרף מלאות (כבוי כברירת מחדל) | אופציונלי |
| `GRAPHIFY_MAX_GRAPH_BYTES` | דריסת תקרת הגודל של graph.json בת 512 MiB — למשל `700MB`, ‏`2GB`, או בתים בלבד | אופציונלי — שימושי לקורפוסים גדולים במיוחד |
| `GRAPHIFY_MAX_CONTEXTS` | מספר גרפי הפרויקט שאינם ברירת מחדל שנשמרים בשרת MCB רב-פרויקטי אחד | אופציונלי — ברירת מחדל: `8`; ערכים לא חוקיים משתמשים ב-`8`, וערכים מתחת ל-`1` משתמשים ב-`1` |
| `GRAPHIFY_LLM_TEMPERATURE` | דריסת ה-temperature של ה-LLM עבור חילוץ סמנטי — למשל `0.7`, או `none` להשמטה | אופציונלי — מושמט אוטומטית עבור מודלי reasoning מסוג o1/o3/o4/gpt-5 |

---

## פרטיות

- **קובצי קוד** — מעובדים מקומית באמצעות tree-sitter. שום דבר לא יוצא מהמחשב שלכם. קורפוס של קוד בלבד אינו דורש מפתח API — ‏`graphify extract` רץ לגמרי במצב לא מקוון. במאגר מעורב, הוסיפו `--code-only` כדי לאנדקס רק את הקוד ולדלג על מסמכים/PDF/תמונות שהיו דורשים LLM.
- **וידאו / אודיו** — מתומללים מקומית עם faster-whisper. שום דבר לא יוצא מהמחשב שלכם.
- **מסמכים, קובצי PDF, תמונות** — נשלחים לעוזר ה-AI שלכם לחילוץ סמנטי (דרך ה-skill ‏`/graphify`, עם המודל שסשן ה-IDE שלכם מריץ). ‏`graphify extract` ב-headless דורש `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), ‏`MOONSHOT_API_KEY` (Kimi), ‏`ANTHROPIC_API_KEY` (Claude), ‏`OPENAI_API_KEY` (OpenAI), ‏`DEEPSEEK_API_KEY` (DeepSeek), מופע Ollama פעיל (`OLLAMA_BASE_URL`), אישורי AWS דרך שרשרת הספקים הסטנדרטית (Bedrock — ללא צורך במפתח API, משתמש ב-IAM), או את הבינארי `claude` של ה-CLI (Claude Code — ללא צורך במפתח API, משתמש במנוי Claude שלכם). הדגל `--dedup-llm` משתמש באותו מפתח.
- **מיקום נתונים** — ‏`graphify extract` מזהה אוטומטית באיזה ספק להשתמש לפי מפתח ה-API שהוגדר (סדר עדיפויות: Gemini ← Kimi ← Claude ← OpenAI ← DeepSeek ← Azure ← Bedrock ← Ollama). עבור קוד עם דרישות מיקום נתונים, השתמשו ב-`--backend ollama` (מקומי לחלוטין) או העבירו דגל `--backend` מפורש. ‏Kimi (`MOONSHOT_API_KEY`) מנתב לשרתי Moonshot AI בסין.
- **ללא טלמטריה**, ללא מעקב שימוש, ללא analytics.
- **תיעוד שאילתות** — כל קריאה ל-`graphify query`, ‏`graphify path`, ‏`graphify explain` ול-`query_graph` ב-MCP מתועדת ב-`~/.cache/graphify-queries.log` בפורמט JSON Lines (חותמת זמן, שאלה, קורפוס, צמתים שהוחזרו, משך). תשובות תת-גרף מלאות **אינן** נשמרות כברירת מחדל. הגדירו `GRAPHIFY_QUERY_LOG_DISABLE=1` כדי לבטל, או `GRAPHIFY_QUERY_LOG=/dev/null` כדי להשתיק בלי לנטרל את נתיב הקוד.

---

## פתרון תקלות

**‏`graphify: command not found` אחרי ההתקנה**
ה-CLI מותקן אבל תיקיית ה-bin שלו אינה ב-`PATH` של ה-shell. בחרו את הפתרון לפי אופן ההתקנה:
- **uv** (`uv tool install graphifyy`): הפקודה נוחתת בתיקיית ה-bin של כלי uv (`~/.local/bin`), שלרוב אינה ב-`PATH` בהתקנה טרייה של macOS/zsh. הריצו `uv tool update-shell`, ואז פתחו טרמינל חדש. (אתרו את התיקייה עם `uv tool dir --bin`.)
- **pipx** (`pipx install graphifyy`): הריצו `pipx ensurepath`, ואז פתחו טרמינל חדש.
- **pip** (`pip install graphifyy`): ‏pip מתקין תסריטים לתיקיית bin של המשתמש שעשויה לא להיות ב-`PATH` — הוסיפו `~/Library/Python/3.x/bin` (macOS) או `~/.local/bin` (Linux) ל-`PATH` בקובץ `~/.zshrc`/`~/.bashrc`, או פשוט הריצו `python -m graphify`.

**‏`uvx graphify …` או `uv tool run graphify …` נכשלים בפתירת `graphify`**
חבילת ה-PyPI היא `graphifyy`; ‏`graphify` היא רק הפקודה שהיא מספקת. הפקודה `uv tool run` מתייחסת למילה הראשונה כאל *שם חבילה*, ולכן היא מחפשת חבילה בשם `graphify` ומדווחת `No solution found … no versions of graphify`. ציינו את החבילה במפורש: `uvx --from graphifyy graphify install` (זהה ל-`uv tool run --from graphifyy graphify install`). לחלופין הריצו `uv tool install graphifyy` פעם אחת ואז קראו ל-`graphify` ישירות.

**‏`uv run --with graphifyy python -m graphify` מריץ בשקט התקנה ישנה**
הפקודה `uv run` משתמשת ב-Python של ה*מערכת*, ולכן אם גם `graphifyy` ישן יותר נמצא שם (למשל מ-`pip install graphifyy` בעבר), ‏Python עלול למצוא את העותק הזה ראשון ב-`sys.path` ו-`--with graphifyy` לא ידרוס אותו. זה רץ ללא שגיאה, אבל אתם מקבלים את התנהגות הגרסה ה*ישנה* — למשל דריסות של משתני סביבה כמו `OPENAI_BASE_URL` מתעלמות בשקט, כך שהבקשות מגיעות ל-endpoint ברירת המחדל ונכשלות עם 401 שנראה כמו מפתח שגוי. הסימן המזהה הוא השורה `warning: skill is from graphify <newer>, package is <older>` — כלומר נטענה התקנה אחרת, ולא רק skill מיושן. בדקו איזה עותק נטען בפועל:
```bash
python -c "import graphify; print(graphify.__file__)"
```
ואז הריצו את הפקודה המותקנת ישירות (היא משתמשת בעותק שמנוהל על ידי uv), או הסירו את העותק הישן במערכת:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**‏`python -m graphify` עובד אבל הפקודה `graphify` לא**
ה-`PATH` של ה-shell שלכם לא כולל את תיקיית ה-bin שאליה הותקנה הפקודה. העדיפו `uv tool install` / `pipx install` על פני `pip` רגיל, ואז הריצו `uv tool update-shell` / `pipx ensurepath` ופתחו טרמינל חדש (ראו את הערות ההתקנה למעלה).

**‏`/graphify .` גורם ל-"path not recognized" ב-PowerShell**
‏PowerShell מתייחס ללוכסן פותח כאל מפריד נתיבים. השתמשו ב-`graphify .` (בלי לוכסן) ב-Windows.

**לגרף יש פחות צמתים אחרי `--update` או בנייה מחדש**
אם ריפקטור מחק קבצים, הצמתים הישנים נשארים. העבירו `--force` (או הגדירו `GRAPHIFY_FORCE=1`) כדי לדרוס גם כשלבנייה המחודשת יש פחות צמתים.

**‏`extract` יוצא עם "extraction was incomplete ... refusing to overwrite"**
כאשר מעבר חילוץ קורס או שהסריקה לא מצליחה לקרוא את הקורפוס במלואו, ההרצה תהיה קטנה מהרצה שלמה, ולכן `graphify extract` מסרב לדרוס גרף קיים גדול יותר בתוצאה חלקית (הגנה על `graph.json` שלכם). תקנו את הכשל הבסיסי והריצו שוב, או העבירו `--allow-partial` כדי לדרוס בכל זאת.

**לגרף יש צמתים כפולים לאותה ישות (כפילויות רפאים)**
כפילויות רפאים (אותו סמל מופיע פעמיים — פעם מחילוץ AST עם מיקום מקור, ופעם מחילוץ סמנטי בלעדיו) ממוזגות כעת אוטומטית בזמן הבנייה. אם אתם רואים זאת בגרף שנבנה לפני v0.8.33, הריצו חילוץ מחדש מלא כדי לנקות:
```bash
graphify extract . --force
```

**ל-Ollama נגמר ה-VRAM / חריגה מחלון ההקשר**
חלון ה-KV-cache נקבע אוטומטית אך עשוי להיות גדול מדי ל-GPU שלכם. הקטינו אותו:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**אזהרות `LLM returned invalid JSON` / `Unterminated string`**
תשובת ה-JSON של המודל נתקלה במגבלת טוקני הפלט ונחתכה באמצע מחרוזת. ‏graphify מתאושש אוטומטית (הוא מפצל את ה-chunk ומחלץ מחדש את החצאים, ומסמך יחיד גדול מדי נחתך תחילה בגבולות כותרות/פסקאות כך שכל הקובץ עדיין מכוסה), ולכן האזהרות האלה רועשות אך אינן אובדן נתונים. כדי להפחית את התחלופה, העלו את תקרת הפלט או הקטינו את הפלט של כל chunk:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
עם שער ענן כמו OpenRouter, העדיפו `--backend openai` (הגדירו `OPENAI_BASE_URL`) על פני ה-shim של Ollama — זה נתיב תואם-OpenAI נקי יותר. אם למודל יש תקרת פלט משלו, הורדת `--token-budget` היא הידית האמינה.

**קובץ ה-HTML של הגרף גדול מדי לפתיחה בדפדפן (מעל 5000 צמתים)**
דלגו על יצירת ה-HTML והשתמשו ישירות ב-JSON:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**ל-`graph.json` יש סימני קונפליקט אחרי ששני מפתחים ביצעו commit בו-זמנית**
הריצו `graphify hook install` — הוא מגדיר merge driver של git שממזג את `graph.json` באיחוד אוטומטי, כך שקונפליקטים פשוט לא קורים.

**החילוץ מחזיר צמתים/קשתות ריקים עבור מסמכים או PDF**
מסמכים, קובצי PDF ותמונות דורשים קריאה ל-LLM — קורפוסים של קוד בלבד אינם צריכים מפתח. ודאו שמפתח ה-API מוגדר ושה-backend נכון:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**אזהרה על אי-התאמת גרסת skill ב-IDE שלכם**
גרסת graphify המותקנת שונה מקובץ ה-skill. עדכנו:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**מטמון ה-prompt של Claude Code מתבטל אחרי כל `graphify extract`**
‏Graphify כותב קובצי פלט (`graph.json`, ‏`graphify-out/`) לתוך סביבת העבודה. אם הנתיבים האלה אינם מוחרגים, כל כתיבה מבטלת את מטמון ה-prompt של Claude Code וכופה העלאה מלאה מחדש בתעריפי cache-write בתור הבא. הוסיפו אותם ל-`.claudeignore`:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## סימוכין מלא לפקודות

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

> **שמות קהילות:** בתוך סוכן (Claude Code, ‏Gemini CLI) הסוכן עצמו מעניק שמות לקהילות. כשמריצים את ה-CLI החשוף, ‏`cluster-only` מעניק להן שמות אוטומטית באמצעות ה-backend המוגדר (מובנה או ספק מותאם תואם-OpenAI) — העבירו `--no-label` כדי להשאיר `Community N`, או הריצו `graphify label` כדי לייצר שמות (מחדש) לפי דרישה.

---

## למידע נוסף

- [איך זה עובד](../how-it-works.md) — צינור החילוץ, זיהוי קהילות, ניקוד ודאות, benchmarks
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — פירוט המודולים, איך מוסיפים שפה
- [אינטגרציות אופציונליות](../docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — הספר על הרעיונות שמאחורי graphify, הארכיטקטורה מקצה לקצה

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) היא השכבה הפעילה-תמיד שנבנתה מעל graphify — היא מיישמת את אותה גישת גרף על כל הקשר העבודה שלכם: פגישות, קבצים, מסמכים וקוד, ומתעדכנת ברציפות ברקע.

נבנתה עבור אנשים וצוותים שהעבודה שלהם מתפרסת על פני מאות שיחות ומסמכים שהם לעולם לא יוכלו לשחזר במלואם.

**[הצטרפו לרשימת ההמתנה ב-graphify.com](https://graphify.com).** ניסיון חינם יושק בקרוב.

---

<details>
<summary>תרומה לפרויקט</summary>

### הקמת סביבת פיתוח

הפרויקט משתמש ב-[uv](https://docs.astral.sh/uv/) עבור זרימת עבודת הפיתוח. התקינו אותו פעם אחת, ואז:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

אמתו את ההתקנה במצב editable:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### הרצת בדיקות

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> הערה ל-macOS: חבילת הבדיקות כוללת גם את `sample.f90` וגם את `sample.F90` כ-fixtures. אלה מתנגשים במערכות קבצים HFS+ / APFS שאינן רגישות לאותיות גדולות/קטנות. הריצו על Linux או בקונטיינר Docker אם אתם צריכים לבדוק את שתי גרסאות Fortran בו-זמנית.

### זרימת עבודה ב-git

- הפיתוח הפעיל מתרחש בענף `v8`.
- סגנון commit: ‏`fix: <description>` / `feat: <description>` / `docs: <description>`
- לפני פתיחת PR, הריצו `uv run pytest tests/ -q` וודאו שהוא עובר.
- הוסיפו קובץ fixture אל `tests/fixtures/` ובדיקות אל `tests/test_languages.py` עבור כל מחלץ שפה חדש.

### מה כדאי לתרום

**דוגמאות מעובדות** הן התרומה המועילה ביותר. הריצו `/graphify` על קורפוס אמיתי, שמרו את הפלט ב-`worked/{slug}/`, כתבו `review.md` כן שמתאר מה הגרף קלע נכון ובמה טעה, ופתחו PR.

**באגים בחילוץ** — פתחו issue עם קובץ הקלט, רשומת המטמון (`graphify-out/cache/`), ומה פוספס או היה שגוי.

ראו [ARCHITECTURE.md](../../ARCHITECTURE.md) עבור אחריות המודולים וכיצד להוסיף שפה.

</details>
