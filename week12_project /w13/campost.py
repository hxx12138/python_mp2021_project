'''
Author: Yang Yang
LastEditors: Yang Yang
Date: 2021-12-10 12:09:01
LastEditTime: 2021-12-10 12:37:34
Description: 
'''
import socket
import cv2
import numpy as np
import sys

def post_cam(udp_socket,addr,frame):
    img_encode = cv2.imencode('.jpg', frame)[1]
    data_encode = np.array(img_encode)
    data = data_encode.tobytes()
    udp_socket.sendto(data, addr)

def get_cam():
    capture = cv2.VideoCapture(0)
    
    #sudo sysctl -w net.inet.udp.maxdgram=65535 
    #mac上需要对udp的长度进行设定
    capture.set(3, 160)#故意修改小的，不然mac上容易超过udp发送数据的长度限制
    capture.set(4, 90)#windows上好像不用这么小
    
    while True:
        ret, frame = capture.read()  # ret为返回值，frame为视频的每一帧
        #cv2.imshow("post", frame)
        yield frame
        c = cv2.waitKey(50)
        if c == 27:  # esc可退出
            break

if __name__ == "__main__":
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    addr=(sys.argv[1], int(sys.argv[2]))
    for frame in get_cam():
        post_cam(udp_socket,addr,frame)