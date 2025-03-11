from api import get_hero_lookup, get_match_data, get_item_lookup
from utils import convert

heroes_lookup = get_hero_lookup()

def analyze_match(match_id):
    match_data = get_match_data(match_id)
    items_lookup = get_item_lookup()

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
        last_hits = player.get("last_hits", 0)
        denies = player.get("denies", 0)
        gpm = player.get("gold_per_min", 0)
        xpm = player.get("xp_per_min", 0)
        hero_damage = player.get("hero_damage", 0)
        hero_healing = player.get("hero_healing", 0)
        net_worth = player.get("net_worth", 0)

        item_ids = [player.get(f'item_{i}', 0) for i in range(6)]
        backpack_ids = [player.get(f'backpack_{i}', 0) for i in range(3)]
        all_items = [items_lookup.get(item_id, "Unknown") for item_id in item_ids + backpack_ids]

        items_text = ", ".join(item for item in all_items if item != "Unknown")

        print(f"🔹 {player_name} | {hero_name} | {kills}K/{deaths}D/{assists}A LH/D:{last_hits}/{denies}")
        print(f"🎒 Items: {items_text}\n")

    if match_data['radiant_win']:
        print("Radiant Win ✅")
        print("Dire Loss ❌")
    else:
        print("Radiant Loss ❌")
        print("Dire Win ✅")

    print(f"Radiant Score: {match_data['radiant_score']}\n")
    print(f"Dire Score: {match_data['dire_score']}\n")

    match_duration = match_data['duration']
    print(f"The match time was: {convert(match_duration)}")
