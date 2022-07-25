import asyncio
import psycopg

async def fetchmany(dsn,volume=1000):
    async with await psycopg.AsyncConnection.connect(dsn) as aconn:
        print(f"connection established for {volume}")
        async with aconn.cursor() as acur:
            await acur.execute("SELECT * FROM test")
            res=await acur.fetchmany(size=volume)
            return volume, res

dsn = 'dbname=zhaojichang'
loop = asyncio.get_event_loop()
tasks=[loop.create_task(fetchmany(dsn,volume=v)) for v in range(10,30)]
loop.run_until_complete(asyncio.wait(tasks))
for t in tasks:
    v,res=t.result()
    print(f'{v}:{len(res)}')