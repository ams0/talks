# Life of a token — delivery script

**Game of Codes 2026 · Science & Technology Park, Niš · Saturday 10 October 2026**
35 slides · **26:10** of material in a 30-minute slot · press `T` on the title to start the clock.

This is a **visual deck**. The slides carry pictures; you carry the words. Almost no slide can be
read instead of listened to — which is the point, and also means you cannot wing it. Read these
notes once the night before.

The strip across the top of every journey slide says where the token is: amber going down, teal
coming home. If you lose your place, look at the strip.

---

## Before you go on

- Press `F`. Press `T`. `N` toggles notes on the presenter screen.
- Open from `file://` if the venue Wi-Fi looks shaky. Only Google Fonts is remote, with a fallback.
- **Slide 28 reveals one bar per click** (3 clicks). Everything else is a single click.
- Have a terminal with an agent open on the laptop in case someone asks to see a real context dump.

---

## Running order

| # | Slide | Say | Time | Cum. |
|---|---|---|---|---|
| 1 | Title | one request, all the way down and back | 0:30 | 0:30 |
| 2 | **Terminal: you type seven words** | the hook — ask who has an agent open right now | 0:40 | 1:10 |
| 3 | Eight stops, down and back | point at 3, 5, 6 — do not narrate all eight | 0:40 | 1:50 |
| 4 | § 01 | — | 0:08 | 1:58 |
| 5 | **The request, proportionally** | the harness wrote this, not you | 1:15 | 3:13 |
| 6 | 1,643× | say the number, pause | 0:25 | 3:38 |
| 7 | Tokenisation, three alphabets | the 75% Cyrillic surcharge | 1:05 | 4:43 |
| 8 | Nothing knows what a tool is | everything above is a convention | 0:30 | 5:13 |
| 9 | § 02 | — | 0:08 | 5:21 |
| 10 | **Three protocols, one gateway** | the dangerous lane is MCP | 1:10 | 6:31 |
| 11 | **Authorisation per tool** | the control that did not exist a year ago | 1:15 | 7:46 |
| 12 | Identity all the way down | "the agent did it" is a useless audit log | 0:55 | 8:41 |
| 13 | Budget · two backends | runaway loops are cost incidents | 1:00 | 9:41 |
| 14 | § 03 | — | 0:08 | 9:49 |
| 15 | **Identical ≠ interchangeable** | the cold-replica slide. Slow down. | 1:25 | 11:14 |
| 16 | Two lines of YAML | deliberately anticlimactic | 0:30 | 11:44 |
| 17 | § 04 | land the title | 0:12 | 11:56 |
| 18 | **Prefill vs decode** | the two indigo bars are identical | 1:35 | 13:31 |
| 19 | 8.9 ms | physics, not code | 0:40 | 14:11 |
| 20 | Read once, serve 64 | batching is the business model | 0:35 | 14:46 |
| 21 | Disaggregation | earn it, don't start here | 1:10 | 15:56 |
| 22 | llm-d, three cards | one sentence each | 0:50 | 16:46 |
| 23 | § 05 | — | 0:08 | 16:54 |
| 24 | Continuous batching | the hatching is money | 1:00 | 17:54 |
| 25 | PagedAttention | the OS's oldest trick | 0:55 | 18:49 |
| 26 | **One red block** | caching and routing are one optimisation | 1:00 | 19:49 |
| 27 | § 06 | — | 0:08 | 19:57 |
| 28 | **HBM budget** (3 clicks) | weights are rent, KV is inventory | 1:15 | 21:12 |
| 29 | **Dense vs MoE** | why decode got cheap | 1:10 | 22:22 |
| 30 | § 07 | — | 0:08 | 22:30 |
| 31 | 128,256 numbers | temperature 0 is not a seed | 0:50 | 23:20 |
| 32 | **🎲 is two tokens** | built for this room | 1:00 | 24:20 |
| 33 | **And round again** | the loop, and quadratic cost | 1:05 | 25:25 |
| 34 | Close | stop talking, take questions | 0:45 | 26:10 |
| 35 | Sources | backup — do not present | — | — |

---

## If you are behind

Cut in this order. Nothing downstream refers back to any of them.

1. **16** — two lines of YAML. Slide 15 already made the argument. **−30s**
2. **31** — the logit distribution. Nice, not load-bearing. **−50s**
3. **12** — identity. Painful to lose, but 11 carries the gateway act. **−55s**
4. **25** — PagedAttention. Slide 26 works without it. **−55s**

**Never cut:** 2, 5, 11, 15, 18, 29, 33. Those seven are the talk.

---

## The seven slides that matter, and what to say on them

**2 · the terminal**
> "Here is the entire user interface of modern AI. Seven words. Nineteen tokens. Everything I show
> you for the next twenty-five minutes happens between this keystroke and the first character
> coming back — and almost none of it was written by you."

