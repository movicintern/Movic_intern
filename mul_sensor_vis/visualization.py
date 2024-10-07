import matplotlib.pyplot as plt
import os
from setup import Setup
from feature_extraction import feature_extraction
import numpy as np

def frequency_cut(data, low_cut=20000, high_cut = 500000):
    unit = 2049/192000
    data = data[int(unit*low_cut):, :]
    return data

class Visualization:
    def __init__(self):
        pass


    def save_png(self, instance: Setup, data1, data2):
        from main import args
        data_nm1 = os.path.basename(data1).split('.')[0]
        data_nm2 = os.path.basename(data2).split('.')[0]
        
        f1, t1, dB1 = feature_extraction(data1, instance)
        f2, t2, dB2 = feature_extraction(data2, instance)

        #dB1 = frequency_cut(dB1)
        #dB2 = frequency_cut(dB2)

        # 스펙트로그램 시각화
        fig, axes = plt.subplots(1, 2, figsize=(20,10))
        
        dB1 = np.flip(dB1, axis=0)
        axes[0].imshow(dB1, extent=[0, args.total_times, 0, int(384000 / 1000 / 2)], cmap='jet', aspect='auto')
        axes[0].set(title=f'{instance.sensor_nm[0]} ({data_nm1}.wav)', ylabel='Frequency (Hz)', xlabel='Time (sec)')
        
        dB2 = np.flip(dB2, axis=0)
        axes[1].imshow(dB2, extent=[0, args.total_times, 0, int(384000 / 1000 / 2)], cmap='jet', aspect='auto')
        axes[1].set(title=f'{instance.sensor_nm[1]} ({data_nm2}.wav)', ylabel='Frequency (Hz)', xlabel='Time (sec)')

        save_path = os.path.join(instance.save_directory, f'{instance.folder}/Date_{instance.start_point}~{instance.end_point}', f'{instance.sensor_nm[0]}_{instance.sensor_nm[1]}/{data_nm1}_{data_nm2}.png')
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        plt.savefig(fname=save_path, bbox_inches='tight', format='png')
        plt.close()
