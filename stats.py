import pandas as pd

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

data = data.splitlines() ## split string on newlines or use data.split('\n')

## split each list item by commas into a list comprehension 
data = [i.split(', ') for i in data] 

## create pandas dataframe 
column_names = data[0]  ## first row
data_rows = data[1::]  ## all subsequent rows of data
df = pd.DataFrame(data_rows, columns=column_names) 

import scipy.stats 
from scipy import stats

## convert Alcohol and Tobacco columns to float
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

df['Alcohol'].mean()
df['Alcohol'].median()
stats.mode(df['Alcohol'])

df['Tobacco'].mean()
df['Tobacco'].median()
stats.mode(df['Tobacco'])

max(df['Alcohol']) - min(df['Alcohol'])
df['Alcohol'].std()
df['Alcohol'].var()

max(df['Tobacco']) - min(df['Tobacco'])
df['Tobacco'].std()
df['Tobacco'].var()

## Challenge
print "Mean values for Alcohol and Tobacco in Great Britian, respectively:", df['Alcohol'].mean(), df['Tobacco'].mean()
print "Median values for Alcohol and Tobacco in Great Britian, respectively:", df['Alcohol'].median(), df['Tobacco'].median()
print "The Mode for the Alcohol and Tobacco in Great Britian, respectively ", stats.mode(df['Alcohol'])[0][0], stats.mode(df['Tobacco'])[0][0]

print "Range values for Alcohol and Tobacco in Great Britian, respectively:", max(df['Alcohol']) - min(df['Alcohol']), max(df['Tobacco']) - min(df['Tobacco'])
print "Variance values for Alcohol and Tobacco in Great Britian, respectively:", df['Alcohol'].var(), df['Tobacco'].var()
print "Standard deviation values for Alcohol and Tobacco in Great Britian, respectively:", df['Alcohol'].std(), df['Tobacco'].std()


