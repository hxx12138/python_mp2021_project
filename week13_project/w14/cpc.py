def consumer():
	while True:
		product=yield
		print('consume %s' % product)

def producer(n,con):
	con.send(None)#第一次需要先启动生成器，如果使用了装饰器则不需要该行
	for i in range(n):
		print("produce %s" % i)
		con.send(i)

con=consumer()
producer(20,con)