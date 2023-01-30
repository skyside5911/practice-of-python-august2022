import asyncio
from asyncore import loop
from lib2to3.pgen2.token import DOUBLESTAREQUAL
from urllib import response
import aiohttp
import time

urls =  'https://jsonplaceholder.typicode.com/todos/{}'

results = []

start = time.time()


async def get_symboles(urls):
    async with aiohttp.ClientSession() as session:
        for i in range(4000):
            response = await session.get(urls.format(i))
            results.append(await response.json())

    session.close()        


asyncio.run(get_symboles(urls))


dorutaion = time.time() - start

print(f"Completed {len(urls)} requests with {len(results)} results")

print(dorutaion)



