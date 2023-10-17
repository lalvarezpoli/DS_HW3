import os
import pandas as pd




#Function that loads the data and returns a df.
def load_sample_diabetes_data():
    path = os.getcwd()
    df = pd.read_csv(path+'/sample_diabetes_mellitus_data.csv')
    return df

#Function that divides df into training and test.
def divide_data(df: pd.DataFrame):
    data_train, data_test = train_test_split(df, test_size=0.2, random_state=30)
    return data_train, data_test

#Function that takes the loaded data and splits into training and test subdatasets.
def load_n_split_diabetes_data():
    df = load_sample_diabetes_data()
    data_train, data_test = divide_data(df)
    return data_train, data_test

# # Function that remove rows that contain NaN values in the columns: age, gender, ethnicity.
# def rm_na(df):
#     rm_df = df.dropna(subset=["age", "gender", "ethnicity"])
#     return df





