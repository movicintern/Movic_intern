from setup import Setup
import os

class DataLoader:
    def __init__(self):
        pass

    def transform_list(self, instance: Setup):
        base_dir = os.path.join(instance.root, instance.sensor_nm)
        subfolders = [
            os.path.join(base_dir, d) 
            for d in os.listdir(base_dir) 
            if os.path.isdir(os.path.join(base_dir, d)) and 
            f"{d}" >= instance.start_point and f"{d}" <= instance.end_point
        ]
        wav_files = [
            file    
            for subfolder in subfolders 
            for _, _, files in os.walk(subfolder) 
            for file in files 
            if file.endswith('.wav')
        ]
        return wav_files