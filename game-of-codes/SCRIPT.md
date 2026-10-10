# Life of a token — delivery script

**Alessandro Vozza · Lovelace Engineering**

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
| 5 | Seven words. Nine tokens | 0:35 | 1:33 |
| 6 | Tokens aren’t words | 0:55 | 2:28 |
| 7 | Bytes. Words. The compromise | 0:35 | 3:03 |
| 8 | Compression, learned | 0:50 | 3:53 |
| 9 | Same meaning. Different bill | 0:55 | 4:48 |
| 10 | Down to silicon. Back again | 0:35 | 5:23 |
| 11 | The prompt you never wrote | 0:08 | 5:31 |
| 12 | Your prompt is 0.03% | 1:05 | 6:36 |
| 13 | ≈3,468× | 0:20 | 6:56 |
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

## Word-for-word script

These are the exact spoken lines shown in each slide’s speaker notes. Delivery cues and supporting explanations follow separately. Slide 41 is backup; speak its line only when opening that slide for questions.

**1.** Everyone here called a model this week. Many of you have an agent running right now. Today I want to follow one request after you press Enter: through the software, down to the silicon, and back again. Our question is simple: where do the time, memory and money go after an agent receives a tiny request? One example will carry us through the whole stack.

**2.** Hands up if you use AI, any day of the week.

**3.** Keep your hand up if you use it every day, as part of how you actually work.

**4.** Now keep it up if you run a fleet of agents: they keep working while you do something else. Look around. This talk follows what all those agents ask the infrastructure to do.

**5.** Here is our starting point: seven words typed by a human, represented by nine tokens. We will follow this request from the harness to the GPU and back. On screen, the request looks almost free. The harness may wrap it in instructions, tools, files and history. These nine tokens are only our starting point. First, what exactly is a token?

**6.** This example answer has fifty-four characters, nine words and twelve tokens. Those are three different counts. The tokenizer keeps common pieces together: “failed” stays whole, while “ETL” and “deserialization” split. A token is a learned piece of text, sometimes including a leading space. Notice the leading spaces on several chips. A space can be part of a token, so the count belongs to this exact string and tokenizer. That is why words and tokens are not interchangeable.

**7.** Why split text at all? Starting with individual bytes gives us only two hundred and fifty-six possible byte values, but very long sequences. Whole words give shorter sequences, but new names need a way through. Subword tokens are the compromise: a fixed vocabulary that can still represent unfamiliar text. Longer byte sequences give the model more positions to process. A word-only vocabulary struggles with new product names and code identifiers. The middle lane keeps common pieces and still spells the rest.

**8.** Byte-pair encoding starts with bytes and repeatedly merges frequent neighboring pieces. These examples come from the tokenizer used in this talk: “GPU” gets one token; “Kubernetes” gets two; “vLLM” gets three. The vocabulary reflects patterns in its training text. It does not understand the words. These rows show storage decisions, not definitions. Another tokenizer may split the same word differently. Measure with the tokenizer behind the model you actually serve.

**9.** Listen to the same thought in Serbian: “Сваки позив агента завршава као токени на неком GPU-у.” Here, the English sentence takes twelve tokens, Serbian in Latin script takes twenty, and Serbian in Cyrillic takes twenty-three. This particular Cyrillic example uses about ninety-two percent more tokens than the English one. Token budgets and billing can therefore differ by language; measure the text your users actually send. The Latin and Cyrillic versions both express ordinary thoughts, yet occupy different amounts of context here. I am not claiming the same ratio for latency. English-only budget tests can misrepresent another language.

**10.** Here is our route: the request travels down through the harness, gateway, routing layer and model engine, then streams back. Watch the loop at the top. An agent can call a tool, add its result and make another model request. The colors change where the answer starts home. We will focus on the gateway, the replica choice, and the engine where prefill and decode use the GPU differently.

**11.** First, let us open the request and see the prompt you never wrote.

**12.** Our nine-token question is the red sliver. In this illustrative request, instructions, tool descriptions, files and conversation history bring the total to thirty-one thousand, two hundred and nine tokens. The harness decides what context to supply; different harnesses trim, retrieve or compact it in different ways. The model sees the context it receives on this call. The diagram assigns ten thousand two hundred tokens to tool schemas and nine thousand six hundred to files. These are illustrative amounts. Export a real request from your harness to learn what it sends.

