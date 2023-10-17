from sklearn.model_selection import train_test_split
import pandas as pd


# Function that returns features (X) and target (Y)
def define_features(df):
    X = df[["age", "height", "weight", "aids", "cirrhosis", "hepatic_failure", "immunosuppression", "leukemia", "lymphoma", "solid_tumor_with_metastasis"]]
    Y = df["diabetes_mellitus"]
    return X, Y

#Input p is the proportion of test sample. The function will divide the sample into train and test.
def train_n_test_features(df):
    X, Y = define_features(df)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=30)
    return X_train, X_test, Y_train, Y_test



from sklearn.linear_model import LogisticRegression

#Function that trains log model for a given features and objective variable.
def train_log_model(X, Y):
    log_model = LogisticRegression()
    log_model.fit(X,Y)
    return log_model

#Function that calculates test scores 
def test_log_model(x_train,y_train,x_test,y_test):
    train_model = train_log_model(x_train, y_train)

    train_score = train_model.score(x_train, y_train)
    test_score = train_model.score(x_test,y_test)

    return (train_score, test_score)

#Function that calculates probabilities.
def predict_probs(x_train, y_train,x_test):
    train_model = train_log_model(x_train, y_train)

    train_probabilities = train_model.predict_proba(x_train)[:, 1]
    test_probabilities = train_model.predict_proba(x_test)[:, 1]
    train_probabilities =  pd.Series(train_probabilities)
    test_probabilities =  pd.Series(test_probabilities)

    return train_probabilities, test_probabilities

def merge_sets(x_train, x_test, train_probabilities, test_probabilities):
    x_train['predictions'] = train_probabilities
    x_test['predictions'] = test_probabilities

    return x_train , x_test





