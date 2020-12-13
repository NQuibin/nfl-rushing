from typing import List

from pymongo import MongoClient
from pymongo.collection import Collection

client = None


def get_collection() -> Collection:
    global client
    if client is None:
        client = MongoClient(f'mongodb://thescore:thescore123123@localhost:27017/thescore?authSource=admin')
    db = client.theScore
    return db.playerStats


class PlayerStatsRepository:
    def __init__(self):
        self.collection = get_collection()

    def find_all(self, fields: dict, sort_fields: list, page_num: int = 1, page_size: int = 25):
        return list(
            self.collection
                .find(fields)
                .sort(sort_fields)
                .skip(page_size * (page_num - 1))
                .limit(page_size)
        )

    def insert_many(self, player_stats: List[dict]) -> List:
        return self.collection.insert_many(player_stats)
