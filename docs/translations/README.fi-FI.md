<p align="center">
  <img src="../logo-decouple.svg" width="420" height="64" alt="Graphify Decouple"/>
</p>

<p align="center">
  <b>Haara projektista <a href="https://github.com/Graphify-Labs/graphify">graphify</a>, joka lisää <code>graphify decouple</code> -toiminnon</b> — 0-LLM, riskipisteytetyt Extract-Class-ehdokkaat god objecteille, uudelleenvarmennettu todellista lähdekoodia vasten (ei vain kutsugraafia) ennen kuin mitään suositellaan. Katso <a href="#decouple-risk-scored-extract-class-candidates">Decouple: riskipisteytetyt Extract-Class-ehdokkaat</a> alla.
</p>

<div align="center">
<details><summary><b>Lue tämä muilla kielillä</b></summary>

🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇷 <a href="README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="README.fil-PH.md">Filipino</a> | 🇮🇱 <a href="README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <b>Varhainen pääsy graphify-alustaan on avoinna ennen julkista v1-julkaisua: <a href="https://app.graphify.com/login">app.graphify.com</a></b>
</p>

Kirjoita `/graphify` tekoälykoodausavustimeesi, ja se kartoittaa koko projektisi (koodin, dokumentit, PDF:t, kuvat, videot) **tietograafiksi**, jota voit **kysellä grepin sijaan** tiedostojen läpi.

- **Koodikartat ilmaiseksi, täysin paikallisesti.** Koodi jäsennetään tree-sitter AST:llä: deterministisesti, ilman LLM:ää, mikään ei poistu koneeltasi. (Dokumentit, PDF:t, kuvat ja video käyttävät avustimesi mallia tai konfiguroitua API-avainta semanttiseen läpikäyntiin.)
- **Jokainen reuna selitetään.** Jokainen yhteys on merkitty `EXTRACTED` (eksplisiittinen lähteessä) tai `INFERRED` (graphifyn päättelemä), joten näet mikä luettiin suoraan ja mikä pääteltiin.
- **Ei vektori-indeksi.** Ei embeddings-vektoreita, ei vector storea: oikea graafi, jota kuljet läpi. Esitä kysymys, jäljitä polku kahden asian välillä tai selitä yksi käsite.

