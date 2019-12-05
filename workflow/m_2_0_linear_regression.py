import pandas as pd  
from sklearn.linear_model import LinearRegression

def describe():
    
    return print(
        f'Linear Regression\n'
        f'regressor, coeff_df = linear_regression(X_train, y_train, col_order,n_jobs=4,normalize=True) if normalize = True no need to use standard scaler\n'
    )

def linear_regression(X_train, y_train, col_order,n_jobs=4, normalize=True):
    regressor = LinearRegression(normalize=normalize)  
    regressor.fit(X_train, y_train)
    coeff_df = pd.DataFrame(regressor.coef_, col_order, columns=['Coefficient'])  
    print(f'The intercept of the model is {regressor.intercept_}\n')
    
    return regressor, coeff_df