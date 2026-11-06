# Sales process and team

Open this file when the user is building or running a sales function: process design, metrics, hiring,
ramp, coaching, compensation, promotion, territory and SDR/AE models, dividing work between an AI agent
and humans, and the buyer-side facts to plan around. A rule without a context flag holds in both
small-ticket single-call and complex B2B selling. Numbers: `benchmarks.md`. Excluded claims: `claims-audit.md`.

## Contents

- [Rules the model usually gets wrong](#rules-the-model-usually-gets-wrong)
- [Operating benchmarks for an SDR team](#operating-benchmarks-for-an-sdr-team)
- [Designing or fixing the sales process](#designing-or-fixing-the-sales-process)
- [Hiring a seller: what to test](#hiring-a-seller-what-to-test)
- [A new rep is not closing: ramp or fire](#a-new-rep-is-not-closing-ramp-or-fire)
- [Coaching a rep](#coaching-a-rep)
- [Designing or changing the comp plan](#designing-or-changing-the-comp-plan)
- [Choosing who to promote to manager](#choosing-who-to-promote-to-manager)
- [Dividing work between the AI agent and human sellers](#dividing-work-between-the-ai-agent-and-human-sellers)
- [Planning for how buyers actually buy](#planning-for-how-buyers-actually-buy)
- [Worked examples](#worked-examples)
- [Common mistakes and replacements](#common-mistakes-and-replacements)

## Rules the model usually gets wrong

- Train knowledge and adaptiveness before pushing hours: selling-related knowledge (β = .28) and adaptiveness (.27) outrank disposition and effort; role ambiguity costs −.25 (Verbeke 2011 meta-analysis, 79,747 salespeople). [study]
- Hire with a structured interview built on real selling tasks (validity .42) over cognitive tests (.31) or unstructured chats (.19); "born closer" extraversion predicts ratings, not sales (Sackett 2022; Vinchur 1998; Verbeke 2011). [study]
- Promote on managerial potential, not sales rank: top sellers get promoted and their teams' sales fall; promoting on potential could raise subordinates' sales ~30% (Benson, Li & Shue 2019, 214 firms). [study]
- Build the manager's coaching skill before adding sessions: skill, not frequency, predicted goal attainment, and frequent coaching by unskilled managers hurt (Dahling 2016, 1,246 reps). [study]
- Limit feedback for the weakest reps: an AI coach helped middle performers most, overloaded the bottom, and a restricted-feedback version lifted bottom-ranked agents (Luo 2021, field experiments). [study]
- Judge ramp against the deal cycle: B2B SDR ramp averages 3.0 months (Bridge Group 2025, 351 companies), so a 14-day cut confuses ramp with ability outside high-velocity, single-call selling. [data]
- Pay stars uncapped overachievement commissions and pace laggards with quarterly bonuses (Chung 2014); nonlinear plans invite deal-timing gaming (Larkin 2014); incentives raise quantity more than quality (Cerasoli 2014). [study]
- Plan for a buying group (~13 stakeholders, procurement decides 53%, AI in 94% of purchases: Forrester 2026) and treat "67% prefer rep-free" as preference: self-service shows 43% high regret vs 26% rep-led (Gartner). [data]
- Let AI generate and qualify leads and humans persuade: that split won a telemarketing RCT, and AI assistance helped skilled agents most, raising the ceiling more than the floor (Jia 2024, 3,144 customers). [study]

## Operating benchmarks for an SDR team

`[data]` Bridge Group 2025: 351 B2B companies (83% SaaS, median ASP $50K), self-reported vendor survey.
Use for direction and sizing, never as a cause; the vendor sells consulting. Full entries in `benchmarks.md`.

| Metric | Benchmark |
|---|---|
| SDRs at quota | 60%, the lowest on record |
| Activities per SDR per day | 112 (44 phone, 41 email, 19 LinkedIn, 8 other) producing 4.1 quality conversations |
| Phone-centric vs email-centric teams | 4.6 vs 3.4 quality conversations a day (56 vs 28 dials) |
| Ramp to full productivity | 3.0 months (peak 3.8 in 2014) |
| Annual attrition | 40% median (13% involuntary, 11% voluntary, 16% promoted) |
| Tenure | 1.9 years |
| Structure | 1 SDR per 2.4 AEs; 6.4 SDRs per leader |
| Monthly quota | 10 held meetings, down 40% since 2018 |
| Pay | $80K median OTE, 68:32 base to variable |
| "AI SDRs" | 1% of respondents, first year as a category |

## Designing or fixing the sales process

- Define each stage by an observable buyer action (named the decision group, agreed a dated next meeting, shared a budget range), not by seller activity: a stage is an advance the buyer made. [practitioner]
- Write down who owns which accounts, stages and decisions: role ambiguity costs −.25 in performance, and −.27 when selling to businesses, where role sets are larger (Verbeke 2011). [study]
- Track leading metrics per stage, not close rate alone: booking rate, show rate, offer rate, close rate on shows and on offers, cash collected; a 20% show-rate lift equals a 20% close-rate lift. [practitioner]
- Find the constraint from the funnel: lay out each rep's conversion by stage and fix the highest stage with the largest gap first; the top-activity rep may have the worst lead-to-demo rate. [practitioner]
- Orlob reports about 70% process adherence as the realistic ceiling; when reps resist a step, ask why they think it fails before enforcing it. [practitioner]
- Default: knowledge and adaptiveness drive performance in consultative selling. Exception: in transactional selling, disposition matters more (Verbeke 2011 moderators), and Hormozi reports availability driving appointment volume `(small-ticket, single-call)`. [study]
- Score every hire on about ten criteria with written 1–3, 5–7 and 8–10 anchors from the first interview, then correlate scores with ramp and attainment after 18 months (Sales Acceleration Formula, one company). [practitioner]
- In that company's regression, closing ability and objection handling correlated negatively with attainment; preparation, domain experience and intelligence correlated most, matching a consultative buyer. Treat as a method, not a profile. [practitioner]
- Replace "shadow the top rep for two months" with exam-based certification on one methodology; shadowing does not scale and a star's habits are not a recipe. [practitioner]
- Set the marketing-to-sales SLA in lead value (close rate × deal size per lead type), not lead count; on a count SLA, marketing switched to the easiest lead type whenever it fell behind. [practitioner]
- Default: 5–8 touches, per `references/outreach.md`, section Building a cadence. Exception: enterprise, when a measured profit-per-lead curve supports more; Roberge reports peaks at 5 small-business, 8 mid-market, 12 enterprise attempts. [practitioner]
- Give reps an off-the-call SOP (follow-ups, pulling bookings forward, cancelling unconfirmed no-shows) as well as the call script; most teams only have the script `(small-ticket, single-call)`. [practitioner]
- Separate inbound and outbound lead flows, each with its own setters and closers; mixing them loses efficiency because the prospects differ `(small-ticket, single-call)`. [practitioner]
- Specialize only after a couple dozen customers were won without founder charm: first an SDR owning meetings only, then customer success; document the motion, objections included, or it stays oral history. [practitioner]
- Assign someone to build each new motion (new segment, upmarket, new product); telling existing reps to "figure it out" is the common failure. [practitioner]

## Hiring a seller: what to test

- Put a structured interview first: a fixed set of job-related questions scored on a common rubric; operational validity .42 against .19 for an unstructured conversation (Sackett 2022 re-analysis). [study]
- Use situational questions for novices and behaviour-description questions for experienced hires; both fit a structured format, though equal validity across the two is not established (Sackett 2022). [study]
- For experienced hires add a scored work sample (.33) or job-knowledge test (.40), for example a mock discovery call on your product; cognitive tests (.31) suit entry-level hires you will train (Sackett 2022). [study]
- Weight years of experience and generic personality scores lightly: experience at hire .07, conscientiousness .19 (Sackett 2022); personality and biographical variables show no reliable average link to sales performance (Verbeke 2011). [study]
- Probe the two trainable drivers directly: customer and product knowledge, and adaptiveness (ask how they would change approach for two different buyers in your market) (Verbeke 2011). [study]
- Hire beyond the extroverted profile: extraversion's link to actual sales is weak, and talkative reps may need to learn to regulate themselves (Vinchur 1998; Kaski 2017). [study]
- Validate any tool on your own data: validities are means with wide spread (residual SD .19 for structured interviews), so review score sheets against attainment after a few hires (Sackett 2022). [study]
- Practitioner trait lists are hypotheses to score, not profiles: coachability, curiosity, intelligence, work ethic, prior success (Sales Acceleration Formula, one inbound SaaS company); coachable and adaptable in fast-changing companies. [practitioner]
- Match the hire to the motion: a top transactional big-brand rep failed in an evangelistic consultative sale; a big-company rep used to heavy support struggles selling an unbranded new product. [practitioner]
- Character probes for the first half hour: "what is the toughest situation you have been in?", "what is the most competitive thing you ever did?", then "I'm not sure you can do this job". [practitioner]
- Define the job before the profile: the most common reason for failure in sales exit interviews is poor fit with that particular job. [practitioner]
- Ask a sales-director candidate what data they would collect and how they would fix things, and judge by specificity; "hire tigers who love the hunt" is an unmeasured label `(small-ticket, single-call)`. [practitioner]

## A new rep is not closing: ramp or fire

- Default: judge against the role's ramp and deal cycle: B2B SDR ramp averages 3.0 months (Bridge Group 2025); with a 60-day cycle an AE's first deals cannot land before day 60. [data]
- Exception: Hormozi reports firing within 14 days when a rep "looks like a dud" in phone selling at ten-plus calls a day `(small-ticket, single-call)`; outside that motion it confuses ramp with ability. [practitioner]
- Audit the inputs before the person: leads assigned (new reps often get the worst), role clarity, documented motion and onboarding; Kazanjy reports sloppy onboarding doubling ramp from 2–3 to 4–6 months. [practitioner]
- Diagnose by stage before cutting: low connect rate is a cadence or messaging problem; good connects with no progression is a call-skill problem; fix the highest failing stage first. [practitioner]
- Judge adoption of a new technique after about six repetitions, not one call; Orlob reports new behaviours take five or six tries to feel comfortable. [practitioner]
- Plan hiring capacity for structural turnover: median SDR attrition is 40% a year, 13 points involuntary (Bridge Group 2025), so an exit is a scheduling fact, not a surprise. [data]
- Expect tenure, not personality, to predict who stays: grit raised retention odds 40% per SD among 442 reps, but weeks already employed explained far more (Eskreis-Winkler 2014). [study]
- Keep the bar visible and high: Hormozi reports setters at two sets a day moving to three when the minimum rose; people shrink to the standard set `(small-ticket, single-call)`. [practitioner]

## Coaching a rep

- Assess coaching skill in a training exercise before assigning coaching load: skill predicted annual goal attainment partly through team role clarity, and frequent coaching by low-skill managers hurt (Dahling 2016, 1,246 reps). [study]
- Default: skill before frequency. Exception: scripted daily drills (script read-aloud, one objection, one call review) need little coaching skill and can run daily `(small-ticket, single-call)`. [practitioner]
- Give one fix and a hundred reps of it, like a golf pro; all 17 managers one leader promoted first overwhelmed reps with feedback. [practitioner]
- Target the task, not the person: across about 600 feedback studies, feedback helps on average but backfires about a third of the time, and works best aimed at the task (Kluger & DeNisi 1996). [study]
- For bottom-ranked reps restrict feedback to one or two items: unrestricted AI coaching overloaded them, and a restricted version lifted their performance (Luo 2021, field experiment). [study]
- For top-ranked reps pair AI coaching with a human coach: top reps showed AI aversion, and the combination beat either alone (Luo 2021, n = 451). [study]
- Middle-ranked reps gain most from coaching; spend the skilled coach's time there first (Luo 2021). [study]
- Diagnose from the rep's funnel, not impressions: leads worked, connects, demos, closes and each conversion; "activity problem" is the default guess of managers who do not look. [practitioner]
- Coach little and often: short daily drills on one script section beat multi-day courses whose content decays within about six weeks; in call review the rep critiques first, then the team. [practitioner]
- Ask for "advice for next time" or "one thing to do better" instead of "feedback"; it produces a forward-looking note rather than cheerleaders and critics. [practitioner]
- Build peer learning: reps learn by watching how the best handled a price objection; create forums and just-in-time content at the moment of need rather than one-off courses. [practitioner]
- Scaffold, then remove: temporary support on one deal, withdrawn gradually, beats a permanent mentor. [practitioner]

## Designing or changing the comp plan

- Pay uncapped overachievement commissions above quota; they sustain top performers after target (Chung, Steenburgh & Sudhir 2014, structural model on an office-supply sales force). [study]
- Add quarterly bonuses, not only annual: they act as pacers for weaker performers, who show present bias (Chung 2014). [study]
- Show core performers three target tiers (for example 90, 100, 110%); reps given all three tiers outperformed reps given only the first and third (Steenburgh & Ahearne 2012, HBR digest). [study]
- Expect gaming under nonlinear curves: at an enterprise-software vendor, accelerators led reps to time deals and distort pricing around period ends (Larkin 2014); smooth the curve and audit deal timing. [study]
- Financial incentives reliably raise output quantity; quality is driven more by intrinsic motivation (Cerasoli 2014 meta-analysis): pay on quantity, inspect discounting and churn separately. [study]
- Rising commission tiers above quota ("ratcheted comp") are supported; raising next period's quota after a good period (ratcheting) dampens effort, and a model-based redesign raised revenue about 9% (Misra & Nair 2011, 87 reps). [study]
- Test causality and measurability before paying on a metric: does the rep influence it, and can you measure it cleanly? Team selling and channel deals weaken both. [practitioner]
- Judge a plan by its effect on individual reps and company results, not "we made our number"; ZS Associates reports about 70% of companies change the plan yearly, so simulate before changing. [practitioner]
- If most reps miss quota, fix the quota or the plan: a realistic quota beats the largest one; heavy incentives in a mature category drove overselling and gaming (medical devices moved to moderate plans). [practitioner]
- Include every critical component in the goal, involve reps in setting it, and use team goals where cooperation matters: narrow targets cap effort once hit and drove misreporting when people fell short (Ordóñez 2009). [study]
- Hormozi reports cutting commission from 20% to under 10% of revenue by paying setters and closers separately and tiering commission by close rate (10% at 70%, 25% above 80%) `(small-ticket, single-call)`. [practitioner]
- Pay setters on scheduled, qualified throughput, not closes only: setters paid on closes over-disqualify by quoting price; Hormozi reports call-2 scheduling rising from 53% to 94% `(small-ticket, single-call)`. [practitioner]
- Use non-money pay too: recognition, leaderboard, training access and status markers motivate reps who say they do not care; per-deal milestones (50, 100, 150 deals) relieve anxiety in repetitive work. [practitioner]

## Choosing who to promote to manager

- Promote on managerial potential (coaching skill, metric fluency, collaboration), not sales rank: in 214 firms top sellers were likelier to be promoted, yet their subordinates sold less (Benson, Li & Shue 2019, 53,000+ workers). [study]
- A doubling of pre-promotion sales corresponded to a 7.5% drop in manager value added; promoting on potential could raise subordinates' sales about 30%, an estimate ignoring other factors (Benson, Li & Shue 2019). [study]
- Test coaching skill in a training exercise before promoting; it predicted team goal attainment a year later (Dahling 2016). [study]
- Ask the candidate why they want "five more kids": management is no longer about them, and each rep needs different coaching; selfish or mercenary top reps usually fail as leaders. [practitioner]
- Hiring a sales director from outside: someone who sold this product type in this industry, scaled and coached a team, and ties cited metrics to revenue; recruit by outreach, since the best have jobs. [practitioner]
- Keep the top closer's income path open without a title: uncapped overachievement pay and deal milestones mean promotion is not the only reward (Chung 2014). [study]
- Hire one director before scaling the rep count ("hire one to hire ten"); a recurring problem in one department is usually a who problem, not a what problem. [practitioner]

## Dividing work between the AI agent and human sellers

- Default: AI generates and qualifies leads, humans persuade; in a telemarketing RCT (3,144 customers, 40 agents) that split outperformed, and AI assistance helped skilled agents disproportionately (Jia 2024). [study]
- Expect AI to widen the skill gap, not close it: give AI assistance to the best reps first, and give bottom reps restricted feedback plus a human coach (Jia 2024; Luo 2021). [study]
- Seven randomized GenAI experiments on an e-commerce platform ranged from no effect to +16.3% sales; a pre-sale service chatbot gained most, and smaller, less experienced sellers benefited most (Fang 2025, preprint). [study]
- Disclose the AI where required and show knowledge and empathy in the first turns; the 79.7% disclosure penalty and its caveats are in `references/rapport.md`, section Rules the model gets wrong (Luo 2019). [study]
- Treat AI voice in cold calls as a compliance question first: practitioners report a 2024 US FCC ban on AI-generated voices in cold calls; check current rules per country before launch. [practitioner]
- Give the agent the off-call SOP: follow-up cadence at the profit-maximizing attempt count, pulling bookings forward, resurfacing stalled leads, CRM logging; these are the tasks reps skip. [practitioner]
- Keep humans on the persuasion turn, multi-stakeholder navigation (~13 stakeholders, procurement 53%: Forrester 2026) and decision-time de-risking, where 40–60% of deals are lost to no decision (JOLT, ~2.5M recorded conversations, proprietary). [data]
- "Sellers who partner with AI are 3.7× likelier to meet quota" (Gartner 2024, 1,026 sellers) is correlational and skill-confounded; quote the RCT split instead. [data]

## Planning for how buyers actually buy

- Plan for a buying group: ~13 internal stakeholders and 9 external participants on average; procurement decides 53% of the time; genAI-featured purchases roughly double the group, 14 vs 7 (Forrester 2026, ~18,000 buyers). [data]
- Buyers use AI in 94% of purchases (Forrester 2026) and 45% used it in a recent purchase (Gartner 2026, 646 buyers): write proposals and web content an AI summarizer will quote accurately. [data]
- 67% prefer a rep-free experience (Gartner 2026) but self-service purchases show 43% high regret vs 26% rep-led (Gartner abstract, date unconfirmed): sell the value of guidance, do not withdraw it. [data]
- Buyers with high "value clarity" are twice as likely to report a high-quality purchase (Gartner 2026): make a buyer-owned business case a stage, not a leave-behind. [data]
- 73% avoid suppliers who send irrelevant outreach and 69% see inconsistencies between the website and what sellers say (Gartner 2025, 632 buyers): align site and rep messaging before scaling outbound. [data]
- 94% of buying groups rank vendors before first contact and the favourite wins 77% of the time; first contact comes 61% of the way through (6sense 2025, ~4,000 buyers, vendor): invest in pre-contact presence. [data]
- More than 60% of buyers purchase some form of trial (Forrester 2026): design the low-risk entry (pilot, shorter term) as a stage, not a concession. [data]
- Buying is streams, not a funnel: buyers move between online and offline several times, so each seller interaction must add information they could not get alone. [practitioner]
- Digital has not replaced sellers: US salesperson counts rose through the 21st century (Bureau of Labor Statistics); plan an omnichannel path with a seller in it, not a rep-free one. [practitioner]

## Worked examples

### A comp plan decision

Situation: twelve-rep mid-market SaaS team. Three stars pass quota by month two and coast; six core reps
sit at 70–90%; three laggards under 50%. Proposal: a 2× accelerator above 120% plus an annual bonus.

- Keep the accelerator, uncapped and without a cliff at 120%: overachievement pay sustains stars; cliffs invite deal timing (Chung 2014; Larkin 2014). [study]
- Swap the annual bonus for quarterly bonuses to pace the three laggards (Chung 2014). [study]
- Show core reps three tiers, 90/100/110%: all-three-tiers reps outperformed in a field experiment (Steenburgh & Ahearne 2012). [study]
- Pay on booked quantity; audit discount depth and 90-day churn separately, since incentives move quantity more than quality (Cerasoli 2014). Simulate payouts before launch. [study]

### A coaching plan for a mid-ranked rep

Situation: rep ranks sixth of twelve at 85% of quota. Funnel last quarter: 120 leads worked, 48 connects
(40%, team 42%), 14 demos (29%, team 45%), 6 closes (43%, team 40%). The manager wants weekly "coach everything".

- The gap is connect-to-demo, so the fix is the first conversation, not activity; coach that stage only. [practitioner]
- One fix: a problem question before any product mention. Six role-play reps, then two recorded calls the rep critiques first. [practitioner]
- Hold other feedback for four weeks; middle-ranked reps gain most from coaching and one change beats six notes (Luo 2021). Re-measure demo rate at day 30. [study]

## Common mistakes and replacements

- "Hours and availability drive sales" → holds at best in high-velocity selling; train knowledge and adaptiveness and cut role ambiguity (Verbeke 2011). [study]
- Promote the best closer → promote on coaching skill and potential, and keep the closer's pay path open (Benson, Li & Shue 2019; Chung 2014). [study]
- Add more coaching sessions → build the manager's coaching skill first; frequent unskilled coaching hurt attainment (Dahling 2016). [study]
- Six notes after one call review → one fix and many reps; restricted feedback for bottom-ranked reps (Luo 2021). [study]
- Fire at 14 days in a B2B role → judge against the 3.0-month SDR ramp and the deal cycle (Bridge Group 2025); 14 days is a small-ticket, single-call rule. [data]
- Hire for extraversion or years of experience → structured interview on real selling tasks; experience at hire has validity .07 (Sackett 2022). [study]
- Quote "three coaching sessions took close rate from 20% to 75%" → a single anecdote; coaching effects depend on coach skill (Dahling 2016). [study]
- "Buyers prefer rep-free, so cut reps" → a preference, not an outcome: 43% vs 26% high regret (Gartner); redesign the rep's role around value clarity. [data]
- Cap commissions or add payout cliffs → uncapped overachievement on a smooth curve; cliffs invite deal timing (Chung 2014; Larkin 2014). [study]
- Give the AI the persuasion turn → AI generates and qualifies, humans persuade (Jia 2024); disclosure rules in `references/rapport.md`. [study]
