# Trade Example:

* Alice makes an order (Ord1) to sell MKC (ask) at a rate of 10 BTC/MKC for 10 MKC; total 100 BTC
    * Alice pledges these 10 MKC but still has access
* Bob makes an order (Ord2) to buy MKC (bid) at a rate of 12 BTC/MKC for 10 MKC; total 120 BTC
    * Bob pledges a small number of MKC (0.1) but still has access

* Both Ord1 and Ord2 are included in mkc-block 1000 (for the purposes of example, the block has only these two orders)
    * Both Alice and Bob lose access to their pledge
* The block is evaluated and Ord1 and Ord2 are matched
* Trade details are now decided. The decided rate is 11 BTC/MKC for a total of 110 BTC for 10 MKC. This is determined by the deterministic trade matching algorithm.
    
* Bob waits for a few confirmations, and once he's satisfied the orders are locked in he sends the funds to Alice's BTC address.
    * **Alice Receives BTC**
* After Bob's payment is confirmed on the Bitcoin network, he submits the finalisation tx to the Marketcoin network
* The Marketcoin network checks Bob's tx is in the referenced Bitcoin block, not just the merkle root, giving him the rights to unlock Alice's pledge: 10 MKC. In addition, his 0.1 MKC pledge is returned to him.
    * **Bob Receives MKC**
    
Because Bob has to pay BTC first, but the payment itself is what allows him to redeem the MKC, there is no risk of losing funds unless Bob does not redeem the MKC, or is prevented in some way.

Alice has no risk, unless Bob never sends the funds, in which case they are returned to her (along with Bob's pledge) after X blocks on that currency pair.