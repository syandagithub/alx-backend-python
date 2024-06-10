#!/usr/bin/env python3
'''task1.
'''
from typing import List
from importlib import import_module as using


async_random = using('0-async_generator').async_random


async def async_comprehension() -> List[float]:
    '''Makes a list of 10 numbers.
    '''
    return [num async for num in async_generator()]