**13.** The full request is about three thousand, four hundred and sixty-eight times larger than the nine tokens you typed. Your question is just 0.03 percent of this example context. Now follow where it goes.

**14.** Now that the request is assembled, it reaches the boundary where identity and policy matter.

**15.** This part of the stack can be represented by four Kubernetes objects: a Gateway, an HTTPRoute, an InferencePool and a Deployment. That lets you inspect routing and serving configuration in the cluster and review changes in Git. The InferencePool requires its extension and a compatible gateway. Follow the objects in order: Gateway receives traffic, HTTPRoute chooses a target, InferencePool adds an inference-aware destination, and Deployment runs serving pods. This is an architecture map, not an installation manifest.

**16.** An agent sends three kinds of traffic: model requests, tool calls over MCP, and messages to other agents over A2A. A tool call can change a real system. That is why the gateway must understand more than the model endpoint; it needs a place to check each action. The lanes have different consequences. A completion generates text; a tool may read a document or delete a record. Policy has to follow the action the agent requests.

**17.** For a tool call, the question is specific: may this identity invoke this tool under these conditions? In the example, document search is allowed for the right group, while customer deletion is denied. The rule is checked when the call happens, even if the agent discovered the tool earlier. Hiding a dangerous tool during discovery helps, but it does not enforce authorization. The gateway still checks the actual call against current identity and claims.

**18.** To make that decision useful, carry identity through the request. If every user shares one long-lived key, the log only tells you which agent ran. Verify the caller at the gateway and, where the tool supports it, pass a scoped credential so the action can be attributed to the right person or workload. After an incident, you need to trace who initiated the chain and which workload called the tool. Credential exchange needs support at both ends; the diagram shows the intended identity path.

**19.** The left route illustrates model access: verify identity, set a token budget and use our own inference pool as the ordinary destination. An external model is shown with zero weight, so it receives no ordinary weighted traffic. Using it deliberately needs an explicit routing rule in the deployed configuration. The right route illustrates per-tool authorization for MCP calls. Together, those controls can feed one audit trail; this sketch does not show the logging setup. The budget limits an agent loop that could spend tokens without visibly failing. The MCP rule controls its next action. Both policies need to be enforced at the gateway.

**20.** The request has passed the gateway. Next question: which GPU should answer it?

**21.** These replicas run the same model, but one may already hold a reusable prefix in its KV cache. A basic Kubernetes Service has no knowledge of that cache. If it sends the request to a cold replica, the engine may repeat prefill work. The latency numbers here illustrate the potential difference; the actual result depends on the request and the cache. In a continuing conversation, one replica may hold the processed prefix. A request sent there can focus on the new suffix. Equal model weights therefore do not mean equal work for every replica.

**22.** This is where the InferencePool comes in. The HTTPRoute points to the pool, and an endpoint picker can choose a compatible replica using signals such as load and cache locality. The endpoint can stay the same for callers. Deploying this also requires the extension, controller and picker; the highlighted line is the routing change, not the whole installation. The endpoint picker may consider queueing, load and cache locality. Available signals depend on the implementation. Validate the chosen provider and its routing behavior before treating this as a production change.

**23.** We have reached inference. Inside one GPU, the request encounters two very different bottlenecks.

**24.** Prefill processes the long input and can be dominated by arithmetic. Decode produces one new token at a time and, at low batch sizes, often spends much of its time moving model weights. In this simplified dense-model calculation, the weight-read bars are both seventy-one gigabytes, while the arithmetic bars differ by roughly thirty-one thousand times. Real bottlenecks vary with batching, context length and hardware. For this thirty-one-thousand-token input, the simplified dense-model estimate is about four point four petaflops of prefill arithmetic. One decode step is about one hundred and forty-one gigaflops. These are estimates, not measured GPU traces.

**25.** Seventy-one gigabytes of weights divided by eight terabytes per second of peak memory bandwidth is about eight point nine milliseconds. That is an ideal lower bound for one weight read, not measured time per token. KV reads, kernels, communication and imperfect utilization all add time. Batching can share the weight read across requests. That division uses the model’s weight size and advertised peak bandwidth. It omits everything else the engine does. Its reciprocal is a simplified ceiling, not a throughput promise; benchmark the deployment.

