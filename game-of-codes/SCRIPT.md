# Life of a token — delivery script

**Game of Codes 2026 · Science & Technology Park, Niš · Saturday 10 October 2026**
39 slides · **29:10** of material in a 30-minute slot · press `T` on the title to start the clock.

This is a **visual deck on a fixed grid**. The slides carry pictures and manifests; you carry
the words. Almost no slide can be read instead of listened to — which is the point, and also
means you cannot wing it. Read these notes once the night before.

29:10 is over a comfortable 30-minute budget. The cut list below recovers nearly three minutes;
take the first two as a matter of course unless the room is running early.

The strip across the top of every journey slide says where the token is: amber going down, teal
coming home. Slides with no strip are outside the journey — the opening block on what a token
is, and the section dividers.

---

## Before you go on

- Press `F`. Press `T`. `N` toggles notes on the presenter screen.
- Open from `file://` if the venue Wi-Fi looks shaky. Only Google Fonts is remote, with a fallback.
- **Slide 33 reveals one bar per click** (3 clicks). Everything else is a single click.
- Have an agent open on the laptop in case someone asks to see a real context dump, and a
  terminal with a cluster in case someone asks to see a real `InferencePool`.

---

## Running order

| # | Slide | Say | Time | Cum. |
|---|---|---|---|---|
| 1 | Title | one request, all the way down and back | 0:30 | 0:30 |
| 2 | **Who here uses AI?** | your hand up first — the room follows | 0:15 | 0:45 |
| 3 | **Who uses it every day?** | "keep them up" — the drop is the point | 0:12 | 0:57 |
| 4 | **Who has a fleet of agents?** | read the room; it calibrates the rest | 0:18 | 1:15 |
| 5 | **Terminal: you type seven words** | the hook — who has an agent open right now? | 0:40 | 1:55 |
| 6 | **Not a word. Not a letter.** | 54 chars, 9 words, 12 tokens | 1:00 | 2:55 |
| 7 | The two obvious answers are worse | letters vs words vs subwords | 0:55 | 3:50 |
| 8 | **The vocabulary is learned** | GPU earned an entry; Kubernetes did not | 1:05 | 4:55 |
| 9 | And your alphabet sets the price | the 1.9× Cyrillic surcharge | 1:00 | 5:55 |
| 10 | Eight stops, down and back | point at 3, 5, 6 — don't narrate all eight | 0:40 | 6:35 |
| 11 |  01 | — | 0:08 | 6:43 |
| 12 | **The request, proportionally** | the harness wrote this, not you | 1:15 | 7:58 |
| 13 | 1,643× | say the number, pause | 0:25 | 8:23 |
| 14 |  02 | — | 0:08 | 8:31 |
| 15 | **Every hop is a Kubernetes object** | the frame — say it once, then stop repeating it | 0:50 | 9:21 |
| 16 | **Three languages. One is tokens.** | the dangerous lane is MCP | 1:10 | 10:31 |
| 17 | **Per tool. Not per service.** | the control that didn't exist a year ago | 1:15 | 11:46 |
| 18 | It acts *as somebody* | "the agent did it" is a useless audit log | 0:55 | 12:41 |
| 19 | **agentgateway: two routes, one log** | left pane fast, right pane slow | 1:00 | 13:41 |
| 20 |  03 | — | 0:08 | 13:49 |
| 21 | **Identical. Not interchangeable.** | the cold-replica slide. Slow down. | 1:25 | 15:14 |
| 22 | **A pool, where the Service was** | point at the last two lines | 0:50 | 16:04 |
| 23 |  04 | land the title | 0:12 | 16:16 |
| 24 | **Same card. Milliseconds apart.** | the two indigo bars are identical | 1:35 | 17:51 |
| 25 | 8.9 ms | physics, not code — and batching is the way out | 0:45 | 18:36 |
| 26 | Stop making them share | why two pools | 1:00 | 19:36 |
| 27 | **Two pools, as deployments** | the caption is the advice: stop at path one | 1:00 | 20:36 |
| 28 |  05 | — | 0:08 | 20:44 |
| 29 | No queue. A scheduler. | the hatching is money | 1:00 | 21:44 |
| 30 | The KV cache gets a page table | the OS's oldest trick | 0:55 | 22:39 |
| 31 | **Turn seven. One block.** | caching and routing are one optimisation | 1:00 | 23:39 |
| 32 |  06 | — | 0:08 | 23:47 |
| 33 | **Weights are rent. KV is stock.** (3 clicks) | 11 → 35 sessions, two flags | 1:15 | 25:02 |
| 34 | **Why read all of it?** | dense vs MoE — why decode got cheap | 1:10 | 26:12 |
| 35 |  07 | — | 0:08 | 26:20 |
| 36 | **🎲 is three tokens** | built for this room | 1:00 | 27:20 |
| 37 | **It was a tool call. Go again.** | the loop, and quadratic cost | 1:05 | 28:25 |
| 38 | Close | stop talking, take questions | 0:45 | 29:10 |
| 39 | Sources | backup — do not present | — | — |

