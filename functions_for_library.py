import pandas as pd

path="/Users/ruimaciel/Desktop/Barcelona/Computing for Data Science/hw3/sample_diabetes_mellitus_data.csv"

df= pd.read_csv(path)

df.head(20)

!pip install scikit-learn

from sklearn.model_selection import train_test_split

# Split the data into a training set and a testing set (e.g., 80% training, 20% testing)
data_train, data_test = train_test_split(df, test_size=0.2, random_state=30)


# Remove those rows that contain NaN values in the columns: age, gender, ethnicity.

df = df.dropna(subset=["age", "gender", "ethnicity"])


#Fill NaN with the mean value of the column in the columns: height, weight.
df["height"]= df["height"].fillna(df["height"].mean())
df["weight"]= df["weight"].fillna(df["weight"].mean())

#Generate dummies for ethnicity column (One hot encoding).

df = pd.get_dummies(df, columns=["ethnicity"], prefix="ethnicity")

df = df.replace({True: 1, False: 0})

print(df.head(20))

# Your data and labels


# Define your features (X)
X = df[["age", "height", "weight", "aids", "cirrhosis", "hepatic_failure", "immunosuppression", "leukemia", "lymphoma", "solid_tumor_with_metastasis"]]

# Define your target variable (Y)
y = df["diabetes_mellitus"]

X_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=30)

from sklearn.linear_model import LogisticRegression

logistic_model = LogisticRegression()
logistic_model.fit(X_train, y_train)

print(logistic_model.score(x_test, y_test))
print(logistic_model.score(X_train, y_train))
print(X_train)
print(x_test)

train_probabilities = logistic_model.predict_proba(X_train)[:, 1]
test_probabilities = logistic_model.predict_proba(x_test)[:, 1]


# Compute the train and test roc_auc metric using roc_auc_score from sklearn.

from sklearn.metrics import roc_auc_score

train_roc_auc = roc_auc_score(y_train, train_probabilities)
test_roc_auc = roc_auc_score(y_test, test_probabilities)

print(train_roc_auc)
print(test_roc_auc)