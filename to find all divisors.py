#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 22:25:47 2016

@author: gopi-selvi
"""

#to find all the divisors
a=input("Enter a number: ")
b=range(1,int(a))
element=[]
for c in b:
    if int(a)%c==0:
        element.append(c)
        
print ("the number "+str(a)+" is divisible by "+str(element))