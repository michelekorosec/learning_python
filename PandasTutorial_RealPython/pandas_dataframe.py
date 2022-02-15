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

def data_types():

    #print(df.dtypes)
    df_ = df.astype(dtype={'age': np.int32, 'py-score': np.float32})
    #print(df_.dtypes)

    return df_

def dataframe_size(df_=data_types()):

    print(df_.ndim)
    print(df_.shape)
    print(df_.size)
    print(df_.memory_usage())

    return 0

def accessing_modifying_data():

    print(df['name'])
    print(df.loc[10])
    print(df.iloc[0])
    print(df.loc[:,'city'])
    print(df.iloc[:,1])
    print(df.loc[11:15,['name','city']]) #start and stop index inclusive
    print(df.iloc[1:6,[0,1]]) #stop index exclusive
    print(df.iloc[1:6:2,0])
    print(df.iloc[slice(1,6,2),0])
    print(df.iloc[np.s_[1:6:2],0])
    print(df.iloc[pd.IndexSlice[1:6:2], 0])
    print(df.at[12,'name'])
    print(df.iat[2,0])

    return 0

def setting_data_w_accessors():

    print(df.loc[:,'py-score'])

    df.loc[:13,'py-score'] = [40,50,60,70]
    df.loc[14:,'py-score'] = 0
    print(df.loc[:, 'py-score'])

    df.iloc[:, -1] = np.array([88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0])
    print(df['py-score'])

    return 0

def inserting_deleting_data():

    global df

    john = pd.Series(data=['John','Boston',34,79], index=df.columns, name=17)
    #print(john)
    #print(john.name)

    df_ = df.append(john)
    #print(df_)

    df_ = df_.drop(labels=[17])
    #print(df_)

    df['js-score'] = np.array([71.0, 95.0, 88.0, 79.0, 91.0, 91.0, 80.0])
    #print(df)

    df['total-score'] = 0.0
    #print(df)

    df.insert(loc=4, column='django-score', value=np.array([86.0, 81.0, 78.0, 88.0, 74.0, 70.0, 81.0]))
    #print(df)

    del df['total-score']
    #print(df)

    df_ = df.drop(labels='age',axis=1)
    #print(df_)

    return 0


#introducing_dataframes()
#creating_dataframes()
#dataframes_with_lists()
#dataframes_with_np_arrays()
#dataframes_from_files()
#labels_as_sequences()
#dataframe_to_np()
df.index = np.arange(10, 17) #put this here to make the change without calling the function
#data_types()
#dataframe_size()
#accessing_modifying_data()
#setting_data_w_accessors()
inserting_deleting_data()
print(df)