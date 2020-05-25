# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:34:20 2020

@author: ragib
"""

def mysum(a, b=100):
    total = 0
    p=0
    for i in range(a,b):
        total += i
        p=total+10
    return p