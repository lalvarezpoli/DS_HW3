from sklearn.model_selection import train_test_split


# Function that returns features (X) and target (Y)
def define_features(df):
    X = df[["age", "height", "weight", "aids", "cirrhosis", "hepatic_failure", "immunosuppression", "leukemia", "lymphoma", "solid_tumor_with_metastasis"]]
    Y = df["diabetes_mellitus"]
    return X, Y

#Input p is the proportion of test sample. The function will divide the sample into train and test.
def train_n_test_features(p):
    X, Y = define_features()
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=p, random_state=30)
    return X_train, X_test, Y_train, Y_test



from sklearn.linear_model import LogisticRegression

#Function that trains log model for a given features and objective variable.
def train_log_model(X, Y):
    log_model = LogisticRegression()
    log_model.fit(X,Y)
    return log_model

#Function that calculates test scores 
def test_log_model():
    train_model = train_log_model(X_train, Y_train)

    train_score = train_model.score(X_train, Y_train)
    test_score = train_model.score(X_test, Y_test)

    return (train_score, test_score)

#Function that calculates probabilities.
def predict_probs():
    train_model = train_log_model(X_train, Y_train)

    train_probabilities = logistic_model.predict_proba(X_train)[:, 1]
    test_probabilities = logistic_model.predict_proba(X_test)[:, 1]

    return (train_probabilities, test_probabilities)






