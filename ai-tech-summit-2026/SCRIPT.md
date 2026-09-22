# Beyond the Clouds — Skopje · delivery script

AI Tech Summit „Filip Avramchev“ 2026 · National Opera & Ballet, Skopje · **Wednesday 23 September 2026**
Main Stage · **11:45–12:15, 30 minutes, then lunch.** Listed as a keynote, tagged #Sovereign AI.
Preceded at 11:25 by the 20-minute panel *Sovereign AI & the Infrastructure Race* — **three panellists**:
Koen van den Berg (NVIDIA), you, and Slobodan Đinović (Founder & CEO, Orion Telekom), who then has his own
#Sovereign AI keynote at 14:15. Day one had NVIDIA's keynote *From Megawatts to Intelligence: Building the AI
Factory* at 12:15 — the room has already been sold the factory, including its power and cooling layers.

**The panel's four published questions** (deconflict with them, see below): 1. What does it take to go from the
idea of an AI data center to a fully operational one, and where do projects get stuck? 2. As AI demands more
electricity, how can data centers get more compute from the same power? 3. What changes for a country when it
develops local AI infrastructure — economically, technologically, strategically? 4. Can modern data centers be
built with minimal environmental impact?

Mixed audience: founders, executives, students, public sector, some engineers. Less technical than Groningen, more
than the ADA leadership day. Same argument as `../beyond-the-clouds/`, with the stack kept at the level of the
map and the request path (no YAML), and three slides rebuilt around what North Macedonia decided this summer.
Quoted lines are verbatim — say those. Everything else is a cue.

**Timing.** 33 slides, of which two are sources you only open if challenged. Delivered in full it runs
**≈22 min**, which leaves a real five-minute margin for a late start, a laugh, or one question. There is **no Q&A
block** — the provocations slide (30) stays up while you close and sends the argument to lunch. Say the lunch time
out loud on slide 1.

**Cut order if you are behind: 12 → 16 → 7 → 21 → 25.** Never cut 3, 8, 13, 18, 19, 26 or 29 — three of those
carry a reference to another session at this summit. If you are badly behind at slide 20, jump to 22 with
"Koen showed you the factory yesterday; here is the one number I'd add".

**Slides that build.** 10, 24, 26, 27 and 30 reveal one item per click. Right arrow (or space, or click) brings
out the next item, then moves on; left arrow steps back. **Down/Up jump whole slides.**

**The morning of the talk.** Two regional facts can move overnight: the status of the data-centre amendments
in parliament, and anything the ministry says about Vezilka from the stage on day one. Read the Macedonian
press at breakfast. The *Watts Matter* half of the listing has been removed — the session is now billed as
*Beyond the Clouds* alone, so the energy material in § 04 is a supporting act, not a promise. The agenda
prints your name as "Alessandro Stefouli-Vozza" — decide before you go on whether the title slide should match.

**Deconflict with your own panel.** Question 3 is slide 13 of this deck; question 1 is the material that used
to be slide 22, now cut for exactly that reason. Do not spend them on the panel: answer 1 in one sentence and
park 3 with "I have a slide on exactly that in fifteen minutes". Spend your panel time on 2 and 4, which are
operator questions you can answer better than either co-panellist, and which this deck barely touches.

**Competing session.** AI Labs, same 11:25–11:45 slot: *Sovereign by Design — three blueprints for AI that
can't leave the building* (Gjorgji Dimitrov, GAIA Technology Systems) — managed API, private endpoints,
self-hosted open weights, plus a decision framework. That is slides 16 and 26 compressed. It ends as you
begin, so some of that room walks into yours. **Slide 3 now credits it on the slide** — say the line before you
deliver the thesis.

