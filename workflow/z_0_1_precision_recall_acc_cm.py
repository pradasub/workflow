import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix  

def describe():
    
    return print(
        f'This module will give a dataframe of precision, recall, accuracy\n'
        f'and confusion matrix for binary variable\n'
        f'pass in test and prediction of the binary variable\n'
        f'TODO: if other than binary variable\n'
        f'scikit_results(y_test, y_pred) -> gives classification report and confusion matrix from sklearn\n'
        f'prec_recall, confusion_matrix = metrics(y_test, y_pred) -> this is customized'
    )

def metrics(y_test, y_pred):
    lst1 = list(y_test)
    lst2 = list(y_pred)
    x = pd.DataFrame(list(zip(lst1, lst2)), columns =['y_test', 'y_pred'])
    x['y_test'] = x['y_test'].astype(int)
    x['y_pred'] = x['y_pred'].astype(int)


    true_pos = len(x[(x['y_test'] == 1) & (x['y_pred'] == 1)])
    false_pos = len(x[(x['y_test'] == 0) & (x['y_pred'] == 1)])
    true_neg = len(x[(x['y_test'] == 0) & (x['y_pred'] == 0)])
    false_neg = len(x[(x['y_test'] == 1) & (x['y_pred'] == 0)])

    confusion_matrix = pd.DataFrame({'Predicted Positive':[true_pos, false_pos], 
                        'Predicted Negative':[false_neg, true_neg]}, 
                        index=['Actual Positive', 'Actual Negative'])
    
    try:
        precision = true_pos/(true_pos + false_pos)
    except ZeroDivisionError:
        print("Divided by zero for precision; precision is infinite")
        precision = "inf"
        
    try:    
        recall = true_pos/(true_pos + false_neg)
    except ZeroDivisionError:
        print("Divided by zero for recall; recall is infinite")
        recall = "inf"
        
    if (type(precision)==str) or (type(recall)==str):
        f1_score = 0
    else:    
        f1_score = 2 * precision*recall/(precision + recall)
    accuracy = (true_pos + true_neg)/(true_pos+false_pos+true_neg+false_neg)

    prec_recall = pd.DataFrame({'Precision':[precision],'Recall':[recall],
        'F1 Score':[f1_score], 'Accuracy': [accuracy]}, index = ['important metrics'])

    return prec_recall, confusion_matrix

def scikit_results(y_test, y_pred):
    y_test, y_pred
    
    print(confusion_matrix(y_test, y_pred)) 
    print('\n\n')
    print(classification_report(y_test, y_pred))         



