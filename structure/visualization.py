import matplotlib.pyplot as plt
import numpy as np
from setup import Setup
from scipy import signal
from scipy.io import wavfile
from feature_extraction import feature_extraction
from dataloader import DataLoader

class Visualization:
    def __init__(self):
        pass

    def save_png(self, instance:Setup):
        datas = DataLoader.folder_lst
        for num in range(len(datas)):
            _, data = wavfile.read(datas[num])
            t, f, dB = feature_extraction(data)
            plt.pcolormesh(t, f, dB)
            plt.title(instance.sensor_nm)
            plt.ylabel('Frequency(Hz)')
            plt.xlabel('Time(sec)')
            plt.savefig(fname=f'{instance.save_directory}{instance.sensor_nm}/{instance.start_point}_{instance.end_point}/{datas[num].split('/')[-1][:-4]}',
                        bbox_inches=instance.bbox_inches, format=instance.file_format)
            plt.clf()