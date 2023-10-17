import pandas  as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display



#  Return list of numeric  columns in dataset
def numeric_cols(dataset):
    numerics = dataset.select_dtypes(include= np.number).columns.tolist()
    return numerics

# Calculate  Summary Statistics in Dataframe
def pop_parameters(dataset):
    statistics = {}

    for i in dataset.columns:
        size = np.size(dataset[i])
        datatype = dataset[i].dtypes
        unique_values = dataset[i].unique().size
        mean = np.mean(dataset[i])
        stdv = np.std(dataset[i])
        min = dataset[i].min()
        per25 = dataset[i].quantile(0.25)
        median = dataset[i].quantile(0.50)
        per75 = dataset[i].quantile(0.75)
        max = dataset[i].max()
        IQRs = dataset[i].quantile(0.75) - dataset[i].quantile(0.25)
        lower_bound = (dataset[i].quantile(0.25)) - 1.5*(dataset[i].quantile(0.75) - dataset[i].quantile(0.25))
        upper_bound = (dataset[i].quantile(0.75)) + 1.5*(dataset[i].quantile(0.75) - dataset[i].quantile(0.25))

        statistics[i] = (size,datatype,unique_values,mean,stdv,min,per25,median,per75,max,IQRs,lower_bound,upper_bound)
    results = pd.DataFrame.from_dict(statistics,orient='index',columns=['size','datatype','unique_values','mean','stdv','min','per25',
                                                                        'median','per75','max','IQRs','lower_bound','upper_bound'])
    results['lower_bound'] = np.where((results['lower_bound']<0) & (results['min']>=0),0,results['lower_bound'])
    return round(results,2)


# Plot all numeric histograms
def plot_hist_mult(data,var1,var2,bins):
    fig, axes = plt.subplots(var1,var2)

    for i, el in enumerate(list(data.columns.values)):
        a= data.hist(el,ax=axes.flatten()[i], bins=bins)

    fig.set_size_inches(5,6)
    plt.tight_layout()
    plt.show()


# Exploration function
def explore(dataset,num_columns,plot_rows,plot_cols):
    num = numeric_cols(dataset)

    summary_stats = pop_parameters(dataset[num].iloc[:, :num_columns])
    summary_trans = summary_stats.round(2).T

    print('Summary Statistics')
    display(summary_trans)
    print('histograms')
    plot_hist_mult(dataset[num].iloc[:, :num_columns],plot_rows,plot_cols,30)