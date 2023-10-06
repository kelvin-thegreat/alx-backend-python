#!/usr/bin/env python3
""" Complex types - functions"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier as argument,
    returns a function that multiplies a float by multiplier.
    """
    def multiplier_function(x: float) -> float:
        """ multiplies a float by multiplier """
        return float(x * multiplier)

    return multiplier_function
