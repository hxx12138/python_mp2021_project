from collections import Iterable

def flatten(items,ingore_types=(str,bytes)):
	for x in items:
		if isinstance(x,Iterable) and not isinstance(x,ingore_types):
			yield from flatten(x,ingore_types)
		else:
			yield x

items=[1,2,[3,4,5],[6,7],[[[8]]],9,10]
finput=list(flatten(items))
print(finput)
#for x in flatten(items):
#	print(x)