#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 12:34:55 2018

@author: tuheenahmmed
"""

num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num) 


################

num = 10
while num > 3:
    num -= 1
    print(num) 


#############
    
num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')