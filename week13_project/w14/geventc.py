import gevent

def foo():
    print('running in foo')
    gevent.sleep(2)#模拟io
    print('com back from bar in to foo')
    return 'foo'

def bar():
    print('running in bar')
    gevent.sleep(1)#模拟io
    print('com back from foo in to bar')
    return 'bar'

def func():
	print('in func of no io')
	return 'func'

def fund():
	print('in fund of no io')
	return 'fund'

jobs=[gevent.spawn(foo),gevent.spawn(bar),gevent.spawn(func),gevent.spawn(fund)]
gevent.joinall(jobs)
for job in jobs:
	print(job.value) #能够保证返回的顺序