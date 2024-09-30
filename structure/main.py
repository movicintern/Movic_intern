#%%
from setup import Setup
from dataloader import DataLoader
from visualization import Visualization
from tqdm import tqdm

sensor_name = "E0001S02"
start_point = "20240801120001"
end_point = "20240802120000"

setup_instance = Setup(sensor_nm=sensor_name, start_point=start_point, end_point=end_point)

data_loader = DataLoader()
data_files = data_loader.transform_list(setup_instance)
visualization = Visualization()

print(data_files[0])

for data_file in tqdm(data_files, desc="Processing files", unit="file"):
    setup_instance.apply(data_file)
    visualization.save_png(setup_instance, data_file)