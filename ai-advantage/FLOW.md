# Flow review — Turning AI Into Your Advantage

Reviewed 17 Sep 2026 against the deck (24 slides), `SCRIPT.md` and `handout.html`.
The script's slide numbers, cut order and verbatim lines all match the deck. The arc is
sound. The problem is the clock in the exercise block.

## The arc, beat by beat

| # | Slide | Job in the story | Time |
|---|---|---|---|
| 1 | Title | Show of hands: "used AI this week" → "can name the euros". Opens the gap. | 0:00 |
| 2 | Restaurants, same supplier | Anchor analogy: ingredients vs. kitchen. Returns in every section. | 1:00 |
| 3 | McKinsey bars 88 → 33 → 39 → 6 | The gap in numbers. Ends on "what the six do differently". | 2:30 |
| 4 | "Access isn't the advantage. Decisions are." | Thesis #1. | 4:00 |
| 5 | What you leave with | The three outputs: X-rayed process, working teammate, review date. Each is a box on the worksheet. | 4:30 |
| 6 | How the next forty minutes run | Time blocks; the yellow one is theirs. Phones out, pens, pair up. | 5:15 |
| 7 | Section: The three calls | | 5:45 |
| 8 | Three calls overview | Build on top · keep · review. One line each. | 6:15 |
| 9 | Call 1 — dishwasher in the garage | Beside vs. inside the work. Question to the room. | 7:15 |
| 10 | Call 2 — autopilot / pilot | Four things you keep human. Question to the room. | 8:45 |
| 11 | Call 3 — experiment loop | Hypothesis → 2-week test → keep/fix/kill. Chemist line. | 10:15 |
| 12 | Section: Luca's kitchen | Optional 90-second live interview. | 11:45 |
| 13 | Luca's story in five beats | **Placeholder.** Before / built / kept / dropped / after. | 12:45 |
| 14 | The flow with one human checkpoint | **Illustrative.** Points at the coral box = Call 2 made concrete. | 15:15 |
| 15 | Section: Your turn | Pairs confirmed, pens up. | 17:45 |
| 16 | Exercise 1 — Workflow X-ray, 8:00 | Solo 3 · pairs 4 · two shares 1. Feeds Exercise 2. | 18:30 |
| 17 | Verdict example (sales call) | "Before the timer if unsure, or after as debrief." | 26:30 |
| 18 | Exercise 2 template | Role · task · rules · **NEEDS HUMAN** exit. 60 seconds. | 27:30 |
| 19 | Exercise 2 — Build a teammate, 8:00 | Data warning, live build, partner attack, show of hands. | 28:30 |
| 20 | "NEEDS HUMAN is your control point" | Thesis #2, landed *after* they felt it. Links back to slide 14. | 36:30 |
| 21 | Exercise 3 — Kill switch, 4:00 | Owner, success, stop signal, review date in the calendar. | 37:00 |
| 22 | Three takeaways | One line each, no re-teaching. | 41:00 |
| 23 | CTA + commitment sentence | Photo of the box. Closing line. Stays up for Q&A. | 42:00 |
| 24 | Sources (backup) | Press End if challenged. | — |

Times in the right column are what actually happens if every slide takes the time its own
notes ask for. The block finishes at ~44 minutes, not 40.

## What works

- **One analogy, carried all the way.** Kitchen on 2, 8, 9, 12, 22. The exercises are literally "your kitchen".
- **Two theses, placed right.** "Decisions are the advantage" (4) opens; "NEEDS HUMAN is your control point" (20) lands only after the room has typed it and watched it fire in Exercise 2. Don't move 20.
- **The setup pair (5–6) sells the exercises before the theory starts.** Slide 5 promises three photographable outputs; slide 6 shows that half the clock is theirs. People sit differently once they know they'll be working.
- **Exercises map onto the calls.** Ex 1 = find where to build (Call 1) and what to keep (Call 2). Ex 2 = build it, with the Call 2 exit. Ex 3 = Call 3. Each exercise's output feeds the next (top candidate → brief → kill switch → commitment). The handout mirrors this exactly, and now carries a worked example for every box.
- **Dark/light rhythm.** Every exercise and section break is on navy with the big countdown; the teaching is on paper. The room learns "dark = stop listening, do".
- **Cut order and verbatim lines are correct** and reference the right slides.

## What doesn't: the exercise block is overbooked by ~4 minutes

Minutes 17–37 are 20 minutes. The three countdowns alone are 20 minutes (8 + 8 + 4).
Everything else in that block — pairing up, slide 17, slide 18, the data warning, slide 20
said slowly — is on top. Realistic total: 24–25 minutes. The two setup slides add about
45 seconds net to the opening (they replace the spoken "shape of the session" on slide 4),
so the retiming below is now needed, not optional.

Pick from these, in this order:

1. **Worksheets on the tables before people sit down.** Done in the script and on slide 6 ("the worksheet is on your table"). Saves the shuffle at slide 15.
2. **Exercise 1 to 6:00** (2 solo · 3 pairs · 1 shares). X-raying one process in 5–8 steps doesn't need eight minutes; the pairs phase is where the value is and three minutes is enough for one challenge. Change `data-timer="480"` → `360` on slide 16 and the phase strip, the "8:00" on slide 6, and the handout's "8 minutes".
3. **Decide slide 17 now.** "Before or after" is a decision made under pressure in the room. Recommendation: move it *before* slide 16 and give it 30 seconds — the first time people see the 1–3 scoring they will be unsure. If you'd rather keep the momentum from slide 15 straight into the timer, cut it (it's already #1 in the cut order; the rule box and a worked example row are on the worksheet).
4. **Exercise 3 to 3:00.** The output is a calendar entry. The script already says two minutes is enough when behind. Update slide 6's "4:00" too.

2 + 4 bring the block to ~21 minutes with slide 17 kept. Slides 22–23 then get their three
minutes and the commitment photo happens before people stand up.

## Other findings

- **Slides 13 and 14 are the single point of failure.** Six minutes of the talk are placeholders. Add a fallback to the script: if Luca's story isn't confirmed by the day, drop slide 13, keep slide 14 relabelled "a typical pattern from our community", and give the two minutes back to Exercise 1.
- **Two room questions in the six-minute calls section** (slide 9 "what could you offer", slide 10 "which would you add"). Each costs 45–60 seconds. Keep one; slide 10's is better because the answers ("hiring", "legal") go straight onto the worksheet's "four things I keep human".
- **Two places print the timing** — the section slides (5–11, 11–17, 17–37) and slide 6's blocks. If you change any countdown, update both in the same commit.
- **Handout ↔ deck consistency: clean.** Same rule box, same template with the same highlighted line, same kill-switch fields, same commitment sentence. The only mismatch will be the exercise minutes if you shorten them.
- **Still open from the pre-event checklist:** date on slide 1, QR on slide 23, Luca's permission, the backup run for Exercise 2.
