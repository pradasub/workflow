from sklearn.svm import SVC 
from sklearn.model_selection import GridSearchCV

def describe():
    
    return print(
        f'Support Vector Machines Algorithm\n'
        f'model = svm(X_train, y_train) -> simple svm with no grid search\n'
        f'model = svm_grid_search(X_train, y_train, param=default_grid_search_params(), verbose=3)\n'
        f'svm with default grid search, change grid search as desired\n'
    )

def default_grid_search_params():
    param_dict = {'C': [0.1, 1,1,10,100,1000],
                  'gamma': [1,0.1,0.01,0.001,0.0001]}
    
    return param_dict

def svm(X_train, y_train):
    model = SVC()
    model.fit(X_train, y_train)
    
    return model

def svm_grid_search(
    X_train, y_train, param=default_grid_search_params(), verbose=3
):
    grid = GridSearchCV(SVC(), param, verbose=3)
    grid.fit(X_train, y_train)
    
    return grid

