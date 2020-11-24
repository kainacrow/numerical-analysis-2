#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 20:29:01 2018

@author: Kaina
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

f = lambda x: 1.0/(1.0+x)
x = lambda t: -1 + np.sqrt(2.0*t+4.0)



x0, x1 = 1.0, 0.0

T = 16.0
N = 10

delta = T/N

def RK4(xn, delta):
    z1 = 1.0/(1.0+xn)
    z2 = 1.0/(1.0+xn+z1*delta/2)
    z3 = 1.0/(1.0+xn+z2*delta/2)
    z4 = 1.0/(1.0+xn+z3*delta)
    xnplus1 = xn + (delta/6)*(z1+2*z2+2*z3+z4)
    return xnplus1

def trapezoid(x0, N, delta):
    tValues = [0.0]
    xValues = [x0]
    for n in np.arange(0, T, delta):
        tValues.append(n)
        xValues.append(RK4(xValues[-1], delta))  
    #print xValues[-1]
    return xValues[-1]

Nlist = [int(np.sqrt(10)**(i+2)) for i in range(9)]
errorList = []
#print Nlist

for N in Nlist:
    delta = T/N
    lastx = trapezoid(x0, N, delta)
    print lastx
    error = np.abs(x(16) - lastx)
    #print x(16)
    errorList.append(error)
    
ln = lambda x: np.log(x) 
print np.polyfit(ln(Nlist[1:5]), ln(errorList[1:5]),1)  

plt.figure(1,figsize=(20, 15))
plt.subplot(222)
plt.title('Trapezoid Method')
plt.plot(Nlist, errorList,label = 'N vs Error')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.grid(True)
plt.show
    
    
    
    
    
    
    
    
    
  