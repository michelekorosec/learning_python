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

def series_objects():
    revenues = pd.Series([5555,7000,1980])
    '''print(revenues)
    print(revenues.values)
    print(revenues.index)
    print(type(revenues.values))'''

    city_revenues = pd.Series([4200,8000,6500],index=["Amsterdam","Toronto","Tokyo"])
    #print(city_revenues)

    city_employee_count = pd.Series({"Amsterdam":5,"Tokyo":8})
    '''print(city_employee_count)
    print(city_employee_count.keys())
    print("Tokyo" in city_employee_count)
    print("Munich" in city_employee_count)'''

    return city_revenues,city_employee_count

def dataframe_objects(city_revenues,city_employee_count):

    city_data = pd.DataFrame({"revenue":  city_revenues,"employee_count": city_employee_count})
    '''print(city_data)
    print(city_data.index)
    print(city_data.values)

    print(city_data.axes)
    print(city_data.axes[0])
    print(city_data.axes[1])

    print(city_data.keys())
    print("Amsterdam" in city_data)
    print("revenue" in city_data)

    print(nba.axes)
    print("points" in nba)
    print("pts" in nba)'''

    return city_data

def accessing_series_elements(city_revenues):

    print(city_revenues["Toronto"])
    print(city_revenues[1])

    print(city_revenues[-1])
    print(city_revenues[1:])
    print(city_revenues["Toronto":])

    colors = pd.Series(["red","purple","blue","green","yellow"],index=[1,2,3,5,8])
    print(colors)
    print(colors.loc[1]) #label index
    print(colors.iloc[1]) #positional index

    print(colors.iloc[1:3])

    return 0

def accessing_dataframe_elements(city_data):

    print(city_data)
    print(city_data["revenue"])
    print(type(city_data["revenue"]))
    print(city_data.revenue)

    toys = pd.DataFrame([
        {"name":"ball","shape":"sphere"},
        {"name":"Rubik's cube","shape":"cube"}
    ])
    print(toys["shape"])
    print(toys.shape)

    print(city_data.loc["Amsterdam"])
    print(city_data.loc["Tokyo":"Toronto"])
    print(city_data.iloc[1])

    print(nba.iloc[-2])

    print(city_data.loc["Amsterdam":"Tokyo","revenue"])

    print(nba.info)
    print(nba.loc[5555:5559,["fran_id","opp_fran","pts","opp_pts"]])



    return 0

#basics()
#basic_stats()
#exploratory_data_analysis()
#series_objects()
#dataframe_objects(series_objects()[0],series_objects()[1])
#accessing_series_elements(series_objects()[0])
accessing_dataframe_elements(dataframe_objects(series_objects()[0],series_objects()[1]))