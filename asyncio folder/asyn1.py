import asyncio
async def main():
    print('raj')
    task=asyncio.create_task(foo('text'))
    # await task
    await asyncio.sleep(2)
    print("finished")
async def foo(text):
    print(text)
    await asyncio.sleep(1)
asyncio.run(main())