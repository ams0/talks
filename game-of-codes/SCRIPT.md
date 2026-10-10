# Life of a token — delivery script

**Alessandro Vozza · VOLT Datacenters**

**Game of Codes 2026 · Science & Technology Park, Niš · Saturday 10 October 2026**

41 slides, including the introduction and sources backup. **26:21 planned delivery**, with 39 seconds of breathing room against the **27:00 timer target**. All content slides remain; the running order includes the tokenisation trade and identity slides.

The slides carry pictures; these notes carry explanation. Amber follows the request down; teal follows the answer home.

## Before you go on

- Press **F** for fullscreen, **T** to start the timer, **N** for notes. Arrow keys advance; **P** prints.
- Keep a local copy for unreliable venue Wi-Fi. Fonts and artwork are bundled for offline presentation.
- Slide 33 reveals its capacity rows one at a time.
- Have an agent context dump and a cluster terminal ready for optional questions. No embedded live demo or required network call is part of the talk.
- Configuration snippets show architecture, not complete deployable manifests. Check installed versions before demonstrating them.

## Running order

| # | Slide / speaking cue | Time | Cum. |
|---|---|---:|---:|
| 1 | Life of a token | 0:30 | 0:30 |
| 2 | Who uses AI? | 0:05 | 0:35 |
| 3 | Every day? | 0:08 | 0:43 |
| 4 | Who runs a fleet? | 0:15 | 0:58 |
| 5 | Nine words. How many tokens? | 0:35 | 1:33 |
| 6 | Tokens aren’t words | 0:55 | 2:28 |
| 7 | Bytes. Words. The compromise | 0:35 | 3:03 |
| 8 | Compression, learned | 0:50 | 3:53 |
| 9 | Same meaning. Different bill | 0:55 | 4:48 |
| 10 | Down to silicon. Back again | 0:35 | 5:23 |
| 11 | The prompt you never wrote | 0:08 | 5:31 |
| 12 | Your prompt is 0.04% | 1:05 | 6:36 |
| 13 | ≈2,601× | 0:20 | 6:56 |
| 14 | Where trust ends | 0:08 | 7:04 |
| 15 | Four objects. One stack | 0:45 | 7:49 |
| 16 | Models. Tools. Agents | 1:00 | 8:49 |
| 17 | Authorize the action | 1:05 | 9:54 |
| 18 | Carry the identity | 0:35 | 10:29 |
| 19 | Two routes. One audit trail | 1:05 | 11:34 |
| 20 | Which GPU answers? | 0:08 | 11:42 |
| 21 | Same model. Different cost | 1:15 | 12:57 |
| 22 | Route to the cache | 0:55 | 13:52 |
| 23 | One GPU. Two bottlenecks | 0:10 | 14:02 |
| 24 | Prefill computes. Decode reads | 1:25 | 15:27 |
| 25 | 8.9 ms | 0:45 | 16:12 |
| 26 | Separate when it pays | 0:55 | 17:07 |
| 27 | Start with smarter routing | 1:00 | 18:07 |
| 28 | Inside the engine | 0:08 | 18:15 |
| 29 | Refill every step | 0:55 | 19:10 |
| 30 | Give KV a page table | 0:50 | 20:00 |
| 31 | Reuse the prefix | 0:55 | 20:55 |
| 32 | What fits in memory? | 0:08 | 21:03 |
| 33 | Weights are rent. KV is capacity | 1:05 | 22:08 |
| 34 | Activate less. Read less | 1:00 | 23:08 |
| 35 | The journey home | 0:08 | 23:16 |
| 36 | One character. Three tokens | 0:50 | 24:06 |
| 37 | Tool call. Append. Repeat | 0:55 | 25:01 |
| 38 | The answer comes home | 0:20 | 25:21 |
| 39 | Count. Route. Reuse | 0:40 | 26:01 |
| 40 | Alessandro Vozza — introduction | 0:20 | 26:21 |
| 41 | Sources & assumptions — backup | — | — |

These are speaking budgets, not benchmark timings. If discussion runs long, skip slide 38 first (20 seconds), then 7 (35 seconds), then 30 (50 seconds). Slide 31 works with a one-sentence explanation of blocks. Preserve the opening questions and the gateway, routing, prefill/decode, capacity and agent-loop arguments.

