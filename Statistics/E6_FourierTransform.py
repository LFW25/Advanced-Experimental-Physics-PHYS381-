# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 14:00:27 2022

@author: lfw25
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stat
import pandas as pd
import scipy.optimize
import pylab as plb


samplingFreq = np.arange(1, 70, 0.01)
peakPos = []

for rate in samplingFreq:
    fs = rate # sampling frequency (Hz)

    ts = 1/fs # set sampling rate and interval
    period=10.0 #sampling period
    nfft = period/ts # length of DFT
    t=np.arange(0,period,ts)
    #h = ((1.7)*np.sin((2*np.pi*35.0*t)-0.6) + (2.5)*np.random.normal(0.0,1.0,t.shape)) 
    h = ((1.3)*np.sin(2*np.pi*5.0*t) + (1.7)*np.sin((2*np.pi*35.0*t)-0.6) + (2.5)*np.random.normal(0.0,1.0,t.shape))          
    # combination of a 5 Hz signal a 35Hz signal and Gaussian noise
    
    H = np.fft.fft(h) # determine the Discrte Fourier Transform
    
    
    # Take the magnitude of fft of H
    mx = abs(H[0:int(nfft/2)])*(2.0/nfft)  # note only need to examien first half of spectrum

    
    # Frequency vector
    f = np.arange(0,int(nfft/2))*fs/nfft
    
    mxList = list(mx)
    maxAmp = max(mxList)
    maxAmpInd = mxList.index(maxAmp)
    fAtMaxAmp = f[maxAmpInd]
    
    peakPos.append(fAtMaxAmp)



plt.figure(1)
plt.scatter(samplingFreq, peakPos, color = 'firebrick', marker = '.', alpha = 0.5)
#plt.ylabel("Sampling Frequency (Hz)")
#plt.xlabel("Peak Position")
#plt.savefig('Figures/Exercise6PeakGuess.pdf')


#plt.figure(2)
#plt.plot(t,h);
#plt.title('Sine Wave Signals');
#plt.xlabel('Time (s)');
#plt.ylabel('Amplitude');

# =============================================================================
# samplingFreq = [75]
# for rate in samplingFreq:
#     fs = rate # sampling frequency (Hz)
# 
#     ts = 1/fs # set sampling rate and interval
#     period=10.0 #sampling period
#     nfft = period/ts # length of DFT
#     t=np.arange(0,period,ts)
#     h = ((1.7)*np.sin((2*np.pi*35.0*t)-0.6) + (2.5)*np.random.normal(0.0,1.0,t.shape)) 
#     #h = ((1.3)*np.sin(2*np.pi*5.0*t) + (1.7)*np.sin((2*np.pi*35.0*t)-0.6) + (2.5)*np.random.normal(0.0,1.0,t.shape))          
#     # combination of a 5 Hz signal a 35Hz signal and Gaussian noise
#     
#     H = np.fft.fft(h) # determine the Discrte Fourier Transform
#     
#     
#     # Take the magnitude of fft of H
#     mx = abs(H[0:np.int(nfft/2)])*(2.0/nfft)  # note only need to examien first half of spectrum
# 
#     
#     # Frequency vector
#     f = np.arange(0,np.int(nfft/2))*fs/nfft
# 
# 
#     plt.figure(3)
#     plt.plot(f,mx, color = 'firebrick')
#     #plt.title('Amplitude Spectrum of Sine Wave signals');
#     #plt.xlabel('Frequency (Hz)');
#     #plt.ylabel('Amplitude');
#     plt.xlim(0, max(samplingFreq)/2)
#     #plt.ylim(1, 2.5)
#     plt.savefig('Figures/Exercise6Amp35.pdf')
# =============================================================================
