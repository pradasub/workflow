def describe():
    return print(
        f'This module is to flag dataset if:\n'
        f'it has greater than user defined percentage of null values\n'
        f'any categorical variable is highly biased, with number of unique value in that category\n'
        f'flag if a variable has only one unique value\n'
        f'maj_null, bias_n_unique = flag_vars(df,n_unique_for_bias_check=10,frac = 1,perc_null_gtr = 50.)\n'
        f'maj_null gives column with mostly null values\n'
        f'bias_n_unique gives columns that are highly biased- [biased value, biased percentage, n_unique]'
    )



def flag_vars(df,bias_ratio = 0.9,frac=1,perc_null_gtr = 50.,n_unique_for_bias_check=10):
    
    list_cols = list(df.columns)
    df = df.sample(frac=frac)
    
    maj_null = []
    for i in list_cols:
        perc_null = df[i].isna().sum()/df.shape[0] * 100
        if perc_null > perc_null_gtr:
            maj_null.append(i)

    bias_n_unique = {}
    for i in list_cols:
        if df[i].nunique() <= n_unique_for_bias_check:
            value_count = df[i].value_counts()
            biasness = value_count.values[0]/value_count.sum()
            if biasness>bias_ratio:
                n_unique=df[i].nunique()
                bias_n_unique[i] = []
                bias_n_unique[i].append(value_count.index[0])
                bias_n_unique[i].append(biasness)
                bias_n_unique[i].append(n_unique)
                if n_unique==1:
                    print(f'FLAG, column: {i} has only one unique value-cannot be used for modeling')      

    
    return maj_null, bias_n_unique
        
        
            
        


