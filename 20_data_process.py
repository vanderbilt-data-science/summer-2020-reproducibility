#################
## 20_data_process.py
##
## Purpose: in this file, I process the subject file in data_file.csv
#################

#imports
import pandas as pd
import numpy as np
from IPython.display import display

#loading function
data = pd.read_csv('data_file.csv', delimiter='\t')
print('initial data: ')
display(data.head())