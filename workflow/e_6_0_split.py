from sklearn.model_selection import train_test_split
def describe():
    return print(
        f'This module is to split the data set into train and test set\n'
        f'random_split is to split the data randomly into a train and test set\n'
        f'sequentil_split is to split the data sequentially into a train and test set\n'
        f'TODO:research other ways train test split can be achieved\n'
        f'X_train, X_test, y_train, y_test = random_split(data, response, test_size = 0.2, random_state=99)\n'
        f'X_train, X_test, y_train, y_test = sequential_split(data, response, test_size = 0.2)\n'
    )

def random_split(data, response, test_size=0.2, random_state=99):
    X = data.drop([response], axis = 1).copy()
    y = data[response].copy()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test 

def sequential_split(data, response, test_size=0.2):
    train_shape = int((1-test_size)*data.shape[0])
    test_shape = data.shape[0] - train_shape
    
    X_train = data[:train_shape].copy()
    y_train = X_train[response].copy()
    X_train.drop([response], axis=1, inplace = True)
    
    X_test = data[-(test_shape):].copy()
    y_test = X_test[response].copy()
    X_test.drop([response], axis =1 , inplace = True)
    
    return X_train, X_test, y_train, y_test 