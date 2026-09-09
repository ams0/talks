# Beyond the Clouds — technical cut · delivery script

Cloud Native Groningen · 9 September 2026 · 45 minutes hard stop: **≈33 min talk, 10–12 min questions**. Engineering audience.
Same argument as the leadership cut in `../beyond-the-clouds/`, with sections 01–02 compressed and
section 03 rebuilt to go down the stack one layer at a time, with YAML on the screen.
Quoted lines are verbatim — say those. Everything else is a cue.

**What changed from the leadership deck.** Seven slides are gone (the Monty Python title card, the
proverb, the six-laws table, the framework document card, the politicians' quote wall, the five-minute
exercise and the conversation starters). Nine are new or rebuilt: the reference architecture (23), the
request path (24), the Gateway API Inference Extension (25), agentgateway (26), llm-d (27), the HBM
budget (28), the optimisation knobs (29), HAMi (36), the one-box K3s build (40), plus a second sources
slide (50).

**The deck now opens on the title slide.** There is no warm-up card: whatever is on screen as the room
comes in is the first thing you say. Have it up early, and start on your own beat rather than on the
slide's.

**Slides that build.** 15, 35, 41, 42, 43 and 46 reveal one item per click. Right arrow (or space, or
click) brings out the next item, then moves on; left arrow steps back. **Down/Up jump whole slides.**
The technical slides are deliberately static: a code panel that appears in pieces is worse than one you
can point at.

**Timing.** Delivered in full the deck runs **≈33 min**. The technical middle (23–30) is twelve of those
minutes and is where the room will try to pull you into detail — answer the factual ones in one
sentence and park the rest for the end.

**Cut order if you are behind: 43 → 39 → 22 → 18 → 30 → 7.** Never cut 24, 28, 29 or 42. If you
are badly behind at slide 32, jump straight to 36 with "Europe is building the bottom layer; I'll skip
the megawatts" — the technical room already believes the supply side is arriving.

**The morning of the talk.** agentgateway and llm-d both ship monthly. The versions on 25, 26, 27 and 51
were checked on 8 September; a thirty-second look at the release pages is cheap insurance against the
one person in the room who ran the newer one last night.

---

## 00 Opening — 1 min (slides 1–4)

**1 · Title.** Up as the room comes in. One line when you actually begin. "I build AI infrastructure
for a living. I want to argue that the most important AI decision you'll make this year isn't which
model — it's whose jurisdiction you run it in. And then I want to show you the stack that lets you
choose."

**2 · How this session works.** Twenty seconds. "Thirty-three minutes, then questions. Interrupt me on
facts — a wrong flag, a stale version — right away. Save the arguments for the end; there's a slide for
that." Say the hard-stop clock time out loud.

**3 · Ninety days.** Ask it. *"Hands up if you could move your AI workloads to another provider in
ninety days."* Wait. *"Keep them up if you've tested it."* Engineers are more honest here than
directors — expect fewer hands on the first question and almost none on the second. "Anywhere else
we'd call that an untested DR plan."

**4 · Thesis.** Land the word **jurisdiction**. "Somebody signed off on a credit card and a rate
limit. Those turned out to be the same decision."

## 01 The ground moved — 5 min (slides 5–13)

Frame it: *risk register update, not a debate.* Faster than the leadership cut — this room does not
need convincing that the legal ground is soft; it needs the dates.

**6 · Where you actually are.** Two numbers, 30 seconds. 29% to 15%, flat for three years while the
market grew sixfold. **The plateau is the point.**

**7 · Three companies, seventy percent.** Fifteen seconds, point at the 2%. "That is the European
alternative. Which is why this talk is about control planes, not migrations."

**8 · Microsoft France, under oath.** Strongest slide, because it is not your claim. Be scrupulously
fair. "He's describing the structure more honestly than most of our risk registers do."

**9 · Four dates.** Left to right, 60 seconds. The arc: admitted → responded → the ground moved
anyway. "Three times in ten years. If your architecture assumes it survives a fourth, that's a bet."

**10 · AI Act deadline moved.** "Deferred is not cancelled. Paperwork got eighteen months. The
architecture got nothing, because the architecture takes longer."

**11 · The rulebook (gantt).** Do not read it. Red line is today; everything left of it binds you; the
black pin on the Data Act row is the payload: **from 12 January 2027 your provider may not charge you
to leave.** Egress fees are the one lock-in this room has personally paid.

**12–13 · The numbers.** Top one and bottom one. 93% repatriating or evaluating; 41% naming public
cloud as primary inference, **down from 56% in a year**. Concede survey bias immediately if challenged.

## 02 Sovereignty is a dial — 4 min (slides 14–18)

