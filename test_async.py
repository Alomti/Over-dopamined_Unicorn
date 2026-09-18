import asyncio
import time

async def example_async_action(t, c):
    await asyncio.sleep(t)
    print(c)

async def main():
    start1 = time.perf_counter()
    await example_async_action(2, 'A')
    await example_async_action(2, 'B')
    await example_async_action(2, 'C')
    end1 = time.perf_counter()
    start2 = time.perf_counter()
    await asyncio.gather(
        example_async_action(2, 'A'),
        example_async_action(2, 'B'),
        example_async_action(2, 'C')
    )
    end2 = time.perf_counter()
    print(f'Po kolei: {end1 - start1}')
    print(f'Na raz: {end2 - start2}')

asyncio.run(main())