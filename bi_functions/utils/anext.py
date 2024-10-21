import asyncio

async def async_counter(amount: int):
    for i in range(amount):
        yield i
        await asyncio.sleep(1)  