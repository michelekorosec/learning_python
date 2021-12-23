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

#basics()
#basic_stats()