## The opening questions

Get your own hand up on slide 2. On slide 3 say **“keep them up”**; let the audience see the change. Slide 4 calibrates the room. Many hands: move briskly through the harness and spend time on policy and serving. Few hands: slow down on the context breakdown. No hands: “Good — then nothing in this talk has hurt you yet.”

## Opening the request: slides 5–13

**5 — terminal, now a two-click quiz.** Ask “nine words — how many tokens?”, wait for shouts, then click to reveal **Twelve**. The question is `why did the nightly ETL job fail on deserialization?` — deliberately the same nine words and twelve tokens as the answer on slide 6, so the two slides can never contradict each other on stage. Twelve counts raw user text; the example chat template in `tokenizer-check.py` adds nine more, outside the headline.

**6 — token splits.** Walk the amber chips: 54 characters, 9 words, 12 tokens. `ETL` splits into ` E` and `TL`; `deserialization` into ` des` and `erialization`. Leading spaces can belong to tokens. These are measured splits.

**7 — the trade.** The 256 is byte values, not alphabet letters. Bytes express any text but create long sequences. Whole words need a policy for unseen words. Subwords offer a fixed vocabulary with byte fallback. Attention work can grow quadratically with sequence length; total serving cost has more moving parts.

**8 — learned compression.** “Start with bytes, merge frequent pairs. GPU has an entry; Kubernetes does not. Nothing here understands the text: this is compression fitted to a corpus.” Vocabulary size includes special tokens; it is not an exact merge count.

**9 — language.** Read the Serbian sentence aloud before showing its count. These exact sentences produce 12, 20 and 23 tokens. Cyrillic uses 1.92 times the English tokens **in this example**. Measure workloads in users’ languages. Do not generalize that ratio to all Serbian text, tokenizers, context capacity, latency or compute.

**10 — route map.** Point to gateway, prefill and decode; do not narrate all eight stops. Notice the return arrow: an agent can go around again.

**12 — context.** “Instructions, tool schemas, files and history fill the request. Your twelve tokens are the tiny part.” The **illustrative** breakdown is 10,200 + 9,600 + 8,400 + 1,800 + 1,200 + 12 = **31,212 tokens**. The question is 0.0384%, rounded to 0.04%. Protocol/template overhead is omitted. Harnesses can trim, compact, retrieve, cache or reference context; not every system retransmits every byte unchanged. A model conditions on supplied context rather than remembering the previous HTTP call by itself.

**13 — ratio.** **31,212 ÷ 12 ≈ 2,601×**, rounded to the nearest whole number. Pause. This compares illustrative context to raw prompt, not every agent request.

## The Kubernetes spine: slides 15–22

**15 — objects.** Say the through-line once: “Gateway, HTTPRoute, InferencePool, Deployment. Inspect them, put them in git, review the diff.” InferencePool needs the extension, its controller and a compatible gateway. This diagram is not an installation guide.

**16 — protocols.** LLM traffic requests output; MCP invokes tools; A2A connects agents. Tools can change external state, making per-action policy valuable. agentgateway is the example. Other implementations have different feature sets; do not promise equivalent protocol support.

**17 — authorization.** “May this identity call this tool, with these claims, in this environment?” Distinguish search from deletion. The CEL-like snippet illustrates the decision; check actual field names. Filtering advertised tools reduces exposure but does not replace enforcing policy on calls.

**18 — identity.** Shared long-lived keys weaken attribution. Carry an appropriate human or workload identity, verify it, obtain scoped credentials where supported. JWT, OIDC, OAuth token exchange and SPIFFE are building blocks, not automatic end-to-end delegation.

**19 — two routes.** `/v1` illustrates model access and budget policy; `/mcp` illustrates tool authorization. Keep frontier-provider access intentional. Zero backend weight alone does not implement a separate explicit route. Both panels are **illustrative**, not deployable manifests. Validate actual policies and versions before an optional demonstration.

**21 — warm replicas.** “Same image, same weights. One replica already holds your reusable prefix. Pick a cold replica and repeat work.” The 900 ms versus 12 ms contrast is **illustrative**, not a benchmark or guaranteed cost ratio. A basic Service lacks inference-cache awareness; Kubernetes Service behavior is not universally literal round-robin.

