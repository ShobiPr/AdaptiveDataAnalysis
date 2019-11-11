# -*- coding: utf-8 -*-
from __future__ import division
from pyhht import EMD
import matplotlib.pyplot as plt
from hilbert_transform import hilbert_transform
from dataset import get_dataset

import warnings
warnings.filterwarnings("ignore")


def get_imfs(signal):
    decomposer_signal = EMD(signal)
    imfs = decomposer_signal.decompose()
    return imfs


def plot(signal, imfs):

    nIMFs = imfs.shape[0]
    print("nIMFs: ", nIMFs)
    fig = plt.subplot(nIMFs + 1, 1, 1)
    plt.plot(signal)
    plt.title('Emperical Mode Decompositoin')

    for n in range(nIMFs - 1):
        plt.subplot(nIMFs + 1, 1, n + 2)
        plt.plot(imfs[n], label="IMF %i" % (n + 1))
        plt.xlabel(' ')
        plt.legend(loc='lower right')
        plt.locator_params(axis='y', nbins=5)

    plt.subplot(nIMFs + 1, 1, nIMFs + 1)
    plt.plot(imfs[nIMFs-1],'g', label="Residual")
    plt.legend(loc='lower right')

    plt.show()

signal = get_dataset()

# Empirical Mode Decomposition
imfs = get_imfs(signal)
plot(signal, imfs)

# Hilbet Transform
sr = 200

# hilbert_transform(imfs, sr)




