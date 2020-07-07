#################
## data_analysis.py
##
## Purpose: in this file, I analyze the subject files in data_file.csv
#################

#imports
import pandas as pd
import numpy as np
from IPython.display import display

#loading function
data = pd.read_csv('data_file.csv', delimiter='\t')
print('initial data: ')
display(data.head())

#add some random numbers as a column
print('\nwith new test column')
data['test1'] = np.random.random(size=(10,1))*100
display(data.head())