#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 13:20:30 2018

@author: Kaina
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

f = lambda x,t: 1.0/(1.0+x)
x = lambda t: -1 + np.sqrt(2.0*t+4.0)



x0, x1 = 1.0, 0.0

T = 16.0
N = 10

delta = T/N

def helper(xnplus1, xn, delta):
    return -xnplus1 + xn + 0.5*delta*((1.0/(1.0+xn))+(1.0/(1.0+xnplus1)))

def xnplus1(xn, delta):
    sol = optimize.root(helper, [xn], args=(xn, delta))
    return sol.x[0]

def trapezoid(x0, N, delta):
    tValues = [0.0]
    xValues = [x0]
    for n in np.arange(delta, N*delta+delta, delta):
        tValues.append(n)
        xValues.append(xnplus1(xValues[-1], delta))
    print xValues[-1]    
    return xValues[-1]


Nlist = [int(np.sqrt(10)**(i+2)) for i in range(9)]
errorList = []
#print Nlist

for N in Nlist:
    delta = T/N
    lastx = trapezoid(x0, N, delta)
    error = np.abs(x(16) - lastx)
    errorList.append(error)
    
ln = lambda x: np.log(x) 
print np.polyfit(ln(Nlist[2:]), ln(errorList[2:]),1)  

plt.figure(1,figsize=(20, 15))
plt.subplot(222)
plt.title('Trapezoid Method')
plt.plot(Nlist, errorList,label = 'N vs Error')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.grid(True)
plt.show
    
    
    
    
    
    
    
    
    
  