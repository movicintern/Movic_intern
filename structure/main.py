#%%
from scipy import signal
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
from setup import Setup

data_path = '/home/movic/True_NAS2/PoC_SDI_03/E0001S03/2024080219/20240802190036.wav'
_, data = wavfile.read(data_path)
f, t, Sxx = signal.spectrogram(x=data, fs=384000, nperseg=4096, nfft=4096, noverlap=2048, mode='magnitude', scaling='spectrum')
power = Sxx**2
dB = 10*np.log10(power)
plt.pcolormesh(t, f, dB, cmap='seismic')
plt.title('E0001S03')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()
# plt.savefig(fname=f'{Setup.save_directory}{Setup.sensor_nm}/{Setup.start_point}_{Setup.end_point}/{data_paths[i].split('/')[-1][:-4]}')