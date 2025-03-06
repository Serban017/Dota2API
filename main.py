import requests

match_id = 8202861452  # Example match ID
url = f"https://api.opendota.com/api/matches/{match_id}"

response = requests.get(url)
match_data = response.json()

print(f"Players in Match:")

for player in match_data['players']: 
    print(f"- {player['personaname']} ({player['hero_id']})")

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