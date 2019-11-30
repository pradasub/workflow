from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.layers.core import Dropout
from keras.optimizers import Adam,SGD, RMSprop, Adagrad, Adadelta, Adam, Adamax,Nadam
from keras.metrics import categorical_crossentropy
def describe():
    return print(
        f'Neural Network Model for Regression with dropout\n'
        f'This module should include the most basic to the most advanced form of neural netowork model in keras\n'
        f'TODO: Advanced Neural Networks\n'
        f'optimizers: SGD, RMSprop, Adagrad, Adadelta, Adam, Adamax,Nadam\n'
        f'basic_model_classification(in_shape,total_hidden_layer,opt_func="Adam",learning_rate=0.001,loss_func="mse",metric=["mse","mae"], dropout=0.2)\n'
        f'fit_model(X_train, y_train, model, batch_size=10, epochs=100, shuffle=True, verbose=2, validation_split=0.1)\n'
    )

def basic_model_classification(in_shape,total_hidden_layer,opt_func='Adam',
                               learning_rate=0.001,loss_func='mse',metric=['mse','mae'],dropout=0.2):
    
    max_pos_dense = []
    shp = int(3./4.*in_shape)
    i = 2
    max_pos_dense.append(i)
    while i < shp:
        i = 2*i
        max_pos_dense.append(i)
    max_pos_dense.reverse()
    
    len_max = len(max_pos_dense)
    if total_hidden_layer > len_max:
        total_hidden_layer = len_max
    
    model =  Sequential()
    model.add(Dense(max_pos_dense[0], input_shape=(in_shape,), activation='relu'))
    model.add(Dropout(dropout))
    max_pos_dense.remove(max_pos_dense[0])
    
    for j in range(total_hidden_layer-1):    
        model.add(Dense(max_pos_dense[j], activation='relu'))
        model.add(Dropout(dropout))
    model.add(Dense(1, activation = 'linear'))
    
    # compile the model
    model.compile(eval(opt_func)(lr = learning_rate), loss = loss_func, metrics = [metric])
    return model

def fit_model(X_train, y_train, model, batch_size=10, epochs=100, shuffle=True, verbose=2, validation_split=0.1):
    model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, shuffle=shuffle, verbose=verbose, validation_split=validation_split)

    



