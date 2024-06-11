
#!/usr/bin/env python3
'''Task1.
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Makes a list of 10 numbers from the 10 generator.
    '''
    return [num async for num in async_generator()]