**5 · the request**
> "Your harness just loaded a system prompt, read your project instructions, serialised every tool
> it has, pasted in the files it decided were relevant, and replayed the entire conversation from
> the beginning — because the model has no memory. The illusion of memory is retransmission. And
> then, right at the end, your nineteen tokens."
> *Hands up: who has ever counted the tokens in their tool definitions? Nobody. That's the point.*

**11 · per-tool authorisation**
> "This is the control that did not exist a year ago. Not 'may this agent use MCP' — but 'may this
> agent call delete_customer, given these claims, in this environment'. Your agent is a program
> that writes its own next action. You would not give a junior engineer unrestricted production
> credentials on day one."

**15 · identical ≠ interchangeable**
> "Three replicas. Same image, same weights. And one of them already holds thirty thousand of your
> thirty-one thousand tokens, because this is turn seven. That replica is seventy times cheaper for
> this request. A Service cannot know that. You land on a cold one and pay for the same prefill
> twice. No error. No 503. The dashboard is green."

**18 · prefill vs decode**
> "Look at the bottom bars. They are the same — seventy-one gigabytes, both sides. Now look at the
> top bars. Four and a half petaflops on the left; that sliver on the right. Thirty-one thousand
> times less work for exactly the same memory traffic. Prefill uses the GPU as designed. Decode
> turns the most expensive accelerator NVIDIA sells into a very fancy memcpy."

**29 · dense vs MoE**
> "In a dense model every parameter participates in every token, so decode is hostage to the total
> size of the thing. In a mixture of experts a small router picks a handful, and only those get
> read out of memory. The model on the right can have ten times the parameters and still be cheaper
> to decode — because decode is a bandwidth problem, and you just cut the bandwidth bill."

**33 · the loop**
> "The answer that came back was not prose — it was a tool call. So the harness runs the tool,
> appends the result, and sends the whole conversation again. One question from a human is
> routinely five round trips, each longer than the last. Your agent's cost does not grow linearly
> with the conversation. It grows with the square of it."

---

## Numbers you must be able to defend

Everything is division on published figures. None of it is a benchmark. Say so if pressed.

| Claim | Working |
|---|---|
| 12 / 17 / 21 tokens | `tiktoken`, `o200k_base`, October 2026. Four lines to reproduce. |
| 🎲 = two tokens | `decode_single_token_bytes` → `b'\xf0\x9f\x8e'` + `b'\xb2'`, neither valid UTF-8. |
| 1,643× | 31,219 ÷ 19. |
| Prefill 4.4 PFLOP | 2 × 70.6e9 params × 31,219 tokens. Ignores attention's quadratic term. |
| Decode 141 GFLOP | 2 × 70.6e9 × 1 token. |
| 8.9 ms floor | 71 GB of FP8 weights ÷ 8 TB/s HBM → 113 tok/s at batch 1. |
| 62,000 vs 2 FLOP/byte | 4.4e15 ÷ 71e9, and 141e9 ÷ 71e9. Card breaks even ≈ 1,250. |
| KV 320 KB/token | 2 × 80 layers × 8 KV heads × 128 dims × 2 bytes. Half at FP8. |
| 11 → 35 sessions | 110 GB and 180 GB of KV ÷ (31,219 × 320 KB / 160 KB). |
| B300 | 288 GB HBM3e, 8 TB/s, NVLink 5 at 1.8 TB/s per GPU. |

**Illustrative, and the slide says so:** the context breakdown on slide 5, the padding waste on
slide 24, the turn-growth bars on slide 33, and every llm-d figure on slides 21–22 (those are the
project's own — treat as upper bounds).

---

## Expected questions

1. **"What does a box like that cost?"** → Pivot to utilisation. The same card is $0.21 or $15.25
   per million output tokens depending only on how busy you keep it. The hardware is not the
   variable; you are.
2. **"Do I need all this for a 7B model?"** → No. One GPU, one vLLM, done. But fix the routing the
   moment you have a second replica — that part is size-independent.
3. **"Why not Istio / Envoy AI Gateway?"** → Both implement the inference extension; both are fine.
   The point is the API, not the proxy. Do not get drawn into a proxy war on stage.
4. **"Is temperature 0 deterministic?"** → No. Batch composition changes floating-point reduction
   order, which occasionally flips an argmax. It is not a seed.
5. **"Frontier API or self-host?"** → A per-workload decision, not a per-company one. That is what
   the two-backend slide is for.
6. **"How do I see my own context?"** → Most harnesses will dump it; otherwise count with
   `tiktoken` at the client. Offer to show it in the hallway.

---

## Where this talk sits in the programme

Several sessions touch yours. You are not cross-referencing them on the slides — but know the
overlaps so you can defer gracefully rather than re-explaining:

- **Stefan Đokić — running AI agents on real .NET.** Your stop 01 is his whole talk.
- **Stefan Gavrilović — bringing AI into a bank.** The gateway act, from the regulated side.
- **Spirovski & Stefanovski — APIs that don't leak in the era of AI coding.** Adjacent to stop 03.
- **Dušan Stanojević — reliable services are the ones that crash.** Your slide 15 ends on "nothing
  errors, everything degrades" — a good callback if he spoke first.
