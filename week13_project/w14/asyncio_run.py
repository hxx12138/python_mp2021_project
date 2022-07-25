import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main_1():
    print(f"started at {time.strftime('%X')}")

    await say_after(2, 'hello')
    await say_after(1, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main_1())

async def main_2():
    task1 = asyncio.create_task(
        say_after(2, 'hello'))

    task2 = asyncio.create_task(
        say_after(1, 'world'))

    print(f"started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main_2())