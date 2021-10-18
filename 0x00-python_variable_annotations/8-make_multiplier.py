#!/usr/bin/env python3
""" Write a type-annotated function make_multiplier that takes a float
    multiplier as argument and returns a function that multiplies a
    float by multiplier.
"""
from typing import Callable
from typing_extensions import runtime


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ method make_multiplier """

    def multiply(var: int):
        return var * multiplier

    return multiply
