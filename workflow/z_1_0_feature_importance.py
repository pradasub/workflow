import pandas as pd
def describe():
    return print(
        f'This module is to plot the feature importance of variables after random forest model\n'
        f'pass in the model used, order of the column\n'
        f'feature_importance_plot(model,col_order, n_top_features) -> n_top_features is the number of top features wanted\n'
    )

def feature_importance_plot(model,col_order, n_top_features):
    imp = model.feature_importances_
    feat_imp = pd.DataFrame(imp, col_order, columns=['Importance of Features'])
    feat_imp = feat_imp.sort_values(by=['Importance of Features'], ascending=False)
    feat_imp_frac = feat_imp.head(n_top_features)
    return feat_imp_frac.plot.barh()