import Library_hm3_repo
from Library_hm3_repo.lib3.clean_model import load_sample_diabetes_data, model_cleaning
from Library_hm3_repo.lib3.model_running import train_n_test_features, test_log_model, predict_probs
#from Library_hm3_repo.lib3.model_running import 
import os

#Load and split data
df = load_sample_diabetes_data()

df

# Clean data
clean_df = model_cleaning(df)

clean_df

# Running Model
X_train, X_test, Y_train, Y_test = train_n_test_features(clean_df)


#train  model
scores = test_log_model(X_train, Y_train, X_test, Y_test)
scores

#Calculate Probabilities
probabilities = predict_probs(X_train,Y_train, X_test)
probabilities

