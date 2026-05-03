"""
pinecone-query.py
Query the shook-rag/derby-research namespace for Derby contender insights.

Usage:
    # Find the "Golden Tempo profile" — show finishers in G2/G3 preps with classic-distance pedigree
    python pinecone-query.py golden-tempo-profile --year 2027

    # Find horses by sire
    python pinecone-query.py by-sire --sire "Curlin" --year 2027

    # Find trainer barn signal
    python pinecone-query.py trainer-signal --trainer "Cherie DeVaux"

    # Custom semantic search with filters
    python pinecone-query.py semantic --query "deep closer late move stamina" --top-k 20

    # Generate the watch list (top composites)
    python pinecone-query.py watch-list --year 2027 --min-composite 6.5

Environment:
    OPENAI_API_KEY    OpenAI API key for embeddings
    PINECONE_API_KEY  Pinecone API key
    PINECONE_INDEX    Default: shook-rag
    PINECONE_HOST     Index host URL
"""
import argparse
import os
import sys
from collections import Counter, defaultdict
from typing import Any

import requests
from openai import OpenAI

# ---------- Config ----------
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
PINECONE_HOST = os.environ["PINECONE_HOST"]
NAMESPACE = "derby-research"
EMBED_MODEL = "text-embedding-3-small"

openai_client = OpenAI(api_key=OPENAI_API_KEY)


def embed(text: str) -> list[float]:
    resp = openai_client.embeddings.create(model=EMBED_MODEL, input=text)
    return resp.data[0].embedding


def pinecone_query(
    vector: list[float],
    filter_dict: dict | None = None,
    top_k: int = 10,
) -> list[dict[str, Any]]:
    url = f"{PINECONE_HOST}/query"
    headers = {"Api-Key": PINECONE_API_KEY, "Content-Type": "application/json"}
    payload: dict[str, Any] = {
        "vector": vector,
        "topK": top_k,
        "namespace": NAMESPACE,
        "includeMetadata": True,
        "includeValues": False,
    }
    if filter_dict:
        payload["filter"] = filter_dict
    r = requests.post(url, headers=headers, json=payload, timeout=30)
    r.raise_for_status()
    return r.json().get("matches", [])


# ---------- Query patterns ----------
def golden_tempo_profile(year: int = 2027, top_k: int = 30) -> None:
    """
    Find horses matching the Golden Tempo profile:
    - Show finish (1-3) in G1/G2 preps
    - Deep closer (S/SS) running style
    - Classic-distance pedigree
    - Composite >= 6.0
    """
    print(f"\n🔍 Golden Tempo Profile · {year}")
    print("=" * 60)

    query_text = (
        "deep closer rallied from far back wide trip late move stamina "
        "Curlin Tapit classic distance G2 prep show finish"
    )
    vec = embed(query_text)

    matches = pinecone_query(
        vec,
        filter_dict={
            "$and": [
                {"type": {"$eq": "horse_race_note"}},
                {"finish_position": {"$lte": 3}},
                {"grade": {"$in": ["G1", "G2"]}},
                {"running_style": {"$in": ["S", "SS"]}},
                {"year": {"$eq": year}},
                {"framework_composite": {"$gte": 6.0}},
            ]
        },
        top_k=top_k,
    )

    # Aggregate by horse — horses appearing 2+ times = high signal
    horse_appearances: dict[str, list] = defaultdict(list)
    for m in matches:
        meta = m["metadata"]
        horse_appearances[meta["horse"]].append(meta)

    # Sort by number of appearances DESC, then by avg composite DESC
    sorted_horses = sorted(
        horse_appearances.items(),
        key=lambda kv: (
            -len(kv[1]),
            -sum(m["framework_composite"] for m in kv[1]) / len(kv[1]),
        ),
    )

    print(f"{'Horse':<25} {'Appearances':<12} {'Avg Composite':<15} {'Sire':<15}")
    print("-" * 75)
    for horse, appearances in sorted_horses[:15]:
        avg_comp = sum(m["framework_composite"] for m in appearances) / len(appearances)
        sire = appearances[0].get("sire", "?")
        print(f"{horse[:24]:<25} {len(appearances):<12} {avg_comp:<15.2f} {sire:<15}")


def by_sire(sire: str, year: int = 2027, top_k: int = 30) -> None:
    print(f"\n🔍 Horses by sire: {sire} · {year}")
    print("=" * 60)
    vec = embed(f"{sire} progeny prep race performance dirt classic distance")
    matches = pinecone_query(
        vec,
        filter_dict={
            "$and": [
                {"sire": {"$eq": sire}},
                {"year": {"$eq": year}},
                {"type": {"$eq": "horse_race_note"}},
            ]
        },
        top_k=top_k,
    )

    by_horse: dict[str, dict] = {}
    for m in matches:
        meta = m["metadata"]
        if meta["horse"] not in by_horse or by_horse[meta["horse"]][
            "framework_composite"
        ] < meta.get("framework_composite", 0):
            by_horse[meta["horse"]] = meta

    print(f"{'Horse':<25} {'Best Finish':<12} {'Best Composite':<16} {'Last Race':<25}")
    print("-" * 80)
    for horse, meta in sorted(
        by_horse.items(), key=lambda kv: -kv[1].get("framework_composite", 0)
    )[:15]:
        print(
            f"{horse[:24]:<25} {meta['finish_position']:<12} "
            f"{meta.get('framework_composite', 0):<16.2f} {meta['race_name'][:24]:<25}"
        )


