import sys
from socket import *
from threading import Thread
import random
import time

CHARS='abcdefghijklmnopqrstuvwxyz'
ROUND=8

class ChatBot(Thread):
	
	def __init__(self,ip,port,mlength):
		super().__init__()
		self._ip=ip
		self._port=port
		self._max_msg_length=mlength

	def _random_message(self):
		message=[]
		for i in range(self._max_msg_length):
			word=[]
			for j in range(random.randint(1,5)):
				word.append(random.choice(CHARS))
			message.append(''.join(word))
		return ' '.join(message)
	
	def run(self):
		_client=socket(AF_INET,SOCK_STREAM)
		_client.connect((self._ip,self._port))
		_sent_count=0
		while True:
			msg=self._random_message()
			_client.send(msg.encode('utf-8'))
			_sent_count+=1
			time.sleep(random.randint(1,5))
			if _sent_count>ROUND:
				_client.send('byebye'.encode('utf-8'))
				break
		_client.close()

def main():
	ip=sys.argv[1]
	port=int(sys.argv[2])
	tlist=[]
	for i in range(int(sys.argv[3])):
		tlist.append(ChatBot(ip,port,random.randint(4,8)))
	for t in tlist:
		t.start()
	for t in tlist:
		t.join()
	print("All bots exit...")

if __name__=='__main__':
	main()


