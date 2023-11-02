# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 17:07:53 2023

@author: Jerome
"""

import pandas as pd
import numpy as np

a = 1
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
            temp = [csv_raw.iloc[index,j + a]]
        else:
            temp = raw_dic.get(name)
            temp.append(csv_raw.iloc[index,j + a])
        raw_dic[name] = temp
        
s = pd.Series(raw_dic)
csv_score = s.apply(pd.Series)
csv_score = csv_score.astype(float)
# 对于缺少的分数，使用NaN值填充
max_cols = csv_score.shape[1]

csv_score = csv_score.reindex(columns=range(max_cols)).fillna(value=np.nan)
# 重命名列名和索引名
columns = []
for i in range(1, max_cols + 1):
    if a == 1:
        columns.append('原始分{}'.format(i))
    else :
        columns.append('标准分{}'.format(i))

csv_score.columns = columns
csv_score.index.name = '专家编码'
csv_score = pd.concat([pd.Series(dtype='float64',name='平均分'), pd.Series(dtype='float64',name='标准差'),csv_score], axis=1)
for p in range(0,len(csv_score.index)):
    b = csv_score.iloc[p]
    arr = np.array(b)
    std = np.nanstd(arr, ddof=1)
    mean = np.nanmean(arr)
    # print(std)
    csv_score.iloc[p,0]=mean
    csv_score.iloc[p,1]=std
csv_score = csv_score.sort_index()
csv_score.index.name="专家编码"

# if a == 1:
#     csv_score.to_csv("原始打分表.csv")
# else:
#     csv_score.to_csv("标准打分表.csv")
# a = csv_score.iloc[0]
# arr = np.array(a)

# # 计算标准差
# std = np.nanstd(arr)

# # 计算带有缺失值的平均值
# mean = np.nanmean(arr)
# count = 0
# nums = 0
# for i in a :
#     if pd.isna(i):
#         continue
#     else:
#         count+=i
#         nums+=1
# print(count/nums)
    