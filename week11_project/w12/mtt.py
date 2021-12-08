from threading import Timer
from time import strftime, localtime

def get_time():
    print(strftime("%Y-%m-%d %H:%M:%S", localtime()))

print(strftime("%Y-%m-%d %H:%M:%S", localtime()))
while(1):
    t=Timer(2, get_time)
    t.start()
    t.join()