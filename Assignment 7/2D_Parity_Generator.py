
"""
2D Parity Generation at Sender side
#We are going to calculate two dimensional even parity with message string
"""


str_example="Hello" 
len_in_str=len(str_example)
#print(str_example,len(str_example))

bin_int=[]#List

#Store the binary version of the message in a list 
for i in str_example:
#    print("ASCII:",i,ord(i),bin(ord(i)))
#First convert to ASCII- by ord
#Second convert ASCII to binary
     bin_int.append(bin(ord(i))[2:])  #Here we discard 0b 
     save_bin=bin_int.copy() #Save the original Data in second list
     
     
#print(bin_int)#Hello looks like this 
#['1001000', '1100101', '1101100', '1101100', '1101111']
#Now calculate 2D Even Parity

#########################Row Parity###################################
for i in range(len(bin_int)):
  #Count total number of 1's
   count=0
   for j in bin_int[i]:
        #Individual elements of String object in the ith position of list
        #print(j,type(j))
    
        if(int(j)==1):
         count=count+1   
   
   #Even Parity
   #print(i,count)#For even count of 1's we append 0, otherwise 1
   if count%2==0:
       #print(type(bin_int[i]))#Str
       bin_int[i]=bin_int[i]+'0'
       #print((bin_int[i]))#debug after appending last character
   else:
       bin_int[i]=bin_int[i]+'1'

   #print("Original:",save_bin[i],len(save_bin[i]),"Row Parity:",bin_int[i],len(bin_int[i]))

#Bin_int now consists of row parity, hence each character will be of 8 bits length instead of 7

########################## Column Parity ########################

parity_col=""
#We have 8 characters after calculating parity for each element of bin_int
for k in range(8):
  count_col=0  
  for i in range(len(bin_int)):
    if(int(bin_int[i][k])==1):
       count_col=count_col+1
    
        
  #print("When k:",k,count_col)     
     
  if(count_col%2==0):
   parity_col=parity_col+'0'
  else:
   parity_col=parity_col+'1'

#print(str(parity_col))        

#Now Calculate the number of 1's in column parity

print()
print("Original Data:",save_bin)
print()
print("Row Parity:",bin_int)
print()
print("Column parity:",str(parity_col))

#Append this column parity at the end of bin_int parity list
bin_int.append(str(parity_col))
print()
print("Data Transmitted with Two Dimensional Parity",bin_int)
