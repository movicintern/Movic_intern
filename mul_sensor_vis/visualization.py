import matplotlib.pyplot as plt
import os
from setup import Setup
from feature_extraction import feature_extraction
import numpy as np

class Visualization:
    def __init__(self):
        pass

    def save_png(self, instance: Setup, data1, data2):
        data_nm = os.path.basename(data1).split('.')[0]
        f1, t1, dB1 = feature_extraction(data1, instance)
        f2, t2, dB2 = feature_extraction(data2, instance)

        # 스펙트로그램 시각화
        fig, axes = plt.subplots(1,2, figsize=(20, 10))
        axes[0].pcolormesh(t1, f1, dB1, cmap='jet')
        axes[0].set(title=instance.sensor_nm[0], ylabel='Frequency (Hz)', xlabel='Time (sec)')

        axes[1].pcolormesh(t2, f2, dB2, cmap='jet')
        axes[1].set(title=instance.sensor_nm[1], ylabel='Frequency (Hz)', xlabel='Time (sec)')
        
        # 저장할 경로 생성 및 파일 저장
        save_path = os.path.join(
            instance.save_directory, 'multi_sensor',
            f"Date_{instance.start_point}~{instance.end_point}", f"{data_nm}.png"
        )
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(fname=save_path, bbox_inches=instance.bbox_inches, format=instance.file_format)
        
        # 플롯 클리어
        plt.clf()

