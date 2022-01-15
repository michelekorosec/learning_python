import pandas as pd
import numpy as np

pd.set_option("display.max.columns",None)
pd.set_option("display.precision",2)

nba = pd.read_csv("nba_all_elo.csv")

def basics():
    print(type(nba))
    print(len(nba))
    print(nba.shape)

    print(nba.head())
    print(nba.tail(3))

    return 0

def basic_stats():
    print(nba.info())
    print(nba.describe())
    print(nba.describe(include=object))

    return 0

def exploratory_data_analysis():
    print(nba["team_id"].value_counts())
    print(nba["fran_id"].value_counts())
    print(nba.loc[nba["fran_id"] == "Lakers","team_id"].value_counts())

    nba["date_played"] =  pd.to_datetime(nba["date_game"])
    print(nba.loc[nba["team_id"] == "MNL", "date_played"].min())
    print(nba.loc[nba["team_id"] == "MNL", "date_played"].max())
    print(nba.loc[nba["team_id"] == "MNL", "date_played"].agg(("min","max")))

    print(nba.info())
    print(nba.loc[nba["team_id"] == "BOS", "pts"].agg(("sum"))) # Suggested solution: nba.loc[nba["team_id"] == "BOS", "pts"].sum()

    return 0

#basics()
#basic_stats()
exploratory_data_analysis()
