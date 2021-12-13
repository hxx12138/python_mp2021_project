import sys
import os
from threading import Thread
from socket import *
import random
import time

# 利用socket和多线程，实现支持多人对话的聊天室。
# 具体地，实现Manager和Chatter 两个类，Chatter只需和Manager之间建立一对一联系，
# 而Manager则负责广播或转发所有用户的消息。
# cd Documents/python_mp2021_project/week12_project\ /w13

BUFFERS=1024
MAXC=64


# 1. 实现Manager类, 服务器，管理成员进入和离开聊天室，接收成员消息并广播
# 3. Manager类使用多线程服务多个用户
# 5. Manager类具备定向转发功能，比如Chatter可以在消息中通过@指定特定用户，这样Manager将仅转发给被指定用户。
# 7. Manager也应保存所有聊天室记录到硬盘。

class Manager(Thread):

    def __init__(self,name,conn):
        super().__init__()
        self.name = name
        self.conn = conn
    
    def speak(self):
        print("欢迎{}进入聊天室...".format(self.name))
        while True:
            try:
                msg=self.conn.recv(BUFFERS)
                if not msg:
                    break
                print("{}:{}".format(self.name,msg.decode('utf-8')))
                if msg.decode('utf-8')=='byebye':
                    print("{}离开了聊天室...".format(self.name))
                    break
            except Exception as e:
                print("server error %s" % e)
                break
        self.conn.close()

    def run(self):
        return

# 2. 实现Chatter类, 用户, 向管理员发送加入和退出请求，发送和接收消息
# 4. Chatter用户发送和接收消息需要依赖不同线程进行
# 6. Chatter在离开时，自动保存聊天记录到硬盘（包括时间、发信人，信息）。

class Chatter(Thread):

    def __init__(self):
        super().__init__()

    def run(self):
        return



