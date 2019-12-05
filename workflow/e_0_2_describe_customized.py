import pandas as pd
def describe():
    return print(
        f'This module is to describe the data\n'
        f'describe_data(data) -> Gives pretty self explanatory result'
    )

def describe_data(data):
    desc_dict = {}
    # define dict with keys as columns
    for i in data.columns:
        desc_dict[i] = []
    # check the type for the columns
    for j in data.columns:
        num_null = data[j].isna().sum()
        count = data[j].count()
        # dtype
        desc_dict[j].append(data[j].dtype)
        # n_unique
        desc_dict[j].append(data[j].nunique())
        # number of nulls
        desc_dict[j].append(num_null)
        # percentage of nulls
        desc_dict[j].append(num_null/(num_null + count) * 100)
        # Average
        if data[j].dtype == "O":
            desc_dict[j].append("")
        else:
            desc_dict[j].append(data[j].mean())
        # median
        if data[j].dtype == "O":
            desc_dict[j].append("")
        else:
            desc_dict[j].append(data[j].median())
        # mode
        desc_dict[j].append(data[j].mode()[0])
        # standard deviation
        if data[j].dtype == "O":
            desc_dict[j].append("")
        else:
            desc_dict[j].append(data[j].std())

    index = ["dtype","nunique","num_nulls","perc_nulls",
             "mean","median","mode","std"]
    return pd.DataFrame(desc_dict, index=index)


