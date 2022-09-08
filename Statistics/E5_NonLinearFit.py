# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 10:16:59 2022

@author: lilyw
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stat
import pandas as pd
import scipy.optimize
import pylab as plb



osloData = pd.read_csv("Files/DAex5_data1.dat", delimiter = ' ', skipinitialspace = True, skiprows = lambda x: x in range(0, 21)).dropna(axis = 1).to_numpy()
canbData = pd.read_csv("Files/DAex5_data2.dat", delimiter = ' ', skipinitialspace = True, skiprows = lambda x: x in range(0, 21)).dropna(axis = 1).to_numpy()

osloYear, osloX = osloData[0:, 0].tolist(), osloData[0:, 1:].tolist()
canbYear, canbX = canbData[0:, 0].tolist(), canbData[0:, 1:].tolist()

osloTemp = []
for i in range(len(osloX)):
    osloTemp += osloX[i]
osloTemp = osloTemp[:-2]    

canbTemp = []
for i in range(len(canbX)):
    canbTemp += canbX[i]
canbTemp = canbTemp[:-2]

##############################
## Sloped
##############################


def fit_sin(tt, yy):
    #Fit sin to the input time sequence, and return fitting parameters "amp", "omega", "phase", "offset", "freq", "period" and "fitfunc"
    tt = np.array(tt)
    yy = np.array(yy)
    ff = np.fft.fftfreq(len(tt), (tt[1]-tt[0]))   # assume uniform spacing
    Fyy = abs(np.fft.fft(yy))
    guess_freq = abs(ff[np.argmax(Fyy[1:])+1])   # excluding the zero frequency "peak", which is related to offset
    guess_amp = np.std(yy) * 2.**0.5
    guess_offset = np.mean(yy)
    guess = np.array([guess_amp, 2.*np.pi*guess_freq, 0., guess_offset, 0])

    def sinfunc(t, A, w, p, c, b):  return A * np.sin(w*t + p) + b*t + c
    popt, pcov = scipy.optimize.curve_fit(sinfunc, tt, yy, p0=guess)
    A, w, p, c, b = popt
    f = w/(2.*np.pi)
    fitfunc = lambda t: A * np.sin(w*t + p) + b*t + c
    return {"amp": A, "omega": w, "phase": p, "offset": c, "freq": f, "gradient": b, "period": 1./f, "fitfunc": fitfunc, "maxcov": np.max(pcov), "rawres": (guess,popt,pcov)}



##### Oslo

osloRes = fit_sin(range(len(osloTemp)), osloTemp)
osloXX = np.linspace(0, len(osloTemp), 5000)
osloMonths = [i for i in range(0, len(osloTemp))]

fig, ax = plt.subplots()

ax.scatter(osloMonths, osloTemp, color = 'firebrick', alpha = 0.5, marker = '.')
ax.plot(osloXX, osloRes["fitfunc"](osloXX), color = 'orange', linewidth = 1, alpha = 0.5)
plt.xlabel("Months Since 1817")
plt.ylabel("Average Temperature (deg C)")

plt.savefig("Figures/Exercise5OsloSlopedFull.svg")

fig, ax = plt.subplots()

ax.scatter(osloMonths, osloTemp, color = 'firebrick', alpha = 0.5, marker = '.')
ax.plot(osloXX, osloRes["fitfunc"](osloXX), color = 'orange', linewidth = 2, alpha = 0.7)
plt.xlabel("Months Since 1817")
plt.ylabel("Average Temperature (deg C)")
plt.xlim(450, 650)

plt.savefig("Figures/Exercise5OsloSlopedTrunc.svg")

# amp -10.679443548066253
# freq 0.08333615255723902
# gradient 0.0008706682279664362
# maxcov 0.007234390030615362
# offset 4.405784012586997
# omega 0.5236164893045206
# period 11.999594045491301
# phase 1.4894133785873147



##### Canberra

canbRes = fit_sin(range(len(canbTemp)), canbTemp)
canbXX = np.linspace(0, len(canbTemp), 5000)
canbMonths = [i for i in range(0, len(canbTemp))]

fig, ax = plt.subplots()

ax.scatter(canbMonths, canbTemp, color = 'dodgerblue', alpha = 0.5, marker = '.')
ax.plot(canbXX, canbRes["fitfunc"](canbXX), color = 'seagreen', linewidth = 2, alpha = 0.5)
plt.xlabel("Months since 1940")
plt.ylabel("Average Temperature (deg C)")

plt.savefig("Figures/Exercise5CanbSlopedFull.svg")

fig, ax = plt.subplots()