---

## If you are behind

Cut in this order. Nothing downstream refers back to any of them.

1. **7** — the letters/words/subwords trade. Slides 6 and 8 carry the idea. **−55s**
2. **18** — identity. Painful to lose, but 17 and 19 carry the gateway act. **−55s**
3. **30** — PagedAttention. Slide 31 works without it, with one sentence of setup. **−55s**
4. **26** — the pools diagram. Slide 27 shows the same thing as config. **−60s**

The opening questions are 45 seconds and buy more goodwill than any slide in the deck — cut elsewhere.
Taking the first two lands you at **27:20**; all four gets you to **25:25**. Aim for the first two.

**Never cut:** the three opening questions (2–4), then 6, 8, 12, 15, 17, 19, 21, 22, 24, 27, 33, 34, 37.

---

## The opening questions

Three slides, 45 seconds, and they do two jobs. They get arms in the air before you have asked
anyone to think, and the third one tells you which talk to give.

Get your own hand up on question one — a room follows the speaker, and a dead first question
poisons the next two. On question two say **"keep them up"** rather than asking again, so people
watch hands going *down*; the drop is the content, not the count. Let them look around for a beat.

Question three is the calibration. **Many hands:** the room already feels the cost, so move
briskly through the harness act and spend what you save on the gateway and llm-d. **Two or three
hands:** slow down on the 31,219-token context slide, because that is what makes the rest matter
and this room has not felt it yet. **No hands at all,** which is quite likely: *"good — then
nothing in this talk has hurt you yet"*, which gets a laugh and reframes the whole thing as a
warning rather than a retrospective.

The indigo ground on question three marks the turn into the talk.

---

## The Kubernetes spine

Four slides carry the platform, and they are the reason an architect stays in the room. The
through-line to say out loud once, on slide 15, and then never repeat:

> "All four of these are Kubernetes objects. Not a vendor console, not a SaaS dashboard, not an
> API you file a ticket against. You can `kubectl get` them, you can put them in git, and you
> can diff them when something changes at three in the morning."

**15 · Every hop is a Kubernetes object.** `Gateway` → `HTTPRoute` → `InferencePool` →
`Deployment`. The amber one is the only unfamiliar kind in the list; everything else has been
in Kubernetes for years.

**19 · agentgateway, as two routes.** The `/v1` route carries identity and a token budget and
sends traffic to your own pool, with the frontier API configured at weight zero — reachable by
explicit route, landing in the same audit log. The `/mcp` route is the one almost nobody has:
per-tool authorisation in CEL, evaluated in the data plane on every call.

**22 · A pool, where the Service was.** One new object and one changed line — `kind:
InferencePool` where it said `kind: Service`. Say the metric names while it is on screen:
`vllm:num_requests_waiting`, `vllm:gpu_cache_usage_perc`, `vllm:prefix_cache_hits_total`. The
picker is a scrape loop and a weighted sum, not magic.

**27 · Two pools, as deployments.** Prefill sized for FLOPs, decode sized for bandwidth, KV
blocks over NIXL on RDMA, one `InferencePool` in front. Then the ordering, which is the real
advice: **cache-aware scheduling first, disaggregation only once you have earned it.**

Both config blocks are the *shape*, not paste-ready files. Say so — field names move between
minors, and an engineer who pastes it and fails will remember that, not the argument.

---

## The opening block — what is a token?

Four slides, and they are new. The deck is called *Life of a token*; the room deserves to know
what one is before you follow it anywhere. Every split on these slides is real output from
**Llama 3's own tokenizer** — the model these slides serve — rebuilt as a `tiktoken` encoding from its
128,256-entry vocabulary. Say that it is measured, because people assume the diagrams are drawn.

**6 · Not a word. Not a letter.**
> "This is the answer the model is going to give you, taken apart. Fifty-four characters. Nine
> words. Twelve tokens — so it is neither. Look at the amber ones: E-T-L is two tokens, because
> the tokenizer has never seen enough ETL to keep it whole. But 'failed' and 'nightly' survive
> intact, because they are common."

**7 · Because the two obvious answers are worse.**
> "Why not letters? Your vocabulary is two hundred and fifty-six and every sentence becomes
> enormous — and attention cost grows with the square of sequence length. Why not whole words?
> The vocabulary is unbounded; new words arrive every day, and a word-level model cannot
> represent `agentgateway` at all."

**8 · The vocabulary is learned, not written.**
> "Nobody sat down and wrote this. You start from raw bytes, count which pair occurs together
> most often, merge it, and do that two hundred thousand times. What falls out is a frequency
> ranking of the internet. GPU appears often enough to earn a single entry. Kubernetes — the
> thing we are all running — does not."
>
> Then land it: **nothing in this vocabulary understands anything. It is compression.**

