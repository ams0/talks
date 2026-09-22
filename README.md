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

`beyond-the-clouds/` is the **non-technical cut**: 47 slides plus a sources backup, plain-language architecture, eight charts, the European regulatory timeline, and a five-minute inventory exercise for the interactive half. `SCRIPT.md` beside it is the delivery script — running order, timings, the lines to say verbatim, and the cut order if you are behind.

`beyond-the-clouds-tech/` is the **technical cut** of the same talk: 50 slides plus two sources slides. It drops the leadership-only material (the proverb, the six-laws table, the framework card, the quote wall, the workshop exercise) and rebuilds section 03 to go down the stack one layer at a time — the request path through an agent gateway and an inference gateway, the Gateway API Inference Extension with an `InferencePool` on screen, agentgateway for MCP/A2A policy, llm-d's three well-lit paths, an HBM budget slide (weights versus KV cache on a B300, with the arithmetic), the vLLM/llm-d optimisation knobs in order, HAMi for fractional GPUs, and a five-step K3s build on a single 8×B300 node. Code panels use a real monospace stack; everything else keeps the VOLT house style. It has its own `SCRIPT.md`. The two decks are separate files on purpose: they share a skeleton but are edited for different rooms.

`ai-tech-summit-2026/` is the **Skopje cut** of *Beyond the Clouds*: 33 slides including two sources slides, about 21 minutes for a 30-minute main-stage slot straight before lunch and straight after a panel on the same subject. It starts from the technical cut and drops everything with YAML on it (the Inference Extension, agentgateway, llm-d, the HBM budget, the K3s build, the knobs table, HAMi) plus the slower beats a summit room does not need (the Monty Python opener, the proverb, the concentration donut, the survey bars, the roadmap trio, the KubeCon list, the maintenance slide, the people slide, the ChemAI card, and the VOLT full-stack slide); it keeps the reference architecture and the request-path slide, and adds three slides for the room: which EU rules bind a candidate country anyway (AI Act Article 2, the GDPR-mirror data law, the Data Act through your supplier), the three sovereignty decisions North Macedonia took between May and July 2026 (the Vezilka AI Factory antenna, the open-weights Macedonian model domestic-yak, the data-centre amendments), and "the smallest sovereign unit fits in one rack". The megawatt chart gains Kragujevac; the 800 MW slide is now measured against the country's own generation. It is **branded for the summit, not for VOLT**: the site's deep-navy ground with a lavender dot field and purple glow, Montserrat throughout (800 for display, standing in for the summit's Mokoto wordmark font, which is not licensed for redistribution), purple and lavender accents, one warning red, and the summit's 2026 logo (`ai-tech-summit-logo.png`, beside the deck) in the footer and on the covers. VOLT appears only as the speaker's affiliation and in the disclosure. Four slides carry an on-slide cross-reference to another session on the summit's own agenda — the competing AI Labs talk on sovereign architecture, the four agent sessions, NVIDIA's AI Factory keynote and the hackathon final — so the talk sits inside the programme rather than beside it. `SCRIPT.md` beside it is the delivery script.

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

Almost everything is inlined — the VOLT wordmark is a data URI, the halftone ground and every chart are CSS and inline SVG. Photographs are the exception: they sit next to the deck as ordinary files (`chemai-ams-2026.jpg`, `alessandro-vozza.jpg`, `and-now-for-something-completely-different.jpg`; the Skopje deck also carries the summit's logo and favicon) and are referenced by relative path, because a 450 KB base64 blob inside a file you edit weekly gets re-stored by git on every commit. Relative paths still work from `file://`, so nothing depends on the network. The only network request is Google Fonts for *Tiro Tamil* (Montserrat for the Skopje deck), and there's a system fallback stack if the venue Wi-Fi is down. Clone the repo and present from `file://` if you'd rather not depend on the network at all.

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
