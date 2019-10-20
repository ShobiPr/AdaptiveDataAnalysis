import numpy as np
import matplotlib as plt
from tftb.processing import ShortTimeFourierTransform


timep = 3000  # Number of seconds
nsamp = 1000  # Number of samples
t = np.linspace(0, timep, nsamp)
samprate = nsamp/timep # Sample rate

s1 = np.sin(2 * np.pi * 5 * t)
s2 = np.sin(2 * np.pi * 12 * t)
s3 = np.sin(2 * np.pi * 15 * t)
s = s1 + s2 + s3

stft = ShortTimeFourierTransform(s)
stft.run()
stft.plot()