---

## The other slides that matter, and what to say on them

**5 · the terminal**
> "Here is the entire user interface of modern AI. Seven words. Nineteen tokens. Everything I show
> you for the next twenty-five minutes happens between this keystroke and the first character
> coming back — and almost none of it was written by you."

**12 · the request**
> "Your harness just loaded a system prompt, read your project instructions, serialised every tool
> it has, pasted in the files it decided were relevant, and replayed the entire conversation from
> the beginning — because the model has no memory. The illusion of memory is retransmission. And
> then, right at the end, your nineteen tokens."
> *Hands up: who has ever counted the tokens in their tool definitions? Nobody. That's the point.*

**17 · per-tool authorisation**
> "This is the control that did not exist a year ago. Not 'may this agent use MCP' — but 'may this
> agent call delete_customer, given these claims, in this environment'. Your agent is a program
> that writes its own next action. You would not give a junior engineer unrestricted production
> credentials on day one."

**21 · identical ≠ interchangeable**
> "Three replicas. Same image, same weights. And one of them already holds thirty thousand of your
> thirty-one thousand tokens, because this is turn seven. That replica is seventy times cheaper for
> this request. A Service cannot know that. You land on a cold one and pay for the same prefill
> twice. No error. No 503. The dashboard is green."

**24 · prefill vs decode**
> "Look at the bottom bars. They are the same — seventy-one gigabytes, both sides. Now look at the
> top bars. Four and a half petaflops on the left; that sliver on the right. Thirty-one thousand
> times less work for exactly the same memory traffic. Prefill uses the GPU as designed. Decode
> turns the most expensive accelerator NVIDIA sells into a very fancy memcpy."

**34 · dense vs MoE**
> "In a dense model every parameter participates in every token, so decode is hostage to the total
> size of the thing. In a mixture of experts a small router picks a handful, and only those get
> read out of memory. The model on the right can have ten times the parameters and still be cheaper
> to decode — because decode is a bandwidth problem, and you just cut the bandwidth bill."

**37 · the loop**
> "The answer that came back was not prose — it was a tool call. So the harness runs the tool,
> appends the result, and sends the whole conversation again. One question from a human is
> routinely five round trips, each longer than the last. Your agent's cost does not grow linearly
> with the conversation. It grows with the square of it."

---

## Numbers you must be able to defend

All token counts were re-measured on **Llama 3's own 128,256-entry tokenizer**, not GPT-4o's
`o200k_base`. The two disagree in exactly the places that matter: Cyrillic costs 1.92× on Llama
against 1.75× on GPT-4o, and the die is three tokens rather than two. They agree on everything
else — slide 6's twelve tokens and all four words on slide 8 are identical on both.
If anyone asks why Llama's numbers: because that is the model in the manifests on slides 15–27.

Everything is division on published figures. None of it is a benchmark. Say so if pressed.

| Claim | Working |
|---|---|
| 12 / 20 / 23 tokens | Llama 3's tokenizer, October 2026. Cyrillic is **1.92×** English. |
| 🎲 = three tokens | `b'\xf0\x9f'` + `b'\x8e'` + `b'\xb2'`, not one of them valid UTF-8. |
| 1,643× | 31,219 ÷ 19. |
| 128,256 | Llama 3 vocabulary: ~100k inherited from tiktoken + 28k added for non-English. |
| 54 / 9 / 12 | "The nightly ETL job failed on a deserialization error." |
| Prefill 4.4 PFLOP | 2 × 70.6e9 params × 31,219 tokens. Ignores attention's quadratic term. |
| Decode 141 GFLOP | 2 × 70.6e9 × 1 token. |
| 8.9 ms floor | 71 GB of FP8 weights ÷ 8 TB/s HBM → 113 tok/s at batch 1. |
| 62,000 vs 2 FLOP/byte | 4.4e15 ÷ 71e9, and 141e9 ÷ 71e9. Card breaks even ≈ 1,250. |
| KV 320 KB/token | 2 × 80 layers × 8 KV heads × 128 dims × 2 bytes. Half at FP8. |
| 11 → 35 sessions | 110 GB and 180 GB of KV ÷ (31,219 × 320 KB / 160 KB). |
| B300 | 288 GB HBM3e, 8 TB/s, NVLink 5 at 1.8 TB/s per GPU. |

**Illustrative, and the slide says so:** the context breakdown on slide 12, the padding waste on
slide 29, the turn-growth bars on slide 37, and both config blocks (19 and 27); every llm-d figure on slides 26–27 is the project's own — treat as upper bounds.

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
- **Dušan Stanojević — reliable services are the ones that crash.** Your slide 21 ends on "nothing
  errors, everything degrades" — a good callback if he spoke first.
