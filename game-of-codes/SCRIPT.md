# Life of a token — delivery script

**Game of Codes 2026 · Science & Technology Park, Niš · Saturday 10 October 2026**
36 slides · **28:25** of material in a 30-minute slot · press `T` on the title to start the clock.

This is a **visual deck on a fixed grid**. The slides carry pictures and manifests; you carry
the words. Almost no slide can be read instead of listened to — which is the point, and also
means you cannot wing it. Read these notes once the night before.

28:25 is at the edge of a 30-minute budget. The cut list below recovers nearly three minutes;
take the first two as a matter of course unless the room is running early.

The strip across the top of every journey slide says where the token is: amber going down, teal
coming home. Slides with no strip are outside the journey — the opening block on what a token
is, and the section dividers.

---

## Before you go on

- Press `F`. Press `T`. `N` toggles notes on the presenter screen.
- Open from `file://` if the venue Wi-Fi looks shaky. Only Google Fonts is remote, with a fallback.
- **Slide 30 reveals one bar per click** (3 clicks). Everything else is a single click.
- Have an agent open on the laptop in case someone asks to see a real context dump, and a
  terminal with a cluster in case someone asks to see a real `InferencePool`.

---

## Running order

| # | Slide | Say | Time | Cum. |
|---|---|---|---|---|
| 1 | Title | one request, all the way down and back | 0:30 | 0:30 |
| 2 | **Terminal: you type seven words** | the hook — who has an agent open right now? | 0:40 | 1:10 |
| 3 | **Not a word. Not a letter.** | 54 chars, 9 words, 12 tokens | 1:00 | 2:10 |
| 4 | The two obvious answers are worse | letters vs words vs subwords | 0:55 | 3:05 |
| 5 | **The vocabulary is learned** | GPU earned an entry; Kubernetes did not | 1:05 | 4:10 |
| 6 | And your alphabet sets the price | the 75% Cyrillic surcharge | 1:00 | 5:10 |
| 7 | Eight stops, down and back | point at 3, 5, 6 — don't narrate all eight | 0:40 | 5:50 |
| 8 | § 01 | — | 0:08 | 5:58 |
| 9 | **The request, proportionally** | the harness wrote this, not you | 1:15 | 7:13 |
| 10 | 1,643× | say the number, pause | 0:25 | 7:38 |
| 11 | § 02 | — | 0:08 | 7:46 |
| 12 | **Every hop is a Kubernetes object** | the frame — say it once, then stop repeating it | 0:50 | 8:36 |
| 13 | **Three languages. One is tokens.** | the dangerous lane is MCP | 1:10 | 9:46 |
| 14 | **Per tool. Not per service.** | the control that didn't exist a year ago | 1:15 | 11:01 |
| 15 | It acts *as somebody* | "the agent did it" is a useless audit log | 0:55 | 11:56 |
| 16 | **agentgateway: two routes, one log** | left pane fast, right pane slow | 1:00 | 12:56 |
| 17 | § 03 | — | 0:08 | 13:04 |
| 18 | **Identical. Not interchangeable.** | the cold-replica slide. Slow down. | 1:25 | 14:29 |
| 19 | **A pool, where the Service was** | point at the last two lines | 0:50 | 15:19 |
| 20 | § 04 | land the title | 0:12 | 15:31 |
| 21 | **Same card. Milliseconds apart.** | the two indigo bars are identical | 1:35 | 17:06 |
| 22 | 8.9 ms | physics, not code — and batching is the way out | 0:45 | 17:51 |
| 23 | Stop making them share | why two pools | 1:00 | 18:51 |
| 24 | **Two pools, as deployments** | the caption is the advice: stop at path one | 1:00 | 19:51 |
| 25 | § 05 | — | 0:08 | 19:59 |
| 26 | No queue. A scheduler. | the hatching is money | 1:00 | 20:59 |
| 27 | The KV cache gets a page table | the OS's oldest trick | 0:55 | 21:54 |
| 28 | **Turn seven. One block.** | caching and routing are one optimisation | 1:00 | 22:54 |
| 29 | § 06 | — | 0:08 | 23:02 |
| 30 | **Weights are rent. KV is stock.** (3 clicks) | 11 → 35 sessions, two flags | 1:15 | 24:17 |
| 31 | **Why read all of it?** | dense vs MoE — why decode got cheap | 1:10 | 25:27 |
| 32 | § 07 | — | 0:08 | 25:35 |
| 33 | **🎲 is two tokens** | built for this room | 1:00 | 26:35 |
| 34 | **It was a tool call. Go again.** | the loop, and quadratic cost | 1:05 | 27:40 |
| 35 | Close | stop talking, take questions | 0:45 | 28:25 |
| 36 | Sources | backup — do not present | — | — |

