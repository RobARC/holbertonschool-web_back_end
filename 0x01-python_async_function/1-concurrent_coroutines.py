#!/usr/bin/env python3
""" import wait_random from the previous python file that you’ve
    written and write an async routine called wait_n that takes
    in 2 int arguments (in this order): n and max_delay.
    You will spawn wait_random n times with the specified max_delay.
    wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order without using
    sort() because of concurrency."""

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ method wait_n Waits for ran delay until max_delay,
        returns list of actual delays"""
    spawn_list = []
    delay_list = []
    for i in range(n):
        delated_task = asyncio.create_task(wait_random(max_delay))
        delated_task.add_done_callback(lambda x: delay_list.append(x.result()))
        spawn_list.append(delated_task)

    for spawn in spawn_list:
        await spawn

    return delay_list
