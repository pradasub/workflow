import pandas as pd
import numpy as np
def describe():
    return print(
        f'This module is for outlier treatment and substituting outlier with median or mean.\n'
        f'User passes the data and the number of unique numeric values (num_unique, default=50)\n'
        f'for columns desired for outlier treatment.\n'
        f'The module automatically finds numeric columns with specified number of unique_values for outlier treatment\n'
        f'TODO: Outlier treatment of categorical variables.\n'
        f'outlier_z_score(data, num_unique=50) -> gives a data frame with outlier based in z-score "z_score"\n'
        f'outlier_inter_quartile(data, num_unique=50)-> gives a data frame with outlier based in inter quartile "qtr"\n'
        f'data = fill_outliers(data,response,thres=2,num_unique=50,replace_median_or_mean="median", qtr_or_zscore="qtr")\n'
        f'-> data, response variable, thres= how many times interquartile range for example, num_unique = number of unique\n'
        f'values required for outlier treatment (default=50), replace_median_or_mean="median", qtr_or_zscore="qtr" or "z_score"\n'
    )

def cols_for_outlier_treatment(data,num_unique):
    reqd_columns = []
    for i in data.columns:
        n_unique = data[i].nunique()
        if n_unique > num_unique and data[i].dtype != "O":
            reqd_columns.append(i)
    print(f"The Columns that have outliers are {reqd_columns}")
    return reqd_columns

def outlier_z_score(data, num_unique=50):
    reqd_columns = cols_for_outlier_treatment(data,num_unique)
    z_score = {}
    index = []
    vals = [1.5,2,2.5,3,4,5]
    tot_length = len(data)
    for i in reqd_columns:
        z_score[i] = []

    for i in reqd_columns:
        std = data[i].std()
        avg = data[i].mean()
        for j in vals:
            Z_data = data[abs((data[i] - avg)/std) > j].shape[0]
            z_score[i].append(int(Z_data))
            z_score[i].append(int(Z_data/tot_length * 100))

    for i in vals:
        index.append(f"Z_score_gtr_than_{i}")
        index.append(f"Z_percentage_than_{i}")

    return pd.DataFrame(z_score, index=index)


def outlier_inter_quartile(data, num_unique=50):
    reqd_columns = cols_for_outlier_treatment(data,num_unique)
    index = []
    range_dict = {}
    vals = [1.5,2,2.5,3,4,5]
    tot_length = len(data)
    for i in reqd_columns:
        range_dict[i] = []

    for i in reqd_columns:
        for j in vals:
            q1, q3= np.percentile(data[i],[25,75])
            iqr = q3 - q1
            lower_bound = q1 -(j * iqr)
            upper_bound = q3 +(j * iqr)
            iqr_num = data[(data[i] < lower_bound) | (data[i] > upper_bound)].shape[0]
            range_dict[i].append(int(iqr_num))
            range_dict[i].append(int(iqr_num/tot_length * 100))

    for i in vals:
        index.append(f"iqr_gtr_than_{i}")
        index.append(f"iqr_percentage_than_{i}")

    return pd.DataFrame(range_dict, index=index)

def fill_outliers(data,response,thres=2,num_unique=50,replace_median_or_mean="median", qtr_or_zscore='qtr'):
    reqd_columns = cols_for_outlier_treatment(data,num_unique)
    if response in reqd_columns:
        reqd_columns.remove(response)

    for i in reqd_columns:
        if replace_median_or_mean == "mean":
            replace = data[i].mean()
        if replace_median_or_mean == "median":
            replace = data[i].median()
        if qtr_or_zscore == "z_score":
            std = data[i].std()
            avg = data[i].mean()
            data[i].values[abs((data[i] - avg)/std) > thres] = replace
        if qtr_or_zscore == "qtr":    
            q1, q3= np.percentile(data[i],[25,75])
            iqr = q3 - q1
            lower_bound = q1 -(thres * iqr) 
            upper_bound = q3 +(thres * iqr) 
            data[i].values[(data[i] < lower_bound) | (data[i] > upper_bound)] = replace 
    return data


