# Marketcoin: A Peer-to-Peer Exchange System for Bitcoin-like Currencies

Draft for public comment and contribution.

If you have any query or contribution in regards to this paper, please raise an issue. This includes but is not limited to: if something is not clear enough, or you think you've spotted something that needs to be considered.

**Max would like this to be as open and free as possible**, this includes writing the Whitepaper, RFC, ANN, Press info, *and* development.

## Abstract

A peer-to-peer decentralised exchange system would allow the users of a currency market to also be the governing body. Removed from the burden of an external regulatory body would allow such markets to become truly free. Furthermore, facilitating relationships between crypto-currencies enables greater monetary diversity, something that is required if economies are to become resilient to negative effects of their chosen monetary systems. We propose a system that expands upon Bitcoin to enable trustless, peer to peer exchange of Bitcoin-like currencies. By allowing the proof of work chain to be a culmination of several smaller chains representing each currency pair, markets can remain resilient from the impacts of one another, while still conserving the cryptographic advantages bestowed by the virtue of being a crypto-currency. In addition, our system is largely incompatible with modern high performance computing algorithms; instead of instantaneous trade, orders are culminated into a block, and then algorithmically matched. This prevents most HPC exchange strategies and eliminates the spread. 

## Introduction

Marketcoin intro and context

Everything -> Marketcoin and Marketcoin -> Everything (but not Everything -> Everything)

Marketcoin provides a better solution to the double coincidence of wants by allowing users to quickly and trustlessly exchange value between monetary systems. This allows the solutions to the double coincidence (monetary systems) to become separate and insulated in ideas and values, while being technologically connected at the same time. Thus both parties can deal predominantly in their currency of choice without any significant barriers to exchange goods and services for money.

## Orders, Transactions and Exchanges

Transactions, or exchanges, in Marketcoin are comprised of three elements. Two orders (one to buy MKC and one to sell) and a finalisation. The transaction is not completed until the finalisation has been included in the blockchain.

### Orders

Orders are for the buying and selling of Marketcoin for some supported cryptocurrency.
In order for a buy order at price m to be matched with a sell order at price n it is required that n <= m. Once matched in a block, these orders are combined to form the beginning of a transaction, and are recorded simultaneously in the blockchain. 

Once this has occurred control of the MKC being sold is relinquished by the seller.

The exchange algorithm is such that any two nodes will always produce the same matching orders from the same input (the block). Both orders include the public key of each party member. At this stage, the transaction is not yet finalised. For finalisation to occur the buyer of Marketcoin must provide a signed transaction for the agreed upon amount on the altcoin network, to the seller's specified public key. This alone does not provide proof of payment, so in addition a reference to the block the transaction was published in is also required. 

Once the finalisation has been published the control of MKC bought falls to the buyer.

To combat users reneging on trades and locking up others' money indefinitely, two tactics are employed. Firstly, a timeout is placed on every transaction; if it is not finalised within a certain length of time (or number of blocks, to be decided), the transaction is disregarded and control of the disbursement of funds is returned to the seller. In addition, the buyer must pledge some MKC (perhaps 1% of the volume of MKC being bought) which is returned to her only upon successful finalisation of the transaction; if the transaction times out that MKC is absorbed by the network - either given to the person who was inconvenienced or to miners as a fee.

Once orders are matched in a block all onus to complete the transaction falls to the buyer of MKC. Because of this, they are the only party required to pledge funds they may lose if they renege.

At the matching stage of the buyer only a little information is known:

* Pubkey of Seller
* Pubkey of Buyer
* Amount each way

There are several steps that must be required for finalisation to be accepted by the Marketcoin network:

1. Transaction for specified amount made on Altcoin network to the pubkey provided by the seller. (TX1)
2. TX1 is included in an Altcoin block.
3. TX1 is broadcast to Marketcoin with details of which block it was included in, merkle tree position, etc.
4. If it is within 24hrs or so Marketcoin will be checking cached altchain blocks to verify a transaction was included in the block and not just the txid in the merkle tree. This is to guard against miners on the altchain forging proof of payment. If the finalisation occurred more than 24hrs ago it is assumed the tx was included.
5. Once Marketcoin knows about the proof of payment disbursement rights to the original MKC to be bought are given to the buyer.

### Mitigating spam

Marketcoin involves a 'pledge' on both sides of the trade, indicating the intention to fulfil that trade.

