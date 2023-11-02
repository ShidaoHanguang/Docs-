# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 21:11:49 2023

@author: Jerome
"""

import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import keyboard


def drowByIndex(csv1,index,time):
    plt.clf()  
    ax = csv1.iloc[index].plot(kind='bar')
    plt.title('Data de Judge '+csv1.index[index])
    plt.xlabel('Score')
    plt.ylabel('Nums')
    for p in ax.patches:
        height = p.get_height()
        ax.text(p.get_x() + p.get_width() / 2, height, height, ha='center', va='bottom')
    plt.draw()  # 修改为 plt.draw()
    plt.pause(time)  # 新增 plt.pause()，在每次迭代后暂停一小段时间


csv_sc = pd.read_csv('打分分布表.csv',index_col=0)
max_index = len(csv_sc.index)
drowByIndex(csv_sc,0)
while True:
    command = input(f'请输入行索引（0 到 {max_index}），或输入 q 退出：')
    if command.lower() == 'q':
        break
    try:
        row_index = int(command)
        if row_index < 0:
            for i in range(0,max_index):
                drowByIndex(csv_sc,i,-row_index/10)
            break
        elif row_index > max_index:
            print(f'索引超出范围，请输入有效的行索引！')
#         else:
#             drowByIndex(csv_sc,row_index,0.001)
#     except ValueError:
#         print(f'无效的输入，请输入有效的行索引或 q 退出！')


        
        