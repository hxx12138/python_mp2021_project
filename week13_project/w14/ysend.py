def gtest():
	print('step-1')
	x=yield 1
	print(x)
	print('step-2')
	y=yield 2
	print(y)
	print('step-3')
	x=yield 3

g=gtest()
print(next(g))
print(next(g))
print(next(g))

#print(g.send(None))
#print(g.send('x=test'))
#print(g.send('y=test'))
