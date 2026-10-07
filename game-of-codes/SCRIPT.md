# Life of a token — delivery script

**Game of Codes 2026 · Science & Technology Park, Niš · Saturday 10 October 2026**
37 slides · **28:25** of material in a 30-minute slot · press `T` on the title to start the clock.

This is a **visual deck on a fixed grid**. The slides carry pictures; you carry the words.
Almost no slide can be read instead of listened to — which is the point, and also means you
cannot wing it. Read these notes once the night before.

28:25 is over a comfortable 30-minute budget. The cut list below recovers nearly three minutes;
take the first two cuts as a matter of course unless the room is running early.

The strip across the top of every journey slide says where the token is: amber going down, teal
coming home. Slides with no strip are outside the journey — the opening block on what a token
actually is, and the section dividers.

---

## Before you go on

- Press `F`. Press `T`. `N` toggles notes on the presenter screen.
- Open from `file://` if the venue Wi-Fi looks shaky. Only Google Fonts is remote, with a fallback.
- **Slide 30 reveals one bar per click** (3 clicks). Everything else is a single click.
- Have an agent open on the laptop in case someone asks to see a real context dump.

---

## Running order

| # | Slide | Say | Time | Cum. |
|---|---|---|---|---|
| 1 | Title | one request, all the way down and back | 0:30 | 0:30 |
| 2 | **Terminal: you type seven words** | the hook — ask who has an agent open now | 0:40 | 1:10 |
| 3 | First — what *is* a token? | a beat before the definition | 0:15 | 1:25 |
| 4 | **Not a word. Not a letter.** | 54 chars, 9 words, 12 tokens | 1:00 | 2:25 |
| 5 | The two obvious answers are worse | letters vs words vs subwords | 0:55 | 3:20 |
| 6 | **The vocabulary is learned** | GPU earned an entry; Kubernetes did not | 1:05 | 4:25 |
| 7 | And your alphabet sets the price | the 75% Cyrillic surcharge | 1:05 | 5:30 |
| 8 | Eight stops, down and back | point at 3, 5, 6 — don't narrate all eight | 0:40 | 6:10 |
| 9 | § 01 | — | 0:08 | 6:18 |
| 10 | **The request, proportionally** | the harness wrote this, not you | 1:15 | 7:33 |
| 11 | 1,643× | say the number, pause | 0:25 | 7:58 |
| 12 | § 02 | — | 0:08 | 8:06 |
| 13 | **Three languages. One is tokens.** | the dangerous lane is MCP | 1:10 | 9:16 |
| 14 | **Per tool. Not per service.** | the control that didn't exist a year ago | 1:15 | 10:31 |
| 15 | It acts *as somebody* | "the agent did it" is a useless audit log | 0:55 | 11:26 |
| 16 | Two more jobs for the gateway | budgets and the two backends | 1:00 | 12:26 |
| 17 | § 03 | — | 0:08 | 12:34 |
| 18 | **Identical. Not interchangeable.** | the cold-replica slide. Slow down. | 1:25 | 13:59 |
| 19 | § 04 | land the title | 0:12 | 14:11 |
| 20 | **Same card. Milliseconds apart.** | the two indigo bars are identical | 1:35 | 15:46 |
| 21 | 8.9 ms | physics, not code | 0:40 | 16:26 |
| 22 | Read once, serve 64 | batching is the business model | 0:35 | 17:01 |
| 23 | Stop making them share | earn it, don't start here | 1:10 | 18:11 |
| 24 | llm-d, three cards | one sentence each | 0:50 | 19:01 |
| 25 | § 05 | — | 0:08 | 19:09 |
| 26 | No queue. A scheduler. | the hatching is money | 1:00 | 20:09 |
| 27 | The KV cache gets a page table | the OS's oldest trick | 0:55 | 21:04 |
| 28 | **Turn seven. One block.** | caching and routing are one optimisation | 1:00 | 22:04 |
| 29 | § 06 | — | 0:08 | 22:12 |
| 30 | **Weights are rent. KV is stock.** (3 clicks) | 11 → 35 sessions, two flags | 1:15 | 23:27 |
| 31 | **Why read all of it?** | dense vs MoE — why decode got cheap | 1:10 | 24:37 |
| 32 | § 07 | — | 0:08 | 24:45 |
| 33 | 128,256 numbers. One wins. | temperature 0 is not a seed | 0:50 | 25:35 |
| 34 | **🎲 is two tokens** | built for this room | 1:00 | 26:35 |
| 35 | **It was a tool call. Go again.** | the loop, and quadratic cost | 1:05 | 27:40 |
| 36 | Close | stop talking, take questions | 0:45 | 28:25 |
| 37 | Sources | backup — do not present | — | — |

---

## If you are behind

Cut in this order. Nothing downstream refers back to any of them.

1. **33** — the logit distribution. Nice, not load-bearing. **−50s**
2. **15** — identity. Painful to lose, but 14 carries the gateway act. **−55s**
3. **27** — PagedAttention. Slide 28 works without it. **−55s**
4. **5** — the letters/words/subwords trade. Slides 4 and 6 carry the idea. **−55s**

Taking the first two lands you at **26:40**, which is the number to aim for.

**Never cut:** 2, 4, 6, 10, 14, 18, 20, 30, 31, 35. Those ten are the talk.

---

## The opening block — what is a token?

Four slides, and they are new. The deck is called *Life of a token*; the room deserves to know
what one is before you follow it anywhere. Every split on these slides is real output from
`tiktoken` with the `o200k_base` encoding — say so, because people assume the diagrams are drawn.

**4 · Not a word. Not a letter.**
> "This is the answer the model is going to give you, taken apart. Fifty-four characters. Nine
> words. Twelve tokens — so it is neither. Look at the amber ones: E-T-L is two tokens, because
> the tokenizer has never seen enough ETL to keep it whole. But 'failed' and 'nightly' survive
> intact, because they are common."

**5 · Because the two obvious answers are worse.**
> "Why not letters? Your vocabulary is two hundred and fifty-six and every sentence becomes
> enormous — and attention cost grows with the square of sequence length. Why not whole words?
> The vocabulary is unbounded; new words arrive every day, and a word-level model cannot
> represent `agentgateway` at all."

**6 · The vocabulary is learned, not written.**
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

**10 · the request**
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

**20 · prefill vs decode**
> "Look at the bottom bars. They are the same — seventy-one gigabytes, both sides. Now look at the
> top bars. Four and a half petaflops on the left; that sliver on the right. Thirty-one thousand
> times less work for exactly the same memory traffic. Prefill uses the GPU as designed. Decode
> turns the most expensive accelerator NVIDIA sells into a very fancy memcpy."

**31 · dense vs MoE**
> "In a dense model every parameter participates in every token, so decode is hostage to the total
> size of the thing. In a mixture of experts a small router picks a handful, and only those get
> read out of memory. The model on the right can have ten times the parameters and still be cheaper
> to decode — because decode is a bandwidth problem, and you just cut the bandwidth bill."

**35 · the loop**
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

**Illustrative, and the slide says so:** the context breakdown on slide 10, the padding waste on
slide 26, the turn-growth bars on slide 35, and every llm-d figure on slides 23–24 (those are the
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
