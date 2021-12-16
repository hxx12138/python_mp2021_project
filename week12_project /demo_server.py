import socket
import threading
import queue
import json # json.dumps(some)打包 json.loads(some)解包
import os
import os.path
import sys
 
 
IP = '127.0.0.1'
PORT = 9999 # 端口
messages = queue.Queue()
users = [] # 0:userName 1:connection
lock = threading.Lock()
 
def onlines(): # 统计当前在线人员
    online = []
    for i in range(len(users)):
        online.append(users[i][0])
    return online
 
class ChatServer(threading.Thread):

    global users, que, lock
 
    def __init__(self): # 构造函数
        threading.Thread.__init__(self)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        os.chdir(sys.path[0])

    # 接受来自客户端的用户名，如果用户名为空，使用用户的IP与端口作为用户名。如果用户名出现重复，则在出现的用户名依此加上后缀“2”、“3”、“4”……
    def receive(self, conn, addr): # 接收消息
        user = conn.recv(1024) # 用户名称
        user = user.decode()
        if user == '用户名不存在':
            user = addr[0] + ':' + str(addr[1])
        tag = 1
        temp = user
        for i in range(len(users)): # 检验重名，则在重名用户后加数字
            if users[i][0] == user:
                tag = tag + 1
                user = temp + str(tag)
        users.append((user, conn))
        USERS = onlines()
        self.Load(USERS,addr)
        # 在获取用户名后便会不断地接受用户端发来的消息（即聊天内容），结束后关闭连接。
        try:
            while True:
                message = conn.recv(1024) # 发送消息
                message = message.decode()
                message = user + ':' + message
                self.Load(message,addr)
            conn.close()
        # 如果用户断开连接，将该用户从用户列表中删除，然后更新用户列表。
        except:
            j = 0 # 用户断开连接
            for man in users:
                if man[0] == user:
                    users.pop(j) # 服务器段删除退出的用户
                    break
                j = j+1
        
            USERS = onlines()
            self.Load(USERS,addr)
            conn.close()
    
    # 将地址与数据（需发送给客户端）存入messages队列。
    def Load(self, data, addr):
        lock.acquire()
        try:
            messages.put((addr, data))
        finally:
            lock.release()
    
    # 服务端在接受到数据后，会对其进行一些处理然后发送给客户端，如下图，对于聊天内容，服务端直接发送给客户端，而对于用户列表，便由json.dumps处理后发送。
    def sendData(self): # 发送数据
        while True:
            if not messages.empty():
                message = messages.get()
                if isinstance(message[1], str):
                    for i in range(len(users)):
                        data = ' ' + message[1]
                        users[i][1].send(data.encode())
                        print(data)
                        print('\n')
    
                if isinstance(message[1], list):
                    data = json.dumps(message[1])
                    for i in range(len(users)):
                        try:
                            users[i][1].send(data.encode())
                        except:
                            pass
    
    def run(self):
        self.s.bind((IP,PORT))
        self.s.listen(5)
        q = threading.Thread(target=self.sendData)
        q.start()
        while True:
            conn, addr = self.s.accept()
            t = threading.Thread(target=self.receive, args=(conn, addr))
            t.start()
        self.s.close()


if __name__ == '__main__':
    cserver = ChatServer()
    cserver.start()