**26.** One option at scale is to use different workers for prefill and decode. Prefill workers emphasize compute; decode workers emphasize bandwidth and room for long-lived KV state. Prefill still needs memory while it builds that state, and transferring KV between workers has a cost. Specialize only when measurements justify that cost. The drawing separates compute-heavy prefill from memory-heavy decode, then transfers KV state. That transfer adds cost and complexity. Small deployments may benefit more from better scheduling on shared workers.

**27.** Here is what that specialized setup can look like: separate prefill and decode deployments, KV transfer between them, and one pool in front. The numbers are illustrative configuration, not a recipe. The adoption order is the real point: measure first, use cache-aware routing, and disaggregate only when the workload is large enough to benefit. The replica counts are illustrations, not target ratios. Measure prefix reuse and queues first. Add separate worker pools only when those measurements show a benefit that exceeds transfer cost.

**28.** Now let us look inside the engine that actually generates the tokens.

**29.** Continuous batching revisits the batch at each scheduling step. When one sequence finishes, the scheduler can admit another instead of leaving a slot idle until the longest request ends. That keeps the GPU busier, although admission limits and competing requests still affect latency. On the left, finished sequences leave capacity idle until the longest member ends. On the right, new work fills slots at later steps. Real schedulers still enforce memory and admission limits.

**30.** The KV cache also needs memory management. PagedAttention allocates it in blocks, using a block table instead of reserving one huge contiguous region for a sequence. That reduces fragmentation and can let matching prefixes share physical blocks. Sixteen-token blocks are an example, not a universal setting. A block table maps logical sequence positions to physical cache blocks. The engine allocates as a sequence grows. Matching content and cache machinery are still required to share a prefix.

**31.** If a new request begins with exactly the same prefix, cached KV blocks can avoid recomputing that part of prefill. The example latency contrast is illustrative. Reuse only helps when the cached blocks are accessible to the replica serving this request, so the cache and the routing decision belong in the same design. Stable system instructions and tool schemas can make useful cached prefixes. New tool results still need processing. The routing choice must balance locality against load on each replica.

**32.** That leads to a practical capacity question: how much of the GPU memory is left for active conversations?

**33.** Weights occupy memory before the first request arrives. KV cache grows with the tokens in active requests. In this simplified capacity model, quantizing weights changes the estimate from ten to seventeen concurrent sessions; quantizing KV as well raises it to thirty-five. Those are modeled capacities, not promised throughput. Check quality, runtime support and memory overhead on your own stack. The bars show an assumed KV budget rising from one hundred and ten to one hundred and eighty gigabytes as weights shrink. Smaller KV entries then hold more tokens. Real capacity moves with overhead and output length.

**34.** The earlier arithmetic described a dense model, where all its layers participate in each token. This diagram introduces a different architecture: a mixture of experts. A router selects some experts per token, so fewer expert weights may need to be read for that step. Shared layers, stored experts and communication still cost resources. Sparse activation changes the workload; it does not remove the hardware limit. Only selected experts are active in the sparse grid, but shared layers still run. Unselected experts still occupy memory somewhere. Sparse activation trades one bottleneck against storage and communication elsewhere.

**35.** Now the tokens stream back, and the agent loop closes.

**36.** Here is a detail built for this room. The dice character is four UTF-eight bytes, and this tokenizer represents it with three tokens. The first fragments cannot be displayed as a complete character; the server has to assemble them. That means token arrival and visible character arrival are different moments in a streamed response. Those three tokens are byte fragments, not three visible dice. The server buffers incomplete UTF-eight until it can display a character. User-visible streaming deserves its own latency measurement.

**37.** Sometimes the model returns a tool request instead of the final answer. The harness calls the tool, appends the result and asks the model again. These bars sketch growth across turns; the separate ETL trace takes five round trips. Later turns can carry more context, although caching, retrieval and compaction change how much work is repeated. Each loop can add tool output and history. Fully resent, growing context can become costly across turns. Prefix reuse, trimming and retrieval change that accounting.

**38.** Here is the answer in Serbian. In English: an invalid schema cache caused the ETL failure. The illustrated request carries about thirty-one thousand input tokens; the agent example takes five round trips.

