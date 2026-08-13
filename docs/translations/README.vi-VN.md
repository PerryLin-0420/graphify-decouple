<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>Một fork của <a href="https://github.com/Graphify-Labs/graphify">graphify</a> bổ sung <code>graphify decouple</code></b> — các ứng viên Extract-Class được chấm điểm rủi ro cho god object, không dùng LLM, được xác minh lại dựa trên mã nguồn thực tế (không chỉ đồ thị lời gọi) trước khi đề xuất bất cứ điều gì. Xem <a href="#decouple-risk-scored-extract-class-candidates">Decouple: các ứng viên Extract-Class được chấm điểm rủi ro</a> bên dưới.
</p>

<div align="center">
<details><summary><b>Đọc bằng ngôn ngữ khác</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>Quyền truy cập sớm vào nền tảng graphify đang mở trước khi ra mắt v1 chính thức: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

Gõ `/graphify` trong trợ lý lập trình AI của bạn và nó sẽ ánh xạ toàn bộ dự án của bạn (mã nguồn, tài liệu, PDF, hình ảnh, video) thành một **đồ thị tri thức** mà bạn có thể **truy vấn thay vì grep** qua các tệp.

- **Ánh xạ mã nguồn miễn phí, hoàn toàn cục bộ.** Mã nguồn được phân tích cú pháp bằng tree-sitter AST: xác định, không dùng LLM, không có gì rời khỏi máy của bạn. (Tài liệu, PDF, hình ảnh và video sử dụng mô hình của trợ lý bạn, hoặc một khóa API đã cấu hình, cho một lượt phân tích ngữ nghĩa.)
- **Mọi cạnh đều được giải thích.** Mỗi kết nối được gắn nhãn `EXTRACTED` (rõ ràng trong nguồn) hoặc `INFERRED` (được graphify suy luận), để bạn biết cái gì được đọc trực tiếp và cái gì được suy luận.
- **Không phải chỉ mục vector.** Không có embeddings, không có vector store: một đồ thị thực sự mà bạn duyệt qua. Đặt câu hỏi, truy tìm đường đi giữa hai thứ, hoặc yêu cầu giải thích một khái niệm.

