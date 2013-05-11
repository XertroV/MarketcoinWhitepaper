# Marketcoin: A Peer-to-Peer Exchange System for Bitcoin-like Currencies

Draft for public comment and contribution.

If you have any query or contibution in regards to this paper, please raise an issue. This includes but is not limited to: if something is not clear enough, or you think you've spotted something that needs to be considered.

## Abstract

A peer-to-peer decentralized exchange system would allow the users of a currency market to also be the govening body. Removed from the burdon of an external regulatory body would allow such markets to become truly free. Furthermore, facilitating relationships between crypto-currencies enables greater monetary diversity, something that is required if economies are to become resilient to negative effects of their chosen monetary systems. We propose a system that expands upon Bitcoin to enable trustless, peer to peer exchange of Bitcoin-like currencies. By allowing the proof of work chain to be a culmination of several smaller chains representing each currency pair, markets can remain resilient from the impacts of one another, while still conserving the cryptographic advantages bestowed by the virtue of being a crypto-currency. In addition, our system is largely incompatible with modern high performance computing algorithms; instead of instantaneous trade, orders are culminated into a block, and then algorithmically matched. This prevents most HPC exchange strategies and eliminates the spread. 

## Introduction

Marketcoin intro and context

Everything -> Marketcoin and Marketcoin -> Everything (but not Everything -> Everything)

## Orders and Transactions

Transactions in Marketcoin differ from those of Bitcoin-like systems. A transaction is broken down into three parts, and is not finalised until all of those parts are present in the blockchain. The first two are matching orders; that being an order to buy Altcoin for the maximum price of m, and an order to sell Altcoin at the minimum price of n, with n <= m. These are combined to form the beginning of a transaction, and are recorded simultaneously in the blockchain. The exchange algorithm is such that any two nodes will always produce the same matching orders from the same input (the block). Both orders include the public key of each party member. At this stage, the transaction is not yet finalised. For finalisation to occur the buyer of Marketcoin must provide a signed transaction for the agreed upon amount from their public key on the altcoin network, to the seller's public key. This alone does not provide proof of payment, to combat this a reference to the block the transaction was published in is also required. After this, control over the disbursement of the kets purchased is granted. Control over the disbursement of the kets is removed once an order is included for their sale in a block.

To combat users reneging on trades and locking up others' money a timeout is placed on every transaction; if it is not finalised within a certain number time (or number of blocks, to be decided), the transaction is disregarded and control of the disbursement of funds is returned to the seller.

As there only needs to be one party to complete any actions after the orders are matched the finalisation of the transfer is the complete onus of the buyer. 


## Issues

Some counter-party risk assumed by seller of Marketcoin; none for buyer unless prevented sending tx on altcoin network (51% attack). 

Timeouts might conflict if altcoin takes too long to produce blocks. Support must be general. Perhaps doing a difficulty style adjustment based on number of blocks over last retarget period (measured in time). Will be weird if a block is produced in more time than the retarget takes (misses a retarget period). Probably not worth considering yet.

Blockchain reorganisation on altcoin; if combined blockchain then it might invalidate later trades; perhaps lag time is placed on accepted block headers of altcoin in marketcoin blocks; like cannot be one of the most recent 6 blocks. How is that verified? Perhaps the limit is on how late after you can include the finalisation.

OR

Merged mining means a hash of the bitcoin block is in the marketcoin block header; the blocks are not invalid, just later become superfluous. When they are abandoned, the headers of the new section of the bitcoin blockchain is inserted in bulk into the marketcoin blockchain. marketcoin finalisations may become invalid on the bitcoin network, but will remain in play on the marketcoin network; they should be accepted as valid. This is an incentive for the buyer to send altcoin quickly, but wait to redeem the marketcoin for an hour or so to ensure there won't be a reorg on the altcoin blockchain. They can, however, choose to submit the finalisation when they choose. The client will warn of the risk of zero-conf finalisation.

* New currency pairs,
* minimum difficulty? 1% of network? how to measure?
* Trail period for volume?
* But blockchain spam from weird new currencies.
* Maybe whitelist of magicbits hardcoded? (bad soln, though leaning towards this atm)
* Adding new currency would require a hardfork
* Perhaps the number of markets available increases every year or so?
* Allows a period for new cryptocurrencies to compete for spots - requirements on market volume by the end of a trial period?
* Not sure if it can be done in a distributed fashion yet.

Perhaps there can be an automatic voting system; blocks produced all contain a vote on currencies to include or exclude; when enough support is gained (probably needs to be 50%+ to align with other behaviours of the network; actually, strike that, not sure it matters as long as there is concensus on what the % should be)

## Random Notes and Glossary

* Market volume provides rough scaling between PoW systems.

## References

Satoshi - Bitcoin Whitepaper, 2008

## Authors:

* XertroV (Max Kaye)
