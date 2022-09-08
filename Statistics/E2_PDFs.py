# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 16:49:04 2022

@author: lfw25
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stat

ant = pd.read_csv("Files/anthropogenic.dat").dropna()
nat = pd.read_csv("Files/natural.dat").dropna()

antDF = pd.DataFrame.to_numpy(ant)
natDF = pd.DataFrame.to_numpy(nat)

antMean = np.mean(ant)
natMean = np.mean(nat)

antVar = np.var(ant)
natVar = np.var(nat)

antStd = np.std(ant)
natStd = np.std(nat)

pVal = stat.ttest_ind(ant, nat).pvalue
fTest = stat.f_oneway(ant, nat)

antX = np.linspace(antMean - 3*antStd, antMean + 3*antStd, 100)
natX = np.linspace(natMean - 3*natStd, natMean + 3*natStd, 100)


fig,ax = plt.subplots()

ax.plot(antX, 2100000*stat.norm.pdf(antX, antMean, antStd), color = 'firebrick')
ax.plot(natX, 6350000*stat.norm.pdf(natX, natMean, natStd), color = 'dodgerblue')

ax.hist(ant, alpha=0.5, color = 'firebrick')
ax.hist(nat, alpha=0.5, color = 'dodgerblue')

#ax.tick_params(axis='both', labelleft=False, labelbottom = False)

#plt.savefig("Exercise2.pdf")

fig,ax = plt.subplots()

ax.plot(antX, stat.norm.pdf(antX, antMean, antStd), color = 'firebrick')
ax.plot(natX, stat.norm.pdf(natX, natMean, natStd), color = 'dodgerblue')

#ax.tick_params(axis='both', labelleft=False, labelbottom = False)

#plt.savefig("Exercise2Gauss.pdf")