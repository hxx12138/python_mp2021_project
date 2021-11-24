import abc

class Fruit(metaclass=abc.ABCMeta):#class Fruit(abc.ABC)
	@abc.abstractmethod
	def harvest(self):
		pass

	@abc.abstractmethod
	def grow(self):
		pass

class Apple(Fruit):
	
	def harvest(self):
		print("从树上摘")

	def grow(self):
		print("种苹果树")

	def juice(self):
		print("做苹果汁")

class Watermelon(Fruit):
	def harvest(self):
		#super().harvest()
		print("从地里摘")

	def grow(self):
		print("用种子种")

@Fruit.register
class Orange:
	def harvest(self):
		print("从树上摘")
	
	def grow(self):
		print("种橘子树")

#f=Fruit()
a=Apple()
a.grow()
w=Watermelon()
w.harvest()

o=Orange()
o.grow()

print(isinstance(o,Fruit))
print(issubclass(Orange,Fruit))
print([sc.__name__ for sc in Fruit.__subclasses__()]) #no orange

