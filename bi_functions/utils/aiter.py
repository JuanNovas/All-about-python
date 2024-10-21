import asyncio

class AsyncCounter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current >= self.end:
            raise StopAsyncIteration
        self.current += 1
        await asyncio.sleep(1)
        return self.current - 1
