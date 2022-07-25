import asyncio
import aiohttp
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


async def fetch_page(url):
    conn=aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(url) as response:
            return response.charset

loop = asyncio.get_event_loop()
urls=['https://www.163.com','https://www.qq.com','https://www.jd.com']
tasks=[loop.create_task(fetch_page(url)) for url in urls]
loop.run_until_complete(asyncio.wait(tasks))
for url,task in zip(urls, tasks):
	print("%s\t %s" % (url,task.result()))
loop.close()