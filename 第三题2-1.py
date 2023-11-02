# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 12:32:02 2023

@author: Jerome
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def getLimit(lie_list,csv_raw):
    limit1 = 0
    limit2 = 0
    for index in range(1,csv_raw.shape[0]):
        for j in lie_list:
            name = csv_raw.iloc[index,j]
            if pd.isna(name):
                if limit2 == 0:
                    limit1 = index
                    limit2 = j
                continue
    return limit1,limit2


def getCsvPro(lie_list,csv_raw,a):
    limit1,limit2 = getLimit(lie_list,csv_raw)
    csv_pic_t = pd.DataFrame(columns=['第一次分数','第二次分数'])
    lie_list = [[n for n in lie_list if n < limit2],[n for n in lie_list if n >= limit2]]
    a += 1
    for index in range(1,limit1):
        score1 = []
        score2 = []
        for j in lie_list[0]:
            score1.append(float (csv_raw.iloc[index,j + a]))
        for j in lie_list[1]:
            score2.append(float (csv_raw.iloc[index,j + a]))
        csv_pic_t.loc[index-1,'第一次分数'] = np.mean(score1)
        csv_pic_t.loc[index-1,'第二次分数'] = np.mean(score2)
        
    return csv_pic_t

def drawPic(lie_list,csv_raw,a,b):
    
    # 读取数据表
    csv_pro = getCsvPro(lie_list,csv_raw,a)
    if b == 1:
        csv_pro.sort_values(by='第一次分数',ascending=False,inplace=True)
        csv_pro.reset_index(inplace=True)
    # 提取成绩1和成绩2列的数据
    score1 = csv_pro['第一次分数']
    score2 = csv_pro['第二次分数']
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 创建折线图
    plt.plot(score1, label='分数1')
    plt.plot(score2, label='分数2')

    # 添加图例、标题和轴标签
    plt.legend()
    plt.xlabel('编号')
    plt.ylabel('分数')
    if a == 0:
        plt.title('原始分')
    else:
        plt.title('标准分')
    # 显示图形
    plt.draw() 
    plt.pause(0.001)
    return csv_pro


def drawPic2(lie_list,csv_raw,a,b):
    
    # 读取数据表
    csv_pro = getCsvPro2(lie_list,csv_raw,a)
    if b == 1:
        csv_pro.sort_values(by='极差1',ascending=False,inplace=True)
        csv_pro.reset_index(inplace=True)
    # 提取成绩1和成绩2列的数据
    score1 = csv_pro['极差1']
    score2 = csv_pro['极差2']
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 创建折线图
    plt.plot(score1, label='极差1')
    plt.plot(score2, label='极差2')

    # 添加图例、标题和轴标签
    plt.legend()
    plt.xlabel('编号')
    plt.ylabel('极差')
    if a == 0:
        plt.title('原始分')
    else:
        plt.title('标准分')
    # 显示图形
    plt.draw() 
    plt.pause(0.001)
    return csv_pro



def getCsvPro2(lie_list,csv_raw,a):
    limit1,limit2 = getLimit(lie_list,csv_raw)
    csv_pic_t = pd.DataFrame(columns=['极差1','极差2'])
    lie_list = [[n for n in lie_list if n < limit2],[n for n in lie_list if n >= limit2]]
    a += 1
    for index in range(1,limit1):
        score1 = []
        score2 = []
        for j in lie_list[0]:
            score1.append(float (csv_raw.iloc[index,j + a]))
        for j in lie_list[1]:
            score2.append(float (csv_raw.iloc[index,j + a]))
        csv_pic_t.loc[index-1,'极差1'] = np.max(score1)-np.min(score1)
        csv_pic_t.loc[index-1,'极差2'] = np.max(score2)-np.min(score2)
    return csv_pic_t


def drawPic3(lie_list,csv_raw,a,b):
    # 读取数据表
    csv_pro = getCsvPro3(lie_list,csv_raw,a)
    # 提取成绩1和成绩2列的数据
    score1 = csv_pro['第一次分数']
    score2 = csv_pro['第二次分数']

    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 创建折线图
    plt.plot(score1, label='分数1')
    plt.plot(score2, label='分数2')

    # 添加图例、标题和轴标签
    plt.legend()
    plt.xlabel('编号')
    plt.ylabel('分数')
    if a == 0:
        plt.title('原始分')
    else:
        plt.title('标准分')
    # 显示图形
    plt.draw() 
    plt.pause(0.001)
    return csv_pro


def getCsvPro3(lie_list,csv_raw,a):
    limit1,limit2 = getLimit(lie_list,csv_raw)
    csv_pic_t = pd.DataFrame(columns=['第一次分数','第二次分数'])
    lie_list = [[n for n in lie_list if n < limit2],[n for n in lie_list if n >= limit2]]
    a += 1
    for index in range(1,len(csv_raw)):
        score1 = []
        score2 = []
        for j in lie_list[0]:
            score1.append(float (csv_raw.iloc[index,j + a]))
        csv_pic_t.loc[index-1,'第一次分数'] = np.mean(score1)
        if index >= limit1 :
            continue
        else:
            for j in lie_list[1]:
                score2.append(float (csv_raw.iloc[index,j + a]))
            csv_pic_t.loc[index-1,'第二次分数'] = np.mean(score2)
    return csv_pic_t

csv_raw = pd.read_excel('C 数据2.1.xlsx',skiprows=2,header=None)
csv_raw = pd.concat([csv_raw.iloc[[0]], csv_raw.iloc[1:].sort_values(by=1)], ignore_index=True)
lie = csv_raw.shape[1]
lie_list=[]
for i in range(0,lie):
    if csv_raw.iloc[0,i]=='专家编码':
        lie_list.append(i)
        
csv_pro = drawPic2(lie_list,csv_raw , 0 , 0)






        
        
        
        
