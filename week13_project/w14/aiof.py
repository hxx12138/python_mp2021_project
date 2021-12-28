import aiofiles
import asyncio
import sys
import os
import random

async def nio_read(path):#有可能出现文件编码的错误，
    async with aiofiles.open(path, mode='r') as f:
        print(f'try to read {path}...')
        await asyncio.sleep(random.randint(1,10))
        contents = await f.read()
        print(f'finish the read of {path}')
        return path, len(contents)

#通过loop无法运行nio_read,认为其没有await，但通过gather可以。
#注意观察gather的顺序
async def main():
    tasks=[]
    root=sys.argv[1]
    extention=sys.argv[2]
    d=os.walk(root)
    for _dir, _, files in d:
        for file in files:
            if file.find(extention)>0:
                tasks.append(nio_read(os.path.join(_dir,file)))
    results=await asyncio.gather(*tasks)
    for f,l in results:
        print(f'{f}: {l}')

asyncio.run(main())