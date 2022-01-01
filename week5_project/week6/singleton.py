class Singleton:
	_instance=None
	def __init__(self, name, volume):
		self.name=name
		self.volume=volume

	def __new__(cls,name,volume):
		if not Singleton._instance:
		#if not hasattr(Singleton,'_instance'):
			Singleton._instance=object.__new__(cls)
			Singleton.__init__(Singleton._instance,name,volume)
		return Singleton._instance

slist=[Singleton('z',100) for i in range(10)]
for s in slist:
	print(hex(id(s)),end='\t')
	print(f"{s.name}\t{s.volume}")