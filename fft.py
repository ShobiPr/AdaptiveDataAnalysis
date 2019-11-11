import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from dataset import get_dataset


def fast_fourier_transform(signal):
    # Number of sample points
    N = 260
    # sample spacing
    T = 1.0 / 200
    y = signal
    yf = fft(y)
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
    plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Amplitude [mV]')
    plt.show()




signal = get_dataset()
fast_fourier_transform(signal)

print("MEAN: ", np.mean(signal))
