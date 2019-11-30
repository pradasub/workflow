import pandas as pd
from treeinterpreter import treeinterpreter as ti

def describe():
    return print(
        f'This module is for interpreting the random forest (or decision tree) model\n'
        f'It traces the decision tree to find decision path fro each instance\n'
        f'This module is only to be performed after one-hot, scaler etc. has been done\n'
        f'interpreter(X_test,model, index_of_instance)->\n'
        f'index_of_instance is as it is defined, however this is iloc not loc\n'
    )


def interpreter(X_test,model, index_of_instance):
    data_point = pd.DataFrame([X_test.iloc[index_of_instance]])
    data_point.index = ['value_variable'] # Once transposed, it will be the column name
    prediction, bias, contributions = ti.predict(model, data_point)
    local_interpretation = data_point.append(pd.DataFrame([[round(c[0],3) for c in contributions[0]]], columns=data_point.columns.tolist(), index=['contribution_variable'])
).T
    return local_interpretation.iloc[local_interpretation['contribution_variable'].abs().argsort()][::-1]