# -- *awaitable anext(async_iterator[, default]) --

# Asynchronous version of next
# Takes an asynchronous iterator and returns the next item

import asyncio
from utils.anext import async_counter


async def async_function():
    generator = async_counter(5)  
    
    try:
       while True:
           value = await anext(generator)
           print(value)
    except StopAsyncIteration:
        print("The iterator has ended")

asyncio.run(async_function())
