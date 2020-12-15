import csv

from typing import Union

from io import StringIO


player_stats_mapping = {
    'player': 'Player',
    'team': 'Team',
    'pos': 'Pos',
    'att': 'Att',
    'att_g': 'Att/G',
    'yds': 'Yds',
    'avg': 'Avg',
    'yds_g': 'Yds/G',
    'td': 'TD',
    'lng': 'Lng',
    'first': '1st',
    'first_percentage': '1st%',
    'twenty_plus': '20+',
    'forty_plus': '40+',
    'fum': 'FUM'
}


def format_lng_stat(lng: float, lng_is_td: bool) -> Union[float, str]:
    return '{:g}T'.format(lng) if lng_is_td else lng


def transform_stat(player_stat: dict) -> dict:
    transformed_stat = {}
    for key, value in player_stats_mapping.items():
        if key in ['player', 'team', 'pos']:
            transformed_stat[key] = player_stat.get(value)
        elif key == 'yds':
            transformed_stat['yds'] = float(str(player_stat.get('Yds')).replace(',', ''))
        elif key == 'lng':
            lng = str(player_stat.get('Lng'))
            is_td = lng[-1] == 'T'

            transformed_stat['lng'] = float(lng[:len(lng) - 1]) if is_td else float(lng)
            transformed_stat['lng_is_td'] = is_td
        else:
            transformed_stat[key] = float(player_stat.get(value))

    return transformed_stat


def prepare_player_stats_csv_file(player_stats: list) -> StringIO:
    output = StringIO()
    writer = csv.writer(output)

    headers = player_stats_mapping.values()
    writer.writerow(headers)

    for stat in player_stats:
        row = []
        for key, value in player_stats_mapping.items():
            if key == 'lng':
                row.append(format_lng_stat(stat.get('lng'), stat.get('lng_is_td')))
            elif type(stat.get(key)) is float:
                row.append('{:g}'.format(stat.get(key)))
            else:
                row.append(stat.get(key))
        writer.writerow(row)

    return output


