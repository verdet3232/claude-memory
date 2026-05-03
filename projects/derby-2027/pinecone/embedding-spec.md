# Pinecone Embedding Spec · Derby Research in `shook-rag`

**Owner:** Ryan Shook · **Created:** 05-02-2026
**Index:** `shook-rag` (existing)
**Namespace:** `derby-research` (new — segregates this from your other personal docs)

## Purpose

Index every prep race result, trip note, jockey/trainer quote, and workout observation across the 12-month 2027 Derby trail. Enable semantic queries like "Curlin sons that showed in G2 preps" or "DeVaux post-race quotes about closers" — exactly the analysis pattern that would have surfaced Golden Tempo months in advance.

## Embedding model

**Default: OpenAI `text-embedding-3-small`**
- 1536 dimensions
- $0.02 / 1M tokens
- Fast, cheap, accurate enough for racing notes

**Upgrade path: `text-embedding-3-large`**
- 3072 dimensions
- $0.13 / 1M tokens
- Use only if recall on subtle queries (e.g., "tactical closer with one-turn experience") is poor

Skip Voyage and BGE for now — they're better at certain specialized domains (legal, code) but OpenAI's general-purpose model is best-fit for free-text race notes.

## Index configuration

Already exists as `shook-rag`. Confirm settings:

```
Index name: shook-rag
Dimensions: 1536 (must match text-embedding-3-small)
Metric: cosine
Pod type: serverless (or s1.x1 if dedicated)
Cloud: aws
Region: us-east-1
```

If your existing `shook-rag` is at a different dimension, create a new index `shook-derby-rag` rather than coexisting incompatible vectors.

## Namespace strategy

```
shook-rag/
├── derby-research/      ← THIS spec
├── academica/           ← (existing) work docs
├── personal/            ← (existing) personal docs
└── automations/         ← (existing) automation index
```

Querying `derby-research` namespace alone keeps Derby work isolated and predictable.

## Document types & chunking

Each prep race produces multiple chunks. Don't shove the whole race chart into one vector — embed each semantic unit separately.

### Type 1: `race_summary`
**One chunk per race.** Top-line summary of what happened.

```
Risen Star Stakes (G2). Fair Grounds, 1 1/16 mi dirt. 02-20-2027.
Won by [horse] over [horse2] by [N] lengths in [time]. Fast pace
contested by [E types]. Closing fractions favored [running style].
Track condition: fast.
```

### Type 2: `horse_race_note`
**One chunk per horse per race.** The most important type — feeds 90% of queries.

```
[Horse name] · [Race name] · [Date]
Finish: [position] (beaten [N] lengths) · Speed Fig: [N]
By [sire] out of [dam] (by [BMS])
Trainer: [trainer] · Jockey: [jockey]
Running style this race: [E/EP/P/S/SS]
Trip: [free-text trip note describing position, traffic, energy at wire]
Framework v2 score (running): SSI=[N] Pace=[N] Stbl=[N] Jock=[N] BFav=[N] Drift=[N] · Composite=[N]
```

### Type 3: `connection_quote`
**One chunk per quote.** Trainer/jockey/owner post-race commentary.

```
Quote · [Speaker name] ([role]) · [Race name] · [Date]
Re: [horse name]
"[exact quote]"
Context: [post-race / morning workout / press conference]
Source: [HRN / Equibase / DRF / Twitter handle]
```

### Type 4: `workout_note`
**One chunk per published work.** Morning training observations.

```
Workout · [Horse name] · [Date]
Track: [track] · Surface: [dirt/turf] · Distance: [furlongs]
Time: [time] · Rank: [N of M for the day]
Clocker note: "[free-text observation]"
Trainer comment if available: "[quote]"
```

### Type 5: `pedigree_note`
**One chunk per horse, updated as more is learned.** Distance breeding analysis.

```
Pedigree · [Horse name]
Sire: [sire] (SSI [N], notable progeny: [N], [N])
Dam: [dam], by [BMS]
Female family (tail-female): [tribe number / notable ancestress]
Distance index for 1 1/4 mi: [score 0-10]
Distance index for 1 1/2 mi: [score 0-10]
Notes: [free-text observations on stamina, precocity, surface fit]
```

## Metadata schema

Filterable on every vector. Cast types correctly — Pinecone is strict.

```json
{
  "type": "horse_race_note",                  // race_summary | horse_race_note | connection_quote | workout_note | pedigree_note
  "horse": "Golden Tempo",                    // string, lowercase normalized for matching
  "horse_id": "golden_tempo_2024",            // stable ID even if name changes (e.g., for foreign horses renamed)
  "sire": "Curlin",
  "dam_sire": "Tapit",
  "trainer": "Cherie DeVaux",
  "jockey": "Jose Ortiz",
  "race_name": "Risen Star Stakes",
  "race_date": "2027-02-20",                  // ISO format for range queries
  "track": "Fair Grounds",
  "grade": "G2",
  "distance_furlongs": 8.5,                   // numeric for range queries
  "surface": "dirt",                          // dirt | turf | synthetic
  "finish_position": 3,
  "speed_fig": 92,
  "running_style": "S",                       // E | EP | P | S | SS
  "derby_points_earned": 15,
  "framework_composite": 7.2,                 // numeric, current composite score
  "is_derby_qualifier": true,
  "year": 2027,                               // for partition queries
  "ingested_at": "2027-02-20T22:30:00Z",
  "source_url": "https://www.horseracingnation.com/race/2027_Risen_Star"
}
```

## Query patterns

### Pattern 1 · Find Curlin sons that showed in G2/G3 preps

