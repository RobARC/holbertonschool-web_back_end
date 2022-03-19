#!/usr/bin/env python3
""" Module to obtain the HTML content of a particular URL and returns it."""

from functools import wraps
import redis
import requests
from typing import Callable

client = redis.Redis()


def count_request(method: Callable) -> Callable:
    """ Method decorator to count how many request has been made """

    @wraps(method)
    def wrapper(url):
        """ function wrapper """
        client.incr(f"count:{url}")
        cached_html = client.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode("utf8")

        html = method(url)
        client.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_request
def get_page(url: str) -> str:
    """ Get the html content of a web page """
    req = requests.get(url)
    return req.text
