import numpy as np
import matplotlib.pyplot as plt
from dataset import get_subdataset, get_samples
import math

from scipy import signal



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



def get_instances_P300(_index, dataset, sampling_rate, _size=1.3):
    instances = []
    for i in _index:
        instances.append(dataset[i:int(math.ceil(i + (_size * sampling_rate)))][:])
    return np.array(instances)



def get_dataset():
    sr = 200
    data = []
    for subject in range(1, 2):  # 1
        for session in range(1, 2):  # 1
            s_s_chs = get_subdataset(subject, session)
            # first instance
            subject_dataset = get_subdataset(subject, session)
            return subject_dataset[3937-(200*2):5431+(200*2), 55]



data_signal = get_dataset()





fs = 200 #Hz
N = len(data_signal)
print(N)
amp = 2 * np.sqrt(2)
time = np.arange(N) / float(fs)

# 50, 40

f, t, Zxx = signal.stft(data_signal, fs, nperseg=2000, window='hamming', noverlap=1800)


plt.pcolormesh(t, f, np.abs(Zxx), vmin=0, vmax=amp)
plt.vlines(2, 0, 100, linestyle="dashed", colors ='r')
plt.vlines(9.47, 0, 100, linestyle="dashed", colors ='r')
plt.vlines(2+1.3, 0, 100, linestyle="dashed", colors ='r')
plt.vlines(9.47+1.3, 0, 100, linestyle="dashed", colors ='r')
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [s]')
axes = plt.gca()

axes.set_ylim([0,100])
plt.show()
