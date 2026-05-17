# Triple Crown Handicapping Framework v2

**Owner:** Ryan Shook · **Created:** 05-02-2026 · **Updated:** 05-17-2026 (Preakness T+1 recap)
**Source of truth.** All dashboards regenerate from this file.

---

## What changed in v2

- Extended the original 6-factor Derby framework to cover all three Triple Crown legs
- Added per-race factor weightings (Derby, Preakness, Belmont each weight differently)
- Added 2026 venue/distance overrides (Preakness at Laurel, Belmont at Saratoga 1 1/4 mi)
- Linked to the 2027 Derby Trail Tracker (separate doc)

## Core principle (unchanged)

Each factor scored 0–10. Composite = weighted average. Composite ≥ 6.0 = "live" alert. Tier-list scoring is the same as v1; only the **weights** change between races.

---

## Race-Specific Factor Weights

|                                   | Derby | Preakness | Belmont (1.5mi) | Belmont 2026 (1.25mi) |
|-----------------------------------|-------|-----------|-----------------|------------------------|
| 1. Sire Stamina Index             | 1.0×  | 0.6×      | **1.5×**        | 1.0×                   |
| 2. Pace Fit                       | 1.5×  | 1.0×      | 0.8×            | 1.0×                   |
| 3. Trainer Stable Activity        | 1.0×  | 1.0×      | 0.8×            | 0.8×                   |
| 4. Jockey Form                    | 1.0×  | 1.0×      | 1.0×            | 1.0×                   |
| 5. Beaten-Favorite Profile        | 1.2×  | 1.0×      | 0.8×            | 0.8×                   |
| 6. ML Drift                       | 1.0×  | 1.0×      | 1.0×            | 1.0×                   |
| 7. **Bounce Risk** (new)          | —     | **1.5×**  | **1.2×**        | **1.2×**               |
| 8. **Distance Pedigree** (new)    | —     | 0.5×      | **2.0×**        | 1.0×                   |
| 9. **Layoff Pattern** (new)       | —     | 0.8×      | **1.5×**        | 1.5×                   |

### Why the weights change

**Derby** — 20-horse field, fast contested pace, 10F. Pace fit dominates (the geometric edge).

**Preakness** — Smaller field (8-12), tighter Pimlico/Laurel turns, 9.5F. Pace pressure drops. The big new variable: **bounce risk**. Horses returning in 2 weeks off a hard Derby effort frequently regress. Plus most non-Derby horses in the Preakness are fresh "new shooters" — a structural advantage.

**Belmont** — Smallest field (6-9), 1.5 mi at Belmont Park is the longest dirt race for 3yos. **Stamina pedigree dominates everything**. Sire SSI weighted 1.5×, plus a separate "Distance Pedigree" factor weighted 2.0× (looks at dam side, broodmare sire, distance breeding). Layoff pattern matters because trainers who skip the Preakness and target Belmont with 5 weeks rest historically over-perform.

**Belmont 2026 (Saratoga, 1.25mi)** — Don't apply the full Belmont stamina premium. At 10F it's basically a Derby rerun with a smaller field. Use weights closer to the traditional Belmont but dial back distance pedigree.

---

## The Six Original Factors (v1)

(Unchanged from v1 framework — see appendix or v1 doc for tier lists.)

1. **Sire Stamina Index** — Curlin/Tapit = 10, sprinter sires = 4 or below
2. **Pace Fit** — Style × pace projection
3. **Trainer Stable Activity** — Horses on the day's full card
4. **Jockey Form** — Hot hand, Oaks/Friday wins
5. **Beaten-Favorite Profile** — Show finishes in major preps
6. **ML Drift** — Money flow vs morning line

## Three New Factors (v2)

### 7. Bounce Risk (Preakness only critical)

Measures regression risk after a hard Derby effort.

- **10** — Fresh horse, didn't run Derby, well-rested (ideal Preakness profile)
- **8** — Ran Derby off-the-board with easy trip, no major exertion
- **6** — Ran Derby in the money but had perfect trip, no hard finish
- **4** — Derby winner or close 2nd/3rd with hard stretch run (high bounce risk!)
- **2** — Derby horse who set/contested the pace and faded (worst bounce profile)

Counterintuitive but historically true: **Derby winners are often POOR Preakness bets** if they had a hard race. Last 10 Derby winners in the Preakness: 4 wins, 2 places, 4 off-the-board. The "Triple Crown story" is great TV but bad math.

### 8. Distance Pedigree (Belmont critical)

Beyond just sire — looks at the full pedigree's classic distance success.

