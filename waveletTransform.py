import pywt
import matplotlib.pyplot as plt
import numpy as np
from dataset import get_dataset





def waveletTransform(instance):
    features = []
    fig, axs = plt.subplots(2)
    fig.suptitle('Decomposition of EEG signal')
    coefficients = pywt.wavedec(instance, 'sym7')
    for i in range(len(coefficients)):
        axs[i].plot(coefficients)

    return 0



def waveletFeatures():
    return 0




data = get_dataset()
# waveletTransform(data)