The seller of MKC pledges the maximum amount she is willing to spend. Once the order is included a block the funds are made unavailable and will remain so unless the trade fails, in which case all of the pledge is returned.

The buyer of MKC pledges an amount proportional to her order. Unlike the seller of MKC these coins will only be returned if the trade is successful. If the buyer fails in her obligations she sacrifices her pledge to the network (collected as a miner's fee).

As users lose control of disbursement of some MKC when making a trade they diminish their own ability to manipulate the exchange (every trade is a manipulation, after all). This means that spammers will rapidly diminish their coffers if they attempt to spam or flood the network.

### Cancelling orders

An feature of any exchange is the ability to cancel orders. Marketcoin deals with this in two ways:

* Firstly, a timeout: All orders broadcast to the Marketcoin network include the height of the last block they may be included in. That is to say you can provide a timeout for the order if it remains unfilled.
* Secondly, as Marketcoin doesn't need to deal with zero-confirmation payments, the behaviour for dealing with broadcast orders/transactions will be different to that of Bitcoin. By allowing orders with a higher fee to replace those with a lower fee, orders can be updated or used in a transaction.

The latter is not as easy to apply to Altcoin orders on the Marketcoin network, and will need more thought.

### notes

* requirement to add tx and location in altcoin blockchain is sufficient since the PoW was done (altcoin block has hash <= diff); does it allow miners to manipulate market since altcoin block will probably produce marketcoin block too? marketcoin reference to current block *cannot* be a block it was simultaneously generated with? (Edit: not sure exactly why I thought this was an issue; not positive it is).

#### Mining attack and mitigation

Not sure what I was thinking when writing this. Merkle tree generation is deterministic in Bitcoin and does not allow arbitrary data. Only place for arbitrary data is the coinbase tx.

**Probably silly and irrelevant now**

* Include hash of tx in Altcoin merkle root; but not in the block. In the block is a conflicting tx that spends the output, also in merkle root. By including conflicting tx there is a doublespend and those coins cannot be redeemed.
* Trade Matched; Miner waits to include block with conflicting tx and hash of the finalisation tx in merkle tree; Broadcasts broken solution to marketcoin network; confirming the transaction.
* Perhaps miners are asked to validate all trades on altcoin network; not just in merkle tree but also in block. Connect to altcoind armory style?
* So BTC/MKC miners check bitcoin blocks for tx finalisations to ensure they really are there. Do not accept block as valid if inconsistencies detected?
* Blocks from all altcoins kept for 24 hours? 288 blocks: the cutoff?. *MIGHT JUST WORK*

#### Altchain forks

How then to deal with Altcoin chainforks? and if bitcoin block in marketcoin is detected as invalid miners of OTHER currencies will still build on the block. Although BTC/MKC miners could detect the invalidity, LTC/MKC miners would not, and will build on the invalid block. *Validation rules included for every merged currency* - lots of hardforks maybe?

How much trash can someone put in the merkle tree? How likely is it for an random hash to be in the merkle tree? [probably not a worry, see solns above]

Dynamic block requests? Can you request LTC block through MKC network? Need to be able to in order to validate tx's from all networks

## Proof-of-Work Chain (blockchain)

* Marketcoin has an odd blockchain; it is comprised of blocks produced by many different PoW systems; potentially a unique PoW system for every currency pair (it is whatever the Altcoin chooses).

* Each Marketcoin block links to the previous, regardless of the currency pair it was mine on. 

* Each block includes sequential headers of not-yet-included Altcoin blocks, up to some maximum.

* Each block MUST be merged mined with the Altcoin blockchain. Marketcoin has no native PoW system.

* Is a buffer needed? Should be enforced by default but is policy not protocol.

* More discussion is needed to figure out exactly what will happen with reorgs and possible attacks on this untested blockchain architecture.

## Block Validation

* Verify all finalisations of transactions have txid in merkle tree
* Verify PoW is valid (using altchain PoW alg with altchain block header)
* Verify MKC hash is in altcoin block header's merkle tree
* Verify MKC transactions and merkle tree
* Verify block hash of Altcoin has not been used in previous blocks

## Block reward algorithm

**Rewrite this**

* Let all currency pairs be denoted by set C = { C1, C2, C3, …., Cn }
* The block rewards all draw from a central pool of size P, the exhaustion of this source triggers the next retarget.
* At the beginning of each retarget period, the volume of Marketcoin transacted (Sk) for each currency pair Ck, is summed to total S.
* Each currency pair has their block reward set to Sk/S*P for the remainder of the retarget period.
* Each currency pair starts with difficulty=1 and block reward=0. This is to facilitate a quick catchup period before the market 'opens' - or becomes stable. Though trading will still be possible. (Technically)
* Once the market opens the reward is calculated as part of set C. Difficulty is calculated based on the time taken to solve X diff=1 blocks
* If there is not enough left in the central pool a miner shall take the remainder and this will trigger the next retarget period.
* Each retarget period is treated to a small decrease in pool reward size, a continuous function as opposed to Satoshi's step function. 
* This means there is still a provably limited supply; in addition, periods of growth will be treated to faster increases in supply, providing not only economic benefit, but also reducing the maturation period of Marketcoin.

## Reward degradation

* Current plan for block reward degradation
* Each block reward pool is 0.9976 of the previous retarget size.
* IE: -0.24% every retarget period.
* MAX COINS: 21,000,000 exactly
* Half coins in existence: 288 weeks ish = ~5.5 years (also when block reward is half of orig)

## Issues

Some sort-of-counter-party risk-stuff is assumed by seller of Marketcoin - lose access to coins for up to 24 hrs (the escrow period). None for buyer unless prevented sending tx on altcoin network (51% attack), or including soln in marketcoin block.
    Altcoin reorg should not effect marketcoin. Users are left to accept transactions whenever they choose.

Timeouts might conflict if altcoin takes too long to produce blocks. Support must be general. Perhaps doing a difficulty style adjustment based on number of blocks over last retarget period (measured in time). Will be weird if a block is produced in more time than the retarget takes (misses a retarget period). Probably not worth considering yet.
    Might not be an issue; who's creating blocks > 2 weeks between them anyway?
    Not even sure this is an issue.

Blockchain reorganisation on altcoin; if combined blockchain then it might invalidate later trades; perhaps lag time is placed on accepted block headers of altcoin in marketcoin blocks; like cannot be one of the most recent 6 blocks. How is that verified? Perhaps the limit is on how late after you can include the finalisation.

OR

Merged mining means a hash of the bitcoin block is in the marketcoin block header; the blocks are not invalid, just later become superfluous. When they are abandoned, the headers of the new section of the bitcoin blockchain is inserted in bulk into the marketcoin blockchain. marketcoin finalisations may become invalid on the bitcoin network, but will remain in play on the marketcoin network; they should be accepted as valid. **This is an incentive for the buyer to send altcoin quickly, but wait to redeem the marketcoin for an hour or so to ensure there won't be a reorg on the altcoin blockchain.** They can, however, choose to submit the finalisation when they choose. The client will warn of the risk of zero-conf finalisation.

* New currency pairs,
* minimum difficulty? 1% of network? how to measure?
* Trail period for volume?
* But blockchain spam from weird new currencies.
* Maybe whitelist of magicbits hardcoded? (bad soln, though leaning towards this atm)
* Adding new currency would require a hardfork
* Perhaps the number of markets available increases every year or so?
* Allows a period for new cryptocurrencies to compete for spots - requirements on market volume by the end of a trial period?
* Not sure if it can be done in a distributed fashion yet.

Perhaps there can be an automatic voting system; blocks produced all contain a vote on currencies to include or exclude; when enough support is gained (probably needs to be 50%+ to align with other behaviours of the network; actually, strike that, not sure it matters as long as there is concensus on what the % should be) blocks containing the new magicbits can be mined.

The above is feasible, I think. **RFC: Above paragraph; on new altcoin<->marktcoin currency paris**.

* not sure **integration with PoS** is possible currently; merged-mining not compatible as far as I can tell. Difficult to validate PoS without entire blockchain (need to get txouts and coinage).

### signed tx valid on two networks?

I suspect signed transactions are valid on similar cryptocoins; at least when pubkeys are used (addresses might break this, thankfully). Coins would require identical inputs, which is difficult, granted (maybe only coinbase transactions?). *RFC*

## Random Notes and Glossary

* Market volume provides rough scaling between PoW systems on a network wide level.

## References

Satoshi - Bitcoin Whitepaper, 2008

## Authors:

* XertroV (Max Kaye)
