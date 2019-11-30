def describe():
    return print(
        f'This module is to check if some variables are highly correlated\n'
        f'Gives correlation between all the variables within a dataframe\n'
        f'correlated_vars(df,corr_value=0.8,frac = 1,corr_method="pearson")\n'
        f'frac = 1, just means what fraction of the sample do you want to use\n'
        
    )

def correlated_vars(df,corr_value=0.8,frac = 1,corr_method="pearson"):

    list_cols = list(df.columns)
    df = df.sample(frac=frac)
    correlated_columns = {}
    for i in list_cols:
        correlated_columns[i] = [] 
    for i in df.columns:
        for j in list_cols:
            if (i != j) and (df[i].corr(df[j], method=corr_method)) > corr_value:
                correlated_columns[i].append(j)
        list_cols.remove(i)
        
    return correlated_columns