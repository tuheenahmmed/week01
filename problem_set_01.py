#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 20:28:29 2018

@author: tuheenahmmed
"""

#Problem 1
#0.0/10.0 points (graded)
#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s. 
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
#For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5

s = 'azcbobobegghakl'

numVowels = 0

for char in s:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1


print('Number of vowels: ' + str(numVowels))



#Problem 2
#0.0/10.0 points (graded)
#Assume s is a string of lower case characters.

#Write a program that prints the number of times the string 'bob' occurs in s. 
#For example, if s = 'azcbobobegghakl', then your program should print

#Number of times bob occurs is: 2



#for i in range(x):

#   s[i : i+3]
#The i parameter will be updated and your start and end parameters to slice the string will change with the value i. Therefore you will get a different string slice on every iteration.
#You can adapt these techniques to the problem (You must think about how to access the last index without getting an error. If you set the end index beyond the last index of the string, you will get an error).



s = 'azcbobobegghakl'

#i = 0   
count=0
for i in range(len(s)): 
    if s[i:i+3] == 'bob':
        count+=1
        
print('Number of times bob occurs is: ' + str(count))


-----------
Problem 3
-----------

Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 

For example, if s = 'azcbobobegghakl', then your program should print. Longest substring in alphabetical order is: beggh.

In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print. Longest substring in alphabetical order is: abc





s= 'azcbobobegghakl'

s = 'zyxwvutsrqponmlkjihgfedcba'

my_tempstring = s[0]
my_longstring = "   "

for i in range(len(s)-1): 
        #print (i)
        if s[i] <= s[i+1]:
        
            my_tempstring += s[i+1]
            #print (my_tempstring)
                
            if len (my_tempstring) > len(my_longstring):
                    my_longstring = my_tempstring
        
        else:
            my_tempstring = s [i+1]
            #print ('darlingthe longest substring of s in alphabetical order is  '+ s[i])

                
print ('Longest substring in alphabetical order is:  '+ my_longstring)


        
 





s='aa'

if s[0] <= s[1]:
    print ('the longest substring of s in alphabetical order is  '+ s)

else:
    print ('the longest substring of s in alphabetical order is  '+ s[1])
    


    
    
    
    
    
    
    



























            
    
       