- **10** — Sire AND dam side both elite at 1.5mi+ (e.g., Curlin × Tapit dam)
- **8** — Strong sire or strong dam side
- **6** — Adequate stamina, no red flags
- **4** — Speed pedigree dressed up as classic
- **2** — Pure speed/middle-distance pedigree

Belmont winners almost always have at least 8 here. Track the broodmare sire — A.P. Indy line, Sunday Silence (Japan), Sadler's Wells line all signal stamina.

### 9. Layoff Pattern (Belmont critical)

Pattern matters more than days. Standard recipes:

- **10** — Skipped Preakness, targeted Belmont with one work in between (5 wks rest)
- **9** — Came off Wood Memorial / Arkansas Derby, skipped Derby and Preakness
- **8** — Ran Derby, skipped Preakness, came back fresh
- **6** — Ran Derby AND Preakness, normal Triple Crown attempt
- **4** — Ran in all three races, deep into a long campaign
- **2** — Surprise entry, no clear training pattern

Modern Belmont winners are increasingly fresh horses. Targeting the Belmont specifically has become a viable trainer strategy — see Arcangelo (2023), Mo Donegal (2022), Tonalist (2014), Creator (2016).

---

## 2026 Triple Crown — Working File

### Preakness Stakes — Saturday, 05-16-2026 · 151st running

- **Venue:** Laurel Park (Pimlico under construction)
- **Distance:** 1 3/16 mi
- **Post:** 7:01 PM ET, NBC · Race 13 of 14
- **Field:** 14 horses (largest since 2011)
- **Purse:** $2,000,000
- **Derby horses returning:** Ocelli (3rd), Incredibolt (6th), Robusta (14th). **Golden Tempo (Derby winner) skipping** — pointing for Belmont 06-06-2026.

#### Pace projection (T-3, 05-13-2026)

10 of 14 horses have an early/early-presser preference. The lead cannot accommodate that many — expect a contested, fast pace early. **Closers and stalkers are favored** by the geometric setup. Watch: Ocelli, Talkin, Bull by the Horns, and Incredibolt are the four most likely beneficiaries.

#### 9-Factor Composite Scoring (Preakness weights)

Weights: SSI 0.6× · Pace 1.0× · Stable 1.0× · Jockey 1.0× · B-Fav 1.0× · Drift 1.0× · **Bounce 1.5×** · Distance 0.5× · Layoff 0.8×. ML Drift held at 5 (neutral) until final tote close on race day.

| PP | Horse | Sire | Trainer / Jockey | ML | SSI | Pace | Stbl | Jock | B-Fav | Drift | Bounce | Dist | Layoff | **Composite** |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | **Talkin** | Good Magic | Gargan / Irad Ortiz Jr. | 20-1 | 7 | 8 | 6 | 10 | 8 | 5 | 10 | 7 | 8 | **7.87** ★ |
| 9 | **Iron Honor** | Nyquist | C. Brown / F. Prat | 9-2 | 6 | 4 | 9 | 9 | 6 | 5 | 10 | 6 | 8 | **7.26** ★ |
| 6 | **Chip Honcho** | Connect | Asmussen / J. Ortiz | 5-1 | 6 | 4 | 8 | 9 | 6 | 5 | 10 | 6 | 9 | **7.24** ★ |
| 1 | **Taj Mahal** | Nyquist | B. Russell / S. Russell | 5-1 | 6 | 4 | 9 | 8 | 5 | 5 | 10 | 6 | 9 | **7.12** ★ |
| 8 | **Bull by the Horns** | Essential Quality | S. Joseph Jr. / Husbands | 30-1 | 8 | 8 | 7 | 5 | 3 | 5 | 10 | 8 | 9 | **7.02** ★ |
| 7 | The Hell We Did | Authentic | Fincher / Saez | 15-1 | 6 | 6 | 5 | 8 | 5 | 5 | 10 | 6 | 8 | **6.79** ★ |
| 12 | **Incredibolt** | Bolt d'Oro | R. Mott / Torres | 5-1 | 7 | 9 | 7 | 8 | 8 | 5 | 5 | 7 | 6 | **6.79** ★ |
| 2 | **Ocelli** | Connect | Beckman / Gaffalione | 6-1 | 6 | 9 | 7 | 8 | 9 | 5 | **4** | 6 | 6 | **6.60** ★ |
| 3 | Crupper | Candy Ride | Von Hemmel / Alvarado | 30-1 | 8 | 4 | 6 | 6 | 4 | 5 | 10 | 8 | 8 | **6.57** ★ |
| 11 | Corona de Oro | Bolt d'Oro | Stewart / Velazquez | 30-1 | 7 | 3 | 5 | 8 | 4 | 5 | 10 | 7 | 8 | **6.44** ★ |
| 10 | Napoleon Solo | Liam's Map | Summers / Lopez | 8-1 | 5 | 3 | 6 | 6 | 6 | 5 | 10 | 4 | 5 | 5.95 |
| 14 | Pretty Boy Miah | Beau Liam | Englehart / Santana Jr. | 15-1 | 5 | 3 | 6 | 6 | 2 | 5 | 10 | 5 | 7 | 5.73 |
| 4 | Robusta | Accelerate | O'Neill / Bejarano | 30-1 | 6 | 4 | 6 | 5 | 2 | 5 | 8 | 6 | 6 | 5.40 |
| 13 | Great White | Volatile | Ennis / Achard | 15-1 | 4 | 4 | 4 | 4 | 4 | 5 | 10 | 3 | 5 | 5.23 |

