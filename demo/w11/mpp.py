from multiprocessing import Process, Pipe
import time
import os
import random

def receiver(conn,name):
	#recv_c, send_c=conn
	#send_c.close()#只用读端，关闭写端，注意windows有可能不能提前关闭
	while True:
		try:
			message=conn.recv()
			print("{} receives a message: {}".format(name,message))
		except EOFError as eof:
			conn.close()
			break

def send(conn,name,messages):
	#recv_c,send_c=conn
	#recv_c.close() #只用写端，关闭读端，注意windows有可能不能提前关闭
	for message in messages:
		conn.send(message)
		time.sleep(random.randint(1,3))
	conn.close()

if __name__=='__main__':
	messages=[]
	with open('po.txt') as f:
		for line in f:
			messages.append(line.strip())
	
	recv_con,send_con=Pipe()#在主进程中建立管道
	
	printer=Process(target=receiver,args=(recv_con,'printer'))
	printer.start()

	sender=Process(target=send,args=(send_con,'sender',messages))
	sender.start()
	
	#注意windows建议仅在此处关闭
	recv_con.close() 
	send_con.close()

	sender.join()
	print("所有消息发送完成...")
	printer.join()
	print('所有消息接收完成...')