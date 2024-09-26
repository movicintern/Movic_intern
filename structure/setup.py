import os

class Setup:
    def __init__(self, sensor_nm, start_point, end_point,
                 root='/home/movic/True_NAS2/PoC_SDI_03/',
                 save_directory='/home/movic/EDA/Movic_intern/structure/Result/',
                 bbox_inches='tight', file_format='png',
                 sampling_rate=384000, fft_size=4096, hop_size=2048):
        self.sensor_nm = sensor_nm
        self.start_point = start_point
        self.end_point = end_point
        
        
        ##

        self.root = root
        self.date = start_point[:-2]+"/"
        self.save_directory = save_directory
        self.sampling_rate = sampling_rate
        self.fft_size = fft_size
        self.hop_size = hop_size
        self.bbox_inches = bbox_inches
        self.file_format = file_format


    def apply(self, filename):
        folder_path = f'{self.save_directory}{self.sensor_nm}/{self.start_point}_{self.end_point}'
        os.makedirs(folder_path, exist_ok=True)
        print(f'{self.start_point}_{self.end_point} 폴더를 생성했습니다.')
        return os.path.join(folder_path, os.path.basename(filename).replace('.wav', 'png'))
    

    def get_parameters(self):
        return {
            'format': self.file_format,
            'bbox_inches': self.bbox_inches,
            'save_directory': self.save_directory,
            'fs': self.sampling_rate,
            'nperseg': self.fft_size,
            'nfft': self.fft_size,
            'noverlap': self.hop_size
        }


######## 폴더 생성 성공


if __name__ == "__main__":
    sensor_nm = 'E0001S01'
    start_point = '/home/movic/True_NAS2/PoC_SDI_03/E0001S01/2024080113'
    end_point = '/home/movic/True_NAS2/PoC_SDI_03/E0001S01/2024080211'
    # a = Setup(sensor_nm, start_point, end_point)
    print(start_point.split('True_NAS2')[-1].split('/'))
    # print(a.get_parameters()['format'])
    # a.apply("/home/movic/True_NAS2/PoC_SDI_03/E0001S01/2024080116/20240801160008.wav")