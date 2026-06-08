# EP012 — DeFi Stablecoin Yield Strategies

From Deploy or Die Episode 12: "DeFi Yield Without the Casino: Stablecoin Strategies That Actually Work"

## The 3 Protocols

| Protocol | Type | Est. Rate | Link |
|----------|------|-----------|------|
| Aave v3 | Lending | 4–6% USDC | https://app.aave.com |
| Compound | Lending | 3–5% USDC | https://app.compound.finance |
| Curve | Liquidity Pool | 1–4% | https://curve.fi |

## Getting Started
1. Install MetaMask or Rabby wallet
2. Buy USDC on Coinbase or Kraken
3. Use Arbitrum or Base chain (near-zero gas fees)
4. Go to app.aave.com → connect wallet → deposit USDC

## Risk Summary
- **Smart contract risk** — audited, but exploits happen. Don't deposit more than you can afford to lose.
- **Depeg risk** — USDC hit $0.87 during SVB collapse (March 2023). Diversify across stablecoins.
- **Liquidity risk** — Curve pool imbalances can affect exit token. Understand before depositing.

## The Yield Stack
```
Base:    USDC → Aave                    (~4–6%)
Layer 2: aUSDC → Yearn / Beefy          (auto-compounds)
Layer 3: Protocol incentive tokens       (adds yield + token exposure)
```

## Tax Tools
- [Koinly](https://koinly.io) — connects wallets/exchanges, tracks yield as income
- [Cointracker](https://cointracker.io) — alternative

## Portfolio Tracking
- [DeBank](https://debank.com) — best cross-protocol DeFi dashboard

## Links
- Newsletter: https://deployordie.io
