

path="/Users/ruimaciel/Desktop/Barcelona/Computing for Data Science/hw3/sample_diabetes_mellitus_data.csv"

df= pd.read_csv(path)

def dropmissingvalues(df):
    df.dropna(subset=["age", "gender", "ethnicity"])
    return df

def fillmissingvalues_with_mean(df):
    df["height"]= df["height"].fillna(df["height"].mean())
    df["weight"]= df["weight"].fillna(df["weight"].mean())
    return df

def inputdummyvariables(df):
    pd.get_dummies(df, columns=["ethnicity"], prefix="ethnicity")
    df = df.replace({True: 1, False: 0})
    return df

def model_cleaning(df):
    df1=dropmissingvalues(df)
    df2=fillmissingvalues_with_mean(df1)
    df3=inputdummyvariables(df2)
    return df3



