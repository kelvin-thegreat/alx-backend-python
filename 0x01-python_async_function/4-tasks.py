#!/usr/bin/env python3
'''Task 4. task_wait_random module
'''

import asyncio
from typing import List

'''Importing task_wait_random from the same module where it's defined'''
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes task_wait_random n times.
    '''
    wt = await asyncio.gather(
        *[task_wait_random(max_delay) for _ in range(n)]
    )
    return sorted(wt)

