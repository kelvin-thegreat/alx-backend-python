# async comprehension

This project contains tasks for learning to use asynchronous comprehensions in Python 3.

## Tasks
+ [x] 0. **Async Generator**<br/>[0-async_generator.py](0-async_generator.py) contains an asynchronous coroutine called `async_generator` that takes no arguments and meets the following requirements:
    + The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number 
    between 0 and 10. For the code below, make the following modifications:
    + Use the random module.
    + Use the Script below to testing the code. (save the script to file `0-main.py`)
  ```python3
      #!/usr/bin/env python3
      
      import asyncio
      
      async_generator = __import__('0-async_generator').async_generator
      
      async def print_yielded_values():
          result = []
          async for i in async_generator():
              result.append(i)
          print(result)
      
      asyncio.run(print_yielded_values())
  ```

+ [x] 1. **Async Comprehensions**<br/>[1-async_comprehension.py](1-async_comprehension.py) Has a script that meets the following requirements:
    + Import `async_generator` from the previous task and then write a coroutine called `async_comprehension` that takes no arguments
    + The coroutine will collect `10 random numbers` using an `async` comprehensing over `async_generator`, then return the `10 random numbers`.
    + Use the Script below for testing the code. (save the script to file `1-main.py`)
  ```python3
    #!/usr/bin/env python3
  
    import asyncio
    
    async_comprehension = __import__('1-async_comprehension').async_comprehension
    
    
    async def main():
        print(await async_comprehension())
    
    asyncio.run(main())
  ```
  + [x] 1. **Run time for four parallel comprehensions**<br/>[2-measure_runtime.py](1-async_comprehension.py) Has a script that meets the following requirements:
    + Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`.
    + `measure_runtime` should measure the total runtime and return it.
    + Use the Script below for testing the code. (save the script to file `2-main.py`)
  ```python3
    #!/usr/bin/env python3
  
    import asyncio
    
    async_comprehension = __import__('1-async_comprehension').async_comprehension
    
    
    async def main():
        print(await async_comprehension())
    
    asyncio.run(main())
  ```
