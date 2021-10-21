#!/usr/bin/env python3
""" Import async_comprehension from the previous file and write a
    measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather. measure_runtime should
    measure the total runtime and return it. Notice that the total
    runtime is roughly 10 seconds, explain it to yourself.
"""
import time
from asyncio import tasks
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Method measure_runtime for four parallel comprehensions """
    tasks = []
    start_time = time.time()
    for i in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*tasks)
    end_time = time.time()

    return end_time - start_time
