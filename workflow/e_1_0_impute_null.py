def describe():
    return print(
        f'This module is to replace null values in the data according to whats appropriate.\n'
        f'If the data is categorical or Object or has less than the number of unique \n'
        f'values (default=10) specified by user, mode is used to replace the NA.\n'
        f'If the data is numeric (int or float) and has more than the number of\n'
        f'unique values (default = 10) specified by user, a user specified "mean" or "median" is used to replace the NA.\n'
        f'data = simple_replace_null(data, num_unique=10, mean_or_median="median") -> give data and specify number of unique values\n'
        f'null_assert(data) run this to see if there are nulls in the data'
    )

def simple_replace_null(data, num_unique=10, mean_or_median="median"):
    cols_not_filled = []
    
    reqd_columns = data.columns[data.isnull().any()].tolist()
    
    print(f"{reqd_columns} are the columns with NA values")

    for i in reqd_columns:
        n_unique = data[i].nunique()
        if n_unique <= num_unique:    # replace the categorical variable by mode
            data[i].fillna(data[i].mode()[0], inplace=True)
        if n_unique > num_unique and data[i].dtype != "O" and mean_or_median == "median":
            data[i].fillna(data[i].median(), inplace=True)
        if n_unique > num_unique and data[i].dtype != "O" and mean_or_median == "mean":
            data[i].fillna(data[i].mean(), inplace=True)
        if n_unique > num_unique and data[i].dtype == "O":
            cols_not_filled.append(i)
    print(f"{cols_not_filled} were not filled: exception - NULL categorical variable with more than {num_unique} categories")       
    return data

def null_assert(data):
    assert data.isnull().sum().sum() == 0
    return print("Asserted: No nulls in the data")
