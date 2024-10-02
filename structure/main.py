#%%
from setup import Setup
from dataloader import DataLoader
from visualization import Visualization
from tqdm import tqdm
#3_0906140000    0924105959
#4_0906140000    0923125959
# 483,363개 데이터 존재
sensor_name = "E0001S01"
start_point = "20240906140000"
end_point = "20240909135959"


setup_instance = Setup(sensor_nm=sensor_name, start_point=start_point, end_point=end_point)

data_loader = DataLoader()
data_files = data_loader.transform_list(setup_instance)
visualization = Visualization()

print(data_files[0])

for index, data_file in tqdm(enumerate(data_files), desc="Processing files", unit="file"):
    setup_instance.apply(data_file)
    visualization.save_png(setup_instance, data_file)
    
    
    if index + 1 >= 300:
        break