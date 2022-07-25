import sys
import os
from threading import Thread
from socket import *

BUFFERS=1024
MAXC=64

def speak(name,conn):
	print("欢迎{}进入聊天室...".format(name))
	while True:
		try:
			msg=conn.recv(BUFFERS)
			if not msg:
				break
			print("{}:{}".format(name,msg.decode('utf-8')))
			if msg.decode('utf-8')=='byebye':
				print("{}离开了聊天室...".format(name))
				break
		except Exception as e:
			print("server error %s" % e)
			break
	conn.close()

if __name__=='__main__':
	ip='127.0.0.1'
	port=30000
	server=socket(AF_INET,SOCK_STREAM)
	server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)#端口释放后马上可以被重新使用
	server.bind((ip,port))
	server.listen(MAXC)
	print("MT server is started...")
	while True:
		conn,addr=server.accept()#block
		#print(conn)
		ci,cp=addr
		#启动一个线程处理该连接，主线程继续处理其他连接
		t=Thread(target=speak,args=("client-"+ci+"-"+str(cp),conn))
		t.start()
	server.close()