**22 — endpoint picking.** Highlight backend kind and picker reference. Compatible pickers can consider load, cache state and prefix locality. Plugins, signals and metrics vary. A prefix-hit counter alone does not locate the cached blocks for an incoming request. Migration needs more than a one-line YAML edit: the extension, controller and picker must exist.

## Two bottlenecks: slides 24–27

**24 — prefill/decode.** Dense 70.6B model arithmetic: `2 × parameters × input tokens` is about **4.4 PFLOP** for this prefill; one decode step is about **141 GFLOP**. Both omit attention and other work. The equal **71 GB** bars model FP8 weight reads, not total measured traffic. “Long prefills can use compute. Low-batch dense decode often moves weights. First-token latency and streaming speed need different diagnostics.” Bottlenecks depend on context length, batches, hardware, kernels and parallelism.

**25 — 8.9 ms.** **71 GB ÷ 8 TB/s ≈ 8.9 ms** is an idealized batch-one weight-read lower bound. It ignores KV traffic, attention, communication, overhead and imperfect bandwidth utilization. About 113 steps/second is its reciprocal, **not observed throughput**. Batching amortizes weight reads; a batch of 64 does not necessarily take the same elapsed time as one request.

**26 — separate workers.** Prefill and decode can use different workers, with KV transferred between them. NIXL/RDMA is one illustrated path. Prefill still needs memory while building and transferring KV; “tiny KV” is a sizing contrast, not zero requirement.

**27 — adoption order.** Measure first; try cache-aware scheduling; disaggregate when workload and scale justify the transfer and complexity. Wide expert parallelism is a later option for appropriate MoE models. Project-reported speedups depend on workload. On small deployments, investigate batching and chunked prefill first. Defaults and flags vary by version.

## Inside the engine: slides 29–34

**29 — batching.** Finished sequences leave; waiting work can join the next scheduling step. Compare empty slots with refilled slots. Real schedulers still have queues and admission constraints. The drawing implies no universal throughput multiple or fixed scheduling frequency. Neighbors affect latency: measure representative concurrency.

**30 — paging.** Allocate KV blocks through a block table instead of reserving a giant contiguous allocation. Sixteen-token blocks are an example; sizes and sharing vary. Paging reduces fragmentation, not every kind of memory waste.

**31 — prefix reuse.** Matching cached blocks can avoid repeated prefill. One new block is a favorable illustration; tool results may add many. Route to reusable cache while considering load. Reuse within one replica can help without an advanced router. Keep stable prefix content stable; place volatile content later where semantics permit. The 900→12 ms contrast is illustrative.

**33 — capacity.** Reveal **10 → 17 → 35**. The graph assumes 110 GB of KV with BF16 weights, 180 GB with FP8 weights, then half the modeled bytes per token with FP8 KV. Allocations leave room for weights and overhead; they are assumptions, not guaranteed consequences of two flags. Quantization needs compatible hardware/engine/model support and quality evaluation. A full cache can constrain concurrency, but one metric cannot establish every bottleneck.

**34 — MoE.** State the architecture change: preceding math uses dense Llama 3.3 70B; the sparse grid is a separate MoE illustration. Fewer active experts can reduce weight traffic. Shared layers still participate; experts reside somewhere or must be transferred; routing adds communication. **8 of 256** does not mean total runtime is 8/256. MoE changes the workload rather than breaking a physical bound for the old one.

## The return trip: slides 36–39

**36 — the die.** “One character, four UTF-8 bytes, three Llama 3 tokens. None of the fragments is independently valid UTF-8. Assemble them before showing the character.” Fragments: `f0 9f`, `8e`, `b2`. Three generation steps do not imply a fixed 27 ms visible delay. Token emission and displayed-character timing differ; measure the user-facing stream too.

**37 — agent loop.** A tool request returns; the harness executes an allowed call, appends its result and requests another model step. Growth bars are illustrative. Fixed growth and fully charged untrimmed context can make cumulative input volume quadratic in turn count. Caching, compaction, retrieval and variable turns change that result. Spoken takeaway: **“Each turn can carry more context than the last.”**

