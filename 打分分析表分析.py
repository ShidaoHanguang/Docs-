# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 14:35:19 2023

@author: Jerome
"""

import pandas as pd
import numpy as np
csv_raw = pd.read_csv('打分分析表.csv',index_col=0)
name_list = csv_raw.columns.to_list()
# name_dict = {}
csv_temp = pd.DataFrame(columns=name_list,index =  name_list)
csv_temp = csv_temp.fillna(0)
nums = len(name_list)
# for name in name_list:
#     csv_filt = csv_raw[csv_raw[name]!=0]
#     for i in csv_filt.index:
#         for j in name_list:
#             if j == name:
#                 continue
#             elif csv_filt.loc[i,j] !=0:
#                 csv_temp.loc[name,j] += 1
# csv_temp.to_csv("评委重合度调查表.csv")
for name in name_list:
    csv_filt = csv_raw[csv_raw[name]>=0]
    for index,row in csv_filt.iterrows():
        temp = row[row >= 0].index.drop(name)
        for j in temp:
            csv_temp.loc[name,j] += 1
csv_temp.to_csv("评委重合度调查表.csv")
            
            
            
            
            
            
            
            
            
            
            
            
            
            