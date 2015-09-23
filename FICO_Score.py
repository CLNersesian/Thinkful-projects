import pandas as pd

loansData = pd.read_csv('/Users/carolynsfolder/Thinkful-projects/loansData.csv'

loansData['Interest.Rate'][0:5] ## shows the first 5 rows of interest rate
loansData['Loan.Length'][0:5] # shows first 5 rows of loan length
loansData['FICO.Range'][0:5] # shows the first 5 rows of FICA range


## Plotting A Histogram of FICO Score

iloansData.csv')

## lambda function to remove % sign from Interest.Rate column
loansData['Interest.Rate'] = map(lambda x: float(x.rstrip('%')), loansData['Interest.Rate'])
## Test response
loansData['Interest.Rate'][0:5] ## shows the first 5 rows of interest rate

## lambda function to remove the word 'month' from Loan.Length column
loansData['Loan.Length'] = map(lambda x: int(x.rstrip('months')), loansData['Loan.Length'])
## Test response 
loansData['Loan.Length'][0:5] # shows first 5 rows of loan length


## Change FICO scores to numerical values. 
loansData['FICO.Score'] = loansData['FICO.Range'].astype('string')
## Save FICO score as a new column called 'FICO.Score'
loansData['FICO.Score'] = map(lambda x: int(x.split("-")[0]), loansData['FICO.Score']) 
## Test response 
loansData['FICO.Score'][0:5] # shows the first 5 rows of FICA range

## Plot histogram 
import matplotlib.pyplot as plt

plt.figure()
p = loansData['FICO.Score'].hist()
## Data is left skewed/ not normally distributed

## Generate a scatterplot of the data (scatterplot matrix) 
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')

## Evidence of linear trend btn FICO scores and Interest Rate.
## No evidence of a linear trend btn Monthly income and Interest Rate or btn Monthly income and Loan Length.
## Evidence of an increasing trend in monthly income for Loan Amount
## FICO Score and Loan Amount are informative independent variables.

