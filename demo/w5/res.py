class Consumer:
	def __init__(self,name):
		self.name=name

class Restraunt:
	''' REstraunt class
	properties: name, location
	methods: checkin, checkout
	'''
	RID=0
	def __init__(self,name,location):
		self.name=name
		self.location=location
		self.id=Restraunt.RID
		self.consumer_list=[]
		Restraunt.RID+=1
	
	def chekin(self,c:Consumer):
		self.consumer_list.append(c)

	def checkout(self,c:Consumer):
		pass
		#self.consumer_list.remove(c)

	def print_consumers(self):
		for con in self.consumer_list:
			print(con.name)

def main():
	print(Restraunt.RID)
	c=Consumer('zjc')
	r=Restraunt('r','11,12')
	r.chekin(c)
	#Restraunt.checkin(r,c)
	r.print_consumers()

if __name__=='__main__':main()
