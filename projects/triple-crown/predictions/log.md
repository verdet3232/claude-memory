# 2026 Triple Crown Predictions Log

Running ledger of every triple-crown-race-brief prediction with rationale tags. Appended on T-1; scored on T+1.

| Race | Date | Predicted Win | Conf | Tags | Result | Win | Place | Show | Exacta | Beyer Δ |
|---|---|---|---|---|---|---|---|---|---|---|
| Preakness Stakes | 05-16-2026 | Talkin (20-1, comp 7.87) | med-low | rider-upgrade, pace-fit-closer, beaten-fav-G1G3, fresh-no-bounce, distance-neutral | Won: Napoleon Solo (8-1, comp 5.95) · Talkin 12th | ❌ | ✅ Iron Honor 2nd | ✅ Chip Honcho 3rd | ❌ | TIGHT (predicted 95-98, actual 96) |

---

## Hit-rate summary (auto-updated on each T+1)

- **Win rate:** 0/1 (0.0%)
- **Place rate:** 1/1 (100.0%)
- **Show rate:** 1/1 (100.0%)
- **Exacta rate:** 0/1 (0.0%)
- **Average Beyer delta:** TIGHT (1 of 1 within predicted range)

## Signal-tag performance

_Populated as predictions accumulate. Tags below 40% validation rate flagged for downweighting in next calibration pass._

| Tag | Times used | Times validated | Validation rate |
|---|---:|---:|---:|
| rider-upgrade | 1 | 0 | 0.0% ⚠ |
| pace-fit-closer | 1 | 0 | 0.0% ⚠ |
| beaten-fav-G1G3 | 1 | 0.5 | 50.0% |
| fresh-no-bounce | 1 | 1 | 100.0% |
| distance-neutral | 1 | 1 (neutral) | 100.0% |

---

*Source: triple-crown-race-brief scheduled task on T-1 (prediction logged) and T+1 (scored). Calibration pass after Belmont T+1 writes calibration-2026.md.*

---

## Detailed T-1 Prediction Entries

### Preakness Stakes · 05-16-2026 (logged T-1 · 05-15-2026)

- **Predicted win:** Talkin (composite 7.87, ML 20-1)
- **Predicted place:** Iron Honor (composite 7.26, ML 9-2)
- **Predicted show:** Chip Honcho (composite 7.24, ML 5-1)
- **Exacta key:** Talkin over Iron Honor / Chip Honcho / Taj Mahal / Bull by the Horns
- **Trifecta key:** Talkin / Iron Honor + Chip Honcho / Taj Mahal + Bull by the Horns + Incredibolt
- **Longshot value:** Bull by the Horns (composite 7.02, ML 30-1)
- **Confidence:** medium-low (model diverges sharply from 9-2 chalk Iron Honor)
- **Rationale tags:** `rider-upgrade`, `pace-fit-closer`, `beaten-fav-G1G3`, `fresh-no-bounce`, `distance-neutral`
- **Predicted winning Beyer:** 95-98
- **T-1 status:** No scratches, track Fast, weather Fair (no rain), live odds match ML 1:1 → Drift neutral, prediction locked unchanged from T-3.

---

## Detailed T+1 Scoring Entries

### Preakness Stakes · 05-16-2026 (scored T+1 · 05-17-2026)

**Actual result:** Napoleon Solo (PP 10, ML 8-1, pre-race composite 5.95) by 1¼ over Iron Honor; Chip Honcho 3rd by 2¾. Final time 1:58.69 (:22.66 · :46.66 · 1:12.08). **Beyer 96.**

**Scoring:**
- **Win-hit:** ❌ MISS — Talkin finished 12th.
- **Place-hit:** ✅ HIT — Iron Honor 2nd.
- **Show-hit:** ✅ HIT — Chip Honcho 3rd.
- **Exacta-hit:** ❌ MISS — Talkin (key over) missed the board entirely.
- **Trifecta-hit:** ❌ MISS — same reason.
- **Longshot-hit:** ❌ MISS — Bull by the Horns 6th.
- **Beyer delta:** ✅ TIGHT — predicted 95-98, actual 96 (Δ = 0 to bottom of range, within range).

**Payoffs missed (suggested 3.25u allocation, all on Talkin-keyed tickets):** **-3.25u P/L**.

**Payoffs available had we keyed Napoleon Solo:** $2 exacta (10-9) $107.20 · trifecta (10-9-6) $1,194.20 · superfecta (10-9-6-2) $4,755.60.

**Rationale-tag verdicts:**
- `rider-upgrade` → ❌ Invalidated. Irad Ortiz on Talkin finished 12th; rider upgrade alone is insufficient.
- `pace-fit-closer` → ❌ Invalidated. Pace projection was the single biggest model miss — only Taj Mahal pressed early; half went in :46.66 (moderate). Closers Ocelli/Incredibolt stranded.
- `beaten-fav-G1G3` → ⚠ Partially invalidated as applied to Talkin (12th); but the *actual* winner Napoleon Solo *was* a G1 winner (Champagne 2025). The framework's tier list inverts the right signal — it rewards G1 *place* finishes more than G1 *wins*. Tag survives, application logic needs revision.
- `fresh-no-bounce` → ✅ Validated. The fresh, skipped-Derby horse (Napoleon Solo) won. Tag is correctly directional; we just under-applied it (or it was indiscriminate when 8 of 14 got the max).
- `distance-neutral` → ⚪ Neutral. 9.5F was no obstacle for the winner. No signal either way.

**Top framework-improvement candidates (carry forward to Belmont T-7 reweighting):**
1. **Pace-fit weight (1.0× at Preakness) was too low** to express a high-confidence pace projection that turned out wrong. Either lift weight to 1.5× *or* lower confidence threshold for projecting contested-pace setups when only 1-2 horses are true wire-to-wire types.
2. **G1 winner premium** — A clear "G1 winner in field" tier-up for Beaten-Favorite (or add a new factor: `Class Ceiling`). Napoleon Solo's Champagne G1 dominance was the largest single under-weighted signal.
3. **Bounce-risk needs finer tiers** — Max-score (10) applied to 8 of 14 horses neutralized the factor. Subdivide: 10 = skipped Derby AND came off a stakes win 3+ wks out; 8 = skipped Derby off an OK race; 6 = ran Derby with easy trip.
4. **Sire Stamina Index** for Liam's Map (proven two-turn, classic-distance G1 producer) — was scored 5; should be 7. Re-audit the SSI table.

**Status:** Logged. Final calibration pass deferred until Belmont T+1 (06-07-2026) per task spec.

## Belmont Stakes · 06-05-2026
Predicted win: Chief Wallabee (composite 7.70, ML 3-1) — pace-fit override over composite #1
Predicted place: Golden Tempo (8.17, 9-2)
Predicted show: Renegade (7.52, 2-1)
Exacta key: Chief Wallabee / Golden Tempo box → Renegade, Commandment
Trifecta key: (Chief Wallabee, Golden Tempo) / (Renegade, Commandment, Growth Equity) / (Renegade, Commandment, Growth Equity, Ottinho)
Longshot value: Ottinho (20-1, 7.10)
Confidence: medium
Rationale tags: pace-fit-tactical, slow-pace-closer-fade, stamina-pedigree, derby-form, fresh-skip-layoff, market-underlay-fav
Predicted winning Beyer: 98-103
Field: 9 (Iron Honor / Napoleon Solo / Ocelli did not enter; Powershift + Vitruvian Man drew in)
Note: scored at T+1 (06-07-2026)
