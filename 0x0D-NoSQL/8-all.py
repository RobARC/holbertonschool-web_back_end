#!/usr/bin/env python3
"""Module Pymongo"""


def list_all(mongo_collection: object) -> list:
    """ Function that lists all documents in a collection"""

    if mongo_collection.find({}):
        return mongo_collection.find({})
    else:
        []
