<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>Fork dari <a href="https://github.com/Graphify-Labs/graphify">graphify</a> yang menambahkan <code>graphify decouple</code></b> — kandidat Extract-Class untuk god object dengan skor risiko, 0-LLM, yang diverifikasi ulang terhadap kode sumber sesungguhnya (bukan hanya call graph) sebelum merekomendasikan apa pun. Lihat <a href="#decouple-kandidat-extract-class-dengan-skor-risiko">Decouple: kandidat Extract-Class dengan skor risiko</a> di bawah.
</p>

<div align="center">
<details><summary><b>Baca dalam bahasa lain</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>Akses awal ke platform graphify sudah dibuka sebelum peluncuran publik v1: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

Ketik `/graphify` di asisten coding AI Anda, dan seluruh proyek Anda (kode, dokumen, PDF, gambar, video) akan dipetakan menjadi **knowledge graph** yang bisa Anda **query**, bukan sekadar di-grep dari file demi file.

- **Peta kode gratis, dan sepenuhnya lokal.** Kode diparsing dengan AST tree-sitter: deterministik, tanpa LLM, tidak ada yang keluar dari mesin Anda. (Dokumen, PDF, gambar, dan video menggunakan model asisten Anda, atau API key yang telah dikonfigurasi, untuk proses semantik.)
- **Setiap edge punya penjelasan.** Setiap koneksi ditandai `EXTRACTED` (eksplisit di kode sumber) atau `INFERRED` (diselesaikan oleh graphify), sehingga Anda bisa tahu mana yang dibaca langsung dan mana yang disimpulkan.
- **Bukan vector index.** Tidak ada embedding, tidak ada vector store: ini graf sungguhan yang bisa Anda telusuri. Ajukan pertanyaan, telusuri jalur antara dua hal, atau minta penjelasan satu konsep.

