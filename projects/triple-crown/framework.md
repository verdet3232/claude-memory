# Triple Crown Handicapping Framework v2.1

**Owner:** Ryan Shook · **Created:** 05-02-2026 · **Updated:** 06-05-2026 (Belmont T-1 post-draw field + prediction)
**Source of truth.** All dashboards regenerate from this file.

---

## What changed in v2

- Extended the original 6-factor Derby framework to cover all three Triple Crown legs
- Added per-race factor weightings (Derby, Preakness, Belmont each weight differently)
- Added 2026 venue/distance overrides (Preakness at Laurel, Belmont at Saratoga 1 1/4 mi)
- Linked to the 2027 Derby Trail Tracker (separate doc)

## What changed in v2.1 (05-17-2026)

Driven by Preakness 2026 recap miss + 5-year backtest 2021–2025 (`backtest-2021-2025.md`).

- **Added Factor 10: Recent Speed Index** — average of last 3 Beyer figures relative to field, scored 0-10. Weight 1.2× across all legs (1.0× at traditional Belmont 1.5mi). Catches "improving rapidly" signal that v2 missed for Rich Strike '22 (composite 4.2) and Mage '23 (composite 5.8).
- **Stalker premium**: when pace projection flags ≥10 EP/Presser horses, Stalker-style runners get +2 Pace fit. Napoleon Solo (today's Preakness winner) would have lifted from 5.95 → ~6.6.
- **Class Ceiling**: Beaten-Favorite tier list now distinguishes G1 *winners* from G1 *placers*. G1 winner = 9; G1 2nd = 6.
- **Rank-based tier replaces composite ≥ 6.0 threshold.** Field-relative: Top-3 composites = `Tier A`, ranks 4-6 = `Tier B` (live), 7+ = `Tier C` (longshot). Eliminates the "10 of 14 flagged" problem.
- **Finer Bounce-Risk tiers** (Preakness): added 8 (Derby off-the-board easy trip), kept 6 (Derby in-money easy trip), 4 (Derby winner/close 2-3rd hard run). Soften penalty for Derby 3rd-placers with come-from-behind trips.
- **Beyer prediction modulator**: when projected pace is slow OR track is sloppy, bias the predicted-winning-Beyer band DOWN by 6-10. Today's Preakness 96 actual vs. predicted 95-98: tight, but only because pace projection happened to be wrong. A slow-pace Preakness should predict 88-92.

Backtest hit rate at v2 composite ≥ 6.0: **10 of 15 = 66.7%** of winners. v2.1 targets >80% by catching the Rich Strike / Mage / Dornoch pattern via Recent Speed Index + Stalker premium.

---

## Core principle (v2.1 updated — see below)

Each factor scored 0–10. Composite = weighted average. **v2.1: rank-based tier replaces absolute threshold.** Field-relative tiers: Top-3 composites = `Tier A` (high confidence); ranks 4-6 = `Tier B` (live); rank 7+ = `Tier C` (longshot territory). Tier-list scoring per factor unchanged from v1; only the **weights** and the **tier mapping** change between races.

---

## Race-Specific Factor Weights

|                                                   | Derby | Preakness | Belmont (1.5mi) | Belmont 2026 (1.25mi) |
|---------------------------------------------------|-------|-----------|-----------------|------------------------|
| 1. Sire Stamina Index                             | 1.0×  | 0.6×      | **1.5×**        | 1.0×                   |
| 2. Pace Fit *(v2.1: + Stalker premium)*           | 1.5×  | 1.0×      | 0.8×            | 1.0×                   |
| 3. Trainer Stable Activity                        | 1.0×  | 1.0×      | 0.8×            | 0.8×                   |
| 4. Jockey Form                                    | 1.0×  | 1.0×      | 1.0×            | 1.0×                   |
| 5. Beaten-Favorite + Class Ceiling *(v2.1)*       | 1.2×  | 1.0×      | 0.8×            | 0.8×                   |
| 6. ML Drift                                       | 1.0×  | 1.0×      | 1.0×            | 1.0×                   |
| 7. Bounce Risk *(v2.1: finer tiers)*              | —     | **1.5×**  | **1.2×**        | **1.2×**               |
| 8. Distance Pedigree                              | —     | 0.5×      | **2.0×**        | 1.0×                   |
| 9. Layoff Pattern                                 | —     | 0.8×      | **1.5×**        | 1.5×                   |
| **10. Recent Speed Index** *(NEW v2.1)*           | **1.2×** | **1.2×** | 1.0×          | **1.2×**               |
| 11. Post-Position Bias *(NEW v2.1, optional)*     | 0.5×  | 0.5×      | 0.3×            | 0.3×                   |

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

### 10. Recent Speed Index (NEW v2.1 — Derby + Preakness + short-Belmont critical)

Average of last 3 Beyer Speed Figures, scored relative to the field.

- **10** — Top Beyer in field; trajectory ↑ over last 3 starts
- **8** — Top-3 Beyer in field
- **6** — Mid-field Beyer; recent form solid
- **4** — Bottom-third Beyer; no clear improvement signal
- **2** — Slow/declining; bottom of field

Backtest motivation: Mystik Dan 2024 (Beyer 101 in last start) and Mage 2023 (Beyer 95) had above-field Beyers that v2 didn't surface; Rich Strike 2022 had improving trajectory from 78 → 85 → 92 over 3 starts that wasn't captured by the Sire/Pace/B-Fav stack. Recent Speed Index is the most powerful single public predictor in handicapping and the framework had been ignoring it.

### 11. Post-Position Bias (NEW v2.1, optional)

Track-and-field-size-specific historical performance from the post position drawn.

- **10** — Statistically favored PP for the track + field size (e.g., outside posts at 14-horse Pimlico)
- **6** — Neutral PP
- **2** — Statistically disfavored (e.g., rail at 14-horse Pimlico; far-outside at 8-horse Belmont)

Weight 0.5× at Derby/Preakness; 0.3× at Belmont. Most signal is at Pimlico/Laurel where the rail consistently collapses in big fields.

Mark this factor "skipped" when historical data for the specific track+field size isn't available — don't fabricate.

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

#### Formal Prediction (LOCKED T-1 · 05-15-2026)

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

#### T-1 Race-Day Brief (05-15-2026) — locked

**Status check** at 07:15 ET, T-1:

- **Scratches:** None. Full 14-horse field intact.
- **Track:** Laurel Park dirt **Fast**, turf Firm (per Equibase race-day update 05-15-2026 10:06 AM ET).
- **Weather:** Fair, 59°F, wind WNW 13 mph. No rain in forecast through Saturday post time → closer/stalker geometric edge from T-3 pace projection **holds**.
- **ML Drift:** Live tote (TwinSpires, as of 05-14-2026 11:59 AM EDT) matches morning line 1:1 across all 14 horses. **Drift = 0 to date** — column stays at 5 (neutral) per methodology. Real Drift event = final tote close on race day; will be scored at T+1 against the 4 PM, 5 PM, and final ET windows.
- **Equipment / rider changes:** None reported on Preakness entrants.
- **Pace projection:** Unchanged — Chip Honcho, Robusta, Corona de Oro, Napoleon Solo, Pretty Boy Miah, Crupper all want the early lead. Contested fast pace setup remains live. Closers/stalkers (Talkin, Iron Honor, Incredibolt, Bull by the Horns, Ocelli) retain the geometric advantage.

**Net effect on composites:** No change to the 9-factor scoring vs. T-3. Prediction is **locked** below; bet allocation unchanged. Final Drift recompute happens at the wire (T+0); recap and scoring at T+1 (05-17-2026).

#### Race-day adjustments to watch (T-1, Fri 05-15-2026)

- **ML Drift** is currently 5 (neutral). By race time update the Drift column with actual movement; recompute composites.
- **Weather** — wet track shifts pace bias toward early speed, would compress closer advantage. No rain currently forecast through Saturday.
- **Scratches** — if a heavy pace setter scratches (Napoleon Solo, Corona de Oro), pace projection softens.

#### T+1 Post-Race Recap (05-17-2026) — final

**Order of finish (margin / cumulative beaten):**

| Fin | PP | Horse | Jockey / Trainer | Margin | ML | Composite (pre-race) |
|---:|---:|---|---|---:|---:|---:|
| **1** | 10 | **Napoleon Solo** | P. Lopez / C. Summers | 1¼ | 8-1 | 5.95 |
| **2** | 9 | Iron Honor | F. Prat / C. Brown | 3¼ | 9-2 | 7.26 |
| **3** | 6 | Chip Honcho | J. Ortiz / Asmussen | 2¾ | 5-1 | 7.24 |
| 4 | 2 | Ocelli | Gaffalione / Beckman | — | 6-1 | 6.60 |
| 5 | 12 | Incredibolt | Torres / R. Mott | — | 5-1 | 6.79 |
| 6 | 8 | Bull by the Horns | Husbands / Joseph Jr. | — | 30-1 | 7.02 |
| 7 | 7 | The Hell We Did | Saez / Fincher | — | 15-1 | 6.79 |
| 8 | 13 | Great White | Achard / Ennis | — | 15-1 | 5.23 |
| 9 | 4 | Robusta | Bejarano / O'Neill | — | 30-1 | 5.40 |
| 10 | 1 | Taj Mahal | S. Russell / B. Russell | — | 5-1 | 7.12 |
| 11 | 11 | Corona de Oro | Velazquez / Stewart | — | 30-1 | 6.44 |
| **12** | 5 | **Talkin** (predicted win) | I. Ortiz Jr. / Gargan | — | 20-1 | **7.87** |
| 13 | 3 | Crupper | Alvarado / Von Hemel | — | 30-1 | 6.57 |
| 14 | 14 | Pretty Boy Miah | Santana Jr. / Englehart | — | 15-1 | 5.73 |

**Final time / fractions:** 1:58.69 — :22.66 · :46.66 · 1:12.08

**Beyer Speed Figure:** **96** (Napoleon Solo) — source: Daily Racing Form post-race.

**Payoffs ($2 base):**
- W/P/S: Napoleon Solo $17.80 / $9.80 / $7.40
- Iron Honor place $9.20, show $6.60
- Chip Honcho show $8.20
- $2 Exacta (10-9): **$107.20**
- $2 Trifecta (10-9-6): **$1,194.20**
- $2 Superfecta (10-9-6-2): **$4,755.60**

**Trip notes:**
- Pace was honest-moderate, **NOT** the contested-fast meltdown the framework projected. Trainer Summers said pre-race he expected ":47s and :48s" — the half went in :46.66, exactly as the winning camp diagnosed.
- Taj Mahal broke from the rail and set the pace, lone and uncontested; **Napoleon Solo stalked from PP 10**, took over on the far turn, and drew off — tactical stalking trip from a horse with cruising speed.
- Iron Honor closed from midpack, was the only real threat in the lane, never got closer than 1¼.
- Chip Honcho sat 4th on the backstretch, plugged for 3rd.
- Closers Ocelli (4th) and Incredibolt (5th) were stranded by the honest pace — the projected geometric edge for closers never materialized.
- **Talkin** (predicted winner, 20-1): no notable trip excuse; finished a well-beaten 12th. Irad Ortiz couldn't manufacture a closing kick into a soft pace.

**Prediction scoring (vs. T-1 lock):**

| Bet | Prediction | Result | Hit? |
|---|---|---|---|
| Win | Talkin | 12th | ❌ MISS |
| Place | Iron Honor | 2nd | ✅ HIT |
| Show | Chip Honcho | 3rd | ✅ HIT |
| Exacta key (Talkin over) | Talkin / Iron Honor box | Talkin 12th | ❌ MISS |
| Trifecta key (Talkin / IH+CH / TM+BBH+IB) | — | Talkin 12th | ❌ MISS |
| Longshot value | Bull by the Horns | 6th | ❌ MISS |
| Beyer prediction | 95-98 | 96 | ✅ HIT (TIGHT) |

**Net P/L on suggested 3.25u allocation:** -3.25u (entire ticket misses; place/show on Talkin do not pay).

**Rationale-tag validation:**

| Tag | Verdict | Why |
|---|---|---|
| `rider-upgrade` | ❌ INVALIDATED | Irad Ortiz on Talkin → 12th. Rider upgrade is necessary but not sufficient; pace fit dominates. |
| `pace-fit-closer` | ❌ INVALIDATED | Pace setup never developed. Six "early/early-presser" horses on paper, but Taj Mahal got an uncontested lead at :22.66 and Napoleon Solo had clear sailing in second. **Framework's pace projection was the single biggest miss.** |
| `beaten-fav-G1G3` | ⚠ MIXED | The horse with the best G1 form (Napoleon Solo, Champagne G1 winner) won. But our application was to Talkin (2nd Champagne G1, 3rd Blue Grass G3) who flopped. The tag-target was wrong. |
| `fresh-no-bounce` | ✅ VALIDATED IN CONCEPT | Winner (Napoleon Solo) was fresh, no Derby start, six weeks off the Wood. Tag scored correctly on the right horse — we just didn't apply 10s here. |
| `distance-neutral` | ⚪ NEUTRAL | 9.5F was no obstacle for the winner. No signal either way. |

**Framework miss — what the model under-weighted:**

1. **Napoleon Solo composite 5.95 was the biggest single-horse mis-rate.** The framework scored him below the 6.0 live-alert threshold despite (a) being the only G1 winner in the field, (b) Lopez/Summers having a positive-EP profile, (c) classic "fresh-skipped-Derby" archetype the framework explicitly rewards in Belmont but under-rates at Preakness. **Sire Stamina (Liam's Map, broodmare sire Scat Daddy) was scored 5 — too low for a horse who had already won a G1 at Aqueduct two-turn.**
2. **Pace projection was the worst input.** We assumed six pace types would collapse the lead; in fact only Taj Mahal pressed early, and Napoleon Solo (mis-classified as a presser, more accurately a stalker with cruising speed) sat the perfect trip. **Pace fit weights at 1.0× hid the magnitude of this miss.**
3. **Beaten-favorite tier list rewarded G1 *place* finishes (Talkin's 2nd Champagne) more than G1 *wins* (Napoleon Solo's 6½-length Champagne romp).** Should be inverted — actual G1 winners beat G1 place-getters at the classics.
4. **Bounce-risk 10 for "skipped Derby" was correct in direction but indiscriminate** — 8 of 14 horses got the max bounce score, neutralizing the factor. Need finer tiering.

These four observations seed the Belmont T-7 reweighting and the post-Belmont calibration pass.

#### Sources

**T-3 scrape (05-12-2026):**
- [Preakness 2026 post positions, odds, jockeys, trainers — NBC Sports](https://www.nbcsports.com/horse-racing/news/2026-preakness-post-positions-full-draw-horses-starting-gate-order-odds-jockeys-trainers-owners)
- [Preakness Stakes 2026: Odds, analysis of the 14-horse field — Horse Racing Nation (Matt Shifman)](https://www.horseracingnation.com/news/Preakness_Stakes_2026_Odds_and_analysis_of_the_14_horse_field_123)

**T-1 scrape (05-15-2026):**
- [2026 Preakness Stakes Full field, odds, analysis — NBC Sports](https://www.nbcsports.com/horse-racing/news/2026-preakness-stakes-full-field-odds-analysis-and-prediction)
- [Preakness odds, betting, horses, post position — Yahoo Sports (05-14-2026)](https://sports.yahoo.com/horse-racing/betting/article/preakness-odds-betting-horses-post-position-updated-field-iron-honor-is-favorite-in-second-triple-crown-race-153151110.html)
- [2026 Preakness Stakes live odds — TwinSpires (as of 05-14-2026 11:59 AM EDT)](https://www.twinspires.com/preakness-stakes/odds/)
- [Laurel Park race-day changes & weather — Equibase (05-15-2026 10:06 AM ET)](https://www.equibase.com/static/latechanges/html/latechangeslrl-USA.html)

**T+1 scrape (05-17-2026):**
- [Preakness S. (G1) race page — BloodHorse](https://www.bloodhorse.com/horse-racing/race/usa/lrl/2026/5/16/13/preakness-s-g1)
- [Napoleon Solo Shines in Preakness, Repels Iron Honor — BloodHorse](https://www.bloodhorse.com/horse-racing/articles/291901/napoleon-solo-shines-in-preakness-repels-iron-honor)
- [Beyer 96 confirmation — DRF on X](https://x.com/DailyRacingForm/status/2056033566673272892)

### Belmont Stakes — Saturday, 06-06-2026 · 158th running

- **Venue:** Saratoga Race Course (final year before Belmont Park reopens — $455M rebuild)
- **Distance:** 1 1/4 mi (third year shortened from 1 1/2 mi)
- **Post:** 7:04 PM ET, FOX (per NYRA countdown clock as of T-7) · NBC slot earlier noted in v2 corrected here
- **Purse:** $2,000,000 · **Field cap:** 14 · **Weights:** Colts 126 lbs, Fillies 121 lbs
- **Post draw:** Monday 06-01-2026, 5:00 PM ET
- **Key prep:** Peter Pan Stakes (G3), Aqueduct, 05-09-2026 (won by Growth Equity by 2)
- **Key handicap:** Because it's only 10F at Saratoga, treat closer to Derby framework than traditional Belmont. Don't over-weight Distance Pedigree (1.0× not 2.0×).

#### T-7 Probable-Field Watchlist (locked 05-30-2026)

Per task spec ML Drift and Post-Position Bias are **blank at T-7** — composite computed on the remaining 9 weighted factors. Belmont 2026 weights: SSI 1.0× · Pace 1.0× · Stable 0.8× · Jockey 1.0× · B-Fav 0.8× · Bounce 1.2× · Distance 1.0× · Layoff 1.5× · Recent Speed 1.2× (sum = 9.5). Field-relative tiers per v2.1 (Top-3 = Tier A, ranks 4-6 = Tier B, 7+ = Tier C).

| Rank | Horse | Sire / Broodmare Sire | Trainer / Jockey | Early ML | SSI | Pace | Stbl | Jock | B-Fav | Bounce | Dist | Layoff | RSI | **Composite** | Tier |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | **Golden Tempo** | Curlin / Bernardini | C. DeVaux / J. Ortiz | 9-2 | 10 | 6 | 9 | 10 | 10 | 6 | 10 | 8 | 10 | **8.67** | A |
| 2 | **Renegade** | Into Mischief / Curlin | T. Pletcher / I. Ortiz Jr. | 9-5 | 7 | 7 | 10 | 10 | 8 | 6 | 7 | 8 | 9 | **7.94** | A |
| 3 | **Chief Wallabee** | Constitution / Medaglia d'Oro | B. Mott / J. Alvarado | 7-1 | 8 | 7 | 10 | 9 | 7 | 7 | 9 | 8 | 7 | **7.94** | A |
| 4 | **Growth Equity** | Nyquist / Wildcat Heir | C. Brown / F. Prat | 8-1 | 5 | 7 | 10 | 10 | 6 | 10 | 6 | 9 | 6 | **7.74** | B |
| 5 | **Commandment** | Into Mischief / Orb | B. Cox / L. Saez | 12-1 | 7 | 7 | 9 | 8 | 7 | 8 | 8 | 8 | 7 | **7.66** | B |
| 6 | **Ottinho** | Quality Road / unknown | C. Brown / TBA | 25-1 | 7 | 6 | 10 | 6 | 6 | 7 | 7 | 9 | 6 | **7.15** | B |
| 7 | Emerging Market | unknown / unknown | C. Brown / TBA | 18-1 | 6 | 6 | 10 | 6 | 6 | 8 | 7 | 8 | 6 | **7.01** | C |
| 8 | Iron Honor | Nyquist / unknown | C. Brown / TBA | 14-1 | 6 | 7 | 10 | 7 | 7 | 4 | 6 | 4 | 7 | **6.19** | C |
| 9 | Napoleon Solo *(TBC)* | Liam's Map / Scat Daddy | C. Summers / P. Lopez | 6-1 | 6 | 7 | 6 | 7 | 9 | 3 | 6 | 4 | 6 | **5.77** | C |
| 10 | Ocelli *(TBC)* | Connect / unknown | W. Beckman / TBA | 25-1 | 7 | 7 | 6 | 6 | 7 | 3 | 7 | 4 | 6 | **5.71** | C |

ML and Drift columns will populate at T-1 (06-05-2026) after the 06-01-2026 post draw. PP-Bias column will be added after the draw.

**Watchlist-only (insufficient data for scoring at T-7):**
- **Powershift** (Pletcher / TBA) — Repole Stable, breezed at Saratoga in tandem with Renegade. Pletcher's "second string" but profile matches the Belmont-fresh recipe. Score at T-1 once entries confirm.
- **Vitruvian Man** (Doug O'Neill / TBA) — Glenn Sorgenstein WC Racing. Listed by NYRA but not in the major handicapping previews. Confirm intent at the draw.
- **Chip Honcho** (Preakness 3rd) — Possible per MyWinners; profile mirrors Iron Honor with worse layoff (back in 3 weeks). Tier C if entered.
- **Talk to Me Jimmy** (Peter Pan 2nd) — Possible; thin résumé, longshot if entered.

#### What the model sees at T-7

**Golden Tempo (8.67) leads the watchlist** on a stack the framework can hardly avoid rewarding: Curlin sire (SSI 10, Distance 10), the field-best 106 Equibase from the Derby (RSI 10), Jose Ortiz back aboard (Jockey 10), G1-winner Beaten-Favorite tier (10), and the *exact* layoff recipe the framework rewards at 1.5× weight ("Ran Derby, skipped Preakness, came back fresh" = 8 plus the Pletcher/DeVaux Belmont-prep pattern). The one real ding is Bounce 6 — the Derby was a hard last-to-first run from the clouds, and the framework's v2.1 finer-tier list now distinguishes "hard stretch run" from "easy trip." But Bounce 6 at 1.2× is a 1.4-pt drag against a stack that's otherwise nine 8-10s. **He's the model's clear T-7 win candidate.**

**Renegade and Chief Wallabee tie at 7.94** for ranks 2-3. Renegade's profile is the textbook Pletcher Belmont setup (Stable 10, Jockey 10, Layoff 8, RSI 9) held back by mid-tier Distance Pedigree (Into Mischief is a speed-leaning sire even with the Curlin broodmare) and Bounce 6 from a hard rail-trip Derby. Chief Wallabee is the inverse: weaker raw speed (RSI 7) but elite stamina pedigree (Distance 9) and the Mott-at-Saratoga premium (Stable 10) coming off a clean Derby 4th — the lowest-bounce-risk profile of the top three. **Both are Tier A live alerts; the post draw 06-01 will likely separate them.**

**Growth Equity (7.74, Tier B) is the framework's favorite "fresh" value.** Never ran the Derby or Preakness, won the traditional Belmont prep (Peter Pan G3) stalking, Chad Brown / Flavien Prat, max Bounce risk score (10), and the Layoff recipe scored 9 ("Came off Wood/Arkansas Derby equivalent, skipped Derby and Preakness"). Distance Pedigree 6 (Nyquist over a Wildcat Heir mare — Brown himself flagged the distance question post-Peter Pan) is the only real concern.

**Commandment (7.66, Tier B)** rounds out the live group — Florida Derby G1 winner, lightly raced, Derby 7th "off-the-board easy trip" (Bounce 8), classic Brad Cox setup. Recent Speed 7 (Beyer 101) and Pace 7 (stalking grinder) both fit Saratoga's tighter configuration.

**Ottinho (7.15, Tier B)** is the longshot the framework upgrades — Quality Road sire, second in the Blue Grass G1, six clean works since, "skipped Derby and Preakness" Layoff 9. If Brown declares him alongside Growth Equity (and possibly Emerging Market), the three-Brown ticket structure could compress prices on Growth Equity and create value on Ottinho.

**Bottom of the watchlist: Napoleon Solo (5.77) and Ocelli (5.71)** both pay the Bounce + Layoff tax for running the Preakness. Napoleon Solo's connections have signaled the Haskell may be the real target — entry status is genuinely uncertain. Iron Honor at 6.19 sits in the same bucket. Belmont 2026 weights penalize Triple Crown campaigners more than the traditional 1.5mi Belmont did, because Recent Speed and Layoff carry more weight here than Distance Pedigree.

#### Pace projection (preliminary T-7, refine at T-1)

Of the top 6 in the watchlist, only Renegade has any forward-press option. Golden Tempo, Chief Wallabee, Growth Equity, Commandment, Ottinho all profile as stalkers or deep closers. **If the field finalizes near this watchlist, the Preakness pace problem repeats — there isn't enough natural early speed to manufacture a contested pace.** That's the exact setup that flopped Talkin at 20-1 in the Preakness. Watch for any speed-type "new shooter" entering between now and the 06-01 draw (a Robusta-type pace presence, or Powershift if Pletcher uses him as a rabbit).

If the pace remains soft, the framework's tier list disadvantages Golden Tempo (deep closer) and slightly favors Chief Wallabee (tactical stalker). Will revisit at T-1.

#### Sources (T-7 scrape, 05-30-2026)

- [2026 Belmont Stakes: Probable Horses — NYRA](https://www.nyra.com/belmont-stakes/racing/belmont-stakes-contenders/)
- [Bet the Belmont Stakes: 2026 Contenders Full Field Guide — MyWinners (Rob Lawson, 05-26-2026)](https://mywinners.com/blog/2026-belmont-stakes-contenders-full-field-guide)
- [2026 Belmont Stakes Cheat Sheet — America's Best Racing](https://www.americasbestracing.net/the-sport/2026-2026-belmont-stakes-cheat-sheet)
- [Belmont Stakes 2026: Overseas odds for June 6 at Saratoga — Horse Racing Nation](https://www.horseracingnation.com/news/Belmont_Stakes_2026_Overseas_odds_for_June_6_at_Saratoga_123)
- [2026 Belmont Stakes odds, date, predictions — CBS Sports](https://www.cbssports.com/general/news/2026-belmont-stakes-odds-date-predictions-expert-who-hit-4-of-last-8-winners-releases-horse-racing-picks/)

#### T-1 Post-Draw Field & Composites (locked 06-05-2026)

**Post draw:** Monday 06-01-2026, 5:00 PM ET. **Field finalized at 9** (cap was 14). Three Preakness runners from the T-7 watchlist — Iron Honor, Napoleon Solo, Ocelli — did **not** enter (Napoleon Solo pointed to the Haskell). Two T-7 "watchlist-only" names drew in: **Powershift** (Pletcher's second Repole colt) and **Vitruvian Man** (Doug O'Neill shipper off a Santa Anita Derby 3rd).

**Official field — program/post order:**

| PP | Horse | ML | Jockey | Trainer | Style | KY Derby |
|---:|---|---:|---|---|---|---|
| 1 | Vitruvian Man | 30-1 | A. Fresu | D. O'Neill | Presser | DNR (SA Derby 3rd) |
| 2 | Powershift | 12-1 | L. Saez | T. Pletcher | Closer | DNR |
| 3 | Chief Wallabee | 3-1 | J. Alvarado | B. Mott | Presser | 4th |
| 4 | Renegade | 2-1 | I. Ortiz Jr. | T. Pletcher | Closer | 2nd |
| 5 | Ottinho | 20-1 | D. Davis | C. Brown | Stalker | DNR (Blue Grass 2nd) |
| 6 | Growth Equity | 12-1 | M. Franco | C. Brown | Presser | DNR (Peter Pan win) |
| 7 | Commandment | 6-1 | J. Velazquez | B. Cox | Stalker | 7th |
| 8 | Emerging Market | 6-1 | F. Prat | C. Brown | Closer | DNR |
| 9 | Golden Tempo | 9-2 | J. Ortiz | C. DeVaux | Closer | **1st** |

Derby rematch at the top: **Golden Tempo (Derby winner) vs Renegade (Derby 2nd)** — but the market sides with Renegade (2-1) over Chief Wallabee (3-1) and the winner Golden Tempo (9-2). Chad Brown saddles three (Ottinho, Growth Equity, Emerging Market) and **Flavien Prat chose Emerging Market**, not Peter Pan winner Growth Equity — a jockey-selection tell.

**Composites — Belmont-2026 weights (sum 10.8):** SSI 1.0 · Pace 1.0 · Stable 0.8 · Jockey 1.0 · B-Fav 0.8 · **Drift 1.0** · Bounce 1.2 · Distance 1.0 · Layoff 1.5 · Recent Speed 1.2 · **PP-Bias 0.3**. ML Drift held at 5 (neutral) — live tote matches the morning line the day before; real Drift is scored at the wire (T+0). PP-Bias held at 6 (neutral) — Saratoga at 1¼ mi has only a 2024-25 sample; rail read deferred to race day per the framework's "don't fabricate" rule.

| Rank | PP | Horse | ML | SSI | Pace | Stbl | Jock | B-Fav | Drift | Bounce | Dist | Layoff | RSI | PP | **Comp** | Tier |
|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 9 | **Golden Tempo** | 9-2 | 10 | 5 | 9 | 10 | 10 | 5 | 6 | 10 | 8 | 10 | 6 | **8.17** | A |
| 2 | 3 | **Chief Wallabee** | 3-1 | 8 | 8 | 10 | 9 | 7 | 5 | 7 | 9 | 8 | 7 | 6 | **7.70** | A |
| 3 | 4 | **Renegade** | 2-1 | 7 | 6 | 10 | 10 | 8 | 5 | 6 | 7 | 8 | 9 | 6 | **7.52** | A |
| 4 | 7 | Commandment | 6-1 | 7 | 7 | 9 | 8 | 7 | 5 | 8 | 8 | 8 | 7 | 6 | **7.37** | B |
| 5 | 6 | Growth Equity | 12-1 | 5 | 8 | 10 | 8 | 6 | 5 | 10 | 6 | 9 | 6 | 6 | **7.34** | B |
| 6 | 5 | Ottinho | 20-1 | 7 | 7 | 10 | 7 | 6 | 5 | 7 | 7 | 9 | 6 | 6 | **7.10** | B |
| 7 | 8 | Emerging Market | 6-1 | 6 | 5 | 10 | 9 | 6 | 5 | 8 | 7 | 8 | 6 | 6 | **6.98** | C |
| 8 | 2 | Powershift | 12-1 | 6\* | 5 | 9 | 8 | 4 | 5 | 8 | 6\* | 7 | 5\* | 6 | **6.32** | C |
| 9 | 1 | Vitruvian Man | 30-1 | 6\* | 7 | 6 | 5 | 5 | 5 | 7 | 6\* | 7 | 5\* | 6 | **5.97** | C |

`*` = sire / broodmare-sire / recent figure not scraped for the two late-confirmed entrants; scored neutral and flagged — **not researched values**. Refine at T+0 once connections/figures publish.

**Pace projection (T-1) — the sharpest read on the race:** four closers (Renegade, Golden Tempo, Emerging Market, Powershift), two stalkers (Commandment, Ottinho), three pressers (Chief Wallabee, Growth Equity, Vitruvian Man). **No natural early speed.** This is the same no-pace shape that stranded the closers and handed the Preakness to a tactical type (Napoleon Solo from off a soft :46.66 half). Expect a slow, tactical race won from forward/mid-pack — deep closers are at structural risk.

**Model vs. market:**
- **Golden Tempo (9-2, model #1, 8.17)** — Derby winner, Curlin, field-best 106 Equibase. Market has him only 4th choice because he's a deep closer; model still tops him on class, **but the slow-pace projection is a live trap** — the exact Talkin spot from the Preakness. Value on the board, trip risk in the run.
- **Chief Wallabee (3-1, model #2, 7.70)** — the pace-fit play: tactical presser, cleanest bounce (easy Derby 4th), Constitution/Medaglia d'Oro stamina, Mott/Alvarado at the Spa. The horse the framework's own Preakness post-mortem says to back in this shape.
- **Renegade (2-1 fav, model #3, 7.52)** — elite connections and figures, but a closer bet to the shortest price. **Model makes him an underlay** — fair horse, no value.
- **Emerging Market (6-1, Prat's pick, model #7, 6.98)** — model is skeptical: another Brown closer into a slow pace. Likely overbet off the Prat headline.
- **Ottinho (20-1, model #6, 7.10)** — Tier-B profile at a Tier-C price; stalker pace-fit + skip-Derby freshness.

**Formal Prediction (LOCKED T-1 · 06-05-2026):**
- **Win:** **Chief Wallabee** (7.70, 3-1) — pace-fit override. In a no-early-speed field the tactical presser is the play; the framework learned this two weeks ago.
- **Top danger / co-key:** Golden Tempo (8.17, 9-2) — highest composite; wins if class trumps trip.
- **Place:** Golden Tempo. **Show:** Renegade.
- **Exacta key:** Chief Wallabee / Golden Tempo box, over Renegade + Commandment.
- **Trifecta key:** (Chief Wallabee, Golden Tempo) / (Renegade, Commandment, Growth Equity) / (Renegade, Commandment, Growth Equity, Ottinho).
- **Longshot value:** Ottinho (20-1, 7.10).
- **Confidence:** medium.
- **Rationale tags:** `pace-fit-tactical`, `slow-pace-closer-fade`, `stamina-pedigree`, `derby-form`, `fresh-skip-layoff`, `market-underlay-fav`.
- **Predicted winning Beyer:** 98-103 (10F, classy field; v2.1 slow-pace modulator caps the top end).

**Suggested allocation (3.0u):**
- 1u Chief Wallabee to win
- 0.5u Golden Tempo to win
- 1u $1 exacta box: Chief Wallabee / Golden Tempo
- 0.5u $1 trifecta key: (Chief Wallabee, Golden Tempo) / (Renegade, Commandment, Growth Equity) / (Renegade, Commandment, Growth Equity, Ottinho)
- 0.25u flier: Ottinho to win at 20-1

**Sources (T-1 scrape, 06-05-2026):**
- [VSiN — 2026 Belmont post draw & opening odds](https://vsin.com/horse-racing/2026-belmont-stakes-post-draw-and-opening-odds/)
- [NYRA — Belmont Stakes contenders](https://www.nyra.com/belmont-stakes/racing/belmont-stakes-contenders/)
- [Horse Racing Nation — post draw & morning-line odds](https://www.horseracingnation.com/news/Belmont_Stakes_2026_Post_position_draw_and_morning_line_odds_123)
- [Covers — 2026 Belmont field profiles](https://www.covers.com/horse-racing/belmont-stakes/horses-2026)

#### T+1 Post-Race Recap (06-07-2026) — final

**Result — 158th Belmont Stakes, Saratoga, 1¼ mi, 06-06-2026:** **Golden Tempo** (PP 9, 6-1) wins by 1¼ lengths in 2:03.49. Jose Ortiz up; Cherie DeVaux becomes the first woman to win both the Derby and the Belmont (second woman to win a Belmont, after Antonucci '23). Half in :48.29, six furlongs in 1:12.38 — modest fractions, as projected; opening quarter not yet published (chart unscraped at T+1). **Beyer 98 (DRF)** — predicted 98-103 → ✅ TIGHT, bottom of range. Winner's Derby Beyer was 95 → forward move of 3.

**Order of finish vs model:**

| Fin | Horse | Comp (rank) | ML → Final | Note |
|---:|---|---|---|---|
| 1 | **Golden Tempo** | 8.17 (#1) | 9-2 → 6-1 | Last of 9 early but in contact (~7L per HRN), two-path, edged clear final 50 yds |
| 2 | Commandment | 7.37 (#4) | 6-1 → 6-1 (al.com, single source) | Second-best late move; Derby 7th |
| 3 | Renegade | 7.52 (#3) | 2-1 → 8-5 fav | Bet down to favoritism, flattened late — underlay call ✅ |
| 4 | Chief Wallabee | 7.70 (#2) | 3-1 → 5-1 | **Led at the 8th pole**, outkicked — 4th, same as Derby |
| 5 | Emerging Market | 6.98 (#7) | 6-1 → unknown | Prat's pick beaten; Derby alumni swept top 5 |
| 6 | Growth Equity | 7.34 (#5) | 12-1 → unknown | Pressed the pace, faded |
| 7 | Vitruvian Man | 5.97 (#9) | 30-1 → unknown | |
| 8 | Ottinho | 7.10 (#6) | 20-1 → unknown | Longshot flier never fired |
| 9 | Powershift | 6.32 (#8) | 12-1 → unknown | Made the lead under Saez — the T-7 "Pletcher rabbit" scenario — faded to last |

`unknown` = final tote for non-board finishers not in T+1 sources; refine if Equibase chart is scraped later.

**Payouts:** $14.00 / $7.32 / $3.88 · $1 exacta (9-7) $55.67 ($2: $111.34) · $2 trifecta (9-7-4) $205.28 ($1: $102.64) · $1 superfecta (9-7-4-3) $237.98.

**Structural headline: the model's top four composites filled the top four finish positions** (comp #1→1st, #2→4th, #3→3rd, #4→2nd). A $1 superfecta box of the model's top four (24 combos, $24) returned $237.98. The composite engine is doing its job as a class filter — it was the win-pick layer on top that failed.

**Prediction scoring (vs LOCKED T-1):**
- **Win-hit:** ❌ MISS — Chief Wallabee 4th.
- **Place-hit:** ✅ HIT — Golden Tempo won; place wager cashes ($7.32). (Exact-slot miss: predicted 2nd, ran 1st.)
- **Show-hit:** ✅ HIT — Renegade 3rd exactly.
- **Exacta-hit:** ❌ MISS — CW/GT box dead with CW 4th.
- **Trifecta-hit:** ✅ **HIT** — key (CW, GT) / (Ren, Com, GE) / (Ren, Com, GE, Ott) covered the 9-7-4 result: GT first slot, Commandment second group, Renegade third group.
- **Longshot-hit:** ❌ MISS — Ottinho 8th.
- **Beyer delta:** ✅ TIGHT — predicted 98-103, actual 98.

**P/L on suggested allocation (3.25u staked):** 1u CW win -1.0u · 0.5u GT win @ $14.00 = +3.0u net · 1u $1 exacta box -1.0u · 0.5u tri key (18 combos) returns 102.64 × (0.5/18) = 2.85u → +2.35u net · 0.25u Ottinho flier -0.25u. **Net +3.10u (ROI +95%).** Season: Preakness -3.25u + Belmont +3.10u = **-0.15u** — rescued by the trifecta architecture and the Golden Tempo hedge win bet.

**Drift (scored at the wire):** the tote faded the winner (GT 9-2 → 6-1) and hammered the wrong horse (Renegade 2-1 → 8-5, ran 3rd). CW 3-1 → 5-1 (drift correct there — ran 4th). Second straight leg won by a horse the tote was drifting or ignoring (Napoleon Solo 8-1, Golden Tempo 6-1). **Drift-as-confidence is 0-for-2 this season** — flagged in calibration.

**Rationale-tag verdicts:**
- `pace-fit-tactical` → ❌ Invalidated. The tactical presser got the perfect trip — led at the 8th pole — and lacked the finishing kick. Pace logic delivered position, not the win.
- `slow-pace-closer-fade` → ❌ Invalidated. The pace WAS modest (:48.29 half) and the deep closer won anyway. Class trumped shape; mitigating note — GT broke well and stayed in contact (Ortiz: "the break helped him a lot"), which moderated the closer risk the tag was built on.
- `stamina-pedigree` → ✅ Validated. Curlin colt (SSI 10 / Distance 10) won at 10F; the speed-leaning Into Mischief favorite flattened to 3rd.
- `derby-form` → ✅ Validated emphatically — Derby runners swept the top five.
- `fresh-skip-layoff` → ✅ Validated. Five weeks rest, skipped the Preakness — second consecutive year the Derby winner skipped Pimlico and won the Belmont (Sovereignty '25, Golden Tempo '26).
- `market-underlay-fav` → ✅ Validated. 8-5 Renegade ran third — fair horse, no value, exactly as priced by the model.

**The big lesson (carried into calibration):** at the Preakness the model trusted a pace projection and got burned; at the Belmont it over-corrected — demoting its own composite #1 on pace grounds — and got burned the other way. Both pace SHAPES were projected correctly; both pace-driven PICK ADJUSTMENTS were wrong. The composite earned the right to pick the winner; the override layer didn't. v3 recommendation: pace overrides barred unless composite gap ≤ 0.25 (Belmont gap was 0.47).

**Data QA flag:** the T-1 field table listed Emerging Market as Derby DNR; he ran 10th in the Derby (HRN). Single-source field builds need a second-source cross-check at T-1 — logged for calibration.

**Sources (T+1 scrape, 06-07-2026):**
- [Horse Racing Nation — Golden Tempo wins with last-to-first rally (Shifman, 06-06-2026)](https://www.horseracingnation.com/news/Belmont_Stakes_2026_Golden_Tempo_wins_with_last_to_first_rally_123)
- [DRF — Golden Tempo goes from Kentucky Derby winner to Belmont Stakes victor (Beyer 98, fractions, trip)](https://live.drf.com/news/golden-tempo-goes-last-belmont-stakes-victory-trainer-cherie-devaux)
- [al.com — 2026 Belmont Stakes: results, payouts, order of finish](https://www.al.com/sports/2026/06/2026-belmont-stakes-results-payouts-order-of-finish-for-golden-tempos-victory.html)
- [ESPN — Kentucky Derby winner Golden Tempo wins Belmont Stakes](https://www.espn.com/horse-racing/story/_/id/48987082/kentucky-derby-winner-golden-tempo-wins-belmont-stakes)
- [AOL/Fox — Golden Tempo takes home 158th Belmont Stakes (Chief Wallabee final odds)](https://www.aol.com/articles/golden-tempo-2026-kentucky-derby-230915763.html)

**Season status:** Triple Crown 2026 closed. Calibration pass fired → `projects/triple-crown/calibration-2026.md`. Next up: the 2027 Derby trail (Iroquois, BC Juvenile) via `derby-prep-race-brief` starting September.

---

## Annual Operating Cadence (post-Derby through Belmont)

| Date | Task | Output |
|------|------|--------|
| 05-02-2026 | Derby post-mortem | Update v1 model gaps, identify bounce risks |
| 05-04-2026 | Preakness watch list | Note likely entries from Wood/Arkansas Derby |
| 05-13-2026 | Preakness entries open | ✅ Run framework, post composite scores (this update) |
| 05-15-2026 | Preakness T-1 brief | triple-crown-race-brief refresh w/ final odds |
| 05-16-2026 | Preakness race | Lock predictions, run bets |
| 05-17-2026 | Preakness T+1 recap | Score predictions, update framework v2.1 |
| 05-19-2026 | Belmont watch list | Track Peter Pan, note skip-Preakness horses |
| 05-30-2026 | Belmont T-7 brief | triple-crown-race-brief watchlist |
| 06-03-2026 | Belmont entries | Run framework |
| 06-05-2026 | Belmont T-1 brief | triple-crown-race-brief final brief |
| 06-06-2026 | Belmont race | Lock predictions, run bets |
| 06-07-2026 | Belmont T+1 recap | ✅ Scored (+3.10u) · calibration-2026.md written |
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
