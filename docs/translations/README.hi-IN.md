<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b><a href="https://github.com/Graphify-Labs/graphify">graphify</a> का एक फ़ोर्क जो <code>graphify decouple</code> जोड़ता है</b> — god objects के लिए जोखिम-स्कोर वाले Extract-Class उम्मीदवार, बिना LLM के, कुछ भी सुझाने से पहले असली सोर्स कोड (सिर्फ़ कॉल ग्राफ़ नहीं) के विरुद्ध दोबारा सत्यापित। नीचे <a href="#decouple-risk-scored-extract-class-candidates">Decouple: जोखिम-स्कोर वाले Extract-Class उम्मीदवार</a> देखें।
</p>

<div align="center">
<details><summary><b>इसे अन्य भाषाओं में पढ़ें</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>सार्वजनिक v1 लॉन्च से पहले graphify प्लेटफ़ॉर्म तक अर्ली एक्सेस खुला है: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

अपने AI कोडिंग असिस्टेंट में `/graphify` टाइप करें और यह आपके पूरे प्रोजेक्ट (कोड, दस्तावेज़, PDF, इमेज, वीडियो) को एक **नॉलेज ग्राफ़** में मैप कर देगा जिसे आप फ़ाइलों में grep करने के बजाय **क्वेरी** कर सकते हैं।

- **कोड मैपिंग मुफ़्त, पूरी तरह लोकल।** कोड को tree-sitter AST से पार्स किया जाता है: नियतात्मक, बिना LLM के, कुछ भी आपकी मशीन से बाहर नहीं जाता। (दस्तावेज़, PDF, इमेज और वीडियो एक सिमैंटिक पास के लिए आपके असिस्टेंट के मॉडल, या एक कॉन्फ़िगर की गई API key का उपयोग करते हैं।)
- **हर एज समझाई जाती है।** हर कनेक्शन को `EXTRACTED` (सोर्स में स्पष्ट) या `INFERRED` (graphify द्वारा निकाला गया) टैग किया जाता है, ताकि आप बता सकें कि क्या सीधे पढ़ा गया और क्या अनुमानित किया गया।
- **यह वेक्टर इंडेक्स नहीं है।** कोई embeddings नहीं, कोई vector store नहीं: एक असली ग्राफ़ जिसे आप ट्रैवर्स करते हैं। एक सवाल पूछें, दो चीज़ों के बीच का रास्ता ट्रेस करें, या एक कॉन्सेप्ट समझाएँ।

