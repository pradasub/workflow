def describe():
    return print(
        f'This is a reminder to change all the categories to a human readable format.\n'
        f'Also change the response variable to "0", "1", "2" for categorical response.\n'
        f'Also change number of categories in the categorical variables etc.\n'
        f'This is a chance to change the data as we put it into a machine learning algorithm.\n'
        f'use pandas qcut to change numerical variable to categorical'
        f'pd.qcut(data["var"], q=3, , labels=["var_class_1","var_class_2","var_class_3"]) -> for example'
        f'TODO: Check the best practice (especially for the response variable)'
    )