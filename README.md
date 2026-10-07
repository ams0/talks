# talks

Conference talk decks. Each deck is a **single self-contained HTML file** — no build step, no dependencies, no bundler. Open it in a browser and present.

Live at **https://ams0.github.io/talks/**

## Decks

| Date | Talk | Event | Audience |
|---|---|---|---|
| 25 Jul 2026 | [Watts Matter](https://ams0.github.io/talks/watt-matters/) — Power- and carbon-aware scheduling for the AI-era data center | KCD & OpenInfra Days Vietnam, Hà Nội | Technical (platform, infra, SRE) |
| 3 Sep 2026 | [Beyond the Clouds](https://ams0.github.io/talks/beyond-the-clouds/) — Sovereign AI infrastructure to regain control and autonomy | ADA AI Leadership Day, Amsterdam | Non-technical (founders, directors) |
| 9 Sep 2026 | [Beyond the Clouds — technical cut](https://ams0.github.io/talks/beyond-the-clouds-tech/) — the same argument, then down the stack: gateways, inference routing, GPU sharing, the HBM budget | Cloud Native Groningen | Technical (platform and ML engineers) |
| TBD | [Turning AI Into Your Advantage](https://ams0.github.io/talks/ai-advantage/) — a 40-minute hands-on workshop: the three calls, a community case study, three timed exercises | Workshop (event TBD) | Non-technical (business operators) |
| 23 Sep 2026 | [Beyond the Clouds — Skopje](https://ams0.github.io/talks/ai-tech-summit-2026/) — the same argument for Southeast Europe: which EU rules reach a candidate country, the three sovereignty decisions North Macedonia took this summer, the stack without the YAML | AI Tech Summit „Filip Avramchev“, Skopje | Mixed (founders, executives, students, some engineers) |
| 10 Oct 2026 | [Life of a token](https://ams0.github.io/talks/game-of-codes/) — from a keystroke in your agent harness, down to the silicon, and back | Game of Codes, Niš | Technical (developers, architects) |

`beyond-the-clouds/` is the **non-technical cut**: 47 slides plus a sources backup, plain-language architecture, eight charts, the European regulatory timeline, and a five-minute inventory exercise for the interactive half. `SCRIPT.md` beside it is the delivery script — running order, timings, the lines to say verbatim, and the cut order if you are behind.

`beyond-the-clouds-tech/` is the **technical cut** of the same talk: 50 slides plus two sources slides. It drops the leadership-only material (the proverb, the six-laws table, the framework card, the quote wall, the workshop exercise) and rebuilds section 03 to go down the stack one layer at a time — the request path through an agent gateway and an inference gateway, the Gateway API Inference Extension with an `InferencePool` on screen, agentgateway for MCP/A2A policy, llm-d's three well-lit paths, an HBM budget slide (weights versus KV cache on a B300, with the arithmetic), the vLLM/llm-d optimisation knobs in order, HAMi for fractional GPUs, and a five-step K3s build on a single 8×B300 node. Code panels use a real monospace stack; everything else keeps the VOLT house style. It has its own `SCRIPT.md`. The two decks are separate files on purpose: they share a skeleton but are edited for different rooms.

`ai-tech-summit-2026/` is the **Skopje cut** of *Beyond the Clouds*: 38 slides including two sources slides, about 25 minutes for a 30-minute main-stage slot straight before lunch and straight after a panel on the same subject. It starts from the technical cut and drops everything with YAML on it (the Inference Extension, agentgateway, llm-d, the HBM budget, the K3s build, the knobs table, HAMi) plus the slower beats a summit room does not need (the Monty Python opener, the proverb, the concentration donut, the survey bars, the roadmap trio, the KubeCon list, the maintenance slide, the people slide, the ChemAI card, and the VOLT full-stack slide); it keeps the reference architecture and the request-path slide, and adds seven slides for the room: a personal opening on leaving a big American hyperscaler to build Europe's own, which puts the speaker's conflict at the front of the talk rather than the middle and names neither company on the slide so it travels; which EU rules bind a candidate country anyway (AI Act Article 2, the GDPR-mirror data law, the Data Act through your supplier); one slide each for the Digital Operational Resilience Act, the Network and Information Security Directive 2 and the Cyber Resilience Act, spelled out in full with an inline-SVG icon and a line on how each one reaches a Macedonian company; the three sovereignty decisions North Macedonia took between May and July 2026 (the Vezilka AI Factory antenna, the open-weights Macedonian model domestic-yak, the data-centre amendments); and "the smallest sovereign unit fits in one rack". The megawatt chart gains Kragujevac; the 800 MW slide is now measured against the country's own generation. It is **branded for the summit, not for VOLT**: the site's deep-navy ground with a lavender dot field and purple glow, Montserrat throughout (800 for display, standing in for the summit's Mokoto wordmark font, which is not licensed for redistribution), purple and lavender accents, one warning red, and the summit's 2026 logo (`ai-tech-summit-logo.png`, beside the deck) in the footer and on the covers. VOLT appears only as the speaker's affiliation and in the disclosure. Four slides carry an on-slide cross-reference to another session on the summit's own agenda — the competing AI Labs talk on sovereign architecture, the four agent sessions, NVIDIA's AI Factory keynote and the hackathon final — so the talk sits inside the programme rather than beside it. Almost every slide carries a corner icon drawn as inline SVG in the deck's own line style — a tricolore on the French Senate testimony, a ring of twelve stars on the EU-rulebook slide, a seal's face on the SEAL levels, a question mark on the four questions. Slide 23 carries `rack.jpeg`, a real GPU rack, with a lavender halo and a radial mask that fades its edges into the ground. The megawatt chart on slide 25 climbs smallest to largest and reveals one bar per click, so the talk ends that section on the gigafactory rather than opening with it. Slide 35 is a full-bleed party card for Garçon (`garcon.jpg`, @garconbar, tonight from 21:00), sitting between the provocations and the contact slide. `SCRIPT.md` beside it is the delivery script.

`game-of-codes/` is a **new talk**, not a cut of anything, and the only **visual-first** deck in the repo: 35 slides for a 30-minute slot, deliberately carrying almost no prose because the narration is the content. It follows one request from a keystroke in an agent harness — Claude Code, Cursor, whatever you have open — down eight stops to the silicon and back. Stop 01 is what the harness does to seven typed words: a proportional bar showing the system prompt, project instructions, tool schemas, file reads and replayed history that turn 19 tokens into 31,219, with the user's question as a 5-pixel red sliver at the right-hand end. Stop 02 is tokenisation, with real `tiktoken` splits for the same sentence in English, Serbian Latin and Cyrillic (12 / 17 / 21 tokens). Stop 03 is the longest act and is mostly **agentgateway**: the three protocols an agent actually speaks (LLM, MCP, A2A) converging on one data plane, authorisation evaluated per individual tool rather than per service, identity carried from the human through the agent to the tool call, token budgets, and the self-hosted pool beside a frontier API at weight zero. Stop 04 is why identical replicas are not interchangeable — three vLLM pods, one of them glowing because it already holds your prefix. Stops 05 and 06 are the hinge: a two-panel slide where the *weights-read* bars are identical at 71 GB while the *arithmetic* bars differ by 31,000×, then the 8.9 ms decode floor, prefill/decode disaggregation over NIXL, llm-d's three paths, continuous batching, PagedAttention, a 244-block prefix-cache grid with exactly one red block in it, the HBM budget as weights-versus-KV, and dense-versus-MoE as two lit grids (64 of 64 against 8 of 256). The return leg covers the logit distribution, detokenisation, and the agent loop closing — a bar chart of context growing across turns, which is the argument for everything in the middle of the talk.

It is **branded for the conference, not for VOLT**: the palette is lifted from gameofcodes.rs — `#121212` ground, `#07005e` indigo surfaces, `#f8a823` amber as the accent, `#f94144` for failure modes — with Inter and JetBrains Mono, the site's own two families. The conference's dice-between-angle-brackets mark is inlined as a data URI. The signature device is a **route strip** across the top of every journey slide: eight stops, the current one lit amber on the way down and teal on the way home. Nearly every figure is hand-authored inline SVG. Slide 32 is the one built for this room specifically: 🎲, the conference's own logo, is two tokens in `o200k_base` and *neither half is valid UTF-8*, which is why a streaming detokenizer has to buffer — verified with `decode_single_token_bytes`, not asserted. `SCRIPT.md` beside it is the delivery script: running order with cumulative timings to 26:10, the cut order if you run long, the seven slides that must not be cut, the working behind every number, and the expected questions.

`ai-advantage/` is a **40-minute working session** for business operators: 22 slides (21 plus a sources backup) built around three calls — build on top, keep human, change your mind on a schedule — a community case study (Luca) and three timed exercises. Exercise slides carry an on-slide countdown: press `X` to start or pause it, `R` to reset. `handout.html` beside it is the two-page A4 worksheet (print double-sided), and `SCRIPT.md` is the delivery script. It carries its own palette: blueprint navy, a highlighter-yellow marker stroke, and three verdict colours (green automate, amber assist, coral keep human). Slides 11 and 12 are marked *Fill in before presenting* — Luca's story is still a placeholder.

`watt-matters/` is the KCD cut of *Watts Matter*: 25 slides across three moves — measure, shift, pack — with two YAML receipts (Kueue power quota, carbon-aware KEDA), five inline SVG charts and a sources backup. `SCRIPT.md` beside it is the delivery script. It carries its own palette rather than the VOLT house style, since it is a community talk: graphite ground, amber for watts, teal for a clean grid, rust for the idle and throttled states. Type is Newsreader plus Be Vietnam Pro — both cover Vietnamese, which Tiro Tamil does not, and the closing slide needs the diacritics. Two slides are marked *illustrative* on the slide itself — the namespace dashboard and the idle-GPU flatline; replace them with live captures from a real cluster before presenting.

## Presenting

| Key | Does |
|---|---|
| `→` / `Space` | Next slide |
| `←` | Previous slide |
| `N` | Toggle speaker notes |
| `T` | Start/stop the presenter timer |
| `X` / `R` | Start-pause / reset the exercise countdown (`ai-advantage` only) |
| `F` | Fullscreen |
| `P` | Print to PDF |

Eight slides build one item per click (right arrow forward, left arrow back, down/up to skip a build). Slides are laid out at a fixed 1920×1080 and scaled to fit the viewport, so they render identically on any projector. The current slide is remembered across reloads (`sessionStorage`), which is useful if the browser dies mid-talk.

Almost everything is inlined — the VOLT wordmark is a data URI, the halftone ground and every chart are CSS and inline SVG. Photographs are the exception: they sit next to the deck as ordinary files (`chemai-ams-2026.jpg`, `alessandro-vozza.jpg`, `and-now-for-something-completely-different.jpg`; the Skopje deck also carries the summit's logo and favicon; the Game of Codes deck inlines its conference mark as a data URI, since it is only 7 KB, and draws every figure as inline SVG) and are referenced by relative path, because a 450 KB base64 blob inside a file you edit weekly gets re-stored by git on every commit. Relative paths still work from `file://`, so nothing depends on the network. The only network request is Google Fonts for *Tiro Tamil* (Montserrat for the Skopje deck; Inter and JetBrains Mono for Game of Codes), and there's a system fallback stack if the venue Wi-Fi is down. Clone the repo and present from `file://` if you'd rather not depend on the network at all.

## Editing

Each deck is one `index.html` plus any photographs beside it. Edit, commit, push — GitHub Pages redeploys in about a minute.

```bash
git clone git@github.com:ams0/talks.git
cd talks
$EDITOR beyond-the-clouds/index.html
git commit -am "Tighten the SEAL slide"
git push
```

Slide structure is one `<section class="slide ...">` per slide. Speaker notes live in a `<div class="s-notes">` inside each section and are hidden until you press `N`.

## Adding a deck

1. `mkdir <talk-slug>` and drop an `index.html` in it. Keep photographs beside it and reference them by relative path; inline anything small (logos, icons) as a data URI.
2. Add a row to the list in the root `index.html` and to the table above.

## Licence

Slide content © Alessandro Vozza. The VOLT wordmark is the property of VOLT Datacenters and is used with permission. The opening title card is a still from *And Now for Something Completely Different* (1971), © Python (Monty) Pictures, reproduced as a brief quotation in a conference talk.
