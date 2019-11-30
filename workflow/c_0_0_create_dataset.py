import seaborn as sns
import pandas as pd
from sklearn.datasets import load_boston, load_iris, load_diabetes


def describe():
    return print(
        f'This module contains practice data available to us\n'
        f'Seaborn data: anscombe, attention, brain_networks, car_crashes, diamonds, dots\n'
        f'Seaborn data: exercise, flights, fmri, gammas, iris, mpg, planets, tips, titanic\n'
        f'scikitlearn available datasets are:\n'
        f'load_boston(), load_iris(), load_diabetes(), load_linnerud()\n'
        f'available_sns_data() to look at seaborn data available\n'
        f'sns_data(data="tips") -> to get sns data\n'
        f'scikitlearn_data(data="load_boston") -> load_iris for iris data etc.\n'
    )

# This is somehow not working says-no module named bs4
#def available_sns_data():
#    return sns.get_dataset_names()


def sns_data(data='tips'):
    return sns.load_dataset(data)

def scikitlearn_data(dataset='load_boston'):
    data = eval(dataset)()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    print(data.DESCR)
    return df