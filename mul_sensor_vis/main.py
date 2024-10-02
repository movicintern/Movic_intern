#%%
from setup import Setup
from dataloader import DataLoader
from feature_extraction import feature_extraction
from visualization import Visualization
from tqdm import tqdm
from multiprocessing import Pool
from concurrent.futures import ProcessPoolExecutor
import os

print(os.cpu_count())


def frequency_cut(data, low_cut=20000, high_cut = 500000):
    """
    data (H, W) -> data (H[low_cut ~ high_cut], W)
    return data(H,W)
    """
    unit = 2049/192000
    data = data[int(unit*low_cut) :  :]
    return data

def process_file(args):
    setup_instance, data_file1, data_file2 = args
    setup_instance.apply(data_file1)
    visualization.save_png(setup_instance, data_file1, data_file2)


sensor_name = ["E0001S01", "E0001S02"]
start_point = "20240906140000"
end_point = "20240909135959"
setup_instance = Setup(sensor_nm=sensor_name, start_point=start_point, end_point=end_point)

data_loader = DataLoader()
all_data_files = data_loader.transform_list(setup_instance)
visualization = Visualization()


data_file1 = all_data_files[0]
data_file2 = all_data_files[1]

data_file1.sort()
data_file2.sort()

resume_index = 20914 + 504 # 재개할 인덱스

# 멀티프로세싱을 위한 인자 준비
args = [(setup_instance, data_file1[num], data_file2[num]) for num in range(len(data_file1))]

# ProcessPoolExecutor 실행
with ProcessPoolExecutor(max_workers=os.cpu_count() - 2) as executor:
    # 인덱스 범위를 조정하여 재개
    for _ in tqdm(executor.map(process_file, args[resume_index:]), total=len(args) - resume_index, desc="Processing files", unit="file"):
        pass
#%%