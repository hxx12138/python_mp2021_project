import socket
import tkinter
import tkinter.messagebox
import threading
import json
import tkinter.filedialog
from tkinter.scrolledtext import ScrolledText
 
IP = ''
PORT = ''
user = ''
listbox1 = '' # 用于显示在线用户的列表框
show = 1 # 用于判断是开还是关闭列表框
users = [] # 在线用户列表
chat = '------Group chat-------' # 聊天对象
 
#登陆窗口
 
root0 = tkinter.Tk()
root0.geometry("300x150")
root0.title('用户登陆窗口')
root0.resizable(0,0)
one = tkinter.Label(root0,width=300,height=150,bg="LightBlue")
one.pack()
 
IP0 = tkinter.StringVar()
IP0.set('')
USER = tkinter.StringVar()
USER.set('')
 
labelIP = tkinter.Label(root0,text='IP地址',bg="LightBlue")
labelIP.place(x=20,y=20,width=100,height=40)
entryIP = tkinter.Entry(root0, width=60, textvariable=IP0)
entryIP.place(x=120,y=25,width=100,height=30)
 
labelUSER = tkinter.Label(root0,text='用户名',bg="LightBlue")
labelUSER.place(x=20,y=70,width=100,height=40)
entryUSER = tkinter.Entry(root0, width=60, textvariable=USER)
entryUSER.place(x=120,y=75,width=100,height=30)
 
def Login(*args):
    global IP, PORT, user
    IP, PORT = entryIP.get().split(':')
    user = entryUSER.get()
    if not user:
        tkinter.messagebox.showwarning('warning', message='用户名为空!')
    else:
        root0.destroy()
 
loginButton = tkinter.Button(root0, text ="登录", command = Login,bg="Yellow")
loginButton.place(x=135,y=110,width=40,height=25)
root0.bind('<Return>', Login)

root0.mainloop()

# 建立连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, int(PORT)))
if user:
    s.send(user.encode()) # 发送用户名
else:
    s.send('用户名不存在'.encode())
    user = IP + ':' + PORT

# 聊天窗口
root1 = tkinter.Tk()
root1.geometry("640x480")
root1.title('群聊')
root1.resizable(0,0)

# 消息界面
listbox = ScrolledText(root1)
listbox.place(x=5, y=0, width=640, height=320)
listbox.tag_config('tag1', foreground='red',backgroun="yellow")
listbox.insert(tkinter.END, '欢迎进入群聊，大家开始聊天吧!', 'tag1')

INPUT = tkinter.StringVar()
INPUT.set('')
entryIuput = tkinter.Entry(root1, width=120, textvariable=INPUT)
entryIuput.place(x=5,y=320,width=580,height=170)

# 在线用户列表
listbox1 = tkinter.Listbox(root1)
listbox1.place(x=510, y=0, width=130, height=320)
 
 
def send(*args):
    message = entryIuput.get() + '~' + user + '~' + chat
    s.send(message.encode())
    INPUT.set('')
    
sendButton = tkinter.Button(root1, text ="\n发\n\n\n送",anchor = 'n',command = send,font=('Helvetica', 18),bg = 'white')
sendButton.place(x=585,y=320,width=55,height=300)
root1.bind('<Return>', send)


def receive():
    global uses
    while True:
        data = s.recv(1024)
        data = data.decode()
        print(data)
        try:
            uses = json.loads(data)
            listbox1.delete(0, tkinter.END)
            listbox1.insert(tkinter.END, "当前在线用户")
            listbox1.insert(tkinter.END, "------Group chat-------")
            for x in range(len(uses)):
                listbox1.insert(tkinter.END, uses[x])
            users.append('------Group chat-------')
        except:
            data = data.split('~')
            message = data[0]
            userName = data[1]
            chatwith = data[2]
            message = '\n' + message
            if chatwith == '------Group chat-------': # 群聊
                if userName == user:
                    listbox.insert(tkinter.END, message)
                else:
                    listbox.insert(tkinter.END, message)
            elif userName == user or chatwith == user: # 私聊
                if userName == user:
                    listbox.tag_config('tag2', foreground='red')
                    listbox.insert(tkinter.END, message, 'tag2')
                else:
                    listbox.tag_config('tag3', foreground='green')
                    listbox.insert(tkinter.END, message,'tag3')    
            listbox.see(tkinter.END)

r = threading.Thread(target=receive)
r.start() # 开始线程接收信息

root1.mainloop()
s.close()
