from scipy import signal
from scipy.io import wavfile
from setup import Setup
from dataloader import DataLoader
import numpy as np
import os

def feature_extraction(data_path, instance:Setup):
    from main import args
    
    if args.total_time != 3:
        data_list = []
        for _ in range(args.total_time // 3):
            _, data = wavfile.read(datapath)
            f, t, Sxx = signal.spectrogram(x=data, fs=instance.sampling_rate,
                                    nperseg=instance.fft_size, nfft=instance.fft_size,
                                    noverlap=instance.hop_size, mode='magnitude', scaling='spectrum')
            data_list.append(Sxx)
        amp = []
        for sub in data_list:
            amp.extend(sub)

        power = np.array(amp)**2
        dB = 10 * np.log10(power + 1e-5)
        dB = np.maximum(dB, dB.max()-80)
    else:
        #data_path = os.path.join(instance.root, instance.sensor_nm, data[:-8], data)
        _, data = wavfile.read(data_path)
        f, t, Sxx = signal.spectrogram(x=data, fs=instance.sampling_rate,
                                        nperseg=instance.fft_size, nfft=instance.fft_size,
                                        noverlap=instance.hop_size, mode='magnitude', scaling='spectrum')

        power = Sxx**2
        dB = 10 * np.log10(power + 1e-5)
        dB = np.maximum(dB, dB.max()-80)
    return f, t, dB