**38 — callback.** “At the start, you asked why the ETL job failed. Here is the answer after looking at the evidence.” Serbian output and round-trip counts are an **illustrative trace**, not an execution log. Do not derive an 11-second latency from ideal bandwidth arithmetic.

**39 — close.** “Count your context. Route to useful cached state. Keep the engine busy. Inspect those before reaching for more hardware.” Advance to the introduction slide and leave it visible for questions.

**40 — introduction.** “I’m Alessandro Vozza, from Lovelace Engineering in Amsterdam, and a Golden Kubestronaut. I work on sovereign AI infrastructure. Lovelace Engineering consults for VOLT Datacenters. Scan these codes for my LinkedIn or more talks — I’d love to hear what you’re building.” Keep this to 20 seconds; email, LinkedIn and more talks are linked on the slide.

## Numbers you can reproduce

`python3 tokenizer-check.py` ran successfully during this revision. It rebuilds the tokenizer from the referenced vocabulary mirror, checks **128,256 entries** and round-trip decoding. The checks do not independently prove the mirror identical to every Llama release; counts describe this script and vocabulary.

| Quantity | Reproduction / assumption |
|---|---|
| Raw question | 7 whitespace-separated words; 9 tokens |
| Question with script’s chat wrapper | 18 tokens, including 9 wrapper tokens |
| Answer sentence | 54 characters / 9 words / 12 tokens |
| GPU / agentgateway / Kubernetes / vLLM | 1 / 2 / 2 / 3 tokens |
| English / Serbian Latin / Serbian Cyrillic | 12 / 20 / 23; 23 ÷ 12 ≈ 1.92, for the displayed examples |
| 🎲 | 4 UTF-8 bytes; 3 tokens; `f0 9f` + `8e` + `b2` |
| Context | 10,200 + 9,600 + 8,400 + 1,800 + 1,200 + 12 = 31,212; illustrative; wrapper omitted |
| Amplification | 31,212 ÷ 12 ≈ 2,601×, rounded |
| Prefill estimate | 2 × 70.6e9 × 31,212 ≈ 4.4e15 FLOP; attention/other work omitted |
| Decode estimate | 2 × 70.6e9 ≈ 141e9 FLOP per step; same omissions |
| Ideal weight-read time | 71e9 bytes ÷ 8e12 bytes/s ≈ 8.9 ms; not measured latency |
| BF16 KV | 2 × 80 × 8 × 128 × 2 = 327,680 bytes/token = **320 KiB/token** |
| FP8 KV | 163,840 bytes/token = **160 KiB/token**, before extra overhead |
| Session estimates | floor(110e9 ÷ 31,212 ÷ 327,680) = 10; floor(180e9 ÷ 31,212 ÷ 327,680) = 17; floor(180e9 ÷ 31,212 ÷ 163,840) = 35 |
| Hardware assumptions | 288 GB HBM and 8 TB/s for the stated B300 example; decimal GB and binary KiB are distinguished |

Context breakdowns, growth curves, cache-latency contrasts, capacity allocations and configuration are illustrative. Project performance reports and vendor peaks are neither independent benchmarks nor service-level guarantees. Consult the links on slide 41 for original sources.

## Expected questions

1. **“What does a box cost?”** Discuss measured utilization and workload, then check current prices. Avoid unsourced per-million-token cost figures from simplified arithmetic.
2. **“Do I need this for a small model?”** Start simple and measure. More replicas make locality and routing worth examining; complexity must earn its keep.
3. **“Which gateway?”** Choose for supported APIs, protocols and operational fit. Check current compatibility rather than promising equivalent features.
4. **“Is temperature zero deterministic?”** Not necessarily; execution and numerical differences can change outputs. Check the actual stack’s guarantees.
5. **“Frontier API or self-host?”** Compare per workload: quality, volume, utilization, latency and operations.
6. **“How do I see my context?”** Use available harness tracing/export or instrument the client. Count with the correct tokenizer and real wrapper.

## Programme context

Original programme notes list related sessions by Stefan Đokić (agents on .NET), Stefan Gavrilović (AI in a bank), Spirovski & Stefanovski (API security), and Dušan Stanojević (reliability). Check the final programme before naming an overlap on stage. These remain delivery cues rather than slide claims.
