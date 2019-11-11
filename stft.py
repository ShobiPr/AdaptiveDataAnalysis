import numpy as np
import matplotlib.pyplot as plt
from dataset import get_subdataset, get_samples
import math



def stft(signal, window):
    # Number of sample points
    N = len(signal)
    # sample spacing
    T = 1.0 / 200
    y = signal

    # Pxx : the periodogram, freqs: frequency vector, bins: the centers of the time bins
    Pxx, freqs, bins, im = plt.specgram(signal, NFFT=N, Fs=200, noverlap=window)
    plt.xlabel('Time [s]')
    plt.ylabel('Frequency [Hz]')
    plt.show()

def get_samples_stft(_index, s_s_chs, sr, _size=1.3):
    return s_s_chs[_index-200*3:int(math.ceil(_index + (_size * sr))) + 200][:]


def get_dataset():
    sr = 200
    for subject in range(1, 2):  # 1
        for session in range(1, 2):  # 1
            s_s_chs = get_subdataset(subject, session)
            # first instance
            _index = 3937
            data = get_samples_stft(_index, s_s_chs, sr)
            # channel O1
            return data[:, 55]

data_signal = get_dataset()



from scipy import signal


fs = 200 #Hz
N = len(data_signal)
print(N)
amp = 2 * np.sqrt(2)
time = np.arange(N) / float(fs)

# 50, 40

f, t, Zxx = signal.stft(data_signal, fs, nperseg=1000, window='hamming', noverlap=950)
plt.pcolormesh(t, f, np.abs(Zxx), vmin=0, vmax=amp,)
plt.vlines(3, 0, 100, linestyle="dashed", colors = 'r')
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [s]')
axes = plt.gca()

axes.set_ylim([0,100])
plt.show()
