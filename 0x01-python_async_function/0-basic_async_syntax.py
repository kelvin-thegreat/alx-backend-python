#!/usr/bin/env python3
'''
Module for Task 0: Asynchronous Coroutine to Wait for a Random Delay.
'''
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    '''
    Asynchronously waits for a random delay between 0 and max_delay seconds (inclusive). '''
    if max_delay < 0:
        raise ValueError("max_delay must be a non-negative value")

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

