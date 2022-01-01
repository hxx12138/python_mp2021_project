class Point:

	def __init__(self,x,y):
		self.x=x
		self.y=y

	def __add__(self,other):
		return Point(self.x+other.x,self.y+other.y)

	def __sub__(self,other):
		return Point(self.x-other.x,self.y-other.y)

	def __str__(self):
		return "({},{})".format(self.x,self.y)

	def __lt__(self,other):
		return self.x<other.x

	def __gt__(self,other):
		return self.x>other.x

	def __le__(self,other):
		return self.x<=other.x

	def __ge__(self,other):
		return self.x>=other.x

	def __eq__(self,other):
		return self.x==other.x

	def __ne__(self,other):
		return self.x!=other.x

	def __call__(self):
		'''
		Point类的实例可调用，也称可调用对象
		'''
		print('我不是函数，别调了')


p1=Point(1,2)
p2=Point(3,4)
print(p1+p2)
p3=p2-p1
print(p3)
print(p1<p2)
plist=[p1,p2,p3]
plist=sorted(plist,reverse=True)
print('\n'.join([str(p) for p in plist]))
p1()
p2()
p3()