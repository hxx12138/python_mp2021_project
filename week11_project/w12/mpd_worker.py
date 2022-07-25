import time
from mp_qm import QueueManager
from urllib.request import urlretrieve
import sys

def download_image(imageurl,root='./'):
	filepath=root+imageurl[imageurl.rindex('/')+1:]
	#print(filepath)
	try:
		urlretrieve('http://'+imageurl,filepath)
		#print(filepath)
		return 1
	except:
		#此处仅示例，属于不好的压制异常的风格
		return 0

if __name__=='__main__':
	ip=sys.argv[1]
	port=int(sys.argv[2])
	pwd='admin'
	rootpath='./images/'
	wname='13w1'
	#使用QueueManager注册获取Queue的方法名称,否则找不到对应的方法
	QueueManager.register('get_task_queue')
	QueueManager.register('get_result_queue')

	#连接到服务器
	print('Connect to server {}:{}...'.format(ip,port))
	# 端口和验证口令
	m=QueueManager(address=(ip, port), authkey=pwd.encode())
	m.connect()
	#获取Queue的对象:
	task=m.get_task_queue()
	result=m.get_result_queue()
	#从task队列取任务,并把结果写入result队列:
	while(not task.empty()):
	        imageurl = task.get(True,timeout=1)
	        #print('run task download %s...' % imageurl)
	        status=download_image(imageurl,rootpath)
	        if status:
	        	result.put('{} succeeded by {}'.format(imageurl[imageurl.rindex('/')+1:],wname))
	        else:
	        	result.put('{} failed by {}'.format(imageurl[imageurl.rindex('/')+1:],wname))
	# 处理结束:
	print('worker finished...')