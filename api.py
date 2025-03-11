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

def get_player_data(player_id):
    url = f"https://api.opendota.com/api/players/{player_id}/recentMatches"
    response = requests.get(url)

    if response.status_code != 200:
        print("No match history found.")
        return []

    return response.json()[:10]

def get_win_rate(player_id):

    url = f"https://api.opendota.com/api/players/{player_id}/wl"
    response = requests.get(url)

    if response.status_code !=200: 
        print("❌ Error fetching win rate data.")
        return []
    
    return response.json()

def get_player_rank_data(player_id):
    url = f"https://api.opendota.com/api/players/{player_id}"
    response = requests.get(url)


    if response.status_code != 200:
        print("❌ Error fetching player rank data.")
        return None

    return response.json()

def get_item_lookup():
    items_url = "https://api.opendota.com/api/constants/items"
    response = requests.get(items_url)

    if response.status_code != 200:
        print("❌ Error fetching item data.")
        return {}

    items_data = response.json()
    return {details["id"]: name.replace("_", " ").title() for name, details in items_data.items()}