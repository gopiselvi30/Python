#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 21:00:40 2016

@author: gopi-selvi
"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b=[n for n in a if n%2==0]
print (b)
'''for n in a:
    if n%2==0:
        b.append(n)
print (b)'''