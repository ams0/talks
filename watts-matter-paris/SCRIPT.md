# Watts Matter — delivery script (Paris)

Cloud Native AI Summit · Paris (CNIT Forest, La Défense) · 1–3 December 2026
23 slides + sources backup · target **22 minutes** for a 25-minute slot, leaving about three minutes for Q&A.

Press `T` at the first word. The timer in the notes pane switches to *into Q&A* at 22:00.

This is the Hanoi cut (`../watt-matters/`), refreshed for a Paris AI-infrastructure room and a shorter slot. What changed:

- **Cut:** *What is intelligence?* (Landauer) and *Kepler, rewritten*. The rewrite was presented as three-week-old news; it actually shipped in v0.10, July 2025. It now lives as one line on the Kepler slide and a paragraph in its notes.
- **Added:** *In Paris, the cheap hour is lunchtime*. France's grid sits near 20 gCO₂/kWh, so a carbon signal barely moves here; price does. That gives the SHIFT section a local ending.
- **Updated:** the power ladder (B200, NVL72 at 132 kW); the token-price source (Epoch AI, Sep 2026); the IEA figure (Apr 2026); Kepler v0.13 metric names (`kepler_pod_{cpu,gpu}_joules_total`, label `pod_namespace`); Kueue `v1beta2` (v0.20 stopped serving `v1beta1`); the carbon-aware KEDA operator, now shown as a pattern because it has not released since 2023; and the closing line, *Merci beaucoup*.
- **Fixed:** the repo link. `github.com/ams0/watts-matter` never existed. The manifests now live in `manifests/` beside this file and were applied on a kind cluster against Kueue v0.20.7.

---

## Running order

| # | Slide | Target | Cumulative |
|---|---|---|---|
| 1 | Title | 0:15 | 0:15 |
| 2 | What is a watt? | 0:45 | 1:00 |
| 3 | What is a token? | 0:50 | 1:50 |
| 4 | Fix the sentence + **hands up** | 1:10 | 3:00 |
| 5 | The margin squeeze | 1:30 | 4:30 |
| 6 | The scheduler is blind | 1:20 | 5:50 |
| 7 | PUE vs tokens/watt | 0:50 | 6:40 |
| 8 | § 01 MEASURE | 0:10 | 6:50 |
| 9 | Kepler | 1:15 | 8:05 |
| 10 | What visibility looks like | 1:00 | 9:05 |
| 11 | **My favourite screenshot** | 0:45 | 9:50 |
| 12 | § 02 SHIFT | 0:10 | 10:00 |
| 13 | Power caps and time windows | 1:15 | 11:15 |
| 14 | Kueue YAML | 1:10 | 12:25 |
| 15 | KEDA YAML (carbon, so is price) | 1:00 | 13:25 |
| 16 | The arithmetic of when | 1:15 | 14:40 |
| 17 | **In Paris, the cheap hour is lunchtime** | 1:00 | 15:40 |
| 18 | § 03 PACK | 0:10 | 15:50 |
| 19 | Pack: tokens per watt | 1:45 | 17:35 |
| 20 | Failure modes | 1:10 | 18:45 |
| 21 | Contribute | 0:30 | 19:15 |
| 22 | Monday morning | 0:50 | 20:05 |
| 23 | Close | 0:40 | 20:45 |

There is 1:15 of slack before the 22:00 mark. Spend it on the hands-up beat, not on the definitions. This room knows what a token is: take slide 3 at speed and land only the caveat (joules per answer).

---

## Lines to say verbatim

**Slide 4 —** "Tokens are the gasoline. Watts are the crude. And your scheduler is the refinery — which is the part nobody is tuning."

**Slide 5 —** "Between a price that halves and a feed that doesn't grow sits exactly one lever: how efficiently you turn watts into tokens."

**Slide 9 —** "They ripped out the fashionable technology because the boring one was more correct." Deliver dry, and only if the room looks like it has tried Kepler before.

**Slide 11 —** "Burning crude. Refining nothing." — then **one full second of silence**.

**Slide 16 —** "Nothing about the job changed. Only when."

**Slide 17 —** "Your night window is a solar window here. Don't hard-code 22:00 — read the signal."

**Slide 23 —** "Tokens are the product. Watts are the crude. Go tune your refinery." Pause. *Merci beaucoup.*

---

## The one interaction beat

End of slide 4, same as Hanoi:

1. "Hands up — who here runs GPUs in production?"
2. "Keep them up. Who knows what your busiest pod draws, in watts, right now?"

A Paris AI-infrastructure room may contain more managed-cloud users than Hanoi's bare-metal crowd. If fewer hands go up on the first question, change the second one to "…who could find out in under five minutes?" The gap is the same.

---

## Cut order, if you are behind

1. **Slide 15** (KEDA YAML). Keep the Kueue receipt and say "same pattern, carbon and price variants are in the repo."
2. **Slide 7** (PUE vs tokens/watt). Fold it into one sentence on slide 6.
3. **Slide 20** (failure modes). Cut it only if you are badly over, because it is what makes this sound like practice rather than a pitch.

Never cut 11, 16, 17 or 19.

---

## Before you present

- [ ] **Set the date on slide 1.** It reads "December 2026" until the slot is confirmed.
- [ ] Replace **slide 10** and **slide 11** with live captures. They are still marked illustrative. Use `kepler_pod_*` metrics and enable GPU with `--experimental.gpu.enabled`.
- [ ] Put a QR code on **slide 23**, pointing at `github.com/ams0/talks/tree/main/watts-matter-paris`.
- [ ] Re-check the French negative-price count the week of the talk (568 by 8 Oct). It only goes up, and a fresher number lands better.
- [ ] Present from `file://` with fonts cached, as before. The only network request is Google Fonts.

---

## Questions you will get

**"Does Kepler work on our cloud VMs?"** Partially. RAPL is usually not exposed, so you get estimation. v0.12 added an HWMON fallback; bare metal still gives full fidelity.

**"Isn't the French grid already clean, so why bother?"** Exactly why slide 17 exists. In France the argument for shifting is price, not carbon, and the cost argument on slide 5 never depended on carbon.

**"Negative prices are wholesale. We don't pay spot."** True. What you pay depends on the contract, and the deck says "day-ahead" on purpose. The point is that the signal exists and is not shaped like a clock; contracts are drifting toward it.

**"Won't power quota starve my jobs?"** Yes, if you set it badly; that is failure mode two. Alert on pending-workload age.

**"What about DRA / the new Workload API?"** DRA is how you hand out MIG slices cleanly, and Kepler now attributes power per slice. Gang scheduling (Workload API, beta in 1.37) makes packing safer for multi-pod training. Neither is power-aware by itself; that's the gap this talk is about.
