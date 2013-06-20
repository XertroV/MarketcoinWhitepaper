# Trade Example:

* Alice makes an order (Ord1) to sell MKC (ask) at a rate of 10 BTC/MKC for 10 MKC; total 100 BTC
    * Alice pledges these 10 MKC but still has access
* Bob makes an order (Ord2) to buy MKC (bid) at a rate of 12 BTC/MKC for 10 MKC; total 120 BTC
    * Bob pledges a small number of MKC (0.1) but still has access
* Both Ord1 and Ord2 are included in mkc-block 1000 (for the purposes of example, the block has only these two orders)
    * Both Alice and Bob lose access to their pledge
* The block is evaluated and Ord1 and Ord2 are matched
* Trade details are now decided. The decided rate is 11 BTC/MKC for a total of 110 BTC for 10 MKC. This is determined by the deterministic trade matching algorithm.
* Bob waits for a few confirmations (mkc-block 1005), and once he's satisfied the orders are locked in he sends the funds to Alice's BTC address (btc-block 3400).
    * **Alice Receives BTC**
* After Bob's payment is confirmed on the Bitcoin network (btc-block 3405), he submits the finalisation tx to the Marketcoin network
* Finalisation tx is included in a block (mkc-block 1020)
* The Marketcoin network checks Bob's tx is in the referenced Bitcoin block (btc-block 3400), not just the merkle root [1], giving him the rights to unlock Alice's pledge: 10 MKC. In addition, his 0.1 MKC pledge is returned to him.
    * **Bob Receives MKC**
    
Because Bob has to pay BTC first, but the payment itself is what allows him to redeem the MKC, there is no risk of losing funds unless Bob does not redeem the MKC, or is prevented in some way.

Alice has no risk, unless Bob never sends the funds, in which case they are returned to her (along with Bob's pledge) after X blocks on that currency pair.

[1] - Checking the block, and not just the merkle root is important as a BTC miner could inject their 'payment' txid into the merkle tree, include a conflicting transaction in the block (or a previous one), and pass this off to the Marketcoin network as 'proof of payment'. Without verifying the transaction itself was included this attack vector is left open.
