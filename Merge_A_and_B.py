import numpy as np, pandas as pd
import os
import csv

dir_str = r'/MScProject/A+B=C'
file_name_list = os.listdir(dir_str)  # Returns a list of all file names in the format
file_dir_list = [os.path.join(dir_str, x) for x in
                 file_name_list]  # The loop gets the list of absolute addresses of the file
df = pd.DataFrame()  # Define the variable df of type DataFrame to hold all the data obtained

files = len(file_name_list)
for i in range(0, files):
    # read_csv: to get the rows from each files
    csv1 = pd.read_csv(file_dir_list[i])
    # concat: merge A and B
    df = pd.concat([df, csv1], ignore_index=True)
df.to_csv('A+B=C.csv')
