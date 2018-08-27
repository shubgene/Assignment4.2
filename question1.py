# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 21:42:11 2018

@author: shurastogi
"""
def moving_function(vec,window_size):
    list_ex=[]
    for i in range(len(vec)-window_size +1):
        list_ex.append(float(sum(vec[x+i] for x in range(window_size))/window_size))
    return list_ex



vec=[10 ,20 ,30 ,40 ,50 ,60 ,70 ,80 ,90 ,100]

moving_function(vec,4)

vec2=[3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]

moving_function(vec2,3)