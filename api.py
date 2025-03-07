import requests

def get_hero_lookup():
    heroes_url = "https://api.opendota.com/api/heroes"
    heroes_response = requests.get(heroes_url)
    heroes_data = heroes_response.json()
    return {hero["id"]: hero["localized_name"] for hero in heroes_data}

def get_match_data(match_id):
    url = f"https://api.opendota.com/api/matches/{match_id}"
    response = requests.get(url)

    if response.status_code == 404:
        return None

    return response.json()
