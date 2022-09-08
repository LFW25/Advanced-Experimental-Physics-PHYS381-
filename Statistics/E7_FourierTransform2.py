# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 16:15:12 2022

@author: lfw25
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stat
import pandas as pd
import scipy.optimize
import pylab as plb

data = pd.read_csv("Files/DAex7data.txt", delimiter = ' ').dropna(axis = 1).to_numpy()
days, horizVel = data[:, 0], data[:, 1]

plt.subplot(2,1,1)
plt.plot(days, horizVel, color = 'black')


# Fourier transformation converting horizVel to the frequency domain.
hvFT = np.fft.fft(horizVel)
dFT = days

# Scaling horizVel vector by (len(horizVel)).
hvFT = abs(hvFT) * 2/256

# Scaling x by (len(horizVel))/fs
# fs = sampling frequency = 240 hours = 10 days*24h each.
dFT *= 256/240

 

plt.subplot(2,1,2)

plt.axvline(12, color='firebrick', label='Semi-Diurnal Tide') # 12 Hours
plt.axvline(23.5, color='dodgerblue', label='Diurnal Tide') # 24 Hours
# Logarithmic x-axis
plt.xscale('log')
plt.plot(dFT, hvFT, color='black')

plt.savefig('Figures/Exercise7.pdf')