> Bạn muốn điều này luôn hoạt động, cập nhật trong nền qua mã nguồn, tài liệu và các cuộc họp của bạn thay vì chỉ theo yêu cầu? Đó là điều chúng tôi đang xây dựng tại **[graphify.com](https://graphify.com)**, và quyền truy cập sớm hiện đang mở tại **[app.graphify.com](https://app.graphify.com/login)**.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="graphify's interactive graph.html showing the FastAPI codebase as a force-directed knowledge graph with a legend of detected communities" width="900">
</p>
<p align="center">
  <em>Mã nguồn FastAPI được graphify ánh xạ. Mỗi node là một khái niệm, màu sắc là các cộng đồng được phát hiện, và toàn bộ có thể nhấp vào trong graph.html.</em>
</p>

**Bắt đầu** (30 giây):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

Sau đó, trong trợ lý AI của bạn:

```
/graphify .
```

Vậy là xong. Bạn nhận được **ba tệp**:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**Hoạt động trong** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, và hơn 15 công cụ khác — [chọn nền tảng của bạn](#install).

---

## Xem nó hoạt động

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="graphify path query: a terminal asks for the shortest path between FastAPI and ModelField, and the answer lights up hop by hop across the knowledge graph" width="900">
</p>

Sau khi đồ thị được xây dựng, bạn truy vấn nó thay vì đọc tệp. Đầu ra thực tế, graphify chạy trên mã nguồn FastAPI được hiển thị ở trên:

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

Mỗi cạnh mang một **nhãn độ tin cậy** (`EXTRACTED` = rõ ràng trong nguồn, `INFERRED` = được suy ra bằng cách giải quyết), để bạn biết cái gì được đọc trực tiếp và cái gì được suy luận. `graphify query "<question>"` trả về một đồ thị con có phạm vi giới hạn cho một câu hỏi bằng ngôn ngữ thông thường, và `graphify path A B` truy tìm cách hai thứ bất kỳ kết nối với nhau.

---

## Decouple: các ứng viên Extract-Class được chấm điểm rủi ro

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: MainWindow god node splitting into risk-scored candidate classes, with a shared-state warning between two of them" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: MainWindow's 5 proposed classes, Node Info panel open on Main Window Axis and Range Controls showing a 0.608 state overlap with Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>DECOUPLE.html trên một lần chạy thực tế — nhấp vào một lớp được đề xuất sẽ hiển thị chính xác nó chia sẻ trạng thái với lớp nào khác, và cụ thể chia sẻ điều gì.</em>
</p>

Cùng một trang cũng hiển thị chính việc phân tách. Bật **Preview decoupled view** sẽ thay thế các phương thức riêng của god class bằng các lớp được đề xuất và định tuyến lại các cạnh tại chỗ — đó là thay đổi kết nối, không phải một sơ đồ được vẽ lại:

| Trước — god class ngày nay | Sau — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html before the toggle: a single MainWindow hub node with its own methods fanned out around it" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html after the toggle: the same node reduced to 5 diamond-shaped proposed classes, green dashed edges showing which methods were extracted into each, red edges showing shared instance state between two of them" width="440"> |
| Một node giữ 47 phương thức riêng của nó, mỗi phương thức chỉ có thể tiếp cận thông qua lớp. | Các lớp được đề xuất. Đường nét đứt màu xanh lá = cái gì được trích xuất vào lớp nào; màu đỏ = trạng thái instance mà hai lớp vẫn còn chia sẻ, đó chính xác là điều quyết định giữa `split` và `keep_as_is`. Chỉ những ứng viên vượt qua ngưỡng rủi ro mới được vẽ — ở đây là 5 trong 6, đó là lý do tại sao một phương thức không có hình thoi để hạ cánh. |

`graphify decouple` tìm các god object và cho bạn biết liệu việc phân tách chúng có thực sự đáng giá không — chứ không chỉ là chúng lớn.

Kiểu thất bại mà tính năng này tồn tại để phát hiện: một lớp với 47 phương thức mà việc phân cụm dựa trên đồ thị lời gọi vui vẻ tách thành 5 nhóm trông gọn gàng, tất cả trong số đó vẫn đọc và ghi chính xác cùng một trạng thái instance `self._chart_style` / `self._crosshair` bên dưới. Nếu bạn triển khai sự phân tách đó, bạn chưa decouple được gì cả — bạn chỉ di chuyển các phương thức sang các tệp mới mà vẫn không thể được kiểm thử, thay đổi, hoặc suy luận độc lập, vì tất cả chúng vẫn cần cùng một trạng thái được chia sẻ truyền trở lại. Một công cụ chỉ nhìn vào đồ thị lời gọi hoàn toàn không thể thấy điều này; nó phải quay lại mã nguồn thực tế.

**Hai kiểm tra, cả hai đều không dùng LLM, cả hai đều xác định:**

1. **Đây có thực sự là một God Object không?** Một node có bậc cao có thể là một God Object thực sự (nhiều phương thức RIÊNG của nó, trải rộng trên các trách nhiệm không liên quan — Extract Class áp dụng được) hoặc một hub/mô hình dữ liệu bị tham chiếu quá mức (ít phương thức riêng, chủ yếu là các tham chiếu *đến* — việc phân tách phần thân của nó không làm được gì cả; giải pháp là thu hẹp giao diện của nó, không phải trích xuất một lớp). `classify_god_node` phân biệt chúng bằng `member_ratio`, không phải bậc thô — sự khác biệt này giúp `TraceSource` (84 cạnh, nhưng chỉ 6 phương thức riêng) không nhận được một gợi ý phân tách sai lầm mà `MainWindow` (88 cạnh, 47 phương thức riêng) nhận được một cách chính đáng.
2. **Việc phân tách có thực sự giảm coupling không?** `risk_before` (kích thước/coupling/phân mảnh hiện tại của god node) được so sánh với `risk_after` — rủi ro MỚI mà chính sự phân tách sẽ mang lại: các lời gọi giữa các nhóm từng là cạnh nội bộ lớp không thể nhìn thấy và trở thành các phụ thuộc liên lớp rõ ràng, các bên gọi giờ sẽ cần phụ thuộc vào nhiều hơn một lớp mới, và — kiểm tra mà một đồ thị lời gọi về mặt cấu trúc không thể làm được — có bao nhiêu trạng thái instance `self`/`this` (đọc, ghi, và các lời gọi phương thức hỗ trợ được chia sẻ, được trọng số riêng biệt: một lần **ghi** được chia sẻ được chấm điểm cao hơn một lần đọc được chia sẻ) mà các nhóm được đề xuất thực sự có chung. Điều này phân tích cú pháp lại trực tiếp tệp nguồn của chính god node bằng tree-sitter; nó không dựa vào đồ thị được graphify tự trích xuất, vốn không bao giờ ghi lại quyền truy cập cấp trường cho bất kỳ ngôn ngữ nào. Chỉ khi `risk_after` vượt qua một ngưỡng thấp hơn `risk_before` thì kế hoạch mới đề xuất `split` — nếu không thì đó là `marginal` hoặc `keep_as_is`, và một ứng viên không được khuyến khích được báo cáo dưới dạng một con số, không bao giờ được vẽ như một hình dạng mà bạn phải đoán bằng mắt.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

Xuất ba tệp bên cạnh `graph.json`:

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

**Phạm vi ngôn ngữ cho kiểm tra chia sẻ trạng thái** (việc phân loại chỉ-dùng-đồ-thị-lời-gọi ở trên hoạt động cho mọi ngôn ngữ mà graphify trích xuất; bảng này đặc biệt nói về việc phân tích cú pháp lại nguồn để xác minh sự chồng chéo trạng thái `self`/`this`):

| Ngôn ngữ | Được hỗ trợ | Ghi chú |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` là node AST riêng của nó, không phải quyền truy cập trường được bọc — được xử lý một cách rõ ràng |
| C# | ✅ | |
| Rust | ✅ | `self.x` thông qua các khối `impl` |
| Ruby | ✅ | `@x` (thành ngữ chính) + các lời gọi `self.foo` |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | phân giải receiver theo từng phương thức — Go không có từ khóa `self`/`this`, vì vậy tên receiver (`f` trong `func (f *Foo) M()`) được phân giải lại mới cho mỗi phương thức |
| C | ❌ | một tham số con trỏ struct không có dấu hiệu cú pháp nào phân biệt nó với bất kỳ tham số nào khác — không có tín hiệu đáng tin cậy nếu không có suy luận kiểu đầy đủ |

Một god node bằng ngôn ngữ không được hỗ trợ, hoặc một node có nguồn không thể đọc được, được đánh dấu là `state_analysis: "skipped"` — việc phân loại và điểm đồ thị lời gọi vẫn chạy, nhưng khuyến nghị chỉ dựa vào đồ thị lời gọi thay vì âm thầm giả định rằng kiểm tra trạng thái đã vượt qua.

---

## Nó làm gì

Những gì bạn nhận được ngay lập tức:

| Khả năng | Bạn nhận được gì |
|---|---|
| **God node** | Các khái niệm được kết nối nhiều nhất, để bạn thấy mọi thứ chảy qua đâu |
| **Cộng đồng** | Đồ thị được chia thành các hệ thống con (Leiden), với các nhãn không dùng LLM |
| **Liên kết chéo tệp** | `calls` / `imports` / `inherits` / `mixes_in` được giải quyết trên ~40 ngôn ngữ thông qua tree-sitter AST |
| **Truy vấn, đường đi, giải thích** | Đặt một câu hỏi, truy tìm đường đi giữa hai thứ, hoặc giải thích một khái niệm, tất cả dựa trên `graph.json` |
| **Lý do + tham chiếu tài liệu** | Các bình luận `# NOTE:` / `# WHY:` và trích dẫn ADR/RFC trở thành các node hạng nhất được liên kết với mã nguồn |
| **Vượt ra ngoài mã nguồn** | Tài liệu, PDF, hình ảnh và video/âm thanh đều được ánh xạ vào cùng một đồ thị |
| **Ưu tiên cục bộ** | Mã nguồn được phân tích cú pháp cục bộ bằng tree-sitter (không dùng LLM, không có gì rời khỏi máy của bạn); chỉ lượt phân tích ngữ nghĩa trên tài liệu/phương tiện mới gọi một backend, và chỉ khi bạn cấu hình một cái |

---

## Bài kiểm tra chuẩn (Benchmark)

| Benchmark | Chỉ số | graphify | Lĩnh vực |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | độ chính xác QA | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | độ chính xác QA | **76%** | ngang bằng với dense RAG |
| Xây dựng đồ thị | tín dụng LLM | **0** | mỗi token cho hầu hết các hệ thống |

Mỗi hệ thống được chạy trên cùng một cơ sở hạ tầng với cùng mô hình và ngân sách, được chấm điểm bởi một giám khảo đã được xác thực mù đối với một giám khảo thứ hai (đồng thuận 90.6%, Cohen's kappa 0.81). Bảng đầy đủ theo từng hệ thống, kết quả code-intelligence, và các lệnh tái tạo: **[BENCHMARKS.md](./BENCHMARKS.md)**.

---

## Yêu cầu tiên quyết

| Yêu cầu | Tối thiểu | Kiểm tra | Cài đặt |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(khuyến nghị)* | bất kỳ | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(thay thế)* | bất kỳ | `pipx --version` | `pip install pipx` |

**Cài đặt nhanh macOS (Homebrew):**
```bash
brew install python@3.12 uv
```

**Cài đặt nhanh Windows:**
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

## Cài đặt

> **Gói chính thức:** Gói PyPI là `graphifyy` (hai chữ y). Các gói `graphify*` khác trên PyPI không liên quan. Lệnh CLI vẫn là `graphify`.

**Bước 1 — cài đặt gói:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**Bước 2 — đăng ký skill với trợ lý AI của bạn:**

```bash
graphify install
```

Vậy là xong. Mở trợ lý AI của bạn và gõ `/graphify .`

Để cài đặt skill trợ lý vào repository hiện tại thay vì hồ sơ người dùng của bạn, thêm `--project`:

```bash
graphify install --project
graphify install --project --platform codex
```

Các bản cài đặt theo phạm vi dự án ghi vào thư mục hiện tại, ví dụ `.claude/skills/graphify/SKILL.md` hoặc `.agents/skills/graphify/SKILL.md` (cộng với một `references/` sidecar mà skill tải theo yêu cầu), và in ra gợi ý `git add` cho các tệp có thể commit được. Các lệnh theo từng nền tảng hỗ trợ cài đặt theo phạm vi dự án chấp nhận cùng một cờ, ví dụ `graphify claude install --project` hoặc `graphify codex install --project`.

> **Lưu ý PowerShell:** Sử dụng `graphify .` không phải `/graphify .` — dấu gạch chéo ở đầu là dấu phân cách đường dẫn trong PowerShell.

> **`graphify: command not found`?** `uv tool install` / `pipx install` đặt lệnh `graphify` vào thư mục bin công cụ của chúng (`~/.local/bin`). Nếu shell của bạn không tìm thấy nó ngay sau khi cài đặt — phổ biến trên một cài đặt macOS + zsh mới — thư mục đó chưa có trong `PATH` của bạn: chạy `uv tool update-shell` (hoặc `pipx ensurepath`), sau đó mở một terminal mới. Với `pip` đơn giản, thêm `~/.local/bin` (Linux) hoặc `~/Library/Python/3.x/bin` (Mac) vào PATH của bạn, hoặc chạy `python -m graphify`.

> **Chạy bằng `uvx` / `uv tool run` thay vì cài đặt?** Đặt tên gói, không phải lệnh: `uvx --from graphifyy graphify install`. `uvx graphify …` đơn giản sẽ thất bại (`No solution found … no versions of graphify`) vì `uv tool run` đọc từ đầu tiên là một *gói*, và gói là `graphifyy` — lệnh `graphify` sống bên trong nó.

> **Tránh `pip install` trên Mac/Windows** nếu có thể. Skill giải quyết Python tại thời điểm chạy từ `graphify-out/.graphify_python`; nếu nó trỏ đến một môi trường khác với nơi `pip` đã cài đặt gói, bạn sẽ nhận được `ModuleNotFoundError: No module named 'graphify'`. `uv tool install` và `pipx install` cô lập gói trong môi trường riêng của chúng và tránh hoàn toàn điều này.

> **Git hooks và uv tool / pipx:** `graphify hook install` nhúng đường dẫn interpreter hiện tại trực tiếp vào các script hook tại thời điểm cài đặt, để hook post-commit kích hoạt đúng cách ngay cả trong các client git GUI và CI runner nơi `~/.local/bin` không có trong PATH. Nếu bạn cài đặt lại hoặc nâng cấp graphify, chạy lại `graphify hook install` để làm mới đường dẫn được nhúng.

> **Chế độ nghiêm ngặt (Claude Code):** `graphify install --project --strict` làm cho trợ lý thực sự sử dụng đồ thị. Cài đặt mặc định *khuyến khích* chạy `graphify query` trước khi đọc tệp; chế độ nghiêm ngặt *chặn* lần đọc nguồn thô đầu tiên của một phiên và chuyển hướng nó đến đồ thị, sau đó quay lại chế độ khuyến khích (vì vậy nó kích hoạt tối đa một lần mỗi phiên và không bao giờ bị kẹt). Chuyển đổi tại thời điểm chạy bằng `GRAPHIFY_HOOK_STRICT=1`/`0`; cài đặt mặc định không thay đổi (khuyến khích nhẹ nhàng).

<details>
<summary><b>Chọn nền tảng của bạn</b> (hơn 20 trợ lý, nhấp để mở rộng)</summary>

| Nền tảng | Lệnh cài đặt |
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

Người dùng Codex cũng cần `multi_agent = true` dưới `[features]` trong `~/.codex/config.toml` để trích xuất song song. CodeBuddy sử dụng cùng cơ chế Agent tool và PreToolUse hook như Claude Code. Factory Droid sử dụng công cụ `Task` để gửi subagent song song. OpenClaw và Aider sử dụng trích xuất tuần tự (hỗ trợ agent song song vẫn còn ở giai đoạn sớm trên các nền tảng này). Trae sử dụng công cụ Agent để gửi subagent song song và **không** hỗ trợ hook `PreToolUse`, vì vậy AGENTS.md là cơ chế luôn bật.

`--platform agents` (bí danh `--platform skills`) nhắm đến các vị trí [Agent-Skills](https://github.com/anthropics/skills) chung, đa framework: `~/.agents/skills/` toàn cầu theo người dùng của đặc tả (được đọc bởi `npx skills` và các framework tuân thủ đặc tả) cho cài đặt toàn cầu, và `./.agents/skills/` cho cài đặt dự án (`--project`). `graphify install` đơn giản vẫn là một nền tảng duy nhất (Claude Code) theo thiết kế — sử dụng nền tảng có tên `agents` khi bạn muốn skill có thể được phát hiện bởi bất kỳ framework nào đọc `.agents/skills`.

> Codex sử dụng `$graphify` thay vì `/graphify`.

</details>

<details>
<summary><b>Các tiện ích bổ sung tùy chọn</b> (chỉ cài đặt những gì bạn cần)</summary>

| Tiện ích | Nó thêm gì | Cài đặt |
|---|---|---|
| `pdf` | Trích xuất PDF | `uv tool install "graphifyy[pdf]"` |
| `office` | Hỗ trợ `.docx` và `.xlsx` | `uv tool install "graphifyy[office]"` |
| `google` | Kết xuất Google Sheets | `uv tool install "graphifyy[google]"` |
| `video` | Phiên âm video/âm thanh (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | Máy chủ MCP stdio | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Hỗ trợ push Neo4j | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | Hỗ trợ push FalkorDB | `uv tool install "graphifyy[falkordb]"` |
| `svg` | Xuất đồ thị SVG | `uv tool install "graphifyy[svg]"` |
| `leiden` | Phát hiện cộng đồng Leiden (chỉ Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Suy luận Ollama cục bộ | `uv tool install "graphifyy[ollama]"` |
| `openai` | OpenAI / các API tương thích OpenAI | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic Claude API (`--backend claude`, sử dụng `ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (sử dụng IAM, không cần khóa API) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, sử dụng `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "graphifyy[openai]"` |
| `sql` | Trích xuất lược đồ SQL | `uv tool install "graphifyy[sql]"` |
| `postgres` | Kiểm tra nội bộ PostgreSQL trực tiếp (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | Trích xuất AST BYOND DreamMaker `.dm`/`.dme` (có thể cần trình biên dịch C + `python3-dev` nếu không có wheel khớp với nền tảng của bạn) | `uv tool install "graphifyy[dm]"` |
| `terraform` | Trích xuất AST Terraform / HCL `.tf`/`.tfvars`/`.hcl` | `uv tool install "graphifyy[terraform]"` |
| `pascal` | Trích xuất AST Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` (cạnh `calls`/`inherits` chính xác hơn; quay lại trình trích xuất regex khi không có) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | Phân đoạn truy vấn tiếng Trung (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | Tất cả những gì ở trên | `uv tool install "graphifyy[all]"` |

</details>

---

## Làm cho trợ lý của bạn luôn sử dụng đồ thị

Chạy lệnh này một lần trong dự án của bạn sau khi xây dựng đồ thị:

| Nền tảng | Lệnh |
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

Lệnh này ghi một tệp cấu hình nhỏ cho biết trợ lý của bạn tham khảo đồ thị tri thức cho các câu hỏi về codebase, ưu tiên các truy vấn có phạm vi như `graphify query "<question>"` hơn là đọc toàn bộ báo cáo hoặc grep các tệp thô.

- **Các nền tảng có hook** (Claude Code, Gemini CLI): một hook tự động kích hoạt trước các lời gọi công cụ kiểu tìm kiếm (và, trên Claude Code, trước khi đọc các tệp nguồn từng cái một thông qua các công cụ Read/Glob) và thúc đẩy trợ lý của bạn hướng đến đường dẫn đồ thị.
- **Các nền tảng dùng tệp hướng dẫn** (Codex, OpenCode, Cursor, v.v.): các tệp hướng dẫn cố định (`AGENTS.md`, `.cursor/rules/`, v.v.) cung cấp hướng dẫn ưu tiên truy vấn tương tự.

`GRAPH_REPORT.md` vẫn có sẵn để xem xét kiến trúc rộng.

**CodeBuddy** làm hai điều giống như Claude Code: viết một phần `CODEBUDDY.md` cho biết CodeBuddy đọc `graphify-out/GRAPH_REPORT.md` trước khi trả lời các câu hỏi về kiến trúc, và cài đặt các hook `PreToolUse` (`.codebuddy/settings.json`) kích hoạt trước các lệnh tìm kiếm Bash và đọc tệp, thúc đẩy hướng đến `graphify query`.

**Codex** ghi vào `AGENTS.md`, đây là thứ thực sự mang hướng dẫn đồ thị luôn bật trên nền tảng này. `graphify codex install` cũng đăng ký một hook `PreToolUse` trong `.codex/hooks.json` (`graphify hook-check`), nhưng mục đó cố ý là **no-op**: Codex Desktop từ chối `hookSpecificOutput.additionalContext` trên `PreToolUse`, vì vậy việc phát ra một sự thúc đẩy ở đó sẽ làm hỏng các lời gọi công cụ Bash. Không giống Claude Code, nơi hook (`graphify hook-guard`) làm việc thúc đẩy, trên Codex hook kích hoạt và cố ý không làm gì cả, và `AGENTS.md` là cơ chế luôn bật.

**Kilo Code** cài đặt skill Graphify vào `~/.config/kilo/skills/graphify/SKILL.md` và một lệnh `/graphify` gốc vào `~/.config/kilo/command/graphify.md`. `graphify kilo install` cũng ghi `AGENTS.md` cộng với một plugin `tool.execute.before` gốc (`.kilo/plugins/graphify.js` + đăng ký `.kilo/kilo.json` hoặc `.kilo/kilo.jsonc`) để Kilo nhận được cùng hành vi nhắc nhở đồ thị luôn bật thông qua cấu hình `.kilo` gốc.

**Cursor** ghi `.cursor/rules/graphify.mdc` với `alwaysApply: true`, vì vậy Cursor tự động bao gồm nó trong mọi cuộc trò chuyện, không cần hook.

Để xóa graphify khỏi tất cả các nền tảng cùng một lúc: `graphify uninstall` (thêm `--purge` để cũng xóa `graphify-out/`). Hoặc sử dụng lệnh theo từng nền tảng (ví dụ `graphify claude uninstall`).

---

## Những gì có trong báo cáo

- **God node** — các khái niệm được kết nối nhiều nhất trong dự án của bạn. Mọi thứ đều chảy qua chúng.
- **Kết nối bất ngờ** — các liên kết giữa những thứ nằm trong các tệp hoặc mô-đun khác nhau. Được xếp hạng theo mức độ bất ngờ của chúng.
- **"Tại sao"** — các bình luận trong dòng (`# NOTE:`, `# WHY:`, `# HACK:`), docstring, và lý do thiết kế từ tài liệu được trích xuất thành các node riêng biệt được liên kết với mã nguồn mà chúng giải thích.
- **Câu hỏi gợi ý** — 4–5 câu hỏi mà đồ thị được định vị đặc biệt tốt để trả lời.
- **Nhãn độ tin cậy** — mọi mối quan hệ được suy luận đều được đánh dấu `EXTRACTED`, `INFERRED`, hoặc `AMBIGUOUS`. Bạn luôn biết cái gì được tìm thấy so với cái gì được đoán.

---

## Nó xử lý những loại tệp nào

| Loại | Phần mở rộng |
|------|-----------|
| Mã nguồn (36 ngữ pháp tree-sitter) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme` cần `uv tool install graphifyy[dm]`; `.mts`/`.cts` tái sử dụng ngữ pháp TypeScript, `.cc`/`.cxx` và CUDA `.cu`/`.cuh` và Metal `.metal` tái sử dụng ngữ pháp C++) |
| Salesforce Apex | `.cls .trigger` (dựa trên regex; các lớp, giao diện, enum, phương thức, trigger, cạnh SOQL/DML) |
| Terraform / HCL | `.tf .tfvars .hcl` (cần `uv tool install graphifyy[terraform]`) |
| Cấu hình MCP | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — trích xuất các node máy chủ, tham chiếu gói, yêu cầu biến môi trường |
| Manifest gói | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — một node gói chuẩn cho mỗi gói (theo tên) cộng với các cạnh `depends_on`, để một gói được tham chiếu từ nhiều manifest là một hub duy nhất |
| Tài liệu | `.md .mdx .qmd .html .txt .rst .yaml .yml` (các liên kết markdown `[text](./other.md)` và `[[wikilinks]]` trở thành các cạnh `references` giữa các tài liệu) |
| Office | `.docx .xlsx` (cần `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (tùy chọn; cần xác thực `gws` và `--google-workspace`; Sheets cần `uv tool install graphifyy[google]`) |
| PDF | `.pdf` |
| Hình ảnh | `.png .jpg .webp .gif` |
| Video / Âm thanh | `.mp4 .mov .mp3 .wav` và nhiều hơn nữa (cần `uv tool install graphifyy[video]`) |
| YouTube / URL | bất kỳ URL video nào (cần `uv tool install graphifyy[video]`) |

Mã nguồn được trích xuất **cục bộ không có lời gọi API** (AST thông qua tree-sitter). Mọi thứ khác đi qua API mô hình của trợ lý AI của bạn.

Các tệp `.gdoc`, `.gsheet`, và `.gslides` của Google Drive for desktop là các con trỏ shortcut, không phải nội dung tài liệu. Để bao gồm Google Docs, Sheets, và Slides gốc trong một lần trích xuất headless, hãy cài đặt và xác thực [`gws` CLI](https://github.com/googleworkspace/cli), sau đó chạy:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

Bạn cũng có thể đặt `GRAPHIFY_GOOGLE_WORKSPACE=1`. Graphify xuất các shortcut vào `graphify-out/converted/` dưới dạng các tệp Markdown phụ trợ, sau đó trích xuất các tệp đó.

---

## Các lệnh thường dùng

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

Xem [Decouple: các ứng viên Extract-Class được chấm điểm rủi ro](#decouple-risk-scored-extract-class-candidates) ở trên, hoặc [tài liệu tham khảo lệnh đầy đủ](#full-command-reference) bên dưới.

---

## Bỏ qua các tệp

Tạo một `.graphifyignore` ở gốc dự án của bạn — cú pháp giống như `.gitignore`, bao gồm cả phủ định `!`.

**`.gitignore` được tôn trọng tự động.** graphify đọc `.gitignore` trong mỗi thư mục. Nếu một `.graphifyignore` cũng hiện diện, hai cái đó được **hợp nhất** — các mẫu `.graphifyignore` được đánh giá cuối cùng, vì vậy chúng thắng khi xung đột (bao gồm cả phủ định `!`). Việc thêm một `.graphifyignore` chỉ bao giờ loại trừ thêm; nó không bao giờ đưa lại một tệp mà `.gitignore` của bạn đã loại trừ. Phạm vi thư mục con hoạt động giống hệt như git — một tệp bỏ qua chỉ ảnh hưởng đến cây con của chính nó.

Truyền `--no-gitignore` cho `graphify extract` khi mã nguồn được tạo hoặc chuyển đổi bị git bỏ qua thuộc về đồ thị. Điều này vô hiệu hóa `.gitignore` và `.git/info/exclude`; `.graphifyignore` vẫn được áp dụng.

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

## Thiết lập nhóm

`graphify-out/` được thiết kế để commit vào git để mọi người trong nhóm bắt đầu với một bản đồ.

**Các bổ sung `.gitignore` được khuyến nghị:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` giờ đây có thể di chuyển được — các khóa được lưu trữ dưới dạng đường dẫn tương đối và được neo lại khi tải, vì vậy việc commit nó là an toàn và tránh việc xây dựng lại toàn bộ khi checkout lần đầu.

**Quy trình làm việc:**
1. Một người chạy `/graphify .` và commit `graphify-out/`.
2. Mọi người pull — trợ lý của họ đọc đồ thị ngay lập tức.
3. Chạy `graphify hook install` để tự động xây dựng lại sau mỗi commit (chỉ AST, không tốn chi phí API). Điều này cũng thiết lập một git merge driver để `graph.json` không bao giờ bị bỏ lại với các dấu hiệu xung đột — hai nhà phát triển commit song song sẽ có đồ thị của họ được hợp nhất tự động.
4. Khi tài liệu hoặc bài báo thay đổi, chạy `/graphify --update` để làm mới các node đó.

---

## Sử dụng đồ thị trực tiếp

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

Máy chủ MCP cung cấp cho trợ lý của bạn quyền truy cập có cấu trúc: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Máy chủ HTTP dùng chung

`--transport stdio` (mặc định) khởi chạy một máy chủ cục bộ cho mỗi nhà phát triển. `--transport http` phục vụ các công cụ tương tự qua giao thức MCP Streamable HTTP, vì vậy một quy trình dùng chung duy nhất có thể phục vụ đồ thị cho toàn bộ nhóm — các client trỏ cấu hình MCP IDE của họ vào `http://<host>:8080/mcp` thay vì chạy graphify cục bộ.

| Cờ | Mặc định | Mục đích |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Giao thức để phục vụ |
| `--host` | `127.0.0.1` | Host liên kết HTTP (sử dụng `0.0.0.0` để mở ra ngoài localhost) |
| `--port` | `8080` | Cổng liên kết HTTP |
| `--api-key` | env `GRAPHIFY_API_KEY` | Yêu cầu `Authorization: Bearer <key>` (hoặc `X-API-Key`) |
| `--path` | `/mcp` | Đường dẫn mount HTTP |
| `--json-response` | tắt | Trả về JSON thuần thay vì luồng SSE |
| `--stateless` | tắt | Không có trạng thái mỗi phiên (cho các triển khai load-balanced / CI) |
| `--session-timeout` | `3600` | Dọn dẹp các phiên stateful không hoạt động sau N giây (`0` vô hiệu hóa) |

Liên kết `127.0.0.1` mặc định chỉ là loopback. Đặt `--host 0.0.0.0` **và** `--api-key` cùng nhau khi mở trên một host dùng chung. Chạy nó trong một container:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **Lưu ý WSL / Linux:** Ubuntu cung cấp `python3`, không phải `python`. Sử dụng venv để tránh xung đột:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## Biến môi trường

Những biến này chỉ cần thiết cho việc trích xuất **headless / CI** (`graphify extract`). Khi chạy qua skill `/graphify` bên trong IDE của bạn, API mô hình được cung cấp bởi phiên IDE của bạn — không cần khóa bổ sung.

| Biến | Dùng cho | Khi nào cần thiết |
|---|---|---|
| `ANTHROPIC_API_KEY` | Backend Claude (Anthropic) | `--backend claude` |
| `ANTHROPIC_BASE_URL` | URL endpoint tương thích Anthropic (proxy LiteLLM, gateway, ...) | `--backend claude` (mặc định: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Tên mô hình cho backend Claude — cho các endpoint tùy chỉnh, sử dụng tên/bí danh mô hình mà máy chủ của bạn cung cấp | `--backend claude` (mặc định: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` hoặc `GOOGLE_API_KEY` | Backend Google Gemini | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI hoặc các API tương thích OpenAI | `--backend openai` (máy chủ cục bộ chấp nhận bất kỳ giá trị không rỗng nào) |
| `OPENAI_BASE_URL` | URL máy chủ tương thích OpenAI (llama.cpp, vLLM, LM Studio, ...) | `--backend openai` (mặc định: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | Tên mô hình cho backend OpenAI — cho các máy chủ self-hosted, sử dụng tên/bí danh mô hình mà máy chủ của bạn cung cấp (kiểm tra endpoint `/v1/models` của nó), ví dụ `LFM2.5-8B-A1B-UD-Q4_K_XL` cho llama.cpp | `--backend openai` (mặc định: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | Backend DeepSeek | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Backend Kimi Code | `--backend kimi` |
| `OLLAMA_BASE_URL` | URL suy luận Ollama cục bộ | `--backend ollama` (mặc định: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Tên mô hình Ollama | `--backend ollama` (mặc định: tự động phát hiện) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Ghi đè kích thước cửa sổ KV-cache của Ollama | tùy chọn — tự động định kích thước theo mặc định |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Số phút giữ mô hình Ollama đã tải | tùy chọn — đặt `0` để dỡ tải sau mỗi phần |
| `AZURE_OPENAI_API_KEY` | Backend Azure OpenAI Service | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | URL endpoint tài nguyên Azure | `--backend azure` (bắt buộc kèm theo khóa API) |
| `AZURE_OPENAI_API_VERSION` | Ghi đè phiên bản API Azure | tùy chọn — mặc định `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` hoặc `GRAPHIFY_AZURE_MODEL` | Tên triển khai Azure | tùy chọn — mặc định `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — chuỗi thông tin xác thực tiêu chuẩn | `--backend bedrock` (không cần khóa API, sử dụng IAM) |
| `GRAPHIFY_MAX_WORKERS` | Số luồng song song hóa AST | tùy chọn — cũng có cờ `--max-workers` |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Tăng giới hạn đầu ra cho các corpus dày đặc | tùy chọn — ví dụ `32768` cho các tệp lớn |
| `GRAPHIFY_API_TIMEOUT` | Thời gian chờ mỗi lệnh gọi tính bằng giây cho các backend HTTP, claude-cli, Anthropic SDK, và Bedrock (mặc định: 600) | tùy chọn — cũng có cờ `--api-timeout` |
| `GRAPHIFY_MAX_RETRIES` | Số lần thử lại một yêu cầu bị giới hạn tốc độ (429) trước khi từ bỏ (mặc định: 6; tôn trọng `Retry-After`) | tùy chọn — tăng lên cho các giới hạn nghiêm ngặt theo tổ chức (ví dụ kimi); `0` vô hiệu hóa |
| `GRAPHIFY_FORCE` | Buộc xây dựng lại đồ thị ngay cả khi có ít node hơn | tùy chọn — cũng có cờ `--force` |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Tự động bật xuất Google Workspace | tùy chọn — đặt thành `1` |
| `GRAPHIFY_TRIAGE_BACKEND` | Backend cho `graphify prs --triage` | tùy chọn — tự động phát hiện từ các khóa có sẵn |
| `GRAPHIFY_TRIAGE_MODEL` | Ghi đè mô hình cho triage | tùy chọn — ví dụ `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | Đặt thành `1` để bật nhật ký truy vấn cục bộ tại `~/.cache/graphify-queries.log` (ghi lại mỗi câu hỏi query/path/explain + đường dẫn corpus). Tắt theo mặc định — không có gì được ghi trừ khi bạn tham gia (#1797) | tùy chọn |
| `GRAPHIFY_QUERY_LOG` | Bật nhật ký truy vấn và ghi nó vào đường dẫn này thay vì mặc định | tùy chọn — tắt trừ khi cái này hoặc `_ENABLE` được đặt |
| `GRAPHIFY_QUERY_LOG_DISABLE` | Đặt thành `1` để buộc tắt nhật ký truy vấn (thắng các biến enable) | tùy chọn |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | Khi nhật ký được bật, cũng ghi lại các phản hồi đồ thị con đầy đủ (tắt theo mặc định) | tùy chọn |
| `GRAPHIFY_MAX_GRAPH_BYTES` | Ghi đè giới hạn kích thước 512 MiB của graph.json — ví dụ `700MB`, `2GB`, hoặc byte thuần | tùy chọn — hữu ích cho các corpus rất lớn |
| `GRAPHIFY_MAX_CONTEXTS` | Số lượng tối đa các đồ thị dự án không mặc định mà một máy chủ MCP đa dự án duy nhất giữ lại | tùy chọn — mặc định: `8`; các giá trị không hợp lệ sử dụng `8`, và các giá trị dưới `1` sử dụng `1` |
| `GRAPHIFY_LLM_TEMPERATURE` | Ghi đè nhiệt độ LLM cho trích xuất ngữ nghĩa — ví dụ `0.7`, hoặc `none` để bỏ qua | tùy chọn — tự động bỏ qua đối với các mô hình suy luận o1/o3/o4/gpt-5 |

---

## Quyền riêng tư

- **Tệp mã nguồn** — được xử lý cục bộ qua tree-sitter. Không có gì rời khỏi máy của bạn. Một corpus chỉ có mã nguồn không cần khóa API — `graphify extract` chạy hoàn toàn ngoại tuyến. Trên một repository hỗn hợp, thêm `--code-only` để chỉ lập chỉ mục mã nguồn và bỏ qua các tài liệu/PDF/hình ảnh mà nếu không sẽ cần LLM.
- **Video / âm thanh** — được phiên âm cục bộ bằng faster-whisper. Không có gì rời khỏi máy của bạn.
- **Tài liệu, PDF, hình ảnh** — được gửi đến trợ lý AI của bạn để trích xuất ngữ nghĩa (thông qua skill `/graphify`, sử dụng bất kỳ mô hình nào mà phiên IDE của bạn chạy). `graphify extract` headless yêu cầu `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), một instance Ollama đang chạy (`OLLAMA_BASE_URL`), thông tin xác thực AWS thông qua chuỗi provider tiêu chuẩn (Bedrock - không cần khóa API, sử dụng IAM), hoặc tệp nhị phân CLI `claude` (Claude Code - không cần khóa API, sử dụng đăng ký Claude của bạn). Cờ `--dedup-llm` sử dụng cùng khóa.
- **Vị trí dữ liệu** — `graphify extract` tự động phát hiện provider nào để sử dụng dựa trên khóa API nào được đặt (thứ tự ưu tiên: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). Đối với mã nguồn có yêu cầu về vị trí dữ liệu, sử dụng `--backend ollama` (hoàn toàn cục bộ) hoặc truyền một cờ `--backend` rõ ràng. Kimi (`MOONSHOT_API_KEY`) định tuyến đến các máy chủ Moonshot AI ở Trung Quốc.
- **Không có telemetry**, không theo dõi sử dụng, không phân tích.
- **Ghi nhật ký truy vấn** — mỗi lệnh gọi `graphify query`, `graphify path`, `graphify explain`, và MCP `query_graph` được ghi vào `~/.cache/graphify-queries.log` ở định dạng JSON Lines (dấu thời gian, câu hỏi, corpus, các node được trả về, thời lượng). Các phản hồi đồ thị con đầy đủ **không** được lưu trữ theo mặc định. Đặt `GRAPHIFY_QUERY_LOG_DISABLE=1` để từ chối, hoặc `GRAPHIFY_QUERY_LOG=/dev/null` để tắt tiếng mà không vô hiệu hóa đường dẫn mã nguồn.

---

## Khắc phục sự cố

**`graphify: command not found` sau khi cài đặt**
CLI đã được cài đặt nhưng thư mục bin của nó không có trong `PATH` shell của bạn. Chọn cách khắc phục cho cách bạn đã cài đặt:
- **uv** (`uv tool install graphifyy`): lệnh nằm trong thư mục bin công cụ của uv (`~/.local/bin`), nơi mà một cài đặt macOS/zsh mới thường không có trong `PATH`. Chạy `uv tool update-shell`, sau đó mở một terminal mới. (Tìm thư mục bằng `uv tool dir --bin`.)
- **pipx** (`pipx install graphifyy`): chạy `pipx ensurepath`, sau đó mở một terminal mới.
- **pip** (`pip install graphifyy`): pip cài đặt các script vào một thư mục bin người dùng có thể không có trong `PATH` — thêm `~/Library/Python/3.x/bin` (macOS) hoặc `~/.local/bin` (Linux) vào PATH của bạn trong `~/.zshrc`/`~/.bashrc`, hoặc chỉ cần chạy `python -m graphify`.

**`uvx graphify …` hoặc `uv tool run graphify …` không giải quyết được `graphify`**
Gói PyPI là `graphifyy`; `graphify` chỉ là lệnh mà nó cung cấp. `uv tool run` coi từ đầu tiên là một *tên gói*, vì vậy nó tìm kiếm một gói tên là `graphify` và báo cáo `No solution found … no versions of graphify`. Đặt tên gói một cách rõ ràng: `uvx --from graphifyy graphify install` (giống như `uv tool run --from graphifyy graphify install`). Hoặc `uv tool install graphifyy` một lần rồi gọi `graphify` trực tiếp.

**`uv run --with graphifyy python -m graphify` âm thầm chạy một bản cài đặt cũ hơn**
`uv run` sử dụng Python *hệ thống* của bạn, vì vậy nếu một `graphifyy` cũ hơn cũng sống ở đó (ví dụ một `pip install graphifyy` trong quá khứ), Python có thể tìm thấy bản sao đó trước tiên trên `sys.path` và `--with graphifyy` sẽ không ghi đè nó. Nó chạy mà không có lỗi, nhưng bạn nhận được hành vi của phiên bản *cũ* — ví dụ các ghi đè môi trường như `OPENAI_BASE_URL` bị âm thầm bỏ qua, vì vậy các yêu cầu chạm vào endpoint mặc định và thất bại với 401 trông giống như một khóa xấu. Dấu vân tay là một dòng `warning: skill is from graphify <newer>, package is <older>` — điều đó có nghĩa là một bản cài đặt khác đã được tải, không chỉ là một skill cũ. Kiểm tra bản sao nào thực sự đã được tải:
```bash
python -c "import graphify; print(graphify.__file__)"
```
Sau đó chạy trực tiếp lệnh đã cài đặt (nó sử dụng bản sao được quản lý bởi uv), hoặc gỡ bỏ bản sao hệ thống cũ:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` hoạt động nhưng lệnh `graphify` thì không**
`PATH` shell của bạn không bao gồm thư mục bin nơi lệnh được cài đặt. Ưu tiên `uv tool install` / `pipx install` hơn `pip` thuần, sau đó chạy `uv tool update-shell` / `pipx ensurepath` và mở một terminal mới (xem các ghi chú cài đặt ở trên).

**`/graphify .` gây ra "path not recognized" trong PowerShell**
PowerShell coi dấu `/` ở đầu là dấu phân cách đường dẫn. Sử dụng `graphify .` (không có dấu gạch chéo) trên Windows.

**Đồ thị có ít node hơn sau `--update` hoặc xây dựng lại**
Nếu một lần tái cấu trúc đã xóa các tệp, các node cũ vẫn còn lại. Truyền `--force` (hoặc đặt `GRAPHIFY_FORCE=1`) để ghi đè ngay cả khi việc xây dựng lại có ít node hơn.

**`extract` thoát với "extraction was incomplete ... refusing to overwrite"**
Khi một lần trích xuất bị sập hoặc một lần duyệt không thể đọc đầy đủ corpus, lần chạy đó sẽ nhỏ hơn một lần chạy hoàn chỉnh, vì vậy `graphify extract` từ chối ghi đè một đồ thị hiện có lớn hơn bằng kết quả một phần (bảo vệ `graph.json` của bạn). Sửa lỗi cơ bản và chạy lại, hoặc truyền `--allow-partial` để ghi đè dù sao đi nữa.

**Đồ thị có các node trùng lặp cho cùng một thực thể (bản sao ma)**
Các bản sao ma (cùng một ký hiệu xuất hiện hai lần — một lần từ trích xuất AST với vị trí nguồn, một lần từ trích xuất ngữ nghĩa không có) giờ đây được tự động hợp nhất tại thời điểm xây dựng. Nếu bạn thấy điều này trong một đồ thị được xây dựng trước v0.8.33, chạy một lần trích xuất lại hoàn toàn để dọn dẹp:
```bash
graphify extract . --force
```

**Ollama hết VRAM / vượt quá cửa sổ context**
Cửa sổ KV-cache tự động định kích thước nhưng có thể quá lớn cho GPU của bạn. Giảm nó:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**Cảnh báo `LLM returned invalid JSON` / `Unterminated string`**
Phản hồi JSON của mô hình đã chạm giới hạn output-token và bị cắt giữa chuỗi. graphify tự động khôi phục (nó chia phần và trích xuất lại các nửa, và một tài liệu đơn lẻ quá lớn trước tiên được cắt tại ranh giới tiêu đề/đoạn văn để toàn bộ tệp vẫn được bao phủ), vì vậy những cảnh báo này ồn ào nhưng không phải mất dữ liệu. Để giảm sự ồn ào, tăng giới hạn đầu ra hoặc thu nhỏ đầu ra của mỗi phần:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
Với một cổng cloud như OpenRouter, ưu tiên `--backend openai` (đặt `OPENAI_BASE_URL`) hơn shim Ollama — đó là một đường dẫn tương thích OpenAI sạch hơn. Nếu mô hình có giới hạn max-output riêng của nó, việc giảm `--token-budget` là một đòn bẩy đáng tin cậy.

**Graph HTML quá lớn để mở trong trình duyệt (>5000 node)**
Bỏ qua việc tạo HTML và sử dụng JSON trực tiếp:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**`graph.json` có các dấu hiệu xung đột sau khi hai nhà phát triển commit cùng lúc**
Chạy `graphify hook install` — nó thiết lập một git merge driver hợp nhất `graph.json` tự động để xung đột không bao giờ xảy ra.

**Trích xuất trả về node/cạnh trống cho tài liệu hoặc PDF**
Tài liệu, PDF, và hình ảnh yêu cầu một lệnh gọi LLM — các corpus chỉ có mã nguồn không cần khóa. Kiểm tra rằng khóa API của bạn được đặt và backend đúng:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**Cảnh báo không khớp phiên bản skill trong IDE của bạn**
Phiên bản graphify đã cài đặt của bạn khác với tệp skill. Cập nhật:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**Bộ nhớ đệm prompt của Claude Code bị vô hiệu sau mỗi lần `graphify extract`**
Graphify ghi các tệp đầu ra (`graph.json`, `graphify-out/`) vào workspace. Nếu các đường dẫn đó không bị bỏ qua, mỗi lần ghi sẽ vô hiệu hóa bộ nhớ đệm prompt của Claude Code, buộc tải lên lại toàn bộ với tốc độ ghi bộ nhớ đệm ở lượt tiếp theo. Thêm chúng vào `.claudeignore`:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## Tài liệu tham khảo lệnh đầy đủ

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

> **Tên cộng đồng:** bên trong một agent (Claude Code, Gemini CLI) chính agent đặt tên cho các cộng đồng. Khi bạn chạy CLI trần, `cluster-only` tự động đặt tên chúng bằng backend đã cấu hình (tích hợp sẵn hoặc provider tương thích OpenAI tùy chỉnh) — truyền `--no-label` để giữ `Community N`, hoặc chạy `graphify label` để tạo (lại) tên theo yêu cầu.

---

## Tìm hiểu thêm

- [Cách nó hoạt động](docs/how-it-works.md) — quy trình trích xuất, phát hiện cộng đồng, chấm điểm độ tin cậy, các bài kiểm tra chuẩn
- [ARCHITECTURE.md](ARCHITECTURE.md) — phân tích mô-đun, cách thêm một ngôn ngữ
- [Tích hợp tùy chọn](docs/docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — cuốn sách về những ý tưởng đằng sau graphify, kiến trúc từ đầu đến cuối

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) là lớp luôn bật được xây dựng trên nền graphify — nó áp dụng cùng cách tiếp cận đồ thị cho toàn bộ bối cảnh làm việc của bạn: các cuộc họp, tệp, tài liệu, và mã nguồn, cập nhật liên tục trong nền.

Được xây dựng cho những người và nhóm có công việc sống trong hàng trăm cuộc trò chuyện và tài liệu mà họ không bao giờ có thể tái tạo lại đầy đủ.

**[Tham gia danh sách chờ tại graphify.com](https://graphify.com).** Bản dùng thử miễn phí sắp ra mắt.

---

<details>
<summary>Đóng góp</summary>

### Thiết lập môi trường phát triển

Dự án sử dụng [uv](https://docs.astral.sh/uv/) cho quy trình phát triển. Cài đặt nó một lần, sau đó:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

Xác minh cài đặt editable:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### Chạy các bài kiểm thử

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> Lưu ý macOS: bộ kiểm thử bao gồm cả fixture `sample.f90` và `sample.F90`. Những thứ này xung đột trên các hệ thống tệp không phân biệt chữ hoa/thường như HFS+ / APFS. Chạy trên Linux hoặc trong một container Docker nếu bạn cần kiểm thử cả hai biến thể Fortran đồng thời.

### Quy trình làm việc Git

- Phát triển tích cực diễn ra trên nhánh `v8`.
- Kiểu commit: `fix: <description>` / `feat: <description>` / `docs: <description>`
- Trước khi mở một PR, chạy `uv run pytest tests/ -q` và xác nhận nó vượt qua.
- Thêm một tệp fixture vào `tests/fixtures/` và các bài kiểm thử vào `tests/test_languages.py` cho bất kỳ trình trích xuất ngôn ngữ mới nào.

### Những gì nên đóng góp

**Các ví dụ đã hoàn thiện (worked examples)** là đóng góp hữu ích nhất. Chạy `/graphify` trên một corpus thực tế, lưu đầu ra vào `worked/{slug}/`, viết một `review.md` trung thực bao gồm những gì đồ thị làm đúng và sai, và mở một PR.

**Lỗi trích xuất** — mở một issue với tệp đầu vào, mục cache (`graphify-out/cache/`), và những gì bị thiếu hoặc sai.

Xem [ARCHITECTURE.md](ARCHITECTURE.md) để biết trách nhiệm mô-đun và cách thêm một ngôn ngữ.

</details>
