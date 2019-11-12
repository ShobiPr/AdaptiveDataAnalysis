import pywt
import matplotlib.pyplot as plt
import numpy as np
from dataset import get_dataset
import statistics as stats


def get_statistics_values(data):
    feat = []
    # For each imf compute 9 values and return it in a single vector. (5 values in this example)
    # Mean, maximum, minimum, standard deviation, variance, kurtosis, skewness, sum and median

    _mean = stats.mean(data)
    _var = np.var(data)
    _std = np.std(data)
    _max = np.max(data)
    _min = np.min(data)
    _median = stats.median(data)
    feat += [_mean, _var, _std, _max, _min, _median]
    return feat


def waveletTransformplot(signal, subject):
    labels = ['cA5', 'cd5', 'cd4', 'cd3', 'cd2', 'cd1']

    coefficients = pywt.wavedec(signal, 'sym7', level=5)
    fig, axs = plt.subplots(nrows=len(coefficients))
    print(len(coefficients))

    features = []
    axs[0].title.set_text('Decomposition of EEG signal, subject {}'.format(subject+1))
    for i in range(len(coefficients)):
        # explicitly create and save the secondary axis
        axs[i].plot(coefficients[i])
        axs[i].set_ylabel(labels[i])




    plt.show()
    return features




data = get_dataset()

for i in range(len(data)):
    waveletTransformplot(data[i], i)

