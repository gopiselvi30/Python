#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 20:54:36 2016

@author: gopi-selvi
"""
#numbers less tha n five in list
a=[1,2,3,4,5,6,7,8,9,10,11]
b=[]
for n in a:
    if int(n)<5:
        b.append(n)
        
print (b)