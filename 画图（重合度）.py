# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 15:07:07 2023

@author: Jerome
"""

import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import keyboard

# class_judge = 0

def drawByIndex(index):
    plt.clf()  
    temp = csv_raw.iloc[index]
    temp.sort_values(inplace = True,ascending = False)
    temp = temp[:10]
    name = name_list[index]
    ax = temp.plot(kind='bar')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title('评委'+name+'重合次数图（取前10人）')
    plt.xlabel('评委名称')
    plt.ylabel('次数')
    for p in ax.patches:
        height = p.get_height()
        ax.text(p.get_x() + p.get_width() / 2, height, height, ha='center', va='bottom')
    plt.draw()  # 修改为 plt.draw()
    plt.pause(0.001)  # 新增 plt.pause()，在每次迭代后暂停一小段时间
    max_list = temp[temp == temp.max()].index
    print('与评委'+name+'重合次数最多的评委：')
    for i in max_list:
        print(i+' : '+str(temp[i]))
    print('\n')
        
def main_Draw(row_index):
    drawByIndex(row_index)
    while True:
        event = keyboard.read_event()
        if event.event_type == 'down':
            if event.name == 'up':
                row_index += 1
                if row_index >= max_index:
                    row_index = 0
                drawByIndex(row_index)
            elif event.name == 'down':
                row_index -= 1
                if row_index < 0:
                    row_index = max_index - 1
                drawByIndex(row_index)
            elif event.name == 'left':
                row_index -= 10
                if row_index < 0:
                    row_index = max_index - 1
                drawByIndex(row_index)
            elif event.name == 'right':
                row_index += 10
                if row_index >= max_index:
                    row_index = 0
                drawByIndex(row_index)
            elif event.name == 'q':
                break

csv_raw = pd.read_csv('评委重合度调查表.csv',index_col=0)
name_list = csv_raw.index
max_index = len(csv_raw.index)
main_Draw(0)







