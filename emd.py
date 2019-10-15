import numpy as np
import matplotlib.pyplot as plt
from pyhht import EMD

from scipy.signal import hilbert


timep = 3000  # Number of seconds
nsamp = 1000  # Number of samples
t = np.linspace(0, timep, nsamp)
samprate = nsamp/timep # Sample rate

s1 = np.sin(2 * np.pi * 5 * t)
s2 = np.sin(2 * np.pi * 12 * t)
s3 = np.sin(2 * np.pi * 15 * t)
s = s1 + s2 + s3

#Plot
plt.subplot(4, 1, 1)
plt.plot(t, s1)
plt.grid()
plt.subplot(4, 1, 2)
plt.plot(t, s2)
plt.grid()
plt.subplot(4, 1, 3)
plt.plot(t, s3)
plt.grid()
plt.subplot(4, 1, 4)
plt.plot(t, s)
plt.grid()
plt.show()

decomposer_signal = EMD(s)
imfs = decomposer_signal.decompose()
LEN_IMF = len(imfs)

plt.subplot(LEN_IMF+1, 1, 1)
plt.plot(s, 'g')
plt.title('Original signal')
plt.xlabel('Hz')
for n, imf in enumerate(imfs):
    plt.subplot(LEN_IMF+1, 1, n+2)
    plt.plot(imf, 'g')
    plt.title("IMF "+str(n+1))
    plt.xlabel("Hz")
plt.show()