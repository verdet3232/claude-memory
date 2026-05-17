# Triple Crown Handicapping Framework v2

**Owner:** Ryan Shook · **Created:** 05-02-2026 · **Updated:** 05-17-2026
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
| 05-17-2026 | Preakness T+1 recap | Score predictions, update framework v2.1 |
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
