a=[1,2,3,4,5,6]
for x in reversed(a):
	pass
	print(x)

for x in reversed(range(1, 7)):
	pass
	#print(x)

class Countdown:
	def __init__(self,start):
		self.start=start
		self._n=self.start
		

	def __iter__(self):
		
		return self

	def __next__(self):
		if self._n>0:
			x=self._n
			self._n-=1
			return x
		else:
			raise StopIteration('Countdown is over')

	def __reversed__(self):
		self._n=1
		while self._n<=self.start:
			yield self._n
			self._n+=1

cd=Countdown(10)

for c in cd:
	print(c)

for c in reversed(cd):
	print(c)