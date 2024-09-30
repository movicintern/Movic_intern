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

sensor_name = ["E0001S02", "E0001S06"]
start_point = "20240801120001"
end_point = "20240802120000"

setup_instance = Setup(sensor_nm=sensor_name, start_point=start_point, end_point=end_point)

data_loader = DataLoader()
all_data_files = data_loader.transform_list(setup_instance)
visualization = Visualization()


data_file1 = all_data_files[0]
data_file2 = all_data_files[1]

for num in tqdm(range(len(data_file1)), desc="Processing files", unit="file"):
        setup_instance.apply(data_file1[num])
        # setup_instance.apply(data_file2[num])

        # f1, t1, dB1 = feature_extraction(data_file1[num], setup_instance)
        # f2, t2, dB2 = feature_extraction(data_file2[num], setup_instance)


        visualization.save_png(setup_instance, data_file1[num], data_file2[num])
        break
# %%
