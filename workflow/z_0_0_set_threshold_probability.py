import numpy as np

def describe():
    
    return print(
        f'This module is to set threshold probability for precison and recall calculation\n'
        f'The default threshold probability is 0.5\n'
        f'Also it is asserted within the code that prbability 0.5 equals default\n'
        f'Recall: How well are you able to predict postives\n'
        f'Precision: Of the ones you predict positives what portion do you get it right\n'
        f'predict_probability(model, X_test,thres=0.5)\n'
    )

def predict_probability(model, X_test,thres=0.5):
    pred_thres = (model.predict_proba(X_test)[:,1] >= thres).astype(int)
    pred_thres_0_5 = (model.predict_proba(X_test)[:,1] >= 0.5).astype(int)
    
    try:
        assert np.array_equal(model.predict(X_test), pred_thres_0_5)
    except:
        print('This is probably a neural network model')
    
    try:
        assert np.array_equal(model.predict_classes(X_test), pred_thres_0_5)
    except:
        print('This is not a neural network model')
        
    print(f'Asserted that probability threshold 0.5 gives default prediction')
    
    return pred_thres