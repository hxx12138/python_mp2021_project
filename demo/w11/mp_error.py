#在windows上会有问题
from multiprocessing import Process
print('main process start')
def run():
    pass
p=Process(target=run)#recursive
p.start()
if __name__=='__main__':
	pass