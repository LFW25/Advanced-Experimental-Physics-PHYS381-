# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 08:47:51 2022

@author: lilyw
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stat
import pandas as pd



ex3Data = pd.read_csv("Files/DAex3.dat", delimiter=' ').dropna(axis = 1).to_numpy()
varX = ex3Data[0:, 0]
varY = ex3Data[0:, 1]
varZ = ex3Data[0:, 2]

xySlope, xyInt, xyCor, xyP, xyStd = stat.linregress(varX, varY)
xzSlope, xzInt, xzCor, xzP, xzStd = stat.linregress(varX, varZ)


Xarray = np.linspace(min(varX)-5, max(varX)+5, 1000)
XYarray = xySlope*Xarray + xyInt
XZarray = xzSlope*Xarray + xzInt

fig, ax = plt.subplots()
ax.plot(Xarray, XYarray, color = 'orange')
ax.plot(Xarray, XZarray, color = 'seagreen')
ax.scatter(varX, varY, color = 'firebrick', label = 'X vs Y')
ax.scatter(varX, varZ, color = 'dodgerblue', label = 'X vs Z')

plt.show()

plt.savefig('Exercise3.pdf')