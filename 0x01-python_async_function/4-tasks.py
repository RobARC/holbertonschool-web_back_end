#!/usr/bin/env python3
""" Take the code from wait_n and alter it into a new function task_wait_n.
    The code is nearly identical to wait_n except task_wait_random is being
    called."""

from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ method wait_n Waits for ran delay until max_delay,
        returns list of actual delays"""
    spawn_list = []
    delay_list = []
    for i in range(n):
        delayed_task = task_wait_random(max_delay)
        delayed_task.add_done_callback(lambda x: delay_list.append(x.result()))
        spawn_list.append(delayed_task)

    for spawn in spawn_list:
        await spawn

    return delay_list
