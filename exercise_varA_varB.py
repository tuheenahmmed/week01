# -*- coding: utf-8 -*-
"""
Created on Fri May 18 17:51:01 2018

@author: etuhahm
"""

varA=int(5)
varB=int(6)
type(varA)
type(varB)

if type(varA) or type(varB) == str:
    print("string involved")
elif varA > varB:
    print ("bigger")
elif varA == varB:
    print ("equal")
elif varA < varB:
    print ("smaller")
    