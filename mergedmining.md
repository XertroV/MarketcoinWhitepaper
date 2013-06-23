# Merged Mining Scheme

## Special Requirements

A requirement of the scheme is the following

    Bitcoind -> Namecoind
       |___     ___|
       	  V     V
       	Marketcoind
       	
And users must be able to produce Bitcoin blocks, Namecoin blocks, BTC/MKC blocks, *and* NMC/MKC blocks.

This means that the PoW must defer in the following ways:

* Namecoin defers to Bitcoin
* BTC/MKC defers to Bitcoin
* NMC/MKC defers to Namecoin which defers to Bitcoin

This means that a Bitcoin block could provide the PoW needed for all 4 blocks. 

So, blocks need to describe **merged depth** which is defined as the number of deferences for PoW undergone. 0 for Bitcoin blocks, 1 for Namecoin and BTC/MKC blocks, and 2 for NMC/MKC blocks.

For Namecoin and BTC/MKC blocks they need to include the Bitcoin block header, coinbase tx and merkle tree branch, location of block hash in AuxPoW merkle tree. They can then verify the Bitcoin block hash falls below the difficulty.

* 80 bytes for the block header,
* 130 for coinbase tx
* ? * 33 Merkle tree branch for coinbase
* ? * 33 AuxPoW Merkle tree branch (32 for hash, 1 for left/right) [this increases like log(base=2,n) for n merged mined coins, I think]

At least 210 bytes

For NMC/MKC blocks they need to include the Namecoin block header, coinbase tx, location of block hash in mm merkle tree, then the Bitcoin block header, coinbase tx, location of block hash in AuxPoW merkle tree. Then they can verify the Bitcoin block hash falls below the difficulty.

* 80 * 2 for block headers
* 130+ * 2 for coinbase txs
* ? * 33 + ? * 33 Merkle tree branches for coinbase txs
* ? * 33 + ? * 33 for AuxPoW Merkle tree branches

Which is at least 420 bytes

With 5 minute block target times this equates to a minimum of 52 MB per year. Not pretty but it will work.

So, these details (along with the NMC/MKC or Namecoin block header) are stored in a vector (to accommodate potentially infinite depth).

AuxPoW Vector of n >= 2:

	# Root PoW Block (Min 210 Bytes)
	Block_Header			80
	Coinbase_Tx				130 [min]
	Tx_Merkle_Branch		33 * ceil(log(nTx)/log(2))
	
	# Subsequent Deferred PoW Blocks (Min 210 Bytes)
	Block_Header			80
	Coinbase_Tx				130
	Tx_Merkle_Branch		33 * ceil(log(nTx)/log(2))
	AuxPoW_Merkle_Branch	33 * ceil(log(nMM)/log(2))

___/MKC Block Header:

	# Normal Block Header (80 Bytes Total) - to be hashed
	Version					4
	Prev_Block_Hash			32
	Merkle_Root_Hash		32
	Time					4
	Bits					4
	Nonce					4
	  
	# Merged Mining			
	Depth					4
	AuxPoW_Merkle_Branch	33 * ceil(log(nMM)/log(2))
	AuxPoW_Blocks 			210 * Depth minimum
	
For NMC/MKC this means a block header size of at best 500 bytes, probably more like 1-2kb. Not great, but do-able.


Eventually the [Bitcoin Protocol Rules](https://en.bitcoin.it/wiki/Protocol_rules) will be re-written to apply to Marketcoin <br>
Criteria for valid block (partial):

    nBits = Bits (from MKC block)
    blockhash = hash(blockheader)
    currenthash = blockhash
    currentAuxMerkleBranch = AuxPow_Merkle_Branch
    currentMerkleBranch = Tx_Merkle_Branch
    for i in range(len(AuxPoW_Blocks)-1, -1, -1):
    	coinbaseTx = AuxPoW_Blocks[i].coinbaseTx
    	merkleRoot = construct (hash(coinbasetx) and currentMerkleBranch)
    	if merkleRoot != AuxPoW_Blocks[i].merkleRoot:
    		return fail
		auxMerkleRoot = construct(currenthash and currentAuxMerkleBranch)
		if auxMerkleRoot not in coinbaseTx.ScriptSig:
			return fail
		
		currenthash = hash(AuxPoW_Blocks[i])
		if block.AuxPoW_Merkel_Branch doesn't exist:
			if currenthash < nBits:
				return valid
			else:
				return fail
		currentAuxMerkleBranch = AuxPoW_Blocks[i].AuxPoW_Merkle_Branch
		currentMerkleBranch = AuxPoW_Blocks[i].Tx_Merkle_Branch
	
	return fail
	
I *think* this should work...
		