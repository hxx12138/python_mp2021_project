import sys
import os
from socket import *
import time
import random

HOST='127.0.0.1'

RSIZE=1024

class TCPServer:#非多线程，只能响应一个client
	
	def __init__(self,port,maxconnections=5):
		self._port=port
		self._maxconnections=maxconnections
		self._server=socket(AF_INET, SOCK_STREAM)
	
	def start(self):
		self._server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)#端口释放后马上可以被重新使用
		self._server.bind((HOST,self._port))
		self._server.listen(self._maxconnections)
		print("SERVER is listening on %s" % self._port)
		while True:#如果有多个client同是发起连接，只响应一个，其他会等待
			conn,addr=self._server.accept()#block
			print(f"client's connection: {conn}, its address:{addr}")
			while True:
				try:
					data=conn.recv(RSIZE)
					if not data:
						break
					print("CLIENT: %s" % data.decode('utf-8'))
					if data.decode('utf-8')=='bye':
						conn.send("再见!".encode('utf-8'))
						break
					else:
						conn.send('收到!'.encode('utf-8'))
				except Exception as e:
					print("SERVER ERROR: %s" % e)
					break
			conn.close()
		self._server.close()

def main():
	ser=TCPServer(int(sys.argv[1]))
	ser.start()

if __name__=='__main__':
	main()

