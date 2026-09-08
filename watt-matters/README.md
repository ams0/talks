# talks

Conference talk decks. Each deck is a **single self-contained HTML file** — no build step, no dependencies, no bundler. Open it in a browser and present.

Live at **https://ams0.github.io/talks/**

## Decks

| Date | Talk | Event | Audience |
|---|---|---|---|
| 3 Sep 2026 | [Beyond the Clouds](https://ams0.github.io/talks/beyond-the-clouds/) — Sovereign AI infrastructure to regain control and autonomy | ADA AI Leadership Day, Amsterdam | Non-technical (founders, directors) |
| 25 Jul 2026 | [Watts Matter](https://ams0.github.io/talks/watts-matter/) — Power- and carbon-aware scheduling for the AI-era data center | KCD & OpenInfra Days Vietnam, Hà Nội | Technical (platform, infra, SRE) |

`beyond-the-clouds/` is the **non-technical cut**: 47 slides plus a sources backup, plain-language architecture, eight charts, the European regulatory timeline, and a five-minute inventory exercise for the interactive half. `SCRIPT.md` beside it is the delivery script — running order, timings, the lines to say verbatim, and the cut order if you are behind. A technical cut for an engineering audience is planned as a separate directory rather than a variant of this file.

`watts-matter/` is the KCD cut: 25 slides across three moves — measure, shift, pack — with two YAML receipts (Kueue power quota, carbon-aware KEDA), five inline SVG charts and a sources backup. `SCRIPT.md` beside it is the delivery script. It carries its own palette rather than the VOLT house style, since it is a community talk: graphite ground, amber for watts, teal for a clean grid, rust for the idle and throttled states. Type is Newsreader plus Be Vietnam Pro — both cover Vietnamese, which Tiro Tamil does not, and the closing slide needs the diacritics.

## Presenting

| Key | Does |
|---|---|
| `→` / `Space` | Next slide |
| `←` | Previous slide |
| `N` | Toggle speaker notes |
| `T` | Start/stop the presenter timer |
| `F` | Fullscreen |
| `P` | Print to PDF |

Eight slides build one item per click (right arrow forward, left arrow back, down/up to skip a build). Slides are laid out at a fixed 1920×1080 and scaled to fit the viewport, so they render identically on any projector. The current slide is remembered across reloads (`sessionStorage`), which is useful if the browser dies mid-talk.

Two slides in `watts-matter/` are marked *illustrative* on the slide itself — the namespace dashboard and the idle-GPU flatline. Replace them with live captures from a real cluster before presenting; the argument is much stronger with your own numbers on it.

Almost everything is inlined — the VOLT wordmark is a data URI, the halftone ground and every chart are CSS and inline SVG. Photographs are the exception: they sit next to the deck as ordinary files (`chemai-ams-2026.jpg`, `alessandro-vozza.jpg`, `and-now-for-something-completely-different.jpg`) and are referenced by relative path, because a 450 KB base64 blob inside a file you edit weekly gets re-stored by git on every commit. Relative paths still work from `file://`, so nothing depends on the network. The only network request is Google Fonts for *Tiro Tamil*, and there's a serif fallback stack if the venue Wi-Fi is down. Clone the repo and present from `file://` if you'd rather not depend on the network at all.

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
