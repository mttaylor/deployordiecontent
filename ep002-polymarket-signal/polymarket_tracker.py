import requests, json, re
from datetime import datetime

# Whole-word keyword matching — no false positives from substrings
# Customize this list to track what matters to you
KEYWORDS = [
    r"\bbitcoin\b", r"\bbtc\b", r"\bethereum\b", r"\beth\b",
    r"\bcrypto\b", r"\bfed\b", r"\binterest rate\b", r"\binflation\b",
    r"\btariff\b", r"\bsec\b", r"\bregulation\b", r"\bnvidia\b",
    r"\bopenai\b", r"\bai\b", r"\bstablecoin\b", r"\betf\b",
]

def get_markets(limit=100):
    url = "https://gamma-api.polymarket.com/markets"
    params = {"limit": limit, "active": "true", "closed": "false"}
    r = requests.get(url, params=params, headers={"User-Agent": "polymarket-tracker/1.0"})
    r.raise_for_status()
    return r.json()

def is_relevant(market):
    q = market["question"].lower()
    return any(re.search(kw, q) for kw in KEYWORDS)

def parse_yes_prob(market):
    try:
        prices = json.loads(market["outcomePrices"])
        return float(prices[0])
    except:
        return None

def check_movers(markets, threshold=0.10):
    """Flag markets where the 24h price move is significant."""
    movers = []
    for m in markets:
        yes = parse_yes_prob(m)
        vol = m.get("volume24hr", 0)
        # Polymarket doesn't expose 24h delta directly — use volume as a proxy
        # High volume relative to total volume = recent activity spike
        total_vol = m.get("volumeNum", 1)
        recency = vol / total_vol if total_vol > 0 else 0
        if recency > threshold:
            movers.append(m)
    return movers

def main():
    print(f"\n{'='*65}")
    print(f"  POLYMARKET SIGNAL — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*65}\n")

    markets = get_markets()
    hits = [m for m in markets if is_relevant(m)]
    hits.sort(key=lambda x: x.get("volume24hr", 0), reverse=True)

    if not hits:
        print("  No relevant markets found. Try expanding KEYWORDS.")
    else:
        for m in hits:
            yes = parse_yes_prob(m)
            vol = m.get("volume24hr", 0)
            print(f"  YES: {yes:.0%}  |  ${vol:>8,.0f}/24h")
            print(f"  {m['question']}")
            print()

    movers = check_movers(hits)
    if movers:
        print(f"  ⚡ {len(movers)} ACTIVE MARKET(S) — high recent volume:\n")
        for m in movers:
            print(f"  >> {m['question']}")
        print()

    print(f"{'='*65}")
    print(f"  {len(hits)} markets matched | Polymarket Gamma API | no key needed")
    print(f"{'='*65}\n")

if __name__ == "__main__":
    main()
