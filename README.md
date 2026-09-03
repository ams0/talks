# talks

Conference talk decks. Each deck is a **single self-contained HTML file** — no build step, no dependencies, no bundler. Open it in a browser and present.

Live at **https://ams0.github.io/talks/**

## Decks

| Date | Talk | Event | Audience |
|---|---|---|---|
| 3 Sep 2026 | [Beyond the Clouds](https://ams0.github.io/talks/beyond-the-clouds/) — Sovereign AI infrastructure to regain control and autonomy | ADA AI Leadership Day, Amsterdam | Non-technical (founders, directors) |

`beyond-the-clouds/` is the **non-technical cut**: 44 slides plus a sources backup, plain-language architecture, eight charts, the European regulatory timeline. `SCRIPT.md` beside it is the delivery script — running order, timings, the lines to say verbatim, and the cut order if you are behind. A technical cut for an engineering audience is planned as a separate directory rather than a variant of this file.

## Presenting

| Key | Does |
|---|---|
| `→` / `Space` | Next slide |
| `←` | Previous slide |
| `N` | Toggle speaker notes |
| `T` | Start/stop the presenter timer |
| `F` | Fullscreen |
| `P` | Print to PDF |

Slides are laid out at a fixed 1920×1080 and scaled to fit the viewport, so they render identically on any projector. The current slide is remembered across reloads (`sessionStorage`), which is useful if the browser dies mid-talk.

Almost everything is inlined — the VOLT wordmark is a data URI, the halftone ground and every chart are CSS and inline SVG. Photographs are the exception: they sit next to the deck as ordinary files (`chemai-ams-2026.jpg`, `alessandro-vozza.jpg`) and are referenced by relative path, because a 450 KB base64 blob inside a file you edit weekly gets re-stored by git on every commit. Relative paths still work from `file://`, so nothing depends on the network. The only network request is Google Fonts for *Tiro Tamil*, and there's a serif fallback stack if the venue Wi-Fi is down. Clone the repo and present from `file://` if you'd rather not depend on the network at all.

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

Slide content © Alessandro Vozza. The VOLT wordmark is the property of VOLT Datacenters and is used with permission.
