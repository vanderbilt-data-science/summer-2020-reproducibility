#################
## 10_data_load.py
##
## Purpose: in this file, I load and modify the subject files in data_file.csv
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

#add set district function
def set_district(row):
    if row % 2 == 0:
        return 'davidson'
    else:
        return 'williamson'

#even IDs are from a particular district
data['district'] = data['subject id'].apply(set_district)
display(data.head())

#change data type of subject id to do math on
data['subject id'] = data['subject id'].astype('float32') + 10e8
display(data.head())

#the first two numbers of the id are the childen's ages
data['year'] = data['subject id']//1e8
display(data.head())

#convert the subject ids to strings to ensure number integrity
data['subject id'] = data['subject id'].apply(lambda x: '{0:2.6e}'.format(x))
display(data.head())

#save file
data.to_csv('data_file.csv', sep='\t', index=False)