import pandas as pd
def describe():
    return print(
        f'This module is to one hot encode the data.\n'
        f'Drop categorical variables that have more than the specified number of unique values (default =10).\n'
        f'data = one_hot_encoding(data, response, n_unique=10) -> data, response variable,drop n_unique\n'
    )
def drop_useless_categories(data,response, n_unique):
    check_columns = list(data.columns)
    check_columns.remove(response)
    for i in check_columns:
        if data[i].nunique() >= n_unique and data[i].dtype == "O":
            data.drop([i], axis = 1, inplace = True)
    used_columns = list(data.columns)
    print(f"{used_columns} are the columns that are used in the data, {response} is the target variable")
    dropped_columns = [i for i in check_columns if i not in used_columns]
    print(f"{dropped_columns} are the columns that are dropped from the data")
    return data        

def one_hot_encoding(data, response, n_unique=10):
    data = drop_useless_categories(data, response, n_unique)
    used_columns = list(data.columns)
    used_columns.remove(response)
    for i in used_columns:
        if data[i].nunique() <= n_unique:
            dums =  pd.get_dummies(data[i], drop_first=True)
            data = pd.concat([data, dums], axis = 1)
            data.drop([i], axis =1, inplace = True)
    return data
