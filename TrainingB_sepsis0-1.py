import numpy as np, pandas as pd
import os
import csv

dir_str= r'E:\Leeds\MSc Project\training_setB'
file_name_list=os.listdir(dir_str)   #返回格式所有文件名的列表list
file_dir_list=[os.path.join(dir_str,x) for x in file_name_list]#for循环获取文件的绝对地址的列表list
df = pd.DataFrame() #定义DataFrame类型的变量df用来存放获取的所有数据

files=len(file_name_list)
for i in range(0,files):
        #read_csv方法，参数sheet_name表示读取的工作簿，skiprows表示忽略几行，usecols表示读取指定的列
        csv1 = pd.read_csv(file_dir_list[i],sep='|')
        print(csv1["SepsisLabel"].head(1).values,csv1["SepsisLabel"].tail(1).values)
        if (csv1["SepsisLabel"].head(1).values==0) & (csv1["SepsisLabel"].tail(1).values==1) :
                csv1 = csv1[['HR', 'O2Sat', 'Temp', 'SBP', 'MAP', 'Resp', 'Age', 'Gender', 'HospAdmTime', 'ICULOS',
                          'SepsisLabel']]
                csv1["HR"] = csv1.groupby("Age")["HR"].transform(lambda x: x.fillna(x.mean()))
                csv1["O2Sat"] = csv1.groupby("Age")["O2Sat"].transform(lambda x: x.fillna(x.mean()))
                csv1["Temp"] = csv1.groupby("Age")["Temp"].transform(lambda x: x.fillna(x.mean()))
                csv1["SBP"] = csv1.groupby("Age")["SBP"].transform(lambda x: x.fillna(x.mean()))
                csv1["MAP"] = csv1.groupby("Age")["MAP"].transform(lambda x: x.fillna(x.mean()))
                csv1["Resp"] = csv1.groupby("Age")["Resp"].transform(lambda x: x.fillna(x.mean()))
                csv1["HospAdmTime"] = csv1.groupby("Age")["HospAdmTime"].transform(lambda x: x.fillna(x.mean()))
                csv1["ICULOS"] = csv1.groupby("Age")["ICULOS"].transform(lambda x: x.fillna(x.mean()))
                csv1["SepsisLabel"] = csv1.groupby("Age")["SepsisLabel"].transform(lambda x: x.fillna(x.mean()))
                csv1["Gender"] = csv1.groupby("Age")["Gender"].transform(lambda x: x.fillna(x.mean()))
        else:
                continue

        csv1["HR"] = np.where(csv1["HR"] >= 200, 200, csv1["HR"])
        csv1["HR"] = np.where(csv1["HR"] <= 30, 30, csv1["HR"])

        csv1["Temp"] = np.where(csv1["Temp"] >= 42, 42, csv1["Temp"])
        csv1["Temp"] = np.where(csv1["Temp"] <= 35, 35, csv1["Temp"])
        # 将异常体温进行统一化

        csv1["O2Sat"] = np.where(csv1["O2Sat"] <= 70, 70, csv1["O2Sat"])
        # 血氧饱和度最低不能低于70  动脉血:约98%、静脉血:约75%
        # 一般人SaO2正常应不低于94%，在94%以下为供氧不足。有学者将SaO2<90%定为低氧血症的标准，并认为当SaO2高于70%时准确性可达±2%，SaO2低于70%时则可有误差。
        # csv1["SBP"] = np.where(csv1["SBP"] >= 180, 180, csv1["SBP"])
        csv1["SBP"] = np.where(csv1["SBP"] <= 80, 80, csv1["SBP"])
        # 血压高压在240也有活着的，但是得吃降压药，但是高压的最低值不能低于80
        # csv1["MAP"] = np.where(csv1["MAP"] <= 80, 80, csv1["MAP"])
        # csv1["MAP"] = np.where(csv1["MAP"] >= 80, 80, csv1["MAP"])
        # 平均动脉压=（收缩压+2*舒张压）/3,但是好多人的数据都没有舒张压，却有MAP的值，很奇怪

        csv1["Resp"] = np.where(csv1["Resp"] <= 10, 10, csv1["Resp"])
        csv1["Resp"] = np.where(csv1["Resp"] >= 24, 24, csv1["Resp"])
        # 超过24次，为呼吸增快，多见于呼吸、循环系统疾病、发热、缺氧等。不足10次，为呼吸减慢。多见于药物中毒、颅内压增高等。
        # 正常成年人每分钟呼吸大约12-20次。新生儿的呼吸频率可达每分钟44次。正常成人静息状态下，呼吸为12到18次/分
        # 人体在情绪激动或者生病情况下会进行高呼吸频率
        form = "{0:.02f}".format  # 全数据保留小数点后两位

        csv1 = csv1.applymap(form)

        #concat方法合并多个文件的数据
        df = pd.concat([df,csv1],ignore_index=True)
df.to_csv('B.csv',index=False)
