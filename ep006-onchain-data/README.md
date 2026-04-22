# EP006 — Free On-Chain Data Briefing

From Deploy or Die Episode 6: "What On-Chain Data Actually Tells You"

## What this does

Fetches live on-chain signals using free public APIs — no API key, no Bloomberg Terminal needed:

- BTC price (CryptoCompare free tier)
- Stablecoin supply breakdown — USDC, USDT, DAI (DeFiLlama)
- DEX 24h volume (DeFiLlama)

## Usage

```bash
pip install requests
python3 onchain_briefing.py
```

## Free Tool Stack

| Tool | What it covers | Cost |
|------|---------------|------|
| [Glassnode](https://glassnode.com) | Exchange flows, HODL waves | Free (basic) |
| [Nansen](https://nansen.ai) | Whale wallet tracking | Free tier |
| [Dune Analytics](https://dune.com) | SQL queries on-chain | Free |
| [DeFiLlama](https://defillama.com) | TVL, DEX volume | Free |
| [Polymarket](https://polymarket.com) | Regulatory probability | Free |

## Links
- Video: https://youtu.be/le1j8NZfC7M
- Newsletter: https://deployordie.io