ax.scatter(canbMonths, canbTemp, color = 'dodgerblue', alpha = 0.5, marker = '.')
ax.plot(canbXX, canbRes["fitfunc"](canbXX), color = 'seagreen', linewidth = 2, alpha = 0.7)
plt.xlabel("Months since 1940")
plt.ylabel("Average Temperature (deg C)")
plt.xlim(450, 650)

plt.savefig("Figures/Exercise5CanbSlopedTrunc.svg")

# amp 7.364528672121448
# freq 0.08333065708618924
# gradient 0.0012350109841513736
# maxcov 0.007057356744071391
# offset 12.586489795394588
# omega 0.5235819602415647
# period 12.0003853919656
# phase 1.5315102102125375




#############################
## Unsloped
#############################

def fit_sin(tt, yy):
    '''Fit sin to the input time sequence, and return fitting parameters "amp", "omega", "phase", "offset", "freq", "period" and "fitfunc"'''
    tt = np.array(tt)
    yy = np.array(yy)
    ff = np.fft.fftfreq(len(tt), (tt[1]-tt[0]))   # assume uniform spacing
    Fyy = abs(np.fft.fft(yy))
    guess_freq = abs(ff[np.argmax(Fyy[1:])+1])   # excluding the zero frequency "peak", which is related to offset
    guess_amp = np.std(yy) * 2.**0.5
    guess_offset = np.mean(yy)
    guess = np.array([guess_amp, 2.*np.pi*guess_freq, 0., guess_offset])

    def sinfunc(t, A, w, p, c):  return A * np.sin(w*t + p) + c
    popt, pcov = scipy.optimize.curve_fit(sinfunc, tt, yy, p0=guess)
    A, w, p, c = popt
    f = w/(2.*np.pi)
    fitfunc = lambda t: A * np.sin(w*t + p) + c
    return {"amp": A, "omega": w, "phase": p, "offset": c, "freq": f, "period": 1./f, "fitfunc": fitfunc, "maxcov": np.max(pcov), "rawres": (guess,popt,pcov)}


#####

osloRes = fit_sin(range(len(osloTemp)), osloTemp)
osloXX = np.linspace(0, len(osloTemp), 5000)


fig, ax = plt.subplots()

ax.scatter(osloMonths, osloTemp, color = 'firebrick', alpha = 0.5, marker = '.')
ax.plot(osloXX, osloRes["fitfunc"](osloXX), color = 'orange', linewidth = 2, alpha = 0.5)
plt.xlabel("Months Since 1817")
plt.ylabel("Average Temperature (deg C)")

plt.savefig("Figures/Exercise5OsloFull.svg")

fig, ax = plt.subplots()

ax.scatter(osloMonths, osloTemp, color = 'firebrick', alpha = 0.5, marker = '.')
ax.plot(osloXX, osloRes["fitfunc"](osloXX), color = 'orange', linewidth = 2, alpha = 0.7)
plt.xlabel("Months Since 1817")
plt.ylabel("Average Temperature (deg C)")
plt.xlim(450, 650)

plt.savefig("Figures/Exercise5OsloTrunc.svg")


# amp -10.681651355305279
#freq 0.0833361993728413
#maxcov 0.003910412379842344
#offset 5.412715328095888
#omega 0.5236167834556251
#period 11.999587304504471
#phase 1.4888928930197116







#####

canbRes = fit_sin(range(len(canbTemp)), canbTemp)
canbXX = np.linspace(0, len(canbTemp), 5000)

fig, ax = plt.subplots()

ax.scatter(canbMonths, canbTemp, color = 'dodgerblue', alpha = 0.5, marker = '.')
ax.plot(canbXX, canbRes["fitfunc"](canbXX), color = 'seagreen', linewidth = 2, alpha = 0.5)
plt.xlabel("Months since 1940")
plt.ylabel("Average Temperature (deg C)")

plt.savefig("Figures/Exercise5CanbFull.svg")

fig, ax = plt.subplots()

ax.scatter(canbMonths, canbTemp, color = 'dodgerblue', alpha = 0.5, marker = '.')
ax.plot(canbXX, canbRes["fitfunc"](canbXX), color = 'seagreen', linewidth = 2, alpha = 0.7)
plt.xlabel("Months since 1940")
plt.ylabel("Average Temperature (deg C)")
plt.xlim(450, 650)

plt.savefig("Figures/Exercise5CanbTrunc.svg")

# amp 7.361485838713342
# freq 0.08333038558950709
# maxcov 0.0037435118122164687
# offset 13.103356014538988
# omega 0.5235802543776005
# period 12.000424490126438
# phase 1.532599955534938
