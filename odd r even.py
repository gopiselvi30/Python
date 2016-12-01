#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 20:47:00 2016

@author: gopi-selvi
"""

#odd or even numbers
num=input("Enter a number:")
if int(num)%2==0 and int(num)%4==0:
    print("The is even number and divisible by 4")
elif int(num)%2==0:
    print("This is even number")
else:   
    print("The number is odd")
