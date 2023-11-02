# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 18:54:00 2023

@author: Jerome
"""
import pandas as pd
import numpy as np


#查找所有对应获奖者的表
def sortByRank(csv_re,rank):
    list_rank = [' ','一等奖','二等奖','三等奖','无奖项']
    if rank == 0:
        return csv_re
    else:
        return csv_re[csv_re['奖项'] == list_rank[rank]]


#查找所有对应获奖者按标准分排名后的表以及其对应输出值
def valueByRank(csv_re,rank):
    csv_re.insert(loc=2, column='标准分成绩',value='')
    for i in csv_re.index:
        csv_re.loc[i,'标准分成绩'] = csv_re.loc[i,'标准分1']+csv_re.loc[i,'标准分2']+csv_re.loc[i,'标准分3']+csv_re.loc[i,'标准分4']+csv_re.loc[i,'标准分5']
    a=csv_raw.index + 1 
    csv_1 = csv_re.sort_values(by = '标准分成绩',ascending=False)
    csv_1.insert(loc=2, column='标准分名次',value=a)
    csv_raw_prize = sortByRank(csv_1,rank)
    count = 0
    for index in csv_raw_prize.index:
        count = count + np.abs(csv_raw_prize.loc[index,'标准分名次']-csv_raw_prize.loc[index,'名次'])
    return [csv_raw_prize.sort_index(),count/len(csv_raw_prize.index)]



csv_raw = pd.read_excel('C 数据1.xlsx',header=None)
csv_raw = csv_raw.loc[3:,0:19]
csv_raw = csv_raw.drop(columns=[3, 4])
csv_raw.reset_index(inplace=True,drop=True)
csv_raw[1] = csv_raw[1].astype(float)
columns = ["最终成绩",'名次','奖项','评委1','原始分1','标准分1','评委2','原始分2','标准分2','评委3','原始分3','标准分3','评委4','原始分4','标准分4','评委5','原始分5','标准分5']
csv_raw.columns=columns

a,b=valueByRank(csv_raw,3)

    