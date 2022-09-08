# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 15:18:14 2022

@author: lfw25
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stat



sampleA = np.genfromtxt("Files/SampleA.dat", delimiter=',',skip_header=1) # Read in data A
sampleB = np.genfromtxt("Files/SampleB.dat", delimiter=',',skip_header=1) # Read in data B

sampleAMean = np.mean(sampleA)
sampleBMean = np.mean(sampleB)

sampleAVar = np.var(sampleA)
sampleBVar = np.var(sampleB)

sampleAStd = np.std(sampleA)
sampleBStd = np.std(sampleB)

pVal = stat.ttest_ind(sampleA, sampleB).pvalue
fTest = stat.f_oneway(sampleA, sampleB)

Ax = np.linspace(sampleAMean - 3*sampleAStd, sampleAMean + 3*sampleAStd, 100)
Bx = np.linspace(sampleBMean - 3*sampleBStd, sampleBMean + 3*sampleBStd, 100)

fig,ax = plt.subplots()

ax.plot(Ax, 105*stat.norm.pdf(Ax, sampleAMean, sampleAStd), color = 'firebrick')
ax.plot(Ax, 135*stat.norm.pdf(Bx, sampleBMean, sampleBStd), color = 'dodgerblue')
ax.hist(sampleA, alpha=0.5, label='Sample A', color = 'firebrick')
ax.hist(sampleB, alpha=0.5, label='Sample B', color = 'dodgerblue')
ax.tick_params(
axis='both',
labelleft=False,
labelbottom = False)
plt.show()

plt.savefig("Exercise1.pdf")