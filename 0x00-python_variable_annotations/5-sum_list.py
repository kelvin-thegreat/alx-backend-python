#!/usr/bin/env python3
""" type-annotated function sum_list which takes a list input_list """
from typing import Callable, Iterator, Union, Optional, List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list input_list of floats as argument returns their sum as a float.
    """

    return sum(input_list)
