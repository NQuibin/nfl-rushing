from typing import List

from pymongo import MongoClient
from pymongo.collection import Collection

client = None


def get_collection() -> Collection:
    global client
    if client is None:
        client = MongoClient(f'mongodb://thescore:thescore123123@db:27017/thescore?authSource=admin')

    db = client.theScore
    return db.playerStats


class PlayerStatsRepository:
    def __init__(self):
        self.collection = get_collection()

    def find_all(self, fields: dict, sort_fields: list, page: int = 1, page_size: int = 0) -> tuple:
        doc_count = self.collection.count_documents(fields)
        docs = self.collection \
            .find(fields) \
            .sort(sort_fields) \
            .skip(page_size * (page - 1)) \
            .limit(page_size)

        return list(docs), doc_count

    def insert_many(self, player_stats: List[dict]) -> list:
        return self.collection.insert_many(player_stats)
