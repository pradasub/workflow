from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.compose import ColumnTransformer, make_column_transformer
def describe():
    return print(
        f'This module is to use standard scalar on the data so data are in the same scale.\n'
        f'The standard scaler is only used after one-hot encoding and train-test split is done.\n'
        f'Two different ways are described to use the standard scaler'
        f'One way is to use only for columns with unique values is greater than 2.\n'
        f'The other way is to use standard scaler for both categorical and numerical variables.\n'
        f'Only two standard scalers (minmax and standard) used for now\n'
        f'TODO: Research more standard scaler types'
        f'Remeber that the order of the column changes after running through the scaler transform only used for numerical variables\n'
        f'Therefore the process identifies the column order once it passes through the standard scaler\n'
        f'So we have to keep track of the order\n'
        f'X_train, X_test, col_order  = numeric(X_train, X_test,scaler = "standard")\n'
        f'-> pass train, test data and scaler ("stadard","minmax"), col_order is the order of column for train data - first method\n'
        f'X_train, X_test = numeric_and_categorical(X_train, X_test, scaler = "standard") -> for scaling both the numeric and categorical variables'
    )
def numeric(X_train, X_test,scaler = 'standard'):
    cols1 = []
    cols2 = []
    pt = []
    ii = 0 
    for i in X_train.columns:
        if X_train[i].nunique() <= 2:  # This is hardcoded for now - may need revisiting
            cols1.append(i)
        else:
            cols2.append(i)
            pt.append(ii)

        ii = ii + 1    
            
    col_order =  cols2 + cols1
    if scaler == 'standard':
        processor = make_column_transformer((StandardScaler(),pt),remainder="passthrough")
    if scaler == 'minmax':
        processor = make_column_transformer((MinMaxScaler(),pt),remainder="passthrough")

    X_train = processor.fit_transform(X_train) 
    X_test = processor.transform(X_test)

    return X_train, X_test, col_order


def numeric_and_categorical(X_train, X_test, scaler = 'standard'):
    if scaler == 'standard':
        processor = StandardScaler() 
    if scaler == 'minmax':
        processor = MinMaxScaler()

    X_train = processor.fit_transform(X_train)  
    X_test = processor.transform(X_test) 
    
    return X_train, X_test












