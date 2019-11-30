import numpy as np
def describe():
    return print(
        f'Change all other categories to object type\n'
        f'data = cat_to_object(data)\n'
    )

def cat_to_object(data):
    for i in data.columns:
        if data[i].dtype.name=="category":
            data[i] = data[i].astype("O")
        
        if data[i].dtype.name=="bool":
            data[i] = data[i].astype(np.int64)
    
    return data
            