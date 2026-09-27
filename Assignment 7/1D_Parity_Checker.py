# -*- coding: utf-8 -*-
"""
We have used strings for easy calculation
Parity Checker
"""
import numpy as np

#Take a binary string
num_a='0b100100'

print(num_a[2:])#100100 #Debug


count_1=0# Counts number of 1's
for i in num_a[2:]:
    #print(int(i)) #Debug
    #We count total number of 1's, String converted to int first
    if int(i)==1:
        count_1=count_1+1

def even_parity_detect():
    print("Even Parity Checker")
    #print(count_1) #Debug
    #Check if count of 1's  
    
    if count_1%2==0:
       print("No Error",num_a)#Count of 1's div by 2 means No error
    else:
       print("Error")#Otherwise 
    
    
def odd_parity_detect():
    print("Odd Parity Checker")
    #print(count_1) #Debug
    #Check if count of 1's  
    #Here last part of the string has been concatenated with one/zero       
    if count_1%2==0:
       print("Error")#Div by 2 means Error
    else:
       print("No Error", num_a)#Otherwise means No 1's needed to be appended    
       
    
even_parity_detect()
odd_parity_detect()


'''OUTPUT
100100
Even Parity Checker
No Error 0b100100
Odd Parity Checker
Error

'''

