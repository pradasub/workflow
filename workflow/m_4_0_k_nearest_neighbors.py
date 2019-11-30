from sklearn.neighbors import KNeighborsClassifier 

def describe():
    return print(
        f'K-nearest neighbor algorithm\n'
        f'knn = nearest_neighbour(X_train, y_train,n_neighbors=4, n_jobs=-1) -> return knn model'
    )

def nearest_neighbour(X_train, y_train,n_neighbors=4, n_jobs=-1):
    knn = KNeighborsClassifier(n_neighbors=n_neighbors, n_jobs=n_jobs) 
    knn.fit(X_train, y_train)
    
    return knn