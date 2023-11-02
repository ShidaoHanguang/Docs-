# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 17:41:28 2023

@author: Jerome
"""

import pandas as pd
import numpy as np

def getLimit(name_index_list,csv_raw):
    limit1 = 0
    limit2 = 0
    for index in range(1,csv_raw.shape[0]):
        for j in name_index_list:
            name = csv_raw.iloc[index,j]
            if pd.isna(name):
                if limit2 == 0:
                    limit1 = index
                    limit2 = j
                continue
    return limit1,limit2


csv_raw = pd.read_excel('C 数据1.xlsx',skiprows=2,header=None)
name_index_list = []
for i in range(0,csv_raw.shape[1]):
    if csv_raw.iloc[0,i]=='专家编码':
        name_index_list.append(i)
limit1,limit2 = getLimit(name_index_list,csv_raw)
name_index_list = [[n for n in name_index_list if n < limit2],[n for n in name_index_list if n >= limit2]]

csv_pro_1 = pd.DataFrame(columns=['作品名次','评委1','原始分1','标准分1','评委2','原始分2','标准分2','评委3','原始分3','标准分3','评委4','原始分4','标准分4','评委5','原始分5','标准分5'],index=range(len(csv_raw)-1))
csv_pro_2 = pd.DataFrame(columns=['作品名次','评委1','原始分1','标准分1','评委2','原始分2','标准分2','评委3','原始分3','标准分3'],index=range(limit1-1))
# raw_dic = {}
for index in range(1,len(csv_raw)):
    csv_pro_1.iloc[index-1,0]  =  csv_raw.iloc[index,1]
    i = 0
    for lie in name_index_list[0]:
        csv_pro_1.iloc[index-1,3*i + 1] = csv_raw.iloc[index,lie]
        csv_pro_1.iloc[index-1,3*i + 2] = csv_raw.iloc[index,lie + 1]
        csv_pro_1.iloc[index-1,3*i + 3] = csv_raw.iloc[index,lie + 2]
        i += 1
    i = 0
    if index >= limit1:
        continue
    else:
        csv_pro_2.iloc[index-1,0]  =  csv_raw.iloc[index,1]
        for lie in name_index_list[1]:
            csv_pro_2.iloc[index-1,3*i + 1] = csv_raw.iloc[index,lie]
            csv_pro_2.iloc[index-1,3*i + 2] = csv_raw.iloc[index,lie + 1]
            csv_pro_2.iloc[index-1,3*i + 3] = csv_raw.iloc[index,lie + 2]
            i += 1
# for index in range(1,limit1):
#     csv_pro.iloc[]
    
    # for j in name_index_list:
    #     name = csv_raw.iloc[index,j]
    #     if pd.isna(name):
    #         continue
    #     if name not in raw_dic:
    #         temp = [csv_raw.iloc[index,j + 1],csv_raw.iloc[index,j + 2]]
    #     else:
    #         temp = raw_dic.get(name)
    #         temp.append(csv_raw.iloc[index,j + 1])
    #         temp.append(csv_raw.iloc[index,j + 2])
    #     raw_dic[name] = temp
