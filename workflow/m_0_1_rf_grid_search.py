from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
def describe():
    return print(
        f'Random forest model with grid search\n'
        f'TODO: Random Forest Bayesian Optimization\n'
        f'Use random forest model only after one hot encoding (and standard scaler which is not completely necessary!)\n'
        f'random_grid_search_regrssor(X_train, y_train, random_grid=default_grid_search_params(), n_iter=50, cv=3, verbose=2, random_state=42,n_jobs=-1)\n'
        f'default parameters used are listed below:'
        f'param_dict = "bootstrap": [True, False]\n'
        f'max_depth: [8, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, None],\n'
        f'max_features: ["auto", "sqrt"],\n'
        f'min_samples_leaf: [1, 2, 4],\n'
        f'min_samples_split: [2, 5, 10],\n'
        f'n_estimators: [200, 400, 600, 800, 1000]\n'
    )

def default_grid_search_params():
    param_dict = {'bootstrap': [True, False],
                  'max_depth': [8, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, None],
                  'max_features': ['auto', 'sqrt'],
                  'min_samples_leaf': [1, 2, 4],
                  'min_samples_split': [2, 5, 10],
                  'n_estimators': [200, 400, 600, 800, 1000]}
    return param_dict

def random_grid_search_classification(X_train, y_train, random_grid=default_grid_search_params(), n_iter=50, cv=3, verbose=2, random_state=42,n_jobs=-1):
    rf = RandomForestClassifier()
    rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = n_iter, cv = cv, verbose=verbose, random_state=random_state, n_jobs = n_jobs)
    rf_random.fit(X_train, y_train)
    return rf_random

def random_grid_search_regressor(X_train, y_train, random_grid=default_grid_search_params(), n_iter=50, cv=3, verbose=2, random_state=42,n_jobs=-1):
    rf = RandomForestRegressor()
    rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = n_iter, cv = cv, verbose=verbose, random_state=random_state, n_jobs = n_jobs)
    rf_random.fit(X_train, y_train)
    return rf_random






