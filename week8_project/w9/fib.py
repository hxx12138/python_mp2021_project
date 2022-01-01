def fib(max):
	n,a,b=0,0,1
	while(n<max):
		yield b
		a,b=b,a+b
		n+=1
	return 'done'

print(fib(6))
#print(len(fib(6)))

for f in fib(6):
	print(f)

f=fib(6)
while True:
	try:
		print(next(f))
	except StopIteration as si:
		print(si.value)
		break

