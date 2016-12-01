#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 21:04:15 2016

@author: gopi-selvi
"""

a=("rock")
b=("paper")
c=("scissors")
print("We are going to play Rock paper Scissor")
print("Please choose from the following")
print(" rock\n paper\n scissors")
in11=input("Enter ur choice:")
in1=in11.lower()
in22=input("Enter your choice:")
in2=in22.lower()
if str(in1)==in2:
    print("Match tie")
elif in1==a and in2==b:
    print("player B wins")
elif str(in1)==str(a) and in2==str(c):
    print("Player A wins")
elif str(in1)==str(b) and in2==str(a):
    print("Player A wins")
elif str(in1)==str(b) and in2==str(c):
    print("Player B wins")
elif str(in1)==str(c) and in2==str(a):
    print("Player B wins")
elif str(in1)==str(c) and in2==str(b):
    print("Player A wins")
else:
    print("Invalid input: please inpur correct choice!!!!!!")
    print(in11)
    print(in22)