import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert


def hilbert_transform(IMFs, sr):
    instantaneous_freq = []
    for s, imfs in enumerate(IMFs):
        nIMFs = 6

        for i, imf in enumerate(imfs):
            if i < nIMFs:
                hs = hilbert(imf)  # Hilbert Transform
                ampl_s = np.abs(hs)  # Calculate amplitude
                omega_s = np.unwrap(np.angle(hs))  # Unwrap phase
                f_inst_s = np.diff(omega_s) / (2 * np.pi / sr)  # Calculate instantaneous frequency
                instantaneous_freq.append(f_inst_s)
                t = np.linspace(0, 1.3*2, 260*2)

                plt.subplot(nIMFs, 1, i+1)
                if i == 0:
                    plt.title('Comparing Instantaneous Frequencies')
                plt.plot(t[1:], f_inst_s, label="Subject %i" % (s + 1), linewidth=0.75)
                plt.xticks([])
                plt.locator_params(axis='y', nbins=5)
                if i == 3:
                    plt.ylabel('Ins. Freq. [Hz]')

    plt.xlabel('Time [s]')
    # plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()

def get_intantaneous_freq(IMFs, sr):
    instantaneous_freq = []
    for s, imfs in enumerate(IMFs):
        insfreq = []
        for i, imf in enumerate(imfs):
            if 2 <= i <= 3:
                hs = hilbert(imf)  # Hilbert Transform
                ampl_s = np.abs(hs)  # Calculate amplitude
                omega_s = np.unwrap(np.angle(hs))  # Unwrap phase
                f_inst_s = np.diff(omega_s) / (2 * np.pi / sr)  # Calculate instantaneous frequency
                insfreq += [f_inst_s]
        instantaneous_freq.append(insfreq)
    return instantaneous_freq

def get_marginal_freq(instFreq):
    marginal_fre = []
    for i, sub in enumerate(instFreq):
        freq = []
        for j, fr in enumerate(sub):
            s = sum(fr)
            freq += [s]
        marginal_fre.append(freq)
    return marginal_fre