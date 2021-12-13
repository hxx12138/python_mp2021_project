from socket import *
import random
import sys
import cv2
import numpy as np

ipaddr=sys.argv[1]
port=int(sys.argv[2])
cap = cv2.VideoCapture(0)

cap.set(3, 160)
cap.set(4, 90)

recv_size=1024

udp_server=socket(AF_INET, SOCK_DGRAM)
udp_server.bind((ipaddr, port))
print("bind udp on port %s" % port)

while True:
	data,addr=udp_server.recvfrom(recv_size)
	if not data:
		break
	else:
		command=data.decode('utf-8')
		print("%s: %s" % (addr,command))
		if command=='play':
			while True:
				ret, frame = cap.read()
				cv2.imshow('server',frame)
				img_encode = cv2.imencode('.jpg', frame)[1]
				data_encode = np.array(img_encode)
				data = data_encode.tobytes()
				udp_server.sendto(data,addr)
				if cv2.waitKey(1) & 0xFF == 27:
					break#等下一个连接
		else:
			break
udp_server.close()
