import sys
import json

from os import getcwd
from pathlib import Path

path = Path(getcwd())
sys.path.insert(0, str(path.parent.parent))

from backend.app.manager import PlayerStatsManager
from backend.app.utils import transform_stat


def insert_seed_data(file_name: str):
    with open(file_name) as json_file:
        player_stats = json.load(json_file)

    transformed_stats = []
    for stat in player_stats:
        transformed_stats.append(transform_stat(stat))

    manager = PlayerStatsManager()
    manager.insert_many(transformed_stats)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Seed file is required.')
        exit(1)

    insert_seed_data(sys.argv[1])
    print('Seed data inserted.')
