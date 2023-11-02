# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 21:47:13 2023

@author: Jerome
"""

import keyboard

# 读取方向键输入
while True:
    event = keyboard.read_event()
    if event.event_type == 'down':
        if event.name == 'up':
            print('按下了上箭头')
        elif event.name == 'down':
            print('按下了下箭头')
        elif event.name == 'left':
            print('按下了左箭头')
        elif event.name == 'right':
            print('按下了右箭头')
        elif event.name == 'q':
            break