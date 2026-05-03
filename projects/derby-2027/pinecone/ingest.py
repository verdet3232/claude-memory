"""
pinecone-ingest.py
Ingest prep race data into shook-rag/derby-research namespace.

Usage:
    # Ingest a single race's data from JSON
    python pinecone-ingest.py --race-file race-data/risen-star-2027.json

    # Bulk backfill from a directory of race JSONs
    python pinecone-ingest.py --bulk race-data/

    # Ingest a single horse's pedigree note
    python pinecone-ingest.py --pedigree horse-id

Environment:
    OPENAI_API_KEY    OpenAI API key for embeddings
    PINECONE_API_KEY  Pinecone API key
    PINECONE_INDEX    Default: shook-rag
    PINECONE_HOST     Index host URL (from Pinecone console)

Race JSON schema:
    {
        "race_name": "Risen Star Stakes",
        "grade": "G2",
        "race_date": "2027-02-20",
        "track": "Fair Grounds",
        "distance_furlongs": 8.5,
        "surface": "dirt",
        "summary": "Race summary text...",
        "pace_notes": "Fast pace, contested by...",
        "horses": [
            {
                "horse": "Example Colt",
                "horse_id": "example_colt_2024",
                "sire": "Curlin",
                "dam_sire": "Tapit",
                "trainer": "Cherie DeVaux",
                "jockey": "Jose Ortiz",
                "finish_position": 3,
                "speed_fig": 92,
                "running_style": "S",
                "trip_note": "Saved ground, late move, just missed.",
                "framework_composite": 7.2,
                "framework_factors": {"ssi": 10, "pace": 8, ...}
            }, ...
        ],
        "quotes": [
            {
                "speaker": "Cherie DeVaux",
                "role": "trainer",
                "horse": "Example Colt",
                "quote": "He's a runner.",
                "context": "post-race",
                "source": "HRN"
            }, ...
        ]
    }
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

# Lazy imports - only load if actually used
try:
    from openai import OpenAI
except ImportError:
    print("Install: pip install openai>=1.0", file=sys.stderr)
    sys.exit(1)

# ---------- Config ----------
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
PINECONE_INDEX = os.environ.get("PINECONE_INDEX", "shook-rag")
PINECONE_HOST = os.environ["PINECONE_HOST"]  # e.g. https://shook-rag-xxxxx.svc.us-east-1.pinecone.io
NAMESPACE = "derby-research"
EMBED_MODEL = "text-embedding-3-small"

openai_client = OpenAI(api_key=OPENAI_API_KEY)


# ---------- Embedding ----------
def embed(text: str) -> list[float]:
    """Get an embedding vector for `text`."""
    resp = openai_client.embeddings.create(model=EMBED_MODEL, input=text)
    return resp.data[0].embedding


def embed_batch(texts: list[str]) -> list[list[float]]:
    """Batch up to 100 inputs per call (OpenAI limit)."""
    out = []
    for i in range(0, len(texts), 100):
        chunk = texts[i : i + 100]
        resp = openai_client.embeddings.create(model=EMBED_MODEL, input=chunk)
        out.extend([d.embedding for d in resp.data])
    return out


# ---------- Pinecone ----------
def pinecone_upsert(vectors: list[dict[str, Any]]) -> None:
    """Upsert a batch of vectors. Each vector is {id, values, metadata}."""
    url = f"{PINECONE_HOST}/vectors/upsert"
    headers = {"Api-Key": PINECONE_API_KEY, "Content-Type": "application/json"}
    # Pinecone accepts up to 100 vectors per call; chunk if larger
    for i in range(0, len(vectors), 100):
        batch = vectors[i : i + 100]
        payload = {"vectors": batch, "namespace": NAMESPACE}
        r = requests.post(url, headers=headers, json=payload, timeout=30)
        r.raise_for_status()
        print(f"  Upserted batch of {len(batch)}: {r.json().get('upsertedCount', 0)} vectors")


def slugify(s: str) -> str:
    return "".join(c if c.isalnum() else "_" for c in s.lower()).strip("_")


# ---------- Chunk builders ----------
def build_race_summary_chunk(race: dict) -> tuple[str, dict]:
    """Returns (text_to_embed, metadata)."""
    text = (
        f"{race['race_name']} ({race['grade']}). "
        f"{race['track']}, {race['distance_furlongs']}F {race['surface']}. "
        f"{race['race_date']}. "
        f"{race.get('summary', '')} "
        f"Pace: {race.get('pace_notes', 'no notes')}."
    )
    metadata = {
        "type": "race_summary",
        "race_name": race["race_name"],
        "race_date": race["race_date"],
        "track": race["track"],
        "grade": race["grade"],
        "distance_furlongs": float(race["distance_furlongs"]),
        "surface": race["surface"],
        "year": int(race["race_date"][:4]),
        "ingested_at": datetime.now(timezone.utc).isoformat(),
    }
    return text, metadata


def build_horse_race_chunk(race: dict, horse: dict) -> tuple[str, dict]:
    f = horse.get("framework_factors", {})
    text = (
        f"{horse['horse']} · {race['race_name']} · {race['race_date']}. "
        f"Finish: {horse['finish_position']}. "
        f"By {horse['sire']} out of dam by {horse.get('dam_sire', 'unknown')}. "
        f"Trainer: {horse['trainer']}. Jockey: {horse['jockey']}. "
        f"Running style: {horse.get('running_style', 'unknown')}. "
        f"Trip: {horse.get('trip_note', 'no notes')}. "
        f"Speed figure: {horse.get('speed_fig', 'n/a')}. "
        f"Framework composite: {horse.get('framework_composite', 'n/a')}."
    )
    metadata = {
        "type": "horse_race_note",
        "horse": horse["horse"],
        "horse_id": horse.get("horse_id", slugify(horse["horse"])),
        "sire": horse["sire"],
        "dam_sire": horse.get("dam_sire", ""),
        "trainer": horse["trainer"],
        "jockey": horse["jockey"],
        "race_name": race["race_name"],
        "race_date": race["race_date"],
        "track": race["track"],
        "grade": race["grade"],
        "distance_furlongs": float(race["distance_furlongs"]),
        "surface": race["surface"],
        "finish_position": int(horse["finish_position"]),
        "speed_fig": int(horse["speed_fig"]) if horse.get("speed_fig") else 0,
        "running_style": horse.get("running_style", ""),
        "framework_composite": float(horse.get("framework_composite", 0)),
        "year": int(race["race_date"][:4]),
        "ingested_at": datetime.now(timezone.utc).isoformat(),
    }
    return text, metadata


def build_quote_chunk(race: dict, quote: dict) -> tuple[str, dict]:
    text = (
        f"Quote · {quote['speaker']} ({quote['role']}) · {race['race_name']} · {race['race_date']}. "
        f"Re: {quote.get('horse', 'general')}. "
        f"\"{quote['quote']}\". "
        f"Context: {quote.get('context', 'unknown')}. "
        f"Source: {quote.get('source', 'unknown')}."
    )
    metadata = {
        "type": "connection_quote",
        "speaker": quote["speaker"],
        "role": quote["role"],
        "horse": quote.get("horse", ""),
        "race_name": race["race_name"],
        "race_date": race["race_date"],
        "trainer": quote["speaker"] if quote["role"] == "trainer" else "",
        "jockey": quote["speaker"] if quote["role"] == "jockey" else "",
        "year": int(race["race_date"][:4]),
        "source_url": quote.get("source_url", ""),
        "ingested_at": datetime.now(timezone.utc).isoformat(),
    }
    return text, metadata


# ---------- Main ingest flow ----------
def ingest_race(race_data: dict) -> int:
    """Ingest a full race JSON. Returns number of vectors upserted."""
    chunks = []
    chunk_ids = []

    # Race summary
    text, meta = build_race_summary_chunk(race_data)
    chunks.append((text, meta))
    chunk_ids.append(f"race_{slugify(race_data['race_name'])}_{race_data['race_date']}")

    # Horse race notes
    for horse in race_data.get("horses", []):
        text, meta = build_horse_race_chunk(race_data, horse)
        chunks.append((text, meta))
        chunk_ids.append(
            f"horse_{meta['horse_id']}_{slugify(race_data['race_name'])}_{race_data['race_date']}"
        )

    # Quotes
    for i, quote in enumerate(race_data.get("quotes", [])):
        text, meta = build_quote_chunk(race_data, quote)
        chunks.append((text, meta))
        chunk_ids.append(
            f"quote_{slugify(quote['speaker'])}_{slugify(race_data['race_name'])}_{race_data['race_date']}_{i}"
        )

    if not chunks:
        print(f"  ⚠ No chunks built for {race_data['race_name']}")
        return 0

    # Embed all texts in one batch
    print(f"  Embedding {len(chunks)} chunks...")
    texts = [c[0] for c in chunks]
    vectors_raw = embed_batch(texts)

    # Build Pinecone payload
    pc_vectors = [
        {"id": cid, "values": vec, "metadata": meta}
        for cid, vec, (_, meta) in zip(chunk_ids, vectors_raw, chunks)
    ]

    pinecone_upsert(pc_vectors)
    return len(pc_vectors)


def ingest_file(path: Path) -> int:
    print(f"📥 {path.name}")
    with open(path) as f:
        race = json.load(f)
    return ingest_race(race)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--race-file", type=Path, help="Single race JSON file")
    parser.add_argument("--bulk", type=Path, help="Directory of race JSON files")
    parser.add_argument("--pedigree", help="Build pedigree note for a horse_id")
    args = parser.parse_args()

    total = 0
    if args.race_file:
        total = ingest_file(args.race_file)
    elif args.bulk:
        for p in sorted(args.bulk.glob("*.json")):
            total += ingest_file(p)
            time.sleep(0.5)  # gentle rate limiting
    elif args.pedigree:
        print("Pedigree note builder not yet implemented — manual JSON for now.")
        sys.exit(1)
    else:
        parser.print_help()
        sys.exit(1)

    print(f"\n✅ Ingested {total} vectors into {PINECONE_INDEX}/{NAMESPACE}")


if __name__ == "__main__":
    main()
