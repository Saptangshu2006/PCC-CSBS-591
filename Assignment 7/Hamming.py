# -*- coding: utf-8 -*-
"""
Hamming Distance

@author: Workstation
"""
import numpy as np

bin_a=0b101010
bin_b=0b111111

#print(bin_a,bin_b)#Default int print

result_xor=np.bitwise_xor(bin_a,bin_b)
#print(result_xor)#Default int
result_xor_bin=bin(result_xor)
#print(result_xor_bin[2:],type(result_xor_bin))#10101 <class 'str'>

list1=[]
dist=0
for i in result_xor_bin[2:]:
    list1.append(int(i))
    
        
for i in list1:
    if i==1:
        dist=dist+1
        
#print(list1,len(list1))
print("Hamming Distance",dist)
print("Max number of error bits can be detected:",dist-1)
print("Max number of error bits can be corrected:",(dist-1)/2)
