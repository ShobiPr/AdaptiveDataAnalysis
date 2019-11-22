import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from scipy import signal
from dataset import get_dataset_P300
from scipy.signal import iirfilter, lfilter
from scipy.signal import butter

"""
data = get_dataset()
subject1 = data[0]
subject2 = data[1]
subject3 = data[2]

data_signal1 = butter_highpass_filter(subject1, 0.01, 200, order=5)
signal_filtered1 = butter_lowpass_filter(data_signal1, 50.0, 200)

data_signal2 = butter_highpass_filter(subject2, 0.01, 200, order=5)
signal_filtered2 = butter_lowpass_filter(data_signal2, 50.0, 200)

data_signal3 = butter_highpass_filter(subject3, 0.01, 200, order=5)
signal_filtered3 = butter_lowpass_filter(data_signal3, 50.0, 200)

fast_fourier_transform(signal_filtered1, signal_filtered2, signal_filtered3)
"""
def butter_bandpass_filter(data, lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    y = signal.filtfilt(b, a, data)
    return y

def notch_filter(s, sr, f0=50, Q=10.0):
    b, a = signal.iirnotch(f0, Q, sr)
    return signal.filtfilt(b, a, s)


def fast_fourier_transform(data, sr, sampling):
    # Number of sample points
    N = sampling
    # sample spacing
    T = 1.0 / sr
    for i, signal in enumerate(data):
        n = notch_filter(signal, sr)
        y = butter_bandpass_filter(n, 0.5, 70.0, sr, order=4)
        yf = fft(y)
        xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)
        plt.plot(xf, 2.0 / N * np.abs(yf[0:N // 2]), label='subject {0}'.format(i+1))
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Amplitude [mV]')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.grid()
    plt.title('FFT on filtered P300')
    plt.show()


data = get_dataset_P300()
sr = 200
sampling = 260
fast_fourier_transform(data, sr, sampling)
