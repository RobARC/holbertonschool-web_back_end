#!/usr/bin/env python3
""" Redis and Python exercise """

import redis
import uuid
from functools import wraps
from typing import Callable, Union


class Cache():
    """Redis´s  Class Cache"""

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store method
            Args: data(Union[str, bytes, int, float]): Data to be store
            Returns: str: string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get (self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """ Get data from redis and transform it to its python type """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ Method get_str transform a redis type varible to str python type """
        Myvar = self._redis.get(key)
        return Myvar.decode('utf8')

    def get_int(self, key: str) -> int:
        """ Method get_int transform a redis type varible to int python type """
        Myvar = self._redis.get(key)
        try:
            Myvar = int(Myvar.decode('utf8'))
        except Exception:
            Myvar = 0
        return Myvar
    
