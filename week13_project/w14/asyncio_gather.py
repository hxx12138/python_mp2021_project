import asyncio
import random

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(random.randint(1,5))
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    # Schedule three calls *concurrently*:
    # 注意其运行顺序
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 4),
        factorial("C", 7),
    )
    print(L)

asyncio.run(main())