---

## If you are behind

Cut in this order. Nothing downstream refers back to any of them.

1. **4** — the letters/words/subwords trade. Slides 3 and 5 carry the idea. **−55s**
2. **15** — identity. Painful to lose, but 14 and 16 carry the gateway act. **−55s**
3. **27** — PagedAttention. Slide 28 works without it, with one sentence of setup. **−55s**
4. **23** — the pools diagram. Slide 24 shows the same thing as config. **−60s**

Taking the first two lands you at **26:35**, which is the number to aim for.

**Never cut:** 2, 3, 5, 9, 12, 14, 16, 18, 19, 21, 24, 30, 31, 34.

---

## The Kubernetes spine

Four slides carry the platform, and they are the reason an architect stays in the room. The
through-line to say out loud once, on slide 12, and then never repeat:

> "All four of these are Kubernetes objects. Not a vendor console, not a SaaS dashboard, not an
> API you file a ticket against. You can `kubectl get` them, you can put them in git, and you
> can diff them when something changes at three in the morning."

**12 · Every hop is a Kubernetes object.** `Gateway` → `HTTPRoute` → `InferencePool` →
`Deployment`. The amber one is the only unfamiliar kind in the list; everything else has been
in Kubernetes for years.

**16 · agentgateway, as two routes.** The `/v1` route carries identity and a token budget and
sends traffic to your own pool, with the frontier API configured at weight zero — reachable by
explicit route, landing in the same audit log. The `/mcp` route is the one almost nobody has:
per-tool authorisation in CEL, evaluated in the data plane on every call.

**19 · A pool, where the Service was.** One new object and one changed line — `kind:
InferencePool` where it said `kind: Service`. Say the metric names while it is on screen:
`vllm:num_requests_waiting`, `vllm:gpu_cache_usage_perc`, `vllm:prefix_cache_hits_total`. The
picker is a scrape loop and a weighted sum, not magic.

**24 · Two pools, as deployments.** Prefill sized for FLOPs, decode sized for bandwidth, KV
blocks over NIXL on RDMA, one `InferencePool` in front. Then the ordering, which is the real
advice: **cache-aware scheduling first, disaggregation only once you have earned it.**

Both config blocks are the *shape*, not paste-ready files. Say so — field names move between
minors, and an engineer who pastes it and fails will remember that, not the argument.

---

## The opening block — what is a token?

Four slides, and they are new. The deck is called *Life of a token*; the room deserves to know
what one is before you follow it anywhere. Every split on these slides is real output from
`tiktoken` with the `o200k_base` encoding — say so, because people assume the diagrams are drawn.

**3 · Not a word. Not a letter.**
> "This is the answer the model is going to give you, taken apart. Fifty-four characters. Nine
> words. Twelve tokens — so it is neither. Look at the amber ones: E-T-L is two tokens, because
> the tokenizer has never seen enough ETL to keep it whole. But 'failed' and 'nightly' survive
> intact, because they are common."

**4 · Because the two obvious answers are worse.**
> "Why not letters? Your vocabulary is two hundred and fifty-six and every sentence becomes
> enormous — and attention cost grows with the square of sequence length. Why not whole words?
> The vocabulary is unbounded; new words arrive every day, and a word-level model cannot
> represent `agentgateway` at all."

