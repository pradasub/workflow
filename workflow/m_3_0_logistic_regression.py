import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

def describe():
    return print(
        f'Logistic Regression\n'
        f'solver : "newton-cg", "lbfgs", "liblinear", "sag", "saga"\n'
        f'model, coeff_df = logistic_regression(X_train, y_train, col_order,random_state=99,solver="lbfgs",n_jobs=4)\n'
        f'logistic_metrics(model,X_test, y_test) get intercept and r2 for the model'
    )

def logistic_regression(X_train, y_train, col_order,random_state=99,solver="lbfgs",n_jobs=4):
    logreg = LogisticRegression()
    logreg.fit(X_train,y_train) 
    coeff_df = pd.DataFrame(np.concatenate(logreg.coef_), col_order, columns=['Coefficient'])
    
    return logreg, coeff_df

def logistic_metrics(model,X_test, y_test):
    return print(
        f'Intercept of the model is {model.intercept_[0]}\n'
        f'r2 of the model is {model.score(X_test, y_test)}\n'
    )