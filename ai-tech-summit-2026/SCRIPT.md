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

**Timing.** 38 slides, of which two are sources you only open if challenged. Delivered in full it runs
**≈25 min**, which leaves a real four-minute margin for a late start, a laugh, or one question. There is **no Q&A
block** — the provocations slide (34) stays up while you close and sends the argument to lunch. Say the lunch time
out loud on slide 1.

**Cut order if you are behind: 10 → 11 → 16 → 20 → 8 → 25 → 29.** The first two are the DORA and NIS2 slides;
they are depth, not spine. Never cut 3, 4, 9, 12, 17, 22, 23, 30 or 33 — two of those carry a reference to
another session at this summit, and 3 is where you disclose. Cutting 25 loses the Koen credit, so say it off
slide 24 instead. If you are badly behind at slide 24, jump to 26 with "Koen showed you the factory yesterday;
here is the one number I'd add".

**Slides that build.** 14, **25**, 28, 30, 31 and 34 reveal one item per click. Right arrow (or space, or click) brings
out the next item, then moves on; left arrow steps back. **Down/Up jump whole slides.**

**The morning of the talk.** Two regional facts can move overnight: the status of the data-centre amendments
in parliament, and anything the ministry says about Vezilka from the stage on day one. Read the Macedonian
press at breakfast. The *Watts Matter* half of the listing has been removed — the session is now billed as
*Beyond the Clouds* alone, so the energy material in § 04 is a supporting act, not a promise. The agenda
prints your name as "Alessandro Stefouli-Vozza" — decide before you go on whether the title slide should match.

**Deconflict with your own panel.** Question 3 is slide 17 of this deck; question 1 is the material that used
to be the VOLT full-stack slide, now cut for exactly that reason. Do not spend them on the panel: answer 1 in one sentence and
park 3 with "I have a slide on exactly that in fifteen minutes". Spend your panel time on 2 and 4, which are
operator questions you can answer better than either co-panellist, and which this deck barely touches.

**Competing session.** AI Labs, same 11:25–11:45 slot: *Sovereign by Design — three blueprints for AI that
can't leave the building* (Gjorgji Dimitrov, GAIA Technology Systems) — managed API, private endpoints,
self-hosted open weights, plus a decision framework. That is slides 20 and 30 compressed. It ends as you
begin, so some of that room walks into yours. **Slide 4 now credits it on the slide** — say the line before you
deliver the thesis.

