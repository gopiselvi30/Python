#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 23:29:43 2016

@author: gopi-selvi
"""
#FLAMES with u and ur partner
name1=input("Enter your name:")
name2=input("Enter your partner's name:")
bname=name1.upper()
gname=name2.upper()
print(gname)
print(bname)
nm1=[]
nm2=[]
nm3=[]
for n1 in bname:
    nm1.append(n1)
   
for n2 in gname:
    nm2.append(n2)
   
for n3 in nm1:
    if n3 in nm2:
        nm1.remove(n3)
        nm2.remove(n3)
    else:
        nm3.append(n3)

for n4 in nm2:
    if n4 in nm1:
        nm1.remove(n4)
        nm2.remove(n4)
    else:
        nm3.append(n4)
        
            

print(nm1)
print(nm2)
print(nm3)

        
        