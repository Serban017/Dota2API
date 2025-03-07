import requests

heroes_url = "https://api.opendota.com/api/heroes"
heroes_response = requests.get(heroes_url)
heroes_data = heroes_response.json()

heroes_lookup = {hero["id"]: hero["localized_name"] for hero in heroes_data}

while True:

    match_id = input("Please provide a match ID ")

    if not match_id.isdigit():
        print("Invalid match ID! Match ID should be a number.")
        continue

    url = f"https://api.opendota.com/api/matches/{match_id}"

    response = requests.get(url)

    if response.status_code == 404:
        print("Invalid match ID! Match not found.")
        continue

    match_data = response.json()

    if "players" not in match_data:
        print("Error: Match data is incomplete or unavailable.")
        continue

    print("Valid match ID! Processing data...")
    break


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


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
     
    return "%d:%02d:%02d" % (hour, minutes, seconds)

match_duration = match_data['duration']
print(f"The match time was: {convert(match_duration)}")