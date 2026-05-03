# Triple Crown Handicapping Framework v2

**Owner:** Ryan Shook · **Created:** 05-02-2026 · **Updated:** 05-02-2026
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

### Preakness Stakes — Saturday, 05-16-2026

- **Venue:** Laurel Park (Pimlico under construction)
- **Distance:** 1 3/16 mi
- **Post:** 7:01 PM ET, NBC
- **Likely Derby horse running back:** Golden Tempo (TBD — DeVaux non-committal in winner's circle)
- **Watch list (new shooters):** Likely Wood Memorial / Arkansas Derby horses skipping Derby
- **Key handicap:** Field will be small. Bounce factor on Golden Tempo is HIGH (deep closer that ran a hard final furlong).

**Pre-race tracker (update as entries finalize):**
| Horse | Trainer/Jockey | ML | SSI | Pace | Stbl | Jock | B-Fav | Drift | Bounce | Composite |
|-------|----------------|-----|-----|------|------|------|-------|-------|--------|-----------|
| _TBD as entries open ~ 05-13-2026_ | | | | | | | | | | |

### Belmont Stakes — Saturday, 06-06-2026

- **Venue:** Saratoga Race Course (final year before Belmont Park reopens)
- **Distance:** 1 1/4 mi (third year shortened from 1 1/2 mi)
- **Post:** 6:50 PM ET, FOX
- **Key prep:** Peter Pan Stakes (G3), Saratoga, ~05-12-2026
- **Key handicap:** Because it's only 10F at Saratoga, treat closer to Derby framework than traditional Belmont. Don't over-weight distance pedigree.

**Pre-race tracker (update as entries finalize):**
| Horse | Trainer/Jockey | ML | SSI | Pace | Stbl | Jock | B-Fav | Drift | Layoff | Composite |
|-------|----------------|-----|-----|------|------|------|-------|-------|--------|-----------|
| _TBD as entries open ~ 06-03-2026_ | | | | | | | | | | |

---

## Annual Operating Cadence (post-Derby through Belmont)

| Date | Task | Output |
|------|------|--------|
| 05-02-2026 | Derby post-mortem | Update v1 model gaps, identify bounce risks |
| 05-04-2026 | Preakness watch list | Note likely entries from Wood/Arkansas Derby |
| 05-13-2026 | Preakness entries open | Run framework, post composite scores |
| 05-16-2026 | Preakness race | Lock predictions, run bets |
| 05-18-2026 | Preakness post-mortem | What worked, what didn't, update framework v2.1 |
| 05-19-2026 | Belmont watch list | Track Peter Pan, note skip-Preakness horses |
| 06-03-2026 | Belmont entries | Run framework |
| 06-06-2026 | Belmont race | Lock predictions, run bets |
| 06-08-2026 | Triple Crown wrap-up | Full post-mortem, framework v3 update |

---

## Linked: 2027 Derby Trail Tracker

After Belmont 2026, the 2yo races leading to the 2027 Derby kick off in September. See `derby-2027-trail-tracker.md` for full schedule and horse-watch system.

## Cowork Automation Hook

New scheduled task: `triple-crown-tracker` (recommended cadence)

```
Race weeks: Daily 6:30 AM - update entries, scores, news
Off-weeks: Sunday 8:00 PM - prep race results review
Annual: Quarterly memory consolidation includes framework version bump
```

Source: `~/projects/triple-crown/framework.md`
Output: `~/Dropbox/triple-crown-dashboard.html` (regenerated each run)
Notify: Email to rshook74@gmail.com on race weeks
