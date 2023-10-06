#!/usr/bin/env python3

""" Complex types - mixed list """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Calculate the sum of a list containing integers and floats. """
    return float(sum(mxd_lst))
