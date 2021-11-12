class DBError(Exception):
	
	def __init__(self,message):
		self.message=message

class DBhelper():
	
	def __init__(self,server_address,server_port,user,pwd):
		self._server_address=server_address
		self._server_port=server_port
		self._user=user
		self._pwd=pwd
		self._conn=None
	
	def get_server_address(self):
		return self._server_address

	def get_server_port(self):
		return self._server_port

	def __enter__(self):
		print("in __enter__: will try to connect the db server")
		return self

	def connect(self):
		try:
			print("in connect: connecting to the server")
			self._conn='success'#simulate the connection
			raise DBError('connect refused by the server')
		except DBError as dbe:
			print("in except: dbe.message")

	def close(self):
		print('in close: the connection is closed')
		#self._conn.close()
		pass

	def __exit__(self,type,value,trace):
		print("in __exit__: will close all the resource occupied")
		self.close()

with  DBhelper('127.0.0.1',3306,'zjc','123') as db:
	db.connect()


