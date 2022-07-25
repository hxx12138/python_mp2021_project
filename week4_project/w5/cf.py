def fmin(self,x,y):
	return min(x,y)

class TestNumber:
	f=fmin

	def f_wighoutself(a,b):
		pass

tn=TestNumber()

print(type(fmin))
print(type(TestNumber.f))
print(type(tn.f))
print(type(tn.f_wighoutself))