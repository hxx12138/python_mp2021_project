class BaseClass:
	num_base_calls=0
	def call_me(self):
		print("calling method on Base Class")
		BaseClass.num_base_calls+=1

class LeftSubclass(BaseClass):
	num_left_calls=0
	def call_me(self):
		BaseClass.call_me(self)
		#super().call_me()
		print("calling method on Left Subclass")
		LeftSubclass.num_left_calls+=1

class RightSubclass(BaseClass):
	num_right_calls=0
	def call_me(self):
		BaseClass.call_me(self)
		#super().call_me()
		print("calling method on Right Subclass")
		RightSubclass.num_right_calls+=1

class Subclass(LeftSubclass,RightSubclass):
	num_sub_calls=0
	def call_me(self):
		LeftSubclass.call_me(self)
		RightSubclass.call_me(self)
		#super().call_me()
		print("print calling method on Subclass")
		Subclass.num_sub_calls+=1
s=Subclass()
s.call_me()
#print(s)

print("\tsub_call:{}\n\
	left_call:{}\n\
	right_call:{}\n\
	base_call:{}".format(Subclass.num_sub_calls,LeftSubclass.num_left_calls,RightSubclass.num_right_calls,BaseClass.num_base_calls))