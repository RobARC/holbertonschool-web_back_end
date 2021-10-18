#!/usr/bin/env python3
""" Write a type-annotated function to_kv that takes a string k and an int
    OR float v as arguments and returns a tuple. The first element of the
    tuple is the string k. The second element is the square of the
    int/float v and should be annotated as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Method to_kv receive two parameters a str and other that could
        be a int or float, return a tuple wich first argument is a str
        a the second is a square of v type float
    """

    return (k, v*v)
