from api import get_hero_lookup, get_match_data
from utils import convert

heroes_lookup = get_hero_lookup()

def analyze_match(match_id):
    match_data = get_match_data(match_id)

    if not match_data or "players" not in match_data:
        print("Error: Match data is incomplete or unavailable.")
        return

    print(f"Players in Match:")

    for player in match_data['players']:
        player_name = player.get('personaname', 'Anonymous Player')
        hero_id = player.get('hero_id', 'Unknown Hero')
        hero_name = heroes_lookup.get(hero_id, 'Unknown Hero')
        kills = player.get('kills', 0)
        deaths = player.get('deaths', 0)
        assists = player.get('assists', 0)
        print(f"- {player_name} {hero_name} {kills}/{deaths}/{assists}")

    print(f"Radiant Win: {match_data['radiant_win']}")
    print(f"Radiant Score: {match_data['radiant_score']} \n")

    if match_data['radiant_win'] is False:
        print(f"Dire Win: True")
    else:
        print(f"Dire Win: False")

    print(f"Dire Score: {match_data['dire_score']} \n")

    match_duration = match_data['duration']
    print(f"The match time was: {convert(match_duration)}")
