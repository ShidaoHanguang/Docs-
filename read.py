# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 00:05:28 2023

@author: 24299
"""

import pandas as pd
csv_raw = pd.read_excel('C 数据1.xlsx',header=None)
hang = csv_raw.shape[1]
lie_list=[]
for i in range(0,hang):
    if csv_raw.iloc[2,i]=='专家编码':
        lie_list.append(i)
raw_dic = {}
for index in range(3,csv_raw.shape[0]):
    for j in lie_list:
        name = csv_raw.iloc[index,j]
        if pd.isna(name):
            continue
        if name not in raw_dic:
            temp = [csv_raw.iloc[index,j+1],csv_raw.iloc[index,j+2]]
        else:
            temp = raw_dic.get(name)
            temp.append(csv_raw.iloc[index,j+1])
            temp.append(csv_raw.iloc[index,j+2])
        raw_dic[name] = temp
        
s = pd.Series(raw_dic)
csv_score = s.apply(pd.Series)
# 对于缺少的分数，使用NaN值填充
max_cols = csv_score.shape[1]

csv_score = csv_score.reindex(columns=range(max_cols)).fillna(value=pd.np.nan)
# 重命名列名和索引名
columns = []
for i in range(1, max_cols + 1):
    if i % 2 == 0:
        columns.append('标准分{}'.format(i // 2))
    else:
        columns.append('原始分{}'.format((i + 1) // 2))

csv_score.columns = columns
csv_score.index.name = '专家编码'
    
# record = pd.DataFrame(columns=['专家编码'])
# record.loc[1,1] = 2
# record.loc[0,0] = 2
# record.loc[1,2] = 2
# # for         
