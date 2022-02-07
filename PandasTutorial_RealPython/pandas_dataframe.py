import pandas as pd
import numpy as np

data = {
    'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
    'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai', 'Manchester', 'Cairo', 'Osaka'],
    'age': [41, 28, 33, 34, 38, 31, 37],
    'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
}

row_labels = [101, 102, 103, 104, 105, 106, 107]

df = pd.DataFrame(data=data, index=row_labels)

def introducing_dataframes():
    print(df)
    print(df.head(n=2))
    print(df.tail(n=2))

    cities = df['city']
    print(cities)

    print(df.city)
    print(cities[102])

    print(df.loc[103])

    return 0

def creating_dataframes():

    d = {'x': [1, 2, 3], 'y': np.array([2, 4, 8]), 'z': 100}
    print(pd.DataFrame(d))
    print(pd.DataFrame(d,index=[100,200,300],columns=['z','y','x']))


    return 0

def dataframes_with_lists():
    l = [{'x': 1, 'y': 2, 'z': 100},
         {'x': 2, 'y': 4, 'z': 100},
         {'x': 3, 'y': 8, 'z': 100}]

    print(pd.DataFrame(l))

    list = [[1, 2, 100],
         [2, 4, 100],
         [3, 8, 100]]

    print(pd.DataFrame(list, columns=['x','y','z']))

    return 0

def dataframes_with_np_arrays():
    arr = np.array([[1, 2, 100],
                    [2, 4, 100],
                    [3, 8, 100]])

    df_ = pd.DataFrame(arr, columns=['x','y','z'])
    print(df_)

    arr[0,0] = 1000
    print(df_) #because default copy=False in DataFrame constructor; saves time and processing power

    return 0

def dataframes_from_files():

    df.to_csv('data.csv')
    print(pd.read_csv('data.csv', index_col=0))

    return 0

def labels_as_sequences():

    print(df.index)
    print(df.columns)
    print(df.columns[1])

    df.index = np.arange(10,17)
    print(df.index)
    print(df)


    return 0

def dataframe_to_np():

    print(df.to_numpy()) #suggested version because of optional parameters dtype and copy
    print(df.values) #older/more widely used

    return 0



#introducing_dataframes()
#creating_dataframes()
#dataframes_with_lists()
#dataframes_with_np_arrays()
#dataframes_from_files()
#labels_as_sequences()
#dataframe_to_np()