```python
results = index.query(
  namespace="derby-research",
  vector=embed("Curlin son finishes third strong stretch run dirt prep"),
  top_k=20,
  filter={
    "$and": [
      {"sire": {"$eq": "Curlin"}},
      {"finish_position": {"$lte": 3}},
      {"grade": {"$in": ["G2", "G3"]}},
      {"surface": {"$eq": "dirt"}},
      {"year": {"$eq": 2027}}
    ]
  }
)
```

### Pattern 2 · DeVaux barn post-race signal

```python
results = index.query(
  namespace="derby-research",
  vector=embed("trainer optimistic about distance two-turn classic horse"),
  top_k=15,
  filter={
    "$and": [
      {"trainer": {"$eq": "Cherie DeVaux"}},
      {"type": {"$eq": "connection_quote"}}
    ]
  }
)
```

### Pattern 3 · Find the 2027 "Golden Tempo profile"

```python
# Multi-stage query: find horses with show-finish patterns in G2/G3 preps
# AND classic-distance pedigree
# AND deep-closer running style

results = index.query(
  namespace="derby-research",
  vector=embed("deep closer rallied from far back wide trip stamina pedigree"),
  top_k=30,
  filter={
    "$and": [
      {"finish_position": {"$lte": 3}},
      {"grade": {"$in": ["G1", "G2"]}},
      {"running_style": {"$in": ["S", "SS"]}},
      {"year": {"$eq": 2027}},
      {"framework_composite": {"$gte": 6.0}}
    ]
  }
)

# Group results by horse_id, count distinct races each appears in
# Horses appearing 2+ times = Golden Tempo profile
```

### Pattern 4 · Pace projection for upcoming race

```python
# Get every horse's running style from their last 3 races
results = index.query(
  namespace="derby-research",
  vector=embed("running style early speed pace setter front-runner"),
  top_k=60,
  filter={
    "$and": [
      {"horse": {"$in": derby_field_horses}},  # array of names
      {"type": {"$eq": "horse_race_note"}}
    ]
  }
)
# Aggregate to determine how many E/EP types are in the field → pace projection
```

## Ingestion pipeline

Three triggers populate the index:

### Trigger A · Make.com scenario (auto)

Extends the existing `derby-2027-trail-tracker` scenario. After step 7 (Claude updates markdown), add a parallel branch:

```
7 → fork
├── existing path: commit markdown, regen HTML, email
└── new path: chunk race data, embed each chunk, upsert to Pinecone
```

Modules:
- `Iterator` over `top5` array → produces 5 horse_race_note chunks
- `Iterator` over connection_quotes → produces N quote chunks
- `OpenAI embeddings` for each chunk
- `HTTP POST` to Pinecone `/vectors/upsert` endpoint with the embedding + metadata

### Trigger B · Manual ingest (Python script)

For backfilling historical races or adding pedigree notes. See `pinecone-ingest.py`.

### Trigger C · Quote scraping (separate Make scenario)

Daily scenario that scrapes Twitter/X for trainer-jockey-owner quotes about Derby horses, embeds, upserts. Runs at 9 PM ET to catch evening interview cycles.

## Maintenance

### Weekly (during prep season)

- Saturday post-race: confirm new vectors landed (check namespace count grew by ~5-15)
- Sunday review: query top-10 composite scores to verify watch list correctness

### Monthly

- Spot-check: pull 20 random vectors, verify metadata is complete and valid
- Cost check: monitor token spend in OpenAI dashboard

### Annually (post-Derby)

- Snapshot the namespace: export all vectors + metadata to JSON for archive
- Rebuild composite scores against finalized framework version (post-mortem might bump weights)
- Reset namespace for following year? Or keep multi-year? Recommend: keep multi-year, add `year` filter to all queries.

## Estimated index size

Per prep race:
- 1 race_summary chunk
- 5-12 horse_race_note chunks
- 0-5 quote chunks
- 5-15 workout_note chunks (across the days leading up)
- 0-10 pedigree_note chunks (initial + updates)

= ~20-50 vectors per race

For 35 prep races + Derby + watch list maintenance:
**~1,500-2,500 vectors total in `derby-research` namespace.**

At 1536-dim float32, that's ~9-15 MB. Trivial size.

## Cost estimate (annual)

| Service | Usage | Cost |
|---------|-------|------|
| OpenAI embeddings | ~2,500 chunks × ~150 tokens avg = 375K tokens | <$0.01 |
| Pinecone serverless | <100K read units, <100K write units | ~$0-2 (within free tier likely) |
| **Total** | | **<$5/yr** |

## Code

See companion files:
- `pinecone-ingest.py` — manual + bulk ingestion
- `pinecone-query.py` — query patterns and watch-list builder

## Integration with framework v2

The `framework_composite` metadata field is the bridge between the markdown framework and semantic search. Every horse_race_note carries the composite at the time of that race. Time-series queries surface horses whose composite is climbing — the leading indicator we want.

## Reference: Pinecone REST endpoints

```
Upsert:    POST https://{INDEX}-{PROJECT}.svc.{REGION}.pinecone.io/vectors/upsert
Query:     POST https://{INDEX}-{PROJECT}.svc.{REGION}.pinecone.io/query
Delete:    POST https://{INDEX}-{PROJECT}.svc.{REGION}.pinecone.io/vectors/delete
Describe:  GET  https://{INDEX}-{PROJECT}.svc.{REGION}.pinecone.io/describe_index_stats

Auth header: Api-Key: {PINECONE_API_KEY}
```
