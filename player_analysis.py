from api import  get_player_data, get_hero_lookup, get_win_rate


def analyze_player(player_id):
    matches  = get_player_data(player_id)
    heroes_lookup = get_hero_lookup()
    win_data = get_win_rate(player_id)
    
    wins = win_data.get("win", 0)
    losses = win_data.get("lose", 0)
    total_games = wins + losses 

    if total_games == 0:
        print("No matches found.") 
    
    winrate = (wins / total_games) * 100

    print(f"✅ Winrate: {winrate:.2f}% ({wins} Wins, {losses} Losses)") 

    if not matches :
        print("No match history found!")
        return

    print(f"\n📊 Last 10 Matches for Player {player_id} 📊\n")

    for match in matches:
        match_id = match.get('match_id', 'Unknown')
        hero_id = match.get('hero_id', 'Unknown Hero')
        hero_name = heroes_lookup.get(hero_id, 'Unknown Hero')
        kills = match.get('kills', 0)
        deaths = match.get('deaths', 0)
        assists = match.get('assists', 0)
        win = match.get('radiant_win', False) if match.get('player_slot', 0) < 128 else not match.get('radiant_win', True)

        print(f"🔹 Match {match_id}: {hero_name} | {kills}/{deaths}/{assists} | {'✅ Win' if win else '❌ Loss'}")
        