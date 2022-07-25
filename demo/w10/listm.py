def add(self,value):
	self.append(value)

class ListMetaClass(type):
	def __new__(cls,name,bases,attrs):
		attrs['add']=add
		return type.__new__(cls,name,bases,attrs)

class Mylist(list,metaclass=ListMetaClass):
	pass

l=Mylist()
l.add(1)
l.add(2)
print(l)