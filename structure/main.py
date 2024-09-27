#%%
from setup import Setup
from dataloader import DataLoader
from feature_extraction import feature_extraction
from visualization import Visualization
from tqdm import tqdm

def frequency_cut(data, low_cut=20000, high_cut = 80000):
    """
    data (H, W) -> data (H[low_cut ~ high_cut], W)
    return data(H,W)
    """
    unit = 2049/192000
    data = data[int(unit*low_cut) : int(unit*high_cut), :]
    return data

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
    
    f, t, dB = feature_extraction(data_file, setup_instance)
    dB = frequency_cut(dB)
    visualization.save_png(setup_instance, data_file)