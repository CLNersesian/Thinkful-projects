## Translate the Markov chain with Bull, Bear, Stagnent markets
## What are the transition probabilities after 1 transition?
## What are the transition probabilities after 2 transitions?
## After 5? 10? 
##What are the steady state probabilities? (i.e., raise the 
## matrix to higher and higher numbers until they converge)

import pandas as pd
df = pd.DataFrame({'rainy' : [.4,.7], 'sunny' : [.6,.3]},
index=["rainy", "sunny"])

print df

## example of square matrix for Markov chain 

print df.dot(df)
## calculates transition probabilities after multiple transitions
## raise transition matrix A to the nth power

df2 = pd.DataFrame({
    'bull': [.9, .075, .025],    
    'bear': [.15, .8, .05],
    'stag': [.25, .25, .5 ]
    },
    index = ['bull', 'bear', 'c_stag'])

print df
print df.dot(df)
print df.dot(df*df)
print df.dot(df*df*df)
print df.dot(df**200)


