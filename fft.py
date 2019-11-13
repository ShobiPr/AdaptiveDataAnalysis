import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from dataset import get_dataset


def fast_fourier_transform(signal1, signal2, signal3):
    # Number of sample points
    N = 260
    # sample spacing
    T = 1.0 / 200
    y1 = signal1
    y2 = signal2
    y3 = signal3
    yf1 = fft(y1)
    yf2 = fft(y2)
    yf3 = fft(y3)
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
    plt.plot(xf, 2.0/N * np.abs(yf1[0:N//2]), label='Subject 1')
    plt.plot(xf, 2.0 / N * np.abs(yf2[0:N // 2]), label='Subject 2')
    plt.plot(xf, 2.0 / N * np.abs(yf3[0:N // 2]), label='Subject 3')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Amplitude [mV]')
    plt.legend(loc='upper right')
    plt.title('FFT')
    plt.show()

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



signal = get_dataset()
fast_fourier_transform(signal)

print("MEAN: ", np.mean(signal))
"""