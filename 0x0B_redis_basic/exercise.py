#!/usr/bin/env python3
""" Redis and Python exercise """
import redis
import uuid
from functools import wraps
from typing import Callable, Union

class Cache():
    """Redis´s  Class Cache"""

    def __init__(self) -> None:
        self._redis =redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store method 
            Args: data(Union[str, bytes, int, float]): Data to be store
            Returns: str: string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key