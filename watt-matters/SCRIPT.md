# Watts Matter — delivery script

KCD & OpenInfra Days Vietnam · Hà Nội · 25 July 2026
25 slides + sources backup · target **28 minutes**, leaving room for Q&A in a 35-minute slot.

Press `T` at the first word. The timer in the notes pane switches to *into Q&A* at 28:00.

---

## Running order

| # | Slide | Target | Cumulative |
|---|---|---|---|
| 1 | Title | 0:15 | 0:15 |
| 2 | What is a watt? | 0:50 | 1:05 |
| 3 | What is intelligence? | 1:00 | 2:05 |
| 4 | What is a token? | 0:55 | 3:00 |
| 5 | Fix the sentence + **hands up** | 1:15 | 4:15 |
| 6 | The margin squeeze | 1:40 | 5:55 |
| 7 | The scheduler is blind | 1:30 | 7:25 |
| 8 | PUE vs tokens/watt | 1:00 | 8:25 |
| 9 | § 01 MEASURE | 0:15 | 8:40 |
| 10 | Kepler | 1:15 | 9:55 |
| 11 | What visibility looks like | 1:10 | 11:05 |
| 12 | **My favourite screenshot** | 0:50 | 11:55 |
| 13 | Kepler, rewritten | 1:05 | 13:00 |
| 14 | § 02 SHIFT | 0:15 | 13:15 |
| 15 | Power caps and time windows | 1:30 | 14:45 |
| 16 | Kueue YAML | 1:20 | 16:05 |
| 17 | KEDA YAML | 1:20 | 17:25 |
| 18 | The arithmetic of when | 1:30 | 18:55 |
| 19 | § 03 PACK | 0:15 | 19:10 |
| 20 | Pack: tokens per watt | 2:00 | 21:10 |
| 21 | Failure modes | 1:15 | 22:25 |
| 22 | Contribute | 0:35 | 23:00 |
| 23 | Monday morning | 1:00 | 24:00 |
| 24 | Close | 0:45 | 24:45 |

Three minutes of slack is deliberate. It goes to the hands-up beat on slide 5 and to whatever the room wants to argue about on slide 20.

---

## Lines to say verbatim

**Slide 3 —** "The best-known intelligence we have runs on twenty watts. An H100 is seven hundred. Physics is not the blocker. Engineering is — and engineering is our job."

**Slide 5 —** "Tokens are the gasoline. Watts are the crude. And your scheduler is the refinery — which is the part nobody is tuning."

**Slide 6 —** "Between a price that halves and a feed that doesn't grow sits exactly one lever: how efficiently you turn watts into tokens."

**Slide 12 —** "Burning crude. Refining nothing." — then **one full second of silence**. Do not fill it.

**Slide 13 —** "They ripped out the fashionable technology because the boring one was more correct." Deliver dry.

**Slide 18 —** "Nothing about the job changed. Only when."

**Slide 24 —** "Tokens are the product. Watts are the crude. Go tune your refinery." Pause. Then *Cảm ơn các bạn rất nhiều!*

---

## The one interaction beat

End of slide 5, before you advance:

1. "Hands up — who here runs GPUs in production?" *(most of the room)*
2. "Keep them up. Who knows what your busiest pod draws, in watts, right now?" *(almost every hand drops)*

That gap is the talk. Name it out loud — "that's the gap, and the rest of this is about closing it" — and move on. Do not let it become a discussion; you get that back at the end.

---

## Cut order, if you are behind

Cut in this order and nothing structural breaks:

1. **Slide 3** (intelligence / Landauer) — the most beautiful slide and the least load-bearing.
2. **Slide 13** (Kepler rewritten) — news, not argument. Mention it in one sentence on slide 10 instead.
3. **Slide 17** (KEDA YAML) — keep the Kueue receipt, drop the second one, say "same pattern, the manifest is in the repo."
4. **Slide 21** (failure modes) — only if you are badly over. It is what makes you sound like a practitioner rather than a vendor, so it costs you real credibility.

Never cut 12, 18 or 20. Those three carry the argument.

---

## Before you present

- [ ] Replace **slide 11** with a live Grafana capture from a real cluster.
- [ ] Replace **slide 12** with a real DCGM flatline. Yours will look worse than the illustration, which is the point.
- [ ] Replace the repo URL on **slide 24** with a QR code.
- [ ] Practise *Cảm ơn các bạn rất nhiều* out loud. Say it once, cleanly, and do not apologise for the accent.
- [ ] Check the projector: the deck is a fixed 1920×1080 canvas scaled to fit, so anything 16:9 is fine. If the venue is 4:3, expect letterboxing rather than clipping.
- [ ] The only network request is Google Fonts. If venue Wi-Fi is hostile it falls back to Georgia and a system sans, which is legible but not the intended look — clone the repo and present from `file://` with the fonts cached, or accept the fallback.

---

## Questions you will get

**"Does Kepler work on our cloud VMs?"** Partially — RAPL is usually not exposed, so you get estimation rather than measurement. Bare metal gives full fidelity. Say this before they ask; it is on slide 10.

**"Isn't this just sustainability with extra steps?"** No — slide 6 is the answer. The carbon signal and the price signal point the same direction most of the time, and the argument works on cost alone.

**"What's the overhead of running Kepler?"** Post-rewrite it reads `/proc` and `/sys` with no privileged capabilities. Do not quote a percentage you have not measured yourself.

**"Won't power quota starve my jobs?"** Yes, if you set it badly — that is failure mode two on slide 21. Alert on pending-workload age and treat starvation as evidence for capacity, not as a reason to remove the envelope.
