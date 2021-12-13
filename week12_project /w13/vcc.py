from socket import *
import sys
import cv2
import numpy as np



ipaddr=sys.argv[1]
port=int(sys.argv[2])

udp_client=socket(AF_INET,SOCK_DGRAM)
receive_size=400000

msg=input("CLIENT:")
udp_client.sendto(msg.encode("utf-8"),(ipaddr,port))

while True:
	recvData, addr = udp_client.recvfrom(receive_size)
	if not recvData:
		print('the server can not be connected...')
		break
	else:
		nparr = np.frombuffer(recvData, np.uint8)
		img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
		cv2.imshow('client', img_decode)
		if cv2.waitKey(1) & 0xFF == 27:
			break
udp_client.close()