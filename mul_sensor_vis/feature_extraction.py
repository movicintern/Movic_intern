from scipy import signal
from scipy.io import wavfile
from setup import Setup
from dataloader import DataLoader
import numpy as np
import os

def feature_extraction(data_path, instance:Setup):
    #data_path = os.path.join(instance.root, instance.sensor_nm, data[:-8], data)
    _, data = wavfile.read(data_path)
    f, t, Sxx = signal.spectrogram(x=data, fs=instance.sampling_rate,
                                    nperseg=instance.fft_size, nfft=instance.fft_size,
                                    noverlap=instance.hop_size, mode='magnitude', scaling='spectrum')

    power = Sxx**2
    dB = 10 * np.log10(power + 1e-5)
    dB = np.maximum(dB, dB.max()-80)
    return f, t, dB