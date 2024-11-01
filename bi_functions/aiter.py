# -- aiter(async_iterable)

# Returns an asynchronous iterator from an asynchronouse iterable
# Equivalent of calling x.__aiter__()

import asyncio
from utils.aiter import AsyncCounter

async def async_function():
    async for number in aiter(AsyncCounter(1, 5)):
        print(number)

asyncio.run(async_function)
