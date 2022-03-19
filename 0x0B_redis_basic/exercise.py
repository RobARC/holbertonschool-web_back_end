#!/usr/bin/env python3
""" Redis and Python exercise """

import redis
import uuid
from functools import wraps
from typing import Callable, Union


def count_calls(method: Callable) -> Callable:
    """ Method to count calls decorator that takes
    method Callable as single argument and returns
    a Callable """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Method wrapper increment the count for
        that key every time the method is called and
        returns the value returned by the original method."""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Method call_history store the history of inputs and outputs
    for a particular function"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Method wrapper save the inputs and output"""
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        output = method(self, *args, **kwargs)

        self._redis.rpush(input_key, str(args))
        self._redis.rpush(output_key, str(output))

        return output

    return wrapper


def replay(fn: Callable):
    """Method replay display the history of calls of a
    particular function"""

    r = redis.Redis()
    f_name = fn.__qualname__
    n_calls = r.get(f_name)
    try:
        n_calls = n_calls.decode('utf-8')
    except Exception:
        n_calls = 0
    print(f'{f_name} was called {n_calls} times:')

    ins = r.lrange(f_name + ':inputs', 0, -1)
    outs = r.lrange(f_name + ':outputs', 0, -1)

    for i, o in zip(ins, outs):
        try:
            i = i.decode('utf-8')
        except Exception:
            i = ''
        try:
            o = o.decode('utf-8')
        except Exception:
            o = ''

        print(f'{f_name}(*{i} -> {o}')


class Cache():
    """Redis´s  Class Cache"""

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store method
            Args: data(Union[str, bytes, int, float]): Data to be store
            Returns: str: string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) \
            -> Union[str, bytes, int, float]:
        """ Get data from redis and transform it to its python type """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ Method get_str transform a redis type varible
            to str python type """
        Myvar = self._redis.get(key)
        return Myvar.decode('utf8')

    def get_int(self, key: str) -> int:
        """ Method get_int transform a redis type varible
             to int python type """
        Myvar = self._redis.get(key)
        try:
            Myvar = int(Myvar.decode('utf8'))
        except Exception:
            Myvar = 0
        return Myvar
