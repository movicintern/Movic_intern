from scipy import signal
from setup import Setup
from dataloader import DataLoader
import numpy as np

def feature_extraction(data, instance:Setup):
    f, t, Sxx = signal.spectrogram(x=data, fs=instance.sampling_rate,
                                    nperseg=instance.fft_size, nfft=instance.fft_size,
                                    noverlap=instance.hop_size,mode='magnitude',
                                    scaling='specturm')

    power = Sxx**2
    dB = 10 * np.log10(power)
    return f, t, dB
    


# 구조가 그럼 dataloader에 리스트로 나온 값을 하나 씩 뽑아서 vis로 넘기고 그걸 저장한 다음 다시 다음 파일 적용