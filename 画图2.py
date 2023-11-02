# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 21:50:25 2023

@author: Jerome
"""
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import keyboard


def drawByIndex(index,cl):
    plt.clf()  
    if cl == 0 :
        csv1 = csv_sc_1
    if cl == 1 :
        csv1 = csv_sc_2
    ax = csv1.iloc[index].plot(kind='bar')
    name = csv1.index[index]
    # plt.annotate('Important Point', xy=(6, 9), xytext=(3, 15),
    #          arrowprops=dict(facecolor='black', arrowstyle='->'))
    plt.rcParams['font.sans-serif'] = ['SimHei']
    if cl == 0:
        plt.title('评委'+csv1.index[index]+'的原始分分布\n'+
                  "平均分:{:.2f}".format(csv_rw.loc[name,"平均分"])+'\n'+
                  "标准差:{:.2f}".format(csv_rw.loc[name,"标准差"]))
    else:
        plt.title('评委'+csv1.index[index]+'的标准分分布\n'+
                  "平均分:{:.2f}".format(csv_sd.loc[name,"平均分"])+'\n'+
                  "标准差:{:.2f}".format(csv_sd.loc[name,"标准差"]))
    plt.xlabel('分数')
    plt.ylabel('数量')
    for p in ax.patches:
        height = p.get_height()
        ax.text(p.get_x() + p.get_width() / 2, height, height, ha='center', va='bottom')
    plt.draw()  # 修改为 plt.draw()
    plt.pause(0.001)  # 新增 plt.pause()，在每次迭代后暂停一小段时间


def main_Draw(row_index,class_judge):
    while True:
        event = keyboard.read_event()
        if event.event_type == 'down':
            if event.name == 'up':
                row_index += 1
                if row_index >= max_index:
                    row_index = 0
                drawByIndex(row_index,class_judge)
            elif event.name == 'down':
                row_index -= 1
                if row_index < 0:
                    row_index = max_index - 1
                drawByIndex(row_index,class_judge)
            elif event.name == 'left':
                class_judge = 1 - class_judge
                drawByIndex(row_index,class_judge)
            elif event.name == 'right':
                class_judge = 1 - class_judge
                drawByIndex(row_index,class_judge)
            elif event.name == 'q':
                break
    

row_index = 0

csv_sc_1 = pd.read_csv('打分分布表（原始）.csv',index_col=0)
csv_sc_2 = pd.read_csv('打分分布表（标准）.csv',index_col=0)
csv_rw = pd.read_csv('原始打分表.csv',index_col=0)
csv_sd = pd.read_csv('标准打分表.csv',index_col=0)

max_index = len(csv_sc_1.index)

class_judge = 0

drawByIndex(row_index,class_judge)

main_Draw(row_index,class_judge)

