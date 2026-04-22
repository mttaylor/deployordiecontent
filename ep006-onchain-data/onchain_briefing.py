#!/usr/bin/env python3
"""
Deploy or Die EP006 — Free On-Chain Data Briefing
"What On-Chain Data Actually Tells You"

Fetches exchange flow data and stablecoin supply from free public APIs.
No API key required for basic usage.

Video: https://youtu.be/le1j8NZfC7M
Newsletter: https://deployordie.io
"""

import requests
import json
from datetime import datetime

# ── CryptoCompare (free, no auth needed for basic endpoints) ──────────────────
def get_btc_price():
    r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD")
    return r.json().get("USD", 0)

# ── Glassnode (free tier — limited endpoints, no key needed for some) ──────────
def get_exchange_balance():
    """BTC balance on exchanges — proxy for sell pressure."""
    # Using CryptoQuant public API (no auth for basic data)
    r = requests.get(
        "https://api.cryptoquant.com/v1/btc/exchange-flows/reserve",
        params={"window": "day", "limit": 2},
        timeout=10
    )
    if r.status_code == 200:
        data = r.json().get("data", [])
        if len(data) >= 2:
            change = data[-1]["value"] - data[-2]["value"]
            return {"current": data[-1]["value"], "change_24h": change}
    return None

# ── Stablecoin supply via DeFiLlama (completely free, no auth) ─────────────────
def get_stablecoin_supply():
    r = requests.get("https://stablecoins.llama.fi/stablecoins?includePrices=true", timeout=10)
    if r.status_code != 200:
        return None

    data = r.json().get("peggedAssets", [])
    total = 0
    breakdown = {}
    for asset in data:
        if asset.get("symbol") in ("USDC", "USDT", "DAI", "BUSD"):
            circ = asset.get("circulating", {}).get("peggedUSD", 0)
            breakdown[asset["symbol"]] = circ
            total += circ

    return {"total_usd": total, "breakdown": breakdown}

# ── DEX volume via DeFiLlama ──────────────────────────────────────────────────
def get_dex_volume():
    r = requests.get("https://api.llama.fi/overview/dexs?excludeTotalDataChart=true", timeout=10)
    if r.status_code == 200:
        return r.json().get("totalVolume24h", 0)
    return None

# ── Main briefing ─────────────────────────────────────────────────────────────
def main():
    print(f"\n{'='*50}")
    print(f"  ON-CHAIN BRIEFING — {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"{'='*50}\n")

    btc = get_btc_price()
    print(f"BTC Price:        ${btc:,.0f}")

    stables = get_stablecoin_supply()
    if stables:
        total_b = stables["total_usd"] / 1e9
        print(f"\nStablecoin Supply: ${total_b:.1f}B total")
        for sym, val in stables["breakdown"].items():
            print(f"  {sym}: ${val/1e9:.1f}B")

    dex_vol = get_dex_volume()
    if dex_vol:
        print(f"\nDEX Volume (24h): ${dex_vol/1e9:.2f}B")

    print(f"\n{'='*50}")
    print("  Source: DeFiLlama (free, no auth)")
    print("  Full breakdown: https://deployordie.io")
    print(f"{'='*50}\n")

if __name__ == "__main__":
    main()
