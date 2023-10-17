
import os
import pandas as pd

path = os.getcwd()
path
df = pd.read_csv(path+'/Notebooks/sample_diabetes_mellitus_data.csv')


def dropmissingvalues(df):
    data = df.dropna(subset=["age", "gender", "ethnicity"])
    return data

def fillmissingvalues_with_mean(df):
    df["height"]= df["height"].fillna(df["height"].mean())
    df["weight"]= df["weight"].fillna(df["weight"].mean())
    return df

def inputdummyvariables(df):
    df2 =pd.get_dummies(df, columns=["ethnicity"], prefix="ethnicity")
    df2 = df2.replace({True: 1, False: 0})
    return df2

def model_cleaning(df):
    df1=dropmissingvalues(df)
    df2=fillmissingvalues_with_mean(df1)
    df3=inputdummyvariables(df2)
    return df3

df.shape
df.isna().sum()

df3 = model_cleaning(df)

df3.shape
df3.isna().sum()