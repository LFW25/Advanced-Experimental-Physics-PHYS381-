# -*- coding: utf-8 -*-
"""
%   Demonstration script to create some simulated data
%   and then fit a polynomial to it.


Created on Sun Jul 12 11:13:47 2020

@author: ajm226
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stat


n = 100                   # number of data points
x = np.random.ranf(n)*15-5;        # random x data values in range -5 to 10 uniformly distibuted
xx = np.arange(-5.5,10.501,0.01)       # x vector to use for plotting
p = [1, -10, -10, 20]        # polynomial coefficients


y = np.polyval(p, x)          # y data values
sigma = np.random.rand(n)*25;      # random uniformly distributed uncertainties in range 0 to 25
error=np.random.normal(0.0, 1.0, n)*sigma   # add gaussian-distributed random noise
y=y+error

realY = np.polyval(p, xx)

coeff, cov = np.polyfit(x, y, 3, cov = True)
fitY = np.polyval(coeff, xx)

chi, pVal = stat.chisquare(fitY, realY)
    

plt.figure()

plt.errorbar(x, y, xerrr=None, yerr=sigma, linestyle='none', marker='*', color = 'orange')
plt.plot(xx, realY, color = 'firebrick', linewidth = 3)
plt.plot(xx, fitY, color = 'dodgerblue', linewidth = 3)

plt.savefig("Exercise4.pdf")