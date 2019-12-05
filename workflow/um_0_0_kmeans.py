from sklearn.cluster import KMeans

def describe():
    
    return print(
        f'Kmeans clustering algorithm\n'
        f'kmeans.cluster_centers_, kmeans_labels = \n'
        f'k_means(data, n_cluster=4) -> Give the data and find the number of cluster\n'
        f'TODO: The algorithm needs to be significantly improved\n'
    )

def k_means(data, n_cluster=4):
    kmeans = KMeans(n_cluster=n_cluster)
    kmeans.fit(data)
    
    return kmeans.cluster_centers_, kmeans_labels

