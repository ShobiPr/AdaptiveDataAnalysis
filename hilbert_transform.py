import numpy as np
import matplotlib.pyplot as plt

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

# Hilbert Transform

hs = hilbert(s1)

#Plot in complex plane
plt.plot(np.real(hs), np.imag(hs))
plt.grid()
plt.show()

#Unwrap instantaneous frequency
omega_s = np.unwrap(np.angle(hs))

# Calculate and plot amplitude
ampl_1 = np.abs(hs)

plt.grid()
plt.plot(t, ampl_1)
plt.show()

# Calculate and plot instantaneous frequency
f_inst_s = np.diff(omega_s)/(2*np.pi/samprate)

plt.grid()
plt.plot(t[1:], f_inst_s)
plt.show()