def trainer_signal(trainer: str, top_k: int = 20) -> None:
    print(f"\n🔍 Trainer signal: {trainer}")
    print("=" * 60)

    # Get all horses + quotes from this trainer
    vec = embed(f"{trainer} barn confidence Derby contender stamina quality")
    matches = pinecone_query(
        vec,
        filter_dict={"trainer": {"$eq": trainer}},
        top_k=top_k,
    )

    horses = Counter()
    quotes = []
    for m in matches:
        meta = m["metadata"]
        if meta.get("type") == "horse_race_note":
            horses[meta["horse"]] += 1
        elif meta.get("type") == "connection_quote":
            quotes.append((meta.get("horse", "?"), meta.get("race_date", "?")))

    print(f"\nHorses ({len(horses)} unique):")
    for horse, count in horses.most_common(10):
        print(f"  · {horse} ({count} race notes)")

    print(f"\nQuotes ({len(quotes)}):")
    for horse, date in quotes[:5]:
        print(f"  · {horse} on {date}")


def semantic(query: str, top_k: int = 20) -> None:
    print(f"\n🔍 Semantic search: '{query}'")
    print("=" * 60)
    vec = embed(query)
    matches = pinecone_query(vec, top_k=top_k)
    for m in matches[:10]:
        meta = m["metadata"]
        score = m["score"]
        if meta.get("type") == "horse_race_note":
            print(
                f"[{score:.3f}] {meta['horse']} · {meta['race_name']} ({meta['race_date']}) · "
                f"finish {meta['finish_position']}"
            )
        elif meta.get("type") == "connection_quote":
            print(f"[{score:.3f}] QUOTE: {meta['speaker']} re: {meta.get('horse', '?')}")
        else:
            print(f"[{score:.3f}] {meta.get('type', '?')} · {meta.get('race_name', '?')}")


def watch_list(year: int = 2027, min_composite: float = 6.5) -> None:
    """Generate the Derby watch list — best composite scores currently in the index."""
    print(f"\n🏆 Derby {year} Watch List · composite >= {min_composite}")
    print("=" * 60)

    vec = embed("Derby contender high composite framework score top 20 points")
    matches = pinecone_query(
        vec,
        filter_dict={
            "$and": [
                {"type": {"$eq": "horse_race_note"}},
                {"year": {"$eq": year}},
                {"framework_composite": {"$gte": min_composite}},
            ]
        },
        top_k=100,
    )

    # Take best-composite race per horse
    best: dict[str, dict] = {}
    for m in matches:
        meta = m["metadata"]
        if (
            meta["horse"] not in best
            or best[meta["horse"]]["framework_composite"] < meta["framework_composite"]
        ):
            best[meta["horse"]] = meta

    sorted_list = sorted(
        best.values(), key=lambda m: -m["framework_composite"]
    )

    print(f"\n{'#':<3} {'Horse':<24} {'Sire':<14} {'Trainer':<22} {'Composite':<10} {'Best Race':<22}")
    print("-" * 100)
    for i, meta in enumerate(sorted_list[:25], 1):
        print(
            f"{i:<3} {meta['horse'][:23]:<24} {meta.get('sire', '?')[:13]:<14} "
            f"{meta['trainer'][:21]:<22} {meta['framework_composite']:<10.2f} "
            f"{meta['race_name'][:21]:<22}"
        )


# ---------- CLI ----------
def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("golden-tempo-profile")
    p1.add_argument("--year", type=int, default=2027)

    p2 = sub.add_parser("by-sire")
    p2.add_argument("--sire", required=True)
    p2.add_argument("--year", type=int, default=2027)

    p3 = sub.add_parser("trainer-signal")
    p3.add_argument("--trainer", required=True)

    p4 = sub.add_parser("semantic")
    p4.add_argument("--query", required=True)
    p4.add_argument("--top-k", type=int, default=20)

    p5 = sub.add_parser("watch-list")
    p5.add_argument("--year", type=int, default=2027)
    p5.add_argument("--min-composite", type=float, default=6.5)

    args = parser.parse_args()

    if args.cmd == "golden-tempo-profile":
        golden_tempo_profile(year=args.year)
    elif args.cmd == "by-sire":
        by_sire(sire=args.sire, year=args.year)
    elif args.cmd == "trainer-signal":
        trainer_signal(trainer=args.trainer)
    elif args.cmd == "semantic":
        semantic(query=args.query, top_k=args.top_k)
    elif args.cmd == "watch-list":
        watch_list(year=args.year, min_composite=args.min_composite)


if __name__ == "__main__":
    main()
