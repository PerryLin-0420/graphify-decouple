<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b><code>graphify decouple</code>를 추가한 <a href="https://github.com/Graphify-Labs/graphify">graphify</a>의 포크</b> — god object에 대한 위험도 평가 기반 Extract-Class 후보를, LLM 없이, 무언가를 추천하기 전에 실제 소스 코드(호출 그래프뿐만 아니라)를 다시 검증합니다. 아래 <a href="#decouple-risk-scored-extract-class-candidates">Decouple: 위험도 평가 기반 Extract-Class 후보</a>를 참고하세요.
</p>

<div align="center">
<details><summary><b>다른 언어로 읽기</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>공식 v1 출시 전 graphify 플랫폼의 얼리 액세스가 진행 중입니다: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

AI 코딩 어시스턴트에 `/graphify`를 입력하면 전체 프로젝트(코드, 문서, PDF, 이미지, 비디오)를 **지식 그래프**로 매핑하여 파일을 **grep하는 대신 쿼리**할 수 있게 해줍니다.

- **무료 및 완전 로컬 코드 매핑.** 코드는 tree-sitter AST로 파싱됩니다: 결정론적이며 LLM을 사용하지 않고 외부로 데이터가 전송되지 않습니다. (문서, PDF, 이미지 및 비디오는 시맨틱 패스를 위해 어시스턴트 모델이나 설정된 API 키를 사용합니다.)
- **모든 연결(Edge)에 대한 설명 제공.** 각 연결은 `EXTRACTED`(소스 코드에 명시됨) 또는 `INFERRED`(graphify가 추론함)로 태그가 지정되어 직접 읽은 항목과 추론된 항목을 구분할 수 있습니다.
- **벡터 인덱스가 아닙니다.** 임베딩이나 벡터 저장소 없이 실제로 탐색할 수 있는 그래프입니다. 질문을 던지거나 두 요소 간의 경로를 추적하거나 하나의 개념을 설명할 수 있습니다.

