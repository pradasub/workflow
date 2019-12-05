from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor

def describe():
    return print(
        f'Basic Random forest regression and classification model\n'
        f'TODO: Random Forest Bayesian Optimization'
        f'Use random forest model only after one hot encoding\n'
        f'(and standard scaler which not completely necessary!)\n'
        f'model = basic_random_forest_classifier(\n'
        f'X_train, y_train, max_depth = 20, n_estimators=100, random_state=12, n_jobs = -1)\n'
    )

def basic_random_forest_classifier(
    X_train, y_train, max_depth = 20, n_estimators=100, random_state=12, n_jobs = -1
):
    clf_rf = RandomForestClassifier(
        n_estimators=n_estimators, random_state=random_state, 
        max_depth=max_depth, n_jobs=n_jobs)
    clf_rf.fit(X_train, y_train)   
    
    return clf_rf
         

def basic_random_forest_regressor(
    X_train, y_train, max_depth = 20,n_estimators=100, random_state=12, n_jobs = -1
):
    clf_rf = RandomForestRegressor(
        n_estimators=n_estimators, random_state=random_state, 
        max_depth=max_depth, n_jobs=n_jobs)
    clf_rf.fit(X_train, y_train)  
    
    return clf_rf
