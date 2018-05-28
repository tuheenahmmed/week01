# -*- coding: utf-8 -*-
"""
Created on Fri May 18 17:51:01 2018

@author: etuhahm
"""

    
varA= 'a'
varB= 'b'
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