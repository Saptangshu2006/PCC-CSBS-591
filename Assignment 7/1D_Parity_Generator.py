"""
We have used strings for easy calculation
Parity Generator 
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

def even_parity():
    print("Even Parity Generator")
    #print(count_1) #Debug
    #Check if count of 1's  
    #Here last part of the string has been concatenated with one/zero
    if count_1%2==0:
       print(num_a+'0')#Div by 2 means No 1's needed to be appended
    else:
       print(num_a+'1')#Otherwise means  1's needed to be appended    
    
    
def odd_parity():
    print("Odd Parity Generator")
    #print(count_1) #Debug
    #Check if count of 1's  
    #Here last part of the string has been concatenated with one/zero       
    if count_1%2==0:
       print(num_a+'1')#Div by 2 means  1's needed to be appended
    else:
       print(num_a+'0')#Otherwise means No 1's needed to be appended    
       
    
even_parity()
odd_parity()



'''OUTPUT
100100
Even Parity Checker
No Error 0b100100
Odd Parity Checker
Error

'''
