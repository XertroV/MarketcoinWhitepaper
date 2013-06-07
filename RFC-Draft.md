# RFC Draft

[These instructions](https://en.bitcoin.it/wiki/Alt-chain_release_RFC) suggest an announcement format that should be taken seriously to give Marketcoin the best chance of success.

This document is a draft for the RFC topic on Bitcointalk in the Altchain subforum. It should not be published till the authors can agree, and should be posted under the Marketcoin user, currently controlled by Max Kaye.

# [RFC] - Marketcoin - The trustless decentralised cryptocoin exchange.

Marketcoin is a new altchain with its own currency. The network creates a trustless distrubuted exchange between most types of altchains.

Max would like Marketcoin to be as open as possible to give it the best chance of a successful launch and continued operation. No code has yet been created to be worked on, currently this is in the whitepaper stage.

## Current Resources

* [GitHub - MarketcoinWhitepaper](https://github.com/XertroV/MarketcoinWhitepaper)
    * The GitHub repo has everything written on Marketcoin thus far.

## Timeline

### Who (developers)

* Max Kaye; [email](mailto:m@xk.io)
* you?

### Benefits

Marketcoin does not compete with Bitcoin or other Altcoins.

Benefits include:

* Trustless exchange
* Open exchange
* Compatible with any merge-mineable chain. Unsure about Proof of Stake chains.
* No additional infrastructure required besides the Marketcoin client
* Does not require alteration to Altcoins. Transactions made are standard.
* Fair market. No spread. Tiny fee (like Bitcoin).
* No native Proof of work function; market security based on parent chain security.
* MORE

### Comparison to other alt chains

There are no comparible alt chains in existance to the authors' knowledge.

Marketcoin differs on many fronts. There is a novel blockchain implementation and an expansion to transactions, in order to facilitate the particular requirements of the network.

### Merged mining

Marketcoin (MKC) requires each currencypair be merged-mined with the parent chain.

### Shortcomings

* Not instant (still very quick, though)
* Block re-orgs on alternate chains may disrupt the market in a similar fashion to accepting zero-conf transactions.
* Still more work to do with issues (see whitepaper)
* Cannot trade with other marketcoin-like systems. Proof of payment is required to gain control of funds, if this is required on two networks neither transaction can be completely satisfied without additional protocol changes. I believe this *is* possible if orders (pledging the MKC as per the requirements of a buy order proves intent to pay at the very least)

### Attacks

* As Marketcoin requires merged mining with parent chains large amounts of hashing power injected into parent chains may disrupt the market in the same way they disrupt the parent chains. Marketcoin itself is immune from this attack at a network level as all PoW is offloaded onto parent chains.

### License

* Marketcoin will inherit the license of borrowed code where appropriate.
* The license may be the MIT license as Bitcoin use. This has not been decided yet. Max is in favour of public domain where possible or as liberal a license as possible.

### Schedule

1. *Source code release date:* Source code will be avaliable from the first commit. A fork will be made under the 'marketcoin' user on GitHub which will become the official repository. This has not yet taken place.
2. *Testnet start date:* Not yet determined.
3. *Mainnet start date:* Not yet determined.
4. *Exchange open date:* Not required but advantageous. If exchanges would like assistance having infrastructure ready for day 1, please contact the development team.

### A note on exchanges

To avoid spam, Marketcoin orders require a 'pledge' of MKC. This is the maximum exchange amount for sell orders and a % for buy orders. As this can be prohibitive for those entering Marketcoin exchanges may wish to enable exchange of MKC for impatient folk to acquire MKC faster than the network can provide (in terms of trading in).

# Authors

Max Kaye