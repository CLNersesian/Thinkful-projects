# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 22:52:48 2015

@author: carolynsfolder
"""

for x in xrange(1, 100):
    if x % 15==0:
        print "FizzBuzz"
    if x % 3==0:
        print "Fizz"
    if x % 5==0:
        print "Buzz"
    else:
        print x
        

