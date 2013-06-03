# Generic Press Resources

This file contains information on Marketcoin designed to allow journalists and members of the press easy access to simple descriptions and explanations of Marketcoin, its inner workings and the theorised economic benefits and effects.

# Marketcoin

## Why?

I believe that no market should have a central point of failure. I believe that no market should be controlled by a few individuals. I believe that markets are crucial to the future of humanity, and I believe that such a fundamental construct of society should not funnel wealth into the pockets of a few. I believe markets should be free, governed by their users, and should ultimately facilitate liquid trade, not profit-mongering.

This is why I'm creating Marketcoin.

## How?

Marketcoin is designed with a similar philosophy and implementation to Bitcoin. Just as Bitcoin challenges the status quo of currency, Marketcoin will challenge the status quo of currency markets. It will help establish new standards of acceptable counter-party risk, fairness, transparency, and accessibilty.

Like Bitcoin, Marketcoin will operate on a blockchain, be p2p, and have a distributed wealth generation algorithm. Unlike contemporary markets, Marketcoin does not adopt standard auction systems, this prevents market abuse. As far as I'm aware this method is not employed elsewhere.

## What?

Marketcoin implements a novel blockchain structure in order to interface with each cryptocurrency being traded. The consequences of using a blockchain radically alter the mechanisms of how such a market operates.

Marketcoin operates in a unique way. Firstly, one currency being traded is *always* Marketcoin. Orders are submitted for both sides of exchange. At some unknown point in the future a block will be produced. Blocks only include orders which are able to be fully or partially matched. There will always be only one partially matched order, and this order will be a sell order for MKC. At this point the exchange algorithm evaluates who is owed what, and at what price. Orders are ranked on both sides of the exchange from highest to lowest bid and then progressively matched. For example, on the Bitcoin <-> Marketcoin exchange the order which pays the most Marketcoin for one Bitcoin is matched with the order which pays the most Bitcoin for one Marketcoin. The bid and ask are then averaged, and this is the exchange value *for that particular match*. If one order remains partially filled, it is matched with the next order in the same fashion. This continues until there is only one partially filled order to sell Marketcoin, and this is returned to the owner.

Furthermore, the Marketcoin blockchain does not resemble any existing PoW chain. Marketcoin will produce many *kinds* of blocks - one for each currency pair - each joined in a unified PoW chain, potentially each having different PoW functions. Each flavour of block (Be it MKCBTC, MKCLTC, MKCNMC, etc) has a block target period of a few minutes, however, the full chain has no specific number of blocks per retarget period: the more currency pairs, the more blocks, *but* each market will progress at a steady rate.

There are still many aspects of Marketcoin to discuss and decide, and any or all of what I've said here might not ever be implemented if a better idea comes along. This is the opportunity to engineer a market, something that little thought has previously been dedicated.

I have many ideas as to where Marketcoin coin should differ to Bitcoin, beyond what I've transcribed here, such as demurrage - which I believe will reduce speculation in Marketcoin and create a more liquid market as speculatory trades will need to be made twice (once in, once out). These are the fine points that help tune a market to efficiency without any effect on the implied exchange rate of two currencies, and as such cannot be ignored.

# Links

* [Whitepaper - Notes/Draft](./README.md)
* [Grant Proposal - Draft](./GrantProposal.md)

# Contact:

[Max Kaye](mailto:m@xk.io)


