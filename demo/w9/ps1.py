import time
class Investor:
	def __init__(self,name,stock):
		self._name=name
		self._stock=stock

	@property
	def stock(self):
		return self._stock
	@stock.setter
	def stock(self,value):
		self._stock=value

	def update(self):
		print("{} invest on {} with price {}: sell it now!!!".format(self._name,self._stock.name,self._stock.price))

class Stock:
	def __init__(self,name,price):
		self._name=name
		self._price=price
		self._investors=[]

	@property
	def name(self):
		return self._name
	
	@property
	def price(self):
		return self._price

	@price.setter
	def price(self,value):
		if self._price>value:
			self.notify()
		self._price=value
	
	def attach(self,investor):
		self._investors.append(investor)

	#deattach

	def notify(self):
		for investor in self._investors:
			investor.update()

def main():
	s=Stock('区块链',11.11)
	i1=Investor('zjc',s)
	i2=Investor('lys',s)
	s.attach(i1)
	s.attach(i2)
	s.price=13
	time.sleep(1)
	s.price=10

if __name__=='__main__':main()	
	