import numpy as np, pandas as pd
import os
import csv

dir_str= r'E:\Python\PycharmProjects\MScProject\trainingA-1.csv'

csv1 = pd.read_csv(dir_str)
csv1.drop("DBP",axis=1,inplace=True)

csv1["HR"] = np.where(csv1["HR"] >= 200, 200, csv1["HR"])
csv1["HR"] = np.where(csv1["HR"] <= 30, 30, csv1["HR"])

csv1["Temp"] = np.where(csv1["Temp"] >= 42, 42, csv1["Temp"])
csv1["Temp"] = np.where(csv1["Temp"] <= 35, 35, csv1["Temp"])


csv1["O2Sat"] = np.where(csv1["O2Sat"] <= 70, 70, csv1["O2Sat"])

csv1["SBP"] = np.where(csv1["SBP"] <= 80, 80, csv1["SBP"])

csv1["Resp"] = np.where(csv1["Resp"] <= 10, 10, csv1["Resp"])
csv1["Resp"] = np.where(csv1["Resp"] >= 24, 24, csv1["Resp"])

form = "{0:.02f}".format

csv1 = csv1.applymap(form)


csv1.to_csv('trainingA-2.csv',index=False)
