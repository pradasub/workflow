import lime
import lime.lime_tabular

def describe():
    
    return print(
        f'This module is for interpreting the machine learning model through LIME\n'
        f'Local Interpretable Model-Agnostic Explanations\n'
        f'This is to interpret every observation using lime interpretation\n'
        f'exp, plot = explain_instances(X_train,y_train,X_test,model',
        f'response_field,class_names, index_of_instance, num_features=5): ->\n'
        f'index_of_instance is as it is defined, however this is iloc not loc\n'
    )

def identify_categorical_features(df):
    # Identify categorical features - any feature with only values of 0 and 1
    categorical_feature_idcs = []
    categorical_feature_names = {}
    
    for ii, col in enumerate(df.columns.values):
        
        if sorted(df[col].unique()) == [0, 1]:
            categorical_feature_idcs.append(ii)
            categorical_feature_names[ii] = ["0", "1"]# Removed from ["False", "True"]

    return categorical_feature_idcs, categorical_feature_names


def explain_instances(
    X_train,y_train,X_test, model,response_field,
    class_names, index_of_instance, num_features=5
):
    # Get categorical features
    categorical_feature_idcs,categorical_feature_names= identify_categorical_features(X_train)
    print(categorical_feature_idcs)
    # LIME (Local Interpretable Model-Agnostic Explanations)
    explainer = lime.lime_tabular.LimeTabularExplainer(
        X_train.to_numpy(),
        training_labels=y_train,
        feature_names=X_train.columns.values,
        categorical_features=categorical_feature_idcs,
        categorical_names=categorical_feature_names,
        class_names=class_names,
        discretize_continuous=True,
    )
    
    def proba(X_test):
        
        return model.predict_proba(X_test)
    
    
    exp = explainer.explain_instance(
        X_test.iloc[index_of_instance].astype(int).values,proba, 
        num_features=num_features)
    
    return exp, exp.show_in_notebook()