★ = composite ≥ 6.0, the framework's "live alert" threshold. **10 of 14 horses qualify.**

#### What the model sees that the market doesn't

**Talkin (20-1) tops the framework at 7.87.** The signal stack: Irad Ortiz pickup (10), closer style in a fast-pace setup (8), beaten-favorite profile from 2nd Champagne G1 and 3rd Blue Grass G1 (8), six weeks fresh off the prep season (8), zero bounce risk (10). **The framework's value play.**

**Ocelli (6-1) drops to 8th at 6.60 despite arguably the best raw form** — 3rd in the Derby, 3rd in the Wood, leading money winner. Why? **Bounce risk 4** drags her composite hard at 1.5× weight. Per the framework's tier list: "Derby winner or close 2nd/3rd with hard stretch run" = 4. She led in the stretch and finished 3rd a length back — textbook high-bounce profile. *The "Triple Crown story" is great TV but bad math* — the framework's exact lesson.

**Incredibolt (5-1) gets a moderate bounce demote** to 5 (rallied 14→6 with a traffic-altered effort — not as taxing as Ocelli's stretch run). Composite 6.79 still — closer pace fit + rally style. The most live Derby returnee.

**The 9-2 favorite Iron Honor lands 2nd at 7.26.** Brown/Prat rider upgrade, Wood trip excuse, bounce-risk-10 (skipped the Derby), but pace-compromised EP style and outside-then-inside post 9 in a 14-horse field hold him at 4 for Pace.

#### Formal Prediction (T-3 · 05-13-2026)

- **Win:** **Talkin** (composite 7.87, ML 20-1) — value play, rider-upgrade-driven
- **Place:** Iron Honor (7.26, 9-2)
- **Show:** Chip Honcho (7.24, 5-1)
- **Exacta key:** Talkin **over** Iron Honor + Chip Honcho + Taj Mahal + Bull by the Horns
- **Trifecta key:** Talkin / Iron Honor + Chip Honcho / Taj Mahal + Bull by the Horns + Incredibolt
- **Longshot value:** Bull by the Horns (30-1, composite 7.02) — closer + Essential Quality stamina + fresh
- **Confidence:** medium-low — model diverges sharply from market
- **Rationale tags:** `rider-upgrade`, `pace-fit-closer`, `beaten-fav-G1G3`, `fresh-no-bounce`, `distance-neutral`
- **Predicted winning Beyer:** 95-98

#### Suggested bet allocation

- 1u Talkin to win
- 0.5u Talkin to place
- 1u $1 exacta box: Talkin / Iron Honor / Chip Honcho
- 0.5u $1 trifecta key: Talkin over (Iron Honor, Chip Honcho, Taj Mahal, Bull by the Horns) over (same plus Incredibolt)
- 0.25u flier: Bull by the Horns to win at 30-1

#### Race-day adjustments to watch (T-1, Fri 05-15-2026)

- **ML Drift** is currently 5 (neutral). By race time update the Drift column with actual movement; recompute composites.
- **Weather** — wet track shifts pace bias toward early speed, would compress closer advantage. No rain currently forecast through Saturday.
- **Scratches** — if a heavy pace setter scratches (Napoleon Solo, Corona de Oro), pace projection softens.

#### Post-race recap (filled 05-17-2026)

**Order of finish:**
1. **Napoleon Solo** (Paco Lopez / Chad Summers, post-time 7.90-1, ML 8-1) — won by 1 1/4 lengths
2. Iron Honor (F. Prat / C. Brown)
3. Chip Honcho (J. Ortiz / Asmussen)
4. Ocelli (Gaffalione / Beckman)
5. Incredibolt (Torres / R. Mott)
6. Bull by the Horns
7. The Hell We Did
8. Great White
9. Robusta
10. Taj Mahal (post-time favorite — led early, collapsed)
11. Corona de Oro
12. **Talkin** ← our win pick
13. Crupper
14. Pretty Boy Miah

**Final time:** 1:58.69 — *slowest Preakness in 75 years*
**Fractions:** :22.66 / :46.66 (Taj Mahal led through the half, then collapsed)
**Beyer Speed Figure:** TBD — official figure not yet published as of 05-17-2026. Race time and "slowest in 75 years" framing suggest 80–85, well below our predicted 95–98.

**Prediction scoring:**
- **Win pick (Talkin, composite 7.87):** ❌ MISS — finished 12th. Biggest framework miss of the race.
- **Place pick (Iron Honor, 7.26):** ✅ HIT — 2nd place
- **Show pick (Chip Honcho, 7.24):** ✅ HIT — 3rd place
- **Exacta box (Talkin / Iron Honor / Chip Honcho):** Iron–Chip permutation HIT (2-3 finish). Payout TBD from official results.
- **Trifecta key (Talkin over...):** ❌ MISS — Napoleon Solo was not in our trifecta
- **Longshot flier (Bull by the Horns, 30-1):** ❌ MISS — finished 6th
- **Beyer delta:** Predicted 95–98 vs. actual TBD (likely well under 90 given the time)

**Bet allocation P/L (per the locked allocation, 05-13):**
- 1u Talkin WIN → −1u
- 0.5u Talkin PLACE → −0.5u
- 1u $1 exacta box Talkin/Iron/Chip → partial recovery via the Iron–Chip permutation (net pending official exacta payout)
- 0.5u $1 trifecta key → −0.5u
- 0.25u Bull by the Horns WIN → −0.25u
- **Net:** meaningful loss; exact figure depends on the official 9–6 exacta payout

**Trip notes & narrative:**
- Pace shape played out exactly as projected at the macro level: Taj Mahal (post 1) went to the lead through :22.66 / :46.66 and collapsed to 10th — the "10 of 14 EP/presser" warning was validated.
- BUT the winner Napoleon Solo (Pace 3 in our model) was a **stalker**, not a closer. He tracked Taj Mahal and pounced at the final turn. Our framework rated him 11th of 14 at composite **5.95 — below the 6.0 live-alert threshold**.
- Iron Honor (Pace 4, our #2) ran the trip we expected: drafted behind the duel, closed late, strong 2nd.
- Chip Honcho (Pace 4, our #3) similar — closed late for 3rd.
- Ocelli's bounce demote (composite 6.60, finished 4th) was probably too harsh; she ran credibly off the Derby.

**Rationale-tag validation:**
- `rider-upgrade` (Talkin/Irad Ortiz Jr.): **FAILED** — Talkin 12th. Rider upgrade couldn't overcome poor trip / pace mismatch.
- `pace-fit-closer`: **PARTIAL** — leaders died as predicted, but closers didn't capitalize; a stalker won. Refine: when 10+ EP/presser horses set up a duel, **stalkers benefit more than deep closers** (closers run out of ground if the overall pace is slow).
- `beaten-fav-G1G3` (Talkin Champagne 2nd, Blue Grass 3rd): **FAILED** — historical G1/G3 placings didn't translate.
- `fresh-no-bounce`: **NEUTRAL** — Talkin had bounce 10 but still ran 12th. Bounce factor is "necessary but not sufficient."
- `distance-neutral`: NEUTRAL — no clear signal at 1 3/16.

**Framework v2.1 calibration items (queue for Belmont prep, T-7 = 05-30-2026):**
1. **Add a stalker premium for projected speed duels.** Current Pace score conflates "low pace fit" with "bad trip." When the projection flags an EP-heavy field, give stalkers a `Pace_Adjusted = Pace + 2` bonus. Would have lifted Napoleon Solo from 5.95 → ~6.6 and put him on the radar.
2. **Soften bounce penalty for Derby 3rd-place horses.** Ocelli (Bounce 4) finished 4th — perfectly respectable. The "stretch run = high bounce" rule should distinguish wire-to-wire winners from come-from-behind 3rd-place finishers (less taxing pattern).
3. **Composite ≥ 6.0 hit rate this race:** 2 of top-3 in the money (Iron Honor 2nd, Chip Honcho 3rd); winner came from below threshold. The threshold is correctly screening "in-the-money" candidates but missing winners that get a perfect trip from sub-6.0 starting position.
4. **Beyer prediction needs a track/pace modulator.** Predicted 95–98 (extrapolated off Derby figures) was way high vs. an actual race that was the slowest in 75 years. Add a "projected pace × surface condition" deflator to the Beyer band.

**Belmont (06-06-2026, Saratoga 1 1/4 mi) implications:**
- Ocelli's credible 4th keeps her on the Belmont watch list if connections re-route.
- Napoleon Solo (Summers/Lopez — trainer's first TC win) — Belmont participation TBD; watch press today/tomorrow.
- Iron Honor closed well at 9.5F; the longer trip at Saratoga should suit. Promote on Belmont T-7 tracker.
- Apply the v2.1 weighting changes above to the Belmont T-7 watch list build.

#### Sources (scraped 05-12-2026)

- [Preakness 2026 post positions, odds, jockeys, trainers — NBC Sports](https://www.nbcsports.com/horse-racing/news/2026-preakness-post-positions-full-draw-horses-starting-gate-order-odds-jockeys-trainers-owners)
- [Preakness Stakes 2026: Odds, analysis of the 14-horse field — Horse Racing Nation (Matt Shifman)](https://www.horseracingnation.com/news/Preakness_Stakes_2026_Odds_and_analysis_of_the_14_horse_field_123)

### Belmont Stakes — Saturday, 06-06-2026

- **Venue:** Saratoga Race Course (final year before Belmont Park reopens)
- **Distance:** 1 1/4 mi (third year shortened from 1 1/2 mi)
- **Post:** 6:50 PM ET, FOX
- **Key prep:** Peter Pan Stakes (G3), Saratoga, ~05-12-2026
- **Key handicap:** Because it's only 10F at Saratoga, treat closer to Derby framework than traditional Belmont. Don't over-weight distance pedigree.

**Pre-race tracker (update as entries finalize):**
| Horse | Trainer/Jockey | ML | SSI | Pace | Stbl | Jock | B-Fav | Drift | Layoff | Composite |
|-------|----------------|-----|-----|------|------|------|-------|-------|--------|-----------|
| _TBD as entries open ~ 06-03-2026 — triple-crown-race-brief task will populate on T-7 (05-30-2026)_ | | | | | | | | | | |

---

## Annual Operating Cadence (post-Derby through Belmont)

| Date | Task | Output |
|------|------|--------|
| 05-02-2026 | Derby post-mortem | Update v1 model gaps, identify bounce risks |
| 05-04-2026 | Preakness watch list | Note likely entries from Wood/Arkansas Derby |
| 05-13-2026 | Preakness entries open | ✅ Run framework, post composite scores (this update) |
| 05-15-2026 | Preakness T-1 brief | triple-crown-race-brief refresh w/ final odds |
| 05-16-2026 | Preakness race | Lock predictions, run bets |
| 05-17-2026 | Preakness T+1 recap | ✅ Done — see recap above. Calibration items queued for v2.1. |
| 05-19-2026 | Belmont watch list | Track Peter Pan, note skip-Preakness horses |
| 05-30-2026 | Belmont T-7 brief | triple-crown-race-brief watchlist |
| 06-03-2026 | Belmont entries | Run framework |
| 06-05-2026 | Belmont T-1 brief | triple-crown-race-brief final brief |
| 06-06-2026 | Belmont race | Lock predictions, run bets |
| 06-07-2026 | Belmont T+1 recap | Score predictions; fire season calibration |
| 06-08-2026 | Triple Crown wrap-up | Full post-mortem, framework v3 update |

---

## Linked: 2027 Derby Trail Tracker

After Belmont 2026, the 2yo races leading to the 2027 Derby kick off in September. The seven key prep races for 2027 — Iroquois Stakes, Breeders' Cup Juvenile, Virginia Derby, Louisiana Derby, Florida Derby, Wood Memorial, Santa Anita Derby — are tracked by the `derby-prep-race-brief` scheduled task. See `projects/derby-2027/` for that flow.

## Cowork Automation Hook

Active scheduled task: `triple-crown-race-brief` (created 05-13-2026)

```
Cron: 0 7 15 * * *  (daily 07:15 America/New_York)
T-7 / T-1 / T+1 cadence around each Triple Crown leg
Writes back to this file via Make.com → GitHub
Logs predictions to projects/triple-crown/predictions/log.md
Belmont T+1 fires the season-end framework calibration
```

Source: `~/projects/triple-crown/framework.md` (this file, on GitHub `verdet3232/claude-memory`)
Renderer: Cowork artifact `derby-dashboard` (auto-refreshes on open via Firecrawl)
Notify: Email to rshook74@gmail.com on race weeks
