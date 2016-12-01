#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 22:46:58 2016

@author: gopi-selvi
"""

list1= range(1,100)
list2= range(50,150)
list3=[]
for a in list1:
    if a in list1:
        list3.append(a)
for b in list2:
    if b not in list1:
        list3.append(b)
        
print(list3)
        