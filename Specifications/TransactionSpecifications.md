# Transaction Examples

## Order

### Sell MKC (ask)

nChainUnlockTime = currentBlock + 288 (24hrs with 5 minute block targets, measured on the currency pair sub-chain).

nUnlockTime and nChainUnlockTime are the opposites of nLockTime. After the specified point the transaction is no longer valid unless it was filled before this point.

nUnlockTime = 400 means that the transaction is valid and can be filled up until, but not including, block 400.

nChainUnlockTime = 400 means that the tx becomes invalid on the 400th block of *that currencypair chain*.


#### Script PubKey requirements:

* Must be filled by providing proof-of-payment.
* This inputs must be (in no particular order): 
	* txid
	* tx
	* block_hash
	
Functions:

* Verify txid belongs to tx
* Verify txid is in merkle root of referenced block
* Verify tx is in referenced block (if recent enough)
* Verify

Script Sig:

    <txid> <rawtx> <blockhash>

Script PubKey:

    OP_LOADBLOCK OP_DUP OP_TXINBLOCKVERIFY OP_GENTXID OP_EQUALVERIFY
    
* `OP_LOADBLOCK` will load the altchain block with `<blockhash>` into memory and removes `<blockhash>` from stack
* `OP_DUP` duplicates `<rawtx>` on the stack
* `OP_TXINBLOCKVERIFY` will verify `<rawtx>` is included in the altchain block, removes `<rawtx>` from stack
* `OP_GENTXID` will generate a txid from `<rawtx>` and remove `<rawtx>`
* `OP_EQUALVERIFY` removes `<txid>` and `<txid2>` and ensures they're the same

Wow, that's awful…

    OP_VERIFYPAYMENT
    
That's better. Not as useful though.

    OP_UNLOCKED OP_IF OP_VERIFYPAYMENT OP
    
#### Output Requirements:

Output of a finalised order *must* be paid to the pubkey of the order with which this order was matched.

IE: Ord1 (ask) and Ord2 (bid) are matched. Output of Ord1 must go to the public key used in Ord2. This means the finalisation says almost nothing about outputs.

### Buy MKC (bid)