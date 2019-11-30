from collections import Counter

from imblearn.combine import SMOTEENN
from imblearn.combine import SMOTETomek

from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import ADASYN
from imblearn.over_sampling import BorderlineSMOTE
from imblearn.over_sampling import KMeansSMOTE
from imblearn.over_sampling import RandomOverSampler
from imblearn.over_sampling import SMOTENC
from imblearn.over_sampling import SVMSMOTE

from imblearn.under_sampling import CondensedNearestNeighbour
from imblearn.under_sampling import EditedNearestNeighbours
from imblearn.under_sampling import RepeatedEditedNearestNeighbours
from imblearn.under_sampling import AllKNN
from imblearn.under_sampling import InstanceHardnessThreshold
from imblearn.under_sampling import NearMiss
from imblearn.under_sampling import NeighbourhoodCleaningRule
from imblearn.under_sampling import OneSidedSelection
from imblearn.under_sampling import RandomUnderSampler
from imblearn.under_sampling import TomekLinks

def describe():
    return print(
        f'This module is for imbalanced learn in python\n'
        f'A lot of the times we deal with imbalanced data\n'
        f'This module is for quick access to the imblearn library\n'
        f'MAKE SURE TO SAVE X_train AND y_train BEFORE RUNNING THROUGH THE SAMPLING ALGORITHM\n\n\n'
        f'sampling(X_train, y_train, sampling_method) -> choose sampling method from one below\n\n'
        f'from imblearn.combine import SMOTEENN\n'
        f'from imblearn.combine import SMOTETomek\n\n\n'
        f'from imblearn.over_sampling import SMOTE\n'
        f'from imblearn.over_sampling import ADASYN\n'
        f'from imblearn.over_sampling import BorderlineSMOTE\n'
        f'from imblearn.over_sampling import KMeansSMOTE\n'
        f'from imblearn.over_sampling import RandomOverSampler\n'
        f'from imblearn.over_sampling import SMOTENC\n'
        f'from imblearn.over_sampling import SVMSMOTE\n\n'
        f'from imblearn.under_sampling import CondensedNearestNeighbour\n'
        f'from imblearn.under_sampling import EditedNearestNeighbours\n'
        f'from imblearn.under_sampling import RepeatedEditedNearestNeighbours\n'
        f'from imblearn.under_sampling import AllKNN\n'
        f'from imblearn.under_sampling import InstanceHardnessThreshold\n'
        f'from imblearn.under_sampling import NearMiss\n'
        f'from imblearn.under_sampling import NeighbourhoodCleaningRule\n'
        f'from imblearn.under_sampling import OneSidedSelection\n'
        f'from imblearn.under_sampling import RandomUnderSampler\n'
        f'from imblearn.under_sampling import TomekLinks\n'
    )

# Combination Sampling methods#################################################
def sampling(X, y, sampling_method, random_state=99):
    print(f'the count of classes before sampling: {Counter(y)}')
    smp = eval(sampling_method)()
    X, y = smp.fit_sample(X, y)
    print(f'the count of classes after sampling: {Counter(y)}')
    print(f'the sampling method that is used: {sampling_method}')
    return X, y








