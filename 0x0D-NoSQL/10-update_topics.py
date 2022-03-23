#!/usr/bin/env python3
""" Update topics """


from typing import List


def update_topics(mongo_collection: object, name: str, topics: List[str]):
    """function that changes all topics of a school document based on the name"""

    data = mongo_collection.update_many(
                {"name": name}, 
                {"$set": "topics": topics}}
                )
    return data.modified_count