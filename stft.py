import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from tftb.generators import fmlin
from tftb.processing import ShortTimeFourierTransform


timep = 3000  # Number of seconds
nsamp = 1000  # Number of samples,  t# he length of the windowing segments
t = np.linspace(0, timep, nsamp)
samprate = nsamp/timep  # Sampling rate

s1 = np.sin(2 * np.pi * 5 * t)
s2 = np.sin(2 * np.pi * 12 * t)
s3 = np.sin(2 * np.pi * 15 * t)
s = s1 + s2 + s3

s_offset = s + 2  # with offset
s_white_noise = s + np.random.random(size=nsamp)  # with white noise, complex
s_linear = np.real(s*fmlin(1000, 0.05, 0.3, 50)[0])
s_offset_noise = (s + np.random.random(size=nsamp)) + 2


def stft(signal, t=t, nsamp=nsamp):
    fig, (ax1, ax2) = plt.subplots(nrows=2)
    ax1.plot(t, s)
    ax1.set_ylabel('Signal')
    # Pxx : the periodogram, freqs: frequency vector, bins: the centers of the time bins
    Pxx, freqs, bins, im = ax2.specgram(s, NFFT=nsamp, Fs=samprate, noverlap=900)
    ax2.set_ylabel('Hz')
    plt.show()


stft(s)
stft(s_offset)
stft(s_white_noise)
stft(s_linear)
stft(s_offset_noise)
