<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>ฟอร์กจาก <a href="https://github.com/Graphify-Labs/graphify">graphify</a> ที่เพิ่ม <code>graphify decouple</code></b> — ผู้สมัคร Extract-Class ที่ให้คะแนนความเสี่ยงสำหรับ god object โดยไม่ใช้ LLM ตรวจสอบซ้ำกับซอร์สโค้ดจริง (ไม่ใช่แค่ call graph) ก่อนที่จะแนะนำอะไรก็ตาม ดู <a href="#decouple-risk-scored-extract-class-candidates">Decouple: ผู้สมัคร Extract-Class ที่ให้คะแนนความเสี่ยง</a> ด้านล่าง
</p>

<div align="center">
<details><summary><b>อ่านเป็นภาษาอื่น</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>เปิดให้เข้าถึงแพลตฟอร์ม graphify ล่วงหน้าก่อนเปิดตัว v1 อย่างเป็นทางการ: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

พิมพ์ `/graphify` ในผู้ช่วยเขียนโค้ด AI ของคุณ แล้วมันจะแมปทั้งโปรเจกต์ของคุณ (โค้ด เอกสาร PDF รูปภาพ วิดีโอ) ให้เป็น **knowledge graph** ที่คุณ **คิวรีได้แทนการ grep** ผ่านไฟล์ต่างๆ

- **แมปโค้ดฟรี ทำงานในเครื่องทั้งหมด** โค้ดถูกพาร์สด้วย tree-sitter AST: กำหนดแน่นอน ไม่ใช้ LLM ไม่มีอะไรออกจากเครื่องคุณ (เอกสาร PDF รูปภาพ และวิดีโอ ใช้โมเดลของผู้ช่วยคุณ หรือ API key ที่ตั้งค่าไว้ สำหรับการวิเคราะห์เชิงความหมาย)
- **ทุกเส้นเชื่อม (edge) มีคำอธิบาย** การเชื่อมโยงแต่ละอันจะถูกแท็กเป็น `EXTRACTED` (ระบุชัดเจนในซอร์ส) หรือ `INFERRED` (สรุปโดย graphify) เพื่อให้คุณบอกได้ว่าอะไรอ่านมาโดยตรงและอะไรเป็นการอนุมาน
- **ไม่ใช่ vector index** ไม่มี embeddings ไม่มี vector store: เป็นกราฟจริงที่คุณเดินสำรวจได้ ถามคำถาม ตามหาเส้นทางระหว่างสองสิ่ง หรือขออธิบายแนวคิดหนึ่งเดียว

