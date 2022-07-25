from functools import singledispatch
class Student:
	pass
@singledispatch
def log(obj):
	print(obj)

@log.register(str)
def _(text):
	print(text.title())

@log.register(int)
def _(num):
	ns=[]
	while num:
		ns.append(num%10)
		num//=10
	for n in ns:
		print(n,end='')
	print()

@log.register(dict)
def _(d):
	print("{} kvs load...".format(len(d)))

@log.register(tuple)
@log.register(list)
def _(l):
	print('不会打印列表或者元组...')

@log.register(Student)
def _(s):
	print("额，学生类也打不了。。。")

log('china')
log(1234)
log([1,2,3,4])
log({'a':1,'b':2,'c':3})
log((1,))
log(Student())
