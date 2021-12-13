import os
import sys
import time
import random
from socket import *

class TCPClient:

	def __init__(self,server_ip,server_port):
		self._server_ip=server_ip
		self._server_port=server_port
		self._client=socket(AF_INET,SOCK_STREAM)

	def start(self):
		self._client.connect((self._server_ip,self._server_port))
		while True:
			msg=input("CLIENT：")
			self._client.send(msg.encode('utf-8'))
			data=self._client.recv(1024)
			if not data:
				continue
			if(data.decode('utf-8')=='再见!'):
				print("结束连接")
				break
			else:
				print("SERVER: %s" % data.decode('utf-8'))
		self._client.close()

def main():
	client=TCPClient(sys.argv[1],int(sys.argv[2]))
	client.start()

if __name__=='__main__':
	main()
