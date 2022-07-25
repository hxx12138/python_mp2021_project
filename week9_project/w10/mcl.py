def say_hello(self):
	print(f"hi,I am {self.name}")

def __init__(self,name):
	self.name=name

People=type('People',(object,),dict(say_hello=say_hello,__init__=__init__))
p=People('zjc')
p.say_hello()