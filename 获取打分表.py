# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 20:37:01 2023

@author: Jerome
"""

import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


csv_raw = pd.read_excel('1.xlsx',header=None)
hang = csv_raw.shape[1]
lie_list=[]
for i in range(0,21):
    if csv_raw.iloc[0,i]=='专家编码':
        lie_list.append(i)
raw_dic = {}
for index in range(3,csv_raw.shape[0]):
    for j in lie_list:
        name = csv_raw.iloc[index,j]
        if pd.isna(name):
            continue
        if name not in raw_dic:
            temp = [csv_raw.iloc[index,j+1]]
        else:
            temp = raw_dic.get(name)
            temp.append(csv_raw.iloc[index,j+1])
        raw_dic[name] = temp

csv_pic=pd.DataFrame(index=raw_dic.keys(),columns=['0~10','10~20','20~30','30~40','40~50','50~60','60~70','70~80','80~90','90~100'])
csv_pic.index.name="专家编码"
csv_pic = csv_pic.fillna(0)

for key in raw_dic.keys():
    for value in raw_dic[key]:
        temp = int(value/10)
        index = csv_pic.index.get_loc(key)
        csv_pic.iloc[index, temp] += 1
        
csv_pic=csv_pic.sort_index()
csv_pic.to_csv("打分分布表.csv")
        
