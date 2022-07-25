class ContactList(list):
	def search(self,name):
		matching_contacts=[]
		for contact in self:
			if name in contact.get_name():
				matching_contacts.append(contact)
		return matching_contacts

class Contact:
	contacts=ContactList()
	def __init__(self,name,email):
		self.__name=name
		self.__email=email
		Contact.contacts.append(self)

	def get_name(self):
		return self.__name

	def get_email(self):
		return self.__email

	def __str__(self):
		return "Name:{}, email:{}".format(self.__name,self.__email)

class Supplier(Contact):

	def order(self,order):
		print("{} order to {}".format(order,self.get_name()))

class Friend(Contact):
	def __init__(self,name,email,mobile):
		super().__init__(name,email)
		self.__mobile=mobile

	def get_mobile(self):
		return self.__mobile

class AddressHolder:
	def __init__(self,street,city,state,code):
		self.__street=street
		self.__city=city
		self.__state=state
		self.__code=code

class BestFriend(Contact, AddressHolder):
	
	def __init__(self,name,email,phone,street,city,state,code):
		Contact.__init__(self,name,email)
		self.__phone=phone
		AddressHolder.__init__(self,street,city,state,code)

	

c1=Contact('zjc','jichang@buaa.edu.cn')
s1=Supplier('lys','yashi@buaa.edu.cn')
c2=Contact('test','test@buaa.edu.cn')
f1=Friend('ls','ls@buaa.edu.cn','1349848484')

print('\n'.join([str(c) for c in Contact.contacts]))
print('-------------------------')
print('\n'.join([str(c) for c in Contact.contacts.search('s')]))

s1.order('ll')