> ต้องการให้สิ่งนี้ทำงานตลอดเวลา อัปเดตในพื้นหลังตลอดโค้ด เอกสาร และการประชุมของคุณ แทนที่จะทำตามคำสั่งเท่านั้นหรือไม่? นั่นคือสิ่งที่เรากำลังสร้างที่ **[graphify.com](https://graphify.com)** และตอนนี้เปิดให้เข้าถึงล่วงหน้าแล้วที่ **[app.graphify.com](https://app.graphify.com/login)**

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="graphify's interactive graph.html showing the FastAPI codebase as a force-directed knowledge graph with a legend of detected communities" width="900">
</p>
<p align="center">
  <em>โค้ดเบส FastAPI ที่ถูกแมปโดย graphify แต่ละโหนดคือแนวคิดหนึ่ง สีคือชุมชนที่ตรวจพบ และทั้งหมดคลิกได้ใน graph.html</em>
</p>

**เริ่มต้นใช้งาน** (30 วินาที):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

จากนั้น ในผู้ช่วย AI ของคุณ:

```
/graphify .
```

แค่นั้นเอง คุณจะได้ **สามไฟล์**:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**ใช้งานได้ใน** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot และอีกกว่า 15 แพลตฟอร์ม — [เลือกแพลตฟอร์มของคุณ](#install)

---

## ดูมันทำงานจริง

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="graphify path query: a terminal asks for the shortest path between FastAPI and ModelField, and the answer lights up hop by hop across the knowledge graph" width="900">
</p>

เมื่อสร้างกราฟแล้ว คุณจะคิวรีมันแทนการอ่านไฟล์ นี่คือผลลัพธ์จริง จาก graphify ที่รันบนโค้ดเบส FastAPI ที่แสดงด้านบน:

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

ทุกเส้นเชื่อมมี **แท็กความเชื่อมั่น** (`EXTRACTED` = ชัดเจนในซอร์ส, `INFERRED` = ได้มาจากการแก้ไขปัญหาความสัมพันธ์) เพื่อให้คุณบอกได้ว่าอะไรอ่านมาโดยตรงและอะไรเป็นการอนุมาน `graphify query "<question>"` จะคืนซับกราฟที่จำกัดขอบเขตสำหรับคำถามภาษาธรรมดา และ `graphify path A B` จะตามหาว่าสองสิ่งเชื่อมโยงกันอย่างไร

---

## Decouple: ผู้สมัคร Extract-Class ที่ให้คะแนนความเสี่ยง

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: MainWindow god node splitting into risk-scored candidate classes, with a shared-state warning between two of them" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: MainWindow's 5 proposed classes, Node Info panel open on Main Window Axis and Range Controls showing a 0.608 state overlap with Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>DECOUPLE.html จากการรันจริง — คลิกคลาสที่เสนอไว้ จะเห็นทันทีว่ามันแชร์สถานะกับคลาสอื่นตัวไหน และแชร์อะไรบ้างโดยเฉพาะ</em>
</p>

หน้าเดียวกันนี้ยังแสดงการแยกส่วนจริงด้วย การสลับ **Preview decoupled view** จะเปลี่ยนเมธอดของ god class เป็นคลาสที่เสนอไว้ และเดินสายเส้นเชื่อมใหม่ในตำแหน่งเดิม — คือการเปลี่ยนแปลงการเชื่อมโยง ไม่ใช่ไดอะแกรมที่วาดใหม่:

| ก่อน — god class ในปัจจุบัน | หลัง — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html before the toggle: a single MainWindow hub node with its own methods fanned out around it" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html after the toggle: the same node reduced to 5 diamond-shaped proposed classes, green dashed edges showing which methods were extracted into each, red edges showing shared instance state between two of them" width="440"> |
| โหนดเดียวที่มีเมธอดของตัวเอง 47 ตัว แต่ละตัวเข้าถึงได้ผ่านคลาสนี้เท่านั้น | คลาสที่เสนอไว้ เส้นประสีเขียว = อะไรถูกดึงเข้าไปในคลาสไหน; สีแดง = สถานะของ instance ที่คลาสสองตัวยังคงแชร์กัน ซึ่งเป็นตัวตัดสินใจว่าจะ `split` หรือ `keep_as_is` เฉพาะผู้สมัครที่ผ่านเกณฑ์ความเสี่ยงเท่านั้นที่จะถูกวาด — ในที่นี้คือ 5 จาก 6 ตัว นั่นคือเหตุผลที่หนึ่งเมธอดไม่มีเพชรให้ลงจอด |

`graphify decouple` ค้นหา god object และบอกว่าการแยกมันคุ้มค่าจริงหรือไม่ — ไม่ใช่แค่บอกว่ามันใหญ่

รูปแบบความล้มเหลวที่มันถูกออกแบบมาเพื่อจับคือ: คลาสที่มี 47 เมธอด ซึ่งการจัดกลุ่มด้วย call graph แยกออกเป็น 5 กลุ่มที่ดูเรียบร้อยได้อย่างง่ายดาย แต่ทั้งหมดยังคงอ่านและเขียนสถานะ instance เดียวกันคือ `self._chart_style` / `self._crosshair` อยู่ข้างใต้ ถ้าคุณส่งการแยกนั้นออกไป คุณยังไม่ได้ decouple อะไรเลย — คุณแค่ย้ายเมธอดไปยังไฟล์ใหม่ที่ยังไม่สามารถทดสอบ เปลี่ยนแปลง หรือทำความเข้าใจได้อย่างอิสระ เพราะทั้งหมดยังต้องการสถานะที่แชร์กันเดิมส่งกลับมา เครื่องมือที่มองแค่ call graph ไม่สามารถเห็นสิ่งนี้ได้เลย มันต้องย้อนกลับไปดูซอร์สจริง

**การตรวจสอบสองแบบ ทั้งคู่ไม่ใช้ LLM ทั้งคู่กำหนดแน่นอน:**

1. **นี่เป็น God Object จริงหรือไม่?** โหนดที่มี degree สูงอาจเป็น God Object จริง (เมธอดของตัวเองจำนวนมาก กระจายไปในความรับผิดชอบที่ไม่เกี่ยวข้องกัน — Extract Class ใช้ได้) หรืออาจเป็น hub/data model ที่ถูกอ้างอิงมากเกินไป (เมธอดของตัวเองน้อย ส่วนใหญ่เป็นการอ้างอิง *ขาเข้า* — การแยกตัวมันเองไม่ช่วยอะไร ทางแก้คือทำให้ interface แคบลง ไม่ใช่แยกคลาส) `classify_god_node` แยกแยะสิ่งเหล่านี้ด้วย `member_ratio` ไม่ใช่ degree ดิบ — ความแตกต่างนี้ป้องกันไม่ให้ `TraceSource` (84 เส้นเชื่อม แต่มีเพียง 6 เมธอดของตัวเอง) ได้รับข้อเสนอแยกที่ผิดพลาด ซึ่ง `MainWindow` (88 เส้นเชื่อม 47 เมธอดของตัวเอง) ได้รับอย่างถูกต้อง
2. **การแยกจะลด coupling จริงหรือไม่?** `risk_before` (ขนาด/coupling/การกระจัดกระจายปัจจุบันของ god node) ถูกเปรียบเทียบกับ `risk_after` — ความเสี่ยงใหม่ที่การแยกเองจะนำมา: การเรียกข้ามกลุ่มที่เคยเป็นเส้นเชื่อมภายในคลาสที่มองไม่เห็น กลายเป็นการพึ่งพาข้ามคลาสที่ชัดเจน ผู้เรียกที่ตอนนี้ต้องพึ่งพาคลาสใหม่มากกว่าหนึ่งตัว และ — การตรวจสอบที่ call graph ไม่สามารถทำได้ในเชิงโครงสร้าง — สถานะ instance `self`/`this` (การอ่าน การเขียน และการเรียกเมธอดช่วยที่แชร์กัน โดยให้น้ำหนักแยกกัน: การ**เขียน**ที่แชร์กันได้คะแนนสูงกว่าการอ่านที่แชร์กัน) ที่กลุ่มที่เสนอไว้มีร่วมกันจริงๆ มากแค่ไหน สิ่งนี้พาร์สไฟล์ซอร์สของ god node เองใหม่โดยตรงด้วย tree-sitter ไม่ได้พึ่งพากราฟที่ graphify ดึงออกมาเอง ซึ่งไม่เคยบันทึกการเข้าถึงระดับฟิลด์สำหรับภาษาใดๆ เลย เฉพาะเมื่อ `risk_after` ต่ำกว่าเกณฑ์ที่สัมพันธ์กับ `risk_before` เท่านั้นที่แผนจะแนะนำ `split` — ไม่เช่นนั้นจะเป็น `marginal` หรือ `keep_as_is` และผู้สมัครที่ไม่แนะนำจะถูกรายงานเป็นตัวเลข ไม่เคยถูกวาดเป็นรูปทรงที่คุณต้องเดาด้วยตา

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

สร้างสามไฟล์ข้าง `graph.json`:

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

**ความครอบคลุมภาษาสำหรับการตรวจสอบการแชร์สถานะ** (การจัดประเภทด้วย call-graph อย่างเดียวข้างต้นใช้ได้กับทุกภาษาที่ graphify ดึงข้อมูล; ตารางนี้กล่าวถึงเฉพาะการพาร์สซอร์สใหม่ที่ตรวจสอบการซ้อนทับของสถานะ `self`/`this`):

| ภาษา | รองรับ | หมายเหตุ |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` เป็นโหนด AST ของตัวเอง ไม่ใช่การเข้าถึงฟิลด์ที่ถูกห่อไว้ — จัดการอย่างชัดเจน |
| C# | ✅ | |
| Rust | ✅ | `self.x` ผ่านบล็อก `impl` |
| Ruby | ✅ | `@x` (สำนวนหลัก) + การเรียก `self.foo` |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | การแก้ไขตัวรับ (receiver) ต่อเมธอด — Go ไม่มีคีย์เวิร์ด `self`/`this` ดังนั้นชื่อตัวรับ (`f` ใน `func (f *Foo) M()`) จะถูกแก้ไขใหม่ทุกเมธอด |
| C | ❌ | พารามิเตอร์ตัวชี้ struct ไม่มีเครื่องหมายทางไวยากรณ์ที่แยกมันจากพารามิเตอร์อื่น — ไม่มีสัญญาณที่เชื่อถือได้หากไม่มีการอนุมานชนิดข้อมูลแบบเต็ม |

god node ในภาษาที่ไม่รองรับ หรือที่ซอร์สอ่านไม่ได้ จะถูกทำเครื่องหมายเป็น `state_analysis: "skipped"` — การจัดประเภทและคะแนน call graph ยังคงทำงาน แต่คำแนะนำจะยึดตาม call graph เพียงอย่างเดียว แทนที่จะสมมติเงียบๆ ว่าการตรวจสอบสถานะผ่านแล้ว

---

## มันทำอะไรได้บ้าง

สิ่งที่คุณได้รับทันที:

| ความสามารถ | สิ่งที่คุณได้รับ |
|---|---|
| **God node** | แนวคิดที่เชื่อมโยงมากที่สุด เพื่อให้คุณเห็นว่าทุกอย่างไหลผ่านอะไร |
| **ชุมชน (Communities)** | กราฟถูกแบ่งเป็นระบบย่อย (Leiden) พร้อมป้ายกำกับที่ไม่ใช้ LLM |
| **ลิงก์ข้ามไฟล์** | `calls` / `imports` / `inherits` / `mixes_in` ที่แก้ไขความสัมพันธ์แล้วในราว 40 ภาษา ผ่าน tree-sitter AST |
| **คิวรี เส้นทาง อธิบาย** | ถามคำถาม ตามหาเส้นทางระหว่างสองสิ่ง หรืออธิบายแนวคิดหนึ่งเดียว ทั้งหมดจาก `graph.json` |
| **เหตุผล + การอ้างอิงเอกสาร** | คอมเมนต์ `# NOTE:` / `# WHY:` และการอ้างอิง ADR/RFC กลายเป็นโหนดชั้นหนึ่งที่เชื่อมกับโค้ด |
| **นอกเหนือจากโค้ด** | เอกสาร PDF รูปภาพ และวิดีโอ/เสียง ทั้งหมดถูกแมปเข้าสู่กราฟเดียวกัน |
| **ทำงานในเครื่องก่อน** | โค้ดถูกพาร์สในเครื่องด้วย tree-sitter (ไม่ใช้ LLM ไม่มีอะไรออกจากเครื่องคุณ); เฉพาะการวิเคราะห์เชิงความหมายของเอกสาร/สื่อเท่านั้นที่เรียก backend และเรียกก็ต่อเมื่อคุณตั้งค่าไว้ |

---

## Benchmark

| Benchmark | ตัวชี้วัด | graphify | คู่แข่ง |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | ความแม่นยำ QA | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | ความแม่นยำ QA | **76%** | เสมอกับ dense RAG |
| การสร้างกราฟ | เครดิต LLM | **0** | ต่อ token สำหรับระบบส่วนใหญ่ |

ทุกระบบรันบน harness เดียวกัน โมเดลเดียวกัน และงบประมาณเดียวกัน ให้คะแนนโดยกรรมการที่ผ่านการตรวจสอบแบบ blind กับกรรมการที่สอง (ตรงกัน 90.6% Cohen's kappa 0.81) ตารางแบบละเอียดต่อระบบ ผลลัพธ์ code-intelligence และคำสั่งสำหรับทำซ้ำผลลัพธ์: **[BENCHMARKS.md](./BENCHMARKS.md)**

---

## ข้อกำหนดเบื้องต้น

| ข้อกำหนด | ขั้นต่ำ | ตรวจสอบ | ติดตั้ง |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(แนะนำ)* | เวอร์ชันใดก็ได้ | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(ทางเลือก)* | เวอร์ชันใดก็ได้ | `pipx --version` | `pip install pipx` |

**ติดตั้งด่วนบน macOS (Homebrew):**
```bash
brew install python@3.12 uv
```

**ติดตั้งด่วนบน Windows:**
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

## การติดตั้ง

> **แพ็กเกจอย่างเป็นทางการ:** แพ็กเกจ PyPI คือ `graphifyy` (มี y สองตัว) แพ็กเกจ `graphify*` อื่นๆ บน PyPI ไม่มีความเกี่ยวข้องกัน คำสั่ง CLI ยังคงเป็น `graphify`

**ขั้นตอนที่ 1 — ติดตั้งแพ็กเกจ:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**ขั้นตอนที่ 2 — ลงทะเบียน skill กับผู้ช่วย AI ของคุณ:**

```bash
graphify install
```

แค่นั้นเอง เปิดผู้ช่วย AI ของคุณและพิมพ์ `/graphify .`

หากต้องการติดตั้ง skill ของผู้ช่วยในรีโพซิทอรีปัจจุบันแทนโปรไฟล์ผู้ใช้ของคุณ ให้เพิ่ม `--project`:

```bash
graphify install --project
graphify install --project --platform codex
```

การติดตั้งแบบจำกัดขอบเขตโปรเจกต์จะเขียนไว้ในไดเรกทอรีปัจจุบัน เช่น `.claude/skills/graphify/SKILL.md` หรือ `.agents/skills/graphify/SKILL.md` (พร้อม sidecar `references/` ที่ skill โหลดตามต้องการ) และพิมพ์คำแนะนำ `git add` สำหรับไฟล์ที่สามารถ commit ได้ คำสั่งเฉพาะแพลตฟอร์มที่รองรับการติดตั้งแบบจำกัดขอบเขตโปรเจกต์จะรับแฟล็กเดียวกัน เช่น `graphify claude install --project` หรือ `graphify codex install --project`

> **หมายเหตุ PowerShell:** ใช้ `graphify .` ไม่ใช่ `/graphify .` — เครื่องหมายทับที่นำหน้าเป็นตัวแบ่งพาธใน PowerShell

> **`graphify: command not found`?** `uv tool install` / `pipx install` จะวางคำสั่ง `graphify` ไว้ในไดเรกทอรี bin ของเครื่องมือ (`~/.local/bin`) ถ้า shell ของคุณหาไม่เจอทันทีหลังติดตั้ง — พบบ่อยในการติดตั้ง macOS + zsh ใหม่ๆ — ไดเรกทอรีนั้นยังไม่อยู่ใน `PATH` ของคุณ: รัน `uv tool update-shell` (หรือ `pipx ensurepath`) แล้วเปิดเทอร์มินัลใหม่ ถ้าใช้ `pip` ธรรมดา ให้เพิ่ม `~/.local/bin` (Linux) หรือ `~/Library/Python/3.x/bin` (Mac) ไปที่ PATH ของคุณ หรือรัน `python -m graphify`

> **รันด้วย `uvx` / `uv tool run` แทนการติดตั้งหรือไม่?** ระบุชื่อแพ็กเกจ ไม่ใช่คำสั่ง: `uvx --from graphifyy graphify install` แค่ `uvx graphify …` เฉยๆ จะล้มเหลว (`No solution found … no versions of graphify`) เพราะ `uv tool run` อ่านคำแรกเป็น *แพ็กเกจ* และแพ็กเกจคือ `graphifyy` — คำสั่ง `graphify` อยู่ข้างในนั้น

> **หลีกเลี่ยง `pip install` บน Mac/Windows** ถ้าเป็นไปได้ skill จะแก้ไข Python ตอนรันไทม์จาก `graphify-out/.graphify_python`; ถ้าชี้ไปยังสภาพแวดล้อมที่ต่างจากที่ `pip` ติดตั้งแพ็กเกจไว้ คุณจะได้ `ModuleNotFoundError: No module named 'graphify'` `uv tool install` และ `pipx install` แยกแพ็กเกจไว้ในสภาพแวดล้อมของตัวเองและหลีกเลี่ยงปัญหานี้ได้ทั้งหมด

> **Git hooks กับ uv tool / pipx:** `graphify hook install` ฝังพาธของ interpreter ปัจจุบันโดยตรงใน hook script ตอนติดตั้ง เพื่อให้ post-commit hook ทำงานได้ถูกต้องแม้ใน git client แบบ GUI และ CI runner ที่ `~/.local/bin` ไม่อยู่ใน PATH ถ้าคุณติดตั้งใหม่หรืออัปเกรด graphify ให้รัน `graphify hook install` อีกครั้งเพื่อรีเฟรชพาธที่ฝังไว้

> **โหมดเข้มงวด (Claude Code):** `graphify install --project --strict` ทำให้ผู้ช่วยใช้กราฟจริงๆ การติดตั้งเริ่มต้นจะ *กระตุ้น* ให้รัน `graphify query` ก่อนอ่านไฟล์; โหมดเข้มงวดจะ *บล็อก* การอ่านซอร์สดิบครั้งแรกของเซสชันและเปลี่ยนเส้นทางไปที่กราฟ จากนั้นกลับไปเป็นการกระตุ้นตามปกติ (จึงทำงานได้อย่างมากหนึ่งครั้งต่อเซสชันและไม่ค้าง) สลับได้ตอนรันไทม์ด้วย `GRAPHIFY_HOOK_STRICT=1`/`0`; การติดตั้งเริ่มต้นไม่เปลี่ยนแปลง (กระตุ้นแบบนุ่มนวล)

<details>
<summary><b>เลือกแพลตฟอร์มของคุณ</b> (ผู้ช่วยกว่า 20 ตัว คลิกเพื่อขยาย)</summary>

| แพลตฟอร์ม | คำสั่งติดตั้ง |
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

ผู้ใช้ Codex ยังต้องการ `multi_agent = true` ใต้ `[features]` ในไฟล์ `~/.codex/config.toml` สำหรับการดึงข้อมูลแบบขนาน CodeBuddy ใช้กลไก Agent tool และ PreToolUse hook แบบเดียวกับ Claude Code Factory Droid ใช้เครื่องมือ `Task` สำหรับการส่งงาน subagent แบบขนาน OpenClaw และ Aider ใช้การดึงข้อมูลแบบลำดับ (การรองรับ agent แบบขนานยังเป็นช่วงเริ่มต้นในแพลตฟอร์มเหล่านี้) Trae ใช้เครื่องมือ Agent สำหรับการส่งงาน subagent แบบขนาน และ**ไม่**รองรับ hook `PreToolUse` ดังนั้น AGENTS.md จึงเป็นกลไกที่ทำงานตลอดเวลา

`--platform agents` (ชื่อเรียกอื่น `--platform skills`) มุ่งเป้าไปที่ตำแหน่ง [Agent-Skills](https://github.com/anthropics/skills) แบบข้ามเฟรมเวิร์กทั่วไป: `~/.agents/skills/` แบบ global ต่อผู้ใช้ตามข้อกำหนด (อ่านโดย `npx skills` และเฟรมเวิร์กที่สอดคล้องกับข้อกำหนด) สำหรับการติดตั้งแบบ global และ `./.agents/skills/` สำหรับการติดตั้งแบบโปรเจกต์ (`--project`) `graphify install` เฉยๆ ยังคงเป็นแพลตฟอร์มเดียว (Claude Code) โดยการออกแบบ — ใช้แพลตฟอร์มที่ชื่อ `agents` เมื่อคุณต้องการให้ skill ค้นพบได้โดยเฟรมเวิร์กใดก็ตามที่อ่าน `.agents/skills`

> Codex ใช้ `$graphify` แทน `/graphify`

</details>

<details>
<summary><b>ส่วนเสริมทางเลือก</b> (ติดตั้งเฉพาะสิ่งที่คุณต้องการ)</summary>

| ส่วนเสริม | สิ่งที่เพิ่มเข้ามา | ติดตั้ง |
|---|---|---|
| `pdf` | การดึงข้อมูล PDF | `uv tool install "graphifyy[pdf]"` |
| `office` | รองรับ `.docx` และ `.xlsx` | `uv tool install "graphifyy[office]"` |
| `google` | การเรนเดอร์ Google Sheets | `uv tool install "graphifyy[google]"` |
| `video` | ถอดข้อความวิดีโอ/เสียง (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | เซิร์ฟเวอร์ MCP stdio | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | รองรับ push ไป Neo4j | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | รองรับ push ไป FalkorDB | `uv tool install "graphifyy[falkordb]"` |
| `svg` | ส่งออกกราฟเป็น SVG | `uv tool install "graphifyy[svg]"` |
| `leiden` | ตรวจจับชุมชนแบบ Leiden (เฉพาะ Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | การอนุมานแบบ Ollama ในเครื่อง | `uv tool install "graphifyy[ollama]"` |
| `openai` | OpenAI / API ที่เข้ากันได้กับ OpenAI | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic Claude API (`--backend claude` ใช้ `ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (ใช้ IAM ไม่ต้องมี API key) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure` ใช้ `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "graphifyy[openai]"` |
| `sql` | การดึงข้อมูลสคีมา SQL | `uv tool install "graphifyy[sql]"` |
| `postgres` | ตรวจสอบสคีมา PostgreSQL แบบสด (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | การดึงข้อมูล AST ของ BYOND DreamMaker `.dm`/`.dme` (อาจต้องมีตัวคอมไพล์ C + `python3-dev` ถ้าไม่มี wheel ที่เข้ากับแพลตฟอร์มของคุณ) | `uv tool install "graphifyy[dm]"` |
| `terraform` | การดึงข้อมูล AST ของ Terraform / HCL `.tf`/`.tfvars`/`.hcl` | `uv tool install "graphifyy[terraform]"` |
| `pascal` | การดึงข้อมูล AST ของ Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` (เส้นเชื่อม `calls`/`inherits` แม่นยำกว่า; ใช้ตัวดึงข้อมูล regex สำรองเมื่อไม่มี) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | การแบ่งคำสำหรับคิวรีภาษาจีน (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | ทั้งหมดข้างต้น | `uv tool install "graphifyy[all]"` |

</details>

---

## ทำให้ผู้ช่วยของคุณใช้กราฟเสมอ

รันคำสั่งนี้ครั้งเดียวในโปรเจกต์ของคุณหลังจากสร้างกราฟแล้ว:

| แพลตฟอร์ม | คำสั่ง |
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

คำสั่งนี้จะเขียนไฟล์คอนฟิกเล็กๆ ที่บอกผู้ช่วยของคุณให้ปรึกษา knowledge graph สำหรับคำถามเกี่ยวกับโค้ดเบส โดยเลือกคิวรีที่จำกัดขอบเขตอย่าง `graphify query "<question>"` มากกว่าการอ่านรายงานทั้งหมดหรือ grep ไฟล์ดิบ

- **แพลตฟอร์มที่มี hook** (Claude Code, Gemini CLI): hook จะทำงานอัตโนมัติก่อนการเรียกเครื่องมือประเภทค้นหา (และใน Claude Code ก่อนการอ่านไฟล์ซอร์สทีละไฟล์ผ่านเครื่องมือ Read/Glob) และกระตุ้นให้ผู้ช่วยของคุณไปทางเส้นทางกราฟ
- **แพลตฟอร์มที่มีไฟล์คำสั่ง** (Codex, OpenCode, Cursor เป็นต้น): ไฟล์คำสั่งถาวร (`AGENTS.md`, `.cursor/rules/` เป็นต้น) ให้คำแนะนำแบบคิวรีก่อนเช่นเดียวกัน

`GRAPH_REPORT.md` ยังคงใช้งานได้สำหรับการทบทวนสถาปัตยกรรมแบบกว้าง

**CodeBuddy** ทำสองสิ่งเดียวกับ Claude Code: เขียนส่วน `CODEBUDDY.md` ที่บอก CodeBuddy ให้อ่าน `graphify-out/GRAPH_REPORT.md` ก่อนตอบคำถามเกี่ยวกับสถาปัตยกรรม และติดตั้ง hook `PreToolUse` (`.codebuddy/settings.json`) ที่ทำงานก่อนคำสั่งค้นหา Bash และการอ่านไฟล์ กระตุ้นให้ใช้ `graphify query` แทน

**Codex** เขียนลงใน `AGENTS.md` ซึ่งเป็นสิ่งที่แบกรับคำแนะนำกราฟแบบทำงานตลอดเวลาจริงๆ บนแพลตฟอร์มนี้ `graphify codex install` ยังลงทะเบียน hook `PreToolUse` ใน `.codex/hooks.json` (`graphify hook-check`) ด้วย แต่รายการนั้นตั้งใจให้เป็น **no-op**: Codex Desktop ปฏิเสธ `hookSpecificOutput.additionalContext` บน `PreToolUse` ดังนั้นการส่งการกระตุ้นที่นั่นจะทำให้การเรียกเครื่องมือ Bash พัง ต่างจาก Claude Code ที่ hook (`graphify hook-guard`) ทำการกระตุ้น บน Codex hook จะทำงานแต่ตั้งใจไม่ทำอะไร และ `AGENTS.md` คือกลไกที่ทำงานตลอดเวลา

**Kilo Code** ติดตั้ง skill Graphify ไปที่ `~/.config/kilo/skills/graphify/SKILL.md` และคำสั่ง `/graphify` แบบเนทีฟไปที่ `~/.config/kilo/command/graphify.md` `graphify kilo install` ยังเขียน `AGENTS.md` พร้อมปลั๊กอิน `tool.execute.before` แบบเนทีฟ (`.kilo/plugins/graphify.js` + การลงทะเบียน `.kilo/kilo.json` หรือ `.kilo/kilo.jsonc`) เพื่อให้ Kilo ได้รับพฤติกรรมการเตือนกราฟแบบทำงานตลอดเวลาเดียวกันผ่านคอนฟิก `.kilo` แบบเนทีฟ

**Cursor** เขียน `.cursor/rules/graphify.mdc` ด้วย `alwaysApply: true` ดังนั้น Cursor จะรวมมันไว้ในทุกการสนทนาโดยอัตโนมัติ ไม่ต้องใช้ hook

หากต้องการลบ graphify ออกจากทุกแพลตฟอร์มพร้อมกัน: `graphify uninstall` (เพิ่ม `--purge` เพื่อลบ `graphify-out/` ด้วย) หรือใช้คำสั่งเฉพาะแพลตฟอร์ม (เช่น `graphify claude uninstall`)

---

## สิ่งที่อยู่ในรายงาน

- **God node** — แนวคิดที่เชื่อมโยงมากที่สุดในโปรเจกต์ของคุณ ทุกอย่างไหลผ่านสิ่งเหล่านี้
- **การเชื่อมโยงที่น่าประหลาดใจ** — ลิงก์ระหว่างสิ่งที่อยู่ในไฟล์หรือโมดูลต่างกัน จัดอันดับตามความไม่คาดคิด
- **"ทำไม"** — คอมเมนต์ในโค้ด (`# NOTE:`, `# WHY:`, `# HACK:`) docstring และเหตุผลการออกแบบจากเอกสารถูกดึงออกมาเป็นโหนดแยกที่เชื่อมกับโค้ดที่พวกมันอธิบาย
- **คำถามที่แนะนำ** — 4–5 คำถามที่กราฟมีความพร้อมเป็นพิเศษในการตอบ
- **แท็กความเชื่อมั่น** — ทุกความสัมพันธ์ที่อนุมานได้จะถูกทำเครื่องหมายเป็น `EXTRACTED`, `INFERRED`, หรือ `AMBIGUOUS` คุณจะรู้เสมอว่าอะไรถูกพบเทียบกับอะไรถูกเดา

---

## ไฟล์ประเภทไหนที่มันจัดการได้

| ประเภท | นามสกุล |
|------|-----------|
| โค้ด (36 ไวยากรณ์ tree-sitter) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme` ต้องมี `uv tool install graphifyy[dm]`; `.mts`/`.cts` ใช้ไวยากรณ์ TypeScript ซ้ำ, `.cc`/`.cxx` และ CUDA `.cu`/`.cuh` และ Metal `.metal` ใช้ไวยากรณ์ C++ ซ้ำ) |
| Salesforce Apex | `.cls .trigger` (อิงตาม regex; คลาส อินเทอร์เฟซ enum เมธอด trigger เส้นเชื่อม SOQL/DML) |
| Terraform / HCL | `.tf .tfvars .hcl` (ต้องมี `uv tool install graphifyy[terraform]`) |
| คอนฟิก MCP | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — ดึงโหนดเซิร์ฟเวอร์ การอ้างอิงแพ็กเกจ ข้อกำหนดตัวแปรสภาพแวดล้อม |
| ไฟล์ manifest แพ็กเกจ | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — หนึ่งโหนดแพ็กเกจมาตรฐานต่อแพ็กเกจ (ตามชื่อ) บวกเส้นเชื่อม `depends_on` ดังนั้นแพ็กเกจที่ถูกอ้างอิงจาก manifest หลายไฟล์จะเป็น hub เดียว |
| เอกสาร | `.md .mdx .qmd .html .txt .rst .yaml .yml` (ลิงก์ markdown `[text](./other.md)` และ `[[wikilinks]]` กลายเป็นเส้นเชื่อม `references` ระหว่างเอกสาร) |
| Office | `.docx .xlsx` (ต้องมี `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (ต้องเปิดใช้เอง; ต้องยืนยันตัวตนด้วย `gws` และ `--google-workspace`; Sheets ต้องมี `uv tool install graphifyy[google]`) |
| PDF | `.pdf` |
| รูปภาพ | `.png .jpg .webp .gif` |
| วิดีโอ / เสียง | `.mp4 .mov .mp3 .wav` และอื่นๆ (ต้องมี `uv tool install graphifyy[video]`) |
| YouTube / URL | URL วิดีโอใดก็ได้ (ต้องมี `uv tool install graphifyy[video]`) |

โค้ดถูกดึงข้อมูล **ในเครื่องโดยไม่มีการเรียก API** (AST ผ่าน tree-sitter) ทุกอย่างอื่นผ่าน API โมเดลของผู้ช่วย AI ของคุณ

ไฟล์ `.gdoc`, `.gsheet`, และ `.gslides` ของ Google Drive for desktop เป็นตัวชี้ shortcut ไม่ใช่เนื้อหาเอกสาร หากต้องการรวม Google Docs, Sheets, และ Slides แบบเนทีฟในการดึงข้อมูลแบบ headless ให้ติดตั้งและยืนยันตัวตนด้วย [`gws` CLI](https://github.com/googleworkspace/cli) แล้วรัน:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

คุณสามารถตั้งค่า `GRAPHIFY_GOOGLE_WORKSPACE=1` ได้เช่นกัน Graphify ส่งออก shortcut ไปยัง `graphify-out/converted/` เป็นไฟล์ Markdown ประกอบ แล้วดึงข้อมูลจากไฟล์เหล่านั้น

---

## คำสั่งที่ใช้บ่อย

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

ดู [Decouple: ผู้สมัคร Extract-Class ที่ให้คะแนนความเสี่ยง](#decouple-risk-scored-extract-class-candidates) ด้านบน หรือ [รายการคำสั่งฉบับเต็ม](#full-command-reference) ด้านล่าง

---

## การละเว้นไฟล์

สร้าง `.graphifyignore` ที่รากของโปรเจกต์คุณ — ไวยากรณ์เดียวกับ `.gitignore` รวมถึงการปฏิเสธด้วย `!`

**`.gitignore` จะถูกเคารพโดยอัตโนมัติ** graphify อ่าน `.gitignore` ในทุกไดเรกทอรี ถ้ามี `.graphifyignore` ด้วย ทั้งสองจะถูก **รวมกัน** — รูปแบบของ `.graphifyignore` จะถูกประเมินทีหลังสุด ดังนั้นจึงชนะเมื่อขัดแย้งกัน (รวมถึงการปฏิเสธด้วย `!`) การเพิ่ม `.graphifyignore` จะยกเว้นเพิ่มขึ้นเท่านั้น มันจะไม่รวมไฟล์ที่ `.gitignore` ของคุณยกเว้นไปแล้วกลับเข้ามาอีก ขอบเขตของไดเรกทอรีย่อยทำงานเหมือนกับ git — ไฟล์ ignore จะมีผลกับ subtree ของตัวเองเท่านั้น

ส่ง `--no-gitignore` ให้ `graphify extract` เมื่อโค้ดที่สร้างขึ้นหรือแปลงแล้วที่ git ละเว้นอยู่ควรอยู่ในกราฟ วิธีนี้จะปิดใช้งาน `.gitignore` และ `.git/info/exclude`; `.graphifyignore` ยังคงมีผล

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

## การตั้งค่าสำหรับทีม

`graphify-out/` ตั้งใจให้ commit ลง git เพื่อให้ทุกคนในทีมเริ่มต้นด้วยแผนที่เดียวกัน

**สิ่งที่แนะนำให้เพิ่มใน `.gitignore`:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` ตอนนี้ย้ายได้แล้ว — คีย์ถูกเก็บเป็นพาธสัมพัทธ์และถูกกำหนดตำแหน่งใหม่ตอนโหลด ดังนั้นการ commit มันจึงปลอดภัยและหลีกเลี่ยงการสร้างใหม่ทั้งหมดตอน checkout ครั้งแรก

**ขั้นตอนการทำงาน:**
1. คนหนึ่งรัน `/graphify .` และ commit `graphify-out/`
2. ทุกคน pull — ผู้ช่วยของพวกเขาอ่านกราฟทันที
3. รัน `graphify hook install` เพื่อสร้างใหม่อัตโนมัติหลังทุก commit (เฉพาะ AST ไม่มีค่าใช้จ่าย API) วิธีนี้ยังตั้งค่า git merge driver เพื่อให้ `graph.json` ไม่มีเครื่องหมายขัดแย้งค้างอยู่เลย — นักพัฒนาสองคนที่ commit พร้อมกันจะได้กราฟถูก union-merge อัตโนมัติ
4. เมื่อเอกสารหรือบทความเปลี่ยนแปลง รัน `/graphify --update` เพื่อรีเฟรชโหนดเหล่านั้น

---

## ใช้กราฟโดยตรง

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

เซิร์ฟเวอร์ MCP ให้ผู้ช่วยของคุณเข้าถึงแบบมีโครงสร้าง: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`

### เซิร์ฟเวอร์ HTTP แบบแชร์

`--transport stdio` (ค่าเริ่มต้น) จะสร้างเซิร์ฟเวอร์ในเครื่องหนึ่งตัวต่อนักพัฒนาหนึ่งคน `--transport http` ให้บริการเครื่องมือเดียวกันผ่าน MCP Streamable HTTP transport ดังนั้นโปรเซสที่แชร์กันตัวเดียวสามารถให้บริการกราฟสำหรับทั้งทีมได้ — client ชี้คอนฟิก MCP ของ IDE ไปที่ `http://<host>:8080/mcp` แทนการรัน graphify ในเครื่อง

| แฟล็ก | ค่าเริ่มต้น | จุดประสงค์ |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Transport ที่จะให้บริการ |
| `--host` | `127.0.0.1` | โฮสต์ที่ bind HTTP (ใช้ `0.0.0.0` เพื่อเปิดใช้งานนอกเหนือจาก localhost) |
| `--port` | `8080` | พอร์ตที่ bind HTTP |
| `--api-key` | env `GRAPHIFY_API_KEY` | ต้องมี `Authorization: Bearer <key>` (หรือ `X-API-Key`) |
| `--path` | `/mcp` | พาธที่ mount HTTP |
| `--json-response` | ปิด | คืน JSON ธรรมดาแทนสตรีม SSE |
| `--stateless` | ปิด | ไม่มี state ต่อเซสชัน (สำหรับการปรับใช้แบบ load-balanced / CI) |
| `--session-timeout` | `3600` | ล้างเซสชันแบบ stateful ที่ไม่ใช้งานหลัง N วินาที (`0` ปิดใช้งาน) |

การ bind `127.0.0.1` เริ่มต้นเป็นแบบ loopback เท่านั้น ตั้งค่า `--host 0.0.0.0` **และ** `--api-key` พร้อมกันเมื่อเปิดใช้งานบนโฮสต์ที่แชร์ รันมันในคอนเทนเนอร์:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **หมายเหตุ WSL / Linux:** Ubuntu มี `python3` ให้ ไม่ใช่ `python` ใช้ venv เพื่อหลีกเลี่ยงความขัดแย้ง:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## ตัวแปรสภาพแวดล้อม

ตัวแปรเหล่านี้จำเป็นเฉพาะสำหรับการดึงข้อมูลแบบ **headless / CI** (`graphify extract`) เท่านั้น เมื่อรันผ่าน skill `/graphify` ใน IDE ของคุณ API โมเดลจะมาจากเซสชัน IDE ของคุณ — ไม่ต้องใช้คีย์เพิ่มเติม

| ตัวแปร | ใช้สำหรับ | จำเป็นเมื่อไร |
|---|---|---|
| `ANTHROPIC_API_KEY` | backend Claude (Anthropic) | `--backend claude` |
| `ANTHROPIC_BASE_URL` | URL endpoint ที่เข้ากันได้กับ Anthropic (LiteLLM proxy, gateway, ...) | `--backend claude` (ค่าเริ่มต้น: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | ชื่อโมเดลสำหรับ backend Claude — สำหรับ endpoint แบบกำหนดเอง ใช้ชื่อ/alias ของโมเดลที่เซิร์ฟเวอร์ของคุณเปิดให้ใช้ | `--backend claude` (ค่าเริ่มต้น: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` หรือ `GOOGLE_API_KEY` | backend Google Gemini | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI หรือ API ที่เข้ากันได้กับ OpenAI | `--backend openai` (เซิร์ฟเวอร์ในเครื่องรับค่าใดก็ได้ที่ไม่ว่างเปล่า) |
| `OPENAI_BASE_URL` | URL เซิร์ฟเวอร์ที่เข้ากันได้กับ OpenAI (llama.cpp, vLLM, LM Studio, ...) | `--backend openai` (ค่าเริ่มต้น: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | ชื่อโมเดลสำหรับ backend OpenAI — สำหรับเซิร์ฟเวอร์ self-hosted ใช้ชื่อ/alias ของโมเดลที่เซิร์ฟเวอร์ของคุณเปิดให้ใช้ (ตรวจสอบ endpoint `/v1/models`) เช่น `LFM2.5-8B-A1B-UD-Q4_K_XL` สำหรับ llama.cpp | `--backend openai` (ค่าเริ่มต้น: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | backend DeepSeek | `--backend deepseek` |
| `MOONSHOT_API_KEY` | backend Kimi Code | `--backend kimi` |
| `OLLAMA_BASE_URL` | URL การอนุมาน Ollama ในเครื่อง | `--backend ollama` (ค่าเริ่มต้น: `http://localhost:11434`) |
| `OLLAMA_MODEL` | ชื่อโมเดล Ollama | `--backend ollama` (ค่าเริ่มต้น: ตรวจจับอัตโนมัติ) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | เขียนทับขนาดหน้าต่าง KV-cache ของ Ollama | ทางเลือก — กำหนดขนาดอัตโนมัติโดยค่าเริ่มต้น |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | นาทีที่จะเก็บโมเดล Ollama ไว้ในหน่วยความจำ | ทางเลือก — ตั้งเป็น `0` เพื่อเลิกโหลดหลังแต่ละส่วน |
| `AZURE_OPENAI_API_KEY` | backend Azure OpenAI Service | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | URL endpoint ทรัพยากร Azure | `--backend azure` (จำเป็นควบคู่กับ API key) |
| `AZURE_OPENAI_API_VERSION` | เขียนทับเวอร์ชัน API ของ Azure | ทางเลือก — ค่าเริ่มต้น `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` หรือ `GRAPHIFY_AZURE_MODEL` | ชื่อ deployment ของ Azure | ทางเลือก — ค่าเริ่มต้น `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — chain ของ credential มาตรฐาน | `--backend bedrock` (ไม่ต้องใช้ API key ใช้ IAM) |
| `GRAPHIFY_MAX_WORKERS` | จำนวน thread สำหรับการทำงานแบบขนานของ AST | ทางเลือก — มีแฟล็ก `--max-workers` ด้วย |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | เพิ่มเพดานผลลัพธ์สำหรับ corpus ที่หนาแน่น | ทางเลือก — เช่น `32768` สำหรับไฟล์ขนาดใหญ่ |
| `GRAPHIFY_API_TIMEOUT` | timeout ต่อการเรียกเป็นวินาที สำหรับ backend HTTP, claude-cli, Anthropic SDK, และ Bedrock (ค่าเริ่มต้น: 600) | ทางเลือก — มีแฟล็ก `--api-timeout` ด้วย |
| `GRAPHIFY_MAX_RETRIES` | จำนวนครั้งที่จะลองใหม่สำหรับคำขอที่ถูกจำกัดอัตรา (429) ก่อนยอมแพ้ (ค่าเริ่มต้น: 6; เคารพ `Retry-After`) | ทางเลือก — เพิ่มสำหรับข้อจำกัดที่เข้มงวดต่อองค์กร (เช่น kimi); `0` ปิดใช้งาน |
| `GRAPHIFY_FORCE` | บังคับสร้างกราฟใหม่แม้จะมีโหนดน้อยลง | ทางเลือก — มีแฟล็ก `--force` ด้วย |
| `GRAPHIFY_GOOGLE_WORKSPACE` | เปิดใช้งานการส่งออก Google Workspace อัตโนมัติ | ทางเลือก — ตั้งเป็น `1` |
| `GRAPHIFY_TRIAGE_BACKEND` | backend สำหรับ `graphify prs --triage` | ทางเลือก — ตรวจจับอัตโนมัติจากคีย์ที่มีอยู่ |
| `GRAPHIFY_TRIAGE_MODEL` | เขียนทับโมเดลสำหรับ triage | ทางเลือก — เช่น `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | ตั้งเป็น `1` เพื่อเปิดใช้ log คิวรีในเครื่องที่ `~/.cache/graphify-queries.log` (บันทึกทุกคำถาม query/path/explain + พาธ corpus) ปิดโดยค่าเริ่มต้น — ไม่มีอะไรถูกเขียนเว้นแต่คุณจะเปิดใช้เอง (#1797) | ทางเลือก |
| `GRAPHIFY_QUERY_LOG` | เปิดใช้ log คิวรีและเขียนไปยังพาธนี้แทนค่าเริ่มต้น | ทางเลือก — ปิดเว้นแต่ตัวนี้หรือ `_ENABLE` ถูกตั้งค่า |
| `GRAPHIFY_QUERY_LOG_DISABLE` | ตั้งเป็น `1` เพื่อบังคับปิด log คิวรี (ชนะตัวแปร enable) | ทางเลือก |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | เมื่อ log เปิดใช้งาน จะบันทึกคำตอบซับกราฟแบบเต็มด้วย (ปิดโดยค่าเริ่มต้น) | ทางเลือก |
| `GRAPHIFY_MAX_GRAPH_BYTES` | เขียนทับเพดานขนาด 512 MiB ของ graph.json — เช่น `700MB`, `2GB`, หรือไบต์ธรรมดา | ทางเลือก — มีประโยชน์สำหรับ corpus ขนาดใหญ่มาก |
| `GRAPHIFY_MAX_CONTEXTS` | จำนวนสูงสุดของกราฟโปรเจกต์ที่ไม่ใช่ค่าเริ่มต้นที่เซิร์ฟเวอร์ MCP หลายโปรเจกต์หนึ่งตัวเก็บไว้ | ทางเลือก — ค่าเริ่มต้น: `8`; ค่าที่ไม่ถูกต้องจะใช้ `8` และค่าที่ต่ำกว่า `1` จะใช้ `1` |
| `GRAPHIFY_LLM_TEMPERATURE` | เขียนทับอุณหภูมิ LLM สำหรับการดึงข้อมูลเชิงความหมาย — เช่น `0.7` หรือ `none` เพื่อไม่ใส่ | ทางเลือก — ไม่ใส่อัตโนมัติสำหรับโมเดล reasoning o1/o3/o4/gpt-5 |

---

## ความเป็นส่วนตัว

- **ไฟล์โค้ด** — ประมวลผลในเครื่องผ่าน tree-sitter ไม่มีอะไรออกจากเครื่องคุณ corpus ที่มีแต่โค้ดไม่ต้องใช้ API key — `graphify extract` ทำงานแบบออฟไลน์ทั้งหมด ในรีโพที่มีทั้งโค้ดและอย่างอื่นปนกัน เพิ่ม `--code-only` เพื่อจัดทำดัชนีเฉพาะโค้ดและข้ามเอกสาร/PDF/รูปภาพที่ต้องใช้ LLM
- **วิดีโอ / เสียง** — ถอดข้อความในเครื่องด้วย faster-whisper ไม่มีอะไรออกจากเครื่องคุณ
- **เอกสาร PDF รูปภาพ** — ถูกส่งไปยังผู้ช่วย AI ของคุณเพื่อการดึงข้อมูลเชิงความหมาย (ผ่าน skill `/graphify` ใช้โมเดลใดก็ตามที่เซสชัน IDE ของคุณรัน) `graphify extract` แบบ headless ต้องมี `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), instance ของ Ollama ที่กำลังทำงาน (`OLLAMA_BASE_URL`), credential ของ AWS ผ่าน provider chain มาตรฐาน (Bedrock - ไม่ต้องใช้ API key ใช้ IAM) หรือไบนารี CLI `claude` (Claude Code - ไม่ต้องใช้ API key ใช้การสมัครสมาชิก Claude ของคุณ) แฟล็ก `--dedup-llm` ใช้คีย์เดียวกัน
- **ที่ตั้งข้อมูล** — `graphify extract` ตรวจจับอัตโนมัติว่าจะใช้ provider ไหนตาม API key ที่ตั้งไว้ (ลำดับความสำคัญ: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama) สำหรับโค้ดที่มีข้อกำหนดเรื่องที่ตั้งข้อมูล ใช้ `--backend ollama` (ในเครื่องทั้งหมด) หรือส่งแฟล็ก `--backend` แบบชัดเจน Kimi (`MOONSHOT_API_KEY`) ส่งข้อมูลไปยังเซิร์ฟเวอร์ Moonshot AI ในจีน
- **ไม่มี telemetry** ไม่มีการติดตามการใช้งาน ไม่มี analytics
- **การบันทึกคิวรี** — ทุกการเรียก `graphify query`, `graphify path`, `graphify explain`, และ MCP `query_graph` จะถูกบันทึกไปที่ `~/.cache/graphify-queries.log` ในรูปแบบ JSON Lines (timestamp คำถาม corpus โหนดที่คืนมา ระยะเวลา) คำตอบซับกราฟแบบเต็ม **ไม่** ถูกเก็บโดยค่าเริ่มต้น ตั้งค่า `GRAPHIFY_QUERY_LOG_DISABLE=1` เพื่อยกเลิก หรือ `GRAPHIFY_QUERY_LOG=/dev/null` เพื่อปิดเสียงโดยไม่ปิดใช้งาน code path

---

## การแก้ไขปัญหา

**`graphify: command not found` หลังติดตั้ง**
CLI ถูกติดตั้งแล้วแต่ไดเรกทอรี bin ของมันไม่อยู่ใน `PATH` ของ shell คุณ เลือกวิธีแก้ตามวิธีที่คุณติดตั้ง:
- **uv** (`uv tool install graphifyy`): คำสั่งลงเอยในไดเรกทอรี bin ของเครื่องมือ uv (`~/.local/bin`) ซึ่งการติดตั้ง macOS/zsh ใหม่มักจะไม่มีใน `PATH` รัน `uv tool update-shell` แล้วเปิดเทอร์มินัลใหม่ (หาไดเรกทอรีด้วย `uv tool dir --bin`)
- **pipx** (`pipx install graphifyy`): รัน `pipx ensurepath` แล้วเปิดเทอร์มินัลใหม่
- **pip** (`pip install graphifyy`): pip ติดตั้งสคริปต์ไปยังไดเรกทอรี bin ของผู้ใช้ซึ่งอาจไม่อยู่ใน `PATH` — เพิ่ม `~/Library/Python/3.x/bin` (macOS) หรือ `~/.local/bin` (Linux) ไปที่ `PATH` ของคุณใน `~/.zshrc`/`~/.bashrc` หรือรัน `python -m graphify` เฉยๆ

**`uvx graphify …` หรือ `uv tool run graphify …` แก้ไข `graphify` ไม่ได้**
แพ็กเกจ PyPI คือ `graphifyy`; `graphify` เป็นเพียงคำสั่งที่มันมอบให้ `uv tool run` ถือว่าคำแรกเป็น *ชื่อแพ็กเกจ* ดังนั้นมันจะหาแพ็กเกจชื่อ `graphify` และรายงาน `No solution found … no versions of graphify` ระบุชื่อแพ็กเกจอย่างชัดเจน: `uvx --from graphifyy graphify install` (เหมือนกับ `uv tool run --from graphifyy graphify install`) หรือทำ `uv tool install graphifyy` ครั้งเดียวแล้วเรียก `graphify` โดยตรง

**`uv run --with graphifyy python -m graphify` รันเวอร์ชันเก่ากว่าโดยเงียบๆ**
`uv run` ใช้ Python *ของระบบ* คุณ ดังนั้นถ้ามี `graphifyy` เก่ากว่าอยู่ที่นั่นด้วย (เช่น `pip install graphifyy` ในอดีต) Python อาจพบสำเนานั้นก่อนใน `sys.path` และ `--with graphifyy` จะไม่เขียนทับมัน มันรันโดยไม่มีข้อผิดพลาด แต่คุณจะได้พฤติกรรมของเวอร์ชัน *เก่า* — เช่น การเขียนทับสภาพแวดล้อมอย่าง `OPENAI_BASE_URL` จะถูกเพิกเฉยอย่างเงียบๆ ทำให้คำขอไปกระทบ endpoint เริ่มต้นและล้มเหลวด้วย 401 ที่ดูเหมือนคีย์ผิด ลายนิ้วมือคือบรรทัด `warning: skill is from graphify <newer>, package is <older>` — นั่นหมายความว่ามีการติดตั้งอื่นถูกโหลด ไม่ใช่แค่ skill เก่า ตรวจสอบว่าสำเนาไหนถูกโหลดจริง:
```bash
python -c "import graphify; print(graphify.__file__)"
```
จากนั้นรันคำสั่งที่ติดตั้งแล้วโดยตรง (มันใช้สำเนาที่ uv จัดการ) หรือลบสำเนาระบบเก่า:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` ทำงาน แต่คำสั่ง `graphify` ไม่ทำงาน**
`PATH` ของ shell คุณไม่มีไดเรกทอรี bin ที่คำสั่งถูกติดตั้งไว้ เลือก `uv tool install` / `pipx install` แทน `pip` ธรรมดา แล้วรัน `uv tool update-shell` / `pipx ensurepath` และเปิดเทอร์มินัลใหม่ (ดูหมายเหตุการติดตั้งด้านบน)

**`/graphify .` ทำให้เกิด "path not recognized" ใน PowerShell**
PowerShell ถือว่าเครื่องหมายทับที่นำหน้าเป็นตัวแบ่งพาธ ใช้ `graphify .` (ไม่มีเครื่องหมายทับ) บน Windows

**กราฟมีโหนดน้อยลงหลัง `--update` หรือสร้างใหม่**
ถ้าการปรับโครงสร้างลบไฟล์ออกไป โหนดเก่าจะยังค้างอยู่ ส่ง `--force` (หรือตั้งค่า `GRAPHIFY_FORCE=1`) เพื่อเขียนทับแม้ว่าการสร้างใหม่จะมีโหนดน้อยลง

**`extract` จบด้วย "extraction was incomplete ... refusing to overwrite"**
เมื่อขั้นตอนการดึงข้อมูลล้มเหลวหรือการเดินไฟล์อ่าน corpus ไม่ครบ การรันนั้นจะเล็กกว่าการรันที่สมบูรณ์ ดังนั้น `graphify extract` จะปฏิเสธไม่เขียนทับกราฟที่มีอยู่ซึ่งใหญ่กว่าด้วยผลลัพธ์บางส่วน (ปกป้อง `graph.json` ของคุณ) แก้ไขความล้มเหลวที่ต้นเหตุแล้วรันใหม่ หรือส่ง `--allow-partial` เพื่อเขียนทับต่อไปอยู่ดี

**กราฟมีโหนดซ้ำสำหรับ entity เดียวกัน (โหนดผีซ้ำ)**
โหนดผีซ้ำ (สัญลักษณ์เดียวกันปรากฏสองครั้ง — ครั้งหนึ่งจากการดึงข้อมูล AST พร้อมตำแหน่งซอร์ส อีกครั้งจากการดึงข้อมูลเชิงความหมายโดยไม่มี) ตอนนี้ถูกรวมอัตโนมัติตอนสร้างกราฟแล้ว ถ้าคุณเห็นสิ่งนี้ในกราฟที่สร้างก่อน v0.8.33 รันการดึงข้อมูลใหม่ทั้งหมดเพื่อทำความสะอาด:
```bash
graphify extract . --force
```

**Ollama ใช้ VRAM หมด / เกินขนาดหน้าต่าง context**
หน้าต่าง KV-cache กำหนดขนาดอัตโนมัติแต่อาจใหญ่เกินไปสำหรับ GPU ของคุณ ลดขนาด:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**คำเตือน `LLM returned invalid JSON` / `Unterminated string`**
คำตอบ JSON ของโมเดลชนเพดาน output-token และถูกตัดกลางข้อความ graphify กู้คืนอัตโนมัติ (มันแบ่งส่วนและดึงข้อมูลครึ่งหนึ่งใหม่ และเอกสารเดี่ยวที่ใหญ่เกินไปจะถูกตัดที่ขอบเขตหัวข้อ/ย่อหน้าก่อน เพื่อให้ทั้งไฟล์ยังถูกครอบคลุม) ดังนั้นคำเตือนเหล่านี้จะดังแต่ไม่ใช่ข้อมูลสูญหาย เพื่อลดเสียงรบกวน เพิ่มเพดานผลลัพธ์หรือลดผลลัพธ์ของแต่ละส่วน:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
กับ cloud gateway อย่าง OpenRouter เลือก `--backend openai` (ตั้ง `OPENAI_BASE_URL`) มากกว่า Ollama shim — เป็นเส้นทางที่เข้ากันได้กับ OpenAI ที่สะอาดกว่า ถ้าโมเดลมีเพดาน max-output ของตัวเอง การลด `--token-budget` เป็นตัวปรับที่เชื่อถือได้

**Graph HTML ใหญ่เกินไปที่จะเปิดในเบราว์เซอร์ (มากกว่า 5000 โหนด)**
ข้ามการสร้าง HTML และใช้ JSON โดยตรง:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**`graph.json` มีเครื่องหมายขัดแย้งหลังนักพัฒนาสองคน commit พร้อมกัน**
รัน `graphify hook install` — มันตั้งค่า git merge driver ที่ union-merge `graph.json` โดยอัตโนมัติ เพื่อไม่ให้เกิดความขัดแย้งเลย

**การดึงข้อมูลคืนโหนด/เส้นเชื่อมว่างเปล่าสำหรับเอกสารหรือ PDF**
เอกสาร PDF และรูปภาพต้องใช้การเรียก LLM — corpus ที่มีแต่โค้ดไม่ต้องใช้คีย์ ตรวจสอบว่า API key ของคุณตั้งค่าแล้วและ backend ถูกต้อง:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**คำเตือนเวอร์ชัน skill ไม่ตรงกันใน IDE ของคุณ**
เวอร์ชัน graphify ที่ติดตั้งของคุณต่างจากไฟล์ skill อัปเดต:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**cache prompt ของ Claude Code ถูกทำให้ใช้ไม่ได้หลังทุก `graphify extract`**
Graphify เขียนไฟล์ผลลัพธ์ (`graph.json`, `graphify-out/`) ลงใน workspace ถ้าพาธเหล่านั้นไม่ถูกละเว้น ทุกครั้งที่เขียนจะทำให้ cache prompt ของ Claude Code ใช้ไม่ได้ บังคับให้อัปโหลดใหม่ทั้งหมดในอัตราการเขียน cache ในรอบถัดไป เพิ่มพาธเหล่านั้นไปที่ `.claudeignore`:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## รายการคำสั่งฉบับเต็ม

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

> **ชื่อชุมชน:** ภายใน agent (Claude Code, Gemini CLI) ตัว agent จะตั้งชื่อชุมชนเอง เมื่อคุณรัน CLI เปล่าๆ `cluster-only` จะตั้งชื่อให้อัตโนมัติด้วย backend ที่ตั้งค่าไว้ (built-in หรือ provider ที่เข้ากันได้กับ OpenAI แบบกำหนดเอง) — ส่ง `--no-label` เพื่อคงไว้เป็น `Community N` หรือรัน `graphify label` เพื่อสร้างชื่อ (ใหม่) ตามต้องการ

---

## เรียนรู้เพิ่มเติม

- [มันทำงานอย่างไร](docs/how-it-works.md) — pipeline การดึงข้อมูล การตรวจจับชุมชน การให้คะแนนความเชื่อมั่น benchmark
- [ARCHITECTURE.md](ARCHITECTURE.md) — การแบ่งโมดูล วิธีเพิ่มภาษา
- [การผสานรวมทางเลือก](docs/docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — หนังสือเกี่ยวกับแนวคิดเบื้องหลัง graphify สถาปัตยกรรมตั้งแต่ต้นจนจบ

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) คือชั้นที่ทำงานตลอดเวลาที่สร้างบน graphify — มันใช้แนวทางกราฟเดียวกันกับบริบทการทำงานทั้งหมดของคุณ: การประชุม ไฟล์ เอกสาร และโค้ด อัปเดตอย่างต่อเนื่องในพื้นหลัง

สร้างขึ้นสำหรับคนและทีมที่งานของพวกเขาอยู่ในบทสนทนาและเอกสารหลายร้อยรายการที่พวกเขาไม่มีวันสร้างขึ้นใหม่ได้อย่างสมบูรณ์

**[เข้าร่วม waitlist ที่ graphify.com](https://graphify.com)** ทดลองใช้ฟรีเร็วๆ นี้

---

<details>
<summary>การมีส่วนร่วม</summary>

### การตั้งค่าสภาพแวดล้อมสำหรับพัฒนา

โปรเจกต์ใช้ [uv](https://docs.astral.sh/uv/) สำหรับขั้นตอนการพัฒนา ติดตั้งครั้งเดียว จากนั้น:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

ตรวจสอบการติดตั้งแบบ editable:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### การรันเทสต์

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> หมายเหตุ macOS: ชุดเทสต์รวม fixture ทั้ง `sample.f90` และ `sample.F90` สิ่งเหล่านี้จะชนกันบนระบบไฟล์ที่ไม่แยกตัวพิมพ์ใหญ่-เล็กอย่าง HFS+ / APFS รันบน Linux หรือในคอนเทนเนอร์ Docker ถ้าคุณต้องการทดสอบตัวแปร Fortran ทั้งสองพร้อมกัน

### ขั้นตอนการทำงานของ Git

- การพัฒนาเชิงรุกเกิดขึ้นบนสาขา `v8`
- รูปแบบ commit: `fix: <description>` / `feat: <description>` / `docs: <description>`
- ก่อนเปิด PR รัน `uv run pytest tests/ -q` และยืนยันว่าผ่าน
- เพิ่มไฟล์ fixture ไปที่ `tests/fixtures/` และเทสต์ไปที่ `tests/test_languages.py` สำหรับตัวดึงข้อมูลภาษาใหม่ทุกตัว

### สิ่งที่ควรมีส่วนร่วม

**ตัวอย่างที่ทำสำเร็จแล้ว (worked examples)** เป็นการมีส่วนร่วมที่มีประโยชน์ที่สุด รัน `/graphify` บน corpus จริง บันทึกผลลัพธ์ไปที่ `worked/{slug}/` เขียน `review.md` ที่ตรงไปตรงมาซึ่งครอบคลุมสิ่งที่กราฟทำถูกและผิด แล้วเปิด PR

**บั๊กในการดึงข้อมูล** — เปิด issue พร้อมไฟล์อินพุต รายการ cache (`graphify-out/cache/`) และสิ่งที่พลาดหรือผิดพลาด

ดู [ARCHITECTURE.md](ARCHITECTURE.md) สำหรับความรับผิดชอบของแต่ละโมดูลและวิธีเพิ่มภาษา

</details>
