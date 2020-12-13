import re

from typing import Optional

from pymongo import ASCENDING

from .repository import PlayerStatsRepository
from .models import PaginatedData, PlayerStat


class PlayerStatsManager:
    def __init__(self):
        self.repository = PlayerStatsRepository()

    def _to_model(self, stat: dict) -> PlayerStat:
        kwargs = {
            **stat,
            'id': str(stat.get('_id')),
            'lng': '{:g}T'.format(stat.get('lng')) if stat.get('lng_is_td') else stat.get('lng')
        }
        kwargs.pop('_id', None)
        kwargs.pop('lng_is_td', None)

        return PlayerStat(**kwargs)

    def find_all(
            self,
            player: Optional[str] = None,
            sort_field: Optional[str] = 'player',
            order: int = ASCENDING,
            page_num: int = 1,
            page_size: int = 25
    ) -> PaginatedData:
        fields = {}
        if player:
            like_player_rgx = re.compile(f'.*{player}.*', re.IGNORECASE)
            fields = {'player': like_player_rgx}

        sort_fields = [(sort_field, order)]
        if sort_field != 'player':
            sort_fields.append((sort_field, order))
        sort_fields.append(('player', order))
        sort_fields.append(('_id', ASCENDING))

        results, total = self.repository.find_all(
            fields=fields,
            sort_fields=sort_fields,
            page_num=page_num,
            page_size=page_size
        )
        return PaginatedData(
            data=[self._to_model(stat) for stat in results],
            page_num=page_num,
            page_size=len(results),
            total=total
        )

    def insert_many_player_stats(self, player_stats: list) -> list:
        return self.repository.insert_many(player_stats)
