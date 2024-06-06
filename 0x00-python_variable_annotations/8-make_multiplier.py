#!/usr/bin/env python3
'''Task 8's module or 9. Let's duck type an iterable object
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a multiplier function.
    '''
    return lambda x: x * multiplier
