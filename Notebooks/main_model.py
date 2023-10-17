import Library_hm3_repo
from Library_hm3_repo.lib3.clean_model import load_sample_diabetes_data, model_cleaning
from Library_hm3_repo.lib3.model_running import train_n_test_features, test_log_model, predict_probs, merge_sets
import os

#Load and split data
df = load_sample_diabetes_data()

# Clean data
clean_df = model_cleaning(df)

# Running Model
X_train, X_test, Y_train, Y_test = train_n_test_features(clean_df)

#Calculate Probabilities
proba_train, proba_test = predict_probs(X_train,Y_train, X_test)

#Compute the train and test roc_auc
scores = test_log_model(X_train, Y_train, X_test, Y_test)

#Merge train and test sets with predictions
train_predict_set, test_predict_set = merge_sets(X_train,X_test,proba_train,proba_test)

