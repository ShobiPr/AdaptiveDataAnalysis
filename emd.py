# -*- coding: utf-8 -*-
from __future__ import division
from pyhht import EMD
import matplotlib.pyplot as plt
from hilbert_transform import hilbert_transform, get_intantaneous_freq, get_marginal_freq
from dataset import get_dataset_P300

import warnings
warnings.filterwarnings("ignore")

def get_imfs(signal):
    decomposer_signal = EMD(signal)
    imfs = decomposer_signal.decompose()
    return imfs


def plot(signal, imfs):
    nIMFs = imfs.shape[0]

    plt.subplot(nIMFs + 1, 1, 1)
    plt.plot(signal, 'g', linewidth=0.75)
    plt.xticks([])
    plt.title('EMD - Subject 1')

    for n in range(nIMFs - 1):
        plt.subplot(nIMFs + 1, 1, n + 2)
        plt.plot(imfs[n], label="IMF %i" % (n + 1), linewidth=0.75)
        plt.xticks([])
        plt.legend(loc='lower right')
        plt.locator_params(axis='y', nbins=5)
        if n == 3:
            plt.ylabel('Amplitude')


    plt.subplot(nIMFs + 1, 1, nIMFs + 1)
    plt.plot(imfs[nIMFs-1],'r', label="Residual", linewidth=0.75)
    plt.legend(loc='lower right')
    plt.xlabel('Samples')
    plt.show()


# Empirical Mode Decomposition
data = get_dataset_P300()

IMFs = []
HHT = []
sr = 200
for i, signal in enumerate(data):
    IMFs.append(get_imfs(signal))


hilbert_transform(IMFs, sr)


# insFreq = get_intantaneous_freq(IMFs, sr)
# margianl_frequenci = get_marginal_freq(insFreq)