> Ingin ini selalu aktif, terus diperbarui di latar belakang lintas kode, dokumen, dan rapat Anda, bukan hanya saat diminta? Itulah yang kami bangun di **[graphify.com](https://graphify.com)**, dan akses awal sudah dibuka sekarang di **[app.graphify.com](https://app.graphify.com/login)**.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="graph.html interaktif dari graphify menampilkan codebase FastAPI sebagai knowledge graph force-directed dengan legenda komunitas yang terdeteksi" width="900">
</p>
<p align="center">
  <em>Codebase FastAPI yang dipetakan oleh graphify. Setiap node adalah sebuah konsep, warna menunjukkan komunitas yang terdeteksi, dan semuanya bisa diklik di graph.html.</em>
</p>

**Mulai dalam** (30 detik):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

Lalu, di asisten AI Anda:

```
/graphify .
```

Selesai. Anda mendapatkan **tiga file**:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**Berjalan di** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, dan 15+ lainnya — [pilih platform Anda](#instalasi).

---

## Lihat Langsung Aksinya

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="Query jalur graphify: sebuah terminal menanyakan jalur terpendek antara FastAPI dan ModelField, dan jawabannya menyala hop demi hop di sepanjang knowledge graph" width="900">
</p>

Setelah graf terbentuk, Anda meng-query-nya, bukan membaca file. Output nyata, hasil menjalankan graphify pada codebase FastAPI di atas:

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

Setiap edge membawa **tag kepercayaan** (`EXTRACTED` = eksplisit di kode sumber, `INFERRED` = diturunkan melalui resolusi), sehingga Anda bisa tahu mana yang dibaca langsung dan mana yang disimpulkan. `graphify query "<question>"` mengembalikan subgraf yang terlingkupi untuk pertanyaan berbahasa natural, dan `graphify path A B` menelusuri bagaimana dua hal saling terhubung.

---

## Decouple: kandidat Extract-Class dengan skor risiko

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: god node MainWindow terpecah menjadi kelas-kelas kandidat dengan skor risiko, dengan peringatan shared-state antara dua di antaranya" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: 5 kelas yang diusulkan untuk MainWindow, panel Node Info terbuka pada Main Window Axis and Range Controls menunjukkan overlap state 0.608 dengan Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>DECOUPLE.html pada jalankan nyata — mengklik satu kelas yang diusulkan menunjukkan tepat kelas mana lagi yang berbagi state dengannya, dan apa persisnya yang dibagikan.</em>
</p>

Halaman yang sama juga merender pemecahannya sendiri. Mengaktifkan **Preview decoupled view** menukar method milik god class dengan kelas-kelas yang diusulkan dan merutekan ulang edge-nya di tempat — perubahan sambungannya, bukan diagram yang digambar ulang:

| Sebelum — god class hari ini | Sesudah — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html sebelum toggle: satu node hub MainWindow dengan method-method miliknya terbentang di sekelilingnya" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html sesudah toggle: node yang sama menyusut menjadi 5 kelas usulan berbentuk belah ketupat, edge hijau putus-putus menunjukkan method mana yang diekstrak ke masing-masing, edge merah menunjukkan state instance yang masih dibagi antara dua di antaranya" width="440"> |
| Satu node berisi 47 method miliknya sendiri, yang setiap satunya hanya bisa dijangkau lewat kelas itu. | Kelas-kelas yang diusulkan. Hijau putus-putus = apa yang diekstrak ke masing-masing; merah = state instance yang masih dibagi dua di antaranya, dan itulah yang menentukan `split` atau `keep_as_is`. Hanya kandidat yang lolos ambang risiko yang digambar — di sini 5 dari 6, itulah sebabnya satu method tidak punya belah ketupat untuk mendarat. |

`graphify decouple` menemukan god object dan memberi tahu Anda apakah memecahnya benar-benar sepadan — bukan sekadar bahwa objek itu besar.

Pola kegagalan yang ingin ditangkap alat ini: sebuah kelas dengan 47 method yang dengan senang hati dipecah oleh clustering berbasis call graph menjadi 5 kelompok yang tampak rapi, padahal semuanya masih membaca dan menulis instance state `self._chart_style` / `self._crosshair` yang sama persis di bawahnya. Jika Anda merilis pemecahan seperti itu, Anda belum men-decouple apa pun — Anda hanya memindahkan method ke file baru yang tetap tidak bisa diuji, diubah, atau dipahami secara independen, karena semuanya masih memerlukan shared state yang sama untuk dioper balik. Alat yang hanya melihat call graph sama sekali tidak bisa melihat ini; ia harus kembali ke kode sumber sesungguhnya.

**Dua pemeriksaan, keduanya 0-LLM, keduanya deterministik:**

1. **Apakah ini benar-benar God Object?** Node dengan degree tinggi bisa jadi God Object sejati (banyak method miliknya SENDIRI, tersebar di tanggung jawab yang tidak berkaitan — Extract Class relevan) atau hub/data model yang terlalu banyak dirujuk (sedikit method miliknya sendiri, sebagian besar referensi yang *masuk*) — memecah tubuhnya tidak menghasilkan apa-apa; perbaikannya adalah mempersempit interface-nya, bukan mengekstrak kelas. `classify_god_node` membedakan keduanya berdasarkan `member_ratio`, bukan degree mentah — perbedaan inilah yang menyelamatkan `TraceSource` (84 edge, tetapi hanya 6 method miliknya sendiri) dari saran pemecahan yang keliru, sementara `MainWindow` (88 edge, 47 method miliknya sendiri) dengan tepat mendapatkan saran tersebut.
2. **Apakah pemecahan ini benar-benar mengurangi coupling?** `risk_before` (ukuran, coupling, dan fragmentasi god node saat ini) dibandingkan dengan `risk_after` — risiko BARU yang justru ditimbulkan oleh pemecahan itu sendiri: pemanggilan antar-grup yang sebelumnya berupa edge internal kelas yang tak terlihat lalu berubah menjadi dependensi eksplisit antar-kelas, pemanggil (caller) yang kini harus bergantung pada lebih dari satu kelas baru, dan — pemeriksaan yang secara struktural tidak mungkin dilakukan oleh call graph — seberapa banyak state instance `self`/`this` (baca, tulis, dan pemanggilan helper method bersama, masing-masing diberi bobot berbeda: **penulisan** bersama diberi skor lebih tinggi daripada pembacaan bersama) yang benar-benar dimiliki bersama oleh grup-grup yang diusulkan. Ini mem-parsing ulang file sumber god node itu sendiri secara langsung dengan tree-sitter; ia tidak bergantung pada graf hasil ekstraksi graphify sendiri, yang tidak pernah mencatat akses tingkat field untuk bahasa apa pun. Hanya ketika `risk_after` berada di bawah `risk_before` melewati ambang tertentu, rencana akan merekomendasikan `split` — selain itu hasilnya `marginal` atau `keep_as_is`, dan kandidat yang tidak dianjurkan dilaporkan sebagai angka, bukan digambar sebagai bentuk yang harus Anda ragukan sendiri secara visual.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

Menghasilkan tiga file di samping `graph.json`:

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

**Dukungan bahasa untuk pemeriksaan shared-state** (klasifikasi berbasis call-graph di atas bekerja untuk semua bahasa yang bisa diekstrak graphify; tabel ini secara spesifik untuk parsing ulang kode sumber yang memverifikasi overlap state `self`/`this`):

| Language | Supported | Notes |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` is its own AST node, not a wrapped field access — handled explicitly |
| C# | ✅ | |
| Rust | ✅ | `self.x` via `impl` blocks |
| Ruby | ✅ | `@x` (the dominant idiom) + `self.foo` calls |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | per-method receiver resolution — Go has no `self`/`this` keyword, so the receiver name (`f` in `func (f *Foo) M()`) is resolved fresh for every method |
| C | ❌ | a struct-pointer parameter has no syntactic marker distinguishing it from any other parameter — no reliable signal without full type inference |

God node dalam bahasa yang tidak didukung, atau yang kode sumbernya tidak bisa dibaca, ditandai `state_analysis: "skipped"` — klasifikasi dan skor call-graph tetap berjalan, tetapi rekomendasinya bersandar pada call graph saja, bukan diam-diam berasumsi bahwa pemeriksaan state lolos.

---

## Apa yang Dilakukannya

Yang Anda dapatkan langsung dari awal:

| Capability | What you get |
|---|---|
| **God nodes** | The most-connected concepts, so you see what everything flows through |
| **Communities** | The graph split into subsystems (Leiden), with LLM-free labels |
| **Cross-file links** | `calls` / `imports` / `inherits` / `mixes_in` resolved across ~40 languages via tree-sitter AST |
| **Query, path, explain** | Ask a question, trace the path between two things, or explain one concept, all against `graph.json` |
| **Rationale + doc refs** | `# NOTE:` / `# WHY:` comments and ADR/RFC citations become first-class nodes linked to the code |
| **Beyond code** | Docs, PDFs, images, and video/audio all map into the same graph |
| **Local-first** | Code is parsed locally with tree-sitter (no LLM, nothing leaves your machine); only the semantic pass over docs/media calls a backend, and only if you configure one |

---

## Benchmark

| Benchmark | Metric | graphify | Field |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | QA accuracy | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | QA accuracy | **76%** | tied with dense RAG |
| Graph build | LLM credits | **0** | per-token for most systems |

Setiap sistem dijalankan pada harness yang sama, model yang sama, dan budget yang sama, dinilai oleh juri yang divalidasi secara blind terhadap juri kedua (kesepakatan 90,6%, Cohen's kappa 0,81). Tabel lengkap per sistem, hasil code-intelligence, dan perintah reproduksi: **[BENCHMARKS.md](../../BENCHMARKS.md)**.

---

## Prasyarat

| Requirement | Minimum | Check | Install |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(recommended)* | any | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(alternative)* | any | `pipx --version` | `pip install pipx` |

**Instalasi cepat di macOS (Homebrew):**
```bash
brew install python@3.12 uv
```

**Instalasi cepat di Windows:**
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

## Instalasi

> **Paket resmi:** Paket PyPI-nya adalah `graphifyy` (dua huruf y). Paket `graphify*` lain di PyPI tidak berafiliasi. Perintah CLI-nya tetap `graphify`.

**Langkah 1 — instal paketnya:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**Langkah 2 — daftarkan skill ke asisten AI Anda:**

```bash
graphify install
```

Selesai. Buka asisten AI Anda dan ketik `/graphify .`

Untuk menginstal skill asisten ke repositori saat ini alih-alih ke profil
pengguna Anda, tambahkan `--project`:

```bash
graphify install --project
graphify install --project --platform codex
```

Instalasi bercakupan proyek menulis ke bawah direktori saat ini, misalnya
`.claude/skills/graphify/SKILL.md` atau `.agents/skills/graphify/SKILL.md` (beserta sidecar
`references/` yang dimuat skill saat dibutuhkan), dan
mencetak petunjuk `git add` untuk file yang bisa di-commit.
Perintah per-platform yang mendukung instalasi bercakupan proyek menerima flag yang sama,
misalnya `graphify claude install --project` atau `graphify codex install --project`.

> **Catatan PowerShell:** Gunakan `graphify .`, bukan `/graphify .` — garis miring di awal adalah pemisah path di PowerShell.

> **`graphify: command not found`?** `uv tool install` / `pipx install` menaruh perintah `graphify` di direktori bin tool masing-masing (`~/.local/bin`). Jika shell Anda tidak menemukannya tepat setelah instalasi — hal umum pada setup macOS + zsh yang baru — direktori itu belum ada di `PATH` Anda: jalankan `uv tool update-shell` (atau `pipx ensurepath`), lalu buka terminal baru. Dengan `pip` biasa, tambahkan `~/.local/bin` (Linux) atau `~/Library/Python/3.x/bin` (Mac) ke `PATH` Anda, atau jalankan `python -m graphify`.

> **Menjalankan dengan `uvx` / `uv tool run` alih-alih menginstal?** Sebutkan nama paketnya, bukan nama perintahnya: `uvx --from graphifyy graphify install`. `uvx graphify …` biasa akan gagal (`No solution found … no versions of graphify`) karena `uv tool run` membaca kata pertama sebagai *nama paket*, dan paketnya adalah `graphifyy` — perintah `graphify` berada di dalamnya.

> **Hindari `pip install` di Mac/Windows** jika memungkinkan. Skill ini me-resolve Python saat runtime dari `graphify-out/.graphify_python`; jika itu menunjuk ke environment yang berbeda dari tempat `pip` menginstal paketnya, Anda akan mendapat `ModuleNotFoundError: No module named 'graphify'`. `uv tool install` dan `pipx install` mengisolasi paket dalam environment-nya sendiri dan menghindari masalah ini sama sekali.

> **Git hook dan uv tool / pipx:** `graphify hook install` menyisipkan path interpreter yang sedang aktif langsung ke dalam skrip hook saat instalasi, sehingga hook post-commit tetap berjalan dengan benar bahkan di klien git GUI dan CI runner yang tidak memiliki `~/.local/bin` di `PATH`. Jika Anda menginstal ulang atau meng-upgrade graphify, jalankan ulang `graphify hook install` untuk memperbarui path yang disisipkan tersebut.

> **Mode strict (Claude Code):** `graphify install --project --strict` membuat asisten benar-benar menggunakan graf. Instalasi default hanya *mendorong* asisten untuk menjalankan `graphify query` sebelum membaca file; mode strict *memblokir* pembacaan sumber mentah pertama dalam satu sesi dan mengarahkannya ke graf, lalu kembali ke mode dorongan biasa (sehingga hanya terjadi paling banyak sekali per sesi dan tidak akan pernah macet). Alihkan saat runtime dengan `GRAPHIFY_HOOK_STRICT=1`/`0`; instalasi default tidak berubah (dorongan lembut/soft nudge).

<details>
<summary><b>Pilih platform Anda</b> (20+ asisten, klik untuk membuka)</summary>

| Platform | Install command |
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

Pengguna Codex juga perlu `multi_agent = true` di bawah `[features]` pada `~/.codex/config.toml` untuk ekstraksi paralel. CodeBuddy menggunakan mekanisme Agent tool dan PreToolUse hook yang sama dengan Claude Code. Factory Droid menggunakan tool `Task` untuk dispatch subagent paralel. OpenClaw dan Aider menggunakan ekstraksi sekuensial (dukungan agent paralel masih tahap awal di kedua platform tersebut). Trae menggunakan Agent tool untuk dispatch subagent paralel dan **tidak** mendukung hook `PreToolUse`, sehingga AGENTS.md menjadi mekanisme yang selalu aktif.

`--platform agents` (alias `--platform skills`) menyasar lokasi [Agent-Skills](https://github.com/anthropics/skills) lintas-framework generik: `~/.agents/skills/` yang bersifat user-global sesuai spesifikasi (dibaca oleh `npx skills` dan framework yang mengikuti spesifikasi tersebut) untuk instalasi global, dan `./.agents/skills/` untuk instalasi proyek (`--project`). `graphify install` biasa tetap khusus untuk satu platform (Claude Code) secara sengaja — gunakan platform bernama `agents` saat Anda ingin skill ini dapat ditemukan oleh framework apa pun yang membaca `.agents/skills`.

> Codex menggunakan `$graphify`, bukan `/graphify`.

</details>

<details>
<summary><b>Ekstra opsional</b> (instal hanya yang Anda perlukan)</summary>

| Extra | What it adds | Install |
|---|---|---|
| `pdf` | PDF extraction | `uv tool install "graphifyy[pdf]"` |
| `office` | `.docx` and `.xlsx` support | `uv tool install "graphifyy[office]"` |
| `google` | Google Sheets rendering | `uv tool install "graphifyy[google]"` |
| `video` | Video/audio transcription (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | MCP stdio server | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Neo4j push support | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | FalkorDB push support | `uv tool install "graphifyy[falkordb]"` |
| `svg` | SVG graph export | `uv tool install "graphifyy[svg]"` |
| `leiden` | Leiden community detection (Python < 3.13 only) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Ollama local inference | `uv tool install "graphifyy[ollama]"` |
| `openai` | OpenAI / OpenAI-compatible APIs | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic Claude API (`--backend claude`, uses `ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (uses IAM, no API key) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, uses `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "graphifyy[openai]"` |
| `sql` | SQL schema extraction | `uv tool install "graphifyy[sql]"` |
| `postgres` | Live PostgreSQL introspection (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | BYOND DreamMaker `.dm`/`.dme` AST extraction (may need a C compiler + `python3-dev` if no wheel matches your platform) | `uv tool install "graphifyy[dm]"` |
| `terraform` | Terraform / HCL `.tf`/`.tfvars`/`.hcl` AST extraction | `uv tool install "graphifyy[terraform]"` |
| `pascal` | Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` AST extraction (more accurate `calls`/`inherits` edges; falls back to a regex extractor when absent) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | Chinese query segmentation (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | Everything above | `uv tool install "graphifyy[all]"` |

</details>

---

## Membuat Asisten Anda Selalu Menggunakan Graf

Jalankan ini sekali di proyek Anda setelah membangun sebuah graf:

| Platform | Command |
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

Ini menulis sebuah file konfigurasi kecil yang memberi tahu asisten Anda untuk merujuk pada knowledge graph untuk pertanyaan seputar codebase, lebih memilih query terlingkupi seperti `graphify query "<question>"` dibandingkan membaca laporan lengkap atau meng-grep file mentah.

- **Platform berbasis hook** (Claude Code, Gemini CLI): sebuah hook otomatis dipicu sebelum pemanggilan tool bergaya pencarian (dan, di Claude Code, sebelum membaca file sumber satu per satu lewat tool Read/Glob) dan mendorong asisten Anda ke arah jalur graf.
- **Platform berbasis file instruksi** (Codex, OpenCode, Cursor, dll.): file instruksi persisten (`AGENTS.md`, `.cursor/rules/`, dll.) memberikan panduan query-first yang sama.

`GRAPH_REPORT.md` tetap tersedia untuk tinjauan arsitektur secara luas.

**CodeBuddy** melakukan dua hal yang sama seperti Claude Code: menulis sebuah bagian `CODEBUDDY.md` yang memberi tahu CodeBuddy untuk membaca `graphify-out/GRAPH_REPORT.md` sebelum menjawab pertanyaan arsitektur, dan menginstal hook `PreToolUse` (`.codebuddy/settings.json`) yang dipicu sebelum perintah pencarian Bash dan pembacaan file, mendorong ke arah `graphify query` sebagai gantinya.

**Codex** menulis ke `AGENTS.md`, yang merupakan mekanisme sesungguhnya yang membawa panduan graf yang selalu aktif di platform ini. `graphify codex install` juga mendaftarkan hook `PreToolUse` di `.codex/hooks.json` (`graphify hook-check`), tetapi entri itu sengaja dibuat **no-op**: Codex Desktop menolak `hookSpecificOutput.additionalContext` pada `PreToolUse`, sehingga memunculkan dorongan di sana akan merusak pemanggilan tool Bash. Berbeda dengan Claude Code, di mana hook (`graphify hook-guard`) yang melakukan pendorongan, di Codex hook-nya terpicu dan sengaja tidak melakukan apa-apa, dan `AGENTS.md` menjadi mekanisme yang selalu aktif.

**Kilo Code** menginstal skill Graphify ke `~/.config/kilo/skills/graphify/SKILL.md` dan perintah native `/graphify` ke `~/.config/kilo/command/graphify.md`. `graphify kilo install` juga menulis `AGENTS.md` beserta plugin native `tool.execute.before` (`.kilo/plugins/graphify.js` + registrasi `.kilo/kilo.json` atau `.kilo/kilo.jsonc`) sehingga Kilo mendapatkan perilaku pengingat graf yang selalu aktif yang sama melalui konfigurasi `.kilo` native.

**Cursor** menulis `.cursor/rules/graphify.mdc` dengan `alwaysApply: true`, sehingga Cursor menyertakannya secara otomatis di setiap percakapan tanpa perlu hook.

Untuk menghapus graphify dari semua platform sekaligus: `graphify uninstall` (tambahkan `--purge` untuk juga menghapus `graphify-out/`). Atau gunakan perintah per-platform (misalnya `graphify claude uninstall`).

---

## Apa yang Ada di dalam Laporan

- **God nodes** — konsep-konsep yang paling banyak terhubung di proyek Anda. Semuanya mengalir melalui node-node ini.
- **Koneksi yang mengejutkan** — tautan antara hal-hal yang berada di file atau modul yang berbeda. Diberi ranking berdasarkan seberapa tak terduganya.
- **"Alasan"-nya** — komentar inline (`# NOTE:`, `# WHY:`, `# HACK:`), docstring, dan rasional desain dari dokumen diekstrak sebagai node tersendiri yang ditautkan ke kode yang mereka jelaskan.
- **Pertanyaan yang disarankan** — 4–5 pertanyaan yang secara unik bisa dijawab oleh graf ini.
- **Tag kepercayaan** — setiap relasi yang disimpulkan ditandai `EXTRACTED`, `INFERRED`, atau `AMBIGUOUS`. Anda selalu tahu mana yang ditemukan dan mana yang ditebak.

---

## File Apa Saja yang Didukung

| Type | Extensions |
|------|-----------|
| Code (36 tree-sitter grammars) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme` requires `uv tool install graphifyy[dm]`; `.mts`/`.cts` reuse the TypeScript grammar, `.cc`/`.cxx` and CUDA `.cu`/`.cuh` and Metal `.metal` reuse the C++ grammar) |
| Salesforce Apex | `.cls .trigger` (regex-based; classes, interfaces, enums, methods, triggers, SOQL/DML edges) |
| Terraform / HCL | `.tf .tfvars .hcl` (requires `uv tool install graphifyy[terraform]`) |
| MCP configs | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — extracts server nodes, package refs, env var requirements |
| Package manifests | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — one canonical package node per package (by name) plus `depends_on` edges, so a package referenced from many manifests is a single hub |
| Docs | `.md .mdx .qmd .html .txt .rst .yaml .yml` (markdown `[text](./other.md)` links and `[[wikilinks]]` become `references` edges between docs) |
| Office | `.docx .xlsx` (requires `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (opt-in; requires `gws` auth and `--google-workspace`; Sheets need `uv tool install graphifyy[google]`) |
| PDFs | `.pdf` |
| Images | `.png .jpg .webp .gif` |
| Video / Audio | `.mp4 .mov .mp3 .wav` and more (requires `uv tool install graphifyy[video]`) |
| YouTube / URLs | any video URL (requires `uv tool install graphifyy[video]`) |

Kode diekstrak **secara lokal tanpa panggilan API apa pun** (AST via tree-sitter). Selain itu semuanya melalui model API asisten AI Anda.

File `.gdoc`, `.gsheet`, dan `.gslides` dari Google Drive for desktop hanyalah shortcut
penunjuk, bukan konten dokumen sesungguhnya. Untuk menyertakan Google Docs, Sheets, dan
Slides asli dalam ekstraksi headless, instal dan autentikasikan
[`gws` CLI](https://github.com/googleworkspace/cli), lalu jalankan:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

Anda juga bisa mengatur `GRAPHIFY_GOOGLE_WORKSPACE=1`. Graphify mengekspor shortcut ke
`graphify-out/converted/` sebagai sidecar Markdown, lalu mengekstrak file-file tersebut.

---

## Perintah Umum

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

Lihat [Decouple: kandidat Extract-Class dengan skor risiko](#decouple-kandidat-extract-class-dengan-skor-risiko) di atas, atau [referensi lengkap perintah](#referensi-lengkap-perintah) di bawah.

---

## Mengabaikan File

Buat `.graphifyignore` di root proyek Anda — sintaksnya sama seperti `.gitignore`, termasuk negasi `!`.

**`.gitignore` dihormati secara otomatis.** graphify membaca `.gitignore` di setiap direktori. Jika `.graphifyignore` juga ada, keduanya akan **digabungkan** — pola `.graphifyignore` dievaluasi terakhir, sehingga menang saat terjadi konflik (termasuk negasi `!`). Menambahkan `.graphifyignore` hanya akan mengecualikan lebih banyak file; ia tidak akan pernah menyertakan kembali file yang sudah dikecualikan oleh `.gitignore` Anda. Scoping subdirektori bekerja sama seperti git — sebuah file ignore hanya mempengaruhi subtree miliknya sendiri.

Sertakan `--no-gitignore` pada `graphify extract` saat kode hasil generate atau transpile yang di-gitignore-kan perlu masuk ke dalam graf. Ini menonaktifkan `.gitignore` dan `.git/info/exclude`; `.graphifyignore` tetap berlaku.

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

## Pengaturan Tim

`graphify-out/` dimaksudkan untuk di-commit ke git agar semua orang di tim mulai dengan peta yang sama.

**Tambahan `.gitignore` yang disarankan:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` kini portabel — key-nya disimpan sebagai path relatif dan di-re-anchor ulang saat dimuat, sehingga meng-commit-nya aman dan menghindari rebuild penuh pada checkout pertama.

**Alur kerja:**
1. Satu orang menjalankan `/graphify .` dan meng-commit `graphify-out/`.
2. Semua orang menarik (pull) perubahan — asisten mereka langsung membaca graf tersebut.
3. Jalankan `graphify hook install` agar rebuild otomatis setelah setiap commit (hanya AST, tanpa biaya API). Ini juga mengatur sebuah git merge driver sehingga `graph.json` tidak akan pernah tertinggal dengan penanda konflik — dua developer yang commit secara paralel akan mendapatkan graf mereka di-union-merge secara otomatis.
4. Saat dokumen atau paper berubah, jalankan `/graphify --update` untuk menyegarkan node-node tersebut.

---

## Menggunakan Graf Secara Langsung

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

Server MCP memberi asisten Anda akses terstruktur: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Server HTTP Bersama

`--transport stdio` (default) memunculkan satu server lokal per developer. `--transport http` menyajikan kumpulan tool yang sama lewat transport MCP Streamable HTTP, sehingga satu proses bersama bisa menyajikan graf untuk seluruh tim — klien mengarahkan konfigurasi MCP IDE mereka ke `http://<host>:8080/mcp` alih-alih menjalankan graphify secara lokal.

| Flag | Default | Purpose |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Transport to serve on |
| `--host` | `127.0.0.1` | HTTP bind host (use `0.0.0.0` to expose beyond localhost) |
| `--port` | `8080` | HTTP bind port |
| `--api-key` | env `GRAPHIFY_API_KEY` | Require `Authorization: Bearer <key>` (or `X-API-Key`) |
| `--path` | `/mcp` | HTTP mount path |
| `--json-response` | off | Return plain JSON instead of SSE streams |
| `--stateless` | off | No per-session state (for load-balanced / CI deployments) |
| `--session-timeout` | `3600` | Reap idle stateful sessions after N seconds (`0` disables) |

Bind default `127.0.0.1` bersifat loopback-only. Atur `--host 0.0.0.0` **dan** `--api-key` bersamaan saat mengekspos ke host bersama. Jalankan dalam kontainer:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **Catatan WSL / Linux:** Ubuntu menyertakan `python3`, bukan `python`. Gunakan venv untuk menghindari konflik:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## Variabel Lingkungan

Variabel-variabel ini hanya diperlukan untuk **ekstraksi headless / CI** (`graphify extract`). Saat berjalan lewat skill `/graphify` di dalam IDE Anda, model API disediakan oleh sesi IDE Anda — tidak ada key tambahan yang diperlukan.

| Variable | Used for | When required |
|---|---|---|
| `ANTHROPIC_API_KEY` | Claude (Anthropic) backend | `--backend claude` |
| `ANTHROPIC_BASE_URL` | Anthropic-compatible endpoint URL (LiteLLM proxy, gateways, ...) | `--backend claude` (default: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Model name for the Claude backend — for custom endpoints, use the model name/alias your server exposes | `--backend claude` (default: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` or `GOOGLE_API_KEY` | Google Gemini backend | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI or OpenAI-compatible APIs | `--backend openai` (local servers accept any non-empty value) |
| `OPENAI_BASE_URL` | OpenAI-compatible server URL (llama.cpp, vLLM, LM Studio, ...) | `--backend openai` (default: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | Model name for the OpenAI backend — for self-hosted servers, use the model name/alias your server exposes (check its `/v1/models` endpoint), e.g. `LFM2.5-8B-A1B-UD-Q4_K_XL` for llama.cpp | `--backend openai` (default: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | DeepSeek backend | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Kimi Code backend | `--backend kimi` |
| `OLLAMA_BASE_URL` | Ollama local inference URL | `--backend ollama` (default: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Ollama model name | `--backend ollama` (default: auto-detect) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Override Ollama KV-cache window size | optional — auto-sized by default |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Minutes to keep Ollama model loaded | optional — set `0` to unload after each chunk |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI Service backend | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | Azure resource endpoint URL | `--backend azure` (required alongside API key) |
| `AZURE_OPENAI_API_VERSION` | Azure API version override | optional — default `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` or `GRAPHIFY_AZURE_MODEL` | Azure deployment name | optional — default `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — standard credential chain | `--backend bedrock` (no API key, uses IAM) |
| `GRAPHIFY_MAX_WORKERS` | AST parallelism thread count | optional — also `--max-workers` flag |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Raise output cap for dense corpora | optional — e.g. `32768` for large files |
| `GRAPHIFY_API_TIMEOUT` | Per-call timeout in seconds for HTTP, claude-cli, Anthropic SDK, and Bedrock backends (default: 600) | optional — also `--api-timeout` flag |
| `GRAPHIFY_MAX_RETRIES` | How many times to retry a rate-limited (429) request before giving up (default: 6; honors `Retry-After`) | optional — raise for strict per-org limits (e.g. kimi); `0` disables |
| `GRAPHIFY_FORCE` | Force graph rebuild even with fewer nodes | optional — also `--force` flag |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Auto-enable Google Workspace export | optional — set to `1` |
| `GRAPHIFY_TRIAGE_BACKEND` | Backend for `graphify prs --triage` | optional — auto-detected from available keys |
| `GRAPHIFY_TRIAGE_MODEL` | Model override for triage | optional — e.g. `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | Set to `1` to turn on the local query log at `~/.cache/graphify-queries.log` (records each query/path/explain question + corpus path). Off by default — nothing is written unless you opt in (#1797) | optional |
| `GRAPHIFY_QUERY_LOG` | Enable the query log and write it to this path instead of the default | optional — off unless this or `_ENABLE` is set |
| `GRAPHIFY_QUERY_LOG_DISABLE` | Set to `1` to force the query log off (wins over the enable vars) | optional |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | When the log is enabled, also record full subgraph responses (off by default) | optional |
| `GRAPHIFY_MAX_GRAPH_BYTES` | Override the 512 MiB graph.json size cap — e.g. `700MB`, `2GB`, or plain bytes | optional — useful for very large corpora |
| `GRAPHIFY_MAX_CONTEXTS` | Maximum number of non-default project graphs retained by one multi-project MCP server | optional — default: `8`; invalid values use `8`, and values below `1` use `1` |
| `GRAPHIFY_LLM_TEMPERATURE` | Override LLM temperature for semantic extraction — e.g. `0.7`, or `none` to omit | optional — auto-omitted for o1/o3/o4/gpt-5 reasoning models |

---

## Privasi

- **File kode** — diproses secara lokal via tree-sitter. Tidak ada yang keluar dari mesin Anda. Korpus khusus kode tidak memerlukan API key — `graphify extract` berjalan sepenuhnya offline. Pada repo campuran, tambahkan `--code-only` untuk mengindeks kode saja dan melewati dokumen/PDF/gambar yang jika tidak akan membutuhkan LLM.
- **Video / audio** — ditranskripsikan secara lokal dengan faster-whisper. Tidak ada yang keluar dari mesin Anda.
- **Dokumen, PDF, gambar** — dikirim ke asisten AI Anda untuk ekstraksi semantik (via skill `/graphify`, menggunakan model apa pun yang dijalankan sesi IDE Anda). `graphify extract` headless memerlukan `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), instance Ollama yang berjalan (`OLLAMA_BASE_URL`), kredensial AWS via provider chain standar (Bedrock — tanpa API key, menggunakan IAM), atau binary CLI `claude` (Claude Code — tanpa API key, menggunakan subscription Claude Anda). Flag `--dedup-llm` menggunakan key yang sama.
- **Residensi data** — `graphify extract` otomatis mendeteksi provider mana yang akan digunakan berdasarkan API key mana yang diset (prioritas: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). Untuk kode dengan persyaratan residensi data, gunakan `--backend ollama` (sepenuhnya lokal) atau sertakan flag `--backend` secara eksplisit. Kimi (`MOONSHOT_API_KEY`) merutekan ke server Moonshot AI di Tiongkok.
- **Tanpa telemetri**, tanpa pelacakan penggunaan, tanpa analitik.
- **Pencatatan query** — setiap pemanggilan `graphify query`, `graphify path`, `graphify explain`, dan `query_graph` MCP dicatat ke `~/.cache/graphify-queries.log` dalam format JSON Lines (timestamp, pertanyaan, korpus, jumlah node yang dikembalikan, durasi). Respons subgraf lengkap **tidak** disimpan secara default. Atur `GRAPHIFY_QUERY_LOG_DISABLE=1` untuk opt out, atau `GRAPHIFY_QUERY_LOG=/dev/null` untuk membisukannya tanpa menonaktifkan code path-nya.

---

## Pemecahan Masalah

**`graphify: command not found` setelah instalasi**
CLI-nya sudah terinstal tetapi direktori bin-nya tidak ada di `PATH` shell Anda. Pilih perbaikan sesuai cara Anda menginstal:
- **uv** (`uv tool install graphifyy`): perintahnya masuk ke direktori bin tool milik uv (`~/.local/bin`), yang sering belum ada di `PATH` pada setup macOS/zsh yang baru. Jalankan `uv tool update-shell`, lalu buka terminal baru. (Temukan direktorinya dengan `uv tool dir --bin`.)
- **pipx** (`pipx install graphifyy`): jalankan `pipx ensurepath`, lalu buka terminal baru.
- **pip** (`pip install graphifyy`): pip menginstal skrip ke direktori bin pengguna yang mungkin tidak ada di `PATH` — tambahkan `~/Library/Python/3.x/bin` (macOS) atau `~/.local/bin` (Linux) ke `PATH` Anda di `~/.zshrc`/`~/.bashrc`, atau cukup jalankan `python -m graphify`.

**`uvx graphify …` atau `uv tool run graphify …` gagal me-resolve `graphify`**
Paket PyPI-nya adalah `graphifyy`; `graphify` hanyalah perintah yang disediakan olehnya. `uv tool run` memperlakukan kata pertama sebagai *nama paket*, sehingga ia mencari paket bernama `graphify` dan melaporkan `No solution found … no versions of graphify`. Sebutkan nama paketnya secara eksplisit: `uvx --from graphifyy graphify install` (sama dengan `uv tool run --from graphifyy graphify install`). Atau, jalankan `uv tool install graphifyy` sekali lalu panggil `graphify` secara langsung.

**`uv run --with graphifyy python -m graphify` secara diam-diam menjalankan instalasi lama**
`uv run` menggunakan Python *sistem* Anda, sehingga jika `graphifyy` versi lama juga ada di sana (misalnya dari `pip install graphifyy` sebelumnya), Python bisa menemukan copy tersebut lebih dulu di `sys.path` dan `--with graphifyy` tidak akan menimpanya. Ini berjalan tanpa error, tetapi Anda mendapatkan perilaku versi *lama* — misalnya override environment seperti `OPENAI_BASE_URL` diam-diam diabaikan, sehingga request diarahkan ke endpoint default dan gagal dengan 401 yang tampak seperti key yang salah. Cirinya adalah baris `warning: skill is from graphify <newer>, package is <older>` — itu berarti instalasi yang berbeda yang dimuat, bukan hanya skill yang basi. Periksa copy mana yang sebenarnya dimuat:
```bash
python -c "import graphify; print(graphify.__file__)"
```
Lalu jalankan perintah yang terinstal secara langsung (ini menggunakan copy yang dikelola uv), atau hapus copy sistem yang basi:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` berjalan tetapi perintah `graphify` tidak**
`PATH` shell Anda tidak menyertakan direktori bin tempat perintah tersebut diinstal. Lebih baik gunakan `uv tool install` / `pipx install` daripada `pip` biasa, lalu jalankan `uv tool update-shell` / `pipx ensurepath` dan buka terminal baru (lihat catatan instalasi di atas).

**`/graphify .` menyebabkan "path not recognized" di PowerShell**
PowerShell memperlakukan `/` di awal sebagai pemisah path. Gunakan `graphify .` (tanpa garis miring) di Windows.

**Graf memiliki lebih sedikit node setelah `--update` atau rebuild**
Jika sebuah refactor menghapus file, node lama akan tetap tertinggal. Sertakan `--force` (atau atur `GRAPHIFY_FORCE=1`) untuk menimpanya meskipun rebuild-nya menghasilkan lebih sedikit node.

**`extract` keluar dengan "extraction was incomplete ... refusing to overwrite"**
Saat sebuah proses ekstraksi crash atau sebuah walk tidak bisa membaca seluruh korpus, hasil jalankan tersebut akan lebih kecil dari jalankan yang lengkap, sehingga `graphify extract` menolak menimpa graf existing yang lebih besar dengan hasil parsial (melindungi `graph.json` Anda). Perbaiki kegagalan yang mendasarinya lalu jalankan ulang, atau sertakan `--allow-partial` untuk tetap menimpanya.

**Graf memiliki node duplikat untuk entitas yang sama (ghost duplicates)**
Ghost duplicate (simbol yang sama muncul dua kali — sekali dari ekstraksi AST dengan lokasi sumber, sekali dari ekstraksi semantik tanpa lokasi sumber) kini digabungkan secara otomatis saat build. Jika Anda melihat ini pada graf yang dibangun sebelum v0.8.33, jalankan re-extract penuh untuk membersihkannya:
```bash
graphify extract . --force
```

**Ollama kehabisan VRAM / context window terlampaui**
Window KV-cache diukur secara otomatis tetapi mungkin terlalu besar untuk GPU Anda. Kecilkan:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**Peringatan `LLM returned invalid JSON` / `Unterminated string`**
Respons JSON model mencapai batas token output-nya dan terpotong di tengah string. graphify melakukan recovery otomatis (ia membagi chunk dan mengekstrak ulang kedua bagiannya, dan sebuah dokumen tunggal yang terlalu besar akan dipotong lebih dulu di batas heading/paragraf sehingga seluruh file tetap tercakup), sehingga peringatan ini berisik tetapi bukan kehilangan data. Untuk mengurangi kegaduhannya, naikkan batas output atau kecilkan output tiap chunk:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
Dengan gateway cloud seperti OpenRouter, lebih baik gunakan `--backend openai` (atur `OPENAI_BASE_URL`) daripada shim Ollama — itu jalur yang lebih bersih dan kompatibel dengan OpenAI. Jika model itu sendiri memiliki batas output maksimum, menurunkan `--token-budget` adalah cara yang paling bisa diandalkan.

**HTML graf terlalu besar untuk dibuka di browser (>5000 node)**
Lewati pembuatan HTML dan gunakan JSON secara langsung:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**`graph.json` memiliki penanda konflik setelah dua developer commit secara bersamaan**
Jalankan `graphify hook install` — ini mengatur sebuah git merge driver yang meng-union-merge `graph.json` secara otomatis sehingga konflik tidak akan pernah terjadi.

**Ekstraksi mengembalikan node/edge kosong untuk dokumen atau PDF**
Dokumen, PDF, dan gambar memerlukan pemanggilan LLM — korpus khusus kode tidak memerlukan key apa pun. Periksa bahwa API key Anda sudah diset dan backend-nya benar:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**Peringatan ketidaksesuaian versi skill di IDE Anda**
Versi graphify yang terinstal berbeda dengan file skill-nya. Perbarui:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**Prompt cache Claude Code menjadi tidak valid setelah setiap `graphify extract`**
Graphify menulis file output (`graph.json`, `graphify-out/`) ke dalam workspace. Jika path-path tersebut tidak diabaikan, setiap penulisan akan membatalkan prompt cache Claude Code, memaksa unggah ulang penuh dengan tarif cache-write pada giliran berikutnya. Tambahkan ke `.claudeignore`:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## Referensi Lengkap Perintah

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

> **Nama komunitas:** di dalam sebuah agent (Claude Code, Gemini CLI) agent itu sendiri yang menamai komunitas. Saat Anda menjalankan CLI mentah, `cluster-only` otomatis menamainya dengan backend yang telah dikonfigurasi (bawaan atau provider kustom yang kompatibel dengan OpenAI) — sertakan `--no-label` untuk mempertahankan `Community N`, atau jalankan `graphify label` untuk membuat (ulang) nama sesuai kebutuhan.

---

## Pelajari Lebih Lanjut

- [Cara kerjanya](../how-it-works.md) — pipeline ekstraksi, community detection, penilaian kepercayaan, benchmark
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — pembagian modul, cara menambahkan bahasa
- [Integrasi opsional](../docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — buku tentang ide-ide di balik graphify, arsitekturnya secara menyeluruh

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) adalah lapisan selalu-aktif yang dibangun di atas graphify — ia menerapkan pendekatan graf yang sama pada seluruh konteks kerja Anda: rapat, file, dokumen, dan kode, diperbarui secara berkelanjutan di latar belakang.

Dibangun untuk orang dan tim yang pekerjaannya tersebar di ratusan percakapan dan dokumen yang tidak akan pernah bisa mereka rekonstruksi ulang secara penuh.

**[Ikuti waitlist di graphify.com](https://graphify.com).** Uji coba gratis akan segera diluncurkan.

---

<details>
<summary>Kontribusi</summary>

### Pengaturan Pengembangan

Proyek ini menggunakan [uv](https://docs.astral.sh/uv/) untuk alur kerja pengembangan. Instal sekali, lalu:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

Verifikasi instalasi editable-nya:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### Menjalankan Pengujian

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> Catatan macOS: test suite ini menyertakan fixture `sample.f90` maupun `sample.F90`. Keduanya bertabrakan pada sistem file yang tidak membedakan huruf besar/kecil seperti HFS+ / APFS. Jalankan di Linux atau dalam kontainer Docker jika Anda perlu menguji kedua varian Fortran tersebut secara bersamaan.

### Alur Kerja Git

- Pengembangan aktif berlangsung di branch `v8`.
- Gaya commit: `fix: <description>` / `feat: <description>` / `docs: <description>`
- Sebelum membuka PR, jalankan `uv run pytest tests/ -q` dan pastikan lolos.
- Tambahkan file fixture ke `tests/fixtures/` dan pengujian ke `tests/test_languages.py` untuk setiap ekstraktor bahasa baru.

### Apa yang Bisa Dikontribusikan

**Contoh nyata (worked examples)** adalah kontribusi yang paling berguna. Jalankan `/graphify` pada sebuah korpus nyata, simpan outputnya ke `worked/{slug}/`, tulis `review.md` yang jujur mencakup apa yang benar dan salah dari graf tersebut, lalu buka sebuah PR.

**Bug ekstraksi** — buka sebuah issue dengan file input, entri cache (`graphify-out/cache/`), dan apa yang terlewat atau salah.

Lihat [ARCHITECTURE.md](../../ARCHITECTURE.md) untuk tanggung jawab modul dan cara menambahkan bahasa.

</details>
