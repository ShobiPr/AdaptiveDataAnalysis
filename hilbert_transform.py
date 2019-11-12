import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert


def hilbert_transform(IMFs, sr):

    for s, imfs in enumerate(IMFs):
        nIMFs = 5

        for i, imf in enumerate(imfs):
            if 1 <= i <= nIMFs:
                hs = hilbert(imf)  # Hilbert Transform
                ampl_s = np.abs(hs)  # Calculate amplitude
                omega_s = np.unwrap(np.angle(hs))  # Unwrap phase
                f_inst_s = np.diff(omega_s) / (2 * np.pi / sr)  # Calculate instantaneous frequency
                t = np.linspace(0, 1.3, 260)

                plt.subplot(nIMFs, 1, i)
                if i == 1:
                    plt.title('Comparing Instantaneous Frequencies')
                plt.plot(t[1:], f_inst_s, label="Subject %i" % (s + 1), linewidth=0.75)
                plt.xticks([])
                plt.locator_params(axis='y', nbins=5)
                if i == 3:
                    plt.ylabel('Ins. Freq. [Hz]')

    plt.xlabel('Time [s]')
    plt.legend(loc='lower right')
    plt.show()

# label="Subject %i" % (i + 1)