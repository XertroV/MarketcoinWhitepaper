# Marketcoin: A Peer-to-Peer Exchange System for Bitcoin-like Currencies

Draft for public comment and contribution.

If you have any query or contibution in regards to this paper, please raise an issue. This includes but is not limited to: if something is not clear enough, or you think you've spotted something that needs to be considered.

## Abstract

A peer-to-peer decentralized exchange system would allow the users of a currency market to also be the govening body. Removed from the burdon of an external regulatory body would allow such markets to become truly free. Furthermore, facilitating relationships between crypto-currencies enables greater monetary diversity, something that is required if economies are to become resilient to negative effects of their chosen monetary systems. We propose a system that expands upon Bitcoin to enable trustless, peer to peer exchange of Bitcoin-like currencies. By allowing the proof of work chain to be a culmination of several smaller chains representing each currency pair, markets can remain resilient from the impacts of one another, while still conserving the cryptographic advantages bestowed by the virtue of being a crypto-currency. In addition, our system is largely incompatible with modern high performance computing algorithms; instead of instantaneous trade, orders are culminated into a block, and then algorithmically matched. This prevents most HPC exchange strategies and eliminates the spread. 

## Introduction

Marketcoin intro and context

Everything -> Marketcoin and Marketcoin -> Everything (but not Everything -> Everything)

Marketcoin provides a better solution to the double coincidence of wants by allowing users to quickly and trustlessly exchange value between monetary systems. This allows the solutions to the double coincidence (monetary systems) to become separate and insulated, while being trivially connected at the same time. This means that both parties can deal in their currency of choice without any significant barriers to exchange goods and services for money.

## Orders and Transactions

Transactions in Marketcoin differ from those of Bitcoin-like systems. A transaction is broken down into three parts, and is not finalised until all of those parts are present in the blockchain. The first two are matching orders; that being an order to buy Altcoin for the maximum price of m, and an order to sell Altcoin at the minimum price of n, with n <= m. These are combined to form the beginning of a transaction, and are recorded simultaneously in the blockchain. The exchange algorithm is such that any two nodes will always produce the same matching orders from the same input (the block). Both orders include the public key of each party member. At this stage, the transaction is not yet finalised. For finalisation to occur the buyer of Marketcoin must provide a signed transaction for the agreed upon amount from their public key on the altcoin network, to the seller's public key. This alone does not provide proof of payment, to combat this a reference to the block the transaction was published in is also required. After this, control over the disbursement of the kets (marketcoin units) purchased is granted. Control over the disbursement of the kets is removed once an order is included for their sale in a block.

To combat users reneging on trades and locking up others' money a timeout is placed on every transaction; if it is not finalised within a certain number time (or number of blocks, to be decided), the transaction is disregarded and control of the disbursement of funds is returned to the seller.

As there only needs to be one party to complete any actions after the orders are matched the finalisation of the transfer is the complete onus of the buyer. 

At the matching stage of the buyer only a little information is known:

* Pubkey of Seller
* Pubkey of Buyer
* Amount each way

To finalize this transaction (and avoid relaying excess data) the finalisation of the transaction takes place on Altcoin with a TX for the *amount* to *pubkey of seller*; then included in marketcoin blockchain as evidence (must have been in altcoin blockchain first; referenced through altcoin blockheaders included in MKC blockchain).

### Cancelling orders

An feature of any exchange is the ability to cancel orders. Marketcoin deals with this in two ways:

* Firstly, a timeout: All orders broadcast to the Marketcoin network include the height of the last block they may be included in. That is to say you can provide a timeout for the order if it remains unfilled.
* Secondly, as Marketcoin doesn't need to deal with zero-confirmation payments, the behaviour for dealing with broadcast orders/transactions will be different to that of Bitcoin. By allowing orders with a higher fee to replace those with a lower fee, orders can be updated or used in a transaction.

The latter is not as easy to apply to Altcoin orders on the Marketcoin network, and will need more thought.

### notes

* requirement to add tx and location in altcoin blockchain is sufficient since the PoW was done (altcoin block has hash <= diff); does it allow miners to manipulate market since altcoin block will probably produce marketcoin block too? marketcoin reference to current block *cannot* be a block it was simultaneously generated with? (Edit: not sure exactly why I thought this was an issue; not positive it is).

* Mining attack
* Include hash of tx in Altcoin merkle root; but not in the block. In the block is a conflicting tx that spends the output, also in merkle root. By including conflicting tx there is a doublespend and those coins cannot be redeemed.
* Trade Matched; Miner waits to include block with conflicting tx and hash of the finasation tx in merkle tree; Broadcasts broken solution to marketcoin network; confirming the transaction.
* Perhaps miners are asked to validate all trades on altcoin network; not just in merkle tree but also in block. Connect to altcoind armory style?
* So BTC/MKC miners check bitcoin blocks for tx finalisations to ensure they really are there. Do not accept block as valid if inconsistancies detected?
* Blocks from all altcoins kept for 24 hours? 288 blocks: the cutoff?. **MIGHT JUST WORK**

* How then to deal with Altcoin chainforks? and if bitcoin blcok in marketcoin is detected as invalid miners of OTHER currencies will still build on the block. Although BTC/MKC miners could detect the invalidity, LTC/MKC miners would not, and will build on the invalid block.

* How much trash can someone put in the merkle tree? How likely is it for an random hash to be in the merkle tree?

* Dynamic block requests? Can you request LTC block through MKC network? Perhaps.

## Proof-of-Work Chain (blockchain)

* Marketcoin has an odd blockchain; it is comprised of blocks produced by many different PoW systems; potentially a unique PoW system for every currency pair (it is whatever the Altcoin chooses).

* Each Marketcoin block links to the previous, regardless of the currency pair it was mine on. 

* Each block includes sequential headers of unincluded Altcoin blocks, upto some maximum.

* Each block MUST be merged mined with the Altcoin blockchain. Marketcoin has no native PoW system.

* Is a buffer needed? Should be enforced by default but is policy not protocol.

* More discussion is needed to figure out exactly what will happen with reorgs and possible attacks on this untested blockchain architecture.

## Block Validation

* Verfity all finalisations of transactions have txid in merkle tree
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

## Reward degredation

* Current plan for block reward degredation
* Each block reward pool is 0.9976 of the previous retarget size.
* IE: -0.24% every retarget period.
* MAX COINS: 21,000,000 exactly
* Half coins in existance: 288 weeks ish = ~5.5 years (also when block reward is half of orig)

## Issues

Some counter-party risk assumed by seller of Marketcoin; none for buyer unless prevented sending tx on altcoin network (51% attack), or including soln in marketcoin block.
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

Perhaps there can be an automatic voting system; blocks produced all contain a vote on currencies to include or exclude; when enough support is gained (probably needs to be 50%+ to align with other behaviours of the network; actually, strike that, not sure it matters as long as there is concensus on what the % should be) blocks continaing the new magicbits can be mined.

The above is feasable, I think. **RFC: Above paragraph; on new altcoin<->marktcoin currency paris**.

* not sure **integration with PoS** is possible currently; merged-mining not compatiable as far as I can tell. Difficult to validate PoS without entire blockchain (need to get txouts and coinage).

## Random Notes and Glossary

* Market volume provides rough scaling between PoW systems on a network wide level.

## References

Satoshi - Bitcoin Whitepaper, 2008

## Authors:

* XertroV (Max Kaye)
