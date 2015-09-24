import numpy as np
import pandas as pd
import statsmodels.api as sm

loansData = pd.read_csv('/Users/carolynsfolder/Thinkful-projects/loansData.csv')

## Cleaning data frame
loansData['Interest.Rate'] = map(lambda x: float(x.rstrip('%')), loansData['Interest.Rate'])
loansData['Interest.Rate'][0:5] ## shows the first 5 rows of interest rate

loansData['Loan.Length'] = map(lambda x: int(x.rstrip('months')), loansData['Loan.Length'])
loansData['Loan.Length'][0:5] # shows first 5 rows of loan length

loansData['FICO.Score'] = loansData['FICO.Range'].astype('string')
loansData['FICO.Score'] = map(lambda x: int(x.split("-")[0]), loansData['FICO.Score']) 
loansData['FICO.Score'][0:5] # shows the first 5 rows of FICA range

## Cleaned data frame 
intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

## Assigning dependent variable to y
y = np.matrix(intrate).transpose()
## Assigning independent variables to x1 (fico) and x2 (loanamt)
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

## creating two columns, one for each independent variable (input matrix)
x = np.column_stack([x1, x2])

## linear model
x = sm.add_constant(x)
model = sm.OLS(y,x)
f = model.fit()

## shows results
f.summary() 

print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-values: ', f.pvalues
print 'R-Squared: ', f.rsquared

loansData.to_csv('loansData_clean.csv', header=True, index=False)