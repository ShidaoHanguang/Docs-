# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 16:05:12 2023

@author: Jerome
"""

import pandas as pd
import numpy as np
def getIter(index_list):
    name_list2 = ['P'+ "{:03d}".format(x) for x in index_list if isinstance(x, int)] + [x for x in index_list if isinstance(x, str)]
    name_list2.sort()
    temp = csv_raw
    for name in name_list2:
        if name not in name_list:
            print("评委编号错误，"+name+"不在范围内")
            return 0
        else:
            temp = temp[temp[name] >=0]
        if len(temp) == 0:
            return 0
    csv_res = pd.DataFrame(columns=['作品编号','评委1','打分1','评委2','打分2','评委3','打分3','评委4','打分4','评委5','打分5'],index=range(len(temp)))
    i = 0
    for index,row in temp.iterrows():
        df_list = row[row >=0].index
        csv_res.iloc[i,0] = index
        for j in range(0,len(df_list)):
            csv_res.iloc[i,j*2+1] = df_list[j]
            csv_res.iloc[i,2*(j+1)] = row[df_list[j]]
        i += 1
    return csv_res


    
enq_list = [625]
csv_raw = pd.read_csv('打分分析表.csv',index_col=0)   
csv_su = pd.read_csv('评委重合度调查表.csv',index_col=0) 
name_list = csv_su.index
for index,row in csv_su.iterrows():
    temp_name_list = row[row > 0].index
    for temp_name in temp_name_list:
        a = getIter([index , temp_name])


# name_list = csv_raw.columns
# a = getIter(enq_list)
# print(a)