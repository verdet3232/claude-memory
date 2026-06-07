# 2026 Triple Crown — Season Framework Calibration

*Generated 06-07-2026 by `triple-crown-race-brief` (Belmont T+1 trigger). Evaluates framework v2.1 against the season's two formal predictions and recommends v3 changes. The Derby pre-dates the formal prediction log (v1 era) and is excluded from hit-rate math.*

---

## Season record

| Race | Predicted win | Actual win | Win | Place | Show | Exacta | Trifecta | Beyer | P/L |
|---|---|---|---|---|---|---|---|---|---:|
| Preakness 05-16-2026 | Talkin (comp #1, 7.87, 20-1) | Napoleon Solo (comp 5.95, 8-1) | ❌ | ✅ | ✅ | ❌ | ❌ | TIGHT (96 in 95-98) | -3.25u |
| Belmont 06-06-2026 | Chief Wallabee (comp #2, 7.70, 3-1 — pace override) | Golden Tempo (comp #1, 8.17, 6-1) | ❌ | ✅ | ✅ | ❌ | ✅ | TIGHT (98 in 98-103) | +3.10u |

**Totals:** Win 0/2 · Place 2/2 · Show 2/2 · Exacta 0/2 · Trifecta 1/2 · Longshot 0/2 · Beyer 2/2 TIGHT · **Season P/L -0.15u on 6.5u staked (-2.3% ROI)**

The two win misses have opposite shapes — that's the central calibration finding:
- **Preakness:** trusted a pace projection (closer setup) that was wrong → comp #1 ran 12th, winner was comp ~#9.
- **Belmont:** over-corrected — demoted comp #1 on pace grounds (gap 0.47) → the demoted horse won, the override pick ran 4th.

## Signal hit rates (cumulative)

| Signal / family | Record | Verdict |
|---|---|---|
| Pace family (pace-fit-closer, pace-fit-tactical, slow-pace-closer-fade) | **0/3** | ⚠⚠ Worst signal in the book. Both pace *shapes* were projected correctly; both pick *adjustments* from them were wrong |
| Freshness family (fresh-no-bounce, fresh-skip-layoff) | **2/2** | Both winners were the fresh horse. Strongest signal of the season |
| stamina-pedigree | 1/1 | Curlin won at 10F; speed-sire favorite flattened |
| derby-form | 1/1 | Derby alumni swept Belmont top 5 |
| market-underlay-fav | 1/1 | 8-5 Renegade ran 3rd |
| beaten-fav-G1G3 | 0.5/1 | Application inverted — framework rewards G1 *placings* over G1 *wins*; both season winners were G1 winners |
| rider-upgrade | 0/1 | Insufficient alone |
| distance-neutral | 1/1 (neutral) | No signal |
| ML Drift as confidence | 0/2 on winners | Tote faded both winners (Napoleon Solo 8-1, Golden Tempo 9-2→6-1). Anti-signal as used |
| Beyer range projection (v2.1 slow-pace modulator) | 2/2 TIGHT | Keep unchanged |
| **Composite as class filter** | **Belmont comps #1-4 = finishers 1-4**; Preakness place/show both from comps | Engine validated. The failures live in the override layer, not the composite |

## Factor-level notes

- **SSI:** Belmont ✓ (Curlin 10 → won). Preakness ✗ (Liam's Map scored 5, should be ≥7 — flagged 05-17). **Full SSI table audit due before the first 2027 prep brief.**
- **Layoff:** validated at both legs but only weighted 0.8× at the Preakness, where the fresh horse won — the season's largest single weight miss.
- **Bounce:** over-punitive at 5-week spacing — Golden Tempo carried Bounce 6 ("hard Derby run") and won the Belmont comfortably. Needs a spacing-relief tier.
- **RSI (1.2× Belmont):** ✓ — winner held the field-best figure (106 Equibase / 95 Beyer entering; ran 98).
- **Distance Pedigree at 1.0× for the 10F Belmont:** ✓ — correctly avoided the traditional 2.0× over-weight on a shortened race.
- **PP-Bias (0.3×, neutral-scored):** no signal either way; harmless. Keep optional.

## Recommended v3 changes

### Weights (only where season evidence exists)

| Factor | Current | Recommended | Evidence |
|---|---|---|---|
| Layoff — Preakness | 0.8× | **1.2×** | Fresh horse won both legs; 0.8× was the largest weight miss |
| ML Drift — all legs | 1.0× | **0.5×** | 0-for-2 on winners; tote faded both |
| Bounce — all legs | tiers per v2.1 | **add +2 relief when spacing ≥ 5 weeks** | GT Bounce 6 won easily off 5 weeks |
| **NEW — Class Ceiling (factor 12)** | — | **1.0× all legs** | Both winners were the field's highest class-ceiling horse. Scale: 10 = two-turn G1 win · 8 = one-turn G1 win · 6 = G1 placed · 4 = G2 win · 2 = G3 win. Replaces the inverted G1-placing logic inside Beaten-Favorite (B-Fav reverts to pure beaten-favorite trips) |
| Belmont-10F weight set otherwise | 2026 set | **keep** | Comp ranks 1-4 = finish 1-4 |

### Rules (the real fixes)

1. **No-override rule:** pace projections may swap adjacent composite ranks only when the composite gap ≤ 0.25, and composite #1 may never be demoted below co-key. Applied retroactively: Belmont gap was 0.47 → override barred → model picks Golden Tempo → win bet cashes at 6-1.
2. **Pace shape ≠ pick:** pace reads go into the Pace Fit score *before* the composite is computed — never re-litigated after.
3. **Two-source field verification at T-1.** (Belmont T-1 listed Emerging Market as Derby DNR; he was Derby 10th per HRN.)
4. **Drift-out on a Tier-A horse = value flag, not a fade.** Both 2026 winners were drifting or market-ignored.
5. **Tag hygiene:** merge `fresh-no-bounce` + `fresh-skip-layoff` → `fresh-layoff`. Retire `rider-upgrade` as a standalone tag (fold into Jockey factor).

### Betting structure

The season was rescued by vertical exotics (Belmont $1 tri key 18-combo: +2.35u net; a $24 super box of model top-4 returned $237.98). Until the win engine proves out (0/2), default allocation shifts to:

- 0.5u win — composite #1 only (no override picks)
- 1u $1 exacta box — comps 1-2
- 1u $1 trifecta key — comps 1-2 / comps 1-5 / comps 1-5
- 0.25u $1 superfecta box — comps 1-4 (24 combos)

## 2027 readiness

- `derby-prep-race-brief` (8-factor) resumes with the Iroquois (09-2026) — carry Class Ceiling and the no-override rule into that framework too.
- SSI table audit before the first 2027 prep brief.
- Belmont 2027: confirm venue/distance once NYRA announces (Belmont Park rebuild → possible 12F restoration → revert Distance Pedigree to 2.0× and re-derive the weight column).
- This file is the v2.1 → v3 bridge; apply the accepted changes to `framework.md` §Race-Specific Factor Weights as v3.0 before the first 2027 brief.

---

*Sources: projects/triple-crown/predictions/log.md (both scored entries) · framework.md §Preakness T+1 (05-17-2026) and §Belmont T+1 (06-07-2026) recaps and their cited charts/recaps (Equibase, DRF, HRN, al.com, ESPN, AOL/Fox).*