> क्या आप चाहते हैं कि यह हमेशा चालू रहे, केवल माँग पर नहीं बल्कि आपके कोड, दस्तावेज़ों और मीटिंग्स में बैकग्राउंड में अपडेट होता रहे? यही हम **[graphify.com](https://graphify.com)** पर बना रहे हैं, और अर्ली एक्सेस अभी **[app.graphify.com](https://app.graphify.com/login)** पर खुला है।

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="graphify's interactive graph.html showing the FastAPI codebase as a force-directed knowledge graph with a legend of detected communities" width="900">
</p>
<p align="center">
  <em>graphify द्वारा मैप किया गया FastAPI कोडबेस। हर नोड एक कॉन्सेप्ट है, रंग पहचानी गई कम्युनिटीज़ हैं, और पूरी चीज़ graph.html में क्लिक करने योग्य है।</em>
</p>

**शुरू करें** (30 सेकंड):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

फिर, अपने AI असिस्टेंट में:

```
/graphify .
```

बस इतना ही। आपको **तीन फ़ाइलें** मिलती हैं:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**यह काम करता है** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, और 15+ अन्य में — [अपना प्लेटफ़ॉर्म चुनें](#install)।

---

## इसे काम करते देखें

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="graphify path query: a terminal asks for the shortest path between FastAPI and ModelField, and the answer lights up hop by hop across the knowledge graph" width="900">
</p>

एक बार ग्राफ़ बन जाने के बाद आप फ़ाइलें पढ़ने के बजाय उससे क्वेरी करते हैं। ऊपर दिखाए गए FastAPI कोडबेस पर चलाया गया असली आउटपुट:

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

हर एज एक **कॉन्फ़िडेंस टैग** रखती है (`EXTRACTED` = सोर्स में स्पष्ट, `INFERRED` = रिज़ॉल्यूशन से निकाला गया), ताकि आप बता सकें कि क्या सीधे पढ़ा गया और क्या अनुमानित किया गया। `graphify query "<question>"` एक सामान्य भाषा के सवाल के लिए एक सीमित सबग्राफ़ लौटाता है, और `graphify path A B` ट्रेस करता है कि कोई भी दो चीज़ें कैसे जुड़ी हैं।

---

## Decouple: जोखिम-स्कोर वाले Extract-Class उम्मीदवार

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: MainWindow god node splitting into risk-scored candidate classes, with a shared-state warning between two of them" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: MainWindow's 5 proposed classes, Node Info panel open on Main Window Axis and Range Controls showing a 0.608 state overlap with Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>एक असली रन पर DECOUPLE.html — किसी प्रस्तावित क्लास पर क्लिक करने से ठीक-ठीक दिखता है कि वह किस दूसरी क्लास के साथ स्टेट शेयर करती है, और क्या विशेष रूप से शेयर होता है।</em>
</p>

यही पेज विभाजन को भी दिखाता है। **Preview decoupled view** को टॉगल करने से god क्लास के अपने मेथड्स को प्रस्तावित क्लासेस से बदल दिया जाता है और एजेज़ को उसी जगह फिर से रूट किया जाता है — यह वायरिंग में बदलाव है, कोई दोबारा बनाया गया डायग्राम नहीं:

| पहले — आज की god क्लास | बाद में — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html before the toggle: a single MainWindow hub node with its own methods fanned out around it" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html after the toggle: the same node reduced to 5 diamond-shaped proposed classes, green dashed edges showing which methods were extracted into each, red edges showing shared instance state between two of them" width="440"> |
| एक नोड जिसमें अपने 47 मेथड्स हैं, जिनमें से हर एक केवल क्लास के ज़रिए ही पहुँचा जा सकता है। | प्रस्तावित क्लासेस। हरा डैश्ड = किसमें क्या निकाला गया; लाल = वह इंस्टेंस स्टेट जो दो क्लासेस अभी भी शेयर करती हैं, जो ठीक यही तय करता है कि `split` हो या `keep_as_is`। केवल वही उम्मीदवार बनाए जाते हैं जो जोखिम सीमा पार करते हैं — यहाँ 6 में से 5, इसीलिए एक मेथड के पास उतरने के लिए कोई डायमंड नहीं है। |

`graphify decouple` god objects खोजता है और बताता है कि क्या उन्हें विभाजित करना वाकई फ़ायदेमंद है — सिर्फ़ यह नहीं कि वे बड़े हैं।

यह जिस विफलता को पकड़ने के लिए बना है: 47 मेथड्स वाली एक क्लास जिसे कॉल-ग्राफ़ क्लस्टरिंग खुशी-खुशी 5 साफ़-सुथरी दिखने वाली ग्रुप्स में बाँट देती है, जिनमें से सभी अभी भी ठीक वही `self._chart_style` / `self._crosshair` इंस्टेंस स्टेट पढ़ती और लिखती हैं। अगर आप वह विभाजन शिप करते हैं तो आपने कुछ भी decouple नहीं किया — आपने बस मेथड्स को नई फ़ाइलों में ले जाया है जो अभी भी स्वतंत्र रूप से टेस्ट, बदली या समझी नहीं जा सकतीं, क्योंकि उन सभी को अभी भी वही शेयर्ड स्टेट वापस पास किए जाने की ज़रूरत है। सिर्फ़ कॉल ग्राफ़ देखने वाला टूल इसे बिल्कुल नहीं देख सकता; इसे असली सोर्स पर वापस जाना ही होगा।

**दो जाँचें, दोनों बिना LLM, दोनों नियतात्मक:**

1. **क्या यह वाकई एक God Object है?** उच्च डिग्री वाला नोड एक असली God Object हो सकता है (कई अपने खुद के मेथड्स, असंबंधित ज़िम्मेदारियों में फैले हुए — Extract Class लागू होता है) या एक अत्यधिक-संदर्भित हब/डेटा मॉडल (कम अपने मेथड्स, ज़्यादातर *इनकमिंग* संदर्भ — इसके शरीर को विभाजित करने से कुछ नहीं होता; समाधान है इसके इंटरफ़ेस को संकीर्ण करना, क्लास निकालना नहीं)। `classify_god_node` इन्हें `member_ratio` से अलग करता है, कच्ची डिग्री से नहीं — वह अंतर जो `TraceSource` (84 एजेज़, लेकिन केवल 6 अपने मेथड्स) को एक झूठा विभाजन सुझाव मिलने से रोकता है जो `MainWindow` (88 एजेज़, 47 अपने मेथड्स) को सही तरीके से मिलता है।
2. **क्या विभाजन वाकई कपलिंग कम करेगा?** `risk_before` (god नोड का वर्तमान आकार/कपलिंग/फ़्रैगमेंटेशन) की तुलना `risk_after` से की जाती है — वह नया जोखिम जो खुद विभाजन पेश करेगा: क्रॉस-ग्रुप कॉल्स जो अदृश्य इंट्रा-क्लास एजेज़ थीं और स्पष्ट इंटर-क्लास डिपेंडेंसीज़ बन जाती हैं, कॉलर्स जिन्हें अब एक से अधिक नई क्लास पर निर्भर होना पड़ेगा, और — वह जाँच जो एक कॉल ग्राफ़ संरचनात्मक रूप से नहीं कर सकता — प्रस्तावित ग्रुप्स में वाकई कितना `self`/`this` इंस्टेंस स्टेट (रीड्स, राइट्स, और शेयर्ड हेल्पर-मेथड कॉल्स, अलग-अलग वेटेज के साथ: एक शेयर्ड **राइट** एक शेयर्ड रीड से ऊँचा स्कोर करता है) कॉमन है। यह सीधे tree-sitter से god नोड की अपनी सोर्स फ़ाइल को दोबारा पार्स करता है; यह graphify के अपने निकाले गए ग्राफ़ पर निर्भर नहीं करता, जो किसी भी भाषा के लिए फ़ील्ड-लेवल एक्सेस कभी रिकॉर्ड नहीं करता। केवल जब `risk_after` `risk_before` से नीचे एक सीमा पार करता है तब प्लान `split` की सिफ़ारिश करता है — अन्यथा यह `marginal` या `keep_as_is` है, और एक हतोत्साहित उम्मीदवार को एक संख्या के रूप में रिपोर्ट किया जाता है, कभी भी ऐसे आकार के रूप में नहीं जिसे आपको आँख से अनुमान लगाना पड़े।

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

`graph.json` के बगल में तीन फ़ाइलें आउटपुट करता है:

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

**स्टेट-शेयरिंग जाँच के लिए भाषा कवरेज** (ऊपर दिया गया सिर्फ़-कॉल-ग्राफ़ वर्गीकरण उन सभी भाषाओं के लिए काम करता है जिन्हें graphify निकालता है; यह टेबल विशेष रूप से उस सोर्स री-पार्स के बारे में है जो `self`/`this` स्टेट ओवरलैप को सत्यापित करता है):

| भाषा | समर्थित | नोट्स |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` अपना खुद का AST नोड है, कोई रैप्ड फ़ील्ड एक्सेस नहीं — स्पष्ट रूप से हैंडल किया गया |
| C# | ✅ | |
| Rust | ✅ | `impl` ब्लॉक्स के ज़रिए `self.x` |
| Ruby | ✅ | `@x` (प्रमुख मुहावरा) + `self.foo` कॉल्स |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | प्रति-मेथड रिसीवर रिज़ॉल्यूशन — Go में कोई `self`/`this` कीवर्ड नहीं है, इसलिए रिसीवर नाम (`func (f *Foo) M()` में `f`) हर मेथड के लिए ताज़ा रिज़ॉल्व किया जाता है |
| C | ❌ | एक struct-pointer पैरामीटर के पास कोई सिंटैक्टिक मार्कर नहीं है जो इसे किसी अन्य पैरामीटर से अलग करे — पूर्ण टाइप इनफ़रेंस के बिना कोई भरोसेमंद संकेत नहीं |

एक असमर्थित भाषा में god नोड, या जिसका सोर्स पढ़ा नहीं जा सकता, उसे `state_analysis: "skipped"` चिह्नित किया जाता है — वर्गीकरण और कॉल-ग्राफ़ स्कोर अभी भी चलते हैं, लेकिन सिफ़ारिश केवल कॉल ग्राफ़ पर टिकी होती है बजाय चुपचाप यह मान लेने के कि स्टेट जाँच पास हो गई।

---

## यह क्या करता है

बॉक्स से बाहर आपको क्या मिलता है:

| क्षमता | आपको क्या मिलता है |
|---|---|
| **God nodes** | सबसे ज़्यादा जुड़े हुए कॉन्सेप्ट्स, ताकि आप देख सकें कि सब कुछ कहाँ से होकर बहता है |
| **कम्युनिटीज़** | ग्राफ़ उप-सिस्टम्स में विभाजित (Leiden), बिना LLM के लेबल्स के साथ |
| **क्रॉस-फ़ाइल लिंक्स** | `calls` / `imports` / `inherits` / `mixes_in` को tree-sitter AST के ज़रिए ~40 भाषाओं में रिज़ॉल्व किया गया |
| **क्वेरी, पाथ, एक्सप्लेन** | एक सवाल पूछें, दो चीज़ों के बीच का रास्ता ट्रेस करें, या एक कॉन्सेप्ट समझाएँ, सब कुछ `graph.json` के विरुद्ध |
| **कारण + दस्तावेज़ संदर्भ** | `# NOTE:` / `# WHY:` टिप्पणियाँ और ADR/RFC उद्धरण कोड से जुड़े प्रथम-श्रेणी नोड्स बन जाते हैं |
| **कोड से आगे** | दस्तावेज़, PDF, इमेज, और वीडियो/ऑडियो सभी एक ही ग्राफ़ में मैप होते हैं |
| **लोकल-फ़र्स्ट** | कोड को tree-sitter के साथ लोकली पार्स किया जाता है (बिना LLM, कुछ भी आपकी मशीन से बाहर नहीं जाता); केवल दस्तावेज़ों/मीडिया पर सिमैंटिक पास एक बैकएंड को कॉल करता है, और केवल अगर आप एक कॉन्फ़िगर करें |

---

## बेंचमार्क्स

| बेंचमार्क | मेट्रिक | graphify | फ़ील्ड |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | QA सटीकता | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | QA सटीकता | **76%** | dense RAG के बराबर |
| ग्राफ़ बिल्ड | LLM क्रेडिट | **0** | अधिकतर सिस्टम्स के लिए प्रति-टोकन |

हर सिस्टम एक ही हार्नेस पर एक ही मॉडल और बजट के साथ चला, एक जज द्वारा स्कोर किया गया जो एक दूसरे जज के विरुद्ध ब्लाइंड-वैलिडेटेड था (90.6% सहमति, Cohen's kappa 0.81)। पूरी प्रति-सिस्टम टेबल्स, कोड-इंटेलिजेंस परिणाम, और रीप्रोडक्शन कमांड्स: **[BENCHMARKS.md](./BENCHMARKS.md)**।

---

## पूर्वापेक्षाएँ

| आवश्यकता | न्यूनतम | जाँच | इंस्टॉल |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(अनुशंसित)* | कोई भी | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(विकल्प)* | कोई भी | `pipx --version` | `pip install pipx` |

**macOS त्वरित इंस्टॉल (Homebrew):**
```bash
brew install python@3.12 uv
```

**Windows त्वरित इंस्टॉल:**
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

## इंस्टॉल

> **आधिकारिक पैकेज:** PyPI पैकेज `graphifyy` है (डबल-y)। PyPI पर अन्य `graphify*` पैकेज संबद्ध नहीं हैं। CLI कमांड अभी भी `graphify` है।

**चरण 1 — पैकेज इंस्टॉल करें:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**चरण 2 — अपने AI असिस्टेंट के साथ स्किल रजिस्टर करें:**

```bash
graphify install
```

बस इतना ही। अपना AI असिस्टेंट खोलें और `/graphify .` टाइप करें।

असिस्टेंट स्किल को अपने यूज़र प्रोफ़ाइल के बजाय वर्तमान रिपॉज़िटरी में इंस्टॉल करने के लिए, `--project` जोड़ें:

```bash
graphify install --project
graphify install --project --platform codex
```

प्रोजेक्ट-स्कोप्ड इंस्टॉल्स वर्तमान डायरेक्टरी के अंतर्गत लिखते हैं, उदाहरण के लिए `.claude/skills/graphify/SKILL.md` या `.agents/skills/graphify/SKILL.md` (साथ ही एक `references/` साइडकार जिसे स्किल माँग पर लोड करती है), और कमिट किए जा सकने वाली फ़ाइलों के लिए एक `git add` संकेत प्रिंट करते हैं। प्रोजेक्ट-स्कोप्ड इंस्टॉल्स का समर्थन करने वाले प्रति-प्लेटफ़ॉर्म कमांड्स वही फ़्लैग स्वीकार करते हैं, उदाहरण के लिए `graphify claude install --project` या `graphify codex install --project`।

> **PowerShell नोट:** `graphify .` का उपयोग करें `/graphify .` नहीं — शुरुआती स्लैश PowerShell में एक पाथ सेपरेटर है।

> **`graphify: command not found`?** `uv tool install` / `pipx install` `graphify` कमांड को अपने टूल bin डायरेक्टरी (`~/.local/bin`) में डालते हैं। अगर आपका शेल इंस्टॉल के तुरंत बाद इसे नहीं ढूँढ पाता — एक फ़्रेश macOS + zsh सेटअप पर आम — वह डायरेक्टरी अभी तक आपके `PATH` में नहीं है: `uv tool update-shell` (या `pipx ensurepath`) चलाएँ, फिर एक नया टर्मिनल खोलें। सादे `pip` के साथ, अपने PATH में `~/.local/bin` (Linux) या `~/Library/Python/3.x/bin` (Mac) जोड़ें, या `python -m graphify` चलाएँ।

> **इंस्टॉल करने के बजाय `uvx` / `uv tool run` से चला रहे हैं?** पैकेज का नाम लें, कमांड का नहीं: `uvx --from graphifyy graphify install`। सादा `uvx graphify …` विफल होता है (`No solution found … no versions of graphify`) क्योंकि `uv tool run` पहले शब्द को एक *पैकेज* के रूप में पढ़ता है, और पैकेज है `graphifyy` — `graphify` कमांड इसके अंदर रहता है।

> **Mac/Windows पर `pip install` से बचें** अगर संभव हो। स्किल रनटाइम पर `graphify-out/.graphify_python` से Python रिज़ॉल्व करती है; अगर यह एक अलग एनवायरनमेंट की ओर इशारा करता है जहाँ `pip` ने पैकेज इंस्टॉल किया, तो आपको `ModuleNotFoundError: No module named 'graphify'` मिलेगा। `uv tool install` और `pipx install` पैकेज को अपने खुद के एनवायरनमेंट में अलग करते हैं और इसे पूरी तरह टालते हैं।

> **Git hooks और uv tool / pipx:** `graphify hook install` इंस्टॉल के समय हुक स्क्रिप्ट्स में सीधे वर्तमान इंटरप्रेटर पाथ को एम्बेड करता है, ताकि post-commit हुक GUI git क्लाइंट्स और CI runners में भी सही तरीके से फ़ायर हो जहाँ `~/.local/bin` PATH पर नहीं है। अगर आप graphify को फिर से इंस्टॉल या अपग्रेड करते हैं, तो एम्बेडेड पाथ को रीफ़्रेश करने के लिए `graphify hook install` फिर से चलाएँ।

> **स्ट्रिक्ट मोड (Claude Code):** `graphify install --project --strict` असिस्टेंट को वाकई ग्राफ़ का उपयोग करने पर मजबूर करता है। डिफ़ॉल्ट इंस्टॉल फ़ाइलें पढ़ने से पहले `graphify query` चलाने के लिए *नज करता है*; स्ट्रिक्ट मोड सेशन के पहले रॉ सोर्स रीड को *ब्लॉक करता है* और उसे ग्राफ़ की ओर रीडायरेक्ट करता है, फिर नज पर वापस आ जाता है (ताकि यह प्रति सेशन ज़्यादा से ज़्यादा एक बार फ़ायर हो और कभी अटके नहीं)। रनटाइम पर `GRAPHIFY_HOOK_STRICT=1`/`0` से टॉगल करें; डिफ़ॉल्ट इंस्टॉल अपरिवर्तित रहता है (सॉफ़्ट नज)।

<details>
<summary><b>अपना प्लेटफ़ॉर्म चुनें</b> (20+ असिस्टेंट्स, विस्तार के लिए क्लिक करें)</summary>

| प्लेटफ़ॉर्म | इंस्टॉल कमांड |
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

Codex यूज़र्स को समानांतर निष्कर्षण के लिए `~/.codex/config.toml` में `[features]` के तहत `multi_agent = true` की भी ज़रूरत है। CodeBuddy Claude Code जैसा ही Agent tool और PreToolUse हुक मैकेनिज़्म इस्तेमाल करता है। Factory Droid समानांतर सबएजेंट डिस्पैच के लिए `Task` टूल इस्तेमाल करता है। OpenClaw और Aider क्रमिक निष्कर्षण इस्तेमाल करते हैं (इन प्लेटफ़ॉर्म्स पर समानांतर एजेंट समर्थन अभी शुरुआती है)। Trae समानांतर सबएजेंट डिस्पैच के लिए Agent tool इस्तेमाल करता है और `PreToolUse` हुक्स **का** समर्थन नहीं करता, इसलिए AGENTS.md हमेशा-चालू मैकेनिज़्म है।

`--platform agents` (उपनाम `--platform skills`) सामान्य क्रॉस-फ़्रेमवर्क [Agent-Skills](https://github.com/anthropics/skills) स्थानों को लक्षित करता है: स्पेक का यूज़र-ग्लोबल `~/.agents/skills/` (जिसे `npx skills` और स्पेक-अनुरूप फ़्रेमवर्क्स पढ़ते हैं) एक ग्लोबल इंस्टॉल के लिए, और `./.agents/skills/` एक प्रोजेक्ट (`--project`) इंस्टॉल के लिए। सादा `graphify install` डिज़ाइन के अनुसार सिंगल-प्लेटफ़ॉर्म (Claude Code) रहता है — नामित `agents` प्लेटफ़ॉर्म का उपयोग करें जब आप चाहें कि स्किल किसी भी फ़्रेमवर्क द्वारा खोजी जा सके जो `.agents/skills` पढ़ता है।

> Codex `/graphify` के बजाय `$graphify` इस्तेमाल करता है।

</details>

<details>
<summary><b>वैकल्पिक extras</b> (केवल वही इंस्टॉल करें जो आपको चाहिए)</summary>

| Extra | यह क्या जोड़ता है | इंस्टॉल |
|---|---|---|
| `pdf` | PDF निष्कर्षण | `uv tool install "graphifyy[pdf]"` |
| `office` | `.docx` और `.xlsx` समर्थन | `uv tool install "graphifyy[office]"` |
| `google` | Google Sheets रेंडरिंग | `uv tool install "graphifyy[google]"` |
| `video` | वीडियो/ऑडियो ट्रांसक्रिप्शन (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | MCP stdio सर्वर | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Neo4j push समर्थन | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | FalkorDB push समर्थन | `uv tool install "graphifyy[falkordb]"` |
| `svg` | SVG ग्राफ़ एक्सपोर्ट | `uv tool install "graphifyy[svg]"` |
| `leiden` | Leiden कम्युनिटी डिटेक्शन (केवल Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | लोकल Ollama इनफ़रेंस | `uv tool install "graphifyy[ollama]"` |
| `openai` | OpenAI / OpenAI-संगत APIs | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic Claude API (`--backend claude`, `ANTHROPIC_API_KEY` इस्तेमाल करता है) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (IAM इस्तेमाल करता है, कोई API key नहीं) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT` इस्तेमाल करता है) | `uv tool install "graphifyy[openai]"` |
| `sql` | SQL स्कीमा निष्कर्षण | `uv tool install "graphifyy[sql]"` |
| `postgres` | लाइव PostgreSQL इंट्रोस्पेक्शन (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | BYOND DreamMaker `.dm`/`.dme` AST निष्कर्षण (अगर आपके प्लेटफ़ॉर्म से कोई wheel मेल नहीं खाता तो C कंपाइलर + `python3-dev` की ज़रूरत हो सकती है) | `uv tool install "graphifyy[dm]"` |
| `terraform` | Terraform / HCL `.tf`/`.tfvars`/`.hcl` AST निष्कर्षण | `uv tool install "graphifyy[terraform]"` |
| `pascal` | Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` AST निष्कर्षण (अधिक सटीक `calls`/`inherits` एजेज़; अनुपस्थित होने पर regex एक्सट्रैक्टर पर वापस जाता है) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | चाइनीज़ क्वेरी सेगमेंटेशन (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | ऊपर दिया गया सब कुछ | `uv tool install "graphifyy[all]"` |

</details>

---

## अपने असिस्टेंट को हमेशा ग्राफ़ इस्तेमाल करने के लिए बनाएँ

एक ग्राफ़ बनाने के बाद अपने प्रोजेक्ट में इसे एक बार चलाएँ:

| प्लेटफ़ॉर्म | कमांड |
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

यह एक छोटी कॉन्फ़िग फ़ाइल लिखता है जो आपके असिस्टेंट को बताती है कि कोडबेस से जुड़े सवालों के लिए नॉलेज ग्राफ़ से सलाह लें, पूरी रिपोर्ट पढ़ने या रॉ फ़ाइलों में grep करने के बजाय `graphify query "<question>"` जैसी सीमित क्वेरीज़ को प्राथमिकता देते हुए।

- **हुक प्लेटफ़ॉर्म्स** (Claude Code, Gemini CLI): सर्च-स्टाइल टूल कॉल्स से पहले एक हुक अपने आप फ़ायर होता है (और, Claude Code पर, Read/Glob टूल्स के ज़रिए सोर्स फ़ाइलों को एक-एक करके पढ़ने से पहले) और आपके असिस्टेंट को ग्राफ़ पाथ की ओर धकेलता है।
- **इंस्ट्रक्शन-फ़ाइल प्लेटफ़ॉर्म्स** (Codex, OpenCode, Cursor, आदि): स्थायी इंस्ट्रक्शन फ़ाइलें (`AGENTS.md`, `.cursor/rules/`, आदि) वही क्वेरी-फ़र्स्ट गाइडेंस देती हैं।

`GRAPH_REPORT.md` अभी भी व्यापक आर्किटेक्चर समीक्षा के लिए उपलब्ध है।

**CodeBuddy** Claude Code जैसे ही दो काम करता है: एक `CODEBUDDY.md` सेक्शन लिखता है जो CodeBuddy को आर्किटेक्चर सवालों के जवाब देने से पहले `graphify-out/GRAPH_REPORT.md` पढ़ने को कहता है, और `PreToolUse` हुक्स (`.codebuddy/settings.json`) इंस्टॉल करता है जो Bash सर्च कमांड्स और फ़ाइल रीड्स से पहले फ़ायर होते हैं, `graphify query` की ओर धकेलते हुए।

**Codex** `AGENTS.md` में लिखता है, जो इस प्लेटफ़ॉर्म पर हमेशा-चालू ग्राफ़ गाइडेंस को वाकई ले जाता है। `graphify codex install` `.codex/hooks.json` (`graphify hook-check`) में एक `PreToolUse` हुक भी रजिस्टर करता है, लेकिन वह एंट्री जानबूझकर **no-op** है: Codex Desktop `PreToolUse` पर `hookSpecificOutput.additionalContext` को अस्वीकार करता है, इसलिए वहाँ एक नज भेजने से Bash टूल कॉल्स टूट जाएँगे। Claude Code के विपरीत, जहाँ हुक (`graphify hook-guard`) नज करता है, Codex पर हुक फ़ायर होता है और जानबूझकर कुछ नहीं करता, और `AGENTS.md` हमेशा-चालू मैकेनिज़्म है।

**Kilo Code** Graphify स्किल को `~/.config/kilo/skills/graphify/SKILL.md` में और एक नेटिव `/graphify` कमांड को `~/.config/kilo/command/graphify.md` में इंस्टॉल करता है। `graphify kilo install` `AGENTS.md` भी लिखता है साथ ही एक नेटिव `tool.execute.before` प्लगइन (`.kilo/plugins/graphify.js` + `.kilo/kilo.json` या `.kilo/kilo.jsonc` रजिस्ट्रेशन) ताकि Kilo को नेटिव `.kilo` कॉन्फ़िग के ज़रिए वही हमेशा-चालू ग्राफ़ रिमाइंडर व्यवहार मिले।

**Cursor** `.cursor/rules/graphify.mdc` को `alwaysApply: true` के साथ लिखता है, इसलिए Cursor इसे हर बातचीत में अपने आप शामिल करता है, किसी हुक की ज़रूरत नहीं।

graphify को सभी प्लेटफ़ॉर्म्स से एक साथ हटाने के लिए: `graphify uninstall` (`graphify-out/` को भी डिलीट करने के लिए `--purge` जोड़ें)। या प्रति-प्लेटफ़ॉर्म कमांड इस्तेमाल करें (जैसे `graphify claude uninstall`)।

---

## रिपोर्ट में क्या है

- **God nodes** — आपके प्रोजेक्ट में सबसे ज़्यादा जुड़े हुए कॉन्सेप्ट्स। सब कुछ इनसे होकर बहता है।
- **आश्चर्यजनक कनेक्शन्स** — अलग-अलग फ़ाइलों या मॉड्यूल्स में रहने वाली चीज़ों के बीच लिंक्स। वे कितने अप्रत्याशित हैं, इसके हिसाब से रैंक किए गए।
- **"क्यों"** — इनलाइन टिप्पणियाँ (`# NOTE:`, `# WHY:`, `# HACK:`), docstrings, और दस्तावेज़ों से डिज़ाइन तर्क अलग नोड्स के रूप में निकाले जाते हैं जो उस कोड से जुड़े होते हैं जिसे वे समझाते हैं।
- **सुझाए गए सवाल** — 4–5 सवाल जिनका जवाब देने के लिए ग्राफ़ विशिष्ट रूप से तैयार है।
- **कॉन्फ़िडेंस टैग्स** — हर अनुमानित संबंध को `EXTRACTED`, `INFERRED`, या `AMBIGUOUS` चिह्नित किया जाता है। आप हमेशा जानते हैं कि क्या पाया गया बनाम क्या अनुमान लगाया गया।

---

## यह किन फ़ाइलों को हैंडल करता है

| प्रकार | एक्सटेंशन |
|------|-----------|
| कोड (36 tree-sitter ग्रामर्स) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme` के लिए `uv tool install graphifyy[dm]` चाहिए; `.mts`/`.cts` TypeScript ग्रामर दोबारा इस्तेमाल करते हैं, `.cc`/`.cxx` और CUDA `.cu`/`.cuh` और Metal `.metal` C++ ग्रामर दोबारा इस्तेमाल करते हैं) |
| Salesforce Apex | `.cls .trigger` (regex-आधारित; क्लासेस, इंटरफ़ेसेस, enums, मेथड्स, ट्रिगर्स, SOQL/DML एजेज़) |
| Terraform / HCL | `.tf .tfvars .hcl` (`uv tool install graphifyy[terraform]` चाहिए) |
| MCP कॉन्फ़िग्स | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — सर्वर नोड्स, पैकेज संदर्भ, env var आवश्यकताएँ निकालता है |
| पैकेज मैनिफ़ेस्ट्स | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — प्रति पैकेज एक कैननिकल पैकेज नोड (नाम से) साथ ही `depends_on` एजेज़, ताकि कई मैनिफ़ेस्ट्स से संदर्भित पैकेज एक ही हब हो |
| दस्तावेज़ | `.md .mdx .qmd .html .txt .rst .yaml .yml` (markdown `[text](./other.md)` लिंक्स और `[[wikilinks]]` दस्तावेज़ों के बीच `references` एजेज़ बन जाते हैं) |
| Office | `.docx .xlsx` (`uv tool install graphifyy[office]` चाहिए) |
| Google Workspace | `.gdoc .gsheet .gslides` (opt-in; `gws` ऑथ और `--google-workspace` चाहिए; Sheets के लिए `uv tool install graphifyy[google]` चाहिए) |
| PDF | `.pdf` |
| इमेजेज़ | `.png .jpg .webp .gif` |
| वीडियो / ऑडियो | `.mp4 .mov .mp3 .wav` और अधिक (`uv tool install graphifyy[video]` चाहिए) |
| YouTube / URLs | कोई भी वीडियो URL (`uv tool install graphifyy[video]` चाहिए) |

कोड **बिना API कॉल्स के लोकली** निकाला जाता है (tree-sitter के ज़रिए AST)। बाकी सब कुछ आपके AI असिस्टेंट के मॉडल API से होकर गुज़रता है।

Google Drive for desktop की `.gdoc`, `.gsheet`, और `.gslides` फ़ाइलें शॉर्टकट पॉइंटर्स हैं, दस्तावेज़ कंटेंट नहीं। एक headless निष्कर्षण में नेटिव Google Docs, Sheets, और Slides शामिल करने के लिए, [`gws` CLI](https://github.com/googleworkspace/cli) इंस्टॉल और ऑथेंटिकेट करें, फिर चलाएँ:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

आप `GRAPHIFY_GOOGLE_WORKSPACE=1` भी सेट कर सकते हैं। Graphify शॉर्टकट्स को `graphify-out/converted/` में Markdown साइडकार्स के रूप में एक्सपोर्ट करता है, फिर उन फ़ाइलों को निकालता है।

---

## आम कमांड्स

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

ऊपर [Decouple: जोखिम-स्कोर वाले Extract-Class उम्मीदवार](#decouple-risk-scored-extract-class-candidates) देखें, या नीचे [पूरा कमांड संदर्भ](#full-command-reference)।

---

## फ़ाइलों को अनदेखा करना

अपने प्रोजेक्ट रूट में एक `.graphifyignore` बनाएँ — `.gitignore` जैसा ही सिंटैक्स, `!` नेगेशन सहित।

**`.gitignore` को अपने आप सम्मानित किया जाता है।** graphify हर डायरेक्टरी में `.gitignore` पढ़ता है। अगर एक `.graphifyignore` भी मौजूद है, तो दोनों **मर्ज** हो जाते हैं — `.graphifyignore` पैटर्न्स आख़िर में मूल्यांकित होते हैं, इसलिए वे संघर्षों में जीतते हैं (`!` नेगेशन्स सहित)। एक `.graphifyignore` जोड़ना केवल और अधिक बाहर करता है; यह कभी भी उस फ़ाइल को फिर से शामिल नहीं करता जिसे आपका `.gitignore` पहले ही बाहर कर चुका है। सब-डायरेक्टरी स्कोपिंग git जैसे ही काम करती है — एक ignore फ़ाइल केवल अपने खुद के सबट्री को प्रभावित करती है।

`graphify extract` को `--no-gitignore` पास करें जब git-ignored जनरेट या ट्रांसपाइल किया गया कोड ग्राफ़ में शामिल होना चाहिए। यह `.gitignore` और `.git/info/exclude` को अक्षम करता है; `.graphifyignore` अभी भी लागू होता है।

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

## टीम सेटअप

`graphify-out/` को git में कमिट किया जाना चाहिए ताकि टीम में हर कोई एक मैप के साथ शुरू करे।

**अनुशंसित `.gitignore` जोड़ें:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` अब पोर्टेबल है — keys को सापेक्ष पाथ के रूप में स्टोर किया जाता है और लोड पर फिर से एंकर किया जाता है, इसलिए इसे कमिट करना सुरक्षित है और पहले checkout पर पूरी रीबिल्ड से बचाता है।

**वर्कफ़्लो:**
1. एक व्यक्ति `/graphify .` चलाता है और `graphify-out/` कमिट करता है।
2. हर कोई pull करता है — उनका असिस्टेंट तुरंत ग्राफ़ पढ़ता है।
3. हर कमिट के बाद अपने आप रीबिल्ड करने के लिए `graphify hook install` चलाएँ (केवल AST, कोई API लागत नहीं)। यह एक git merge driver भी सेट करता है ताकि `graph.json` कभी भी कॉन्फ़्लिक्ट मार्कर्स के साथ न रह जाए — समानांतर कमिट करने वाले दो डेवलपर्स को उनके ग्राफ़ अपने आप यूनियन-मर्ज्ड मिलते हैं।
4. जब दस्तावेज़ या पेपर्स बदलते हैं, उन नोड्स को ताज़ा करने के लिए `/graphify --update` चलाएँ।

---

## ग्राफ़ को सीधे इस्तेमाल करना

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

MCP सर्वर आपके असिस्टेंट को संरचित एक्सेस देता है: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`।

### शेयर्ड HTTP सर्वर

`--transport stdio` (डिफ़ॉल्ट) प्रति डेवलपर एक लोकल सर्वर स्पॉन करता है। `--transport http` वही टूल्स MCP Streamable HTTP transport पर सर्व करता है, ताकि एक ही शेयर्ड प्रोसेस पूरी टीम के लिए ग्राफ़ सर्व कर सके — क्लाइंट्स अपने IDE MCP कॉन्फ़िग को लोकली graphify चलाने के बजाय `http://<host>:8080/mcp` की ओर इंगित करते हैं।

| फ़्लैग | डिफ़ॉल्ट | उद्देश्य |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | सर्व करने के लिए ट्रांसपोर्ट |
| `--host` | `127.0.0.1` | HTTP बाइंड होस्ट (localhost से आगे एक्सपोज़ करने के लिए `0.0.0.0` इस्तेमाल करें) |
| `--port` | `8080` | HTTP बाइंड पोर्ट |
| `--api-key` | env `GRAPHIFY_API_KEY` | `Authorization: Bearer <key>` (या `X-API-Key`) की ज़रूरत |
| `--path` | `/mcp` | HTTP माउंट पाथ |
| `--json-response` | off | SSE स्ट्रीम्स के बजाय सादा JSON लौटाता है |
| `--stateless` | off | प्रति-सेशन कोई स्टेट नहीं (load-balanced / CI डिप्लॉयमेंट्स के लिए) |
| `--session-timeout` | `3600` | N सेकंड बाद निष्क्रिय stateful सेशन्स को रीप करता है (`0` अक्षम करता है) |

डिफ़ॉल्ट `127.0.0.1` बाइंड केवल loopback है। शेयर्ड होस्ट पर एक्सपोज़ करते समय `--host 0.0.0.0` **और** `--api-key` दोनों साथ सेट करें। इसे एक कंटेनर में चलाएँ:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **WSL / Linux नोट:** Ubuntu `python3` देता है, `python` नहीं। संघर्षों से बचने के लिए एक venv इस्तेमाल करें:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## एनवायरनमेंट वेरिएबल्स

ये केवल **headless / CI निष्कर्षण** (`graphify extract`) के लिए ज़रूरी हैं। जब अपने IDE के अंदर `/graphify` स्किल के ज़रिए चलाया जाए, तो मॉडल API आपके IDE सेशन द्वारा दिया जाता है — कोई अतिरिक्त keys की ज़रूरत नहीं।

| वेरिएबल | किसके लिए इस्तेमाल | कब ज़रूरी |
|---|---|---|
| `ANTHROPIC_API_KEY` | Claude (Anthropic) बैकएंड | `--backend claude` |
| `ANTHROPIC_BASE_URL` | Anthropic-संगत endpoint URL (LiteLLM proxy, gateways, ...) | `--backend claude` (डिफ़ॉल्ट: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Claude बैकएंड के लिए मॉडल नाम — कस्टम endpoints के लिए, वह मॉडल नाम/उपनाम इस्तेमाल करें जो आपका सर्वर एक्सपोज़ करता है | `--backend claude` (डिफ़ॉल्ट: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` या `GOOGLE_API_KEY` | Google Gemini बैकएंड | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI या OpenAI-संगत APIs | `--backend openai` (लोकल सर्वर्स कोई भी गैर-खाली वैल्यू स्वीकार करते हैं) |
| `OPENAI_BASE_URL` | OpenAI-संगत सर्वर URL (llama.cpp, vLLM, LM Studio, ...) | `--backend openai` (डिफ़ॉल्ट: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | OpenAI बैकएंड के लिए मॉडल नाम — self-hosted सर्वर्स के लिए, वह मॉडल नाम/उपनाम इस्तेमाल करें जो आपका सर्वर एक्सपोज़ करता है (इसका `/v1/models` endpoint चेक करें), जैसे llama.cpp के लिए `LFM2.5-8B-A1B-UD-Q4_K_XL` | `--backend openai` (डिफ़ॉल्ट: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | DeepSeek बैकएंड | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Kimi Code बैकएंड | `--backend kimi` |
| `OLLAMA_BASE_URL` | लोकल Ollama इनफ़रेंस URL | `--backend ollama` (डिफ़ॉल्ट: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Ollama मॉडल नाम | `--backend ollama` (डिफ़ॉल्ट: ऑटो-डिटेक्ट) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Ollama KV-cache विंडो साइज़ को ओवरराइड करता है | वैकल्पिक — डिफ़ॉल्ट रूप से ऑटो-साइज़्ड |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | लोड किए गए Ollama मॉडल को रखने के मिनट | वैकल्पिक — हर चंक के बाद अनलोड करने के लिए `0` सेट करें |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI Service बैकएंड | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | Azure रिसोर्स endpoint URL | `--backend azure` (API key के साथ ज़रूरी) |
| `AZURE_OPENAI_API_VERSION` | Azure API वर्शन ओवरराइड | वैकल्पिक — डिफ़ॉल्ट `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` या `GRAPHIFY_AZURE_MODEL` | Azure deployment नाम | वैकल्पिक — डिफ़ॉल्ट `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — मानक क्रेडेंशियल चेन | `--backend bedrock` (कोई API key नहीं, IAM इस्तेमाल करता है) |
| `GRAPHIFY_MAX_WORKERS` | AST समानांतरता थ्रेड काउंट | वैकल्पिक — `--max-workers` फ़्लैग भी |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | घने कॉर्पस के लिए आउटपुट कैप बढ़ाएँ | वैकल्पिक — जैसे बड़ी फ़ाइलों के लिए `32768` |
| `GRAPHIFY_API_TIMEOUT` | HTTP, claude-cli, Anthropic SDK, और Bedrock बैकएंड्स के लिए प्रति-कॉल टाइमआउट सेकंड में (डिफ़ॉल्ट: 600) | वैकल्पिक — `--api-timeout` फ़्लैग भी |
| `GRAPHIFY_MAX_RETRIES` | हार मानने से पहले rate-limited (429) रिक्वेस्ट को कितनी बार दोबारा कोशिश करनी है (डिफ़ॉल्ट: 6; `Retry-After` का सम्मान करता है) | वैकल्पिक — सख़्त प्रति-संगठन सीमाओं के लिए बढ़ाएँ (जैसे kimi); `0` अक्षम करता है |
| `GRAPHIFY_FORCE` | कम नोड्स के साथ भी ग्राफ़ रीबिल्ड को मजबूर करें | वैकल्पिक — `--force` फ़्लैग भी |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Google Workspace एक्सपोर्ट को ऑटो-इनेबल करें | वैकल्पिक — `1` पर सेट करें |
| `GRAPHIFY_TRIAGE_BACKEND` | `graphify prs --triage` के लिए बैकएंड | वैकल्पिक — उपलब्ध keys से ऑटो-डिटेक्टेड |
| `GRAPHIFY_TRIAGE_MODEL` | triage के लिए मॉडल ओवरराइड | वैकल्पिक — जैसे `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | `~/.cache/graphify-queries.log` पर लोकल query log ऑन करने के लिए `1` सेट करें (हर query/path/explain सवाल + कॉर्पस पाथ रिकॉर्ड करता है)। डिफ़ॉल्ट रूप से बंद — जब तक आप opt in न करें, कुछ नहीं लिखा जाता (#1797) | वैकल्पिक |
| `GRAPHIFY_QUERY_LOG` | query log ऑन करता है और इसे डिफ़ॉल्ट के बजाय इस पाथ पर लिखता है | वैकल्पिक — बंद जब तक यह या `_ENABLE` सेट न हो |
| `GRAPHIFY_QUERY_LOG_DISABLE` | query log को मजबूरन बंद करने के लिए `1` सेट करें (enable vars पर जीतता है) | वैकल्पिक |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | जब log ऑन हो, पूरे सबग्राफ़ रिस्पॉन्सेज़ भी रिकॉर्ड करता है (डिफ़ॉल्ट रूप से बंद) | वैकल्पिक |
| `GRAPHIFY_MAX_GRAPH_BYTES` | graph.json के 512 MiB साइज़ कैप को ओवरराइड करें — जैसे `700MB`, `2GB`, या सादे bytes | वैकल्पिक — बहुत बड़े कॉर्पस के लिए उपयोगी |
| `GRAPHIFY_MAX_CONTEXTS` | एक multi-project MCP सर्वर द्वारा रखे गए गैर-डिफ़ॉल्ट प्रोजेक्ट ग्राफ़्स की अधिकतम संख्या | वैकल्पिक — डिफ़ॉल्ट: `8`; अमान्य वैल्यूज़ `8` इस्तेमाल करती हैं, और `1` से नीचे की वैल्यूज़ `1` इस्तेमाल करती हैं |
| `GRAPHIFY_LLM_TEMPERATURE` | सिमैंटिक निष्कर्षण के लिए LLM टेम्परेचर ओवरराइड करें — जैसे `0.7`, या छोड़ने के लिए `none` | वैकल्पिक — o1/o3/o4/gpt-5 reasoning मॉडल्स के लिए ऑटो-छोड़ा जाता है |

---

## गोपनीयता

- **कोड फ़ाइलें** — tree-sitter के ज़रिए लोकली प्रोसेस की जाती हैं। कुछ भी आपकी मशीन से बाहर नहीं जाता। एक कोड-ओनली कॉर्पस को किसी API key की ज़रूरत नहीं — `graphify extract` पूरी तरह ऑफ़लाइन चलता है। एक मिश्रित रिपॉज़िटरी पर, केवल कोड को इंडेक्स करने और अन्यथा LLM की ज़रूरत वाले दस्तावेज़ों/PDF/इमेज को छोड़ने के लिए `--code-only` जोड़ें।
- **वीडियो / ऑडियो** — faster-whisper के साथ लोकली ट्रांसक्राइब्ड। कुछ भी आपकी मशीन से बाहर नहीं जाता।
- **दस्तावेज़, PDF, इमेजेज़** — सिमैंटिक निष्कर्षण के लिए आपके AI असिस्टेंट को भेजे जाते हैं (`/graphify` स्किल के ज़रिए, आपके IDE सेशन जो भी मॉडल चलाता है उसका उपयोग करते हुए)। Headless `graphify extract` को `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), एक चलती हुई Ollama इंस्टेंस (`OLLAMA_BASE_URL`), मानक प्रोवाइडर चेन के ज़रिए AWS क्रेडेंशियल्स (Bedrock - कोई API key नहीं चाहिए, IAM इस्तेमाल करता है), या `claude` CLI बाइनरी (Claude Code - कोई API key नहीं चाहिए, आपकी Claude सदस्यता इस्तेमाल करता है) की ज़रूरत है। `--dedup-llm` फ़्लैग वही key इस्तेमाल करता है।
- **डेटा निवास** — `graphify extract` अपने आप पता लगाता है कि कौन सा key सेट है इसके आधार पर कौन सा प्रोवाइडर इस्तेमाल करना है (प्राथमिकता: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama)। डेटा निवास आवश्यकताओं वाले कोड के लिए, `--backend ollama` (पूरी तरह लोकल) इस्तेमाल करें या एक स्पष्ट `--backend` फ़्लैग पास करें। Kimi (`MOONSHOT_API_KEY`) चीन में Moonshot AI सर्वर्स की ओर रूट करता है।
- **कोई टेलीमेट्री नहीं**, कोई उपयोग ट्रैकिंग नहीं, कोई एनालिटिक्स नहीं।
- **क्वेरी लॉगिंग** — हर `graphify query`, `graphify path`, `graphify explain`, और MCP `query_graph` कॉल को JSON Lines फ़ॉर्मेट में `~/.cache/graphify-queries.log` पर लॉग किया जाता है (टाइमस्टैम्प, सवाल, कॉर्पस, लौटाए गए नोड्स, अवधि)। पूरे सबग्राफ़ रिस्पॉन्सेज़ डिफ़ॉल्ट रूप से **नहीं** स्टोर किए जाते। opt out करने के लिए `GRAPHIFY_QUERY_LOG_DISABLE=1` सेट करें, या कोड पाथ को अक्षम किए बिना चुप कराने के लिए `GRAPHIFY_QUERY_LOG=/dev/null` सेट करें।

---

## समस्या निवारण

**इंस्टॉल के बाद `graphify: command not found`**
CLI इंस्टॉल है लेकिन इसकी bin डायरेक्टरी आपके शेल के `PATH` में नहीं है। आपने कैसे इंस्टॉल किया उसके हिसाब से फ़िक्स चुनें:
- **uv** (`uv tool install graphifyy`): कमांड uv के टूल bin डायरेक्टरी (`~/.local/bin`) में जाता है, जो एक फ़्रेश macOS/zsh सेटअप में अक्सर `PATH` में नहीं होता। `uv tool update-shell` चलाएँ, फिर एक नया टर्मिनल खोलें। (`uv tool dir --bin` से डायरेक्टरी ढूँढें।)
- **pipx** (`pipx install graphifyy`): `pipx ensurepath` चलाएँ, फिर एक नया टर्मिनल खोलें।
- **pip** (`pip install graphifyy`): pip स्क्रिप्ट्स को एक यूज़र bin डायरेक्टरी में इंस्टॉल करता है जो `PATH` में नहीं हो सकती — अपने `~/.zshrc`/`~/.bashrc` में `PATH` में `~/Library/Python/3.x/bin` (macOS) या `~/.local/bin` (Linux) जोड़ें, या बस `python -m graphify` चलाएँ।

**`uvx graphify …` या `uv tool run graphify …` `graphify` को रिज़ॉल्व करने में विफल**
PyPI पैकेज `graphifyy` है; `graphify` केवल वह कमांड है जो यह प्रदान करता है। `uv tool run` पहले शब्द को एक *पैकेज नाम* मानता है, इसलिए यह `graphify` नाम के पैकेज को ढूँढता है और रिपोर्ट करता है `No solution found … no versions of graphify`। पैकेज को स्पष्ट रूप से नाम दें: `uvx --from graphifyy graphify install` (`uv tool run --from graphifyy graphify install` जैसा ही)। या `uv tool install graphifyy` एक बार करें और फिर सीधे `graphify` कॉल करें।

**`uv run --with graphifyy python -m graphify` चुपचाप एक पुराना इंस्टॉल चलाता है**
`uv run` आपके *सिस्टम* Python का इस्तेमाल करता है, इसलिए अगर एक पुरानी `graphifyy` भी वहाँ रहती है (जैसे एक पिछला `pip install graphifyy`), तो Python `sys.path` पर पहले वह कॉपी ढूँढ सकता है और `--with graphifyy` इसे ओवरराइड नहीं करेगा। यह बिना किसी एरर के चलता है, लेकिन आपको *पुराने* वर्शन का व्यवहार मिलता है — जैसे `OPENAI_BASE_URL` जैसे env ओवरराइड्स चुपचाप नज़रअंदाज़ हो जाते हैं, इसलिए रिक्वेस्ट्स डिफ़ॉल्ट endpoint से टकराती हैं और 401 के साथ विफल होती हैं जो एक खराब key जैसा दिखता है। फ़िंगरप्रिंट एक `warning: skill is from graphify <newer>, package is <older>` लाइन है — इसका मतलब है कि एक अलग इंस्टॉल लोड हुआ, सिर्फ़ एक पुरानी स्किल नहीं। जाँचें कि वाकई कौन सी कॉपी लोड हुई:
```bash
python -c "import graphify; print(graphify.__file__)"
```
फिर इंस्टॉल की गई कमांड को सीधे चलाएँ (यह uv-मैनेज्ड कॉपी इस्तेमाल करता है), या पुरानी सिस्टम कॉपी हटाएँ:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` काम करता है लेकिन `graphify` कमांड नहीं**
आपके शेल के `PATH` में वह bin डायरेक्टरी शामिल नहीं है जिसमें कमांड इंस्टॉल हुई थी। सादे `pip` के बजाय `uv tool install` / `pipx install` को प्राथमिकता दें, फिर `uv tool update-shell` / `pipx ensurepath` चलाएँ और एक नया टर्मिनल खोलें (ऊपर इंस्टॉल नोट्स देखें)।

**PowerShell में `/graphify .` "path not recognized" का कारण बनता है**
PowerShell शुरुआती `/` को एक पाथ सेपरेटर मानता है। Windows पर `graphify .` (बिना स्लैश) इस्तेमाल करें।

**`--update` या रीबिल्ड के बाद ग्राफ़ में कम नोड्स हैं**
अगर एक रीफ़ैक्टर ने फ़ाइलें डिलीट कर दीं, पुराने नोड्स बने रहते हैं। कम नोड्स के साथ रीबिल्ड होने पर भी ओवरराइट करने के लिए `--force` (या `GRAPHIFY_FORCE=1` सेट करें) पास करें।

**`extract` "extraction was incomplete ... refusing to overwrite" के साथ बाहर निकलता है**
जब एक निष्कर्षण पास क्रैश होता है या एक वॉक कॉर्पस को पूरी तरह नहीं पढ़ पाता, तो रन एक पूरे रन से छोटा होगा, इसलिए `graphify extract` एक बड़े मौजूदा ग्राफ़ को आंशिक परिणाम से ओवरराइट करने से मना कर देता है (आपके `graph.json` की रक्षा करते हुए)। अंतर्निहित विफलता ठीक करें और दोबारा चलाएँ, या फिर भी ओवरराइट करने के लिए `--allow-partial` पास करें।

**ग्राफ़ में एक ही एंटिटी के लिए डुप्लिकेट नोड्स हैं (भूत डुप्लिकेट्स)**
भूत डुप्लिकेट्स (एक ही सिंबल दो बार दिखना — एक बार सोर्स लोकेशन के साथ AST निष्कर्षण से, एक बार बिना सोर्स लोकेशन के सिमैंटिक निष्कर्षण से) अब बिल्ड टाइम पर अपने आप मर्ज हो जाते हैं। अगर आप इसे v0.8.33 से पहले बने ग्राफ़ में देखते हैं, तो साफ़ करने के लिए एक पूरा री-एक्सट्रैक्ट चलाएँ:
```bash
graphify extract . --force
```

**Ollama VRAM ख़त्म हो जाता है / context window पार हो जाता है**
KV-cache विंडो ऑटो-साइज़्ड है लेकिन आपके GPU के लिए बहुत बड़ी हो सकती है। इसे घटाएँ:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**`LLM returned invalid JSON` / `Unterminated string` चेतावनियाँ**
मॉडल का JSON रिस्पॉन्स आउटपुट-टोकन लिमिट तक पहुँच गया और स्ट्रिंग के बीच में कट गया। graphify अपने आप रिकवर करता है (यह चंक को विभाजित करता है और आधे हिस्सों को दोबारा निकालता है, और एक बहुत बड़ा सिंगल डॉक्यूमेंट पहले हेडिंग/पैराग्राफ़ सीमाओं पर काटा जाता है ताकि पूरी फ़ाइल अभी भी कवर हो), इसलिए ये चेतावनियाँ शोरगुल वाली हैं लेकिन डेटा नुकसान नहीं। शोर कम करने के लिए, आउटपुट कैप बढ़ाएँ या हर चंक का आउटपुट घटाएँ:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
OpenRouter जैसे cloud gateway के साथ, Ollama shim के बजाय `--backend openai` (`OPENAI_BASE_URL` सेट करें) को प्राथमिकता दें — यह एक साफ़-सुथरा OpenAI-संगत रास्ता है। अगर मॉडल की अपनी max-output सीमा है, तो `--token-budget` घटाना एक भरोसेमंद लीवर है।

**Graph HTML ब्राउज़र में खोलने के लिए बहुत बड़ा है (>5000 नोड्स)**
HTML जनरेशन छोड़ें और सीधे JSON इस्तेमाल करें:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**दो डेवलपर्स के एक साथ कमिट करने के बाद `graph.json` में कॉन्फ़्लिक्ट मार्कर्स हैं**
`graphify hook install` चलाएँ — यह एक git merge driver सेट करता है जो `graph.json` को अपने आप यूनियन-मर्ज करता है ताकि कॉन्फ़्लिक्ट्स कभी न हों।

**दस्तावेज़ों या PDF के लिए निष्कर्षण खाली नोड्स/एजेज़ लौटाता है**
दस्तावेज़, PDF, और इमेजेज़ को एक LLM कॉल की ज़रूरत होती है — केवल-कोड कॉर्पस को कोई key नहीं चाहिए। जाँचें कि आपकी API key सेट है और बैकएंड सही है:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**आपके IDE में स्किल वर्शन मिसमैच चेतावनी**
आपका इंस्टॉल किया गया graphify वर्शन स्किल फ़ाइल से अलग है। अपडेट करें:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**हर `graphify extract` के बाद Claude Code प्रॉम्प्ट कैश अमान्य हो जाता है**
Graphify आउटपुट फ़ाइलें (`graph.json`, `graphify-out/`) वर्कस्पेस में लिखता है। अगर वे पाथ इग्नोर नहीं किए गए हैं, तो हर राइट Claude Code के प्रॉम्प्ट कैश को अमान्य कर देती है, अगली टर्न पर cache-write दरों पर पूरा री-अपलोड मजबूर करती है। उन्हें `.claudeignore` में जोड़ें:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## पूरा कमांड संदर्भ

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

> **कम्युनिटी नाम:** एक एजेंट (Claude Code, Gemini CLI) के अंदर एजेंट खुद कम्युनिटीज़ का नाम रखता है। जब आप सादा CLI चलाते हैं, `cluster-only` कॉन्फ़िगर किए गए बैकएंड (बिल्ट-इन या कस्टम OpenAI-संगत प्रोवाइडर) से उन्हें अपने आप नाम देता है — `Community N` रखने के लिए `--no-label` पास करें, या माँग पर नाम (दोबारा) जनरेट करने के लिए `graphify label` चलाएँ।

---

## और जानें

- [यह कैसे काम करता है](docs/how-it-works.md) — निष्कर्षण पाइपलाइन, कम्युनिटी डिटेक्शन, कॉन्फ़िडेंस स्कोरिंग, बेंचमार्क्स
- [ARCHITECTURE.md](ARCHITECTURE.md) — मॉड्यूल ब्रेकडाउन, एक भाषा कैसे जोड़ें
- [वैकल्पिक इंटीग्रेशन्स](docs/docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — graphify के पीछे के आइडियाज़ पर किताब, शुरू से अंत तक आर्किटेक्चर

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) graphify के ऊपर बनी हमेशा-चालू परत है — यह उसी ग्राफ़ अप्रोच को आपके पूरे कामकाजी संदर्भ पर लागू करती है: मीटिंग्स, फ़ाइलें, दस्तावेज़, और कोड, बैकग्राउंड में लगातार अपडेट होते हुए।

उन लोगों और टीमों के लिए बनाया गया जिनका काम सैकड़ों बातचीतों और दस्तावेज़ों में रहता है जिन्हें वे कभी पूरी तरह से फिर से नहीं बना सकते।

**[graphify.com पर वेटलिस्ट में शामिल हों](https://graphify.com)।** मुफ़्त ट्रायल जल्द आ रहा है।

---

<details>
<summary>योगदान</summary>

### डेवलपमेंट सेटअप

यह प्रोजेक्ट डेव वर्कफ़्लो के लिए [uv](https://docs.astral.sh/uv/) इस्तेमाल करता है। इसे एक बार इंस्टॉल करें, फिर:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

editable इंस्टॉल को सत्यापित करें:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### टेस्ट चलाना

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> macOS नोट: टेस्ट सूट में `sample.f90` और `sample.F90` दोनों फ़िक्स्चर्स शामिल हैं। ये case-insensitive HFS+ / APFS फ़ाइल सिस्टम्स पर टकराते हैं। अगर आपको एक साथ दोनों Fortran वेरिएंट्स टेस्ट करने की ज़रूरत है तो Linux पर या Docker कंटेनर में चलाएँ।

### Git वर्कफ़्लो

- सक्रिय डेवलपमेंट `v8` ब्रांच पर होता है।
- कमिट स्टाइल: `fix: <description>` / `feat: <description>` / `docs: <description>`
- एक PR खोलने से पहले, `uv run pytest tests/ -q` चलाएँ और पुष्टि करें कि यह पास होता है।
- किसी भी नए भाषा एक्सट्रैक्टर के लिए `tests/fixtures/` में एक फ़िक्स्चर फ़ाइल और `tests/test_languages.py` में टेस्ट जोड़ें।

### क्या योगदान करें

**वर्क्ड एग्ज़ाम्पल्स** सबसे उपयोगी योगदान हैं। एक असली कॉर्पस पर `/graphify` चलाएँ, आउटपुट को `worked/{slug}/` में सेव करें, एक ईमानदार `review.md` लिखें जिसमें बताया गया हो कि ग्राफ़ ने क्या सही और क्या गलत किया, और एक PR खोलें।

**निष्कर्षण बग्स** — इनपुट फ़ाइल, cache एंट्री (`graphify-out/cache/`), और क्या छूटा या गलत था, इसके साथ एक issue खोलें।

मॉड्यूल ज़िम्मेदारियों और एक भाषा कैसे जोड़ें, इसके लिए [ARCHITECTURE.md](ARCHITECTURE.md) देखें।

</details>
