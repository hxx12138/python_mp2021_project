import getpass

class Record:
	def read(self):
		pass
	def add(self,user):
		pass

class RecordError(Exception):
	def __init__(self):
		self.message='Access Record Failed'

class AddUserNotAllowedRecordError(RecordError):
	def __init__(self,user):
		self.message="Add user of {} failed due to no permission!".format(user)

class ReadUsersNotAllowedRecordError(RecordError):
	def __init__(self):
		self.message="read users not allowed due to no permission!"

class KeyRecords(Record):
	def __init__(self):
		self.users=['admin']

	def read(self):
		return ' '.join(self.users)

	def add(self,user):
		self.users.append(user)

class ProxyRecords(Record):
	def __init__(self):
		self.key_records=KeyRecords()
		self.secrect='test' #硬编码密码，不推荐，仅示例

	def read(self,pwd):
		if self.secrect==pwd:
			return self.key_records.read()
		else:
			raise ReadUsersNotAllowedRecordError()

	def add(self,pwd,user):
		if self.secrect == pwd:
			self.key_records.add(user)
		else:
			raise AddUserNotAllowedRecordError(user)
		return 1

def main():
	pr=ProxyRecords()
	pwd=getpass.getpass("plz input the pwd:")
	try:
		print(pr.read(pwd))
		if pr.add(pwd,'zjc'):
			print("ADD Succeeded...")
	except ReadUsersNotAllowedRecordError as runare:
		print(runare.message)
	except AddUserNotAllowedRecordError as aunare:
		print(aunare.message)
	except RecordError as re:
		print(re.message)

if __name__=='__main__':
	main()


