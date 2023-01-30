import sys
import os
import json
import asyncio
import time
import aiohttp


# Initialize connection pool
conn = aiohttp.TCPConnector(limit_per_host=100, limit=0, ttl_dns_cache=300)
PARALLEL_REQUESTS = 100
results = []
urls = [f'https://jsonplaceholder.typicode.com/todos/{i}' for i in range(4000)] #array of urls

start_time = time.time()

async def gather_with_concurrency(n):
    semaphore = asyncio.Semaphore(n)
    session = aiohttp.ClientSession(connector=conn)
    # session = aiohttp.ClientSession()

    # heres the logic for the generator
    async def get(url):
        async with semaphore:
            async with session.get(url) as response:
                print(response)
                obj = json.loads(await response.read())
                print(type(obj))
                #print(obj)
                results.append(obj)
    await asyncio.gather(*(get(url) for url in urls))
    await session.close()

# asyncio.run(gather_with_concurrency())
loop = asyncio.get_event_loop()
loop.run_until_complete(gather_with_concurrency(PARALLEL_REQUESTS))
conn.close()

duration = time.time() - start_time

print(f"Completed {len(urls)} requests with {len(results)} results")

print(f"finish within = {duration} seconds" )