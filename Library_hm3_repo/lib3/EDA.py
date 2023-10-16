import pandas  as pd
import numpy as np


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
