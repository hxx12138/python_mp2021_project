import itertools
import operator

l1=list(range(1,6))
l2=[True,False,True,False,True]
for i in itertools.compress(l1,l2):
	pass
	#print(i)

def predictate(k):
	if k%2==0:
		return True
	else:
		return False

for i in itertools.takewhile(predictate,l1):
	pass
	#print(i)

for i in itertools.dropwhile(predictate,l1):
	pass
	#print(i)

for i in itertools.islice(l1,2):
	pass
	#print(i)

for i in itertools.accumulate(l1):
	pass
	#print(i)

l2=['a','b','c','d']
for s in itertools.starmap(operator.mul,enumerate(l2,1)):
	pass
	#print(s)

for i in itertools.chain(l1,l2):
	pass
	#print(i)

for i in itertools.chain.from_iterable(enumerate(l2,1)):
	pass
	#print(i)

l3=['e','f','g']
for i in itertools.product(l1,l2,l3):
	pass
	#print(i)

for e in zip(l1,l2,l3):
	pass
	#print(e)

z=zip(l1,l2)
#print(*z)
#print(*z)
for i in zip(*z):
	pass
	#print(i)

for e in itertools.zip_longest(l1,l2,l3,fillvalue='0'):
	pass
	#print(e)

l4=[1,1,2,3]
for i in itertools.combinations(l4,3):
	pass
	#print(i)
for i in itertools.combinations_with_replacement(l4,2):
	pass
	#print(i)
#for n in itertools.count(start=0,step=0.1):
	#pass
	#print(n)
#for s in itertools.cycle(l2):
#	pass
#	print(s)
for c in itertools.permutations(l4):
	pass
	#print(c)
for n in itertools.repeat('a',5):
	pass
	#print(n)
animals = ['duck','eagle','rat','giraffe','bear','bat','dolphin','shark','lion']
animals.sort(key=len,reverse=True)
for length,group in itertools.groupby(animals,len):#reversed(animals)
	pass
	print(length,':',list(group))

#g1,g2,g3=itertools.tee(l2,3)
#print(list(g1))
#print(list(g2))
#print(list(g3))