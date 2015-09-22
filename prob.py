## plotting a normal distribution 
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

mean = 0
variance = 1
sigma = np.sqrt(variance) ## standard deviation 
x = np.linspace(-3, 3, 100)
plt.plot(x, mlab.normpdf(x, mean, sigma))


## calculating frequency  
import collections

test = [1, 4, 5, 6, 9, 9, 9]

c = collections.Counter(test)

print c

count_sum = sum(c.values()) # computes number of instances in the list

for k,v in c.iteritems():
	print "Frequency for number " + str(k) + " is " + str(float(v) / count_sum)


## drawing a box plot
import matplotlib.pyplot as plt

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
plt.boxplot(x)
plt.show()  ## opens a second window with the plot, or use savefig(): plt.savefig("boxplot.png") -- saves plot as plt w/ filename

## drawing a histogram of x
plt.hist(x, histtype = 'bar')
plt.show()

## drawing a QQ-plot
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

plt.figure()
test = np.random.normal(size=1000)  ## randomly generate 1000 normally distributed data points 
fig1 = stats.probplot(test, dist="norm", plot-plt)

plt.figure()
test2 = np.random.uniform(size=1000) ## randomly generate 1000 uniformally distributed data points. 
fig2 = stats.probplot(test2, dist="norm", plt=plt)



