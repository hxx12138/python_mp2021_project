'''
Author: Yang Yang
LastEditors: Yang Yang
Date: 2021-12-10 12:09:34
LastEditTime: 2021-12-10 12:38:53
Description: 
'''
import socket
import numpy as np
import cv2
import sys

rsize = 400000

def receive_cam(addr):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(addr)
    while True:
        data, addr = s.recvfrom(rsize)
        nparr = np.frombuffer(data, np.uint8)
        img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        cv2.imshow('receive',img_decode)
        c = cv2.waitKey(50)
        if c == 27:  # 按了esc候可以退出
            break

receive_cam((sys.argv[1],int(sys.argv[2])))