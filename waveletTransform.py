import pywt
import matplotlib.pyplot as plt
import numpy as np
from dataset import get_dataset





def waveletTransform(signal):
    labels = ['cA4', 'cd4', 'cd3', 'cd2', 'cd1']

    plt.subplot(521)
    plt.title('Decomposition of EEG signal')
    coefficients = pywt.wavedec(signal, 'sym7')
    fig, axs = plt.subplots(nrows=len(coefficients))

    features = []

    for i in range(len(coefficients)):
        axs[i].plot(coefficients[i])
        axs[i].set_ylabel(labels[i])

        features.append(instantaneous_energy(coefficients[i]))
        features.append(teager_energy(coefficients[i]))
    plt.show()
    return features


def teager_energy(data):
    sum_values = sum(abs(data[x] ** 2) if x == 0
                     else abs(data[x] ** 2 - data[x - 1] * data[x + 1])
                     for x in range(0, len(data) - 1))
    return np.log10((1 / float(len(data))) * sum_values)


def instantaneous_energy(data):
    return np.log10((1 / float(len(data))) * sum(i ** 2 for i in data))



signal = get_dataset()
print(waveletTransform(signal))