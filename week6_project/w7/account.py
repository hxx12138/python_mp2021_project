class AccoutError(Exception):
	def __init__(self,user):
		self.user=user

class AccountNegativeDepositError(AccoutError):
	def __init__(self,user,m):
		self.user=user
		self.m=m
		self.message="{} deposit negative amount: {}".format(user,m)

class AccountBalanceNotEnoughError(AccoutError):

	def __init__(self,user,balance, m):
		self.user=user
		self.m=m
		self.balance=balance
		self.message="{}'s balance {} is smaller than the withdraw amount of {}. Loan is suggested.".format(user,balance,m) 

class Account:

	def __init__(self,user,balance):
		self._user=user
		self._balance=balance

	def set_balance(self,balance):
		self._balance=balance

	def get_balance(self):
		return self._balance

	def get_user(self):
		return self._user

	def deposit(self,m):
		if m<0:
			raise AccountNegativeDepositError(self.get_user(),m)
		else:
			self.set_balance(self.get_balance()+m)

	def withdraw(self,m):
		if self.get_balance()<m:
			raise AccountBalanceNotEnoughError(self.get_user(),self.get_balance(),m)
		else:
			self.set_balance(self.get_balance()-m)

account=Account('zjc',100)
try:
	#account.deposit(-100)
	account.withdraw(10000)
except AccountNegativeDepositError as ande:
	print(ande.message)
except AccountBalanceNotEnoughError as abnee:
	print(abnee.message)
except AccoutError:
	print('noname exception')
else:
	print('no except...')
	print(account.get_balance())
