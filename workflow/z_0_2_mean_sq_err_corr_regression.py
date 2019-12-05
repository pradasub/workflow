import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics  

def describe():
    
    return print(
        f'This module will give a evaluation metrics for regression problem\n'
        f'correlation, mean_absolute_error, mean_squared_error, mean_squared_log_error\n'
        f'also use the module for correlation plot\n'
        f'prediction_metrics(y_test, y_pred) will give data frame with all prediction metrics\n'
        f'prediction_metrics(y_test, y_pred) plots actual vs predicted\n'
    )

def prediction_metrics(y_test, y_pred):
    
    if y_pred.ndim==2:
        y_pred = np.concatenate(y_pred)
        
    all_metrics = []
    all_metrics.append(metrics.mean_squared_log_error(y_test, y_pred))
    all_metrics.append(metrics.mean_absolute_error(y_test, y_pred))
    all_metrics.append(metrics.mean_squared_error(y_test, y_pred))
    all_metrics.append(metrics.median_absolute_error(y_test, y_pred))
    all_metrics.append(metrics.r2_score(y_test, y_pred))
    all_metrics.append(metrics.explained_variance_score(y_test, y_pred))
    all_metrics.append(metrics.max_error(y_test, y_pred))
    y_test = pd.Series(y_test).reset_index(drop=True)
    y_pred = pd.Series(y_pred).reset_index(drop=True)
    all_metrics.append(y_test.corr(y_pred, method='pearson'))
    all_metrics.append(y_test.corr(y_pred, method='spearman'))
    all_metrics.append(y_test.corr(y_pred, method='kendall'))
    
    index = ['mean_squared_log_error', 'metrics.mean_absolute_error', 'mean_squared_error',
            'median_absolute_error', 'r2_score', 'explained_variance_score', 'max_error',
            'pearson_correlation', 'spearman_correlation', 'kendall_correlation']
    
    return pd.DataFrame({'Values':all_metrics}, index=index)

def corr_polt(y_test, y_pred):
    
    fig, ax = plt.subplots()
    ax.plot(y_test, y_pred, 'o', mfc = 'none')
    ax.plot([y_test.min(), y_pred.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
    ax.set_xlabel('Actual')
    ax.set_ylabel('Predicted')
    
    return plt.show()



