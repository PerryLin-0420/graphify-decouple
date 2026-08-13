<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b><a href="https://github.com/Graphify-Labs/graphify">graphify</a> loyihasining <code>graphify decouple</code> qoʻshilgan fork'i</b> — god object'lar uchun 0-LLM, xavf bahosi berilgan Extract-Class nomzodlari; tavsiya berishdan oldin ular faqat call graph bilan emas, balki haqiqiy manba kodi bilan qayta tekshiriladi. Quyidagi <a href="#decouple-xavf-bahosi-bilan-extract-class-nomzodlari">Decouple: xavf bahosi bilan Extract-Class nomzodlari</a> boʻlimiga qarang.
</p>

<div align="center">
<details><summary><b>Buni boshqa tillarda oʻqing</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>graphify platformasiga erta kirish ochiq — ommaviy v1 chiqishidan oldin: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

AI kodlash yordamchingizda `/graphify` deb yozing va u butun loyihangizni (kod, hujjatlar, PDF'lar, rasmlar, videolar) **bilim grafiga** aylantiradi — endi fayllarni grep qilish oʻrniga **soʻrov yuborasiz**.

- **Kod xaritalari bepul va toʻliq lokal.** Kod tree-sitter AST bilan tahlil qilinadi: deterministik, LLM'siz, hech narsa kompyuteringizdan chiqmaydi. (Hujjatlar, PDF'lar, rasmlar va videolar semantik bosqich uchun yordamchingizning modelidan yoki sozlangan API kalitidan foydalanadi.)
- **Har bir qirra izohlanadi.** Har bir bogʻlanish `EXTRACTED` (manbada aniq koʻrsatilgan) yoki `INFERRED` (graphify tomonidan aniqlangan) deb belgilanadi, shuning uchun nima bevosita oʻqilgani va nima xulosa qilingani sizga ayon boʻladi.
- **Bu vektor indeks emas.** Embedding yoʻq, vektor ombori yoʻq: siz kezib chiqadigan haqiqiy graf. Savol bering, ikki narsa orasidagi yoʻlni kuzating yoki bitta tushunchani tushuntiring.

