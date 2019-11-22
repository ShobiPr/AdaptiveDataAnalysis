# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import math
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt
from scipy import signal
import warnings
warnings.filterwarnings("ignore")


def get_subdataset(_S, Sess):
    _file = 'P300/train/Data_S%02d_Sess%02d.csv' % (_S, Sess)
    _f = open(_file).readlines()
    channels = []
    for i, _rows in enumerate(_f):
        if i > 0:
            channels.append(eval(_rows))
        else:
            _headers = _rows
        if i > 11000:
            return np.array(channels)
    return np.array(channels)


def get_samples(_index, s_s_chs, sr, _size=1.3):
    return s_s_chs[_index:int(math.ceil(_index + (_size * 2*sr)))][:]


def get_dataset_P300():
    sr = 200
    data = []
    for subject in range(1, 27):  # 1
        for session in range(1, 2):  # 1
            subject_dataset = get_subdataset(subject, session)
            # first instance
            _index = [i + 1 for i, d in enumerate(subject_dataset[:, -1]) if d == 1]
            print(_index[0])
            all_channels = get_samples(_index[0], subject_dataset, sr)
            data.append(all_channels[:, 55])
            # channel O1
    return data

"""
def butter_lowpass_filter(data, cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = signal.filtfilt(b, a, data)
    return y


def butter_highpass_filter(data, cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
    y = signal.filtfilt(b, a, data)
    return y


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    y = signal.filtfilt(b, a, data)
    return y


data = get_dataset()

subject1 = data[0]
subject2 = data[1]
subject3 = data[2]

lp1 = butter_lowpass_filter(subject1, 50.0, 200)
lp2 = butter_lowpass_filter(subject2, 50.0, 200)
lp3 = butter_lowpass_filter(subject3, 50.0, 200)

hp1 = butter_highpass_filter(lp1, 0.01, 200)
hp2 = butter_highpass_filter(lp2, 0.01, 200)
hp3 = butter_highpass_filter(lp3, 0.01, 200)

b1 = butter_bandpass_filter(subject1, 0.01, 50.0, 200)
b1fix = butter_bandpass_filter(subject1, 0.01, 50.0, 200, order=4)

plt.plot(hp1, label='Subject 1')
plt.plot(hp2, label='Subject 2')
plt.plot(hp3, label='Subject 3')
plt.ylabel('Amplitude [mV]')
plt.xlabel('Samples')
plt.legend()
plt.title('Raw signals filtered')
plt.show()


#plt.plot(subject2)
plt.plot(hp1, label='lowpass + highpass')
#plt.plot(hp2, label='Subject 2')
#plt.plot(hp3, label='Subject 3')
#plt.plot(b1, label='bandpass1')
plt.plot(b1, label='order5')
plt.plot(b1fix, label='order4')
#plt.plot(b2, label='bandpass2')
plt.ylabel('Amplitude [mV]')
plt.xlabel('Samples')
plt.legend()
plt.title('Raw signals filtered')
plt.show()
"""