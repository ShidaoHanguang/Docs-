# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 22:39:56 2023

@author: 24299
"""
import pandas as pd
import numpy as np

csv_raw = pd.read_excel('C 数据1.xlsx',skiprows=2,header=None)
csv_raw = csv_raw.loc[:,0:19]
# csv_raw = csv_raw.drop(columns=[3, 4])
# csv_raw.reset_index(inplace=True,drop=True)
csv_raw[1] = csv_raw[1].astype(float)
# columns = ["最终成绩",'名次','奖项','评委1','原始分1','标准分1','评委2','原始分2','标准分2','评委3','原始分3','标准分3','评委4','原始分4','标准分4','评委5','原始分5','标准分5']
# csv_raw.columns=columns
hang = csv_raw.shape[1]
lie_list=[]
for i in range(0,18):
    if csv_raw.iloc[0,i]=='专家编码':
        lie_list.append(i)
raw_dic = {}

for index in range(1,csv_raw.shape[0]):
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

  
columns = list(raw_dic.keys())
columns.sort()
columns=['名次']  + columns
csv_pro = pd.DataFrame(columns=columns)
for index in range(1,len(csv_raw.index)):
    csv_pro.loc[index-1,'名次'] = csv_raw.iloc[index,1]
    for lie in lie_list:
        csv_pro.loc[index-1,csv_raw.iloc[index,lie]] = csv_raw.iloc[index,lie + 1]
csv_pro = csv_pro.fillna(-1) 
csv_pro.sort_values(by = '名次',inplace=True)
csv_pro.to_csv("打分分析表.csv",index=None)


# csv_pro.index.name = '作品索引编号'
# csv_pro.to_csv("打分分析表.csv",index=None)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