> Buni faqat talab boʻyicha emas, balki kod, hujjatlar va uchrashuvlaringiz boʻylab fonda doimiy yangilanib turadigan holda xohlaysizmi? Aynan shuni **[graphify.com](https://graphify.com)**'da qurmoqdamiz va erta kirish hozir **[app.graphify.com](https://app.graphify.com/login)**'da ochiq.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="graphify'ning interaktiv graph.html sahifasi FastAPI kod bazasini kuch bilan joylashtirilgan bilim grafi sifatida va aniqlangan hamjamiyatlar legendasi bilan koʻrsatmoqda" width="900">
</p>
<p align="center">
  <em>graphify tomonidan xaritalangan FastAPI kod bazasi. Har bir tugun — bu tushuncha, ranglar — aniqlangan hamjamiyatlar va butun narsa graph.html ichida bosiladi.</em>
</p>

**Boshlash** (30 soniya):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

Soʻngra AI yordamchingizda:

```
/graphify .
```

Tamom. Siz **uchta fayl** olasiz:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**Quyidagilarda ishlaydi:** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot va yana 15+ — [platformangizni tanlang](#installyatsiya).

---

## Amalda koʻring

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="graphify path soʻrovi: terminal FastAPI va ModelField orasidagi eng qisqa yoʻlni soʻraydi, javob esa bilim grafi boʻylab qadamma-qadam yonib chiqadi" width="900">
</p>

Graf qurilgach, fayllarni oʻqish oʻrniga unga soʻrov yuborasiz. Haqiqiy natija — yuqorida koʻrsatilgan FastAPI kod bazasida ishlatilgan graphify:

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

Har bir qirra **ishonch belgisini** olib yuradi (`EXTRACTED` = manbada aniq, `INFERRED` = aniqlash orqali chiqarilgan), shuning uchun nima bevosita oʻqilgani va nima xulosa qilingani ayon boʻladi. `graphify query "<question>"` oddiy tilda berilgan savol uchun chegaralangan qism-grafni qaytaradi, `graphify path A B` esa istalgan ikki narsa qanday bogʻlanishini kuzatadi.

---

## Decouple: xavf bahosi bilan Extract-Class nomzodlari

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: MainWindow god tuguni xavf bahosi berilgan nomzod klasslarga boʻlinmoqda, ulardan ikkitasi orasida umumiy state haqida ogohlantirish bor" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: MainWindow uchun taklif qilingan 5 klass, Node Info paneli Main Window Axis and Range Controls uchun ochiq va Main Window Controller Core bilan 0.608 state kesishuvini koʻrsatmoqda" width="900">
</p>
<p align="center">
  <em>Haqiqiy ishga tushirishda DECOUPLE.html — taklif qilingan klassni bosish uning qaysi boshqa klass bilan state ulashishini va aynan nima ulashilishini aniq koʻrsatadi.</em>
</p>

Xuddi shu sahifa boʻlinishning oʻzini ham chizadi. **Preview decoupled view** tugmasini yoqish god klassning oʻz metodlarini taklif qilingan klasslarga almashtiradi va qirralarni oʻsha joyda qayta yoʻnaltiradi — bu qayta chizilgan diagramma emas, ulanishlarning haqiqiy oʻzgarishi:

| Oldin — god klass bugungi holatda | Keyin — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html tugma yoqilishidan oldin: atrofida oʻz metodlari yoyilgan bitta MainWindow markaz tuguni" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html tugma yoqilgandan keyin: oʻsha tugun 5 ta romb shaklidagi taklif qilingan klassga qisqargan, yashil punktir qirralar qaysi metodlar qayerga ajratilganini, qizil qirralar esa ulardan ikkitasi ulashadigan instansiya state'ini koʻrsatmoqda" width="440"> |
| Bitta tugun oʻzining 47 ta metodini saqlaydi va ularning har biriga faqat klass orqali yetib borish mumkin. | Taklif qilingan klasslar. Yashil punktir = har biriga nima ajratilgani; qizil = ulardan ikkitasi hamon ulashadigan instansiya state'i, aynan shu `split` va `keep_as_is` oʻrtasida qaror qiladi. Faqat xavf chegarasidan oʻtgan nomzodlar chiziladi — bu yerda 6 tadan 5 tasi, shuning uchun bitta metod uchun qoʻnadigan romb yoʻq. |

`graphify decouple` god object'larni topadi va ularni boʻlish haqiqatan arziydimi degan savolga javob beradi — nafaqat ular katta ekanini aytadi.

Bu vosita ushlash uchun yaratilgan nosozlik namunasi: 47 ta metodli klassni call graph klasterlash bemalol 5 ta ozoda koʻrinadigan guruhga boʻladi, biroq ularning barchasi ostida hamon aynan bir xil `self._chart_style` / `self._crosshair` instansiya state'ini oʻqiydi va yozadi. Shunday boʻlinishni chiqarsangiz, siz hech nimani ajratmagan boʻlasiz — metodlarni yangi fayllarga koʻchirgansiz, xolos; ular hamon mustaqil test qilinmaydi, oʻzgartirilmaydi va tushunilmaydi, chunki barchasiga oʻsha umumiy state qaytarib berilishi kerak. Faqat call graph'ga qaraydigan vosita buni umuman koʻra olmaydi; buning uchun haqiqiy manba kodiga qaytish shart.

**Ikkita tekshiruv, ikkalasi ham 0-LLM va deterministik:**

1. **Bu umuman God Object'mi?** Yuqori darajali tugun haqiqiy God Object boʻlishi mumkin (koʻp OʻZ metodlari bogʻliq boʻlmagan mas'uliyatlarga tarqalgan — Extract Class qoʻllanadi) yoki haddan tashqari koʻp murojaat qilinadigan markaz/ma'lumot modeli boʻlishi mumkin (oʻz metodlari kam, asosan *kiruvchi* murojaatlar — uning tanasini boʻlish hech narsa bermaydi; yechim interfeysini toraytirish, klass ajratish emas). `classify_god_node` bularni xom daraja emas, `member_ratio` orqali farqlaydi — aynan shu farq `TraceSource` (84 qirra, lekin atigi 6 ta oʻz metodi) uchun soxta boʻlish taklifi berilishining oldini oladi, `MainWindow` (88 qirra, 47 ta oʻz metodi) esa uni haqli ravishda oladi.
2. **Boʻlinish haqiqatan bogʻliqlikni kamaytiradimi?** `risk_before` (god tugunning hozirgi hajmi/bogʻliqligi/parchalanganligi) `risk_after` bilan solishtiriladi — bu boʻlinishning oʻzi keltirib chiqaradigan YANGI xavf: ilgari klass ichidagi koʻrinmas qirralar boʻlgan va endi klasslararo aniq bogʻliqlikka aylanadigan guruhlararo chaqiruvlar, endi bittadan ortiq yangi klassga bogʻlanishi kerak boʻladigan chaqiruvchilar va — call graph tuzilishi jihatidan bajara olmaydigan tekshiruv — taklif qilingan guruhlar aslida qancha `self`/`this` instansiya state'ini (oʻqishlar, yozishlar va umumiy yordamchi metod chaqiruvlari alohida vaznlanadi: umumiy **yozish** umumiy oʻqishdan yuqori baholanadi) umumiy ishlatishi. Buning uchun god tugunning oʻz manba fayli tree-sitter bilan bevosita qayta tahlil qilinadi; graphify'ning oʻz ajratilgan grafiga tayanilmaydi, chunki u hech bir til uchun maydon darajasidagi murojaatni yozib olmaydi. Faqat `risk_after` `risk_before`'dan chegara qadar past boʻlgandagina reja `split` deb tavsiya beradi — aks holda u `marginal` yoki `keep_as_is` boʻladi, tavsiya etilmagan nomzod esa raqam sifatida xabar qilinadi va koʻz bilan shubhalanib chiqishingiz kerak boʻlgan shakl sifatida hech qachon chizilmaydi.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

`graph.json` yonida uchta fayl chiqaradi:

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

**State ulashish tekshiruvi uchun tillar qamrovi** (yuqoridagi faqat call graph'ga asoslangan tasniflash graphify ajratadigan har bir til uchun ishlaydi; bu jadval aynan `self`/`this` state kesishuvini tasdiqlaydigan manba qayta tahlili haqida):

| Til | Qoʻllab-quvvatlanadi | Izohlar |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` alohida AST tugunidir, oʻralgan maydon murojaati emas — alohida ishlov beriladi |
| C# | ✅ | |
| Rust | ✅ | `impl` bloklari orqali `self.x` |
| Ruby | ✅ | `@x` (asosiy uslub) + `self.foo` chaqiruvlari |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | har bir metod uchun receiver aniqlanadi — Go'da `self`/`this` kalit soʻzi yoʻq, shuning uchun receiver nomi (`func (f *Foo) M()` dagi `f`) har bir metod uchun qaytadan aniqlanadi |
| C | ❌ | struct koʻrsatkichi parametrini boshqa parametrlardan ajratadigan sintaktik belgi yoʻq — toʻliq tip inferensiyasisiz ishonchli signal yoʻq |

Qoʻllab-quvvatlanmaydigan tildagi yoki manbasi oʻqib boʻlmaydigan god tugun `state_analysis: "skipped"` deb belgilanadi — tasniflash va call graph bahosi baribir ishlaydi, lekin tavsiya state tekshiruvi oʻtgan deb jimgina faraz qilish oʻrniga faqat call graph'ga tayanadi.

---

## U nima qiladi

Quti ochilishi bilan olasiz:

| Imkoniyat | Nima olasiz |
|---|---|
| **God tugunlar** | Eng koʻp bogʻlangan tushunchalar — hamma narsa nima orqali oqishini koʻrasiz |
| **Hamjamiyatlar** | Graf quyi tizimlarga boʻlinadi (Leiden), LLM'siz yorliqlar bilan |
| **Fayllararo bogʻlanishlar** | `calls` / `imports` / `inherits` / `mixes_in` tree-sitter AST orqali ~40 tilda aniqlanadi |
| **Query, path, explain** | Savol bering, ikki narsa orasidagi yoʻlni kuzating yoki bitta tushunchani tushuntiring — barchasi `graph.json` boʻyicha |
| **Asos + hujjat havolalari** | `# NOTE:` / `# WHY:` izohlari va ADR/RFC iqtiboslari kodga bogʻlangan toʻliq huquqli tugunlarga aylanadi |
| **Koddan tashqari** | Hujjatlar, PDF'lar, rasmlar va video/audio — barchasi bitta grafga tushadi |
| **Avvalo lokal** | Kod lokal tarzda tree-sitter bilan tahlil qilinadi (LLM yoʻq, hech narsa kompyuteringizdan chiqmaydi); faqat hujjatlar/media boʻyicha semantik bosqich backend'ga murojaat qiladi va faqat siz uni sozlagan boʻlsangiz |

---

## Benchmark'lar

| Benchmark | Metrika | graphify | Sohadagilar |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | QA accuracy | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | QA accuracy | **76%** | dense RAG bilan tenglashdi |
| Graf qurilishi | LLM kreditlari | **0** | koʻpchilik tizimlarda token boʻyicha toʻlanadi |

Har bir tizim bir xil harness'da, bir xil model va byudjetlar bilan ishlatilgan; baholovchi ikkinchi baholovchi bilan koʻr-koʻrona tasdiqlangan (90.6% moslik, Cohen kappa 0.81). Tizimlar boʻyicha toʻliq jadvallar, code-intelligence natijasi va takrorlash buyruqlari: **[BENCHMARKS.md](../../BENCHMARKS.md)**.

---

## Talablar

| Talab | Minimal | Tekshirish | Oʻrnatish |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(tavsiya etiladi)* | istalgan | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(muqobil)* | istalgan | `pipx --version` | `pip install pipx` |

**macOS uchun tezkor oʻrnatish (Homebrew):**
```bash
brew install python@3.12 uv
```

**Windows uchun tezkor oʻrnatish:**
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

## Installyatsiya

> **Rasmiy paket:** PyPI paketi `graphifyy` deb ataladi (ikkita y bilan). PyPI'dagi boshqa `graphify*` paketlari bu loyihaga aloqador emas. CLI buyrugʻi esa hamon `graphify`.

**1-qadam — paketni oʻrnating:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**2-qadam — skill'ni AI yordamchingizda roʻyxatdan oʻtkazing:**

```bash
graphify install
```

Tamom. AI yordamchingizni oching va `/graphify .` deb yozing.

Yordamchi skill'ini foydalanuvchi profilingiz oʻrniga joriy repozitoriyga oʻrnatish uchun
`--project` qoʻshing:

```bash
graphify install --project
graphify install --project --platform codex
```

Loyiha doirasidagi oʻrnatishlar joriy katalog ostiga yozadi, masalan
`.claude/skills/graphify/SKILL.md` yoki `.agents/skills/graphify/SKILL.md` (hamda skill talab boʻyicha
yuklaydigan `references/` yordamchi katalogi) va commit qilinishi mumkin boʻlgan fayllar uchun
`git add` maslahatini chiqaradi.
Loyiha doirasidagi oʻrnatishni qoʻllab-quvvatlaydigan platformaga xos buyruqlar ham shu bayroqni qabul qiladi,
masalan `graphify claude install --project` yoki `graphify codex install --project`.

> **PowerShell haqida eslatma:** `/graphify .` emas, `graphify .` deb yozing — PowerShell'da boshidagi slash yoʻl ajratuvchisi hisoblanadi.

> **`graphify: command not found` chiqdimi?** `uv tool install` / `pipx install` `graphify` buyrugʻini oʻz vosita bin katalogiga (`~/.local/bin`) joylaydi. Agar shell uni oʻrnatishdan soʻng darhol topa olmasa — yangi macOS + zsh sozlamalarida bu keng tarqalgan — demak, u katalog hali `PATH`'ingizda yoʻq: `uv tool update-shell` (yoki `pipx ensurepath`) ni bajaring va yangi terminal oching. Oddiy `pip` bilan `PATH`'ga `~/.local/bin` (Linux) yoki `~/Library/Python/3.x/bin` (Mac) ni qoʻshing yoki `python -m graphify` ni ishga tushiring.

> **Oʻrnatish oʻrniga `uvx` / `uv tool run` bilan ishlatyapsizmi?** Buyruqni emas, paket nomini yozing: `uvx --from graphifyy graphify install`. Oddiy `uvx graphify …` xatoga uchraydi (`No solution found … no versions of graphify`), chunki `uv tool run` birinchi soʻzni *paket* deb oʻqiydi, paket esa `graphifyy` — `graphify` buyrugʻi uning ichida yashaydi.

> **Mac/Windows'da iloji boricha `pip install` dan qoching.** Skill ishga tushish vaqtida Python'ni `graphify-out/.graphify_python` orqali aniqlaydi; agar u `pip` paketni oʻrnatgan muhitdan boshqasiga ishora qilsa, `ModuleNotFoundError: No module named 'graphify'` xatosini olasiz. `uv tool install` va `pipx install` paketni oʻz muhitida izolyatsiya qiladi va bundan butunlay qutqaradi.

> **Git hook'lari va uv tool / pipx:** `graphify hook install` oʻrnatish vaqtida joriy interpretator yoʻlini bevosita hook skriptlariga joylaydi, shuning uchun post-commit hook `~/.local/bin` PATH'da boʻlmagan GUI git mijozlari va CI runner'larida ham toʻgʻri ishlaydi. graphify'ni qayta oʻrnatsangiz yoki yangilasangiz, joylashtirilgan yoʻlni yangilash uchun `graphify hook install` ni qayta bajaring.

> **Qat'iy rejim (Claude Code):** `graphify install --project --strict` yordamchini grafdan haqiqatan foydalanishga majbur qiladi. Standart oʻrnatish uni fayllarni oʻqishdan oldin `graphify query` ishlatishga faqat *undaydi*; qat'iy rejim esa seansdagi birinchi xom manba oʻqishini *bloklaydi* va uni grafga yoʻnaltiradi, keyin yana undash rejimiga qaytadi (shuning uchun u seansda koʻpi bilan bir marta ishlaydi va hech qachon tiqilib qolmaydi). Ish vaqtida `GRAPHIFY_HOOK_STRICT=1`/`0` bilan almashtiring; standart oʻrnatish oʻzgarmagan (yumshoq undash).

<details>
<summary><b>Platformangizni tanlang</b> (20+ yordamchi, ochish uchun bosing)</summary>

| Platforma | Oʻrnatish buyrugʻi |
|----------|----------------|
| Claude Code (Linux/Mac) | `graphify install` |
| Claude Code (Windows) | `graphify install` (avtomatik aniqlanadi) yoki `graphify install --platform windows` |
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
| Agent Skills (freymvorklararo) | `graphify install --platform agents` (alias `--platform skills`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify install --platform pi` |
| Cursor | `graphify cursor install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

Codex foydalanuvchilariga parallel ajratish uchun `~/.codex/config.toml` faylidagi `[features]` ostida `multi_agent = true` ham kerak. CodeBuddy Claude Code bilan bir xil Agent vositasi va PreToolUse hook mexanizmidan foydalanadi. Factory Droid parallel subagent yuborish uchun `Task` vositasidan foydalanadi. OpenClaw va Aider ketma-ket ajratishdan foydalanadi (bu platformalarda parallel agent qoʻllab-quvvatlashi hali boshlangʻich bosqichda). Trae parallel subagent yuborish uchun Agent vositasidan foydalanadi va `PreToolUse` hook'larini qoʻllab-quvvatla**maydi**, shuning uchun AGENTS.md doimiy ishlaydigan mexanizm hisoblanadi.

`--platform agents` (alias `--platform skills`) umumiy freymvorklararo [Agent-Skills](https://github.com/anthropics/skills) joylashuvlarini nishonga oladi: global oʻrnatish uchun spetsifikatsiyaning foydalanuvchi darajasidagi `~/.agents/skills/` katalogi (`npx skills` va spetsifikatsiyaga mos freymvorklar oʻqiydi), loyiha (`--project`) oʻrnatishi uchun esa `./.agents/skills/`. Oddiy `graphify install` ataylab bitta platformaga (Claude Code) qaratilgan — skill `.agents/skills` ni oʻqiydigan har qanday freymvork uchun koʻrinadigan boʻlishini xohlasangiz, `agents` platformasini nomma-nom koʻrsating.

> Codex `/graphify` oʻrniga `$graphify` dan foydalanadi.

</details>

<details>
<summary><b>Ixtiyoriy qoʻshimchalar</b> (faqat kerakligini oʻrnating)</summary>

| Qoʻshimcha | Nima qoʻshadi | Oʻrnatish |
|---|---|---|
| `pdf` | PDF ajratish | `uv tool install "graphifyy[pdf]"` |
| `office` | `.docx` va `.xlsx` qoʻllab-quvvatlash | `uv tool install "graphifyy[office]"` |
| `google` | Google Sheets render qilish | `uv tool install "graphifyy[google]"` |
| `video` | Video/audio transkripsiyasi (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | MCP stdio serveri | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Neo4j'ga push qoʻllab-quvvatlash | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | FalkorDB'ga push qoʻllab-quvvatlash | `uv tool install "graphifyy[falkordb]"` |
| `svg` | SVG graf eksporti | `uv tool install "graphifyy[svg]"` |
| `leiden` | Leiden hamjamiyat aniqlash (faqat Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Ollama lokal inferensiyasi | `uv tool install "graphifyy[ollama]"` |
| `openai` | OpenAI / OpenAI'ga mos API'lar | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic Claude API (`--backend claude`, `ANTHROPIC_API_KEY` ishlatadi) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (IAM ishlatadi, API kaliti kerak emas) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT` ishlatadi) | `uv tool install "graphifyy[openai]"` |
| `sql` | SQL sxemasini ajratish | `uv tool install "graphifyy[sql]"` |
| `postgres` | Jonli PostgreSQL introspeksiyasi (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | BYOND DreamMaker `.dm`/`.dme` AST ajratish (platformangizga mos wheel boʻlmasa, C kompilyator + `python3-dev` kerak boʻlishi mumkin) | `uv tool install "graphifyy[dm]"` |
| `terraform` | Terraform / HCL `.tf`/`.tfvars`/`.hcl` AST ajratish | `uv tool install "graphifyy[terraform]"` |
| `pascal` | Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` AST ajratish (aniqroq `calls`/`inherits` qirralari; boʻlmasa regex ajratuvchiga qaytadi) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | Xitoycha soʻrovni segmentlash (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | Yuqoridagilarning barchasi | `uv tool install "graphifyy[all]"` |

</details>

---

## Yordamchingiz doimo grafdan foydalansin

Graf qurilgandan soʻng loyihangizda buni bir marta bajaring:

| Platforma | Buyruq |
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
| Agent Skills (freymvorklararo) | `graphify agents install` (alias `graphify skills install`) |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify pi install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

Bu kichik konfiguratsiya fayli yozadi va yordamchingizga kod bazasi haqidagi savollarda bilim grafiga murojaat qilishni, toʻliq hisobotni oʻqish yoki xom fayllarni grep qilish oʻrniga `graphify query "<question>"` kabi chegaralangan soʻrovlarni afzal koʻrishni aytadi.

- **Hook platformalari** (Claude Code, Gemini CLI): hook qidiruv turidagi vosita chaqiruvlaridan oldin (Claude Code'da esa Read/Glob vositalari orqali manba fayllarni birma-bir oʻqishdan oldin ham) avtomatik ishga tushadi va yordamchingizni graf yoʻliga undaydi.
- **Koʻrsatma fayli platformalari** (Codex, OpenCode, Cursor va boshqalar): doimiy koʻrsatma fayllari (`AGENTS.md`, `.cursor/rules/` va h.k.) xuddi shunday "avval soʻrov" yoʻriqnomasini beradi.

Keng arxitektura tahlili uchun `GRAPH_REPORT.md` hamon mavjud.

**CodeBuddy** Claude Code bilan bir xil ikki ishni qiladi: CodeBuddy'ga arxitektura savollariga javob berishdan oldin `graphify-out/GRAPH_REPORT.md` ni oʻqishni aytadigan `CODEBUDDY.md` boʻlimini yozadi va Bash qidiruv buyruqlari hamda fayl oʻqishlaridan oldin ishga tushib `graphify query` tomon undaydigan `PreToolUse` hook'larini (`.codebuddy/settings.json`) oʻrnatadi.

**Codex** `AGENTS.md` ga yozadi va bu platformada doimiy graf yoʻriqnomasini aynan shu fayl olib yuradi. `graphify codex install` shuningdek `.codex/hooks.json` da `PreToolUse` hook'ini (`graphify hook-check`) roʻyxatdan oʻtkazadi, lekin bu yozuv ataylab **no-op**: Codex Desktop `PreToolUse` da `hookSpecificOutput.additionalContext` ni rad etadi, shuning uchun u yerda undash chiqarish Bash vosita chaqiruvlarini buzardi. Claude Code'dan farqli oʻlaroq — u yerda undashni hook (`graphify hook-guard`) bajaradi — Codex'da hook ishga tushadi va ataylab hech nima qilmaydi, doimiy mexanizm esa `AGENTS.md`.

**Kilo Code** Graphify skill'ini `~/.config/kilo/skills/graphify/SKILL.md` ga va native `/graphify` buyrugʻini `~/.config/kilo/command/graphify.md` ga oʻrnatadi. `graphify kilo install` shuningdek `AGENTS.md` ni hamda native `tool.execute.before` plaginini (`.kilo/plugins/graphify.js` + `.kilo/kilo.json` yoki `.kilo/kilo.jsonc` roʻyxatga olish) yozadi, shunda Kilo native `.kilo` konfiguratsiyasi orqali oʻsha doimiy graf eslatmasi xatti-harakatini oladi.

**Cursor** `.cursor/rules/graphify.mdc` faylini `alwaysApply: true` bilan yozadi, shuning uchun Cursor uni har bir suhbatga avtomatik qoʻshadi, hook kerak emas.

graphify'ni barcha platformalardan bir vaqtda olib tashlash uchun: `graphify uninstall` (`graphify-out/` ni ham oʻchirish uchun `--purge` qoʻshing). Yoki platformaga xos buyruqdan foydalaning (masalan, `graphify claude uninstall`).

---

## Hisobotda nima bor

- **God tugunlar** — loyihangizdagi eng koʻp bogʻlangan tushunchalar. Hamma narsa ular orqali oqadi.
- **Kutilmagan bogʻlanishlar** — turli fayl yoki modullarda yashaydigan narsalar orasidagi bogʻlanishlar. Qanchalik kutilmaganligiga qarab tartiblangan.
- **"Nega" savoli** — inline izohlar (`# NOTE:`, `# WHY:`, `# HACK:`), docstring'lar va hujjatlardagi dizayn asoslari alohida tugunlar sifatida ajratilib, ular tushuntirayotgan kodga bogʻlanadi.
- **Taklif qilingan savollar** — graf ayniqsa yaxshi javob bera oladigan 4–5 savol.
- **Ishonch belgilari** — har bir xulosa qilingan munosabat `EXTRACTED`, `INFERRED` yoki `AMBIGUOUS` deb belgilanadi. Nima topilgani va nima taxmin qilingani doim ma'lum.

---

## Qanday fayllar bilan ishlaydi

| Turi | Kengaytmalar |
|------|-----------|
| Kod (36 ta tree-sitter grammatikasi) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme` uchun `uv tool install graphifyy[dm]` kerak; `.mts`/`.cts` TypeScript grammatikasidan, `.cc`/`.cxx` hamda CUDA `.cu`/`.cuh` va Metal `.metal` esa C++ grammatikasidan foydalanadi) |
| Salesforce Apex | `.cls .trigger` (regex asosida; klasslar, interfeyslar, enum'lar, metodlar, trigger'lar, SOQL/DML qirralari) |
| Terraform / HCL | `.tf .tfvars .hcl` (`uv tool install graphifyy[terraform]` kerak) |
| MCP konfiguratsiyalari | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — server tugunlari, paket havolalari, muhit oʻzgaruvchilari talablarini ajratadi |
| Paket manifestlari | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — har bir paket uchun bitta kanonik paket tuguni (nom boʻyicha) va `depends_on` qirralari, shuning uchun koʻp manifestdan havola qilingan paket bitta markaz boʻladi |
| Hujjatlar | `.md .mdx .qmd .html .txt .rst .yaml .yml` (markdown `[text](./other.md)` havolalari va `[[wikilinks]]` hujjatlar orasida `references` qirralariga aylanadi) |
| Office | `.docx .xlsx` (`uv tool install graphifyy[office]` kerak) |
| Google Workspace | `.gdoc .gsheet .gslides` (ixtiyoriy; `gws` autentifikatsiyasi va `--google-workspace` kerak; Sheets uchun `uv tool install graphifyy[google]` kerak) |
| PDF'lar | `.pdf` |
| Rasmlar | `.png .jpg .webp .gif` |
| Video / Audio | `.mp4 .mov .mp3 .wav` va boshqalar (`uv tool install graphifyy[video]` kerak) |
| YouTube / URL'lar | istalgan video URL (`uv tool install graphifyy[video]` kerak) |

Kod **API chaqiruvlarisiz lokal** ajratiladi (tree-sitter orqali AST). Qolgan hamma narsa AI yordamchingizning model API'si orqali oʻtadi.

Google Drive for desktop'ning `.gdoc`, `.gsheet` va `.gslides` fayllari hujjat mazmuni emas,
yorliq koʻrsatkichlaridir. Headless ajratishga native Google Docs, Sheets va Slides'ni
qoʻshish uchun [`gws` CLI](https://github.com/googleworkspace/cli) ni oʻrnating va
autentifikatsiyadan oʻting, soʻngra bajaring:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

Shuningdek `GRAPHIFY_GOOGLE_WORKSPACE=1` ni ham sozlashingiz mumkin. Graphify yorliqlarni
`graphify-out/converted/` ichiga Markdown sidecar fayllari sifatida eksport qiladi va soʻngra oʻsha fayllarni ajratadi.

---

## Keng tarqalgan buyruqlar

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

Yuqoridagi [Decouple: xavf bahosi bilan Extract-Class nomzodlari](#decouple-xavf-bahosi-bilan-extract-class-nomzodlari) boʻlimiga yoki quyidagi [buyruqlarning batafsil tavsifiga](#buyruqlarning-batafsil-tavsifi) qarang.

---

## Fayllarni e'tiborsiz qoldirish

Loyiha ildizida `.graphifyignore` yarating — sintaksis `.gitignore` bilan bir xil, `!` inkori ham qoʻllab-quvvatlanadi.

**`.gitignore` avtomatik hisobga olinadi.** graphify har bir katalogdagi `.gitignore` ni oʻqiydi. Agar `.graphifyignore` ham mavjud boʻlsa, ikkalasi **birlashtiriladi** — `.graphifyignore` shablonlari oxirida baholanadi, shuning uchun ziddiyatlarda ular gʻolib chiqadi (`!` inkorlari ham). `.graphifyignore` qoʻshish faqat qoʻshimcha fayllarni chiqarib tashlaydi; u `.gitignore` allaqachon chiqarib tashlagan faylni hech qachon qaytarmaydi. Quyi kataloglar qamrovi git'dagidek ishlaydi — ignore fayli faqat oʻz quyi daraxtiga ta'sir qiladi.

git tomonidan e'tiborsiz qoldirilgan generatsiya qilingan yoki transpilyatsiya qilingan kod grafga kirishi kerak boʻlsa, `graphify extract` ga `--no-gitignore` uzating. Bu `.gitignore` va `.git/info/exclude` ni oʻchiradi; `.graphifyignore` esa amal qilishda davom etadi.

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

## Jamoa uchun sozlash

`graphify-out/` git'ga commit qilish uchun moʻljallangan, shunda jamoadagi har bir kishi tayyor xarita bilan boshlaydi.

**`.gitignore` ga tavsiya etilgan qoʻshimchalar:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` endi koʻchma — kalitlar nisbiy yoʻllar sifatida saqlanadi va yuklashda qayta bogʻlanadi, shuning uchun uni commit qilish xavfsiz va birinchi checkout'da toʻliq qayta qurishning oldini oladi.

**Ish jarayoni:**
1. Bir kishi `/graphify .` ni bajaradi va `graphify-out/` ni commit qiladi.
2. Qolganlar pull qiladi — ularning yordamchisi grafni darhol oʻqiydi.
3. Har bir commit'dan keyin avtomatik qayta qurish uchun `graphify hook install` ni bajaring (faqat AST, API xarajati yoʻq). Bu shuningdek git merge driver'ini sozlaydi, shunda `graph.json` hech qachon konflikt belgilari bilan qolmaydi — parallel commit qilgan ikki dasturchining graflari avtomatik ravishda birlashtiriladi.
4. Hujjatlar yoki maqolalar oʻzgarsa, oʻsha tugunlarni yangilash uchun `/graphify --update` ni bajaring.

---

## Grafdan bevosita foydalanish

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

MCP serveri yordamchingizga tuzilmali kirish beradi: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Umumiy HTTP server

`--transport stdio` (standart) har bir dasturchi uchun bitta lokal server ishga tushiradi. `--transport http` xuddi shu vositalarni MCP Streamable HTTP transporti orqali xizmat qiladi, shunda bitta umumiy jarayon butun jamoa uchun grafni taqdim eta oladi — mijozlar graphify'ni lokal ishlatish oʻrniga IDE MCP konfiguratsiyasini `http://<host>:8080/mcp` ga yoʻnaltiradi.

| Bayroq | Standart | Maqsad |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Xizmat koʻrsatiladigan transport |
| `--host` | `127.0.0.1` | HTTP bind host (localhost'dan tashqariga ochish uchun `0.0.0.0` ishlating) |
| `--port` | `8080` | HTTP bind porti |
| `--api-key` | muhit `GRAPHIFY_API_KEY` | `Authorization: Bearer <key>` (yoki `X-API-Key`) talab qiladi |
| `--path` | `/mcp` | HTTP mount yoʻli |
| `--json-response` | oʻchiq | SSE oqimlari oʻrniga oddiy JSON qaytaradi |
| `--stateless` | oʻchiq | Seans holati yoʻq (yuk balanslangan / CI joylashtirishlar uchun) |
| `--session-timeout` | `3600` | Boʻsh turgan holatli seanslarni N soniyadan keyin tozalaydi (`0` oʻchiradi) |

Standart `127.0.0.1` bind faqat loopback uchun. Umumiy hostda ochayotganda `--host 0.0.0.0` **va** `--api-key` ni birga qoʻying. Uni konteynerda ishga tushiring:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **WSL / Linux haqida eslatma:** Ubuntu `python` emas, `python3` bilan keladi. Ziddiyatlardan qochish uchun venv ishlating:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## Muhit oʻzgaruvchilari

Bular faqat **headless / CI ajratish** (`graphify extract`) uchun kerak. IDE ichida `/graphify` skill'i orqali ishlatganda model API'sini IDE seansingiz taqdim etadi — qoʻshimcha kalitlar kerak emas.

| Oʻzgaruvchi | Nima uchun | Qachon kerak |
|---|---|---|
| `ANTHROPIC_API_KEY` | Claude (Anthropic) backend'i | `--backend claude` |
| `ANTHROPIC_BASE_URL` | Anthropic'ga mos endpoint URL (LiteLLM proxy, gateway'lar, ...) | `--backend claude` (standart: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Claude backend'i uchun model nomi — maxsus endpoint'larda serveringiz taqdim etgan model nomi/aliasidan foydalaning | `--backend claude` (standart: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` yoki `GOOGLE_API_KEY` | Google Gemini backend'i | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI yoki OpenAI'ga mos API'lar | `--backend openai` (lokal serverlar boʻsh boʻlmagan istalgan qiymatni qabul qiladi) |
| `OPENAI_BASE_URL` | OpenAI'ga mos server URL (llama.cpp, vLLM, LM Studio, ...) | `--backend openai` (standart: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | OpenAI backend'i uchun model nomi — oʻzingiz joylashtirgan serverlarda serveringiz taqdim etgan model nomi/aliasidan foydalaning (uning `/v1/models` endpoint'ini tekshiring), masalan llama.cpp uchun `LFM2.5-8B-A1B-UD-Q4_K_XL` | `--backend openai` (standart: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | DeepSeek backend'i | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Kimi Code backend'i | `--backend kimi` |
| `OLLAMA_BASE_URL` | Ollama lokal inferensiya URL'i | `--backend ollama` (standart: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Ollama model nomi | `--backend ollama` (standart: avtomatik aniqlash) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Ollama KV-kesh oynasi hajmini bekor qiladi | ixtiyoriy — standart holda avtomatik oʻlchamlanadi |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Ollama modelini yuklangan holda ushlab turish daqiqalari | ixtiyoriy — har bir chunk'dan keyin tushirish uchun `0` qoʻying |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI Service backend'i | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | Azure resurs endpoint URL'i | `--backend azure` (API kaliti bilan birga talab qilinadi) |
| `AZURE_OPENAI_API_VERSION` | Azure API versiyasini bekor qilish | ixtiyoriy — standart `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` yoki `GRAPHIFY_AZURE_MODEL` | Azure deployment nomi | ixtiyoriy — standart `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — standart credential zanjiri | `--backend bedrock` (API kaliti yoʻq, IAM ishlatadi) |
| `GRAPHIFY_MAX_WORKERS` | AST parallelizmi uchun oqimlar soni | ixtiyoriy — `--max-workers` bayrogʻi ham bor |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Zich korpuslar uchun chiqish chegarasini koʻtarish | ixtiyoriy — masalan, katta fayllar uchun `32768` |
| `GRAPHIFY_API_TIMEOUT` | HTTP, claude-cli, Anthropic SDK va Bedrock backend'lari uchun har bir chaqiruv taymauti (soniyada, standart: 600) | ixtiyoriy — `--api-timeout` bayrogʻi ham bor |
| `GRAPHIFY_MAX_RETRIES` | Rate-limit (429) boʻlgan soʻrov necha marta qayta urinilishi (standart: 6; `Retry-After` hisobga olinadi) | ixtiyoriy — qat'iy tashkilot limitlarida oshiring (masalan, kimi); `0` oʻchiradi |
| `GRAPHIFY_FORCE` | Tugunlar kamaygan boʻlsa ham grafni qayta qurishga majbur qiladi | ixtiyoriy — `--force` bayrogʻi ham bor |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Google Workspace eksportini avtomatik yoqadi | ixtiyoriy — `1` qiling |
| `GRAPHIFY_TRIAGE_BACKEND` | `graphify prs --triage` uchun backend | ixtiyoriy — mavjud kalitlardan avtomatik aniqlanadi |
| `GRAPHIFY_TRIAGE_MODEL` | Triage uchun model almashtirish | ixtiyoriy — masalan `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | `~/.cache/graphify-queries.log` dagi lokal soʻrov jurnalini yoqish uchun `1` qiling (har bir query/path/explain savoli + korpus yoʻlini yozadi). Standart holda oʻchiq — siz yoqmaguningizcha hech narsa yozilmaydi (#1797) | ixtiyoriy |
| `GRAPHIFY_QUERY_LOG` | Soʻrov jurnalini yoqadi va uni standart yoʻl oʻrniga shu yoʻlga yozadi | ixtiyoriy — bu yoki `_ENABLE` qoʻyilmaguncha oʻchiq |
| `GRAPHIFY_QUERY_LOG_DISABLE` | Soʻrov jurnalini majburan oʻchirish uchun `1` qiling (yoqish oʻzgaruvchilaridan ustun) | ixtiyoriy |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | Jurnal yoqilganda toʻliq qism-graf javoblarini ham yozadi (standart holda oʻchiq) | ixtiyoriy |
| `GRAPHIFY_MAX_GRAPH_BYTES` | graph.json uchun 512 MiB hajm chegarasini bekor qiladi — masalan `700MB`, `2GB` yoki oddiy baytlar | ixtiyoriy — juda katta korpuslar uchun foydali |
| `GRAPHIFY_MAX_CONTEXTS` | Bitta koʻp loyihali MCP server saqlaydigan standart boʻlmagan loyiha graflarining maksimal soni | ixtiyoriy — standart: `8`; notoʻgʻri qiymatlarda `8`, `1` dan kichik qiymatlarda `1` ishlatiladi |
| `GRAPHIFY_LLM_TEMPERATURE` | Semantik ajratish uchun LLM temperaturasini bekor qiladi — masalan `0.7` yoki tashlab yuborish uchun `none` | ixtiyoriy — o1/o3/o4/gpt-5 reasoning modellarida avtomatik tashlanadi |

---

## Maxfiylik

- **Kod fayllari** — lokal tarzda tree-sitter orqali qayta ishlanadi. Hech narsa kompyuteringizdan chiqmaydi. Faqat koddan iborat korpus uchun API kaliti kerak emas — `graphify extract` toʻliq oflayn ishlaydi. Aralash repozitoriyda faqat kodni indekslash va aks holda LLM talab qiladigan hujjatlar/PDF'lar/rasmlarni oʻtkazib yuborish uchun `--code-only` qoʻshing.
- **Video / audio** — faster-whisper bilan lokal transkripsiya qilinadi. Hech narsa kompyuteringizdan chiqmaydi.
- **Hujjatlar, PDF'lar, rasmlar** — semantik ajratish uchun AI yordamchingizga yuboriladi (`/graphify` skill'i orqali, IDE seansingiz ishlatayotgan modeldan foydalanib). Headless `graphify extract` uchun `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), ishlab turgan Ollama nusxasi (`OLLAMA_BASE_URL`), standart provayder zanjiri orqali AWS hisob ma'lumotlari (Bedrock — API kaliti kerak emas, IAM ishlatadi) yoki `claude` CLI binari (Claude Code — API kaliti kerak emas, Claude obunangizdan foydalanadi) talab qilinadi. `--dedup-llm` bayrogʻi ham shu kalitdan foydalanadi.
- **Ma'lumot rezidentligi** — `graphify extract` qaysi API kaliti qoʻyilganiga qarab qaysi provayderni ishlatishni avtomatik aniqlaydi (ustuvorlik: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). Ma'lumot rezidentligi talablari boʻlgan kod uchun `--backend ollama` (toʻliq lokal) ni ishlating yoki aniq `--backend` bayrogʻini uzating. Kimi (`MOONSHOT_API_KEY`) Xitoydagi Moonshot AI serverlariga yoʻnaltiradi.
- **Telemetriya yoʻq**, foydalanishni kuzatish yoʻq, analitika yoʻq.
- **Soʻrov jurnali** — har bir `graphify query`, `graphify path`, `graphify explain` va MCP `query_graph` chaqiruvi `~/.cache/graphify-queries.log` fayliga JSON Lines formatida yoziladi (vaqt belgisi, savol, korpus, qaytarilgan tugunlar, davomiylik). Toʻliq qism-graf javoblari standart holda saqlan**maydi**. Voz kechish uchun `GRAPHIFY_QUERY_LOG_DISABLE=1` ni qoʻying yoki kod yoʻlini oʻchirmasdan jimlantirish uchun `GRAPHIFY_QUERY_LOG=/dev/null` ni ishlating.

---

## Nosozliklarni bartaraf etish

**Oʻrnatgandan keyin `graphify: command not found`**
CLI oʻrnatilgan, lekin uning bin katalogi shell'ingizning `PATH` ida yoʻq. Qanday oʻrnatganingizga mos yechimni tanlang:
- **uv** (`uv tool install graphifyy`): buyruq uv'ning vosita bin katalogiga (`~/.local/bin`) tushadi, u yangi macOS/zsh sozlamalarida koʻpincha `PATH` da boʻlmaydi. `uv tool update-shell` ni bajaring, soʻngra yangi terminal oching. (Katalogni `uv tool dir --bin` bilan toping.)
- **pipx** (`pipx install graphifyy`): `pipx ensurepath` ni bajaring, soʻngra yangi terminal oching.
- **pip** (`pip install graphifyy`): pip skriptlarni `PATH` da boʻlmasligi mumkin boʻlgan foydalanuvchi bin katalogiga oʻrnatadi — `~/.zshrc`/`~/.bashrc` da `PATH` ga `~/Library/Python/3.x/bin` (macOS) yoki `~/.local/bin` (Linux) ni qoʻshing yoki shunchaki `python -m graphify` ni ishga tushiring.

**`uvx graphify …` yoki `uv tool run graphify …` `graphify` ni aniqlay olmayapti**
PyPI paketi `graphifyy` deb ataladi; `graphify` — bu u taqdim etadigan buyruq, xolos. `uv tool run` birinchi soʻzni *paket nomi* deb qabul qiladi, shuning uchun `graphify` nomli paketni qidiradi va `No solution found … no versions of graphify` deb xabar beradi. Paketni aniq koʻrsating: `uvx --from graphifyy graphify install` (`uv tool run --from graphifyy graphify install` bilan bir xil). Yoki bir marta `uv tool install graphifyy` ni bajaring va keyin `graphify` ni bevosita chaqiring.

**`uv run --with graphifyy python -m graphify` jimgina eski oʻrnatilgan nusxani ishga tushiryapti**
`uv run` sizning *tizim* Python'ingizni ishlatadi, shuning uchun u yerda eski `graphifyy` ham yashasa (masalan, oldingi `pip install graphifyy` dan), Python `sys.path` da avval oʻsha nusxani topishi mumkin va `--with graphifyy` uni bekor qilmaydi. Xatosiz ishlaydi, lekin siz *eski* versiya xatti-harakatini olasiz — masalan, `OPENAI_BASE_URL` kabi muhit almashtirishlari jimgina e'tiborsiz qoldiriladi, natijada soʻrovlar standart endpoint'ga boradi va notoʻgʻri kalitga oʻxshab koʻrinadigan 401 bilan yiqiladi. Belgisi — `warning: skill is from graphify <newer>, package is <older>` qatori; bu shunchaki eskirgan skill emas, boshqa oʻrnatma yuklanganini bildiradi. Qaysi nusxa haqiqatan yuklanganini tekshiring:
```bash
python -c "import graphify; print(graphify.__file__)"
```
Soʻngra oʻrnatilgan buyruqni bevosita ishga tushiring (u uv boshqaradigan nusxadan foydalanadi) yoki eskirgan tizim nusxasini oʻchiring:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` ishlaydi, lekin `graphify` buyrugʻi ishlamaydi**
Shell'ingizning `PATH` i buyruq oʻrnatilgan bin katalogini oʻz ichiga olmaydi. Oddiy `pip` oʻrniga `uv tool install` / `pipx install` ni afzal koʻring, soʻngra `uv tool update-shell` / `pipx ensurepath` ni bajaring va yangi terminal oching (yuqoridagi oʻrnatish eslatmalariga qarang).

**PowerShell'da `/graphify .` "path not recognized" xatosini beradi**
PowerShell boshidagi `/` ni yoʻl ajratuvchisi deb qabul qiladi. Windows'da `graphify .` (slashsiz) ishlating.

**`--update` yoki qayta qurishdan keyin grafda tugunlar kamaydi**
Agar refactoring fayllarni oʻchirgan boʻlsa, eski tugunlar qolib ketadi. Qayta qurishda tugunlar kamaygan boʻlsa ham qayta yozish uchun `--force` ni uzating (yoki `GRAPHIFY_FORCE=1` ni qoʻying).

**`extract` "extraction was incomplete ... refusing to overwrite" bilan chiqib ketmoqda**
Ajratish bosqichi qulasa yoki korpusni toʻliq oʻqib boʻlmasa, natija toʻliq ishga qaraganda kichikroq boʻlardi, shuning uchun `graphify extract` mavjud kattaroq grafni qisman natija bilan qayta yozishdan bosh tortadi (bu `graph.json` ingizni himoya qiladi). Asosiy nosozlikni tuzatib qayta ishga tushiring yoki baribir qayta yozish uchun `--allow-partial` ni uzating.

**Grafda bir xil obyekt uchun takroriy tugunlar bor (ghost dublikatlar)**
Ghost dublikatlar (bir xil belgi ikki marta paydo boʻladi — biri manba joyi bilan AST ajratishdan, biri joysiz semantik ajratishdan) endi qurish vaqtida avtomatik birlashtiriladi. Buni v0.8.33 dan oldin qurilgan grafda koʻrsangiz, tozalash uchun toʻliq qayta ajratish qiling:
```bash
graphify extract . --force
```

**Ollama VRAM'i tugayapti / kontekst oynasi oshib ketdi**
KV-kesh oynasi avtomatik oʻlchamlanadi, lekin GPU'ngiz uchun juda katta boʻlishi mumkin. Uni kichraytiring:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**`LLM returned invalid JSON` / `Unterminated string` ogohlantirishlari**
Modelning JSON javobi chiqish token chegarasiga yetib, satr oʻrtasida kesilgan. graphify avtomatik tiklanadi (chunk'ni boʻlib, yarmlarini qayta ajratadi, juda katta bitta hujjat esa avval sarlavha/paragraf chegaralarida kesiladi, shunda butun fayl baribir qamrab olinadi), shuning uchun bu ogohlantirishlar shovqinli, lekin ma'lumot yoʻqolmaydi. Bunday holatlarni kamaytirish uchun chiqish chegarasini koʻtaring yoki har bir chunk chiqishini kichraytiring:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
OpenRouter kabi bulut gateway bilan Ollama shim'i oʻrniga `--backend openai` ni afzal koʻring (`OPENAI_BASE_URL` ni qoʻying) — bu tozaroq, OpenAI'ga mos yoʻl. Modelning oʻz maksimal chiqish chegarasi boʻlsa, `--token-budget` ni pasaytirish ishonchli richag hisoblanadi.

**Graf HTML'i brauzerda ochish uchun juda katta (>5000 tugun)**
HTML generatsiyasini oʻtkazib yuboring va bevosita JSON'dan foydalaning:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**Ikki dasturchi bir vaqtda commit qilgandan keyin `graph.json` da konflikt belgilari paydo boʻldi**
`graphify hook install` ni bajaring — u `graph.json` ni avtomatik birlashtiradigan git merge driver'ini sozlaydi, shunda konfliktlar umuman yuz bermaydi.

**Hujjatlar yoki PDF'lar uchun ajratish boʻsh tugun/qirralarni qaytarmoqda**
Hujjatlar, PDF'lar va rasmlar LLM chaqiruvini talab qiladi — faqat koddan iborat korpuslarga kalit kerak emas. API kalitingiz qoʻyilganini va backend toʻgʻriligini tekshiring:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**IDE'ingizda skill versiyasi mos kelmasligi haqida ogohlantirish**
Oʻrnatilgan graphify versiyangiz skill faylidan farq qiladi. Yangilang:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**Har bir `graphify extract` dan keyin Claude Code prompt keshi bekor qilinmoqda**
Graphify chiqish fayllarini (`graph.json`, `graphify-out/`) ish maydoniga yozadi. Agar bu yoʻllar e'tiborsiz qoldirilmagan boʻlsa, har bir yozish Claude Code prompt keshini bekor qiladi va keyingi qadamda kesh-yozish narxlarida toʻliq qayta yuklashga majbur qiladi. Ularni `.claudeignore` ga qoʻshing:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## Buyruqlarning batafsil tavsifi

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

> **Hamjamiyat nomlari:** agent ichida (Claude Code, Gemini CLI) hamjamiyatlarni agentning oʻzi nomlaydi. Toza CLI'ni ishlatganingizda `cluster-only` ularni sozlangan backend (ichki yoki maxsus OpenAI'ga mos provayder) bilan avtomatik nomlaydi — `Community N` ni saqlab qolish uchun `--no-label` ni uzating yoki nomlarni talab boʻyicha (qayta) yaratish uchun `graphify label` ni ishga tushiring.

---

## Batafsil ma'lumot

- [Qanday ishlaydi](../how-it-works.md) — ajratish quvuri, hamjamiyat aniqlash, ishonch bahosi, benchmark'lar
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — modullar taqsimoti, til qanday qoʻshiladi
- [Ixtiyoriy integratsiyalar](../docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — graphify ortidagi gʻoyalar va arxitektura haqidagi kitob

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) — bu graphify ustiga qurilgan doimiy ishlaydigan qatlam; u xuddi shu graf yondashuvini butun ish kontekstingizga qoʻllaydi: uchrashuvlar, fayllar, hujjatlar va kod, fonda uzluksiz yangilanib turadi.

Ishi yuzlab suhbatlar va hujjatlar boʻylab tarqalgan, ularni hech qachon toʻliq tiklay olmaydigan odamlar va jamoalar uchun qurilgan.

**[graphify.com'da navbat roʻyxatiga qoʻshiling](https://graphify.com).** Bepul sinov muddati tez orada boshlanadi.

---

<details>
<summary>Hissa qoʻshish</summary>

### Ishlab chiqish muhitini sozlash

Loyiha ishlab chiqish jarayoni uchun [uv](https://docs.astral.sh/uv/) dan foydalanadi. Uni bir marta oʻrnating, soʻngra:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

Editable oʻrnatishni tekshiring:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### Testlarni ishga tushirish

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> macOS haqida eslatma: test toʻplamida `sample.f90` va `sample.F90` fixture'larining ikkalasi ham bor. Ular registrga sezgir boʻlmagan HFS+ / APFS fayl tizimlarida toʻqnashadi. Ikkala Fortran variantini bir vaqtda test qilish kerak boʻlsa, Linux'da yoki Docker konteynerida ishga tushiring.

### Git ish jarayoni

- Faol ishlab chiqish `v8` branch'ida boradi.
- Commit uslubi: `fix: <description>` / `feat: <description>` / `docs: <description>`
- PR ochishdan oldin `uv run pytest tests/ -q` ni bajaring va u muvaffaqiyatli oʻtishiga ishonch hosil qiling.
- Har qanday yangi til ajratuvchisi uchun `tests/fixtures/` ga fixture fayl va `tests/test_languages.py` ga testlar qoʻshing.

### Nimaga hissa qoʻshish mumkin

**Ishlab chiqilgan misollar** eng foydali hissadir. `/graphify` ni haqiqiy korpusda ishga tushiring, natijani `worked/{slug}/` ga saqlang, graf nimani toʻgʻri va nimani notoʻgʻri qilganini ochiq yozadigan `review.md` tayyorlang va PR oching.

**Ajratish xatolari** — kirish fayli, kesh yozuvi (`graphify-out/cache/`) va nima oʻtkazib yuborilgani yoki notoʻgʻri boʻlgani bilan issue oching.

Modullar mas'uliyati va til qoʻshish tartibi uchun [ARCHITECTURE.md](../../ARCHITECTURE.md) ga qarang.

</details>
