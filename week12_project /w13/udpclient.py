from socket import *
import sys

ipaddr=sys.argv[1]
port=int(sys.argv[2])

udp_client=socket(AF_INET,SOCK_DGRAM)

while True:
	msg=input("CLIENT:")
	udp_client.sendto(msg.encode("utf-8"),(ipaddr,port))
	reply,addr=udp_client.recvfrom(1024)
	if not reply:
		print('the server can not be connected...')
		break
	else:
		msg=reply.decode('utf-8')
		print("%s: %s" % (addr,msg))
		if msg[-2:]==':)':
			print('the server is alive, :)')
			break
		if msg[-3:]=='orz':
			print('wrong command, input again')
		if msg[-2:]==':(':
			print('the server is temporarily broken, keep pinging, orz')