from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
def describe():
    return print(
        f'Random forest regression and classification model\n'
        f'This module should include the most basic to the most advanced form of random forest starting with basic\n'
        f'TODO: Random Forest Grid Search'
        f'TODO: Random Forest Bayesian Optimization'
        f'TODO: Random Forest Probabilistic interpretation'
        f'Use random forest model only after one hot encoding (and standard scaler which not completely necessary!)\n'
        f'basic_random_forest_classifier(X_train, y_train, max_depth = 20, n_estimators=100, random_state=12, n_jobs = -1)\n'
    )

def basic_random_forest_classifier(X_train, y_train, max_depth = 20, n_estimators=100, random_state=12, n_jobs = -1):
    clf_rf = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state, max_depth=max_depth, n_jobs=n_jobs)
    clf_rf.fit(X_train, y_train)   
    return clf_rf
         

def basic_random_forest_regressor(X_train, y_train, max_depth = 20,n_estimators=100, random_state=12, n_jobs = -1):
    clf_rf = RandomForestRegressor(n_estimators=n_estimators, random_state=random_state, max_depth=max_depth, n_jobs=n_jobs)
    clf_rf.fit(X_train, y_train)   
    return clf_rf
