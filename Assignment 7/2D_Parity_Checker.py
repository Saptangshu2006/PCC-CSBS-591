
"""
2D Parity Checker at Receiver side
#We are going to calculate two dimensional even parity with message string
Data Transmitted with Two Dimensional Parity 
test-1=['10010000', '11001010', '11011000', '11011000', '11011110', '10000100']
test-2=['10010000', '11001010', '11011000', '11011000', '11011110', '10010100']

"""
#import numpy as np



data=['10010000', '11001010', '11011000', '11011000', '11011110', '10000100'] #No Error
#data=['10010000', '11001010', '11011000', '11011000', '11011110', '10010100'] #Error
print(data)

parity_count=[]
flag=0

for i in range(len(data)):
    #print(data[i],type(data[i]))
    count=0
    for j in range(len(data[i])):
       # print(data[i][j])
       if(int(data[i][j])==1):
           count=count+1
    #print(i,data[i],count) 
    parity_count.append(count)
    

for count in parity_count:
    if count%2!=0:
        flag=1
        break
    
if flag==0:
    print("Data has no Error") 
else:
    print("Data is Corrupted")    