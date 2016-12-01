#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 23:09:30 2016

@author: gopi-selvi
"""
#string is palindrome or not
a=input("Enter an string : ")
b=[]
c=len(a)
d=-1
for n in a:
    b.insert(int(d),n)
    d-=1
    c-=1
    if c==0:
        break
e=''.join(b)
print(e)
if str(e)==a:
    print ("it is a palindrome")
else:
    print("it is not an palindrome")
    
    
    