**39.** If you take three things away, make them these: count the context your agent sends, route requests toward reusable state, and keep the engine busy with good batching. Measure those before you size more hardware. Those checks map to the journey: the harness decides context, routing decides location, and the engine shares GPU work. Make those choices visible before buying more capacity. Thank you.

**40.** I am Alessandro Vozza, from Lovelace Engineering in Amsterdam, and a Golden Kubestronaut. I work on sovereign AI infrastructure. Lovelace Engineering consults for VOLT Datacenters. Scan the codes for my LinkedIn profile or more talks. I would love to hear what you are building.

**41.** These are the sources and assumptions behind the examples. The tokenizer counts are reproducible; the configuration and performance comparisons are illustrative. I am happy to open any of these links or walk through a number.

## The opening questions

Get your own hand up on slide 2. On slide 3 say **“keep them up”**; let the audience see the change. Slide 4 calibrates the room. Many hands: move briskly through the harness and spend time on policy and serving. Few hands: slow down on the context breakdown. No hands: “Good — then nothing in this talk has hurt you yet.”

## Opening the request: slides 5–13

**5 — terminal.** “Seven words. Nine tokens. Follow what the harness does with them, all the way to the GPU and back.” Nine counts raw user text. The example chat template in `tokenizer-check.py` adds another nine tokens; those are outside the headline.

**6 — token splits.** Walk the amber chips: 54 characters, 9 words, 12 tokens. `ETL` splits into ` E` and `TL`; `deserialization` into ` des` and `erialization`. Leading spaces can belong to tokens. These are measured splits.

**7 — the trade.** The 256 is byte values, not alphabet letters. Bytes express any text but create long sequences. Whole words need a policy for unseen words. Subwords offer a fixed vocabulary with byte fallback. Attention work can grow quadratically with sequence length; total serving cost has more moving parts.

**8 — learned compression.** “Start with bytes, merge frequent pairs. GPU has an entry; Kubernetes does not. Nothing here understands the text: this is compression fitted to a corpus.” Vocabulary size includes special tokens; it is not an exact merge count.

**9 — language.** Read the Serbian sentence aloud before showing its count. These exact sentences produce 12, 20 and 23 tokens. Cyrillic uses 1.92 times the English tokens **in this example**. Measure workloads in users’ languages. Do not generalize that ratio to all Serbian text, tokenizers, context capacity, latency or compute.

**10 — route map.** Point to gateway, prefill and decode; do not narrate all eight stops. Notice the return arrow: an agent can go around again.

**12 — context.** “Instructions, tool schemas, files and history fill the request. Your nine tokens are the tiny part.” The **illustrative** breakdown is 10,200 + 9,600 + 8,400 + 1,800 + 1,200 + 9 = **31,209 tokens**. The question is 0.0288%, rounded to 0.03%. Protocol/template overhead is omitted. Harnesses can trim, compact, retrieve, cache or reference context; not every system retransmits every byte unchanged. A model conditions on supplied context rather than remembering the previous HTTP call by itself.

**13 — ratio.** **31,209 ÷ 9 ≈ 3,468×**, rounded to the nearest whole number. Pause. This compares illustrative context to raw prompt, not every agent request.

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

**40 — introduction.** Keep this to 20 seconds; email, LinkedIn and more talks are linked on the slide. Read the exact line in the word-for-word section above.

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
| Context | 10,200 + 9,600 + 8,400 + 1,800 + 1,200 + 9 = 31,209; illustrative; wrapper omitted |
| Amplification | 31,209 ÷ 9 ≈ 3,468×, rounded |
| Prefill estimate | 2 × 70.6e9 × 31,209 ≈ 4.4e15 FLOP; attention/other work omitted |
| Decode estimate | 2 × 70.6e9 ≈ 141e9 FLOP per step; same omissions |
| Ideal weight-read time | 71e9 bytes ÷ 8e12 bytes/s ≈ 8.9 ms; not measured latency |
| BF16 KV | 2 × 80 × 8 × 128 × 2 = 327,680 bytes/token = **320 KiB/token** |
| FP8 KV | 163,840 bytes/token = **160 KiB/token**, before extra overhead |
| Session estimates | floor(110e9 ÷ 31,209 ÷ 327,680) = 10; floor(180e9 ÷ 31,209 ÷ 327,680) = 17; floor(180e9 ÷ 31,209 ÷ 163,840) = 35 |
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
