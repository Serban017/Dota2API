from api import  (get_player_data,
                  get_hero_lookup,
                  get_win_rate,
                  get_player_rank_data)

from match_analysis import get_match_data

RANK_NAMES = {
    1: "Herald", 2: "Guardian", 3: "Crusader",
    4: "Archon", 5: "Legend", 6: "Ancient",
    7: "Divine", 8: "Immortal"
}

def analyze_player(player_id):
    matches = get_player_data(player_id)
    heroes_lookup = get_hero_lookup()
    win_data = get_win_rate(player_id)
    rank_data = get_player_rank_data(player_id)

    if not rank_data:
        print("No rank data found!")
        return

    rank_tier = rank_data.get("rank_tier", "Unknown")
    mmr = rank_data.get("competitive_mmr")
    leaderboard_rank = rank_data.get("leaderboard_rank", "Not in top 1000")

    if isinstance(rank_tier, int):
        medal = rank_tier // 10  # First digit = medal
        star = rank_tier % 10  # Second digit = star

        rank_name = RANK_NAMES.get(medal, "Unknown")
        rank_display = f"{rank_name} {star}" if rank_name != "Immortal" else "Immortal"
    else:
        rank_display = "Unknown Rank"

    print(f"🏆 Rank: {rank_display} | 🎯 MMR: {mmr} | 📊 Leaderboard: {leaderboard_rank}")

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

