from scipy.fftpack import fft
import numpy as np
import matplotlib.pyplot as plt

timep = 3000  # Number of seconds
nsamp = 1000  # Number of samples
t = np.linspace(0.0, timep, nsamp)
samprate = nsamp/timep  # Sample rate

s1 = np.sin(2 * np.pi * 5 * t)
s2 = np.sin(2 * np.pi * 12 * t)
s3 = np.sin(2 * np.pi * 15 * t)
s = s1 + s2 + s3

sf = fft(s)
tf = np.linspace(0, 1/2*samprate, nsamp//2)

fig, ax = plt.subplots()
ax.plot(tf, 2/nsamp * np.abs(sf[:nsamp//2]))
plt.show()