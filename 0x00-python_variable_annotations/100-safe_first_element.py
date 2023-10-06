#!/usr/bin/env python3
""" Duck typing 2 a sequence """
from typing import Any, Union, Sequence, Iterable, List, Tuple


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Safely retrieve the first element from a sequence, or None if the sequence is empty. 
    """
    if lst:
        return lst[0]
    else:
        return None
