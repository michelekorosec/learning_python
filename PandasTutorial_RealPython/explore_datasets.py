import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

def querying_dataset():

    current_decade = nba[nba.year_id  > 2010]
    print(current_decade.shape)

    games_with_notes = nba[nba.notes.notnull()]
    print(games_with_notes.shape)

    ers = nba[nba.fran_id.str.endswith("ers")]
    print(ers.shape)

    baltimore = nba[(nba["_iscopy"] == 0) & (nba.pts > 100) & (nba.opp_pts > 100) & (nba.team_id == "BLB")]
    print(baltimore)

    la = nba[(nba._iscopy == 0) & (nba.team_id.str.contains("LA")) & (nba.notes.str.contains("at"))  & (nba.year_id == 1992)] #example solution: nba[(nba["_iscopy"] == 0) & (nba["team_id"].str.startswith("LA")) & (nba["year_id"]==1992) & (nba["notes"].notnull())]
    print(la)

    return 0

def grouping_aggregating(city_revenues):

    print(city_revenues.sum())
    print(city_revenues.max())

    points = nba.pts
    print(type(points))
    print(points.sum())

    print(nba.groupby("fran_id",sort=False)["pts"].sum())

    print(nba[(nba.fran_id == "Spurs") & (nba.year_id > 2010)].groupby(["year_id","game_result"])["game_id"].count())

    nba.info()

    warriors = nba[(nba.team_id == "GSW") & (nba.year_id == 2015)].groupby(["is_playoffs","game_result"])["game_id"].count()
    print(warriors)

    return 0


def manipulating_columns():

    df = nba.copy()
    print(df.shape)

    df["difference"] = df.pts-df.opp_pts
    print(df.shape)
    print(df.difference.max())

    renamed_df =df.rename(columns={"game_result":"result","game_location":"location"})
    renamed_df.info()

    elo_columns = ["elo_i","elo_n","opp_elo_i","opp_elo_n"]
    df.drop(elo_columns,inplace=True,axis=1)
    print(df.shape)

    return df

def specifying_datatypes(df):

    df.info()
    df["date_game"] = pd.to_datetime(df["date_game"])
    df.info()

    print(df["game_location"].nunique())
    print(df.game_location.value_counts())
    df["game_location"] = pd.Categorical(df["game_location"])
    print(df.game_location.dtype)

    df.info() #decreased memory usage due to categorial type

    print(df.game_result.nunique())
    df.game_result = pd.Categorical(df.game_result)
    print(df.game_result)
    df.info()

    return 0

def missing_values():

    rows_without_missing_data = nba.dropna()
    print(rows_without_missing_data.shape)

    data_without_missing_columns = nba.dropna(axis=1)
    print(data_without_missing_columns.shape)

    data_w_default_notes = nba.copy()
    data_w_default_notes.notes.fillna(value="no notes at all", inplace=True)
    print(data_w_default_notes.notes.describe())

    return 0

def invalid_values():

    print(nba[nba.pts == 0])

    return 0

def inconsistent_values():

    print(nba[(nba.pts > nba.opp_pts) & (nba.game_result != 'W')].empty)
    print(nba[(nba.pts < nba.opp_pts) & (nba.game_result != 'L')].empty)

    return 0

def combining_multiple_datasets(city_data = dataframe_objects(series_objects()[0],series_objects()[1])):

    further_city_data = pd.DataFrame(
        {"revenue": [7000,3400], "employee_count":[2,2]},
        index=["New York","Barcelona"])

    print(further_city_data)

    all_city_data = pd.concat([city_data, further_city_data], sort=False)
    print(all_city_data)

    city_countries = pd.DataFrame({
        "country": ["Holland","Japan","Holland","Canada","Spain"],
        "capital": [1,1,0,0,0]},
        index=["Amsterdam","Tokyo","Rotterdam","Toronto","Barcelona"]
    )

    cities = pd.concat([all_city_data,city_countries],axis=1,sort=False)
    print(cities)

    countries = pd.DataFrame({
        "population_millions": [17,127,37],
        "continent": ["Europe","Asia","North America"]},
        index= ["Holland","Japan","Canada"]
    )

    all = pd.merge(cities,countries, left_on="country",right_index=True,how="left")
    print(all)


    return 0

def visualization():

    nba[nba.fran_id == "Knicks"].groupby("year_id")["pts"].sum().plot()
    plt.show()
    nba.fran_id.value_counts().head(10).plot(kind="bar")
    plt.show()
    nba[(nba.fran_id == "Heat") & (nba.year_id == 2013)]["game_result"].value_counts().plot(kind="pie")
    plt.show()
    return 0

#basics()
#basic_stats()
#exploratory_data_analysis()
nba["date_played"] =  pd.to_datetime(nba["date_game"]) #placed here to give same results for next tasks
#series_objects()
#dataframe_objects(series_objects()[0],series_objects()[1])
#accessing_series_elements(series_objects()[0])
#accessing_dataframe_elements(dataframe_objects(series_objects()[0],series_objects()[1]))
#querying_dataset()
#grouping_aggregating(series_objects()[0])
#manipulating_columns()
#specifying_datatypes(manipulating_columns())
#missing_values()
#invalid_values()
#inconsistent_values()
#combining_multiple_datasets()
#visualization()