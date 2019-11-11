import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert


def hilbert_transform(imfs, sr):
    for i, imf in enumerate(imfs):

        hs = hilbert(imf)  # Hilbert Transform
        ampl_s = np.abs(hs)  # Calculate amplitude
        omega_s = np.unwrap(np.angle(hs))  # Unwrap phase
        f_inst_s = np.diff(omega_s)/(2*np.pi/sr)  # Calculate instantaneous frequency
        t = np.linspace(0, 1.3, 260)

        # Plot
        fig, axs = plt.subplots(nrows=4)
        axs[0].plot(t, imf)
        axs[0].set_ylabel('Signal')
        axs[0].grid(True)
        axs[1].plot(t, omega_s)
        axs[1].set_ylabel('Phase angel')
        axs[1].grid(True)
        axs[2].plot(t, ampl_s, 'b', t, imf, 'k--', linewidth=1)
        axs[2].set_ylabel('Instantaneous Amplitude')
        axs[2].grid(True)
        axs[3].plot(t[1:], f_inst_s)
        axs[3].set_ylabel('Instantaneous frequency')
        axs[3].grid(True)
        fig.suptitle('Hilbert Transform')
        plt.show()


"""

hilbert_transform(1*np.sin(2 * np.pi * 5 * t), 'sin')

hilbert_transform(s, 'Original Signal')

hilbert_transform(s_offset, 'Signal with offset')

hilbert_transform(s_white_noise, 'Signal with white noise')

hilbert_transform(s_linear, 'Signal with linearly time varying frequency component')

hilbert_transform(s_offset_noise, 'Signal with offset and white noise')


NFFT = 1024
fig, (ax1, ax2) = plt.subplots(nrows=2)
ax1.plot(t, s)
Pxx, freqs, bins, im = ax2.specgram(s, NFFT=NFFT, Fs=samprate, noverlap=900)
plt.show()
"""