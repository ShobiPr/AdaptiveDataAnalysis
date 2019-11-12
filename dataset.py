# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import math
import warnings

warnings.filterwarnings("ignore")


def get_subdataset(_S, Sess):
    _file = 'Data_S%02d_Sess%02d.csv' % (_S, Sess)
    _f = open(_file).readlines()
    channels = []
    for i, _rows in enumerate(_f):
        if i > 0:
            channels.append(eval(_rows))
        else:
            _headers = _rows
        if i > 11500:
            return np.array(channels)
    return np.array(channels)


def get_samples(_index, s_s_chs, sr, _size=1.3):
    return s_s_chs[_index:int(math.ceil(_index + (_size * sr)))][:]


def get_dataset():
    sr = 200
    data = []
    for subject in range(1, 4):  # 1
        for session in range(1, 2):  # 1
            subject_dataset = get_subdataset(subject, session)
            # first instance
            _index = [i + 1 for i, d in enumerate(subject_dataset[:, -1]) if d == 1]
            print(_index[0])
            all_channels = get_samples(_index[0], subject_dataset, sr)
            data.append(all_channels[:,55])
            # channel O1
    return data
