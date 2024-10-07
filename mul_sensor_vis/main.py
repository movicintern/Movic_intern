#%%
from setup import Setup
from dataloader import DataLoader
from visualization import Visualization
from tqdm import tqdm
from multiprocessing import Pool
from concurrent.futures import ProcessPoolExecutor
import os

print(os.cpu_count())

def process_file(args):
    setup_instance, data_file1, data_file2 = args
    setup_instance.apply(data_file1)
    visualization.save_png(setup_instance, data_file1, data_file2)




import argparse
parser = argparse.ArgumentParser(description="Set Arguments")
parser.add_argument('--root', type=str, required=True, help='data path')
parser.add_argument('--save_directory', type=str, required=True, help='save dir')
parser.add_argument('--sensor_name', type=str, required=True, nargs='+', help='sensor name(s)')
parser.add_argument('--start_point', type=str, required=True, help='start point for the extraction')
parser.add_argument('--end_point', type=str, required=True, help='end point for the extraction')
parser.add_argument('--total_time', type=int, required=True, help='total time of spectrogram')

args = parser.parse_args()


#sensor_name__ = ["E0001S01", "E0001S02"]


setup_instance = Setup(root = args.root, save_directory=args.save_directory, sensor_nm=args.sensor_name, start_point=args.start_point, end_point=args.end_point, folder=args.root.split('/')[-1])
# args.root.split('/')[-1]
# start_point = 20240908045923

# sensor_name = ["E0001S01", "E0001S02"]
# start_point = "20240906140000"
# start_point = "20240906141600"
# end_point = "20240909135959"
# setup_instance = Setup(sensor_nm=sensor_name, start_point=start_point, end_point=end_point)

data_loader = DataLoader()
all_data_files = data_loader.transform_list(setup_instance)
visualization = Visualization()

data_file1 = all_data_files[0]
data_file2 = all_data_files[1]

data_file1.sort()
data_file2.sort()

# nohup python main.py > 로그저장할파일이름.out &

# resume_index = 20914 + 504 + 24282# 재개할 인덱스

num_files = len(data_file1)

# 멀티프로세싱을 위한 인자 준비
arguments = [(setup_instance, data_file1[num], data_file2[num]) for num in range(len(data_file1))]

# ProcessPoolExecutor 실행
with ProcessPoolExecutor(max_workers=os.cpu_count() - 2) as executor:
    futures = []

    for i in range(num_files // 3):
        start_index = i * 3
        end_index = min(start_index + 3, num_files) 
      
        for j in range(start_index, end_index):
            futures.append(executor.submit(process_file, setup_instance, data_file1[j], data_file2[j]))

    if num_files % 3 != 0:
        for j in range((num_files // 3) * 3, num_files):
            futures.append(executor.submit(process_file, setup_instance, data_file1[j], data_file2[j]))

    for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc="Processing files"):
        future.result()
# %%
