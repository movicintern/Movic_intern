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

    def save_png(self, instance: Setup, data):
        data_nm = os.path.basename(data).split('.')[0]
        f, t, dB = feature_extraction(data, instance)
        
        dB = frequency_cut(dB)

        # 스펙트로그램 시각화
        plt.pcolormesh(t, f, dB, cmap='jet')
        plt.title(instance.sensor_nm)
        plt.ylabel('Frequency (Hz)')
        plt.xlabel('Time (sec)')
        
        # 저장할 경로 생성 및 파일 저장
        save_path = os.path.join(
            instance.save_directory, instance.sensor_nm,
            f"Date_{instance.start_point}~{instance.end_point}", f"{data_nm}.png"
        )
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(fname=save_path, bbox_inches=instance.bbox_inches, format=instance.file_format)
        
        # 플롯 클리어
        plt.clf()