**Four slides carry an on-slide cross-reference** to another session here, in a lavender label: slide 4
(Dimitrov, AI Labs), slide 22 (four agent sessions, all before yours — Greenwood's *Augmented Team* is after
you, so it is deliberately not named), slide 25 (Koen's AI Factory keynote) and slide 36 (the hackathon final). They are there so the room can see you watched the rest of the programme. Say each one
out loud — a reference nobody reads aloud is decoration.

**What this cut dropped** (all still in `../beyond-the-clouds/` or `../beyond-the-clouds-tech/`): the Monty Python opener, the proverb,
the concentration donut, the five-survey bars, "who decides the roadmap", the KubeCon session list, "Europe is
building the bottom layer", "open source is the floor", the people slide, the ChemAI card, and the VOLT
full-stack slide — cut once the agenda put its content into panel question 1. Their one-line payloads moved
into the speaker notes of the slides that survive; the data-centre-law clause now lives in move four of the
ninety-day plan, slide 31.

---

## 00 Opening — 3 min (slides 1–4)

**1 · Title.** Up as the chair introduces you. You have just come off the panel, so do not re-introduce yourself. One line and the contract.
"I build AI infrastructure for a living. For the next twenty minutes I want to argue that the most important
AI decision you'll make this year isn't which model — it's whose jurisdiction you run it in. And then I want to
show you what that looks like from here, not from Amsterdam." Then: "Twenty minutes, then lunch at a quarter past
twelve. There's a slide at the end with five things I believe and you might not — argue with me in the foyer."

**2 · Ninety days.** Ask it. *"Hands up if you could move your AI workloads to another provider in ninety
days."* Wait. *"Keep them up if you've tested it."* Most hands in this room belong to people who buy AI rather
than run it, so the second question lands harder. "Anywhere else we'd call that an untested disaster recovery
plan."

**3 · I quit a big American hyperscaler to build Europe's own. ★new** Thirty-five seconds, and resist making it
longer. **This is not a bio** — the bio is on the last slide with your face on it. It does three jobs: you have
stood on both sides, your affiliation lands at the front instead of halfway through, and the thesis that follows
becomes personal rather than academic.
**The slide names neither company on purpose**, so it travels to any room and does not read as a swipe at a
former employer. Both names are on the title byline and in the programme anyway, so the room has them either
way. Decide on stage how specific to be:
"I spent years inside one of the big American hyperscalers, selling the thing I am about to spend twenty minutes
taking apart. Then I left, to go and build sovereign AI gigafactories here instead — because I think this
continent should be able to run its own, and because I would rather build that than sell around it. So I am not
a neutral analyst, and you should not listen to me as if I were."
Swap in "at Microsoft" and "and I came to VOLT" if the room is right for it.
Then the tail line, which hands off to the thesis: **"I did not change my mind about the technology. I changed
my mind about who should be holding it."** Say the number of years out loud; the slide deliberately does not, so
it survives being given again. No titles, no products, no customer names — the moment it becomes a CV it stops
working.

**4 · Thesis.** ★**Credit the room next door first**, in one breath: "If you were next door just now, you saw
three blueprints. They are all good. I want to add the question that picks between them — and it is not a
technical question." It is on the slide, so land it rather than paraphrase it. Then the thesis, slowly. The
word that does the work is **jurisdiction**. "Somebody signed off on a credit card and a rate limit. Those
turned out to be the same decision."

## 01 The ground moved — 6 min (slides 5–12)

Risk register, not debate. The payload is slide 9, and the three slides after it name the rules one at a time.

**6 · Where you actually are.** Sixty seconds; it carries three dropped slides. The chart: 29% to 15%, flat for
three years while the market grew sixfold — **the plateau is the point.** Then, spoken: "Seventy percent of that
market is three American companies; the largest European provider is two percent. And none of the three has a
region in the Western Balkans — every prompt sent from this building crosses a border before it reaches a GPU."
Then the two survey numbers: 93% repatriating or evaluating, and public cloud as primary inference down from 56%
to 41% in a year. "The market has already voted — with procurement forms, not manifestos."

**7 · Microsoft France, under oath.** Strongest slide, because it is not your claim. Be scrupulously fair.
"He's describing the structure more honestly than most of our risk registers do."

**8 · Four dates.** Left to right, 60 seconds. Admitted → responded → the ground moved anyway. "Three times in
ten years. If your architecture assumes it survives a fourth, that's a bet." *Cut if short.*

**9 · You are not in the EU. Most of its rulebook binds you anyway. ★new** Ninety seconds; this earns the talk
its place in Skopje. Read points one and three. "The AI Act doesn't care where you are — it cares where your
customer is, and for most of the software built in this country the customer is in the EU. And the one law in
this list that *helps* you, the Data Act, helps you through your supplier: buy from a European provider and from
January they cannot charge you to leave. You inherit the protections and the obligations of a market you don't
yet vote in. That's an argument for owning the architecture, not for waiting." Do not turn it into an accession
lecture; the only claim you need is "the rulebook already reaches you; the vote does not — yet." If challenged
on scope: Article 2(1)(a) and 2(1)(c).

**10 · Digital Operational Resilience Act.** *Cut first of the three.* Forty seconds. Say the full name once,
then the second point: if a service supports a critical function, a European bank needs a documented, **tested**
exit plan. "Not a clause in a contract. A rehearsal." The surprise is the third point — a critical provider based
outside the Union must open a subsidiary inside it, which is sovereignty written into financial law before anyone
in Brussels was using the word. Detail if a banker pushes: Article 28(8); nineteen providers designated on
18 November 2025.

**11 · Network and Information Security Directive 2.** *Cut second.* Thirty seconds, and the second point is the
whole slide. "The controls are not the interesting part. A board has to approve them and can be held personally
liable, so the duty cannot be delegated to a supplier. It lands on you instead, as a questionnaire. If you have
wondered why your German customer suddenly wants to know who maintains your dependencies, this is why."

**12 · Cyber Resilience Act.** **Protect this one.** Fifty seconds. It is the only European law in the deck that
binds a Macedonian company directly rather than through somebody else's contract. "It does not bind European
companies. It binds anyone placing a product with digital elements on the European market, wherever they are. And
the reporting obligation did not start in 2027. It started on the eleventh of this month, for products that are
already out there." Say "twelve days ago" only while it stays true. Do not attempt the open-source stewardship
carve-out from the stage.

## 02 Sovereignty is a dial — 5 min (slides 13–17)

**14 · SEAL 0 to 4 (builds).** One rung per click; read 0, 2 and 3. **The gap between 2 and 3 is the whole
talk.** "No hyperscaler bid at SEAL-3." For this room: nothing stops a Macedonian ministry or bank writing
"SEAL-3 or a written explanation" into a tender tomorrow — the framework is public.

**15 · Four questions, per workload.** "Most organisations have one AI policy and forty AI workloads."

**16 · What changes.** Read the last line of each column. "The right-hand column is not better. It's
different, and it's yours." *Cut if short.*

**17 · Three decisions, one country, one summer. ★new** Two minutes, the slide the deck was rebuilt for.
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

## 03 The stack is ready — 5 min (slides 18–23)

**Change your voice.** Sections 01–02 were risk; this is opportunity. No YAML in this cut — point at plain-language
labels and never name a field.

**19 · Boring is the achievement.** 66% serve inference on Kubernetes; 31 conformant platforms; llm-d donated by
the people selling the alternative. "The hard engineering got commoditised — by the people selling the
alternative. That's the window."

**20 · "Open weights" ≠ open model.** The honesty beat. "You can download the weights, you cannot audit what
went into them, and the licence still says what you may build. Portable — not accountable." domestic-yak is on
the third card on purpose: nowhere near the frontier, and the only model in the talk whose whole corpus you can
download. Both true. *Cut if short.*

**21 · Every layer open, every layer replaceable.** Sixty seconds, the map. Read the italic sub-labels, not the
chips: the front door that decides who may ask what; the receptionist that decides which machine answers; how
you share an expensive card. Then the data layer (the moat) and the bottom layer (cannot download).

**22 · One request, four hops.** Ninety seconds, the most technical the deck gets. "Hop two decides *whether*
a request may happen and what it may touch. Hop three decides *where* it runs. Own those two and it does not
matter whether hop four is a GPU in Skopje, a rack in Athens or a frontier API in Virginia — the caller cannot
tell, and neither can the audit log. You don't have to leave the cloud to stop being captured by it. You have
to own the two boxes in the middle." If an engineer wants the YAML, the Groningen deck has it.

★**Then the agent line, and do not skip it.** It is the tie to the biggest theme of this summit — five or six
main-stage sessions across two days — and it is on the slide. "You have spent two days hearing that agents will
run your business. Every one of those demos has an agent calling tools: your CRM, your repository, your payment
system. Hop two is where you decide which tools it may call, and it is the only place you can prove afterwards
what it actually did. I have not seen that box in a single agent demo this week."

**23 · The smallest sovereign unit fits in one rack. ★new, now with the photograph** Ninety seconds. **Point at
the picture once** and say "this is not a render" — after two days of architecture diagrams a real rack with real
cable management does more work than another box-and-arrow drawing. If it is one of yours, say where it is; if
the caption should name the machine or the site, change it before you present. "This is one server. Eight GPUs,
two-and-a-bit terabytes of memory, fourteen kilowatts. It runs a seventy-billion-parameter open model for
hundreds of people at once and still has room for a Macedonian model next to it. The software is an afternoon.
And the point isn't the box — once your workload runs behind a standard route on it, sending it to Athens, or to
a European cloud, or to OpenAI, is a change in one file." Land "a receipt, not a strategy document": the room
has heard strategy documents for two days.

## 04 The bottom layer — 2 min (slides 24–26)

**Keep it to three minutes.** NVIDIA did the factory keynote yesterday and you were just on the panel. "Koen
showed you the factory yesterday; here is what it costs in grid, and what the numbers look like from here."
**Disclose the VOLT relationship** here if you have not already.

**25 · In megawatts. ★builds, smallest first — one click per bar.** The Koen reference is **on the slide**, so
say it: "Koen showed you the five-layer factory yesterday. This is what its bottom layer costs in grid, and
where it is being poured." Then: "Nineteen AI Factories and thirteen antennas run on EuroHPC money today, and
one of them is in this city." Then start clicking, one sentence per bar.
Bar 1 — "Fourteen megawatts. Amsterdam. Live this month." Bar 2, **the one for this room** — "Forty megawatts,
Kragujevac, three hundred kilometres from here. Serbia's state data centre: fourteen today, forty more promised
by a Gulf telecom. The regional version of this race, already running." Tenants there are Oracle, IBM and
Huawei: the landlord point with a Serbian address. Bars 3 and 4 — "France, Finland, a couple of hundred each."
Bar 5, slowly, **then stop talking** — "Eight hundred. Rotterdam, 2027, the same company as the first bar. A
fifty-seven-fold step in eighteen months, and the constraint is not chips and not capital. It is a grid
connection."
The climb is the argument: four bars you could imagine building, then one you could not. *First slide to cut; 26
makes the point in five seconds. If you keep it but are rushed, press down-arrow to show all five at once.*

**26 · 800 MW.** The number they repeat at lunch. "That single site, running flat out, would use more
electricity in a year than this whole country generated last year." Say **at full load**. If asked: 800 MW ×
8,760 h ≈ 7 TWh; North Macedonia generated 6.1 TWh in 2024, 89% of its own demand; REK Bitola is 675 MW.
"Every AI strategy eventually becomes an energy strategy — and a country deciding its data-centre law and its
energy transition in the same parliament, in the same year, can decide them together."

## 05 What the keynote leaves out — 3 min (slides 27–30)

Credibility section. In a summit full of vendor keynotes this is what makes yours not one.

**28 · Four failure modes (builds).** "I've watched two teams fight over eight GPUs for six weeks. No technology
fixed it. A quota policy and one uncomfortable meeting fixed it."

**29 · The curve.** Ninety seconds, the CFO slide. Same H100, $0.21 to $15.25 per million tokens. Give explicit
permission not to self-host: "€4,000 a month and spiky is a hobby. Come back at €40,000 and flat." The curve
is arithmetic anchored on two published endpoints — say so.

**30 · Self-host / federate / rent (builds).** **Never cut.** Row two: "You don't have to leave the
hyperscalers to stop being captured by them. You have to own the layer where the decisions are made." Row
four is Vezilka as a procurement verdict — this country already has a federated training path, paid for.

## 06 Close — 4 min (slides 31–36)

**31 · Ninety days, four moves (builds).** Slow down. Inventory → gateway in front → prove portability once
(to a European provider, to Pharos through Vezilka, or to the one box) → SEAL in the next procurement, or
"who operates the control plane" in the data-centre law. "None of these need a business case. The first is a
spreadsheet, and I'd bet nobody here can produce it today."

**32 · "The clouds aren't going anywhere. Your autonomy shouldn't live there."** Pause. Do not fill it.

**33 · Sovereignty is not a product. It's a practice.** Forty seconds, the three middle lines slowly. "Landlord
model" lands twice as hard in a room that has just been told about the data-centre amendments — do not point
that out; they will. The last line carries the maintenance argument on its own: "If you adopt an open stack and
fund none of it, you haven't become sovereign — you've moved your dependency somewhere with no support contract."

**34 · Five things I believe (builds).** Leave it up while you finish. "Lunch is next door. Pick a number and
find me." Honest positions: half-believe #1 (the Vezilka card on 13 is the answer); do not believe #2 (slide 19
is why); #3 is the one you want somebody from the ministry to argue with; strongly believe #5, and it was the
panel. If the chair offers three minutes, take one question and send the rest to the foyer.

**35 · The party is at Garçon. ★new** Fifteen seconds, and the last thing on screen before your contact card.
It follows the provocations on purpose: you have just told the room to argue with you, and this is where the
arguing can actually happen.
"One more thing, and then I am done. There is a party at Garçon afterwards — the handle is on the screen. Same
argument, better music. Come and tell me which of those five I have wrong."
**The slide does not state a time** — add one under the handle before you present, or say it out loud. If that
is you behind the decks in the photograph, say so; it is the only slide in the deck where you are not being
serious.

**36 · Close.** Who you are, the disclosure, the deck URL. One sentence on ChemAI AMS (12–13 November,
Amsterdam) if you want it. "Start with the inventory — everything else follows from it."

★**Then the hackathon line, and stop.** It is the only moment in the talk aimed at the students rather than the
buyers; the finalists are on this stage four hours later, and the organisers built the summit around them. It
is on the slide. "One last thing. At half past four, three student teams present on this stage. Every one of
those projects is built on somebody's API. Whose, is the only question I have been asking for twenty minutes.
Enjoy lunch."

**37–38 · Sources.** Backup. 37 is the argument, 38 is the region. Only open if a number is challenged.
