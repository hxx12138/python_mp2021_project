class People:
	"""
	人的类，定义人相关的一些基本信息如姓名，身高，年龄等。

	"""
	def __init__(self,name,height,age):
		self.__name=name
		self.__height=height
		self.__age=age

	def get_name(self):
		return self.__name

	def set_name(self,name):
		self.__name=name

	def get_height(self):
		return self.__height

	def set_height(self,height):
		self.__height=height

	def get_age(self):
		return self.__age

	def set_age(self,age):
		self.__age=age

	def print_info(self):
		print('in People')
		print('Name:{},Age:{},Height:{}'.\
			format(self.get_name(),self.get_age(),self.get_height()))

	def __add__(self,other):
		return self.get_height()+other.get_height()

class Speaker():
	"""
	演讲家类
	"""
	def __init__(self,topic):
		self.__topic=topic

	def get_topic(self):
		return self.__topic

	def set_topic(self,topic):
		self.__topic=topic

	def speak(self):
		print('in Speaker')
		print("speak topic is {}".format(self.get_topic()))

class Student(People,Speaker):
	"""
	学生类，继承人的类，同时添加一些新的属性，并覆盖方法
	
	"""
	def __init__(self,name,height,age,topic,ID,major):
		People.__init__(self,name,height,age)
		Speaker.__init__(self,topic)
		self.__ID=ID
		self.__major=major

	def get_ID(self):
		return self.__ID

	def set_ID(self,ID):
		self.__ID=ID

	def get_major(self):
		return self.__major;

	def set_major(self,major):
		self.__major=major

	def print_info(self):
		print('ID:{}, Name:{}, Major:{}, Age:{}, Height:{}'.\
			format(self.get_ID(),self.get_name(),self.get_major(), self.get_age(),self.get_height()))

	def speak(self):
		#super(Student,self).print_info()
		#super(Student,self).speak()
		super().print_info()
		super().speak()

p1=People('z',175,40)
s1=Student('zjc',175,35,'python',33060828,'cs')
print(p1+s1)

#s1.print_info()
s1.speak()

People.print_info(s1)
