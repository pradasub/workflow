import matplotlib.pyplot as plt
import seaborn as sns

def describe():
    
    return print(
        f'This module is for plots using seaborn library.\n'
        f'It includes some of the basic plots that can be performed on the data.\n'
        f'Description on the functions and how to pass is given below:\n'
        f'pair_plot(data, sample) -> pass in data.sample(n = your_choice) default is 0.5,\n'
        f'fraction of dataframe to be passed\n'
        f'heat_map(data,num_unique) -> This gives corr heat map and does not take objects.\n' 
        f'num_unique is how many number of unique values you want.\n'
        f'dist_plot(data, column) -> data and the column you want the distribution plot for\n'
        f'bar_plot(data,x,y,hue=None) -> bar plot with x and y column and hue.\n'
        f'Gives mean of the bar plot. Estimator=median not working\n'
        f'scatter_plot(data,x,y,hue=None) -> scatter plot with x and y column and hue\n'
           )

def pair_plot(data, sample = 0.5):
    sample_num = int(sample*len(data))
    sample_data = data.sample(n = sample_num)
    
    return sns.pairplot(sample_data)

def cols_for_map_dist(data, num_unique=100):
    cols_hm = []
    
    for i in data.columns:
        
        if data[i].nunique() > num_unique and data[i].dtype != "O":
            cols_hm.append(i)
            
    return cols_hm

def heat_map(data, num_unique):
    cols_hm = cols_for_map_dist(data, num_unique)
    inr_data = data[cols_hm].copy()
    
    return sns.heatmap(inr_data.corr(),annot = True,linewidths=.5)

def dist_plot(data, column):
    
    return sns.distplot(data[column])


def bar_plot(data, x, y, hue=None):
    
    return sns.barplot(x = x, y = y, data=data,hue=hue)


def scatter_plot(data, x, y, hue=None):
    
    return sns.scatterplot(x = x, y = y, data=data,hue=hue)





