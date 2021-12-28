import threading
import asyncio

@asyncio.coroutine #标记为coroutine类型，过时的写法，仅示例
def foo(i):
    print('foo {} before yield from {}'.format(i,threading.currentThread()))
    yield from asyncio.sleep(100)
    print('foo {} after yield from {}'.format(i,threading.currentThread()))

loop = asyncio.get_event_loop()
tasks = [foo(i) for i in range(10000)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()