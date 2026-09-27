# -*- coding: utf-8 -*-
"""
Checksum Sender Side 
Test: End Carry Generated
"""
import numpy as np

str_a='0b11110010'
str_b='0b10011111'

num_a=int(str_a,2)
num_b=int(str_b,2)

#Debug
print("Decimal:",int(num_a),"Binary:",bin(num_a),"Bit-Length:",num_a.bit_length())
print("Decimal:",int(num_b),"Binary:",bin(num_b),"Bit-Length:",num_b.bit_length())

sum_a_b=int(num_a)+int(num_b)
bin_sum_a_b=str(bin(sum_a_b))

print("Decimal:",int(sum_a_b),"Binary:",bin(sum_a_b),"Bit-Length:",sum_a_b.bit_length())

print()
print()

#####Check if End Carry Produced#####

size_a=num_a.bit_length()
size_b=num_b.bit_length()
size_a_b=sum_a_b.bit_length()



#If End Carry Generated
if (size_a_b>size_a) and (size_a_b>size_b):
    #1. Extract the MSB    
    carry=int(bin_sum_a_b[2],2)
    #2. Add the carry to rest of bin_sum_a_b at LSB position
    #Rest of the bits
    intermidiate=int(bin_sum_a_b[3:],2)
    #Sum with Carry
    final_sum=intermidiate+carry
    bin_final_sum=bin(final_sum) #This will be binary string object starting with "0b"
    print("Final sum:",bin_final_sum[2:])
    
    checksum=""
  
    for i in bin_final_sum[2:]:
        checksum=checksum+str(1-int(i))
        
        #print(1-int(i))
    
    print("Checksum: ", checksum)  

#If No end Carry Produced    
else:
    print("Final Sum:",bin_sum_a_b)
    checksum=""
    for i in bin_final_sum[2:]:
        checksum=checksum+str(1-int(i))
        #print(1-int(i))
    
    print("Checksum: ", checksum)  
    
print("Data after appending Checksum::Transmission End:",str_a[2:]+str_b[2:]+checksum)   
