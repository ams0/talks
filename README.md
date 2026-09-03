# talks

Conference talk decks. Each deck is a **single self-contained HTML file** — no build step, no dependencies, no bundler. Open it in a browser and present.

Live at **https://ams0.github.io/talks/**

## Decks

| Date | Talk | Event | Audience |
|---|---|---|---|
| 3 Sep 2026 | [Beyond the Clouds](https://ams0.github.io/talks/beyond-the-clouds/) — Sovereign AI infrastructure to regain control and autonomy | ADA AI Leadership Day, Amsterdam | Non-technical (founders, directors) |

`beyond-the-clouds/` is the **non-technical cut**: 35 slides, plain-language architecture, five charts, the European regulatory timeline. A technical cut for an engineering audience is planned as a separate directory rather than a variant of this file.

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

Everything is inlined — the VOLT wordmark is a data URI, the halftone ground is CSS gradients. The only network request is Google Fonts for *Tiro Tamil*, and there's a serif fallback stack if the venue Wi-Fi is down. Clone the repo and present from `file://` if you'd rather not depend on the network at all.

## Editing

Each deck is one file. Edit it, commit, push — GitHub Pages redeploys in about a minute.

```bash
git clone git@github.com:ams0/talks.git
cd talks
$EDITOR beyond-the-clouds/index.html
git commit -am "Tighten the SEAL slide"
git push
```

Slide structure is one `<section class="slide ...">` per slide. Speaker notes live in a `<div class="s-notes">` inside each section and are hidden until you press `N`.

## Adding a deck

1. `mkdir <talk-slug>` and drop an `index.html` in it.
2. Add a row to the list in the root `index.html` and to the table above.

## Licence

Slide content © Alessandro Vozza. The VOLT wordmark is the property of VOLT Datacenters and is used with permission.
