from scipy import stats
import collections

loansData = pd.read_csv('/Users/carolynsfolder/Thinkful-projects/loansData.csv')
loansData.dropna(inplace = True)  ## removes rows with null values 

freq = collections.Counter(loansData['Open.CREDIT.Lines'])
## provides counts of observations for each number of credit lines

plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
# Summary - freq data is slightly left skewed, but generally normally distributed

chi, p = stats.chisquare(freq.values())
print chi
print p 
