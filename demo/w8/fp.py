from functools import wraps
from functools import reduce
from functools import partial
import time

def compose(x,y,f):
	return f(x)+f(y)

f=abs
print(compose(1,-2,f))

def f(x,y):
	return x*10+y

print(reduce(f,[1,2,3,4]))

def cton(s):
	digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	return digits[s]

print(reduce(f,map(cton,'1234')))

def odd(d):
	if d%2==0:
		return False
	else:
		return True

print(list(filter(odd,list(range(10)))))
print([x for x in range(10) if odd(x)])


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

def count():
    def f(j):
        def g():
            return j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())



def log(func):
	@wraps(func)
	def wrapper(*args,**kwargs):
		print("call "+func.__name__)#extra function
		return func(*args,**kwargs)
	return wrapper

@log
def now():
	print(time.strftime('%Y-%m-%d',time.localtime(time.time())))

now()
print(now.__name__)
#now=log(now), now() == log(now)()

while(1):
	pass

def log(text):
	def decorator(func):
		@wraps(func)
		def wrapper(*args,**kwargs):
			print(text+' '+'call '+func.__name__)
			return func(*args,**kwargs)
		return wrapper
	return decorator

@log('日志：')
def now():
	print(time.strftime('%Y-%m-%d',time.localtime(time.time())))
print(now.__name__)
now() #now = log('日志：')(now),now() == log('日志')(now)()

def growth(step=1,limit=200):
	g=0
	while(True):
		if g+step>limit:
			break
		g+=step
	return g

print(growth())
print(growth(step=3))

growth3=partial(growth,step=3)
print(growth3())
print(growth3(limit=300))

class Log:
	def __init__(self,logfile='out.log'):
		self.logfile=logfile
	def __call__(self,func):
		@wraps(func)
		def wrapper(*args,**kwargs):
			info="INFO: "+func.__name__+" was called"
			with open(self.logfile,'a') as file:
				file.write(info+'\n')
			return func(*args,**kwargs)
		return wrapper

@Log('test.log')
def myfunc():
	pass
#myfunc()

class Student:
	
	def __init__(self,id):
		self._id=id

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self,id_value):
		if(id_value<0):
			pass
		else:
			self._id=id_value

	@id.deleter
	def id(self):
		del self._id

s=Student(12)
print(s.id)
s.id=18
print(s.id)

class Employee:
	def __init__(self,name):
		self._name=name

	def _get_name(self):
		return self._name

	def _set_name(self,name):
		self._name=name

	def _del_name(self,name):
		del self._name
	
	Name=property(_get_name,_set_name,_del_name,'Name')

employee=Employee('lsy')
employee.Name='zhaojichang'
print(employee.Name)


class Finder:
	def __init__(self,path):
		self._path=path

	def get_path(self):
		return self._path

	@staticmethod
	def list_files(dir):
		print("{} contains files as listed:".format(dir))
		pass

	@classmethod
	def generate_finder(cls,root):
		print("class info: {}".format(cls))
		return cls(root)

print(type(Finder.list_files))
print(type(Finder.get_path))
print(type(Finder.generate_finder))

finder_1=Finder('info')
print(type(finder_1.list_files))
print(type(finder_1.get_path))
print(type(finder_1.generate_finder))

Finder.list_files('test')
finder_2=Finder.generate_finder('test')
print(finder_2.get_path())
finder_2.list_files('finder_2')
	