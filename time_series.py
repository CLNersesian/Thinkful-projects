import pandas as pd
import numpy as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/carolynsfolder/Thinkful-projects/LoanStats3c.csv', header=1, low_memory=False)
df = df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)


df['list_d_format'] = pd.to_datetime(df['issue_d'])
dfts = df.set_index('list_d_format')
year_month_summary = dfts.groupby('issue_d').count()
loan_count_summary = year_month_summary['issue_d']

plt.plot(loan_count_summary)

## indicates that it is not a stationary time-series.
## use the difference to assess the data
loan_count_summary_diff = loan_count_summary.diff()
loan_count_summary_diff = loan_count_summary_diff.fillna(0)

plt.plot(loan_count_summary_diff)

## Plot shows negative values. Add a threshold of 316 to all terms
## or try dividing the with the maximum value
loan_count_summary_diff = loan_count_summary_diff + 316
loan_count_summary_diff = loan_count_summary_diff/max(loan_count_summary_diff)
plt.plot(loan_count_summary_diff)

## plot ACF and PACF 
sm.graphics.tsa.plot_acf(loan_count_summary_diff) # autocorrelation
sm.graphics.tsa.plot_pacf(loan_count_summary_diff) # partial autocorrelation