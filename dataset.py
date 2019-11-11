# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import math
import warnings

warnings.filterwarnings("ignore")


def get_subdataset(_S=1, Sess=1):
    _file = 'Data_S%02d_Sess%02d.csv' % (_S, Sess)
    _f = open(_file).readlines()
    channels = []
    for i, _rows in enumerate(_f):
        if i > 0:
            channels.append(eval(_rows))
        else:
            _headers = _rows
        if i > 4500:
            return np.array(channels)
    return np.array(channels)


def get_samples(_index, s_s_chs, sr, _size=1.3):
    return s_s_chs[_index:int(math.ceil(_index + (_size * sr)))][:]


def get_feedback_signal():
    sr = 200
    for subject in range(1, 2):  # 1
        for session in range(1, 2):  # 1
            s_s_chs = get_subdataset(subject, session)
            # first instance
            _index = 3937
            data = get_samples(_index, s_s_chs, sr)
            # channel O1
            return data[:, 55]


def get_feedback_signal():
    sr = 200
    for subject in range(1, 2):  # 1
        for session in range(1, 2):  # 1
            s_s_chs = get_subdataset(subject, session)
            # first instance
            _index = 3937
            data = get_samples(_index, s_s_chs, sr)
            # channel O1
            return data[:, 55]


def get_resting_signal():
    sr = 200
    for subject in range(1, 2):  # 1
        for session in range(1, 2):  # 1
            s_s_chs = get_subdataset(subject, session)
            # first instance
            _index = 3937 - 200*2
            data = get_samples(_index, s_s_chs, sr)
            # channel O1
            return data[:, 55]