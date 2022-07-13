# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 06:46:57 2022

@author: Rakesh
"""

##importing package#

import pandas as pd
#loading data frame calorie.csv#

calories=pd.read_csv('D:/DATA SCIENCE ASSIGNMENT/DataSets-Data Pre Processing/DataSets/calories_consumed.csv')

calories.info() ##there is no null values in dataset##

calories.shape

calories.describe()

EDA =pd.DataFrame({'columns_name':[calories.columns],
                   "means": [calories.mean()],
                   'median': [calories.median()],
                   'mode': [calories.mode()],
                   'std deviation': [calories.std()],
                   'variance': [calories.var()],
                   'skewness':[calories.skew()],
                   'kurtosis':[calories.kurt()]})
EDA

##lets transform the columns##

result = calories.transform(func=['sqrt','log','Exp'])

print(result)
