import asyncio
import random
import aiohttp
import time


async def get_sum(session, number):
    numbers = {'first_number': random.randint(0, 10), 'second_number': random.randint(0, 10)}

    async with session.post('http://0.0.0.0:8080/post', data=numbers) as r:
        print(f'Task {number}: {await r.text()}')


async def main(loop_count):
    start_time = time.time()

    async def one_iteration(number):
        async with aiohttp.ClientSession() as session:
            await get_sum(session, number)

    coroutines = [one_iteration(j) for j in range(loop_count)]
    await asyncio.gather(*coroutines)

    print(f"--- {(time.time() - start_time)} seconds ---")


loops = 1000

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loops))
loop.close()
