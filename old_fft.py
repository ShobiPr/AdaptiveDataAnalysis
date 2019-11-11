from scipy.fftpack import fft
import numpy as np
import matplotlib.pyplot as plt
from tftb.generators import fmlin

timep = 3000  # Number of seconds
nsamp = 1000  # Number of samples
t = np.linspace(0.0, timep, nsamp)
samprate = nsamp/timep  # Sample rate

s1 = np.sin(2 * np.pi * 5 * t)
s2 = np.sin(2 * np.pi * 12 * t)
s3 = np.sin(2 * np.pi * 15 * t)
s = s1 + s2 + s3

s_offset = s + 2  # with offset
s_white_noise = s + np.random.random(size=nsamp)  # with white noise, complex
s_linear = np.real(s*fmlin(1000, 0.05, 0.3, 50)[0])
s_offset_noise = (s + np.random.random(size=nsamp)) + 2


# discrete Fourier transform
def fast_fourier_transform(signal, t=t, nsamp=nsamp):
    sf = fft(signal)
    tf = np.linspace(0, 1/2*samprate, nsamp//2)  # , stop: 0.166, nsamp: 500

    # Plot
    fig, (ax1, ax2) = plt.subplots(nrows=2)
    ax1.plot(t, signal)
    ax1.set_ylabel('Signal')
    ax2.plot(tf, 2/nsamp * np.abs(sf[:nsamp//2]))  # the positive-frequency terms
    ax2.set_xlabel('Hz')
    plt.show()


fast_fourier_transform(s)
fast_fourier_transform(s_offset)
fast_fourier_transform(s_white_noise)
fast_fourier_transform(s_linear)
fast_fourier_transform(s_offset_noise)