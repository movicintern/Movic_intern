from setup import Setup
import os

class DataLoader:
    def __init__(self):
        pass

    def transform_list(self, instance: Setup):
        all_wav_files = []

        for num in range(len(instance.sensor_nm)):
            base_dir = os.path.join(instance.root, instance.sensor_nm[num])
            wav_files = [] 

            for d in os.listdir(base_dir):
                if os.path.isdir(os.path.join(base_dir, d)) and f"{d}" >= instance.start_point and f"{d}" <= instance.end_point:
                    subfolder = os.path.join(base_dir, d)

                    for _, _, files in os.walk(subfolder):
                        for file in files:
                            if file.endswith('.wav'):
                                wav_files.append(os.path.join(subfolder, file))
                                
            all_wav_files.append(wav_files)

        return all_wav_files
        