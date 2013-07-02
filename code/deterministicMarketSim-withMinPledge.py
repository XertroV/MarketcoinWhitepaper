#!/usr/bin/python

'''
NOT YET FUNCTIONAL

issues: 
	currently can generate more orders on the ask side than needed;
	there should never be any trades unfilled on either side, and 1 which is partially 
	filled on the ask side.'''

import random, math

class Order():
	def __init__(self, side, numMKC, rate):
		# side: 'bid' or 'ask'
		if side != 'bid' and side != 'ask':
			raise ValueError("Order is neither bid nor ask")
		self.side = side
		self.volume = numMKC
		self.rate = rate
		self.id = None
		
	def __repr__(self):
		return "%s@%s" % (self.volume, self.rate)
		
	def __lt__(self, other):
		if other.rate > self.rate:
			return True
		if other.rate == self.rate and other.volume > self.volume:
			return True
		return False
	
	def __gt__(self, other):
		if other.rate < self.rate:
			return True
		if other.rate == self.rate and other.volume < self.volume:
			return True
		return False
		
	def __eq__(self, other):
		if isinstance(other, Order):
			if other.rate == self.rate and other.volume == self.volume:
				return True
			if self.volume == 0 and self.volume == other.volume:
				return True
		return False
	
	def __ge__(self, other):
		return self > other or self == other
		
	def __le__(self, other):
		return self < other or self == other
		
	def __ne__(self, other):
		return not self == other
	
	def __add__(self, other):
		if isinstance(other, Order):
			return self.volume + other.volume
		return self.volume + other
		
	def getVolume(self):
		return self.volume
	
	def setId(self, id):
		self.id = id

class Trade():
	def __init__(self, buyOrder, sellOrder):
		self.volume = min(buyOrder.volume, sellOrder.volume)
		self.rate = (buyOrder.rate + sellOrder.rate)/2.0
		self.buyId = buyOrder.id
		self.sellId = sellOrder.id
		
	def __repr__(self):
		return "%3d - %4.2f at %6.2f - %-3d" % (self.buyId, self.volume, self.rate, self.sellId)
	
ORDERBOOK = {'bid':[], 'ask':[]}

# All MKC blocks require bid orders to be fully filled (bid ALT for MKC) and ask orders to have little or no change.

def sortOrders(listOfOrders):
	pass

def unfilledOrderbook():
	# incomplete, does not sort yet
	bids = ORDERBOOK['bid']
	totalBids = sum([bid.volume for bid in bids])
	asks = ORDERBOOK['ask']
	totalAsks = sum([ask.volume for ask in asks])
	if totalBids > totalAsks:
		return True

def genConst(side):
	return 1 if side == 'bid' else -1

def genRandomOrder(price, side):
	# volume limits
	maxVol = 10
	vol = random.random()*maxVol
	
	const = genConst(side)
	rate = round(price + abs(random.normalvariate(0,1)) * const, 2)
	
	minPledge = round(abs(random.normalvariate(0,0.01)), 2)
	
	return Order(side, vol, rate, minPledge)

def appendToOrderbook(price, side):
	ORDERBOOK[side].append(genRandomOrder(price, side))

def fillSideOfOrderbook(price, side):
	# fill orderbook with random orders
	const = genConst(side)
	if side == 'bid':
		# then prices should be above `price`
		for i in range(100):
			appendToOrderbook(price, side)
	if side == 'ask':
		while unfilledOrderbook():
			appendToOrderbook(price, side)

def fillOrderbook(price):
	fillSideOfOrderbook(price,'bid')
	fillSideOfOrderbook(price,'ask')

def setOrderIds():
	for side in ['bid','ask']:
		for i in range(len(ORDERBOOK[side])):
			ORDERBOOK[side][i].setId(i)

def printOrderbook():
	formatting = "%20s | %20s"
	print formatting % ("Bids","Asks")
	print formatting % ("%3s %7s %8s" % ('id','vol','rate'), "%8s %7s %3s" % ('rate','vol','id'))
	print '-'*21 + '|' + '-'*21
	for i in range(max(len(ORDERBOOK['bid']),len(ORDERBOOK['ask']))):
		ob = ORDERBOOK['bid'][i] if i < len(ORDERBOOK['bid']) else None
		oa = ORDERBOOK['ask'][-1*i - 1] if i < len(ORDERBOOK['ask']) else None
		
		pb = ''
		pa = ''
		
		if ob != None:
			pb = "%3d %7.4f %8.4f" % (ob.id, ob.volume, ob.rate)
		if oa != None:
			pa = "%8.4f %7.4f %3d" % (oa.rate, oa.volume, oa.id)
		print formatting % (pb, pa)
	print '\n'

blankOrder = Order('bid', 0, 0)
ALLTRADES = []

def popLeft(list):
	try:
		toReturn = list[0]
		list.remove(toReturn)
	except:
		toReturn = None
	return toReturn
	
def popRight(list):
	try:
		toReturn = list[-1]
		list.remove(toReturn)
	except:
		toReturn = None
	return toReturn

queueBids = []
def evalOrderbook():
	nextBid = blankOrder
	nextAsk = blankOrder
	while ORDERBOOK['bid'] != []:
		if nextBid == blankOrder:
			nextBid = popRight(ORDERBOOK['bid'])
		
		if nextAsk == blankOrder:
			# new ask means queued bids should be readded to the orderbook to judge against pledges
			nextAsk = popLeft(ORDERBOOK['ask'])
			
		
		if nextAsk.minPledge > nextBid.minPledge: # nextBid.minPledge is the amount being pledged, nextAsk.minPledge is the pledge requirement
			# trade doesn't happen
			# add bid to queueBids
			queueBids.append(nextBid)
			nextBid = 
		
		theTrade = Trade(nextBid, nextAsk)
		
		nextAsk.volume -= theTrade.volume
		nextBid.volume -= theTrade.volume
		
		ALLTRADES.append(theTrade)

def printTrades():
	allRates = []
	allVolume = []
	print '%41s' % ('Trades')
	print '-'*41
	for trade in ALLTRADES:
		print "%41s" % trade
		allRates.append(trade.rate)
		allVolume.append(trade.volume)
	print "Average price: %-6.2f" % (sum(allRates)/len(allRates))
	print "Max deviations: %-6.2f, %-6.2f" % (max(allRates), min(allRates))

def main():
	print '\n [Marketcoin] order evaluation simulation'
	print 'Rates are randomly calculated from a normal distribution'
	print 'mu = 100, sd = 1'
	print
	fillOrderbook(100)
	for side in ['bid','ask']:
		ORDERBOOK[side].sort()
	setOrderIds()
	printOrderbook()
	evalOrderbook()
	printTrades()
	







if __name__ == "__main__":
	main()
	
	
	
	
	
	
	
	
