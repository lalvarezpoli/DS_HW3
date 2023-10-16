import Library_hm3_repo
from Library_hm3_repo.lib3.compute_death_rate import pop_parameters
import pandas as pd
import numpy as np
import os 

path = os.getcwd()
path
df = pd.read_csv(path+'/Notebooks/sample_diabetes_mellitus_data.csv')

pop_parameters(df[['height','weight']])