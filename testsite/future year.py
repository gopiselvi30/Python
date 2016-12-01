#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 20:37:35 2016

@author: gopi-selvi
"""

import datetime
now=datetime.datetime.now()
current_year=now.year
print("find your future year here!!!!!!!")
name=input("Enter your name:")
age=input("Enter your age:")
future_year=(current_year-int(age))+100
print(name+" u will reach 100 in the year ",(future_year))
print(now)