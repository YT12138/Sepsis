import numpy as np, pandas as pd
import os
import csv

dir_str = r'E:\Leeds\MSc Project\training_setA'
file_name_list = os.listdir(dir_str)  # Returns a list of all file names in the format
file_dir_list = [os.path.join(dir_str, x) for x in
                 file_name_list]  # The loop gets the list of absolute addresses of the file
df = pd.DataFrame()  # Define the variable df of type DataFrame to hold all the data obtained

files = len(file_name_list)
for i in range(0, files):
    # read_csv: to get the rows from each files
    # sep='|': data is separated by '|'
    csv1 = pd.read_csv(file_dir_list[i], sep='|')
    csv1 = csv1[['HR', 'O2Sat', 'Temp', 'SBP', 'MAP', 'DBP', 'Resp', 'Age', 'Gender', 'HospAdmTime', 'ICULOS',
                 'SepsisLabel']]
    csv1["HR"] = csv1.groupby("Age")["HR"].transform(lambda x: x.fillna(x.mean()))
    csv1["O2Sat"] = csv1.groupby("Age")["O2Sat"].transform(lambda x: x.fillna(x.mean()))
    csv1["Temp"] = csv1.groupby("Age")["Temp"].transform(lambda x: x.fillna(x.mean()))
    csv1["SBP"] = csv1.groupby("Age")["SBP"].transform(lambda x: x.fillna(x.mean()))
    csv1["MAP"] = csv1.groupby("Age")["MAP"].transform(lambda x: x.fillna(x.mean()))
    csv1["DBP"] = csv1.groupby("Age")["DBP"].transform(lambda x: x.fillna(x.mean()))
    csv1["Resp"] = csv1.groupby("Age")["Resp"].transform(lambda x: x.fillna(x.mean()))
    csv1["HospAdmTime"] = csv1.groupby("Age")["HospAdmTime"].transform(lambda x: x.fillna(x.mean()))
    csv1["ICULOS"] = csv1.groupby("Age")["ICULOS"].transform(lambda x: x.fillna(x.mean()))
    csv1["SepsisLabel"] = csv1.groupby("Age")["SepsisLabel"].transform(lambda x: x.fillna(x.mean()))
    csv1["Gender"] = csv1.groupby("Age")["Gender"].transform(lambda x: x.fillna(x.mean()))

    # concat:merger all of them
    df = pd.concat([df, csv1], ignore_index=True)
df.to_csv('trainingA-1.csv', index=False)
