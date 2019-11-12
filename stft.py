import numpy as np
import matplotlib.pyplot as plt
from dataset import get_dataset

from scipy import signal






data = get_dataset()

data_signal = data[0]





fs = 200 #Hz
N = len(data_signal)
print(N)
amp = 2 * np.sqrt(2)
time = np.arange(N) / float(fs)

# 50, 40

f, t, Zxx = signal.stft(data_signal, fs, nperseg=260, window='hamming', noverlap=240)


plt.pcolormesh(t, f, np.abs(Zxx), vmin=0, vmax=amp)
plt.title('STFT, Subject 1')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [s]')
axes = plt.gca()

axes.set_ylim([0,100])
plt.show()
