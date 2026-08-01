# EP016 — Robinhood Chain: Engineer's Breakdown

From Deploy or Die Episode 16: "Robinhood Just Built a Blockchain: What Engineers Need to Know"

## TL;DR

| Property | Value |
|----------|-------|
| Type | Ethereum L2 |
| Stack | Arbitrum (EVM-compatible) |
| Launched | July 1, 2026 |
| TVL (3 weeks) | $431M |
| Daily transactions | ~6M |
| Revenue split | 10% to Arbitrum, ~0.6% to Ethereum |

## The Technical Stack

- **L2 type:** Optimistic rollup (Arbitrum stack)
- **EVM compatible:** Yes — existing Solidity contracts deploy without modification
- **Settlement:** Ethereum mainnet
- **Node software:** Open source (Arbitrum's codebase)

## Key Products

### Tokenized Stocks (RWAs)
- Stocks + ETFs as ERC-20 tokens
- Backed 1:1 by real shares at US custodian
- Issued by Robinhood Assets (Jersey) Limited
- Tradeable 24/7 including weekends
- Composable with DeFi protocols

### Robinhood Earn (DeFi Lending)
- Accessible from main Robinhood app
- Deposits: USDG stablecoin
- Powered by: Morpho vaults
- Vault managers: Steakhouse, Ethena, Spark, Maple
- Advertised APY: 7% (subsidized)
- **Insurance: Lloyd's of London** (smart contract exploits + cyber events)

## The Distribution Moat

28 million funded retail customers with:
- KYC already completed
- Fiat on-ramps already connected
- Mobile interface they already trust

No crypto-native chain can replicate this quickly.

## Base or Blast?

| Chain | Launch | Outcome |
|-------|--------|---------|
| Base (2023) | Memecoins + hype → real developer ecosystem | Survived |
| Blast | $2B TVL → $29M after incentives ended | Collapsed |
| Robinhood Chain | ? | TBD — 30 days old |

Staying power depends on tokenized stocks becoming useful as DeFi collateral.

## Resources

- [Robinhood Chain](https://chain.robinhood.com)
- [DefiLlama — live TVL](https://defillama.com/chain/Robinhood)
- [Newsletter: deployordie.io](https://deployordie.io)
- [EP012 — DeFi stablecoin yield](https://github.com/mttaylor/deployordiecontent/tree/main/ep012-defi-stablecoin-yield)
