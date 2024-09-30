#%%
import os
from scipy import signal
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def frequency_cut(data, low_cut=20000, high_cut = 80000):
    """
    data (H, W) -> data (H[low_cut ~ high_cut], W)
    return data(H,W)
    """
    unit = 2049/192000
    data = data[int(unit*low_cut) : int(unit*high_cut), :]
    return data

base_dir = '/home/movic/EDA/240926/Mixdown'

subfolders = [
    os.path.join(base_dir, d)
    for d in os.listdir(base_dir)
    if os.path.isdir(os.path.join(base_dir, d))
]

wav_file = [
    file
    for subfolder in subfolders
    for _, _, files in os.walk(subfolder)
    for file in files
    if file.endswith('.wav')
]
# print(wav_file)
data_path = []

for num in range(len(wav_file)):
    if 'natural' in wav_file[num]:
        data_path.append(os.path.join(base_dir, '1. natural', wav_file[num]))
    elif 'actuator_o' in wav_file[num]:
        data_path.append(os.path.join(base_dir, '2. actuator_o', wav_file[num]))
    elif 'actuator_x' in wav_file[num]:
        data_path.append(os.path.join(base_dir, '3. actuator_x', wav_file[num]))
    elif 'gpu' in wav_file[num]:
        data_path.append(os.path.join(base_dir, '4. gpu', wav_file[num]))
    elif '800_ac_off' in wav_file[num]:
        data_path.append(os.path.join(base_dir, '5. 800_off', wav_file[num]))
    elif '800_ac_on' in wav_file[num]:
        data_path.append(os.path.join(base_dir, '6. 800_on', wav_file[num]))
    elif '1000_ac_on' in wav_file[num]:
        data_path.append(os.path.join(base_dir, '7. 1000_on', wav_file[num]))
    elif '1500_ac_on' in wav_file[num]:
        data_path.append(os.path.join(base_dir, '8. 1500_on', wav_file[num]))
    elif 'type_1' in wav_file[num] or 'std_type_1' in wav_file[num]:
        data_path.append(os.path.join(base_dir, '9. type_1', wav_file[num]))
    elif 'type_2' in wav_file[num] or 'std_type_2' in wav_file[num]:
        data_path.append(os.path.join(base_dir, '10. type_2', wav_file[num]))

# /home/movic/EDA/240926/Mixdown/5. 900_off/800_ac_off_01.wav
# print(data_path[0])
# print(data_path[0].split('/')[6])

####### y축 범위 수정과 frequency_cut 함수만 수정하면 됨 ########

for num in tqdm(range(len(data_path)), desc="Processing files"):
    data_nm = data_path[num].split('/')[7][:-4]
    _, data = wavfile.read(data_path[num])
    f, t, Sxx = signal.spectrogram(x=data, fs=384000,
                                   nperseg=4096, nfft=4096,
                                   noverlap=2048, mode='magnitude', scaling='spectrum')
    power = Sxx**2
    dB = 10 * np.log10(power +1e-5)
    dB = np.maximum(dB, dB.max()-80)
    dB = frequency_cut(dB)
    print("Shape of dB:", dB.shape)
    print("Length of t:", len(t))
    print("Length of f:", len(f))


    plt.pcolormesh(t, f, dB, cmap='jet', shading='auto')
    plt.title(data_nm)
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (sec)')

    save_path = os.path.join(base_dir, 'Frequency_cut_Visualization', data_path[num].split('/')[6],
                              f'{data_nm}.png')
    
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(fname=save_path, bbox_inches='tight', format='png')
    plt.clf()
# %%
