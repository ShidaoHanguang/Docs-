# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 21:32:54 2023

@author: Jerome
"""
import pandas as pd
import numpy as np

def getIter(index_list):
    name_list2 = ['P'+ "{:03d}".format(x) for x in index_list if isinstance(x, int)] + [x for x in index_list if isinstance(x, str)]
    # name_list2.sort()
    temp = csv_raw
    for name in name_list2:
        if name not in name_list:
            print("评委编号错误，"+name+"不在范围内")
            return 0
        else:
            temp = temp[temp[name] >=0]
        if len(temp) == 0:
            return 0
    return temp.loc[:, name_list2]

csv_raw = pd.read_csv('打分分析表.csv',index_col=0)   
csv_su = pd.read_csv('评委重合度调查表.csv',index_col=0) 
csv_res = csv_su * 0
name_list = csv_su.index
a = getIter([5,70])
for index,row in csv_su.iterrows():
    temp_name_list = row[row > 0].index
    for temp_name in temp_name_list:
        temp_array = getIter([index , temp_name]) 
        temp_mean = (temp_array.iloc[:,0]-temp_array.iloc[:,1]).mean()
        csv_res.loc[index,temp_name] = temp_mean
        
        
        
        
        
        
        
        
        
        