**5 · The vocabulary is learned, not written.**
> "Nobody sat down and wrote this. You start from raw bytes, count which pair occurs together
> most often, merge it, and do that two hundred thousand times. What falls out is a frequency
> ranking of the internet. GPU appears often enough to earn a single entry. Kubernetes — the
> thing we are all running — does not."
>
> Then land it: **nothing in this vocabulary understands anything. It is compression.**

---

## The other slides that matter, and what to say on them

**2 · the terminal**
> "Here is the entire user interface of modern AI. Seven words. Nineteen tokens. Everything I show
> you for the next twenty-five minutes happens between this keystroke and the first character
> coming back — and almost none of it was written by you."

**9 · the request**
> "Your harness just loaded a system prompt, read your project instructions, serialised every tool
> it has, pasted in the files it decided were relevant, and replayed the entire conversation from
> the beginning — because the model has no memory. The illusion of memory is retransmission. And
> then, right at the end, your nineteen tokens."
> *Hands up: who has ever counted the tokens in their tool definitions? Nobody. That's the point.*

**14 · per-tool authorisation**
> "This is the control that did not exist a year ago. Not 'may this agent use MCP' — but 'may this
> agent call delete_customer, given these claims, in this environment'. Your agent is a program
> that writes its own next action. You would not give a junior engineer unrestricted production
> credentials on day one."

**18 · identical ≠ interchangeable**
> "Three replicas. Same image, same weights. And one of them already holds thirty thousand of your
> thirty-one thousand tokens, because this is turn seven. That replica is seventy times cheaper for
> this request. A Service cannot know that. You land on a cold one and pay for the same prefill
> twice. No error. No 503. The dashboard is green."

**21 · prefill vs decode**
> "Look at the bottom bars. They are the same — seventy-one gigabytes, both sides. Now look at the
> top bars. Four and a half petaflops on the left; that sliver on the right. Thirty-one thousand
> times less work for exactly the same memory traffic. Prefill uses the GPU as designed. Decode
> turns the most expensive accelerator NVIDIA sells into a very fancy memcpy."

**31 · dense vs MoE**
> "In a dense model every parameter participates in every token, so decode is hostage to the total
> size of the thing. In a mixture of experts a small router picks a handful, and only those get
> read out of memory. The model on the right can have ten times the parameters and still be cheaper
> to decode — because decode is a bandwidth problem, and you just cut the bandwidth bill."

**34 · the loop**
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
| 200,019 | `tiktoken` vocab size for `o200k_base`. |
| 54 / 9 / 12 | "The nightly ETL job failed on a deserialization error." |
| Prefill 4.4 PFLOP | 2 × 70.6e9 params × 31,219 tokens. Ignores attention's quadratic term. |
| Decode 141 GFLOP | 2 × 70.6e9 × 1 token. |
| 8.9 ms floor | 71 GB of FP8 weights ÷ 8 TB/s HBM → 113 tok/s at batch 1. |
| 62,000 vs 2 FLOP/byte | 4.4e15 ÷ 71e9, and 141e9 ÷ 71e9. Card breaks even ≈ 1,250. |
| KV 320 KB/token | 2 × 80 layers × 8 KV heads × 128 dims × 2 bytes. Half at FP8. |
| 11 → 35 sessions | 110 GB and 180 GB of KV ÷ (31,219 × 320 KB / 160 KB). |
| B300 | 288 GB HBM3e, 8 TB/s, NVLink 5 at 1.8 TB/s per GPU. |

**Illustrative, and the slide says so:** the context breakdown on slide 9, the padding waste on
slide 26, the turn-growth bars on slide 34, and both config blocks (16 and 24), and every llm-d figure on slides 23–24 (those are the
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
- **Dušan Stanojević — reliable services are the ones that crash.** Your slide 18 ends on "nothing
  errors, everything degrades" — a good callback if he spoke first.
