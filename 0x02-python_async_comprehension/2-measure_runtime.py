#!/usr/bin/env python3
'''Task 2. Run time for four parallel comprehensions module.
'''
import asyncio
from typing import List
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension  # Import the async_comprehension function

async def measure_runtime() -> float:
    '''Create a list of tasks to execute async_comprehension concurrently.
    '''

    st = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    et = time.time()
    return et - st