**15 · SEAL 0 to 4 (builds).** One rung per click; read 0, 2 and 3 only. **The gap between 2 and 3 is
the whole talk**: SEAL-2 is what a contract buys and it fails when a foreign court instructs the
parent; SEAL-3 is what an architecture buys. "No hyperscaler bid at SEAL-3." If challenged that SEAL-4
is unachievable, agree at once.

**16 · Four questions, per workload.** "Most organisations have one AI policy and forty AI workloads."

**17 · What changes.** Read the last line of each column. "The right-hand column is not better. It's
different, and it's yours."

**18 · Who decides the roadmap.** *Cut if short.* America owns the platform, China forked it, Europe is
betting you can stay in the commons and still have a vote. This is the open-source governance argument
and engineers care about it more than directors did.

## 03 The stack is ready — 12 min (slides 19–30)

**Change your voice.** Sections 01–02 were risk; this is the part they came for. Twelve minutes for
23–29. Point, don't read; every code panel has its source in the footer.

**20 · Boring is the achievement.** 66% serve inference on Kubernetes; 31 conformant platforms; llm-d
donated by the people selling the alternative. "The reason I can make this argument in 2026 and
couldn't in 2023 is that the hard engineering got commoditised — by the people selling the alternative.
That's the window."

**21 · "Open weights" ≠ open model.** The honesty beat. "You can download the weights, you cannot audit
what went into them, and the licence still says what you may build. Portable — not accountable." If
challenged that tier 3 is behind the frontier, agree without hedging.

**22 · KubeCon sessions.** Fifteen seconds. *Cut if short.*

**23 · Reference architecture ★rebuilt.** Sixty seconds, the map for the next seven slides. Eight layers;
point at the **three new since 2024**: the agent gateway (who may call what), inference routing (which
replica answers), fractional GPU scheduling (how much of the card). Then the data layer (the moat) and
the bottom layer (cannot download). "Each of those three was a proprietary advantage eighteen months ago."

**24 · One request, four hops ★new.** Ninety seconds. The technical spine. "Hop two decides *whether*
a request may happen and what it may touch. Hop three decides *where* it runs. Own those two and it
does not matter whether hop four is a B300 in Amsterdam or a frontier API in Virginia — the caller
can't tell, and neither can the audit log." Point at the signals under hop three: that list is why a
Service is the wrong abstraction. If asked "why not Istio": Istio implements the extension too; the
point is the API, not the proxy.

**25 · Gateway API Inference Extension ★new.** Two minutes. The YAML is boring on purpose: an HTTPRoute
whose backend is a pool instead of a Service — that is the whole migration for the app team. "Two
replicas with the same weights are not interchangeable — one of them already has your prefix in its KV
cache. Round-robin can't know that. The endpoint picker can, because vLLM tells it." Metric names if
asked: `vllm:num_requests_waiting`, `vllm:gpu_cache_usage_perc`, `vllm:lora_requests_info`. Five
implementations, same YAML: Envoy Gateway, kgateway, Istio, agentgateway, GKE. On the v1.6 move of the
EPP into llm-d: "healthier than it sounds — the SIG owns the conformance suite."

**26 · agentgateway ★new.** Ninety seconds. "Everyone here has a gateway in front of chat completions.
Almost nobody has one in front of the tool calls — and the tool calls are where an agent does damage.
MCP authorisation at the tool level is the control that did not exist a year ago." The second backend
with `weight: 0` is "rent, knowingly" as YAML. **Say that the config block is illustrative** — field
names move between minors; the reference docs are the truth. If asked "why not Envoy AI Gateway": also
fine, also implements the extension. Pick one that speaks Gateway API.

**27 · llm-d ★new.** Two minutes. "vLLM plus the fleet problems." Every number is the project's own —
say so, treat them as upper bounds. Path 1 is where most of this room should start and stop; path 2
pays only above a size; path 3 is MoE at scale. Operational gotcha worth saying: CUDA 13 since v0.7
means driver 580 or newer.

**28 · HBM is the budget ★new.** Two minutes, **the slide engineers photograph.** The bars are
arithmetic, not benchmarks. "Weights are rent — you pay it per replica whether anyone is talking to the
model or not. The KV cache is the inventory you actually sell. So the interesting effect of quantisation
isn't that the model is smaller — it's that the same card now holds three times as many conversations."
Worked numbers if asked: Llama 70B is 163,840 KV values per token, 320 KB in BF16, 160 KB in FP8; at 8k
context that is ~40 sessions per B300 in the top row and ~140 in the third. DeepSeek's MLA is ~70 KB per
token — a 671B model with a *smaller* per-token cache than a 70B dense one — so one 8×B300 box holds it
with 1.3 TB spare. On FP8 KV quality: the vLLM team measured at most 1–2 points on reasoning; "measure
it on your evals."

