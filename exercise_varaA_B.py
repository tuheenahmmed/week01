#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 10:36:26 2018

@author: tuheenahmmed
"""

#Assume that two variables, varA and varB, are assigned values, either numbers or strings.

#Write a piece of Python code that evaluates varA and varB, and then prints out one of the following messages:

#"string involved" if either varA or varB are strings

#"bigger" if varA is larger than varB

#"equal" if varA is equal to varB

#"smaller" if varA is smaller than varB

varA= 1
varB= 10
type (varA)
type (varB)

if type (varA) == str or type (varB)== str:
    print ('string involved')
    
else:
    
  if varA > varB :
          print ('bigger')
          
  if varA == varB:
          print ('equal')
          
  if varA < varB:
          print ('smaller')
                    