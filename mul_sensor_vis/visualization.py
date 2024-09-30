import matplotlib.pyplot as plt
import os
from setup import Setup
from feature_extraction import feature_extraction
import numpy as np

def frequency_cut(data, low_cut=20000, high_cut = 80000):
    """
    data (H, W) -> data (H[low_cut ~ high_cut], W)
    return data(H,W)
    """
    unit = 2049/192000
    data = data[int(unit*low_cut) : int(unit*high_cut), :]
    return data

class Visualization:
    def __init__(self):
        pass

    def save_png(self, instance: Setup, data1, data2):
        data_nm = os.path.basename(data1).split('.')[0]
        f1, t1, dB1 = feature_extraction(data1, instance)
        f2, t2, dB2 = feature_extraction(data2, instance)


        dB1 = frequency_cut(dB1)
        dB2 = frequency_cut(dB2)

        
        # 스펙트로그램 시각화
        fig, axes = plt.subplots(1,2, figsize=(20, 10))
        t1 = t1[:dB1.shape[1]]
        f1 = f1[:dB1.shape[0]]
        axes[0].pcolormesh(t1, f1, dB1, cmap='jet')
        axes[0].set(title=instance.sensor_nm[0], ylabel='Frequency (Hz)', xlabel='Time (sec)')

        # t2, f2의 크기를 dB2에 맞춰 조정
        t2 = t2[:dB2.shape[1]]
        f2 = f2[:dB2.shape[0]]
        axes[1].pcolormesh(t2, f2, dB2, cmap='jet')
        axes[1].set(title=instance.sensor_nm[1], ylabel='Frequency (Hz)', xlabel='Time (sec)')

        # 저장 경로 설정
        save_path = os.path.join(instance.save_directory, f'multi_sensor/Date_{instance.start_point}~{instance.end_point}', f'{instance.sensor_nm[0]}_vs_{instance.sensor_nm[1]}.png')
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # 그래프 저장
        plt.savefig(fname=save_path, bbox_inches='tight', format='png')
        plt.clf()