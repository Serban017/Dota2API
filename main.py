from match_analysis import analyze_match

while True:
    match_id = input("Please provide a match ID ")

    if not match_id.isdigit():
        print("Invalid match ID! Match ID should be a number.")
        continue

    analyze_match(match_id)
    break