**Four slides carry an on-slide cross-reference** to another session here, in a lavender label: slide 3
(Dimitrov, AI Labs), slide 18 (the four agent sessions), slide 21 (Koen's AI Factory keynote) and slide 31
(the hackathon final). They are there so the room can see you watched the rest of the programme. Say each one
out loud — a reference nobody reads aloud is decoration.

**What this cut dropped** (all still in `../beyond-the-clouds/` or `../beyond-the-clouds-tech/`): the Monty Python opener, the proverb,
the concentration donut, the five-survey bars, "who decides the roadmap", the KubeCon session list, "Europe is
building the bottom layer", "open source is the floor", the people slide, the ChemAI card, and the VOLT
full-stack slide — cut once the agenda put its content into panel question 1. Their one-line payloads moved
into the speaker notes of the slides that survive; the data-centre-law clause now lives in move four of the
ninety-day plan, slide 27.

---

## 00 Opening — 2 min (slides 1–3)

**1 · Title.** Up as the chair introduces you. You have just come off the panel, so do not re-introduce yourself. One line and the contract.
"I build AI infrastructure for a living. For the next twenty minutes I want to argue that the most important
AI decision you'll make this year isn't which model — it's whose jurisdiction you run it in. And then I want to
show you what that looks like from here, not from Amsterdam." Then: "Twenty minutes, then lunch at a quarter past
twelve. There's a slide at the end with five things I believe and you might not — argue with me in the foyer."

**2 · Ninety days.** Ask it. *"Hands up if you could move your AI workloads to another provider in ninety
days."* Wait. *"Keep them up if you've tested it."* Most hands in this room belong to people who buy AI rather
than run it, so the second question lands harder. "Anywhere else we'd call that an untested disaster recovery
plan."

**3 · Thesis.** ★**Credit the room next door first**, in one breath: "If you were next door just now, you saw
three blueprints. They are all good. I want to add the question that picks between them — and it is not a
technical question." It is on the slide, so land it rather than paraphrase it. Then the thesis, slowly. The
word that does the work is **jurisdiction**. "Somebody signed off on a credit card and a rate limit. Those
turned out to be the same decision."

## 01 The ground moved — 4 min (slides 4–8)

Risk register, not debate. The payload of the section for this room is slide 8.

**5 · Where you actually are.** Sixty seconds; it carries three dropped slides. The chart: 29% to 15%, flat for
three years while the market grew sixfold — **the plateau is the point.** Then, spoken: "Seventy percent of that
market is three American companies; the largest European provider is two percent. And none of the three has a
region in the Western Balkans — every prompt sent from this building crosses a border before it reaches a GPU."
Then the two survey numbers: 93% repatriating or evaluating, and public cloud as primary inference down from 56%
to 41% in a year. "The market has already voted — with procurement forms, not manifestos."

**6 · Microsoft France, under oath.** Strongest slide, because it is not your claim. Be scrupulously fair.
"He's describing the structure more honestly than most of our risk registers do."

**7 · Four dates.** Left to right, 60 seconds. Admitted → responded → the ground moved anyway. "Three times in
ten years. If your architecture assumes it survives a fourth, that's a bet." *Cut if short.*

**8 · You are not in the EU. Most of its rulebook binds you anyway. ★new** Ninety seconds; this earns the talk
its place in Skopje. Read points one and three. "The AI Act doesn't care where you are — it cares where your
customer is, and for most of the software built in this country the customer is in the EU. And the one law in
this list that *helps* you, the Data Act, helps you through your supplier: buy from a European provider and from
January they cannot charge you to leave. You inherit the protections and the obligations of a market you don't
yet vote in. That's an argument for owning the architecture, not for waiting." Do not turn it into an accession
lecture; the only claim you need is "the rulebook already reaches you; the vote does not — yet." If challenged
on scope: Article 2(1)(a) and 2(1)(c).

## 02 Sovereignty is a dial — 5 min (slides 9–13)

**10 · SEAL 0 to 4 (builds).** One rung per click; read 0, 2 and 3. **The gap between 2 and 3 is the whole
talk.** "No hyperscaler bid at SEAL-3." For this room: nothing stops a Macedonian ministry or bank writing
"SEAL-3 or a written explanation" into a tender tomorrow — the framework is public.

**11 · Four questions, per workload.** "Most organisations have one AI policy and forty AI workloads."

**12 · What changes.** Read the last line of each column. "The right-hand column is not better. It's
different, and it's yours." *Cut if short.*

**13 · Three decisions, one country, one summer. ★new** Two minutes, the slide the deck was rebuilt for.
Left to right, and be scrupulously fair to the third card — you work for a data-centre company and the room
knows it. "In June the Ministry and FINKI switched on Vezilka: six million euros, and it plugs this country into
the Greek AI Factory — two thousand of the best chips in Europe, in Athens, without building any of them.
Second, a group of researchers released domestic-yak: an eight-billion-parameter Macedonian model where you can
read the weights, the training data and the code. Third, in May and June the government moved to change the
planning and construction laws so large data centres can be built quickly, for investors it hasn't named yet."
Then the line that has to be said by someone who builds data centres: "The third one is necessary. Somebody has
to pour the bottom layer. But a hall full of somebody else's GPUs, running somebody else's software, is an
electricity export with a nice roof. The same hall with a Macedonian-run control plane on top is an AI
industry. The law decides the hall. What this room does decides the rest." The Vezilka card is also your answer
to "isn't this protectionism?" — an antenna is staying in the European commons and keeping a vote. Do not use the
critics' word "extractivism" from the stage. If the ministry is in the room, offer the constructive clause: write
"who operates the control plane" into the law, the way the Commission wrote SEAL into procurement.

## 03 The stack is ready — 5 min (slides 14–19)

**Change your voice.** Sections 01–02 were risk; this is opportunity. No YAML in this cut — point at plain-language
labels and never name a field.

**15 · Boring is the achievement.** 66% serve inference on Kubernetes; 31 conformant platforms; llm-d donated by
the people selling the alternative. "The hard engineering got commoditised — by the people selling the
alternative. That's the window."

**16 · "Open weights" ≠ open model.** The honesty beat. "You can download the weights, you cannot audit what
went into them, and the licence still says what you may build. Portable — not accountable." domestic-yak is on
the third card on purpose: nowhere near the frontier, and the only model in the talk whose whole corpus you can
download. Both true. *Cut if short.*

**17 · Every layer open, every layer replaceable.** Sixty seconds, the map. Read the italic sub-labels, not the
chips: the front door that decides who may ask what; the receptionist that decides which machine answers; how
you share an expensive card. Then the data layer (the moat) and the bottom layer (cannot download).

**18 · One request, four hops.** Ninety seconds, the most technical the deck gets. "Hop two decides *whether*
a request may happen and what it may touch. Hop three decides *where* it runs. Own those two and it does not
matter whether hop four is a GPU in Skopje, a rack in Athens or a frontier API in Virginia — the caller cannot
tell, and neither can the audit log. You don't have to leave the cloud to stop being captured by it. You have
to own the two boxes in the middle." If an engineer wants the YAML, the Groningen deck has it.

★**Then the agent line, and do not skip it.** It is the tie to the biggest theme of this summit — five or six
main-stage sessions across two days — and it is on the slide. "You have spent two days hearing that agents will
run your business. Every one of those demos has an agent calling tools: your CRM, your repository, your payment
system. Hop two is where you decide which tools it may call, and it is the only place you can prove afterwards
what it actually did. I have not seen that box in a single agent demo this week."

**19 · The smallest sovereign unit fits in one rack. ★new** Ninety seconds. "This is one server. Eight GPUs,
two-and-a-bit terabytes of memory, fourteen kilowatts. It runs a seventy-billion-parameter open model for
hundreds of people at once and still has room for a Macedonian model next to it. The software is an afternoon.
And the point isn't the box — once your workload runs behind a standard route on it, sending it to Athens, or to
a European cloud, or to OpenAI, is a change in one file." Land "a receipt, not a strategy document": the room
has heard strategy documents for two days.

## 04 The bottom layer — 2 min (slides 20–22)

**Keep it to three minutes.** NVIDIA did the factory keynote yesterday and you were just on the panel. "Koen
showed you the factory yesterday; here is what it costs in grid, and what the numbers look like from here."
**Disclose the VOLT relationship** here if you have not already.

**21 · In megawatts.** ★The Koen reference is **on the slide** now, so say it: "Koen showed you the five-layer
factory yesterday. This is what its bottom layer costs in grid, and where it is being poured." Then: "Nineteen
AI Factories and thirteen antennas run on EuroHPC money today, and one of them is in this city." Let them see
the gap, then the fourth bar.
"Kragujevac, three hundred kilometres from here. Serbia's state data centre — fourteen megawatts today, forty
more promised by a Gulf telecom. That is the regional version of the same race." Tenants there are Oracle, IBM
and Huawei: the landlord point with a Serbian address. *First slide to cut; 23 makes the point in five seconds.*

**22 · 800 MW.** The number they repeat at lunch. "That single site, running flat out, would use more
electricity in a year than this whole country generated last year." Say **at full load**. If asked: 800 MW ×
8,760 h ≈ 7 TWh; North Macedonia generated 6.1 TWh in 2024, 89% of its own demand; REK Bitola is 675 MW.
"Every AI strategy eventually becomes an energy strategy — and a country deciding its data-centre law and its
energy transition in the same parliament, in the same year, can decide them together."

## 05 What the keynote leaves out — 3 min (slides 23–26)

Credibility section. In a summit full of vendor keynotes this is what makes yours not one.

**24 · Four failure modes (builds).** "I've watched two teams fight over eight GPUs for six weeks. No technology
fixed it. A quota policy and one uncomfortable meeting fixed it."

**25 · The curve.** Ninety seconds, the CFO slide. Same H100, $0.21 to $15.25 per million tokens. Give explicit
permission not to self-host: "€4,000 a month and spiky is a hobby. Come back at €40,000 and flat." The curve
is arithmetic anchored on two published endpoints — say so.

**26 · Self-host / federate / rent (builds).** **Never cut.** Row two: "You don't have to leave the
hyperscalers to stop being captured by them. You have to own the layer where the decisions are made." Row
four is Vezilka as a procurement verdict — this country already has a federated training path, paid for.

## 06 Close — 3 min (slides 27–31)

**27 · Ninety days, four moves (builds).** Slow down. Inventory → gateway in front → prove portability once
(to a European provider, to Pharos through Vezilka, or to the one box) → SEAL in the next procurement, or
"who operates the control plane" in the data-centre law. "None of these need a business case. The first is a
spreadsheet, and I'd bet nobody here can produce it today."

**28 · "The clouds aren't going anywhere. Your autonomy shouldn't live there."** Pause. Do not fill it.

**29 · Sovereignty is not a product. It's a practice.** Forty seconds, the three middle lines slowly. "Landlord
model" lands twice as hard in a room that has just been told about the data-centre amendments — do not point
that out; they will. The last line carries the maintenance argument on its own: "If you adopt an open stack and
fund none of it, you haven't become sovereign — you've moved your dependency somewhere with no support contract."

**30 · Five things I believe (builds).** Leave it up while you finish. "Lunch is next door. Pick a number and
find me." Honest positions: half-believe #1 (the Vezilka card on 13 is the answer); do not believe #2 (slide 19
is why); #3 is the one you want somebody from the ministry to argue with; strongly believe #5, and it was the
panel. If the chair offers three minutes, take one question and send the rest to the foyer.

**31 · Close.** Who you are, the disclosure, the deck URL. One sentence on ChemAI AMS (12–13 November,
Amsterdam) if you want it. "Start with the inventory — everything else follows from it."

★**Then the hackathon line, and stop.** It is the only moment in the talk aimed at the students rather than the
buyers; the finalists are on this stage four hours later, and the organisers built the summit around them. It
is on the slide. "One last thing. At half past four, three student teams present on this stage. Every one of
those projects is built on somebody's API. Whose, is the only question I have been asking for twenty minutes.
Enjoy lunch."

**32–33 · Sources.** Backup. 32 is the argument, 33 is the region. Only open if a number is challenged.
