import pandas as pd
import numpy as np

date_info = pd.read_excel("/home/movic/EDA/Movic_intern/IPA_50motor_date_info.xlsx", sheet_name="E000S01 && E000S02  ", usecols='D:E')
date_info_ = date_info[10:-1]

date_info_.columns = ['[Sync]start', '[Sync]end']
print(date_info_.tail())
print("------")
print(date_info_["[Sync]start"].head())

text_list = []
for i in range(len(date_info_)):
    text_list.append(f"python OPT_processor.py --data_abs_dir /home/movic/True_NAS/PoC_IPA_01/1_motor-50kt --target_sensors E0001S01 E0001S02 --start_date {date_info_['[Sync]start'][i+10]} --end_date {date_info_['[Sync]end'][i+10]} --case_num {i+1}")


file_name = '/home/movic/EDA/Movic_intern/date_info.txt'
with open(file_name, 'w+') as file:
    file.write('\n'.join(text_list))