**29 · One 8×B300 box, K3s ★new.** Two minutes; slow down on step four. "K3s is right here for the same
reason it's wrong for a datacentre: one binary, SQLite instead of etcd, containerd embedded. On one box
that is exactly the amount of Kubernetes you need. The point isn't the box — once the workload runs
behind a Gateway API route here, moving it to a European neocloud is a kubeconfig change." Step 4 is the
memory slide in flags: 70B FP8 at TP 4 leaves ~900 GB of KV across four cards. The last line is the
punchline: half the node is spare — two NVFP4 DeepSeek replicas, or a nightly eval fleet. If asked about
power: 14 kW per box, 56 kW per rack of four, nothing on this slide fits in an office — that is why
section 04 is about megawatts.

**30 · The knobs ★new.** Ninety seconds; **do not read the table.** First row and last row. "The first
row is free and closes most tickets. FP8 weights and FP8 KV are the two flags from the memory slide.
Four-bit is where you start trading accuracy for money and need your own evals. And the bottom row is
what a hyperscaler's serving team was doing for you — now a Helm chart, still their job's worth of
complexity." *Cut if short* — 28 and 29 carry the point on their own.

## 04 The bottom layer — 2 min (slides 31–35)

**31 · Divider.** Register change. You have just spent twelve minutes in HBM budgets and Helm charts;
drop the numbers and zoom out to the floor all of it stands on.

**32–35 · The build-out.** Ninety seconds total. "The bottom bar is live this month, twenty kilometres
from here. The constraint isn't chips or capital — it's a grid connection." **Disclose the VOLT
relationship plainly.** Then: "Every AI strategy in this country eventually becomes an energy strategy."

## 05 What the keynote leaves out — 7 min (slides 36–43)

Credibility section. Do not rush, do not soften.

**37 · Four failure modes (builds).** "I've watched two teams fight over eight GPUs for six weeks. No
technology fixed it. A quota policy and one uncomfortable meeting fixed it." Then: "The technical half
is the next slide."

**38 · HAMi ★new.** Ninety seconds. "Kubernetes hands out GPUs as whole integers. An embedding model
that needs 20 gigabytes gets a 288-gigabyte card and the other team gets nothing. HAMi lets the pod ask
for 24 gigabytes and 15 per cent of the SMs, and enforces it in the CUDA layer. The fight goes away
because the scarcity was mostly fake." Caveats to volunteer: software isolation is a trust boundary
inside one organisation, not between hostile tenants — MIG or separate nodes for that. If asked HAMi or
DRA: "DRA is the API, HAMi is the policy." The seven non-NVIDIA vendors are the sovereignty point.

**39 · Open source is the floor.** *Cut if short.* "If you adopt an open stack and fund none of it, you
haven't become sovereign — you've moved your dependency somewhere with no support contract." The ask:
name the dependencies you could not replace in a quarter, budget line against each.

**40–41 · Economics.** Same H100: $0.21 to $15.25 per million output tokens. Give permission not to
self-host: "€4,000 a month and spiky is a hobby. Come back at €40,000 and flat."

**42 · Self-host / federate / rent (builds).** **Never cut.** Row two: "You don't have to leave the
hyperscalers to stop being captured by them. You have to own the layer where the decisions are made."
For this room, "the layer" now has a name: hops two and three.

**43 · People (builds).** *Cut first.* "Every infrastructure question in this talk is a hiring question
in disguise."

## 06 Close — 2 min (slides 44–46)

**44 · Ninety days, four moves (builds).** Slow down. Inventory → gateway in front (model calls *and*
tool calls) → prove portability once, behind the same route → SEAL level in the next procurement. "None
of these need a business case. The first is a spreadsheet, and I'd bet nobody here can produce it today."

**45 · "The clouds aren't going anywhere. Your autonomy shouldn't live there."** Pause. Do not fill it.

**46 · Sovereignty is not a product. It's a practice.** Forty seconds, the three middle lines slowly.
"Landlord model" is the line that lands. Then stop, advance, and let them start.

## 07 Questions — 10–12 min (slides 47–49)

**47 · Five things I believe (builds).** Leave it up. "Pick a number and take it apart." If the room is
quiet, open #4 yourself — who has tried to hire a platform engineer this year. With engineers, expect
the pushback on #1 (slide 18 is your answer) and a detailed one on the HBM arithmetic — welcome it, the
numbers are on 28 and the sources on 50.

**48 · ChemAI card.** Fifteen seconds, then stop talking and let them photograph it.

**49 · Close.** Who I am, the VOLT disclosure one last time, the deck URL. Fifteen seconds.

**50–51 · Sources.** Backup. 50 is the argument, 51 is the stack. Only open if a number is challenged —
then find the line and read it.
