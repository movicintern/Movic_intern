import os
from setup import Setup


# subfolders = [os.path.join(base_dir, d) for d in os.listdir(base_dir) 
#              if os.path.isdir(os.path.join(base_dir, d)) and start_folder <= d <= end_folder]

class DataLoader():
    def __init__(self):
        pass

    def transform_list(self, instance: Setup):
        basefolder = instance.root + instance.sensor_nm +instance.date
        st_point, ed_point = basefolder+instance.start_point, basefolder+instance.end_point
        folder_lst = [os.path.join(basefolder, d) for d in os.listdir(basefolder)
                      if os.path.isdir(os.path.join(basefolder, d)) and st_point <= d <= ed_point]
        self.folder_lst = folder_lst

# st_point와 ed_point는 파일명을 기준으로 잡는다.
# "root + sensor_nm + date + start_point" 가 시작 값 