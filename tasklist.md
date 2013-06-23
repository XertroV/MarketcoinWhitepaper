# Tasklist

This is a rough outline of what needs to happen for marketcoin to happen.

Most of this is in reference to modifying Bitcoin-QT / bitcoind. Libbitcoin is an option but I'm less familiar with it. I imagine most of this can be translated into tasks on libbitcoin easily

These aren't in any particular order, except sometimes. They should be obvious when they are.

## Implement new block types

* Create DBlock, with code copy pasted from CBlock* stuff. CBlock will be used to read Bitcoin blocks for payment verification (has to read Bitcoin blocks to 'catch up' with Bitcoin currently)
* Implement the currency pair idea; add/change:
	* prevblock is now a vector
	* parentchain indicates the parent chain via some id, maybe UUID - can't deal with permanent chainforks

## Implement merged mining

*Will* require modified copies of bitcoin to add MM support

* No real plan yet, look into p2pool's merged mining
* Based on Namecoin/p2pool style, hold hashes in merkle trees of parent blockchain

Support for altchains like Namecoin should be added as early as possible because it is almost certain that more Bitcoin+Altcoin situations will arise. Bitcoin+Altcoin+Altcoin2 should also be possible without Altcoin and Altcoin2 knowing about eachother.

Marketcoin must latch on so mining the Bitcoin market, Namecoin market, etc are all possible simultaneously.

### Develop new Merged mining standard to allow this

## Implement merged mining with Bitcoin

## Implement merged mining with Bitcoin + Altcoin (like Namecoin)

## Implement merged mining with Litecoin

### Add script support
### Port bitcoin MM code to litecoin

## Implement multiple chain types (btcmkc, ltcmkc, etc)

### Add in support for multi-merged mining, where each block is merged mined from any possible parent chain

* Blocks should link to highest last known blocks (possibly 1 or more) and link to the last block in the currency pair.

## Implement order transaction types

* Maybe do it like namecoin? something like `OP_TRADE <currpair> <rate>`
* Need a different transaction type for bid/ask
* Maybe:
	* Sell MKC: `OP_ASK <currpair> <min rate>`
	* Buy MKC: `OP_BID <currpair> <rate> <amount>`
* Then, Fulfil trade (only for buyer - fulfils the ask):
	* ScriptSig `<bidId> <txid-payment> <blockhash> <merklepath> OP_REDEEM`
	* `<blockhash>` is the block hash of the block which includes the payment on the alt chain
	* `<bidId>` is needed to relieve ambiguity as to which part of the Ask you're fulfilling (as one ask can fill more than one bid and vice versa)
	* `<merklepath>` is the path needed to verify the txid is in the altchain block

## Implement redemption of orders - claim MKC

## Implement trading algorithm