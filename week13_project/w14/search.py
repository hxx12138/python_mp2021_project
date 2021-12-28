#利用生成器send函数进行参数的传递示例
#注意执行顺序：search->openf->readl(根据find的tag决定是否继续读下一行）->find(这里yield要生成一个tag给readl)->(可能)printer，完了再回去（局部会有小循环，如果readl需要继续读的话）

import os
import functools
import sys

def gdeco(func):
	@functools.wraps(func)
	def wrapper(*args,**kwargs):
		resutled_g=func(*args,**kwargs)
		next(resutled_g)
		return resutled_g
	return wrapper

@gdeco
def search(target):
	while True:
		path=yield #获取参数
		g=os.walk(path)
		for _dir, _, files in g:
			for file in files:
				if file.find('.py')>0:
					file_path=os.path.join(_dir,file)
					print('in search, start target')
					target.send(file_path)#传值给别的生成器
					print('in search, after the send')

@gdeco
def openf(target):
	while True:
		file_path=yield
		with open(file_path) as f:
			print('in openf, start target')
			target.send((file_path,f))#传值给别的生成器
			print('in openf, after the send')

@gdeco
def readl(target):
	while True:
		file_path,f=yield
		try:
			for line in f:
				print('in readl, start send')
				tag=target.send((file_path,line))
				print('in readl, after the send')
				if tag:
					break
		except:
			continue

@gdeco
def find(target,pattern):
	tag=False
	while True:
		file_path,line=yield tag
		tag=False
		if pattern in line:
			print('in find, start the target')
			target.send(file_path)
			print('in find, after the send')
			tag=True

@gdeco
def printer():
	while True:
		file_path=yield
		print(file_path)

s=search(openf(readl(find(printer(),sys.argv[2]))))
s.send(sys.argv[1])
