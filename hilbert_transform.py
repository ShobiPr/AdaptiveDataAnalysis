import numpy as np
import matplotlib.pyplot as plt
from tftb.generators import sigmerge, noisecg, fmlin
from scipy.signal import hilbert


timep = 3000  # Number of seconds
nsamp = 1000  # Number of samples
t = np.linspace(0, timep, nsamp)
samprate = nsamp/timep # Sample rate

s1 = np.sin(2 * np.pi * 5 * t)
s2 = np.sin(2 * np.pi * 12 * t)
s3 = np.sin(2 * np.pi * 15 * t)
s = s1 + s2 + s3

s_offset = s + 2  # with offset
# s_white_noise = sigmerge(s, noisecg(nsamp), 0)
s_white_noise = s + np.random.random(size=nsamp)  # with white noise, complex
s_linear = np.real(s*fmlin(1000, 0.05, 0.3, 50)[0])
s_offset_noise = (s + np.random.random(size=nsamp)) + 2

def hilbert_transform(signal, fig_titel):

    hs = hilbert(signal)  # Hilbert Transform
    ampl_s = np.abs(hs)  # Calculate amplitude
    omega_s = np.unwrap(np.angle(hs))  # Unwrap phase
    f_inst_s = np.diff(omega_s)/(2*np.pi/samprate)  # Calculate instantaneous frequency

    # Plot
    fig, axs = plt.subplots(nrows=4)
    axs[0].plot(t, signal)
    axs[0].set_ylabel('Signal')
    axs[0].grid(True)
    axs[1].plot(t, omega_s)
    axs[1].set_ylabel('Phase angel')
    axs[1].grid(True)
    axs[2].plot(t, ampl_s, 'b', t, signal, 'k--', linewidth=1)
    axs[2].set_ylabel('Instantaneous Amplitude')
    axs[2].grid(True)
    axs[3].plot(t[1:], f_inst_s)
    axs[3].set_ylabel('Instantaneous frequency')
    axs[3].grid(True)
    fig.suptitle(fig_titel)
    plt.show()


hilbert_transform(1*np.sin(2 * np.pi * 15 * t), 'sin')

hilbert_transform(s, 'Original Signal')

hilbert_transform(s_offset, 'Signal with offset')

hilbert_transform(s_white_noise, 'Signal with white noise')

hilbert_transform(s_linear, 'Signal with linearly time varying frequency component')

hilbert_transform(s_offset_noise, 'Signal with offset and white noise')


# -------------------------------------------

"""
NFFT = 1024
fig, (ax1, ax2) = plt.subplots(nrows=2)
ax1.plot(t, s)
Pxx, freqs, bins, im = ax2.specgram(s, NFFT=NFFT, Fs=samprate, noverlap=900)
plt.show()
"""