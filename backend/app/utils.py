def transform_stat(player_stat: dict) -> dict:
    transformed_stat = {
        'player': player_stat.get('Player'),
        'team': player_stat.get('Team'),
        'pos': player_stat.get('Pos'),
        'att': float(player_stat.get('Att')),
        'att_g': float(player_stat.get('Att/G')),
        'yds': float(str(player_stat.get('Yds')).replace(',', '')),
        'avg': float(player_stat.get('Avg')),
        'yds_g': float(player_stat.get('Yds/G')),
        'td': float(player_stat.get('TD')),
        'first': float(player_stat.get('1st')),
        'first_percentage': float(player_stat.get('1st%')),
        'twenty_plus': float(player_stat.get('20+')),
        'forty_plus': float(player_stat.get('40+')),
        'fum': float(player_stat.get('FUM'))
    }

    lng = str(player_stat.get('Lng'))
    if lng[-1] == 'T':
        transformed_stat['lng'] = float(lng[:len(lng) - 1])
        transformed_stat['lng_is_td'] = True
    else:
        transformed_stat['lng'] = float(lng)
        transformed_stat['lng_is_td'] = False

    return transformed_stat
