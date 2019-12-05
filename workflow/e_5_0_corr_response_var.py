def describe():
    return print(
        f'This module is to find correlation between data and response variable.\n'
        f'This module is run only after one hot encoding is done.\n'
        f'correlation(data, response, method="pearson") ->\n' 
        f'data, response variable, ‘pearson’, ‘kendall’, ‘spearman’\n'
    )

def correlation(data, response, method='pearson'):
    
    return data.astype(float).corr(method=method)[response].abs().sort_values(ascending=False)

