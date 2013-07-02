# RFC Draft

[These instructions](https://en.bitcoin.it/wiki/Alt-chain_release_RFC) suggest an announcement format that should be taken seriously to give Marketcoin the best chance of success.

This document is a draft for the RFC topic on Bitcointalk in the Altchain subforum. It should not be published till the authors can agree, and should be posted under the Marketcoin user, currently controlled by Max Kaye.

# [RFC] - Marketcoin - a distributed p2p cryptocoin exchange network with no counterparty risk; impervious to outside influence or control.

Marketcoin is a new altchain with its own currency. The network creates a trustless distrubuted exchange that is able to interface with most types of altchains. Marketcoin is only able to trade between cryptocurrencies.

Max (XertroV) would like Marketcoin to be as open as possible to give it the best chance of a successful launch and continued operation. Code is starting to be written and experimented with.

## Current Resources

* [GitHub - MarketcoinWhitepaper](https://github.com/XertroV/MarketcoinWhitepaper)
    * The GitHub repo has everything written on Marketcoin thus far. It was going to be a whitepaper, but I feel like it might be a bit too cumbersome to bother with; protocol specification can be just as specific.

## Technical and timeline

### Who (developers)

* Max Kaye, XertroV; [email](mailto:m@xk.io)
* you?

### Benefits

Marketcoin does not compete with Bitcoin or other Altcoins, currently.

Benefits include:

* Trustless exchange
* Open exchange
* Compatible with any merge-mineable chain. Should be compatible with PoW elements of hybrid PoS/PoW chains.
* No additional infrastructure required besides the Marketcoin client
* Does not require alteration to Altcoin policy/protocol. Transactions are required to be standard.
* Fair market. No spread. Tiny fee (like Bitcoin).
* No native Proof of work function; market security based on parent chain security.
* Allows trustless trading between forked chains (in the case of a network split).
* Resistant to high frequency trading
* Resistant to market manipulation
* More (probably)

### Comparison to other alt chains

There are no comparible alt chains in existance to the authors' knowledge.

Marketcoin differs on many fronts. There is a novel blockchain implementation and an expansion to transactions in order to facilitate the particular requirements of the network.

### Merged mining

Marketcoin (MKC) requires each currencypair be merged-mined with the parent chain.

### Shortcomings

* Not instant (still very quick, though)
* Block re-orgs on alternate chains may disrupt the market with similar consequences to accepting zero-conf transactions, easily mitigated.
* Issues and attack vectors are not well discussed yet.
* Possibly unable to trade with other marketcoin-like systems. Proof of payment is required to gain control of funds, if this is required on two networks neither transaction can be completely satisfied without additional protocol changes. Protocol changes are currently required to facilitate this. (Need to accept pledges as proof-of-payments, both networks must know of each other, not merge minable, etc)
* Proof-of-Work algorithms and valid block criteria, etc, for each altcoin must be known to Marketcoin as it must validate altcoin blocks to ascertain proof of payment. This means hard-fork changes to a traded currency may mean a hardfork change to Marketcoin :(
* MORE (probably)

### Attacks

* As Marketcoin requires merged mining with parent chains large amounts of hashing power injected into parent chains may disrupt the market in the same way they disrupt the parent chains. Marketcoin itself is immune from this attack at a network level as all PoW is offloaded onto parent chains.
* Trading can be halted for a short while by an attacker but they will quickly lose their MKC pledges.
* Probably new economic attack methods that are not well understood.
* MORE (probably)

## License

* Marketcoin will inherit the license of borrowed code where appropriate.
* The license may be the MIT license as Bitcoin use. This has not been decided yet. Max is in favour of public domain where possible or as liberal a license as possible.

### Schedule

1. *Source code release date:* Source code will be avaliable from the first commit. A fork will be made under the 'marketcoin' user on GitHub which will become the official repository.
2. *Testnet start date:* Not yet determined.
3. *Mainnet start date:* Not yet determined.
4. *Exchange open date:* Not required but advantageous. If exchanges would like assistance having infrastructure ready for day 1, please contact the development team at a point closer to the release date.

### Want to know more?

Of course you do! Head over to GitHub and take a look at what design documents have been written so far. https://github.com/XertroV/MarketcoinWhitepaper

## Economics 

### Market Structure

The market structure reflects the blockchain structure to a degree; it is, after all, technically bound by it. It is very different in some ways from contemporary market structures.

Each currency pair runs in parallel and contains no conflicting transactions. Each currency pair is a blockchain which contains matched bids and asks, and transactions. Bids and asks are only matched if bid >= ask and the exchange value is the average of the two. Bids and asks are matched *as they are included in a block*, and they must be included in the same block. The time between each block is can be thought of a 'round' length, where bids and asks may be submitted or retracted within this period, and at the end of this period they are collected and matched, where possible.

### Demurrage?

Max is torn on the topic of demurrage; it may be an interesting property for an exchange to have, but possibly not a popular one. As the economic effects in such an exchange environment are unknown, it is difficult to tell whether it will be advantageous for the exchange as a whole or not. However, the safe option is to not include such a feature, and so unless there is overwhelming evidence that it should be adopted, it will not be. Remember that anyone can take and fork Marketcoin and release a clone with demurrage. Let the free market decide.

### Equitable markets

Part of the problem Marketcoin aims to solve is that of the equality that contemporary markets lack. One massive member of the community working against 100 small members should not have greater power just because of a greater centralisation of wealth. Part of the problem that a market with a short interval (like 5 minutes) instead of continuous trading would solve is that the community is able to proactively react to massive movements before they've become solidified in the blockchain. In addition, as orders are not stored in the blockchain, there is competition within each round for the placement of orders. Because not all executed orders will trade at the same price, there is the possibility of intra-block arbitrage, forcing big players to pay more to move a lot of value through the market, and allowing everyday users to profit from the experience.

### Further discussion

More discussion is warranted in terms of the economic repercussions of such a system. If something is missing please suggest it be answered and it will be added.

# Authors

* Max Kaye

# Thanks

* Tod Gillespie