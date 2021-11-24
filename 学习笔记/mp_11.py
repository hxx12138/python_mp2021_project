# 第10周 现代程序设计

# 作业问题 要用raise方法才能将错误抛出


# 课堂内容
# 抽象类 适配器模式

# 抽象类

# 类的另外一种构建方法，利用type函数
# metaclass 元类 -> 类 -> 实例
# 特殊点 类以Metaclass结尾
# 元类要继承type类型 元编程

def add(self,a,b):
	return a+b

class universe_Metaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = add
		return type.__new__(cls, name, bases, attrs)

class Game(metaclass=universe_Metaclass):
	def __init__(self, a, b):
		self.a = a
		self.b = b

game = Game(1,2)

print('run')
print(game.add(1,2))

# 元类的使用 ORM(Object Relational Mapping)
# 使用场景比较少


# 抽象类 abstract class
# 把多个类的共同属性抽象出来放入抽象类中。
# 抽象类中的方法不需要实现，在继承的子类中实现方法。（必须实现）（否则会报错）
# 多态性实现
# 抽象类的设计要尽可能简单

import abc

class Fruit(metaclass=abc.ABCMeta):

	@abc.abstractmethod
	def harvest(self):
		pass

	@abc.abstractmethod
	def grow(self):
		pass

#fruit = Fruit()	
#TypeError: Can't instantiate abstract class Fruit with abstract methods grow, harvest

# 继承与注册类的差别，注册子类不放到subclass里面

# 接口 Interface 最好只有一个方法
# 与抽象类区别很大 结构中只能实现方法不能放数据。
# 抽象类尽量避免多继承

# 泛函数 对不同参数类型进行不同的处理


# 适配器模式 消除借口不匹配产生的兼容性问题






