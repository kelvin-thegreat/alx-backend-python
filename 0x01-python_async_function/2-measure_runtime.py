#!/usr/bin/env python3
"""This module function for measuring the average execution time of the wait_n function
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure Average Execution Time

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay for each call.

    Returns:
        float: The average execution time per call to wait_n.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - start_time) / n
