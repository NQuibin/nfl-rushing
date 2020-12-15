import re

from io import StringIO
from typing import Optional

from pymongo import ASCENDING

from .repository import PlayerStatsRepository
from .models import PaginatedData, PlayerStat
from .utils import format_lng_stat, prepare_player_stats_csv_file


class PlayerStatsManager:
    def __init__(self):
        self.repository = PlayerStatsRepository()

    def _to_model(self, stat: dict) -> PlayerStat:
        kwargs = {
            **stat,
            'id': str(stat.get('_id')),
            'lng': format_lng_stat(stat.get('lng'), stat.get('lng_is_td'))
        }
        kwargs.pop('_id', None)
        kwargs.pop('lng_is_td', None)

        return PlayerStat(**kwargs)

    def insert_many(self, player_stats: list) -> list:
        return self.repository.insert_many(player_stats)

    def find_all(
        self,
        player: Optional[str] = None,
        sort_field: Optional[str] = 'player',
        order: int = ASCENDING,
        page: int = 1,
        page_size: int = 0
    ) -> tuple:
        fields = {}
        if player:
            like_player_rgx = re.compile(f'.*{player}.*', re.IGNORECASE)
            fields = {'player': like_player_rgx}

        sort_fields = [('player', order), ('_id', order)]
        if sort_field != 'player':
            sort_fields.insert(0, (sort_field, order))

        results, total = self.repository.find_all(
            fields=fields,
            sort_fields=sort_fields,
            page=page,
            page_size=page_size
        )

        return results, total

    def find_all_paginated(
            self,
            player: Optional[str] = None,
            sort_field: Optional[str] = 'player',
            order: int = ASCENDING,
            page: int = 1,
            page_size: int = 25
    ) -> PaginatedData:
        results, total = self.find_all(
            player=player,
            sort_field=sort_field,
            order=order,
            page=page,
            page_size=page_size
        )
        return PaginatedData(
            data=[self._to_model(stat) for stat in results],
            page=page,
            page_size=len(results),
            total=total
        )

    def get_download_file_stream(
        self,
        player: Optional[str] = None,
        sort_field: Optional[str] = 'player',
        order: int = ASCENDING,
    ) -> StringIO:
        results, _ = self.find_all(
            player=player,
            sort_field=sort_field,
            order=order
        )
        return prepare_player_stats_csv_file(results)
