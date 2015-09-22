""" Write a script that reads in loan data, cleans it, and loads it into a pandas DataFrame""""
"""Use the script to generate and save a boxplot, histogram, and QQ-plot for the values in the "Amount.Requested" Column"""
"""Describe the results and how it compares to the "Amount.Funded.By.Investors" column"""

import matplotlib.pyplot as plt
import pandas as pd

loansData = pd.read_csv('/Users/carolynsfolder/Thinkful-projects/loansData.csv')

loansData.dropna(inplace = True)  ## removes rows with null values 

## Boxplot 
loansData.boxplot(column = 'Amount.Funded.By.Investors')
plt.savefig("AFBIloansData_Box.png")
# Summary - AFBIboxplot shows an outlier in the upper 25th percentile. Data is skewed towards upper 25th percentile.

loansData.boxplot(column = 'Amount.Requested')
plt.savefig("ARloansData_Box.png")
# Summary - ARboxplot data is skewed towards upper 25h percentile. 

## Histogram - saved figure
loansData.hist(column= 'Amount.Funded.By.Investors')
plt.savefig("AFBIloansData_Hist.png")
# Summary - AFBIhist data is left-skewed/not normally distributed

loansData.hist(column= 'Amount.Requested')
plt.savefig("ARloansData_Hist.png")
# Summary - ARhist data is left-skewed/not normally distributed

## QQ-Plot
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

plt.figure() 
QQ_loansData = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.savefig("AFBIloansData_QQ")
# Summary - AFBIQQ data is heavy tailed with more pronounced left skew 

QQ_loansData = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig("ARloansData_QQ")
# Summary - ARQQ data is heavy tailed with more pronounced left skew 

