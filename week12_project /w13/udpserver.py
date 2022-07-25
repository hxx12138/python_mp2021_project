from socket import *
import random
import sys

ipaddr=sys.argv[1]
port=int(sys.argv[2])
recv_size=1024

udp_server=socket(AF_INET, SOCK_DGRAM)
udp_server.bind((ipaddr, port))
print("bind udp on port %s" % port)
while True:
	data,addr=udp_server.recvfrom(recv_size)#block
	if not data:
		break
	else:
		command=data.decode('utf-8')
		print("%s: %s" % (addr,command))
		if command=='heartbeat':
			if random.random()>0.5:
				udp_server.sendto("I am alive,:)".encode('utf-8'),addr)
			else:
				udp_server.sendto("I was dead,:(".encode('utf-8'),addr)
		else:
			udp_server.sendto("Invalid command,orz".encode('utf-8'),addr)


