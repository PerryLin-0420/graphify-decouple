<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b><code>graphify decouple</code> ekleyen <a href="https://github.com/Graphify-Labs/graphify">graphify</a>'in bir fork'u</b> — god object'ler için risk puanlı Extract-Class adayları, LLM kullanmadan, herhangi bir şey önermeden önce gerçek kaynak koduna karşı (sadece çağrı grafiğine değil) yeniden doğrulanır. Aşağıda <a href="#decouple-risk-scored-extract-class-candidates">Decouple: risk puanlı Extract-Class adayları</a> bölümüne bakın.
</p>

<div align="center">
<details><summary><b>Bunu diğer dillerde okuyun</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>graphify platformuna erken erişim, herkese açık v1 lansmanından önce açık: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

AI kodlama asistanınıza `/graphify` yazın, tüm projenizi (kod, dokümanlar, PDF'ler, görseller, videolar) dosyalarda **grep yapmak yerine sorgulayabileceğiniz** bir **bilgi grafiğine** eşler.

- **Kod haritalama ücretsiz, tamamen yerel.** Kod tree-sitter AST ile ayrıştırılır: deterministik, LLM yok, hiçbir şey makinenizden çıkmaz. (Dokümanlar, PDF'ler, görseller ve video, anlamsal bir geçiş için asistanınızın modelini veya yapılandırılmış bir API anahtarını kullanır.)
- **Her kenar açıklanır.** Her bağlantı `EXTRACTED` (kaynakta açık) veya `INFERRED` (graphify tarafından çözümlenmiş) olarak etiketlenir, böylece neyin doğrudan okunduğunu, neyin çıkarsandığını anlayabilirsiniz.
- **Bu bir vektör indeksi değil.** Embeddings yok, vector store yok: gezinebileceğiniz gerçek bir grafik. Bir soru sorun, iki şey arasındaki yolu izleyin veya bir kavramı açıklayın.

> Bunun sadece istek üzerine değil, kodunuz, dokümanlarınız ve toplantılarınız boyunca arka planda güncellenerek her zaman açık olmasını mı istiyorsunuz? **[graphify.com](https://graphify.com)**'da inşa ettiğimiz şey tam olarak bu, ve erken erişim şu anda **[app.graphify.com](https://app.graphify.com/login)** adresinde açık.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="graphify's interactive graph.html showing the FastAPI codebase as a force-directed knowledge graph with a legend of detected communities" width="900">
</p>
<p align="center">
  <em>graphify tarafından eşlenmiş FastAPI kod tabanı. Her düğüm bir kavramdır, renkler tespit edilen topluluklardır, ve tümü graph.html içinde tıklanabilir.</em>
</p>

**Başlayın** (30 saniye):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

Sonra, AI asistanınızda:

```
/graphify .
```

Bu kadar. **Üç dosya** elde edersiniz:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**Şunlarda çalışır:** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot ve 15'ten fazlası — [platformunuzu seçin](#install).

---

## Aksiyonda görün

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="graphify path query: a terminal asks for the shortest path between FastAPI and ModelField, and the answer lights up hop by hop across the knowledge graph" width="900">
</p>

Grafik oluşturulduktan sonra, dosyaları okumak yerine onu sorgularsınız. Gerçek çıktı, yukarıda gösterilen FastAPI kod tabanı üzerinde çalıştırılan graphify:

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

Her kenar bir **güven etiketi** taşır (`EXTRACTED` = kaynakta açık, `INFERRED` = çözümleme yoluyla türetilmiş), böylece neyin doğrudan okunduğunu, neyin çıkarsandığını anlayabilirsiniz. `graphify query "<question>"` düz dilde bir soru için kapsamlı bir alt grafik döndürür, ve `graphify path A B` herhangi iki şeyin nasıl bağlandığını izler.

---

## Decouple: risk puanlı Extract-Class adayları

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: MainWindow god node splitting into risk-scored candidate classes, with a shared-state warning between two of them" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: MainWindow's 5 proposed classes, Node Info panel open on Main Window Axis and Range Controls showing a 0.608 state overlap with Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>Gerçek bir çalıştırmada DECOUPLE.html — önerilen bir sınıfa tıklamak, tam olarak hangi başka sınıfla state paylaştığını ve özellikle neyin paylaşıldığını gösterir.</em>
</p>

Aynı sayfa ayrıca ayrımın kendisini de render eder. **Preview decoupled view**'ı açmak, god sınıfın kendi metodlarını önerilen sınıflarla değiştirir ve kenarları yerinde yeniden yönlendirir — yeniden çizilmiş bir diyagram değil, kablolama değişikliği:

| Önce — bugünkü god sınıf | Sonra — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html before the toggle: a single MainWindow hub node with its own methods fanned out around it" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html after the toggle: the same node reduced to 5 diamond-shaped proposed classes, green dashed edges showing which methods were extracted into each, red edges showing shared instance state between two of them" width="440"> |
| Kendi 47 metodunu tutan tek bir düğüm, her biri yalnızca sınıf üzerinden erişilebilir. | Önerilen sınıflar. Yeşil kesikli çizgi = her birine ne çıkarıldığı; kırmızı = ikisinin hâlâ paylaştığı instance state, ki bu tam olarak `split` mi `keep_as_is` mi kararını belirleyen şey. Yalnızca risk eşiğini geçen adaylar çizilir — burada 6'da 5, bu yüzden bir metodun inecek bir elması yok. |

`graphify decouple` god object'leri bulur ve onları bölmenin gerçekten değip değmediğini söyler — sadece büyük olduklarını değil.

Bunun yakalamak için var olduğu başarısızlık modu: çağrı grafiği kümelemesinin memnuniyetle 5 düzenli görünen gruba böldüğü, 47 metodlu bir sınıf, ki bunların hepsi hâlâ tam olarak aynı `self._chart_style` / `self._crosshair` instance state'ini altta okur ve yazar. Bu ayrımı gönderirseniz hiçbir şeyi decouple etmemişsinizdir — sadece metodları, hâlâ bağımsız olarak test edilemeyen, değiştirilemeyen veya akıl yürütülemeyen yeni dosyalara taşımışsınızdır, çünkü hepsi hâlâ geri iletilen aynı paylaşılan state'e ihtiyaç duyar. Yalnızca çağrı grafiğine bakan bir araç bunu hiç göremez; gerçek kaynağa geri dönmesi gerekir.

**İki kontrol, ikisi de LLM'siz, ikisi de deterministik:**

1. **Bu gerçekten bir God Object mi?** Yüksek dereceli bir düğüm gerçek bir God Object olabilir (birbiriyle ilgisiz sorumluluklara yayılmış çok sayıda KENDİ metodu — Extract Class uygulanır) veya aşırı referanslanmış bir hub/veri modeli olabilir (az sayıda kendi metodu, çoğunlukla *gelen* referanslar — gövdesini bölmek hiçbir şey yapmaz; düzeltme, arayüzünü daraltmaktır, bir sınıf çıkarmak değil). `classify_god_node` bunları ham dereceye göre değil, `member_ratio`'ya göre ayırt eder — bu fark, `TraceSource`'ın (84 kenar, ama yalnızca 6 kendi metodu) `MainWindow`'un (88 kenar, 47 kendi metodu) haklı olarak aldığı sahte bir ayrım önerisi almasını engeller.
2. **Ayrım gerçekten coupling'i azaltır mı?** `risk_before` (god düğümün mevcut boyutu/coupling'i/parçalanması), `risk_after` ile karşılaştırılır — ayrımın kendisinin ortaya çıkaracağı YENİ risk: görünmez sınıf içi kenarlar olan gruplar arası çağrılar açık sınıflar arası bağımlılıklara dönüşür, artık birden fazla yeni sınıfa bağımlı olması gereken çağıranlar, ve — bir çağrı grafiğinin yapısal olarak yapamayacağı kontrol — önerilen grupların gerçekte ne kadar `self`/`this` instance state'i (okumalar, yazmalar ve ayrı ayrı ağırlıklandırılmış paylaşılan yardımcı metod çağrıları: paylaşılan bir **yazma**, paylaşılan bir okumadan daha yüksek puan alır) ortak olduğu. Bu, god düğümün kendi kaynak dosyasını doğrudan tree-sitter ile yeniden ayrıştırır; graphify'ın kendi çıkarılmış grafiğine güvenmez, ki bu hiçbir dil için alan düzeyinde erişimi asla kaydetmez. Yalnızca `risk_after`, `risk_before`'un altında bir eşiği geçtiğinde plan `split`'i önerir — aksi takdirde `marginal` veya `keep_as_is`'tir, ve caydırılan bir aday sayı olarak raporlanır, asla gözle tahmin etmeniz gereken bir şekil olarak çizilmez.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

`graph.json`'ın yanında üç dosya üretir:

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

**State paylaşım kontrolü için dil kapsamı** (yukarıdaki yalnızca-çağrı-grafiği sınıflandırması graphify'ın çıkardığı her dil için çalışır; bu tablo özellikle `self`/`this` state çakışmasını doğrulayan kaynak yeniden ayrıştırma ile ilgilidir):

| Dil | Destekleniyor | Notlar |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` sarmalanmış bir alan erişimi değil, kendi AST düğümüdür — açıkça işlenir |
| C# | ✅ | |
| Rust | ✅ | `impl` blokları aracılığıyla `self.x` |
| Ruby | ✅ | `@x` (baskın deyim) + `self.foo` çağrıları |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | metod başına receiver çözümlemesi — Go'da `self`/`this` anahtar kelimesi yok, bu yüzden receiver adı (`func (f *Foo) M()` içindeki `f`) her metod için yeniden çözümlenir |
| C | ❌ | bir struct-pointer parametresinin onu diğer parametrelerden ayıran sözdizimsel bir işareti yoktur — tam tip çıkarımı olmadan güvenilir bir sinyal yoktur |

Desteklenmeyen bir dildeki bir god düğüm, veya kaynağı okunamayan bir düğüm, `state_analysis: "skipped"` olarak işaretlenir — sınıflandırma ve çağrı grafiği puanı yine de çalışır, ama öneri, state kontrolünün geçtiğini sessizce varsaymak yerine yalnızca çağrı grafiğine dayanır.

---

## Ne yapar

Kutudan çıktığında elde ettikleriniz:

| Yetenek | Ne elde edersiniz |
|---|---|
| **God node'lar** | En çok bağlantılı kavramlar, böylece her şeyin neyin içinden aktığını görürsünüz |
| **Topluluklar** | LLM'siz etiketlerle alt sistemlere bölünmüş grafik (Leiden) |
| **Dosyalar arası bağlantılar** | `calls` / `imports` / `inherits` / `mixes_in`, tree-sitter AST aracılığıyla ~40 dilde çözümlenmiş |
| **Sorgu, yol, açıklama** | Bir soru sorun, iki şey arasındaki yolu izleyin, veya bir kavramı açıklayın, hepsi `graph.json`'a karşı |
| **Gerekçe + doküman referansları** | `# NOTE:` / `# WHY:` yorumları ve ADR/RFC alıntıları koda bağlı birinci sınıf düğümler haline gelir |
| **Kodun ötesinde** | Dokümanlar, PDF'ler, görseller ve video/ses hepsi aynı grafiğe eşlenir |
| **Önce yerel** | Kod, tree-sitter ile yerel olarak ayrıştırılır (LLM yok, hiçbir şey makinenizden çıkmaz); yalnızca dokümanlar/medya üzerindeki anlamsal geçiş bir backend'i çağırır, ve yalnızca bir tane yapılandırırsanız |

---

## Ölçütler (Benchmarks)

| Ölçüt | Metrik | graphify | Alan |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | QA doğruluğu | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | QA doğruluğu | **76%** | dense RAG ile berabere |
| Grafik oluşturma | LLM kredisi | **0** | çoğu sistem için token başına |

Her sistem aynı harness'te aynı model ve bütçelerle çalıştırıldı, ikinci bir yargıca karşı kör olarak doğrulanmış bir yargıç tarafından puanlandı (%90.6 uzlaşma, Cohen's kappa 0.81). Tam sistem başına tablolar, kod zekası sonucu ve yeniden üretim komutları: **[BENCHMARKS.md](./BENCHMARKS.md)**.

---

## Ön koşullar

| Gereksinim | Minimum | Kontrol | Kurulum |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(önerilen)* | herhangi biri | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(alternatif)* | herhangi biri | `pipx --version` | `pip install pipx` |

**macOS hızlı kurulum (Homebrew):**
```bash
brew install python@3.12 uv
```

**Windows hızlı kurulum:**
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

## Kurulum

> **Resmi paket:** PyPI paketi `graphifyy`'dir (çift-y). PyPI'daki diğer `graphify*` paketleri bağlantılı değildir. CLI komutu hâlâ `graphify`'dir.

**Adım 1 — paketi kurun:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**Adım 2 — skill'i AI asistanınıza kaydedin:**

```bash
graphify install
```

Bu kadar. AI asistanınızı açın ve `/graphify .` yazın.

Asistan skill'ini kullanıcı profilinizin yerine mevcut depoya kurmak için `--project` ekleyin:

```bash
graphify install --project
graphify install --project --platform codex
```

Proje kapsamlı kurulumlar, mevcut dizinin altına yazar, örneğin `.claude/skills/graphify/SKILL.md` veya `.agents/skills/graphify/SKILL.md` (artı skill'in isteğe bağlı yüklediği bir `references/` yan dosyası), ve commit edilebilecek dosyalar için bir `git add` ipucu yazdırır. Proje kapsamlı kurulumları destekleyen platform başına komutlar aynı bayrağı kabul eder, örneğin `graphify claude install --project` veya `graphify codex install --project`.

> **PowerShell notu:** `/graphify .` değil `graphify .` kullanın — baştaki eğik çizgi PowerShell'de bir yol ayırıcısıdır.

> **`graphify: command not found`?** `uv tool install` / `pipx install`, `graphify` komutunu kendi araç bin dizinlerine (`~/.local/bin`) koyar. Kabuğunuz kurulumdan hemen sonra onu bulamıyorsa — yeni bir macOS + zsh kurulumunda yaygın — bu dizin henüz `PATH`'inizde değildir: `uv tool update-shell` (veya `pipx ensurepath`) çalıştırın, ardından yeni bir terminal açın. Düz `pip` ile, `~/.local/bin`'i (Linux) veya `~/Library/Python/3.x/bin`'i (Mac) PATH'inize ekleyin, veya `python -m graphify` çalıştırın.

> **Kurmak yerine `uvx` / `uv tool run` ile mi çalıştırıyorsunuz?** Komutu değil, paketi adlandırın: `uvx --from graphifyy graphify install`. Sade `uvx graphify …` başarısız olur (`No solution found … no versions of graphify`) çünkü `uv tool run` ilk kelimeyi bir *paket* olarak okur, ve paket `graphifyy`'dir — `graphify` komutu onun içinde yaşar.

> **Mümkünse Mac/Windows'ta `pip install`'dan kaçının.** Skill, çalışma zamanında Python'ı `graphify-out/.graphify_python`'dan çözer; bu, `pip`'in paketi kurduğu yerden farklı bir ortama işaret ediyorsa, `ModuleNotFoundError: No module named 'graphify'` alırsınız. `uv tool install` ve `pipx install`, paketi kendi ortamlarında izole eder ve bunu tamamen önler.

> **Git hook'ları ve uv tool / pipx:** `graphify hook install`, kurulum sırasında mevcut yorumlayıcı yolunu doğrudan hook script'lerine gömer, böylece post-commit hook'u, `~/.local/bin`'in PATH'te olmadığı GUI git istemcilerinde ve CI runner'larında bile doğru şekilde tetiklenir. graphify'ı yeniden kurar veya yükseltirseniz, gömülü yolu yenilemek için `graphify hook install`'ı yeniden çalıştırın.

> **Katı mod (Claude Code):** `graphify install --project --strict`, asistanın grafiği gerçekten kullanmasını sağlar. Varsayılan kurulum, dosyaları okumadan önce `graphify query` çalıştırmaya *teşvik eder*; katı mod, bir oturumdaki ilk ham kaynak okumasını *engeller* ve onu grafiğe yönlendirir, ardından teşvike geri döner (böylece oturum başına en fazla bir kez tetiklenir ve asla takılmaz). Çalışma zamanında `GRAPHIFY_HOOK_STRICT=1`/`0` ile değiştirin; varsayılan kurulum değişmez (yumuşak teşvik).

<details>
<summary><b>Platformunuzu seçin</b> (20'den fazla asistan, genişletmek için tıklayın)</summary>

| Platform | Kurulum komutu |
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

Codex kullanıcıları, paralel çıkarım için ayrıca `~/.codex/config.toml` içinde `[features]` altında `multi_agent = true`'ya ihtiyaç duyar. CodeBuddy, Claude Code ile aynı Agent tool ve PreToolUse hook mekanizmasını kullanır. Factory Droid, paralel subagent gönderimi için `Task` aracını kullanır. OpenClaw ve Aider sıralı çıkarım kullanır (bu platformlarda paralel agent desteği hâlâ erken aşamadadır). Trae, paralel subagent gönderimi için Agent tool'u kullanır ve `PreToolUse` hook'larını desteklemez, bu yüzden AGENTS.md her zaman açık mekanizmadır.

`--platform agents` (takma ad `--platform skills`), genel, çerçeveler arası [Agent-Skills](https://github.com/anthropics/skills) konumlarını hedefler: küresel bir kurulum için spesifikasyonun kullanıcı-küresel `~/.agents/skills/`'i (`npx skills` ve spesifikasyona uyumlu çerçeveler tarafından okunur), ve bir proje (`--project`) kurulumu için `./.agents/skills/`. Sade `graphify install`, tasarım gereği tek platformlu (Claude Code) kalır — skill'in `.agents/skills`'i okuyan herhangi bir çerçeve tarafından keşfedilebilir olmasını istediğinizde adlandırılmış `agents` platformunu kullanın.

> Codex, `/graphify` yerine `$graphify` kullanır.

</details>

<details>
<summary><b>İsteğe bağlı ekstralar</b> (yalnızca ihtiyacınız olanı kurun)</summary>

| Ekstra | Ne ekler | Kurulum |
|---|---|---|
| `pdf` | PDF çıkarımı | `uv tool install "graphifyy[pdf]"` |
| `office` | `.docx` ve `.xlsx` desteği | `uv tool install "graphifyy[office]"` |
| `google` | Google Sheets render'ı | `uv tool install "graphifyy[google]"` |
| `video` | Video/ses transkripsiyonu (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | MCP stdio sunucusu | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Neo4j push desteği | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | FalkorDB push desteği | `uv tool install "graphifyy[falkordb]"` |
| `svg` | SVG grafik dışa aktarımı | `uv tool install "graphifyy[svg]"` |
| `leiden` | Leiden topluluk tespiti (yalnızca Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Yerel Ollama çıkarımı | `uv tool install "graphifyy[ollama]"` |
| `openai` | OpenAI / OpenAI uyumlu API'ler | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic Claude API (`--backend claude`, `ANTHROPIC_API_KEY` kullanır) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (IAM kullanır, API anahtarı yok) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT` kullanır) | `uv tool install "graphifyy[openai]"` |
| `sql` | SQL şema çıkarımı | `uv tool install "graphifyy[sql]"` |
| `postgres` | Canlı PostgreSQL içgözlemi (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | BYOND DreamMaker `.dm`/`.dme` AST çıkarımı (platformunuza uyan bir wheel yoksa C derleyici + `python3-dev` gerekebilir) | `uv tool install "graphifyy[dm]"` |
| `terraform` | Terraform / HCL `.tf`/`.tfvars`/`.hcl` AST çıkarımı | `uv tool install "graphifyy[terraform]"` |
| `pascal` | Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` AST çıkarımı (daha doğru `calls`/`inherits` kenarları; yokluğunda bir regex çıkarıcıya geri döner) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | Çince sorgu segmentasyonu (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | Yukarıdakilerin hepsi | `uv tool install "graphifyy[all]"` |

</details>

---

## Asistanınızı her zaman grafiği kullanmaya zorlayın

Bir grafik oluşturduktan sonra projenizde bunu bir kez çalıştırın:

| Platform | Komut |
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

Bu, asistanınıza kod tabanı sorularında bilgi grafiğine danışmasını, tüm raporu okumak veya ham dosyaları grep'lemek yerine `graphify query "<question>"` gibi kapsamlı sorguları tercih etmesini söyleyen küçük bir yapılandırma dosyası yazar.

- **Hook platformları** (Claude Code, Gemini CLI): arama tarzı araç çağrılarından önce (ve Claude Code'da, Read/Glob araçları aracılığıyla kaynak dosyaları teker teker okumadan önce) bir hook otomatik olarak tetiklenir ve asistanınızı grafik yoluna doğru dürter.
- **Talimat dosyası platformları** (Codex, OpenCode, Cursor, vb.): kalıcı talimat dosyaları (`AGENTS.md`, `.cursor/rules/`, vb.) aynı sorgu-önce rehberliğini sağlar.

`GRAPH_REPORT.md`, geniş mimari incelemesi için hâlâ mevcuttur.

**CodeBuddy**, Claude Code ile aynı iki şeyi yapar: CodeBuddy'ye mimari sorulara cevap vermeden önce `graphify-out/GRAPH_REPORT.md`'yi okumasını söyleyen bir `CODEBUDDY.md` bölümü yazar, ve Bash arama komutlarından ve dosya okumalarından önce tetiklenen, `graphify query`'ye doğru dürten `PreToolUse` hook'ları (`.codebuddy/settings.json`) kurar.

**Codex**, bu platformda gerçekten her zaman açık grafik rehberliğini taşıyan `AGENTS.md`'ye yazar. `graphify codex install` ayrıca `.codex/hooks.json`'da (`graphify hook-check`) bir `PreToolUse` hook'u kaydeder, ama bu giriş kasıtlı olarak **no-op**'tur: Codex Desktop, `PreToolUse` üzerinde `hookSpecificOutput.additionalContext`'i reddeder, bu yüzden orada bir dürtme yaymak Bash araç çağrılarını bozardı. Hook'un (`graphify hook-guard`) dürttüğü Claude Code'dan farklı olarak, Codex'te hook tetiklenir ve kasıtlı olarak hiçbir şey yapmaz, ve `AGENTS.md` her zaman açık mekanizmadır.

**Kilo Code**, Graphify skill'ini `~/.config/kilo/skills/graphify/SKILL.md`'ye ve yerel bir `/graphify` komutunu `~/.config/kilo/command/graphify.md`'ye kurar. `graphify kilo install` ayrıca `AGENTS.md`'yi artı yerel bir `tool.execute.before` eklentisini (`.kilo/plugins/graphify.js` + `.kilo/kilo.json` veya `.kilo/kilo.jsonc` kaydı) yazar, böylece Kilo aynı her zaman açık grafik hatırlatma davranışını yerel `.kilo` yapılandırması aracılığıyla alır.

**Cursor**, `alwaysApply: true` ile `.cursor/rules/graphify.mdc`'yi yazar, bu yüzden Cursor bunu her konuşmaya otomatik olarak dahil eder, hook gerekmez.

graphify'ı tüm platformlardan bir kerede kaldırmak için: `graphify uninstall` (`graphify-out/`'u da silmek için `--purge` ekleyin). Veya platform başına komutu kullanın (ör. `graphify claude uninstall`).

---

## Raporda ne var

- **God node'lar** — projenizdeki en çok bağlantılı kavramlar. Her şey bunlardan akar.
- **Şaşırtıcı bağlantılar** — farklı dosyalarda veya modüllerde yaşayan şeyler arasındaki bağlantılar. Ne kadar beklenmedik olduklarına göre sıralanır.
- **"Neden"** — satır içi yorumlar (`# NOTE:`, `# WHY:`, `# HACK:`), docstring'ler, ve dokümanlardan tasarım gerekçesi, açıkladıkları koda bağlı ayrı düğümler olarak çıkarılır.
- **Önerilen sorular** — grafiğin cevaplamak için özellikle iyi konumlandığı 4–5 soru.
- **Güven etiketleri** — çıkarsanan her ilişki `EXTRACTED`, `INFERRED`, veya `AMBIGUOUS` olarak işaretlenir. Neyin bulunduğunu, neyin tahmin edildiğini her zaman bilirsiniz.

---

## Hangi dosyaları işler

| Tür | Uzantılar |
|------|-----------|
| Kod (36 tree-sitter grameri) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme`, `uv tool install graphifyy[dm]` gerektirir; `.mts`/`.cts` TypeScript gramerini yeniden kullanır, `.cc`/`.cxx` ve CUDA `.cu`/`.cuh` ve Metal `.metal` C++ gramerini yeniden kullanır) |
| Salesforce Apex | `.cls .trigger` (regex tabanlı; sınıflar, arayüzler, enum'lar, metodlar, trigger'lar, SOQL/DML kenarları) |
| Terraform / HCL | `.tf .tfvars .hcl` (`uv tool install graphifyy[terraform]` gerektirir) |
| MCP yapılandırmaları | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — sunucu düğümlerini, paket referanslarını, ortam değişkeni gereksinimlerini çıkarır |
| Paket manifestleri | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — paket başına bir kanonik paket düğümü (isme göre) artı `depends_on` kenarları, böylece birçok manifestten referanslanan bir paket tek bir hub'dır |
| Dokümanlar | `.md .mdx .qmd .html .txt .rst .yaml .yml` (markdown `[text](./other.md)` bağlantıları ve `[[wikilinks]]`, dokümanlar arası `references` kenarları haline gelir) |
| Office | `.docx .xlsx` (`uv tool install graphifyy[office]` gerektirir) |
| Google Workspace | `.gdoc .gsheet .gslides` (isteğe bağlı; `gws` kimlik doğrulaması ve `--google-workspace` gerektirir; Sheets için `uv tool install graphifyy[google]` gerekir) |
| PDF'ler | `.pdf` |
| Görseller | `.png .jpg .webp .gif` |
| Video / Ses | `.mp4 .mov .mp3 .wav` ve daha fazlası (`uv tool install graphifyy[video]` gerektirir) |
| YouTube / URL'ler | herhangi bir video URL'si (`uv tool install graphifyy[video]` gerektirir) |

Kod **yerel olarak API çağrısı olmadan** çıkarılır (tree-sitter aracılığıyla AST). Diğer her şey AI asistanınızın model API'si aracılığıyla geçer.

Google Drive for desktop'ın `.gdoc`, `.gsheet`, ve `.gslides` dosyaları, doküman içeriği değil kısayol işaretçileridir. Headless bir çıkarımda yerel Google Docs, Sheets ve Slides'ı dahil etmek için, [`gws` CLI](https://github.com/googleworkspace/cli)'yi kurun ve kimlik doğrulayın, ardından çalıştırın:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

`GRAPHIFY_GOOGLE_WORKSPACE=1`'i de ayarlayabilirsiniz. Graphify kısayolları `graphify-out/converted/`'a Markdown yan dosyaları olarak dışa aktarır, ardından bu dosyaları çıkarır.

---

## Yaygın komutlar

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

Yukarıda [Decouple: risk puanlı Extract-Class adayları](#decouple-risk-scored-extract-class-candidates)'na, veya aşağıda [tam komut referansı](#full-command-reference)'na bakın.

---

## Dosyaları yoksayma

Proje kök dizininizde bir `.graphifyignore` oluşturun — `.gitignore` ile aynı sözdizimi, `!` olumsuzlaması dahil.

**`.gitignore` otomatik olarak dikkate alınır.** graphify her dizindeki `.gitignore`'ı okur. Bir `.graphifyignore` de mevcutsa, ikisi **birleştirilir** — `.graphifyignore` desenleri en son değerlendirilir, bu yüzden çakışmalarda kazanırlar (`!` olumsuzlamaları dahil). Bir `.graphifyignore` eklemek yalnızca daha fazlasını hariç tutar; `.gitignore`'unuzun zaten hariç tuttuğu bir dosyayı asla yeniden dahil etmez. Alt dizin kapsamı, git ile tamamen aynı şekilde çalışır — bir yoksay dosyası yalnızca kendi alt ağacını etkiler.

Git tarafından yoksayılan üretilmiş veya derlenmiş kod grafiğe ait olduğunda, `graphify extract`'e `--no-gitignore` geçirin. Bu, `.gitignore` ve `.git/info/exclude`'u devre dışı bırakır; `.graphifyignore` hâlâ geçerlidir.

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

## Takım kurulumu

`graphify-out/`, git'e commit edilmek üzere tasarlanmıştır, böylece takımdaki herkes bir haritayla başlar.

**Önerilen `.gitignore` eklemeleri:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` artık taşınabilir — anahtarlar göreli yollar olarak saklanır ve yükleme sırasında yeniden bağlanır, bu yüzden onu commit etmek güvenlidir ve ilk checkout'ta tam bir yeniden derlemeyi önler.

**İş akışı:**
1. Bir kişi `/graphify .` çalıştırır ve `graphify-out/`'u commit eder.
2. Herkes pull çeker — asistanları grafiği hemen okur.
3. Her commit'ten sonra otomatik yeniden oluşturma için `graphify hook install`'ı çalıştırın (yalnızca AST, API maliyeti yok). Bu ayrıca bir git merge driver kurar, böylece `graph.json` asla çakışma işaretleriyle kalmaz — paralel commit yapan iki geliştirici, grafiklerinin otomatik olarak birleştirildiğini görür.
4. Dokümanlar veya makaleler değiştiğinde, bu düğümleri yenilemek için `/graphify --update`'i çalıştırın.

---

## Grafiği doğrudan kullanma

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

MCP sunucusu, asistanınıza yapılandırılmış erişim sağlar: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Paylaşılan HTTP sunucusu

`--transport stdio` (varsayılan), geliştirici başına bir yerel sunucu başlatır. `--transport http`, aynı araçları MCP Streamable HTTP transport'u üzerinden sunar, böylece tek bir paylaşılan süreç tüm takım için grafiği sunabilir — istemciler, IDE MCP yapılandırmalarını graphify'ı yerel olarak çalıştırmak yerine `http://<host>:8080/mcp`'ye işaret ettirir.

| Bayrak | Varsayılan | Amaç |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Sunulacak transport |
| `--host` | `127.0.0.1` | HTTP bağlanma host'u (localhost'un ötesine açmak için `0.0.0.0` kullanın) |
| `--port` | `8080` | HTTP bağlanma portu |
| `--api-key` | env `GRAPHIFY_API_KEY` | `Authorization: Bearer <key>` (veya `X-API-Key`) gerektirir |
| `--path` | `/mcp` | HTTP mount yolu |
| `--json-response` | kapalı | SSE akışları yerine düz JSON döndürür |
| `--stateless` | kapalı | Oturum başına state yok (load-balanced / CI dağıtımları için) |
| `--session-timeout` | `3600` | Boşta stateful oturumları N saniye sonra temizler (`0` devre dışı bırakır) |

Varsayılan `127.0.0.1` bağlantısı yalnızca loopback'tir. Paylaşılan bir host'ta açığa çıkarırken `--host 0.0.0.0` **ve** `--api-key`'i birlikte ayarlayın. Bir konteynerde çalıştırın:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **WSL / Linux notu:** Ubuntu `python`'ı değil `python3`'ü sağlar. Çakışmaları önlemek için bir venv kullanın:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## Ortam değişkenleri

Bunlar yalnızca **headless / CI çıkarımı** (`graphify extract`) için gereklidir. IDE'niz içinde `/graphify` skill'i aracılığıyla çalıştırıldığında, model API'si IDE oturumunuz tarafından sağlanır — ekstra anahtar gerekmez.

| Değişken | Ne için kullanılır | Ne zaman gerekli |
|---|---|---|
| `ANTHROPIC_API_KEY` | Claude (Anthropic) backend'i | `--backend claude` |
| `ANTHROPIC_BASE_URL` | Anthropic uyumlu endpoint URL'si (LiteLLM proxy, gateway'ler, ...) | `--backend claude` (varsayılan: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Claude backend'i için model adı — özel endpoint'ler için, sunucunuzun sağladığı model adını/takma adını kullanın | `--backend claude` (varsayılan: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` veya `GOOGLE_API_KEY` | Google Gemini backend'i | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI veya OpenAI uyumlu API'ler | `--backend openai` (yerel sunucular boş olmayan herhangi bir değeri kabul eder) |
| `OPENAI_BASE_URL` | OpenAI uyumlu sunucu URL'si (llama.cpp, vLLM, LM Studio, ...) | `--backend openai` (varsayılan: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | OpenAI backend'i için model adı — self-hosted sunucular için, sunucunuzun sağladığı model adını/takma adını kullanın (`/v1/models` endpoint'ini kontrol edin), ör. llama.cpp için `LFM2.5-8B-A1B-UD-Q4_K_XL` | `--backend openai` (varsayılan: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | DeepSeek backend'i | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Kimi Code backend'i | `--backend kimi` |
| `OLLAMA_BASE_URL` | Yerel Ollama çıkarım URL'si | `--backend ollama` (varsayılan: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Ollama model adı | `--backend ollama` (varsayılan: otomatik algılama) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Ollama KV-cache pencere boyutunu geçersiz kılar | isteğe bağlı — varsayılan olarak otomatik boyutlandırılır |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Yüklenmiş Ollama modelini tutma dakikaları | isteğe bağlı — her parçadan sonra kaldırmak için `0` ayarlayın |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI Service backend'i | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | Azure kaynak endpoint URL'si | `--backend azure` (API anahtarıyla birlikte gerekli) |
| `AZURE_OPENAI_API_VERSION` | Azure API sürüm geçersiz kılma | isteğe bağlı — varsayılan `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` veya `GRAPHIFY_AZURE_MODEL` | Azure dağıtım adı | isteğe bağlı — varsayılan `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — standart kimlik bilgisi zinciri | `--backend bedrock` (API anahtarı yok, IAM kullanır) |
| `GRAPHIFY_MAX_WORKERS` | AST paralelliği thread sayısı | isteğe bağlı — `--max-workers` bayrağı da |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Yoğun corpus'lar için çıktı sınırını artırın | isteğe bağlı — ör. büyük dosyalar için `32768` |
| `GRAPHIFY_API_TIMEOUT` | HTTP, claude-cli, Anthropic SDK ve Bedrock backend'leri için çağrı başına saniye cinsinden zaman aşımı (varsayılan: 600) | isteğe bağlı — `--api-timeout` bayrağı da |
| `GRAPHIFY_MAX_RETRIES` | Vazgeçmeden önce hız sınırlı (429) bir isteğin kaç kez yeniden denenebileceği (varsayılan: 6; `Retry-After`'a saygı gösterir) | isteğe bağlı — sıkı kuruluş başına limitler için artırın (ör. kimi); `0` devre dışı bırakır |
| `GRAPHIFY_FORCE` | Daha az düğüm olsa bile grafik yeniden oluşturmayı zorla | isteğe bağlı — `--force` bayrağı da |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Google Workspace dışa aktarımını otomatik etkinleştir | isteğe bağlı — `1`'e ayarlayın |
| `GRAPHIFY_TRIAGE_BACKEND` | `graphify prs --triage` için backend | isteğe bağlı — mevcut anahtarlardan otomatik algılanır |
| `GRAPHIFY_TRIAGE_MODEL` | Triage için model geçersiz kılma | isteğe bağlı — ör. `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | `~/.cache/graphify-queries.log`'daki yerel sorgu günlüğünü açmak için `1`'e ayarlayın (her query/path/explain sorusunu + corpus yolunu kaydeder). Varsayılan olarak kapalı — dahil olmadıkça hiçbir şey yazılmaz (#1797) | isteğe bağlı |
| `GRAPHIFY_QUERY_LOG` | Sorgu günlüğünü etkinleştirir ve varsayılan yerine bu yola yazar | isteğe bağlı — bu veya `_ENABLE` ayarlanmadıkça kapalı |
| `GRAPHIFY_QUERY_LOG_DISABLE` | Sorgu günlüğünü zorla kapatmak için `1`'e ayarlayın (enable değişkenlerine üstün gelir) | isteğe bağlı |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | Günlük etkinleştirildiğinde, tam alt grafik yanıtlarını da kaydeder (varsayılan olarak kapalı) | isteğe bağlı |
| `GRAPHIFY_MAX_GRAPH_BYTES` | graph.json'ın 512 MiB boyut sınırını geçersiz kılın — ör. `700MB`, `2GB`, veya düz bayt | isteğe bağlı — çok büyük corpus'lar için yararlı |
| `GRAPHIFY_MAX_CONTEXTS` | Tek bir çoklu proje MCP sunucusunun tuttuğu varsayılan olmayan proje grafiklerinin maksimum sayısı | isteğe bağlı — varsayılan: `8`; geçersiz değerler `8` kullanır, ve `1`'in altındaki değerler `1` kullanır |
| `GRAPHIFY_LLM_TEMPERATURE` | Anlamsal çıkarım için LLM sıcaklığını geçersiz kılın — ör. `0.7`, veya atlamak için `none` | isteğe bağlı — o1/o3/o4/gpt-5 akıl yürütme modelleri için otomatik olarak atlanır |

---

## Gizlilik

- **Kod dosyaları** — tree-sitter aracılığıyla yerel olarak işlenir. Hiçbir şey makinenizden çıkmaz. Yalnızca kod içeren bir corpus, hiçbir API anahtarı gerektirmez — `graphify extract` tamamen çevrimdışı çalışır. Karma bir depoda, yalnızca kodu indekslemek ve aksi takdirde bir LLM gerektirecek dokümanları/PDF'leri/görselleri atlamak için `--code-only` ekleyin.
- **Video / ses** — faster-whisper ile yerel olarak transkript edilir. Hiçbir şey makinenizden çıkmaz.
- **Dokümanlar, PDF'ler, görseller** — anlamsal çıkarım için AI asistanınıza gönderilir (`/graphify` skill'i aracılığıyla, IDE oturumunuzun çalıştırdığı herhangi bir modeli kullanarak). Headless `graphify extract`, `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), çalışan bir Ollama instance'ı (`OLLAMA_BASE_URL`), standart sağlayıcı zinciri aracılığıyla AWS kimlik bilgileri (Bedrock - API anahtarı gerekmez, IAM kullanır), veya `claude` CLI ikili dosyası (Claude Code - API anahtarı gerekmez, Claude aboneliğinizi kullanır) gerektirir. `--dedup-llm` bayrağı aynı anahtarı kullanır.
- **Veri konumu** — `graphify extract`, hangi API anahtarının ayarlandığına göre hangi sağlayıcının kullanılacağını otomatik olarak algılar (öncelik: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). Veri konumu gereksinimleri olan kod için, `--backend ollama` (tamamen yerel) kullanın veya açık bir `--backend` bayrağı geçirin. Kimi (`MOONSHOT_API_KEY`), Çin'deki Moonshot AI sunucularına yönlendirir.
- **Telemetri yok**, kullanım takibi yok, analitik yok.
- **Sorgu günlüğü** — her `graphify query`, `graphify path`, `graphify explain`, ve MCP `query_graph` çağrısı, JSON Lines biçiminde `~/.cache/graphify-queries.log`'a kaydedilir (zaman damgası, soru, corpus, döndürülen düğümler, süre). Tam alt grafik yanıtları varsayılan olarak **saklanmaz**. Vazgeçmek için `GRAPHIFY_QUERY_LOG_DISABLE=1`'i ayarlayın, veya kod yolunu devre dışı bırakmadan sessize almak için `GRAPHIFY_QUERY_LOG=/dev/null`'ı ayarlayın.

---

## Sorun giderme

**Kurulumdan sonra `graphify: command not found`**
CLI kurulu ama bin dizini kabuğunuzun `PATH`'inde değil. Nasıl kurduğunuza uygun düzeltmeyi seçin:
- **uv** (`uv tool install graphifyy`): komut, taze bir macOS/zsh kurulumunun genellikle `PATH`'te bulunmadığı uv'nin araç bin dizinine (`~/.local/bin`) gider. `uv tool update-shell`'i çalıştırın, ardından yeni bir terminal açın. (Dizini `uv tool dir --bin` ile bulun.)
- **pipx** (`pipx install graphifyy`): `pipx ensurepath`'i çalıştırın, ardından yeni bir terminal açın.
- **pip** (`pip install graphifyy`): pip, `PATH`'te olmayabilecek bir kullanıcı bin dizinine script'ler kurar — `~/Library/Python/3.x/bin`'i (macOS) veya `~/.local/bin`'i (Linux) `~/.zshrc`/`~/.bashrc`'nizde PATH'inize ekleyin, veya sadece `python -m graphify`'ı çalıştırın.

**`uvx graphify …` veya `uv tool run graphify …`, `graphify`'ı çözemiyor**
PyPI paketi `graphifyy`'dir; `graphify` yalnızca sağladığı komuttur. `uv tool run`, ilk kelimeyi bir *paket adı* olarak ele alır, bu yüzden `graphify` adında bir paket arar ve `No solution found … no versions of graphify` raporlar. Paketi açıkça adlandırın: `uvx --from graphifyy graphify install` (`uv tool run --from graphifyy graphify install` ile aynı). Veya `uv tool install graphifyy`'yi bir kez yapın ve ardından `graphify`'ı doğrudan çağırın.

**`uv run --with graphifyy python -m graphify`, sessizce daha eski bir kurulumu çalıştırıyor**
`uv run`, *sistem* Python'unuzu kullanır, bu yüzden daha eski bir `graphifyy` de orada yaşıyorsa (ör. geçmiş bir `pip install graphifyy`), Python `sys.path`'te önce o kopyayı bulabilir ve `--with graphifyy` bunu geçersiz kılmaz. Hatasız çalışır, ama *eski* sürümün davranışını alırsınız — ör. `OPENAI_BASE_URL` gibi ortam geçersiz kılmaları sessizce yoksayılır, bu yüzden istekler varsayılan endpoint'e çarpar ve kötü bir anahtar gibi görünen bir 401 ile başarısız olur. Parmak izi, bir `warning: skill is from graphify <newer>, package is <older>` satırıdır — bu, sadece eski bir skill değil, farklı bir kurulumun yüklendiği anlamına gelir. Hangi kopyanın gerçekten yüklendiğini kontrol edin:
```bash
python -c "import graphify; print(graphify.__file__)"
```
Ardından kurulu komutu doğrudan çalıştırın (uv tarafından yönetilen kopyayı kullanır), veya eski sistem kopyasını kaldırın:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` çalışıyor ama `graphify` komutu çalışmıyor**
Kabuğunuzun `PATH`'i, komutun kurulduğu bin dizinini içermiyor. Düz `pip` yerine `uv tool install` / `pipx install`'ı tercih edin, ardından `uv tool update-shell` / `pipx ensurepath`'i çalıştırın ve yeni bir terminal açın (yukarıdaki kurulum notlarına bakın).

**`/graphify .`, PowerShell'de "path not recognized"e neden oluyor**
PowerShell, baştaki `/`'yi bir yol ayırıcısı olarak ele alır. Windows'ta `graphify .` (eğik çizgi olmadan) kullanın.

**`--update` veya yeniden oluşturmadan sonra grafikte daha az düğüm var**
Bir yeniden yapılandırma dosyaları sildiyse, eski düğümler kalır. Yeniden oluşturmanın daha az düğümü olsa bile üzerine yazmak için `--force`'u (veya `GRAPHIFY_FORCE=1`'i ayarlayın) geçirin.

**`extract`, "extraction was incomplete ... refusing to overwrite" ile çıkıyor**
Bir çıkarım geçişi çöktüğünde veya bir tarama corpus'u tam olarak okuyamadığında, çalıştırma tam bir çalıştırmadan daha küçük olur, bu yüzden `graphify extract`, daha büyük mevcut bir grafiğin üzerine kısmi bir sonuçla yazmayı reddeder (`graph.json`'unuzu korur). Altta yatan hatayı düzeltin ve yeniden çalıştırın, veya yine de üzerine yazmak için `--allow-partial`'ı geçirin.

**Grafikte aynı varlık için yinelenen düğümler var (hayalet yinelemeler)**
Hayalet yinelemeler (aynı sembol iki kez görünür — bir kez kaynak konumlu AST çıkarımından, bir kez kaynak konumsuz anlamsal çıkarımdan) artık derleme zamanında otomatik olarak birleştirilir. Bunu v0.8.33'ten önce oluşturulmuş bir grafikte görüyorsanız, temizlemek için tam bir yeniden çıkarım çalıştırın:
```bash
graphify extract . --force
```

**Ollama VRAM'i tüketiyor / bağlam penceresi aşılıyor**
KV-cache penceresi otomatik boyutlandırılır ama GPU'nuz için çok büyük olabilir. Azaltın:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**`LLM returned invalid JSON` / `Unterminated string` uyarıları**
Modelin JSON yanıtı çıktı-token sınırına çarptı ve string ortasında kesildi. graphify otomatik olarak kurtarır (parçayı böler ve yarıları yeniden çıkarır, ve aşırı büyük tek bir doküman önce başlık/paragraf sınırlarında dilimlenir, böylece tüm dosya hâlâ kapsanır), bu yüzden bu uyarılar gürültülü ama veri kaybı değildir. Gürültüyü azaltmak için, çıktı sınırını artırın veya her parçanın çıktısını küçültün:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
OpenRouter gibi bir bulut gateway'i ile, Ollama shim yerine `--backend openai`'yı (`OPENAI_BASE_URL`'i ayarlayın) tercih edin — daha temiz, OpenAI uyumlu bir yoldur. Modelin kendi max-output tavanı varsa, `--token-budget`'i düşürmek güvenilir bir kaldıraçtır.

**Graph HTML, tarayıcıda açmak için çok büyük (5000'den fazla düğüm)**
HTML oluşturmayı atlayın ve JSON'ı doğrudan kullanın:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**İki geliştirici aynı anda commit ettikten sonra `graph.json`'da çakışma işaretleri var**
`graphify hook install`'ı çalıştırın — bu, `graph.json`'ı otomatik olarak birleştiren bir git merge driver kurar, böylece çakışmalar asla olmaz.

**Çıkarım, dokümanlar veya PDF'ler için boş düğümler/kenarlar döndürüyor**
Dokümanlar, PDF'ler ve görseller bir LLM çağrısı gerektirir — yalnızca kod corpus'ları anahtar gerektirmez. API anahtarınızın ayarlandığından ve backend'in doğru olduğundan emin olun:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**IDE'nizde skill sürüm uyumsuzluğu uyarısı**
Kurulu graphify sürümünüz, skill dosyasından farklı. Güncelleyin:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**Her `graphify extract`'ten sonra Claude Code prompt cache'i geçersiz kılınıyor**
Graphify, çıktı dosyalarını (`graph.json`, `graphify-out/`) çalışma alanına yazar. Bu yollar yoksayılmazsa, her yazma Claude Code'un prompt cache'ini geçersiz kılar, bir sonraki turda cache-yazma oranlarında tam bir yeniden yüklemeyi zorlar. Bunları `.claudeignore`'a ekleyin:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## Tam komut referansı

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

> **Topluluk isimleri:** bir agent (Claude Code, Gemini CLI) içinde, agent toplulukları kendisi adlandırır. Sade CLI'yi çalıştırdığınızda, `cluster-only` onları yapılandırılmış backend (yerleşik veya özel OpenAI uyumlu sağlayıcı) ile otomatik olarak adlandırır — `Community N`'i korumak için `--no-label`'ı geçirin, veya isimleri talep üzerine (yeniden) oluşturmak için `graphify label`'ı çalıştırın.

---

## Daha fazla bilgi edinin

- [Nasıl çalışır](docs/how-it-works.md) — çıkarım pipeline'ı, topluluk tespiti, güven puanlaması, ölçütler
- [ARCHITECTURE.md](ARCHITECTURE.md) — modül dökümü, bir dil nasıl eklenir
- [İsteğe bağlı entegrasyonlar](docs/docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — graphify'ın arkasındaki fikirler, uçtan uca mimari hakkındaki kitap

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com), graphify üzerine inşa edilmiş her zaman açık katmandır — aynı grafik yaklaşımını tüm çalışma bağlamınıza uygular: toplantılar, dosyalar, dokümanlar ve kod, arka planda sürekli güncellenerek.

Çalışması, tam olarak asla yeniden inşa edemeyecekleri yüzlerce konuşma ve dokümanda yaşayan kişiler ve takımlar için inşa edilmiştir.

**[graphify.com'da bekleme listesine katılın](https://graphify.com).** Ücretsiz deneme yakında başlıyor.

---

<details>
<summary>Katkıda bulunma</summary>

### Geliştirme ortamı kurulumu

Proje, geliştirme iş akışı için [uv](https://docs.astral.sh/uv/) kullanır. Bir kez kurun, ardından:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

Editable kurulumu doğrulayın:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### Testleri çalıştırma

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> macOS notu: test paketi hem `sample.f90` hem de `sample.F90` fixture'larını içerir. Bunlar, büyük/küçük harf duyarsız HFS+ / APFS dosya sistemlerinde çakışır. Her iki Fortran çeşidini de aynı anda test etmeniz gerekiyorsa, Linux'ta veya bir Docker konteynerinde çalıştırın.

### Git iş akışı

- Aktif geliştirme `v8` branch'inde gerçekleşir.
- Commit stili: `fix: <description>` / `feat: <description>` / `docs: <description>`
- Bir PR açmadan önce, `uv run pytest tests/ -q`'yu çalıştırın ve geçtiğini doğrulayın.
- Herhangi bir yeni dil çıkarıcı için `tests/fixtures/`'a bir fixture dosyası ve `tests/test_languages.py`'a testler ekleyin.

### Ne katkıda bulunulur

**İşlenmiş örnekler**, en yararlı katkıdır. Gerçek bir corpus üzerinde `/graphify`'ı çalıştırın, çıktıyı `worked/{slug}/`'a kaydedin, grafiğin neyi doğru ve yanlış yaptığını kapsayan dürüst bir `review.md` yazın, ve bir PR açın.

**Çıkarım hataları** — girdi dosyası, cache girişi (`graphify-out/cache/`), ve neyin kaçırıldığı veya yanlış olduğu ile bir issue açın.

Modül sorumlulukları ve bir dilin nasıl ekleneceği için [ARCHITECTURE.md](ARCHITECTURE.md)'ye bakın.

</details>
