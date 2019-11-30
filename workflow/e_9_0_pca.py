from sklearn.decomposition import PCA
from sklearn.decomposition import FactorAnalysis
from sklearn.decomposition import IncrementalPCA
from sklearn.decomposition import KernelPCA

def describe():
    return print(
        f'This module is to find the principal components in the dataset\n'
        f'There are four different methods used\n'
        f'Specify them while passing to a function\n'
        f'It is recommended that all numerical and categorical variables be standardized before passing\n'
        f'these dimensionality reduction methods given below\n'
        f'PCA,  FactorAnalysis,  IncrementalPCA,  KernalPCA\n'
        f'dim_reduction(X_train, X_test, method = "PCA", n_components=3)\n'
    )

def dim_reduction(X_train, X_test, method = "PCA", n_components=3):
    
    dim_reduced = eval(method)(n_components = n_components)
    dim_reduced.fit(X_train)
    X_train = dim_reduced.transform(X_train)
    X_test = dim_reduced.transform(X_test)
    
    return X_train, X_test
    