> 요청 시뿐만 아니라 코드, 문서, 회의 전반에 걸쳐 백그라운드에서 항상 업데이트되기를 원하십니까? 이것이 우리가 **[graphify.com](https://graphify.com)**에서 구축하고 있는 것이며, 얼리 액세스는 **[app.graphify.com](https://app.graphify.com/login)**에서 지금 열려 있습니다.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="graphify's interactive graph.html showing the FastAPI codebase as a force-directed knowledge graph with a legend of detected communities" width="900">
</p>
<p align="center">
  <em>graphify로 매핑된 FastAPI 코드베이스입니다. 각 노드는 개념이며 색상은 감지된 커뮤니티입니다. 전체 요소는 graph.html에서 클릭할 수 있습니다.</em>
</p>

**시작하기** (30초):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

그런 다음, AI 어시스턴트에서:

```
/graphify .
```

완료되었습니다. 다음 **3개의 파일**이 생성됩니다:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**지원되는 플랫폼:** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot 및 15개 이상 — [플랫폼 선택](#install).

---

## 실제 동작 보기

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="graphify path query: a terminal asks for the shortest path between FastAPI and ModelField, and the answer lights up hop by hop across the knowledge graph" width="900">
</p>

그래프가 구축되면 파일을 읽는 대신 쿼리합니다. 위에 표시된 FastAPI 코드베이스에서 graphify를 실행한 실제 출력입니다:

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

모든 연결은 **신뢰도 태그**를 가지고 있어(`EXTRACTED` = 소스에 명시됨, `INFERRED` = 해석으로 도출됨), 직접 읽은 항목과 추론된 항목을 구분할 수 있습니다. `graphify query "<question>"`은 자연어 질문에 대해 범위가 지정된 서브그래프를 반환하며, `graphify path A B`는 임의의 두 항목이 어떻게 연결되는지 추적합니다.

---

## Decouple: 위험도 평가 기반 Extract-Class 후보

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: MainWindow god node splitting into risk-scored candidate classes, with a shared-state warning between two of them" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: MainWindow's 5 proposed classes, Node Info panel open on Main Window Axis and Range Controls showing a 0.608 state overlap with Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>실제 실행에서의 DECOUPLE.html — 제안된 클래스를 클릭하면 다른 어떤 클래스와 상태를 공유하는지, 구체적으로 무엇을 공유하는지 정확히 보여줍니다.</em>
</p>

같은 페이지가 분할 자체도 렌더링합니다. **Preview decoupled view**를 토글하면 god 클래스 자신의 메서드가 제안된 클래스로 바뀌고 엣지가 그 자리에서 다시 라우팅됩니다 — 다시 그린 다이어그램이 아니라 배선 변경입니다:

| 이전 — 오늘의 god 클래스 | 이후 — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html before the toggle: a single MainWindow hub node with its own methods fanned out around it" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html after the toggle: the same node reduced to 5 diamond-shaped proposed classes, green dashed edges showing which methods were extracted into each, red edges showing shared instance state between two of them" width="440"> |
| 자신의 메서드 47개를 담고 있는 하나의 노드로, 각 메서드는 오직 이 클래스를 통해서만 접근할 수 있습니다. | 제안된 클래스들입니다. 녹색 점선 = 각 클래스로 무엇이 추출되었는지; 빨간색 = 두 클래스가 여전히 공유하는 인스턴스 상태로, 이것이 정확히 `split`과 `keep_as_is`를 결정짓는 요소입니다. 위험 임계값을 통과한 후보만 그려집니다 — 여기서는 6개 중 5개이며, 그래서 한 메서드는 착지할 다이아몬드가 없습니다. |

`graphify decouple`은 god object를 찾아내고, 그것들이 단순히 크다는 것이 아니라 실제로 분할할 가치가 있는지 알려줍니다.

이 기능이 잡아내려는 실패 모드는 다음과 같습니다: 47개의 메서드를 가진 클래스를 호출 그래프 클러스터링이 기꺼이 5개의 깔끔해 보이는 그룹으로 나누지만, 그 모두가 여전히 동일한 `self._chart_style` / `self._crosshair` 인스턴스 상태를 밑에서 읽고 씁니다. 그 분할을 그대로 배포하면 아무것도 decouple하지 못한 것입니다 — 그저 메서드를 새 파일로 옮겼을 뿐이며, 그것들은 여전히 독립적으로 테스트하거나 변경하거나 추론할 수 없습니다. 왜냐하면 모두 동일한 공유 상태가 다시 전달되어야 하기 때문입니다. 호출 그래프만 보는 도구는 이것을 전혀 볼 수 없습니다; 실제 소스로 돌아가야만 합니다.

**두 가지 검사, 둘 다 LLM 없이, 둘 다 결정론적으로:**

1. **이것이 정말 God Object인가?** 차수가 높은 노드는 진짜 God Object(관련 없는 책임에 걸쳐 퍼져 있는 많은 자체 메서드 — Extract Class가 적용됨)일 수도 있고, 과도하게 참조되는 허브/데이터 모델(자체 메서드는 적고 대부분 *들어오는* 참조 — 본문을 분할해도 아무 효과가 없으며, 해결책은 인터페이스를 좁히는 것이지 클래스를 추출하는 것이 아님)일 수도 있습니다. `classify_god_node`는 원시 차수가 아니라 `member_ratio`로 이 둘을 구별합니다 — 이 차이 덕분에 `TraceSource`(84개의 엣지지만 자체 메서드는 6개뿐)는 잘못된 분할 제안을 받지 않고, `MainWindow`(88개의 엣지, 자체 메서드 47개)는 올바르게 그 제안을 받습니다.
2. **분할이 실제로 결합도를 줄이는가?** `risk_before`(god 노드의 현재 크기/결합도/파편화)는 `risk_after`와 비교됩니다 — 분할 자체가 도입할 새로운 위험입니다: 보이지 않는 클래스 내부 엣지였던 그룹 간 호출이 명시적인 클래스 간 의존성이 되고, 이제 둘 이상의 새 클래스에 의존해야 하는 호출자가 생기며, 그리고 — 호출 그래프가 구조적으로 할 수 없는 검사인 — 제안된 그룹들이 실제로 얼마나 많은 `self`/`this` 인스턴스 상태(읽기, 쓰기, 그리고 별도로 가중치가 매겨진 공유 헬퍼 메서드 호출: 공유된 **쓰기**는 공유된 읽기보다 더 높은 점수를 받음)를 공통으로 가지고 있는지입니다. 이는 god 노드 자신의 소스 파일을 tree-sitter로 직접 다시 파싱합니다; graphify 자체의 추출된 그래프에 의존하지 않으며, 그 그래프는 어떤 언어에 대해서도 필드 수준 접근을 기록하지 않습니다. `risk_after`가 `risk_before`보다 낮은 임계값을 통과할 때만 계획은 `split`을 추천합니다 — 그렇지 않으면 `marginal` 또는 `keep_as_is`이며, 권장되지 않는 후보는 눈으로 추측해야 하는 도형으로 그려지지 않고 숫자로 보고됩니다.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

`graph.json` 옆에 세 개의 파일을 출력합니다:

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

**상태 공유 검사를 위한 언어 지원 범위** (위의 호출 그래프 전용 분류는 graphify가 추출하는 모든 언어에서 작동합니다; 이 표는 특히 `self`/`this` 상태 겹침을 검증하는 소스 재파싱에 관한 것입니다):

| 언어 | 지원 여부 | 참고 사항 |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()`는 래핑된 필드 접근이 아니라 자체 AST 노드입니다 — 명시적으로 처리됨 |
| C# | ✅ | |
| Rust | ✅ | `impl` 블록을 통한 `self.x` |
| Ruby | ✅ | `@x`(지배적인 관용구) + `self.foo` 호출 |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | 메서드별 receiver 해석 — Go에는 `self`/`this` 키워드가 없으므로, receiver 이름(`func (f *Foo) M()`의 `f`)이 각 메서드마다 새로 해석됩니다 |
| C | ❌ | struct 포인터 매개변수는 다른 매개변수와 구별하는 구문적 표시가 없습니다 — 완전한 타입 추론 없이는 신뢰할 수 있는 신호가 없습니다 |

지원되지 않는 언어의 god 노드, 또는 소스를 읽을 수 없는 노드는 `state_analysis: "skipped"`로 표시됩니다 — 분류와 호출 그래프 점수는 여전히 실행되지만, 상태 검사가 통과했다고 조용히 가정하는 대신 권장 사항은 호출 그래프에만 의존합니다.

---

## 주요 기능

기본으로 제공되는 것:

| 기능 | 제공 내용 |
|---|---|
| **God 노드** | 가장 많이 연결된 개념들로, 모든 것이 무엇을 통해 흐르는지 볼 수 있습니다 |
| **커뮤니티** | LLM 없이 생성된 레이블과 함께 하위 시스템으로 분할된 그래프(Leiden) |
| **파일 간 링크** | tree-sitter AST를 통해 약 40개 언어에서 해석된 `calls` / `imports` / `inherits` / `mixes_in` |
| **쿼리, 경로, 설명** | 질문하기, 두 항목 간 경로 추적, 또는 하나의 개념 설명, 모두 `graph.json`에 대해 |
| **근거 + 문서 참조** | `# NOTE:` / `# WHY:` 주석과 ADR/RFC 인용은 코드에 연결된 1급 노드가 됩니다 |
| **코드를 넘어서** | 문서, PDF, 이미지, 비디오/오디오가 모두 같은 그래프로 매핑됩니다 |
| **로컬 우선** | 코드는 tree-sitter로 로컬에서 파싱됩니다(LLM 없음, 외부로 데이터가 전송되지 않음); 문서/미디어에 대한 시맨틱 패스만 백엔드를 호출하며, 그것도 설정한 경우에만 |

---

## 벤치마크

| 벤치마크 | 지표 | graphify | 분야 |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | QA 정확도 | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | QA 정확도 | **76%** | dense RAG와 동률 |
| 그래프 구축 | LLM 크레딧 | **0** | 대부분 시스템은 토큰당 비용 발생 |

모든 시스템은 동일한 하네스, 동일한 모델, 동일한 예산으로 실행되었으며, 두 번째 심사자와 블라인드 검증된 심사자가 점수를 매겼습니다(합의율 90.6%, Cohen's kappa 0.81). 시스템별 전체 표, 코드 인텔리전스 결과, 재현 명령어: **[BENCHMARKS.md](./BENCHMARKS.md)**.

---

## 사전 요구 사항

| 요구 사항 | 최소 | 확인 | 설치 |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(권장)* | 모든 버전 | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(대안)* | 모든 버전 | `pipx --version` | `pip install pipx` |

**macOS 빠른 설치 (Homebrew):**
```bash
brew install python@3.12 uv
```

**Windows 빠른 설치:**
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

## 설치 방법

> **공식 패키지:** PyPI 패키지는 `graphifyy`입니다(y가 두 개). PyPI의 다른 `graphify*` 패키지는 관련이 없습니다. CLI 명령어는 여전히 `graphify`입니다.

**1단계 — 패키지 설치:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**2단계 — AI 어시스턴트에 스킬 등록:**

```bash
graphify install
```

완료되었습니다. AI 어시스턴트를 열고 `/graphify .`를 입력하세요.

사용자 프로필 대신 현재 저장소에 어시스턴트 스킬을 설치하려면 `--project`를 추가하세요:

```bash
graphify install --project
graphify install --project --platform codex
```

프로젝트 범위 설치는 현재 디렉터리 아래에 작성됩니다. 예를 들어 `.claude/skills/graphify/SKILL.md` 또는 `.agents/skills/graphify/SKILL.md`(스킬이 필요에 따라 로드하는 `references/` 사이드카 포함)이며, 커밋할 수 있는 파일에 대한 `git add` 힌트를 출력합니다. 프로젝트 범위 설치를 지원하는 플랫폼별 명령어는 동일한 플래그를 받습니다. 예를 들어 `graphify claude install --project` 또는 `graphify codex install --project`입니다.

> **PowerShell 참고:** `/graphify .`가 아니라 `graphify .`를 사용하세요 — 선행 슬래시는 PowerShell에서 경로 구분자입니다.

> **`graphify: command not found`?** `uv tool install` / `pipx install`은 `graphify` 명령어를 자체 도구 bin 디렉터리(`~/.local/bin`)에 넣습니다. 설치 직후 셸이 이를 찾지 못한다면 — 새로 설치한 macOS + zsh 환경에서 흔한 일입니다 — 그 디렉터리가 아직 `PATH`에 없는 것입니다: `uv tool update-shell`(또는 `pipx ensurepath`)을 실행한 다음 새 터미널을 여세요. 순수 `pip`를 사용하는 경우, `~/.local/bin`(Linux) 또는 `~/Library/Python/3.x/bin`(Mac)을 PATH에 추가하거나 `python -m graphify`를 실행하세요.

> **설치 대신 `uvx` / `uv tool run`으로 실행하시나요?** 명령어가 아니라 패키지 이름을 지정하세요: `uvx --from graphifyy graphify install`. 단순히 `uvx graphify …`는 실패합니다(`No solution found … no versions of graphify`). `uv tool run`이 첫 단어를 *패키지*로 읽기 때문이며, 패키지는 `graphifyy`입니다 — `graphify` 명령어는 그 안에 있습니다.

> **가능하면 Mac/Windows에서 `pip install`을 피하세요.** 스킬은 런타임에 `graphify-out/.graphify_python`에서 Python을 해석합니다; 이것이 `pip`가 패키지를 설치한 환경과 다른 환경을 가리키면 `ModuleNotFoundError: No module named 'graphify'`가 발생합니다. `uv tool install`과 `pipx install`은 패키지를 자체 환경에 격리시켜 이를 완전히 피합니다.

> **Git 훅과 uv tool / pipx:** `graphify hook install`은 설치 시 현재 인터프리터 경로를 훅 스크립트에 직접 내장하므로, `~/.local/bin`이 PATH에 없는 GUI git 클라이언트나 CI 러너에서도 post-commit 훅이 올바르게 실행됩니다. graphify를 재설치하거나 업그레이드하면 내장된 경로를 새로 고치기 위해 `graphify hook install`을 다시 실행하세요.

> **엄격 모드(Claude Code):** `graphify install --project --strict`는 어시스턴트가 실제로 그래프를 사용하도록 만듭니다. 기본 설치는 파일을 읽기 전에 `graphify query`를 실행하도록 *유도*합니다; 엄격 모드는 세션의 첫 번째 원시 소스 읽기를 *차단*하고 그래프로 리디렉션한 다음 유도 모드로 되돌아갑니다(따라서 세션당 최대 한 번만 실행되고 절대 걸리지 않습니다). 런타임에 `GRAPHIFY_HOOK_STRICT=1`/`0`로 전환할 수 있습니다; 기본 설치는 변경되지 않습니다(부드러운 유도).

<details>
<summary><b>플랫폼 선택</b> (20개 이상의 어시스턴트, 클릭하여 펼치기)</summary>

| 플랫폼 | 설치 명령어 |
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

Codex 사용자는 병렬 추출을 위해 `~/.codex/config.toml`의 `[features]` 아래에 `multi_agent = true`도 필요합니다. CodeBuddy는 Claude Code와 동일한 Agent tool 및 PreToolUse 훅 메커니즘을 사용합니다. Factory Droid는 병렬 서브에이전트 디스패치에 `Task` 도구를 사용합니다. OpenClaw와 Aider는 순차적 추출을 사용합니다(이 플랫폼들에서는 병렬 에이전트 지원이 아직 초기 단계입니다). Trae는 병렬 서브에이전트 디스패치에 Agent tool을 사용하며 `PreToolUse` 훅을 **지원하지 않으므로** AGENTS.md가 상시 작동 메커니즘입니다.

`--platform agents`(별칭 `--platform skills`)는 일반적인 크로스 프레임워크 [Agent-Skills](https://github.com/anthropics/skills) 위치를 대상으로 합니다: 전역 설치를 위한 스펙의 사용자 전역 `~/.agents/skills/`(`npx skills` 및 스펙 준수 프레임워크가 읽음)와 프로젝트(`--project`) 설치를 위한 `./.agents/skills/`입니다. 단순한 `graphify install`은 설계상 단일 플랫폼(Claude Code)으로 유지됩니다 — `.agents/skills`를 읽는 모든 프레임워크에서 스킬을 검색 가능하게 하려면 명명된 `agents` 플랫폼을 사용하세요.

> Codex는 `/graphify` 대신 `$graphify`를 사용합니다.

</details>

<details>
<summary><b>선택적 추가 기능</b> (필요한 것만 설치)</summary>

| 추가 기능 | 추가되는 것 | 설치 |
|---|---|---|
| `pdf` | PDF 추출 | `uv tool install "graphifyy[pdf]"` |
| `office` | `.docx` 및 `.xlsx` 지원 | `uv tool install "graphifyy[office]"` |
| `google` | Google Sheets 렌더링 | `uv tool install "graphifyy[google]"` |
| `video` | 비디오/오디오 전사(faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | MCP stdio 서버 | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Neo4j push 지원 | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | FalkorDB push 지원 | `uv tool install "graphifyy[falkordb]"` |
| `svg` | SVG 그래프 내보내기 | `uv tool install "graphifyy[svg]"` |
| `leiden` | Leiden 커뮤니티 감지(Python < 3.13만 해당) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | 로컬 Ollama 추론 | `uv tool install "graphifyy[ollama]"` |
| `openai` | OpenAI / OpenAI 호환 API | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic Claude API(`--backend claude`, `ANTHROPIC_API_KEY` 사용) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock(IAM 사용, API 키 불필요) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service(`--backend azure`, `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT` 사용) | `uv tool install "graphifyy[openai]"` |
| `sql` | SQL 스키마 추출 | `uv tool install "graphifyy[sql]"` |
| `postgres` | 실시간 PostgreSQL 조사(`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | BYOND DreamMaker `.dm`/`.dme` AST 추출(플랫폼에 맞는 wheel이 없는 경우 C 컴파일러 + `python3-dev`가 필요할 수 있음) | `uv tool install "graphifyy[dm]"` |
| `terraform` | Terraform / HCL `.tf`/`.tfvars`/`.hcl` AST 추출 | `uv tool install "graphifyy[terraform]"` |
| `pascal` | Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` AST 추출(더 정확한 `calls`/`inherits` 엣지; 없을 경우 regex 추출기로 대체) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | 중국어 쿼리 세그먼트화(jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | 위의 모든 것 | `uv tool install "graphifyy[all]"` |

</details>

---

## 어시스턴트가 항상 그래프를 사용하도록 설정

그래프를 구축한 후 프로젝트에서 이것을 한 번 실행하세요:

| 플랫폼 | 명령어 |
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

이것은 어시스턴트에게 전체 보고서를 읽거나 원시 파일을 grep하는 대신 `graphify query "<question>"`과 같은 범위가 지정된 쿼리를 선호하여, 코드베이스 질문에 대해 지식 그래프를 참조하도록 알려주는 작은 구성 파일을 작성합니다.

- **훅 플랫폼**(Claude Code, Gemini CLI): 검색 스타일 도구 호출 전에(그리고 Claude Code에서는 Read/Glob 도구를 통해 소스 파일을 하나씩 읽기 전에) 훅이 자동으로 실행되어 어시스턴트를 그래프 경로로 유도합니다.
- **명령어 파일 플랫폼**(Codex, OpenCode, Cursor 등): 영구적인 명령어 파일(`AGENTS.md`, `.cursor/rules/` 등)이 동일한 쿼리 우선 가이드를 제공합니다.

`GRAPH_REPORT.md`는 광범위한 아키텍처 검토를 위해 여전히 사용할 수 있습니다.

**CodeBuddy**는 Claude Code와 동일한 두 가지 작업을 수행합니다: 아키텍처 질문에 답하기 전에 `graphify-out/GRAPH_REPORT.md`를 읽도록 CodeBuddy에게 알려주는 `CODEBUDDY.md` 섹션을 작성하고, Bash 검색 명령어 및 파일 읽기 전에 실행되어 `graphify query`를 사용하도록 유도하는 `PreToolUse` 훅(`.codebuddy/settings.json`)을 설치합니다.

**Codex**는 이 플랫폼에서 실제로 상시 그래프 가이드를 담당하는 `AGENTS.md`에 작성합니다. `graphify codex install`은 `.codex/hooks.json`(`graphify hook-check`)에 `PreToolUse` 훅도 등록하지만, 그 항목은 의도적으로 **no-op**입니다: Codex Desktop은 `PreToolUse`에서 `hookSpecificOutput.additionalContext`를 거부하므로, 거기서 유도를 보내면 Bash 도구 호출이 깨질 것입니다. 훅(`graphify hook-guard`)이 유도를 담당하는 Claude Code와 달리, Codex에서는 훅이 실행되지만 의도적으로 아무것도 하지 않으며, `AGENTS.md`가 상시 작동 메커니즘입니다.

**Kilo Code**는 Graphify 스킬을 `~/.config/kilo/skills/graphify/SKILL.md`에, 네이티브 `/graphify` 명령어를 `~/.config/kilo/command/graphify.md`에 설치합니다. `graphify kilo install`은 `AGENTS.md`와 함께 네이티브 `tool.execute.before` 플러그인(`.kilo/plugins/graphify.js` + `.kilo/kilo.json` 또는 `.kilo/kilo.jsonc` 등록)도 작성하여, Kilo가 네이티브 `.kilo` 구성을 통해 동일한 상시 그래프 알림 동작을 받도록 합니다.

**Cursor**는 `alwaysApply: true`로 `.cursor/rules/graphify.mdc`를 작성하므로, Cursor는 훅 없이도 모든 대화에 이를 자동으로 포함시킵니다.

모든 플랫폼에서 한 번에 graphify를 제거하려면: `graphify uninstall`(`graphify-out/`도 삭제하려면 `--purge` 추가). 또는 플랫폼별 명령어를 사용하세요(예: `graphify claude uninstall`).

---

## 보고서 구성 요소

- **God 노드** — 프로젝트에서 가장 많이 연결된 개념들. 모든 것이 이들을 통해 흐릅니다.
- **놀라운 연결** — 다른 파일이나 모듈에 있는 항목들 간의 링크. 얼마나 예상 밖인지에 따라 순위가 매겨집니다.
- **"이유"** — 인라인 주석(`# NOTE:`, `# WHY:`, `# HACK:`), docstring, 문서의 설계 근거는 그것이 설명하는 코드에 연결된 별도의 노드로 추출됩니다.
- **추천 질문** — 그래프가 답변하기에 특히 적합한 4-5개의 질문.
- **신뢰도 태그** — 추론된 모든 관계는 `EXTRACTED`, `INFERRED`, 또는 `AMBIGUOUS`로 표시됩니다. 무엇이 발견되었고 무엇이 추측되었는지 항상 알 수 있습니다.

---

## 지원하는 파일 유형

| 유형 | 확장자 |
|------|-----------|
| 코드(36개 tree-sitter 문법) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml`(`.dm`/`.dme`는 `uv tool install graphifyy[dm]` 필요; `.mts`/`.cts`는 TypeScript 문법을 재사용하며, `.cc`/`.cxx`와 CUDA `.cu`/`.cuh` 및 Metal `.metal`은 C++ 문법을 재사용) |
| Salesforce Apex | `.cls .trigger`(regex 기반; 클래스, 인터페이스, enum, 메서드, 트리거, SOQL/DML 엣지) |
| Terraform / HCL | `.tf .tfvars .hcl`(`uv tool install graphifyy[terraform]` 필요) |
| MCP 구성 | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — 서버 노드, 패키지 참조, 환경 변수 요구 사항을 추출 |
| 패키지 매니페스트 | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — 패키지당 하나의 표준 패키지 노드(이름 기준)와 `depends_on` 엣지, 따라서 여러 매니페스트에서 참조되는 패키지는 하나의 허브가 됨 |
| 문서 | `.md .mdx .qmd .html .txt .rst .yaml .yml`(마크다운 `[text](./other.md)` 링크와 `[[wikilinks]]`는 문서 간 `references` 엣지가 됨) |
| Office | `.docx .xlsx`(`uv tool install graphifyy[office]` 필요) |
| Google Workspace | `.gdoc .gsheet .gslides`(선택 사항; `gws` 인증 및 `--google-workspace` 필요; Sheets는 `uv tool install graphifyy[google]` 필요) |
| PDF | `.pdf` |
| 이미지 | `.png .jpg .webp .gif` |
| 비디오 / 오디오 | `.mp4 .mov .mp3 .wav` 등(`uv tool install graphifyy[video]` 필요) |
| YouTube / URL | 모든 비디오 URL(`uv tool install graphifyy[video]` 필요) |

코드는 **API 호출 없이 로컬에서** 추출됩니다(tree-sitter를 통한 AST). 다른 모든 것은 AI 어시스턴트의 모델 API를 거칩니다.

Google Drive for desktop의 `.gdoc`, `.gsheet`, `.gslides` 파일은 바로가기 포인터이며 문서 콘텐츠가 아닙니다. 헤드리스 추출에 네이티브 Google Docs, Sheets, Slides를 포함하려면, [`gws` CLI](https://github.com/googleworkspace/cli)를 설치하고 인증한 다음 실행하세요:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

`GRAPHIFY_GOOGLE_WORKSPACE=1`을 설정할 수도 있습니다. Graphify는 바로가기를 `graphify-out/converted/`에 Markdown 사이드카로 내보낸 다음 해당 파일을 추출합니다.

---

## 자주 사용하는 명령어

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

위의 [Decouple: 위험도 평가 기반 Extract-Class 후보](#decouple-risk-scored-extract-class-candidates) 또는 아래의 [전체 명령어 참조](#full-command-reference)를 참고하세요.

---

## 파일 무시 설정

프로젝트 루트에 `.graphifyignore`를 생성하세요 — `!` 부정을 포함하여 `.gitignore`와 동일한 문법입니다.

**`.gitignore`는 자동으로 존중됩니다.** graphify는 각 디렉터리의 `.gitignore`를 읽습니다. `.graphifyignore`도 있는 경우, 두 가지가 **병합**됩니다 — `.graphifyignore` 패턴이 마지막에 평가되므로 충돌 시 우선합니다(`!` 부정 포함). `.graphifyignore`를 추가하는 것은 항상 더 많이 제외하는 것뿐입니다; `.gitignore`가 이미 제외한 파일을 다시 포함시키지는 않습니다. 하위 디렉터리 범위는 git과 정확히 동일하게 작동합니다 — 무시 파일은 자신의 하위 트리에만 영향을 미칩니다.

git이 무시하는 생성되거나 트랜스파일된 코드가 그래프에 속해야 할 때 `graphify extract`에 `--no-gitignore`를 전달하세요. 이는 `.gitignore`와 `.git/info/exclude`를 비활성화합니다; `.graphifyignore`는 여전히 적용됩니다.

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

## 팀 설정

`graphify-out/`은 팀의 모든 사람이 지도를 가지고 시작할 수 있도록 git에 커밋되도록 만들어졌습니다.

**권장 `.gitignore` 추가 사항:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json`은 이제 이식 가능합니다 — 키가 상대 경로로 저장되고 로드 시 다시 앵커되므로, 이를 커밋하는 것은 안전하며 첫 체크아웃 시 전체 재구축을 피할 수 있습니다.

**워크플로:**
1. 한 사람이 `/graphify .`를 실행하고 `graphify-out/`을 커밋합니다.
2. 모두가 pull합니다 — 그들의 어시스턴트가 즉시 그래프를 읽습니다.
3. 각 커밋 후 자동 재구축을 위해 `graphify hook install`을 실행하세요(AST만, API 비용 없음). 이것은 또한 `graph.json`이 충돌 마커와 함께 남지 않도록 git merge driver를 설정합니다 — 병렬로 커밋하는 두 개발자는 그래프가 자동으로 union-merge됩니다.
4. 문서나 논문이 변경되면, 해당 노드를 새로 고치기 위해 `/graphify --update`를 실행하세요.

---

## 그래프 직접 사용하기

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

MCP 서버는 어시스턴트에게 구조화된 액세스를 제공합니다: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### 공유 HTTP 서버

`--transport stdio`(기본값)는 개발자당 하나의 로컬 서버를 생성합니다. `--transport http`는 MCP Streamable HTTP 전송을 통해 동일한 도구를 제공하므로, 하나의 공유 프로세스가 전체 팀에 그래프를 제공할 수 있습니다 — 클라이언트는 로컬에서 graphify를 실행하는 대신 IDE MCP 구성을 `http://<host>:8080/mcp`로 지정합니다.

| 플래그 | 기본값 | 목적 |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | 제공할 전송 방식 |
| `--host` | `127.0.0.1` | HTTP 바인드 호스트(localhost를 넘어 노출하려면 `0.0.0.0` 사용) |
| `--port` | `8080` | HTTP 바인드 포트 |
| `--api-key` | env `GRAPHIFY_API_KEY` | `Authorization: Bearer <key>`(또는 `X-API-Key`) 필요 |
| `--path` | `/mcp` | HTTP 마운트 경로 |
| `--json-response` | 꺼짐 | SSE 스트림 대신 일반 JSON 반환 |
| `--stateless` | 꺼짐 | 세션별 상태 없음(로드 밸런싱/CI 배포용) |
| `--session-timeout` | `3600` | N초 후 유휴 상태 세션을 정리(`0`은 비활성화) |

기본 `127.0.0.1` 바인드는 loopback 전용입니다. 공유 호스트에 노출할 때는 `--host 0.0.0.0`**과** `--api-key`를 함께 설정하세요. 컨테이너에서 실행:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **WSL / Linux 참고:** Ubuntu는 `python`이 아니라 `python3`를 제공합니다. 충돌을 피하려면 venv를 사용하세요:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## 환경 변수

이것들은 **헤드리스 / CI 추출**(`graphify extract`)에만 필요합니다. IDE 내에서 `/graphify` 스킬을 통해 실행할 때는 모델 API가 IDE 세션에서 제공되므로 — 추가 키가 필요하지 않습니다.

| 변수 | 용도 | 필요한 시점 |
|---|---|---|
| `ANTHROPIC_API_KEY` | Claude(Anthropic) 백엔드 | `--backend claude` |
| `ANTHROPIC_BASE_URL` | Anthropic 호환 엔드포인트 URL(LiteLLM 프록시, 게이트웨이 등) | `--backend claude`(기본값: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Claude 백엔드의 모델 이름 — 사용자 지정 엔드포인트의 경우 서버가 노출하는 모델 이름/별칭 사용 | `--backend claude`(기본값: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` 또는 `GOOGLE_API_KEY` | Google Gemini 백엔드 | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI 또는 OpenAI 호환 API | `--backend openai`(로컬 서버는 비어 있지 않은 모든 값을 허용) |
| `OPENAI_BASE_URL` | OpenAI 호환 서버 URL(llama.cpp, vLLM, LM Studio 등) | `--backend openai`(기본값: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | OpenAI 백엔드의 모델 이름 — self-hosted 서버의 경우, 서버가 노출하는 모델 이름/별칭 사용(`/v1/models` 엔드포인트 확인), 예: llama.cpp의 경우 `LFM2.5-8B-A1B-UD-Q4_K_XL` | `--backend openai`(기본값: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | DeepSeek 백엔드 | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Kimi Code 백엔드 | `--backend kimi` |
| `OLLAMA_BASE_URL` | 로컬 Ollama 추론 URL | `--backend ollama`(기본값: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Ollama 모델 이름 | `--backend ollama`(기본값: 자동 감지) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Ollama KV-cache 윈도우 크기를 재정의 | 선택 사항 — 기본적으로 자동 크기 조정 |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | 로드된 Ollama 모델을 유지할 분 수 | 선택 사항 — 각 청크 후 언로드하려면 `0`으로 설정 |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI Service 백엔드 | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | Azure 리소스 엔드포인트 URL | `--backend azure`(API 키와 함께 필요) |
| `AZURE_OPENAI_API_VERSION` | Azure API 버전 재정의 | 선택 사항 — 기본값 `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` 또는 `GRAPHIFY_AZURE_MODEL` | Azure 배포 이름 | 선택 사항 — 기본값 `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — 표준 자격 증명 체인 | `--backend bedrock`(API 키 없음, IAM 사용) |
| `GRAPHIFY_MAX_WORKERS` | AST 병렬 처리 스레드 수 | 선택 사항 — `--max-workers` 플래그도 있음 |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | 밀도가 높은 코퍼스를 위한 출력 상한 인상 | 선택 사항 — 예: 큰 파일의 경우 `32768` |
| `GRAPHIFY_API_TIMEOUT` | HTTP, claude-cli, Anthropic SDK, Bedrock 백엔드의 호출당 타임아웃(초, 기본값: 600) | 선택 사항 — `--api-timeout` 플래그도 있음 |
| `GRAPHIFY_MAX_RETRIES` | 포기하기 전에 rate-limited(429) 요청을 재시도할 횟수(기본값: 6; `Retry-After` 존중) | 선택 사항 — 엄격한 조직별 제한을 위해 높임(예: kimi); `0`은 비활성화 |
| `GRAPHIFY_FORCE` | 노드가 더 적더라도 그래프 재구축을 강제 | 선택 사항 — `--force` 플래그도 있음 |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Google Workspace 내보내기 자동 활성화 | 선택 사항 — `1`로 설정 |
| `GRAPHIFY_TRIAGE_BACKEND` | `graphify prs --triage`의 백엔드 | 선택 사항 — 사용 가능한 키에서 자동 감지 |
| `GRAPHIFY_TRIAGE_MODEL` | triage용 모델 재정의 | 선택 사항 — 예: `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | `~/.cache/graphify-queries.log`의 로컬 쿼리 로그를 켜려면 `1`로 설정(각 query/path/explain 질문 + 코퍼스 경로 기록). 기본적으로 꺼짐 — 옵트인하지 않으면 아무것도 기록되지 않음(#1797) | 선택 사항 |
| `GRAPHIFY_QUERY_LOG` | 쿼리 로그를 활성화하고 기본값 대신 이 경로에 씀 | 선택 사항 — 이것 또는 `_ENABLE`이 설정되지 않으면 꺼짐 |
| `GRAPHIFY_QUERY_LOG_DISABLE` | 쿼리 로그를 강제로 끄려면 `1`로 설정(enable 변수보다 우선) | 선택 사항 |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | 로그가 활성화되면 전체 서브그래프 응답도 기록(기본적으로 꺼짐) | 선택 사항 |
| `GRAPHIFY_MAX_GRAPH_BYTES` | graph.json의 512 MiB 크기 상한 재정의 — 예: `700MB`, `2GB`, 또는 일반 바이트 | 선택 사항 — 매우 큰 코퍼스에 유용 |
| `GRAPHIFY_MAX_CONTEXTS` | 하나의 다중 프로젝트 MCP 서버가 유지하는 비기본 프로젝트 그래프의 최대 수 | 선택 사항 — 기본값: `8`; 유효하지 않은 값은 `8`을 사용하고, `1` 미만의 값은 `1`을 사용 |
| `GRAPHIFY_LLM_TEMPERATURE` | 시맨틱 추출을 위한 LLM 온도 재정의 — 예: `0.7`, 생략하려면 `none` | 선택 사항 — o1/o3/o4/gpt-5 추론 모델의 경우 자동으로 생략됨 |

---

## 개인정보 보호

- **코드 파일** — tree-sitter를 통해 로컬에서 처리됩니다. 외부로 데이터가 전송되지 않습니다. 코드만 있는 코퍼스는 API 키가 필요하지 않습니다 — `graphify extract`는 완전히 오프라인으로 실행됩니다. 혼합된 저장소에서는 `--code-only`를 추가하여 코드만 인덱싱하고 그렇지 않으면 LLM이 필요한 문서/PDF/이미지를 건너뛰세요.
- **비디오 / 오디오** — faster-whisper로 로컬에서 전사됩니다. 외부로 데이터가 전송되지 않습니다.
- **문서, PDF, 이미지** — 시맨틱 추출을 위해 AI 어시스턴트로 전송됩니다(`/graphify` 스킬을 통해, IDE 세션이 실행하는 모델 사용). 헤드리스 `graphify extract`는 `GEMINI_API_KEY` / `GOOGLE_API_KEY`(Gemini), `MOONSHOT_API_KEY`(Kimi), `ANTHROPIC_API_KEY`(Claude), `OPENAI_API_KEY`(OpenAI), `DEEPSEEK_API_KEY`(DeepSeek), 실행 중인 Ollama 인스턴스(`OLLAMA_BASE_URL`), 표준 제공자 체인을 통한 AWS 자격 증명(Bedrock - API 키 불필요, IAM 사용), 또는 `claude` CLI 바이너리(Claude Code - API 키 불필요, Claude 구독 사용)가 필요합니다. `--dedup-llm` 플래그는 동일한 키를 사용합니다.
- **데이터 거주지** — `graphify extract`는 설정된 API 키에 따라 사용할 제공자를 자동으로 감지합니다(우선순위: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). 데이터 거주지 요구 사항이 있는 코드의 경우, `--backend ollama`(완전 로컬)를 사용하거나 명시적인 `--backend` 플래그를 전달하세요. Kimi(`MOONSHOT_API_KEY`)는 중국의 Moonshot AI 서버로 라우팅됩니다.
- **텔레메트리 없음**, 사용 추적 없음, 분석 없음.
- **쿼리 로깅** — 모든 `graphify query`, `graphify path`, `graphify explain`, MCP `query_graph` 호출은 JSON Lines 형식으로 `~/.cache/graphify-queries.log`에 기록됩니다(타임스탬프, 질문, 코퍼스, 반환된 노드, 지속 시간). 전체 서브그래프 응답은 기본적으로 저장되지 **않습니다**. 옵트아웃하려면 `GRAPHIFY_QUERY_LOG_DISABLE=1`을 설정하거나, 코드 경로를 비활성화하지 않고 조용히 하려면 `GRAPHIFY_QUERY_LOG=/dev/null`을 설정하세요.

---

## 제한 사항 및 적용 범위

graphify가 의도적으로 **하지 않는** 것, 그리고 다루는 범위가 어디에서 끝나는지:

- **시맨틱/벡터 검색 엔진이 아닙니다.** 그래프는 구조적입니다 — 노드와 타입이 지정된 엣지는 임베딩이 아니라 소스에서 해석된 것입니다. `graphify query`/`path`/`explain`은 그 구조를 탐색할 뿐이므로, 엣지로 표현되지 않은 연결은 "의미적으로" 관련이 있더라도 찾아낼 수 없습니다. 유사도/최근접 이웃 기반의 대체 수단은 없습니다.
- **문서, PDF, 이미지, 그리고 헤드리스 비디오/URL 추출은 로컬 전용이 아닙니다.** 완전히 오프라인으로 실행되는 것은 코드(tree-sitter AST)와 오디오/비디오 전사(faster-whisper)뿐입니다. 문서/PDF/이미지 추출은 항상 LLM을 호출합니다 — `/graphify` 스킬을 통해 AI 어시스턴트의 모델을 사용하거나, 헤드리스 `graphify extract`에서는 설정된 백엔드 API 키를 사용합니다. 각 경로에 어떤 플래그나 키가 필요한지는 위의 [개인정보 보호](#개인정보-보호)를 참고하세요.
- **decouple의 상태 공유 검사는 모든 언어를 다루지 않습니다.** C는 완전한 타입 추론 없이는 신뢰할 수 있는 `self`/`this` 신호가 없어 제외됩니다(위의 [언어 지원 표](#decouple-risk-scored-extract-class-candidates) 참고). 지원되지 않는 언어의 god 노드, 또는 소스를 읽을 수 없는 노드는 검증된 상태 검사 대신 호출 그래프에만 기반한 점수(`state_analysis: "skipped"`)로 대체됩니다.
- **3D 데이터 흐름 층(floor)은 이름 기반 휴리스틱이며, 데이터 흐름/테인트 분석이 아닙니다.** `data_floor`의 I/O 경계 감지(파서, 로더, 리더, 라이터, DB/HTTP 클라이언트)는 명명 규칙(`boundary_reason`)에 따라 매칭됩니다. 관례를 따르지 않는 이름의 경계 노드는 누락될 수 있으며, 이는 그래프의 나머지 부분이 실제로 얼마나 깊은지를 과소평가하게 만듭니다.
- **신뢰도 태그는 graphify 자체의 해석 신뢰도이지, 절대적인 사실이 아닙니다.** `INFERRED`와 `AMBIGUOUS` 엣지는 최선을 다한 해석 결과이며 여전히 틀릴 수 있습니다. 특히 정적 AST 분석으로는 완전히 해석할 수 없는 매우 동적인 관용구(리플렉션, 런타임 디스패치, 메타프로그래밍)에서 더욱 그렇습니다.
- **HTML 시각화와 그래프 크기 모두 상한이 있습니다.** `graph.html` / `DECOUPLE.html`은 기본적으로 노드가 5,000개를 넘으면 생성을 건너뜁니다(`MAX_NODES_FOR_VIZ`, `GRAPHIFY_VIZ_NODE_LIMIT`으로 상향 가능). `graph.json` 자체는 512 MiB로 제한됩니다(`GRAPHIFY_MAX_GRAPH_BYTES`로 재정의 가능). 두 한계를 넘는 코퍼스에는 `--no-viz`와 `query`/`path`/`explain`을 함께 사용하세요.
- **프로젝트 간 인식은 자동이 아니라 옵트인입니다.** `graphify query`는 지정한 그래프 하나만 볼 수 있습니다. 여러 저장소에 걸친 질문을 하려면 먼저 각 프로젝트를 공유 그래프에 명시적으로 등록해야 합니다(`graphify global add`, MCP 서버당 기본값이 아닌 컨텍스트는 `GRAPHIFY_MAX_CONTEXTS`개로 제한) — graphify는 스스로 여러분의 컴퓨터에서 다른 저장소를 스캔하지 않습니다.
- **병렬 멀티 에이전트 추출은 플랫폼에 따라 다릅니다.** 서브 에이전트를 생성할 수 있는 어시스턴트 측 지원이 필요합니다(Codex는 `~/.codex/config.toml`의 `multi_agent = true`, Claude Code/CodeBuddy/Factory Droid/Trae는 Agent/Task 도구). OpenClaw와 Aider는 현재 순차적으로만 추출합니다.
- **공유 MCP HTTP 서버는 기본적으로 loopback에만 바인딩됩니다.** 다른 머신에서 접근하려면 `--host 0.0.0.0`**과** `--api-key`를 명시적으로 함께 설정해야 합니다. graphify는 이 단일 bearer 토큰 외에는 TLS나 다른 인증을 관리하지 않습니다.
- **PowerShell은 앞의 `/`를 경로 구분자로 해석합니다.** 이 때문에 `/graphify .`는 Windows PowerShell에서 실패합니다. graphify의 버그가 아니라, 대신 `graphify .`를 사용하세요.

---

## 문제 해결

**설치 후 `graphify: command not found`**
CLI는 설치되었지만 bin 디렉터리가 셸의 `PATH`에 없습니다. 설치한 방법에 맞는 수정 방법을 선택하세요:
- **uv**(`uv tool install graphifyy`): 명령어는 uv의 도구 bin 디렉터리(`~/.local/bin`)에 위치하며, 새로운 macOS/zsh 설정에서는 종종 `PATH`에 없습니다. `uv tool update-shell`을 실행한 다음 새 터미널을 여세요. (`uv tool dir --bin`으로 디렉터리를 찾을 수 있습니다.)
- **pipx**(`pipx install graphifyy`): `pipx ensurepath`를 실행한 다음 새 터미널을 여세요.
- **pip**(`pip install graphifyy`): pip는 `PATH`에 없을 수 있는 사용자 bin 디렉터리에 스크립트를 설치합니다 — `~/.zshrc`/`~/.bashrc`에서 PATH에 `~/Library/Python/3.x/bin`(macOS) 또는 `~/.local/bin`(Linux)을 추가하거나 그냥 `python -m graphify`를 실행하세요.

**`uvx graphify …` 또는 `uv tool run graphify …`가 `graphify`를 해석하지 못함**
PyPI 패키지는 `graphifyy`입니다; `graphify`는 그것이 제공하는 명령어일 뿐입니다. `uv tool run`은 첫 단어를 *패키지 이름*으로 취급하므로, `graphify`라는 패키지를 찾고 `No solution found … no versions of graphify`를 보고합니다. 패키지를 명시적으로 지정하세요: `uvx --from graphifyy graphify install`(`uv tool run --from graphifyy graphify install`과 동일). 또는 `uv tool install graphifyy`를 한 번 실행하고 `graphify`를 직접 호출하세요.

**`uv run --with graphifyy python -m graphify`가 조용히 더 오래된 설치를 실행함**
`uv run`은 *시스템* Python을 사용하므로, 더 오래된 `graphifyy`도 그곳에 있다면(예: 과거의 `pip install graphifyy`), Python이 `sys.path`에서 그 사본을 먼저 찾을 수 있고 `--with graphifyy`가 이를 재정의하지 않습니다. 오류 없이 실행되지만 *이전* 버전의 동작을 얻게 됩니다 — 예를 들어 `OPENAI_BASE_URL` 같은 환경 재정의가 조용히 무시되어, 요청이 기본 엔드포인트에 도달하고 잘못된 키처럼 보이는 401로 실패합니다. 지문은 `warning: skill is from graphify <newer>, package is <older>` 줄입니다 — 이는 단순히 오래된 스킬이 아니라 다른 설치가 로드되었음을 의미합니다. 실제로 어느 사본이 로드되었는지 확인하세요:
```bash
python -c "import graphify; print(graphify.__file__)"
```
그런 다음 설치된 명령어를 직접 실행하거나(uv가 관리하는 사본 사용), 오래된 시스템 사본을 제거하세요:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify`는 작동하지만 `graphify` 명령어는 작동하지 않음**
셸의 `PATH`에 명령어가 설치된 bin 디렉터리가 포함되어 있지 않습니다. 순수 `pip`보다 `uv tool install` / `pipx install`을 선호하고, `uv tool update-shell` / `pipx ensurepath`를 실행한 다음 새 터미널을 여세요(위의 설치 참고 사항 참조).

**PowerShell에서 `/graphify .`가 "path not recognized"를 유발함**
PowerShell은 선행 `/`를 경로 구분자로 취급합니다. Windows에서는 `graphify .`(슬래시 없이)를 사용하세요.

**`--update` 또는 재구축 후 그래프에 노드가 줄어듦**
리팩터링으로 파일이 삭제되었다면 오래된 노드가 남아 있습니다. 재구축의 노드 수가 더 적더라도 덮어쓰려면 `--force`(또는 `GRAPHIFY_FORCE=1` 설정)를 전달하세요.

**`extract`가 "extraction was incomplete ... refusing to overwrite"와 함께 종료됨**
추출 단계가 충돌하거나 순회가 코퍼스를 완전히 읽을 수 없으면, 실행 결과가 완전한 실행보다 작아지므로 `graphify extract`는 더 큰 기존 그래프를 부분적인 결과로 덮어쓰기를 거부합니다(`graph.json`을 보호). 근본적인 실패를 수정하고 다시 실행하거나, 그래도 덮어쓰려면 `--allow-partial`을 전달하세요.

**그래프에 동일한 엔터티에 대한 중복 노드가 있음(고스트 중복)**
고스트 중복(동일한 심볼이 두 번 나타남 — 한 번은 소스 위치가 있는 AST 추출에서, 한 번은 위치가 없는 시맨틱 추출에서)은 이제 빌드 시 자동으로 병합됩니다. v0.8.33 이전에 구축된 그래프에서 이를 본다면, 정리를 위해 전체 재추출을 실행하세요:
```bash
graphify extract . --force
```

**Ollama가 VRAM을 소진하거나 / context 윈도우가 초과됨**
KV-cache 윈도우는 자동으로 크기가 조정되지만 GPU에 비해 너무 클 수 있습니다. 줄이세요:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**`LLM returned invalid JSON` / `Unterminated string` 경고**
모델의 JSON 응답이 출력 토큰 한도에 도달하여 문자열 중간에서 잘렸습니다. graphify는 자동으로 복구합니다(청크를 나누고 절반을 다시 추출하며, 지나치게 큰 단일 문서는 먼저 제목/단락 경계에서 조각내어 전체 파일이 여전히 커버되도록 함), 따라서 이 경고들은 시끄럽지만 데이터 손실은 아닙니다. 소음을 줄이려면, 출력 상한을 높이거나 각 청크의 출력을 줄이세요:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
OpenRouter 같은 클라우드 게이트웨이를 사용할 때는, Ollama shim보다 `--backend openai`(`OPENAI_BASE_URL` 설정)를 선호하세요 — 더 깔끔한 OpenAI 호환 경로입니다. 모델에 자체 max-output 상한이 있다면, `--token-budget`을 낮추는 것이 신뢰할 수 있는 지렛대입니다.

**Graph HTML이 브라우저에서 열기에 너무 큼(5000개 이상의 노드)**
HTML 생성을 건너뛰고 JSON을 직접 사용하세요:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**두 개발자가 동시에 커밋한 후 `graph.json`에 충돌 마커가 있음**
`graphify hook install`을 실행하세요 — 이것은 `graph.json`을 자동으로 union-merge하는 git merge driver를 설정하여 충돌이 절대 발생하지 않도록 합니다.

**문서나 PDF에 대한 추출이 빈 노드/엣지를 반환함**
문서, PDF, 이미지는 LLM 호출이 필요합니다 — 코드만 있는 코퍼스는 키가 필요하지 않습니다. API 키가 설정되어 있고 백엔드가 올바른지 확인하세요:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**IDE에서 스킬 버전 불일치 경고**
설치된 graphify 버전이 스킬 파일과 다릅니다. 업데이트하세요:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**매번 `graphify extract` 후 Claude Code 프롬프트 캐시가 무효화됨**
Graphify는 워크스페이스에 출력 파일(`graph.json`, `graphify-out/`)을 씁니다. 이 경로가 무시되지 않으면, 매번 쓸 때마다 Claude Code의 프롬프트 캐시가 무효화되어, 다음 턴에서 캐시 쓰기 속도로 전체 재업로드를 강제합니다. 이를 `.claudeignore`에 추가하세요:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## 전체 명령어 참조

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

> **커뮤니티 이름:** 에이전트(Claude Code, Gemini CLI) 내부에서는 에이전트 자체가 커뮤니티 이름을 짓습니다. 순수 CLI를 실행하면, `cluster-only`가 설정된 백엔드(내장 또는 사용자 지정 OpenAI 호환 제공자)로 자동 이름을 붙입니다 — `Community N`을 유지하려면 `--no-label`을 전달하거나, 필요에 따라 이름을 (재)생성하려면 `graphify label`을 실행하세요.

---

## 더 알아보기

- [작동 방식](docs/how-it-works.md) — 추출 파이프라인, 커뮤니티 감지, 신뢰도 점수 매기기, 벤치마크
- [ARCHITECTURE.md](ARCHITECTURE.md) — 모듈 분석, 언어 추가 방법
- [선택적 통합](docs/docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — graphify 뒤에 있는 아이디어, 처음부터 끝까지의 아키텍처에 관한 책

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com)는 graphify 위에 구축된 상시 작동 계층입니다 — 동일한 그래프 접근 방식을 전체 작업 컨텍스트에 적용합니다: 회의, 파일, 문서, 코드가 백그라운드에서 지속적으로 업데이트됩니다.

결코 완전히 재구성할 수 없는 수백 개의 대화와 문서에 걸쳐 작업이 이루어지는 사람들과 팀을 위해 만들어졌습니다.

**[graphify.com에서 대기 목록에 참여하세요](https://graphify.com).** 무료 체험판이 곧 시작됩니다.

---

<details>
<summary>기여</summary>

### 개발 환경 설정

이 프로젝트는 개발 워크플로에 [uv](https://docs.astral.sh/uv/)를 사용합니다. 한 번 설치한 다음:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

editable 설치 확인:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### 테스트 실행

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> macOS 참고: 테스트 스위트에는 `sample.f90`과 `sample.F90` 픽스처가 모두 포함되어 있습니다. 이것들은 대소문자를 구분하지 않는 HFS+ / APFS 파일 시스템에서 충돌합니다. 두 Fortran 변형을 동시에 테스트해야 한다면 Linux에서 또는 Docker 컨테이너에서 실행하세요.

### Git 워크플로

- 활발한 개발은 `v8` 브랜치에서 이루어집니다.
- 커밋 스타일: `fix: <description>` / `feat: <description>` / `docs: <description>`
- PR을 열기 전에 `uv run pytest tests/ -q`를 실행하고 통과하는지 확인하세요.
- 새로운 언어 추출기에 대해 `tests/fixtures/`에 픽스처 파일을, `tests/test_languages.py`에 테스트를 추가하세요.

### 기여할 수 있는 것

**작업 예제(worked examples)**가 가장 유용한 기여입니다. 실제 코퍼스에서 `/graphify`를 실행하고, 출력을 `worked/{slug}/`에 저장하고, 그래프가 무엇을 옳고 그르게 했는지 다루는 정직한 `review.md`를 작성한 다음, PR을 열어주세요.

**추출 버그** — 입력 파일, 캐시 항목(`graphify-out/cache/`), 그리고 무엇이 누락되었거나 잘못되었는지와 함께 이슈를 열어주세요.

모듈 책임과 언어 추가 방법에 대해서는 [ARCHITECTURE.md](ARCHITECTURE.md)를 참고하세요.

</details>
