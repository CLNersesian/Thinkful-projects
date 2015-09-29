import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

loans = pd.read_csv("/Users/carolynsfolder/Thinkful-projects/LoanStats3c.csv")

subset = pd.DataFrame(columns = ['Interest_Rate', 'Annual_Income', 'Home'])

subset = ['Interest_Rate'] = loans.int_rate
subset = ['Annual_Income'] = loans.annual_inc.astype(float)
subset = ['Home'] = loansData.home_ownership

## adding an intercept column to dataframe
subset['Intercept'] = float(1.0)

subset.dropna(inplace=True)
subset['Interest_Rate'] = map(lambda x: float(x.rstrip('%')), subset['Interest_Rate'])

## Monthly income
m1 = sm.OLS(subset['Interest_Rate', subset[['Intercept', 'Annual_Income']])
r1 = m1.fit()

print r1.summary()

## Home ownership in the model
subset['Home'] = pd.Categorical(subset.Home).labels
m2 = sm.OLS(subset['Interest_Rate', subset[['Intercept', 'Annual_Income', 'Home']])
r2 = m2.fit()

print r2.summary()

## Add interaction btn income and home ownership
subset['Interaction'] = loansDF['Annual_Income'] * loansDF['Home']

m3 = sm.OLS(subset['Interest_Rate'], subset[['Intercept', 'Annual_Income', 'Home', 'Interaction']])
r3 = m3.fit()

print r3.summary()
 

