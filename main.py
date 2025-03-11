from match_analysis import analyze_match
from  player_analysis import analyze_player

def show_menu():
    """Display the main menu to the user."""
    print("\n🎮 Dota 2 Match Analyzer 🎮")
    print("1. Analyze a Match")
    print("2. Analyze a Player")
    print("3. Exit")
    return input("Select an option: ")


def main():
    while True:
        choice = show_menu()

        if choice == "1":
            match_id = input("Enter Match ID: ")
            if not match_id.isdigit():
                print("❌ Invalid input! Match ID should be a number.")
                continue
            analyze_match(match_id)

        elif choice == "2":
            player_id = input("Enter player ID (Steam ID): \n ")
            if not player_id.isdigit():
                print("❌ Invalid input! Player ID should be a number.")
                continue
            analyze_player(player_id)

        else:
            print("❌ Invalid choice! Please select 1 or 2.")


if __name__ == "__main__":
    main()