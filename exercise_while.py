#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 14:12:07 2018

@author: tuheenahmmed
"""

#1. Convert the following into code that uses a while loop.

#print 2
#prints 4
#prints 6
#prints 8
#prints 10
#prints Goodbye!


number= 0

while number < 10:   
    number+= 2
    print (number)
    
print ('Goodbye!')



#2. Convert the following into code that uses a while loop.

#prints Hello!
#prints 10
#prints 8
#prints 6
#prints 4
#prints 2

number= 10

print ('Hello!')
while number <= 10:   
    
    print (number)
    number-= 2
    if number == 0:
        break 
    
    
    
#3. Write a while loop that sums the values 1 through end, inclusive. 
#end is a variable that we define for you. So, for example, 
#if we define end to be 6, your code should print out the result:

#21
#which is 1 + 2 + 3 + 4 + 5 + 6.

#For problems such as these, do not include input statements or define variables we will provide for you. 
#Our automating testing will provide values so write your code in the following box assuming these variables are already defined.


end = 6
i = 0
while end > 0:
    
    i = i + end
    end-= 1
    
print (i)   





end=6
while end >0:
    end = end*(end+1)/2
    print (end)
    break


























    



