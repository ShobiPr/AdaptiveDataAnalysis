from scipy.fftpack import fft
import numpy as np
import matplotlib.pyplot as plt

timep = 3000  # Number of seconds
nsamp = 1000  # Number of samples
t = np.linspace(0, timep, nsamp)
samprate = nsamp/timep # Sample rate

s1 = np.sin(2 * np.pi * 5 * t)
s2 = np.sin(2 * np.pi * 12 * t)
s3 = np.sin(2 * np.pi * 15 * t)
s = s1 + s2 + s3

plt.subplot(2, 1, 1)
plt.plot(t, s)
plt.title('Signal')
plt.xlabel(' Time (s)')
plt.ylabel('Amplitude')

n = np.size(t)
fr = (nsamp/2) * np.linspace(0,1, n/2)

S = fft(s)
S_m = (2/n) * abs(S[0:np.size(fr)])

plt.subplot(2, 1, 2)
plt.plot(fr, S_m)
plt.title('Magnitude Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.tight_layout()
plt.show()