> Haluatko tämän aina päällä, päivittyvän taustalla koodisi, dokumenttiesi ja kokousten yli sen sijaan että vain pyynnöstä? Sitä rakennamme **[graphify.com](https://graphify.com)**-palvelussa, ja varhainen pääsy on nyt avoinna osoitteessa **[app.graphify.com](https://app.graphify.com/login)**.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="graphify's interactive graph.html showing the FastAPI codebase as a force-directed knowledge graph with a legend of detected communities" width="900">
</p>
<p align="center">
  <em>graphifyn kartoittama FastAPI-koodikanta. Jokainen solmu on käsite, värit ovat havaittuja yhteisöjä, ja koko kokonaisuus on klikattavissa graph.html:ssä.</em>
</p>

**Aloita** (30 sekuntia):

```bash
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```

Sitten, tekoälyavustimessasi:

```
/graphify .
```

Siinä kaikki. Saat **kolme tiedostoa**:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

**Toimii** Claude Codessa, Cursorissa, Codexissa, Gemini CLI:ssä, GitHub Copilotissa ja 15+ muussa — [valitse alustasi](#install).

---

## Näe se toiminnassa

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/demo-path.svg" alt="graphify path query: a terminal asks for the shortest path between FastAPI and ModelField, and the answer lights up hop by hop across the knowledge graph" width="900">
</p>

Kun graafi on rakennettu, kyselet sitä tiedostojen lukemisen sijaan. Todellinen tuloste, graphify ajettuna yllä näytettyyn FastAPI-koodikantaan:

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

Jokainen reuna kantaa **luottamusmerkinnän** (`EXTRACTED` = eksplisiittinen lähteessä, `INFERRED` = pääteltävissä resoluutiolla), joten näet mikä luettiin suoraan ja mikä pääteltiin. `graphify query "<question>"` palauttaa rajatun alagraafin luonnollisen kielen kysymykselle, ja `graphify path A B` jäljittää miten kaksi asiaa liittyvät toisiinsa.

---

## Decouple: riskipisteytetyt Extract-Class-ehdokkaat

<p align="center">
  <img src="../decouple-demo.svg" alt="graphify decouple: MainWindow god node splitting into risk-scored candidate classes, with a shared-state warning between two of them" width="900">
</p>

<p align="center">
  <img src="../decouple-screenshot.svg" alt="DECOUPLE.html: MainWindow's 5 proposed classes, Node Info panel open on Main Window Axis and Range Controls showing a 0.608 state overlap with Main Window Controller Core" width="900">
</p>
<p align="center">
  <em>DECOUPLE.html todellisella ajolla — ehdotettua luokkaa klikkaamalla näet tarkalleen, minkä toisen luokan kanssa se jakaa tilaa, ja mitä täsmälleen jaetaan.</em>
</p>

Sama sivu renderöi myös itse jaon. **Preview decoupled view** -kytkin vaihtaa god-luokan omat metodit ehdotettuihin luokkiin ja reitittää reunat uudelleen paikan päällä — kytkentämuutoksen, ei uudelleenpiirrettyä kaaviota:

| Ennen — god-luokka tänään | Jälkeen — Preview decoupled view |
| --- | --- |
| <img src="../decouple-before.png" alt="DECOUPLE.html before the toggle: a single MainWindow hub node with its own methods fanned out around it" width="440"> | <img src="../decouple-after.png" alt="DECOUPLE.html after the toggle: the same node reduced to 5 diamond-shaped proposed classes, green dashed edges showing which methods were extracted into each, red edges showing shared instance state between two of them" width="440"> |
| Yksi solmu, jolla on 47 omaa metodia, joista jokainen on saavutettavissa vain luokan kautta. | Ehdotetut luokat. Vihreä katkoviiva = mitä poimittiin mihinkin; punainen = instanssitila, jota kaksi niistä yhä jakaa, mikä on täsmälleen se, mikä ratkaisee `split`-vai-`keep_as_is`-päätöksen. Vain riskikynnyksen ylittävät ehdokkaat piirretään — tässä 5/6, minkä vuoksi yhdellä metodilla ei ole timanttia, johon laskeutua. |

`graphify decouple` löytää god objectit ja kertoo, kannattaako niiden jakaminen todella — ei vain sitä, että ne ovat suuria.

Epäonnistumisen malli, jonka tämä on suunniteltu havaitsemaan: luokka, jossa on 47 metodia ja jonka kutsugraafiklusterointi jakaa mielellään 5 siistiltä näyttävään ryhmään, joista kaikki edelleen lukevat ja kirjoittavat täsmälleen samaa `self._chart_style` / `self._crosshair` -instanssitilaa alla. Jos toimitat tuon jaon, et ole eriyttänyt mitään — olet vain siirtänyt metodeja uusiin tiedostoihin, joita ei edelleenkään voi testata, muuttaa tai ymmärtää itsenäisesti, koska ne kaikki tarvitsevat edelleen saman jaetun tilan takaisin välitettynä. Työkalu, joka katsoo vain kutsugraafia, ei voi nähdä tätä lainkaan; sen on palattava todelliseen lähteeseen.

**Kaksi tarkistusta, molemmat ilman LLM:ää, molemmat deterministisiä:**

1. **Onko tämä edes God Object?** Solmu, jolla on korkea aste, voi olla todellinen God Object (monta OMAA metodia, levittäytyneenä toisiinsa liittymättömiin vastuisiin — Extract Class pätee) tai ylireferoitu keskittymä/datamalli (vähän omia metodeja, enimmäkseen *saapuvia* viittauksia — sen rungon jakaminen ei tee mitään; korjaus on sen rajapinnan kaventaminen, ei luokan erottaminen). `classify_god_node` erottaa nämä `member_ratio`-arvolla, ei raa'alla asteella — ero, joka estää `TraceSource`-luokkaa (84 reunaa, mutta vain 6 omaa metodia) saamasta väärää jakoehdotusta, jonka `MainWindow` (88 reunaa, 47 omaa metodia) oikeutetusti saa.
2. **Vähentäisikö jako todella kytkentää?** `risk_before` (god-solmun nykyinen koko/kytkentä/pirstoutuminen) verrataan arvoon `risk_after` — UUTEEN riskiin, jonka itse jako toisi mukanaan: ryhmien väliset kutsut, jotka olivat näkymättömiä luokan sisäisiä reunoja ja joista tulee eksplisiittisiä luokkien välisiä riippuvuuksia, kutsujat, joiden pitäisi nyt olla riippuvaisia useammasta kuin yhdestä uudesta luokasta, ja — tarkistus, jota kutsugraafi ei rakenteellisesti voi tehdä — kuinka paljon `self`/`this`-instanssitilaa (luvut, kirjoitukset ja jaetut apumetodikutsut, painotettuna erikseen: jaettu **kirjoitus** pisteytetään korkeammalle kuin jaettu luku) ehdotetuilla ryhmillä on todella yhteistä. Tämä jäsentää god-solmun oman lähdetiedoston uudelleen suoraan tree-sitterillä; se ei nojaa graphifyn omaan poimittuun graafiin, joka ei koskaan tallenna kenttätason pääsyä millekään kielelle. Vain kun `risk_after` alittaa kynnyksen suhteessa arvoon `risk_before`, suunnitelma suosittelee `split`-toimintoa — muuten se on `marginal` tai `keep_as_is`, ja lannistettu ehdokas raportoidaan numerona, ei koskaan piirrettynä muotona, jota sinun täytyy arvailla silmämääräisesti.

```bash
graphify decouple                              # analyze graphify-out/graph.json
graphify decouple --project-root .             # + the state-sharing check (recommended)
graphify decouple --top 20 --min-group-size 2  # more god nodes, smaller candidate groups
graphify decouple --no-state-check             # call-graph-only scoring (skips the source re-parse)
graphify decouple --json                       # print decouple.json to stdout
```

Tuottaa kolme tiedostoa `graph.json`:n viereen:

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

**Kielikattavuus tilanjakotarkistukselle** (yllä oleva pelkkä kutsugraafiluokittelu toimii jokaiselle kielelle, jonka graphify poimii; tämä taulukko koskee nimenomaan lähdekoodin uudelleenjäsennystä, joka varmentaa `self`/`this`-tilan päällekkäisyyden):

| Kieli | Tuettu | Huomiot |
|---|---|---|
| Python | ✅ | `self.x` |
| JavaScript / TypeScript | ✅ | `this.x` |
| Java | ✅ | `this.foo()` on oma AST-solmunsa, ei kääritty kenttäpääsy — käsitelty eksplisiittisesti |
| C# | ✅ | |
| Rust | ✅ | `self.x` `impl`-lohkojen kautta |
| Ruby | ✅ | `@x` (hallitseva idiomi) + `self.foo`-kutsut |
| PHP | ✅ | `$this->x` |
| Swift | ✅ | `self.x` |
| Kotlin | ✅ | `this.x` |
| C++ | ✅ | `this->x` |
| Go | ✅ | vastaanottajan resoluutio per metodi — Go:lla ei ole `self`/`this`-avainsanaa, joten vastaanottajan nimi (`f` kohdassa `func (f *Foo) M()`) ratkaistaan uudelleen jokaiselle metodille |
| C | ❌ | struct-osoitinparametrilla ei ole syntaktista merkkiä, joka erottaisi sen mistä tahansa muusta parametrista — ei luotettavaa signaalia ilman täyttä tyyppipäättelyä |

God-solmu ei-tuetulla kielellä, tai sellainen jonka lähdettä ei voi lukea, merkitään `state_analysis: "skipped"` — luokittelu ja kutsugraafipisteet toimivat silti, mutta suositus nojaa vain kutsugraafiin sen sijaan että hiljaa oletettaisiin tilatarkistuksen läpäisseen.

---

## Mitä se tekee

Mitä saat suoraan pakkauksesta:

| Ominaisuus | Mitä saat |
|---|---|
| **God-solmut** | Eniten yhdistetyt käsitteet, joten näet mistä kaikki virtaa läpi |
| **Yhteisöt** | Graafi jaettuna alijärjestelmiin (Leiden), ilman LLM:ää tuotetuin nimikkein |
| **Tiedostojen väliset linkit** | `calls` / `imports` / `inherits` / `mixes_in` ratkaistu ~40 kielellä tree-sitter AST:n kautta |
| **Kysely, polku, selitys** | Esitä kysymys, jäljitä polku kahden asian välillä, tai selitä yksi käsite, kaikki `graph.json`:aa vasten |
| **Perustelut + dokumenttiviitteet** | `# NOTE:` / `# WHY:` -kommentit ja ADR/RFC-viittaukset muuttuvat ensiluokan solmuiksi, jotka on linkitetty koodiin |
| **Koodin ulkopuolella** | Dokumentit, PDF:t, kuvat ja video/audio kartoittuvat kaikki samaan graafiin |
| **Paikallinen ensin** | Koodi jäsennetään paikallisesti tree-sitterillä (ei LLM:ää, mikään ei poistu koneeltasi); vain semanttinen läpikäynti dokumenteista/mediasta kutsuu backendia, ja vain jos konfiguroit sellaisen |

---

## Vertailut (Benchmarks)

| Vertailu | Mittari | graphify | Kenttä |
|---|---|---|---|
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | QA-tarkkuus | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | QA-tarkkuus | **76%** | tasan tiheän RAG:n kanssa |
| Graafin rakennus | LLM-krediitit | **0** | tokenia kohden useimmilla järjestelmillä |

Jokainen järjestelmä ajettiin samalla valjaalla, samalla mallilla ja budjeteilla, pisteytettynä tuomarilla, joka oli sokkovalidoitu toista tuomaria vasten (90.6% yhteisymmärrys, Cohenin kappa 0.81). Täydet järjestelmäkohtaiset taulukot, koodiälyllisyys-tulos ja toistokomennot: **[BENCHMARKS.md](./BENCHMARKS.md)**.

---

## Vaatimukset

| Vaatimus | Minimi | Tarkistus | Asennus |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(suositeltu)* | mikä tahansa | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(vaihtoehto)* | mikä tahansa | `pipx --version` | `pip install pipx` |

**macOS pika-asennus (Homebrew):**
```bash
brew install python@3.12 uv
```

**Windows pika-asennus:**
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

## Asennus

> **Virallinen paketti:** PyPI-paketti on `graphifyy` (tupla-y). Muut `graphify*`-paketit PyPI:ssä eivät ole liitoksissa. CLI-komento on edelleen `graphify`.

**Vaihe 1 — asenna paketti:**

```bash
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy  # may need PATH setup — see note below
```

**Vaihe 2 — rekisteröi taito tekoälyavustimeesi:**

```bash
graphify install
```

Siinä kaikki. Avaa tekoälyavustimesi ja kirjoita `/graphify .`

Asentaaksesi avustintaidon nykyiseen repositorioon käyttäjäprofiilisi sijaan, lisää `--project`:

```bash
graphify install --project
graphify install --project --platform codex
```

Projektikohtaiset asennukset kirjoittavat nykyisen hakemiston alle, esimerkiksi `.claude/skills/graphify/SKILL.md` tai `.agents/skills/graphify/SKILL.md` (sekä `references/`-lisäosa, jonka taito lataa tarvittaessa), ja tulostavat `git add`-vihjeen tiedostoille, jotka voidaan committaa. Alustakohtaiset komennot, jotka tukevat projektikohtaisia asennuksia, hyväksyvät saman lipun, esimerkiksi `graphify claude install --project` tai `graphify codex install --project`.

> **PowerShell-huomautus:** Käytä `graphify .` etkä `/graphify .` — alkukauttaviiva on polkueroti PowerShellissä.

> **`graphify: command not found`?** `uv tool install` / `pipx install` laittavat `graphify`-komennon työkalujensa bin-hakemistoon (`~/.local/bin`). Jos kuorasi ei löydä sitä heti asennuksen jälkeen — yleistä tuoreella macOS + zsh -asennuksella — se hakemisto ei ole vielä `PATH`-muuttujassasi: aja `uv tool update-shell` (tai `pipx ensurepath`), avaa sitten uusi pääte. Pelkällä `pip`:llä, lisää `~/.local/bin` (Linux) tai `~/Library/Python/3.x/bin` (Mac) PATH-muuttujaasi, tai aja `python -m graphify`.

> **Ajatko `uvx`/`uv tool run` -komennolla asentamisen sijaan?** Nimeä paketti, ei komentoa: `uvx --from graphifyy graphify install`. Pelkkä `uvx graphify …` epäonnistuu (`No solution found … no versions of graphify`), koska `uv tool run` lukee ensimmäisen sanan *pakettina*, ja paketti on `graphifyy` — `graphify`-komento asuu sen sisällä.

> **Vältä `pip install`-komentoa Macilla/Windowsilla** jos mahdollista. Taito ratkaisee Pythonin ajonaikaisesti tiedostosta `graphify-out/.graphify_python`; jos se osoittaa eri ympäristöön kuin mihin `pip` asensi paketin, saat virheen `ModuleNotFoundError: No module named 'graphify'`. `uv tool install` ja `pipx install` eristävät paketin omaan ympäristöönsä ja välttävät tämän kokonaan.

> **Git-hookit ja uv tool / pipx:** `graphify hook install` upottaa nykyisen tulkin polun suoraan hook-skripteihin asennushetkellä, joten post-commit-hook laukeaa oikein jopa graafisissa git-asiakasohjelmissa ja CI-ajajissa, joissa `~/.local/bin` ei ole PATH-muuttujassa. Jos asennat uudelleen tai päivität graphifyn, aja `graphify hook install` uudelleen upotetun polun päivittämiseksi.

> **Tiukka tila (Claude Code):** `graphify install --project --strict` saa avustimen todella käyttämään graafia. Oletusasennus *kannustaa* ajamaan `graphify query` ennen tiedostojen lukemista; tiukka tila *estää* istunnon ensimmäisen raa'an lähdeluvun ja ohjaa sen graafiin, palaten sitten kannustukseen (joten se laukeaa korkeintaan kerran istuntoa kohden eikä koskaan jää jumiin). Vaihda ajonaikaisesti `GRAPHIFY_HOOK_STRICT=1`/`0`:lla; oletusasennus pysyy muuttumattomana (pehmeä kannustus).

<details>
<summary><b>Valitse alustasi</b> (20+ avustinta, klikkaa laajentaaksesi)</summary>

| Alusta | Asennuskomento |
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

Codex-käyttäjät tarvitsevat myös `multi_agent = true` -asetuksen `[features]`-osion alle tiedostossa `~/.codex/config.toml` rinnakkaista poimintaa varten. CodeBuddy käyttää samaa Agent tool- ja PreToolUse hook -mekanismia kuin Claude Code. Factory Droid käyttää `Task`-työkalua rinnakkaiseen alaagenttien jakeluun. OpenClaw ja Aider käyttävät peräkkäistä poimintaa (rinnakkaisagenttien tuki on näillä alustoilla vielä varhaisessa vaiheessa). Trae käyttää Agent tool -työkalua rinnakkaiseen alaagenttien jakeluun eikä **tue** `PreToolUse`-hookkeja, joten AGENTS.md on aina päällä oleva mekanismi.

`--platform agents` (alias `--platform skills`) kohdistuu yleisiin, kehysriippumattomiin [Agent-Skills](https://github.com/anthropics/skills)-sijainteihin: spesifikaation käyttäjäkohtainen globaali `~/.agents/skills/` (jonka `npx skills` ja spesifikaation mukaiset kehykset lukevat) globaalille asennukselle, ja `./.agents/skills/` projektiasennukselle (`--project`). Pelkkä `graphify install` pysyy suunnitellusti yhden alustan (Claude Code) ratkaisuna — käytä nimettyä `agents`-alustaa, kun haluat taidon olevan minkä tahansa `.agents/skills`-hakemistoa lukevan kehyksen löydettävissä.

> Codex käyttää `$graphify`-komentoa `/graphify`-komennon sijaan.

</details>

<details>
<summary><b>Valinnaiset lisäosat</b> (asenna vain se, mitä tarvitset)</summary>

| Lisäosa | Mitä se lisää | Asennus |
|---|---|---|
| `pdf` | PDF-poiminta | `uv tool install "graphifyy[pdf]"` |
| `office` | `.docx`- ja `.xlsx`-tuki | `uv tool install "graphifyy[office]"` |
| `google` | Google Sheets -renderöinti | `uv tool install "graphifyy[google]"` |
| `video` | Video-/äänitranskriptio (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | MCP stdio -palvelin | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Neo4j push -tuki | `uv tool install "graphifyy[neo4j]"` |
| `falkordb` | FalkorDB push -tuki | `uv tool install "graphifyy[falkordb]"` |
| `svg` | SVG-graafivienti | `uv tool install "graphifyy[svg]"` |
| `leiden` | Leiden-yhteisöntunnistus (vain Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Paikallinen Ollama-päättely | `uv tool install "graphifyy[ollama]"` |
| `openai` | OpenAI / OpenAI-yhteensopivat API:t | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic Claude API (`--backend claude`, käyttää `ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (käyttää IAM:ää, ei API-avainta) | `uv tool install "graphifyy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, käyttää `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "graphifyy[openai]"` |
| `sql` | SQL-skeemapoiminta | `uv tool install "graphifyy[sql]"` |
| `postgres` | Live PostgreSQL-introspektio (`--postgres DSN`) | `uv tool install "graphifyy[postgres]"` |
| `dm` | BYOND DreamMaker `.dm`/`.dme` AST-poiminta (voi tarvita C-kääntäjän + `python3-dev`, jos wheel ei sovi alustallesi) | `uv tool install "graphifyy[dm]"` |
| `terraform` | Terraform / HCL `.tf`/`.tfvars`/`.hcl` AST-poiminta | `uv tool install "graphifyy[terraform]"` |
| `pascal` | Pascal / Delphi `.pas`/`.dpr`/`.dpk`/`.inc` AST-poiminta (tarkemmat `calls`/`inherits`-reunat; palaa regex-poimijaan kun puuttuu) | `uv tool install "graphifyy[pascal]"` |
| `chinese` | Kiinankielisten kyselyjen segmentointi (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | Kaikki yllä oleva | `uv tool install "graphifyy[all]"` |

</details>

---

## Saa avustimesi käyttämään graafia aina

Aja tämä kerran projektissasi graafin rakentamisen jälkeen:

| Alusta | Komento |
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

Tämä kirjoittaa pienen konfiguraatiotiedoston, joka kertoo avustimellesi konsultoida tietograafia koodikantaan liittyvissä kysymyksissä, suosien rajattuja kyselyjä kuten `graphify query "<question>"` sen sijaan että lukisi koko raportin tai käyttäisi grepiä raakoihin tiedostoihin.

- **Hook-alustat** (Claude Code, Gemini CLI): hook laukeaa automaattisesti ennen hakutyylisiä työkalukutsuja (ja Claude Codessa ennen lähdetiedostojen lukemista yksitellen Read/Glob-työkaluilla) ja kannustaa avustintasi graafipolulle.
- **Ohjetiedostoalustat** (Codex, OpenCode, Cursor, jne.): pysyvät ohjetiedostot (`AGENTS.md`, `.cursor/rules/`, jne.) tarjoavat saman kysely-ensin-ohjeistuksen.

`GRAPH_REPORT.md` on edelleen käytettävissä laajaan arkkitehtuurikatsaukseen.

**CodeBuddy** tekee samat kaksi asiaa kuin Claude Code: kirjoittaa `CODEBUDDY.md`-osion, joka kertoo CodeBuddylle lukea `graphify-out/GRAPH_REPORT.md` ennen arkkitehtuurikysymyksiin vastaamista, ja asentaa `PreToolUse`-hookit (`.codebuddy/settings.json`), jotka laukeavat ennen Bash-hakukomentoja ja tiedostolukuja, kannustaen `graphify query`-komennon suuntaan.

**Codex** kirjoittaa `AGENTS.md`-tiedostoon, joka todella kantaa aina päällä olevaa graafiohjeistusta tällä alustalla. `graphify codex install` rekisteröi myös `PreToolUse`-hookin tiedostossa `.codex/hooks.json` (`graphify hook-check`), mutta tuo merkintä on tarkoituksella **no-op**: Codex Desktop hylkää `hookSpecificOutput.additionalContext`-arvon `PreToolUse`-tapahtumassa, joten kannustuksen lähettäminen siellä rikkoisi Bash-työkalukutsut. Toisin kuin Claude Codessa, jossa hook (`graphify hook-guard`) tekee kannustuksen, Codexissa hook laukeaa ja tarkoituksella ei tee mitään, ja `AGENTS.md` on aina päällä oleva mekanismi.

**Kilo Code** asentaa Graphify-taidon polkuun `~/.config/kilo/skills/graphify/SKILL.md` ja natiivin `/graphify`-komennon polkuun `~/.config/kilo/command/graphify.md`. `graphify kilo install` kirjoittaa myös `AGENTS.md`-tiedoston sekä natiivin `tool.execute.before`-pluginin (`.kilo/plugins/graphify.js` + `.kilo/kilo.json`- tai `.kilo/kilo.jsonc`-rekisteröinti), joten Kilo saa saman aina päällä olevan graafimuistutuskäytöksen natiivin `.kilo`-konfiguraation kautta.

**Cursor** kirjoittaa `.cursor/rules/graphify.mdc`-tiedoston `alwaysApply: true`-asetuksella, joten Cursor sisällyttää sen jokaiseen keskusteluun automaattisesti, ilman hookia.

Poistaaksesi graphifyn kaikilta alustoilta kerralla: `graphify uninstall` (lisää `--purge` poistaaksesi myös `graphify-out/`). Tai käytä alustakohtaista komentoa (esim. `graphify claude uninstall`).

---

## Mitä raportissa on

- **God-solmut** — projektisi eniten yhdistetyt käsitteet. Kaikki virtaa niiden kautta.
- **Yllättävät yhteydet** — linkkejä asioiden välillä, jotka elävät eri tiedostoissa tai moduuleissa. Järjestetty sen mukaan, kuinka odottamattomia ne ovat.
- **"Miksi"** — koodin sisäiset kommentit (`# NOTE:`, `# WHY:`, `# HACK:`), docstringit ja suunnitteluperustelut dokumenteista poimitaan erillisiksi solmuiksi, jotka on linkitetty koodiin, jota ne selittävät.
- **Ehdotetut kysymykset** — 4–5 kysymystä, joihin graafi on ainutlaatuisen hyvässä asemassa vastata.
- **Luottamusmerkinnät** — jokainen pääteltävä suhde on merkitty `EXTRACTED`, `INFERRED`, tai `AMBIGUOUS`. Tiedät aina, mikä löydettiin vs. mikä arvattiin.

---

## Mitkä tiedostot se käsittelee

| Tyyppi | Tiedostopäätteet |
|------|-----------|
| Koodi (36 tree-sitter-kielioppia) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .rb .cs .kt .kts .scala .php .swift .lua .luau .toc .zig .ps1 .psm1 .psd1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme` vaatii `uv tool install graphifyy[dm]`; `.mts`/`.cts` käyttävät uudelleen TypeScript-kielioppia, `.cc`/`.cxx` ja CUDA `.cu`/`.cuh` ja Metal `.metal` käyttävät uudelleen C++-kielioppia) |
| Salesforce Apex | `.cls .trigger` (regex-pohjainen; luokat, rajapinnat, enumit, metodit, triggerit, SOQL/DML-reunat) |
| Terraform / HCL | `.tf .tfvars .hcl` (vaatii `uv tool install graphifyy[terraform]`) |
| MCP-konfiguraatiot | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — poimii palvelinsolmut, pakettiviittaukset, ympäristömuuttujavaatimukset |
| Pakettimanifestit | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — yksi kanoninen pakettisolmu per paketti (nimen mukaan) plus `depends_on`-reunat, joten monista manifesteista viitattu paketti on yksi keskittymä |
| Dokumentit | `.md .mdx .qmd .html .txt .rst .yaml .yml` (markdown `[text](./other.md)`-linkit ja `[[wikilinks]]` muuttuvat `references`-reunoiksi dokumenttien välillä) |
| Office | `.docx .xlsx` (vaatii `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (opt-in; vaatii `gws`-todennuksen ja `--google-workspace`-lipun; Sheets vaatii `uv tool install graphifyy[google]`) |
| PDF:t | `.pdf` |
| Kuvat | `.png .jpg .webp .gif` |
| Video / Audio | `.mp4 .mov .mp3 .wav` ja lisää (vaatii `uv tool install graphifyy[video]`) |
| YouTube / URL:t | mikä tahansa video-URL (vaatii `uv tool install graphifyy[video]`) |

Koodi poimitaan **paikallisesti ilman API-kutsuja** (AST tree-sitterin kautta). Kaikki muu kulkee tekoälyavustimesi mallin API:n kautta.

Google Drive for desktopin `.gdoc`-, `.gsheet`- ja `.gslides`-tiedostot ovat pikakuvakeosoittimia, ei dokumenttisisältöä. Sisällyttääksesi natiivit Google Docs-, Sheets- ja Slides-dokumentit headless-poimintaan, asenna ja todenna [`gws` CLI](https://github.com/googleworkspace/cli), aja sitten:

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

Voit myös asettaa `GRAPHIFY_GOOGLE_WORKSPACE=1`. Graphify vie pikakuvakkeet polkuun `graphify-out/converted/` Markdown-liitetiedostoina, poimien sitten nuo tiedostot.

---

## Yleiset komennot

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

Katso [Decouple: riskipisteytetyt Extract-Class-ehdokkaat](#decouple-risk-scored-extract-class-candidates) yllä tai [täydellinen komento-viite](#full-command-reference) alla.

---

## Tiedostojen ohittaminen

Luo `.graphifyignore` projektisi juureen — sama syntaksi kuin `.gitignore`, mukaan lukien `!`-kieltäminen.

**`.gitignore` huomioidaan automaattisesti.** graphify lukee `.gitignore`:n jokaisessa hakemistossa. Jos `.graphifyignore` on myös läsnä, molemmat **yhdistetään** — `.graphifyignore`-kuviot arvioidaan viimeisenä, joten ne voittavat ristiriidoissa (mukaan lukien `!`-kiellot). `.graphifyignore`:n lisääminen vain sulkee pois enemmän; se ei koskaan sisällytä uudelleen tiedostoa, jonka `.gitignore` on jo sulkenut pois. Alihakemiston laajuus toimii samalla tavalla kuin git:ssä — ohitustiedosto vaikuttaa vain omaan alipuuhunsa.

Anna `--no-gitignore`-lippu komennolle `graphify extract`, kun git-ohitettu generoitu tai transpiloitu koodi kuuluu graafiin. Tämä poistaa käytöstä `.gitignore`:n ja `.git/info/exclude`:n; `.graphifyignore` pätee edelleen.

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

## Tiimin asetukset

`graphify-out/` on tarkoitus committaa git:iin, jotta jokainen tiimissä aloittaa kartalla.

**Suositellut `.gitignore`-lisäykset:**
```
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` on nyt siirrettävissä — avaimet tallennetaan suhteellisina polkuina ja ankkuroidaan uudelleen latauksen yhteydessä, joten sen committaaminen on turvallista ja välttää täyden uudelleenrakennuksen ensimmäisellä checkoutilla.

**Työnkulku:**
1. Yksi henkilö ajaa `/graphify .` ja committaa `graphify-out/`:n.
2. Kaikki pullaavat — heidän avustimensa lukee graafin heti.
3. Aja `graphify hook install` automaattista uudelleenrakennusta varten jokaisen commitin jälkeen (vain AST, ei API-kustannusta). Tämä myös asettaa git merge -ajurin, joten `graph.json`:iin ei koskaan jää ristiriitamerkintöjä — kaksi kehittäjää, jotka committaavat rinnakkain, saavat graafinsa automaattisesti union-yhdistettyinä.
4. Kun dokumentit tai artikkelit muuttuvat, aja `/graphify --update` päivittääksesi nuo solmut.

---

## Graafin suora käyttö

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

MCP-palvelin antaa avustimellesi jäsennellyn pääsyn: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Jaettu HTTP-palvelin

`--transport stdio` (oletus) käynnistää yhden paikallisen palvelimen per kehittäjä. `--transport http` tarjoilee samat työkalut MCP Streamable HTTP -siirron yli, joten yksi jaettu prosessi voi tarjoilla graafin koko tiimille — asiakkaat osoittavat IDE:nsä MCP-konfiguraation osoitteeseen `http://<host>:8080/mcp` sen sijaan että ajaisivat graphifyä paikallisesti.

| Lippu | Oletus | Tarkoitus |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Siirtotapa, jolla tarjoillaan |
| `--host` | `127.0.0.1` | HTTP-sidontaisäntä (käytä `0.0.0.0` altistaaksesi localhostin ulkopuolelle) |
| `--port` | `8080` | HTTP-sidontaportti |
| `--api-key` | env `GRAPHIFY_API_KEY` | Vaatii `Authorization: Bearer <key>` (tai `X-API-Key`) |
| `--path` | `/mcp` | HTTP-liitospolku |
| `--json-response` | pois | Palauttaa pelkän JSON:n SSE-virtojen sijaan |
| `--stateless` | pois | Ei tilaa per istunto (kuormantasattuihin/CI-käyttöönottoihin) |
| `--session-timeout` | `3600` | Poistaa passiiviset tilalliset istunnot N sekunnin jälkeen (`0` poistaa käytöstä) |

Oletus `127.0.0.1`-sidonta on vain loopback. Aseta `--host 0.0.0.0` **ja** `--api-key` yhdessä altistaessasi jaetulla isännällä. Aja se kontissa:

```bash
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **WSL / Linux -huomautus:** Ubuntu toimittaa `python3`:n, ei `python`:ia. Käytä venv:iä ristiriitojen välttämiseksi:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## Ympäristömuuttujat

Näitä tarvitaan vain **headless-/CI-poimintaan** (`graphify extract`). Kun ajetaan `/graphify`-taidon kautta IDE:si sisällä, mallin API tulee IDE-istunnostasi — ylimääräisiä avaimia ei tarvita.

| Muuttuja | Käyttötarkoitus | Milloin vaaditaan |
|---|---|---|
| `ANTHROPIC_API_KEY` | Claude (Anthropic) -backend | `--backend claude` |
| `ANTHROPIC_BASE_URL` | Anthropic-yhteensopiva päätepiste-URL (LiteLLM-proxy, yhdyskäytävät, ...) | `--backend claude` (oletus: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Mallin nimi Claude-backendille — mukautetuille päätepisteille, käytä mallin nimeä/aliasta, jonka palvelimesi altistaa | `--backend claude` (oletus: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` tai `GOOGLE_API_KEY` | Google Gemini -backend | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI tai OpenAI-yhteensopivat API:t | `--backend openai` (paikalliset palvelimet hyväksyvät minkä tahansa ei-tyhjän arvon) |
| `OPENAI_BASE_URL` | OpenAI-yhteensopivan palvelimen URL (llama.cpp, vLLM, LM Studio, ...) | `--backend openai` (oletus: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | Mallin nimi OpenAI-backendille — itse isännöidyille palvelimille, käytä mallin nimeä/aliasta, jonka palvelimesi altistaa (tarkista sen `/v1/models`-päätepiste), esim. `LFM2.5-8B-A1B-UD-Q4_K_XL` llama.cpp:lle | `--backend openai` (oletus: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | DeepSeek-backend | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Kimi Code -backend | `--backend kimi` |
| `OLLAMA_BASE_URL` | Paikallinen Ollama-päättely-URL | `--backend ollama` (oletus: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Ollama-mallin nimi | `--backend ollama` (oletus: automaattitunnistus) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Ohittaa Ollaman KV-cache-ikkunan koon | valinnainen — automaattinen koko oletuksena |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Minuutteja, joina Ollama-malli pidetään ladattuna | valinnainen — aseta `0` purkaaksesi latauksen jokaisen palan jälkeen |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI Service -backend | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | Azure-resurssin päätepiste-URL | `--backend azure` (vaaditaan API-avaimen ohella) |
| `AZURE_OPENAI_API_VERSION` | Azure API-version ohitus | valinnainen — oletus `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` tai `GRAPHIFY_AZURE_MODEL` | Azure-käyttöönoton nimi | valinnainen — oletus `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — vakio valtuustietoketju | `--backend bedrock` (ei API-avainta, käyttää IAM:ää) |
| `GRAPHIFY_MAX_WORKERS` | AST-rinnakkaisuuden säiemäärä | valinnainen — myös `--max-workers`-lippu |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Nosta tulostekattoa tiheille korpuksille | valinnainen — esim. `32768` suurille tiedostoille |
| `GRAPHIFY_API_TIMEOUT` | Aikakatkaisu kutsua kohden sekunneissa HTTP-, claude-cli-, Anthropic SDK- ja Bedrock-backendeille (oletus: 600) | valinnainen — myös `--api-timeout`-lippu |
| `GRAPHIFY_MAX_RETRIES` | Kuinka monta kertaa yritetään uudelleen nopeusrajoitettua (429) pyyntöä ennen luovuttamista (oletus: 6; kunnioittaa `Retry-After`:ia) | valinnainen — nosta tiukoille organisaatiokohtaisille rajoille (esim. kimi); `0` poistaa käytöstä |
| `GRAPHIFY_FORCE` | Pakota graafin uudelleenrakennus vaikka solmuja olisi vähemmän | valinnainen — myös `--force`-lippu |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Ota automaattisesti käyttöön Google Workspace -vienti | valinnainen — aseta arvoon `1` |
| `GRAPHIFY_TRIAGE_BACKEND` | Backend komennolle `graphify prs --triage` | valinnainen — automaattitunnistettu saatavilla olevista avaimista |
| `GRAPHIFY_TRIAGE_MODEL` | Mallin ohitus triagelle | valinnainen — esim. `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG_ENABLE` | Aseta arvoon `1` ottaaksesi käyttöön paikallisen kyselylokin polussa `~/.cache/graphify-queries.log` (tallentaa jokaisen query/path/explain-kysymyksen + korpuksen). Oletuksena pois — mitään ei kirjoiteta ellet liity mukaan (#1797) | valinnainen |
| `GRAPHIFY_QUERY_LOG` | Ottaa kyselylokin käyttöön ja kirjoittaa sen tähän polkuun oletuksen sijaan | valinnainen — pois ellei tätä tai `_ENABLE`:ä ole asetettu |
| `GRAPHIFY_QUERY_LOG_DISABLE` | Aseta arvoon `1` pakottaaksesi kyselylokin pois päältä (voittaa enable-muuttujat) | valinnainen |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | Kun loki on käytössä, tallentaa myös täydet alagraafivastaukset (oletuksena pois) | valinnainen |
| `GRAPHIFY_MAX_GRAPH_BYTES` | Ohittaa graph.json:n 512 MiB kokorajan — esim. `700MB`, `2GB`, tai pelkät tavut | valinnainen — hyödyllinen hyvin suurille korpuksille |
| `GRAPHIFY_MAX_CONTEXTS` | Suurin määrä ei-oletusprojektigraafeja, jotka yksi monen projektin MCP-palvelin säilyttää | valinnainen — oletus: `8`; virheelliset arvot käyttävät `8`:aa, ja arvon `1` alle jäävät käyttävät `1`:tä |
| `GRAPHIFY_LLM_TEMPERATURE` | Ohittaa LLM-lämpötilan semanttiselle poiminnalle — esim. `0.7`, tai `none` jättääksesi pois | valinnainen — automaattisesti jätetty pois o1/o3/o4/gpt-5-päättelymalleille |

---

## Yksityisyys

- **Koodi­tiedostot** — käsitellään paikallisesti tree-sitterin kautta. Mikään ei poistu koneeltasi. Pelkkä koodikorpus ei vaadi API-avainta — `graphify extract` toimii täysin offline. Sekakäyttöisessä repossa, lisää `--code-only` indeksoidaksesi vain koodin ja ohittaaksesi dokumentit/PDF:t/kuvat, jotka muuten vaatisivat LLM:n.
- **Video / ääni** — transkriboidaan paikallisesti faster-whisperillä. Mikään ei poistu koneeltasi.
- **Dokumentit, PDF:t, kuvat** — lähetetään tekoälyavustimellesi semanttista poimintaa varten (`/graphify`-taidon kautta, käyttäen mitä tahansa mallia, jota IDE-istuntosi ajaa). Headless `graphify extract` vaatii `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), käynnissä olevan Ollama-instanssin (`OLLAMA_BASE_URL`), AWS-valtuustiedot vakioidun tarjoajaketjun kautta (Bedrock - ei API-avainta tarvita, käyttää IAM:ää), tai `claude` CLI-binäärin (Claude Code - ei API-avainta tarvita, käyttää Claude-tilaustasi). `--dedup-llm`-lippu käyttää samaa avainta.
- **Datan sijaintipaikka** — `graphify extract` tunnistaa automaattisesti, mitä tarjoajaa käyttää sen perusteella, mikä API-avain on asetettu (prioriteetti: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). Koodille, jolla on datan sijaintivaatimuksia, käytä `--backend ollama` (täysin paikallinen) tai anna eksplisiittinen `--backend`-lippu. Kimi (`MOONSHOT_API_KEY`) reitittää Moonshot AI:n palvelimille Kiinassa.
- **Ei telemetriaa**, ei käyttöseurantaa, ei analytiikkaa.
- **Kyselyloki** — jokainen `graphify query`-, `graphify path`-, `graphify explain`- ja MCP `query_graph`-kutsu kirjataan polkuun `~/.cache/graphify-queries.log` JSON Lines -muodossa (aikaleima, kysymys, korpus, palautetut solmut, kesto). Täysiä alagraafivastauksia **ei** tallenneta oletuksena. Aseta `GRAPHIFY_QUERY_LOG_DISABLE=1` kieltäytyäksesi, tai `GRAPHIFY_QUERY_LOG=/dev/null` vaientaaksesi poistamatta koodipolkua käytöstä.

---

## Vianetsintä

**`graphify: command not found` asennuksen jälkeen**
CLI on asennettu, mutta sen bin-hakemisto ei ole kuoresi `PATH`-muuttujassa. Valitse korjaus asennustapasi mukaan:
- **uv** (`uv tool install graphifyy`): komento päätyy uv:n työkalujen bin-hakemistoon (`~/.local/bin`), joka tuoreella macOS/zsh-asennuksella ei usein ole `PATH`-muuttujassa. Aja `uv tool update-shell`, avaa sitten uusi pääte. (Löydä hakemisto komennolla `uv tool dir --bin`.)
- **pipx** (`pipx install graphifyy`): aja `pipx ensurepath`, avaa sitten uusi pääte.
- **pip** (`pip install graphifyy`): pip asentaa skriptit käyttäjän bin-hakemistoon, joka ei välttämättä ole `PATH`-muuttujassa — lisää `~/Library/Python/3.x/bin` (macOS) tai `~/.local/bin` (Linux) PATH-muuttujaasi tiedostossa `~/.zshrc`/`~/.bashrc`, tai aja vain `python -m graphify`.

**`uvx graphify …` tai `uv tool run graphify …` ei ratkaise `graphify`:tä**
PyPI-paketti on `graphifyy`; `graphify` on vain sen tarjoama komento. `uv tool run` käsittelee ensimmäisen sanan *paketin nimenä*, joten se etsii pakettia nimeltä `graphify` ja raportoi `No solution found … no versions of graphify`. Nimeä paketti eksplisiittisesti: `uvx --from graphifyy graphify install` (sama kuin `uv tool run --from graphifyy graphify install`). Tai `uv tool install graphifyy` kerran ja kutsu sitten `graphify`:tä suoraan.

**`uv run --with graphifyy python -m graphify` ajaa hiljaa vanhempaa asennusta**
`uv run` käyttää *järjestelmäsi* Pythonia, joten jos vanhempi `graphifyy` asuu myös siellä (esim. aiempi `pip install graphifyy`), Python saattaa löytää sen kopion ensin `sys.path`:istä, eikä `--with graphifyy` ohita sitä. Se toimii ilman virhettä, mutta saat *vanhan* version käytöksen — esim. ympäristön ohitukset kuten `OPENAI_BASE_URL` jätetään hiljaa huomiotta, joten pyynnöt osuvat oletuspäätepisteeseen ja epäonnistuvat 401:llä, joka näyttää väärältä avaimelta. Sormenjälki on rivi `warning: skill is from graphify <newer>, package is <older>` — se tarkoittaa, että eri asennus latautui, ei vain vanhentunut taito. Tarkista, mikä kopio todella latautui:
```bash
python -c "import graphify; print(graphify.__file__)"
```
Aja sitten asennettu komento suoraan (se käyttää uv:n hallinnoimaa kopiota), tai poista vanhentunut järjestelmäkopio:
```bash
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```

**`python -m graphify` toimii, mutta `graphify`-komento ei**
Kuoresi `PATH` ei sisällä bin-hakemistoa, johon komento asennettiin. Suosi `uv tool install` / `pipx install` -komentoja pelkän `pip`:in sijaan, aja sitten `uv tool update-shell` / `pipx ensurepath` ja avaa uusi pääte (katso asennushuomautukset yllä).

**`/graphify .` aiheuttaa "path not recognized" -virheen PowerShellissä**
PowerShell käsittelee alkukauttaviivan polkuerottimena. Käytä `graphify .` (ilman kauttaviivaa) Windowsilla.

**Graafissa on vähemmän solmuja `--update`-komennon tai uudelleenrakennuksen jälkeen**
Jos refaktorointi poisti tiedostoja, vanhat solmut jäävät jäljelle. Anna `--force` (tai aseta `GRAPHIFY_FORCE=1`) korvataksesi, vaikka uudelleenrakennuksessa olisi vähemmän solmuja.

**`extract` päättyy viestillä "extraction was incomplete ... refusing to overwrite"**
Kun poimintavaihe kaatuu tai läpikäynti ei voi lukea korpusta kokonaan, ajo olisi pienempi kuin täydellinen, joten `graphify extract` kieltäytyy korvaamasta suurempaa olemassa olevaa graafia osittaisella tuloksella (suojellen `graph.json`:iasi). Korjaa taustalla oleva vika ja aja uudelleen, tai anna `--allow-partial` korvataksesi silti.

**Graafissa on kaksoiskappaleita samasta entiteetistä (haamukaksoiskappaleet)**
Haamukaksoiskappaleet (sama symboli esiintyy kahdesti — kerran AST-poiminnasta lähdesijainnin kanssa, kerran semanttisesta poiminnasta ilman) yhdistetään nyt automaattisesti rakennusaikana. Jos näet tämän ennen v0.8.33:a rakennetussa graafissa, aja täysi uudelleenpoiminta siivotaksesi:
```bash
graphify extract . --force
```

**Ollamalta loppuu VRAM / kontekstiikkuna ylittyy**
KV-cache-ikkuna on automaattisesti mitoitettu, mutta voi olla liian suuri GPU:llesi. Pienennä sitä:
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**`LLM returned invalid JSON` / `Unterminated string` -varoitukset**
Mallin JSON-vastaus osui tulostetokenrajaan ja katkesi kesken merkkijonon. graphify palautuu automaattisesti (se jakaa palan ja poimii puolikkaat uudelleen, ja liian suuri yksittäinen dokumentti viipaloidaan ensin otsikko-/kappalerajoista, jotta koko tiedosto katetaan silti), joten nämä varoitukset ovat meluisia mutta eivät tietohäviötä. Vähentääksesi melua, nosta tulosterajaa tai pienennä kunkin palan tulostetta:
```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode deep   # lift the cap
graphify extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
Pilviyhdyskäytävän kanssa kuten OpenRouter, suosi `--backend openai`:a (aseta `OPENAI_BASE_URL`) Ollama-shimin sijaan — se on puhtaampi OpenAI-yhteensopiva polku. Jos mallilla on oma max-output-kattonsa, `--token-budget`:in laskeminen on luotettava vipu.

**Graph HTML on liian suuri avattavaksi selaimessa (>5000 solmua)**
Ohita HTML-generointi ja käytä JSON:ia suoraan:
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**`graph.json`:issa on ristiriitamerkintöjä kahden kehittäjän committaessa samaan aikaan**
Aja `graphify hook install` — se asettaa git merge -ajurin, joka yhdistää `graph.json`:n automaattisesti, joten ristiriitoja ei koskaan tapahdu.

**Poiminta palauttaa tyhjiä solmuja/reunoja dokumenteille tai PDF:ille**
Dokumentit, PDF:t ja kuvat vaativat LLM-kutsun — pelkät koodikorpukset eivät tarvitse avainta. Tarkista, että API-avaimesi on asetettu ja backend on oikea:
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**Taidon versioepäsuhtavaroitus IDE:ssäsi**
Asennettu graphify-versiosi eroaa taitotiedostosta. Päivitä:
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

**Claude Coden kehotusvälimuisti mitätöityy jokaisen `graphify extract`-komennon jälkeen**
Graphify kirjoittaa tulostiedostot (`graph.json`, `graphify-out/`) työtilaan. Jos näitä polkuja ei ohiteta, jokainen kirjoitus mitätöi Claude Coden kehotusvälimuistin, pakottaen täyden uudelleenlatauksen välimuistin kirjoitusnopeudella seuraavalla kierroksella. Lisää ne tiedostoon `.claudeignore`:
```text
# .claudeignore
graph.json
graphify-out/
```

---

## Täydellinen komento-viite

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

> **Yhteisönimet:** agentin sisällä (Claude Code, Gemini CLI) agentti nimeää yhteisöt itse. Kun ajat paljasta CLI:tä, `cluster-only` nimeää ne automaattisesti konfiguroidulla backendilla (sisäänrakennettu tai mukautettu OpenAI-yhteensopiva tarjoaja) — anna `--no-label` pitääksesi `Community N`, tai aja `graphify label` (uudelleen)generoidaksesi nimet tarvittaessa.

---

## Lue lisää

- [Miten se toimii](docs/how-it-works.md) — poimintaputki, yhteisöntunnistus, luottamuspisteytys, vertailut
- [ARCHITECTURE.md](ARCHITECTURE.md) — moduulien jaottelu, miten lisätä kieli
- [Valinnaiset integraatiot](docs/docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite
- [The Memory Layer](https://safishamsi.gumroad.com/l/qetvlo) — kirja graphifyn taustalla olevista ideoista, arkkitehtuurista päästä päähän

---

## graphify Enterprise

[**graphify Enterprise**](https://graphify.com) on graphifyn päälle rakennettu aina päällä oleva kerros — se soveltaa samaa graafilähestymistapaa koko työympäristöösi: kokouksiin, tiedostoihin, dokumentteihin ja koodiin, päivittyen jatkuvasti taustalla.

Rakennettu ihmisille ja tiimeille, joiden työ elää satojen keskustelujen ja dokumenttien joukossa, joita he eivät koskaan voi täysin rekonstruoida.

**[Liity odotuslistalle osoitteessa graphify.com](https://graphify.com).** Ilmainen kokeilu tulossa pian.

---

<details>
<summary>Osallistuminen</summary>

### Kehitysympäristön asetukset

Projekti käyttää [uv](https://docs.astral.sh/uv/):a kehitystyönkulkuun. Asenna se kerran, sitten:

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

Varmenna muokattava asennus:
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### Testien ajaminen

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> macOS-huomautus: testisarja sisältää sekä `sample.f90`- että `sample.F90`-kiinnitystiedostot. Nämä törmäävät kirjainkokoerottelemattomilla HFS+ / APFS-tiedostojärjestelmillä. Aja Linuxilla tai Docker-kontissa, jos sinun täytyy testata molempia Fortran-muunnelmia samanaikaisesti.

### Git-työnkulku

- Aktiivinen kehitys tapahtuu `v8`-haarassa.
- Committityyli: `fix: <description>` / `feat: <description>` / `docs: <description>`
- Ennen PR:n avaamista, aja `uv run pytest tests/ -q` ja varmista, että se läpäisee.
- Lisää kiinnitystiedosto kansioon `tests/fixtures/` ja testit tiedostoon `tests/test_languages.py` jokaiselle uudelle kielipoimijalle.

### Mitä voit osallistua

**Työstetyt esimerkit** ovat hyödyllisin panos. Aja `/graphify` todelliseen korpukseen, tallenna tuloste kansioon `worked/{slug}/`, kirjoita rehellinen `review.md`, joka kattaa mitä graafi teki oikein ja väärin, ja avaa PR.

**Poimintavirheet** — avaa issue syötetiedoston, välimuistimerkinnän (`graphify-out/cache/`) ja sen kanssa, mikä puuttui tai oli väärin.

Katso [ARCHITECTURE.md](ARCHITECTURE.md) moduulien vastuista ja siitä, miten lisätä kieli.

</details>
