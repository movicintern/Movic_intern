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

    # def save_png(self, instance: Setup, data):
    #     data_nm = os.path.basename(data).split('.')[0]
    #     f, t, dB = feature_extraction(data, instance)
        
    #     dB = frequency_cut(dB)

    #     # 스펙트로그램 시각화
    #     plt.pcolormesh(t, f, dB, cmap='jet')
    #     plt.title(f'{instance.sensor_nm}({data_nm + ".wav"})')
    #     plt.ylabel('Frequency (Hz)')
    #     plt.xlabel('Time (sec)')
        
    #     # 저장할 경로 생성 및 파일 저장
    #     save_path = os.path.join(
    #         instance.save_directory, instance.sensor_nm,
    #         f"Date_{instance.start_point}~{instance.end_point}", f"{data_nm}.png"
    #     )
    #     os.makedirs(os.path.dirname(save_path), exist_ok=True)
    #     plt.savefig(fname=save_path, bbox_inches=instance.bbox_inches, format=instance.file_format)
        
    #     # 플롯 클리어
    #     plt.clf()

    def save_png(self, instance, data):
        data_nm = os.path.basename(data).split('.')[0]
        f, t, dB = feature_extraction(data, instance)
        # dB = frequency_cut(dB)

        # # t1, f1의 크기를 dB1에 맞춰 조정
        # t = t[:dB.shape[1]]
        # f = f[:dB.shape[0]]
        # plt.pcolormesh(t, f, dB, cmap='jet')
        dB = np.flip(dB, axis=0)

        plt.imshow(dB, extent=[0, 3, 0, int(384000/1000/2)], cmap='jet', aspect='auto')
        plt.title(f'{instance.sensor_nm}({data_nm + ".wav"})')
        plt.ylabel('Frequency (Hz)')
        plt.xlabel('Time (sec)')
        # plt.ylim(20000, None)
        save_path = os.path.join(instance.save_directory, instance.sensor_nm, f'{data_nm}.png')
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # 그래프 저장
        plt.savefig(fname=save_path, bbox_inches='tight', format='png')
        print(save_path)
        plt.clf()
