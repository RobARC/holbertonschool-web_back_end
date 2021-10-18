#!/usr/bin/env python3
""" Annotate the below function’s parameters and return values
    with the appropriate types """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Method that recive a Iterable list and return a list with a tuple """
    return [(i, len(i)) for i in lst]
