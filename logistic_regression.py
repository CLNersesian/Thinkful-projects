import pandas as pd
from math import * 
import statsmodels.api as sm
import matplotlib.pyplot as plt

## Cleaned loansData file -- see linear_regression.py 
loansData = pd.read_csv('/Users/carolynsfolder/Thinkful-projects/loansData_clean.csv')

## Statsmodel needs an intercept column in the dataframe.
## Add a column and set the intercept to a constant of 1
intercept = [1] * len(loansData)
loansData['Intercept'] = intercept 

## Creating columns for the independent variables, including the intercept 
ind_vars = ['Intercept', 'Amount.Requested', 'FICO.Score']

## Adding a column to the dataframe indicating if interest rate is < 12%
## This is a derived column created from interest rate
## The column contains binary values, i.e., '0' when interest rate < 12% and '1' for > 12%
interest_rate = loansData['Interest.Rate']
interest_rate = [1 if x < 12 else 0 for x in interest_rate]
loansData['IR_TF'] = interest_rate

## Checking above 
loansData[loansData['Interest.Rate'] == 10].head() ## All should be true
loansData[loansData['Interest.Rate'] == 13].head() ## All should be false

## Model for how interest rate varies with loan amount:
## interest_rate = b + a1(FICOScore) + a2(LoanAmount) 
## e.g., interest_rate = b + a1(750) + a2(10000)
## Code for Logistic Model 
x = loansData[ind_vars]
y = loansData['IR_TF']

logit = sm.Logit(y, x)
result = logit.fit()
coeff = result.params  ## coefficients for each independent variable 
print coeff

## Logistic Function 
## p(x) = 1/(1 +e^(intercept + 0.087423(FicoScore) - 0.000174(LoanAmount))
def logistic_function(FicoScore, LoanAmount, coeff):
	prob = 1/(1+exp(coeff[0]+coeff[2]*FicoScore+coeff[1]*LoanAmount))
	if prob > 0.7:
		p = 1
	else:
		p = 0
	return prob, p
	
prob = logistic_function(720, 10000, coeff)[0]
decision = logistic_function(720, 10000, coeff)[1]

## Plotting - testing for different FICO scores for 10,000 loans 
Fico = range(550, 950, 10
p_plus = []
p_minus = []
p = []
for x in Fico:
	p_plus.append(1/(1+exp(coeff[0]+coeff[2]*x+coeff[1]*10000))
	p_minus.append(1/(1+exp(-coeff[0]-coeff[2]*x-coeff[1]*10000))
	p.append(logistic_function(x, 10000, coeff)[1]
	
plt.plot(Fico, p_plus, label = 'p(x) = 1(1+exp(b+mx))', color = 'purple')
plt.plot(Fico, p_minus, label = 'p(x) = 1(1+exp(-b-mx))', color = 'pink'
plt.plot(Fico, p, 'ro', label = 'Results USD $10000')






