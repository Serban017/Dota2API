import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from match_analysis import get_match_data
from pandas import json_normalize

st.title("Dota 2 Match Tracker")

account_id = st.text_input("Enter Dota 2 Account ID:", "")
if account_id:
    st.write(f"Fetching last 20 matches for player `{account_id}`...")
    matches = get_match_data(account_id)

    if matches:

        df = json_normalize(matches)

        # Display table
        st.subheader("Recent Matches")
        st.dataframe(df[["match_id", "kills", "deaths", "assists", "hero_id", "radiant_win"]])

        # Win/Loss Chart
        st.subheader("Win/Loss Chart")
        win_count = sum([(m['radiant_win'] and m['player_slot'] < 128) or
                         (not m['radiant_win'] and m['player_slot'] >= 128) for m in matches])
        loss_count = len(matches) - win_count

        fig, ax = plt.subplots()
        ax.pie([win_count, loss_count], labels=["Wins", "Losses"], autopct='%1.1f%%', startangle=90)
        ax.axis("equal")
        st.pyplot(fig)
    else:
        st.error("No matches found or invalid account ID.")
