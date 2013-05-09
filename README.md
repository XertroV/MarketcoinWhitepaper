# Marketcoin: A Peer-to-Peer Exchange System for Bitcoin-like Currencies

Draft for public comment and contribution

## Abstract

A peer-to-peer decentralized exchange system would allow the users of a currency market to also be the govening body. Removed from the burdon of an external regulatory body would allow such markets to become truly free. Furthermore, facilitating relationships between crypto-currencies enables greater monetary diversity, something that is required if economies are to become resilient to negative effects of their chosen monetary systems. We propose a system that expands upon Bitcoin to enable trustless, peer to peer exchange of Bitcoin-like currencies. By allowing the proof of work chain to be a culmination of several smaller chains representing each currency pair, markets can remain resilient from the impacts of one another, while still conserving the cryptographic advantages bestowed by the virtue of being a crypto-currency. In addition, our system is largely incompatible with modern high performance computing algorithms; instead of instantaneous trade, orders are culminated into a block, and then algorithmically matched. This prevents most HPC exchange strategies and eliminates the spread. 

## Introduction

Marketcoin intro and context

Everything -> Marketcoin and Marketcoin -> Everything (but not Everything -> Everything)

## Orders and Transactions

Transactions in Marketcoin differ from those of Bitcoin-like systems. A transaction is broken down into three parts, and is not finalised until all of those parts are present in the blockchain. The first two are matching orders; that being an order to buy Altcoin for the maximum price of m, and an order to sell Altcoin at the minimum price of n, with n <= m. These are combined to form the beginning of a transaction, and are recorded simultaneously in the blockchain. The exchange algorithm is such that any two nodes will always produce the same matching orders from the same input (the block). Both orders include the public key of each party member. At this stage, the transaction is not yet finalised. For finalisation to occur the buyer of Marketcoin must provide a signed transaction for the agreed upon amount from their public key on the altcoin network, to the seller's public key. This alone does not provide proof of payment, to combat this a reference to the block the transaction was published in is also required. After this, control over the disbursement of the kets purchased is granted. Control over the disbursement of the kets is removed once an order is included for their sale in a block.

To combat users reniging on trades and locking up others' money a timeout is placed on every transaction; if it is not finalised within a certain number of blocks (of the currency-pair), the transaction is disregarded and control of the disbursement of funds is returned to the seller.

As the finalisation of the transfer is the complete onus of the buyer...



## Refernces

## Authors:

* XertroV (Max Kaye)
