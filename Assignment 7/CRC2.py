''' CRC Calculation Generation at Transmission side
Test-Case
data="0b100100"
divisor="0b1101"

'''




data=[1,0,0,1,0,0]
print("data:",data)
data_backup=data.copy()
#print("Len of List1:",len_list1)

divisor=[1,1,0,1]
len_divisor=len(divisor)
print("Divisor:",divisor)

#Here Append zeros one Less than divisor

for i in range(len_divisor-1):
    data.append(0)

len_data=len(data)
print("Data Ready:",data,len_data)

############### Take Remainder as length equal to divisor & Fill with Zeros#######

remainder=[0,0,0,0]

counter=0

rem_list=[]
rem_list2=[]



for outer in range(len_data):

#####################################################################    
    if outer==0:
        #First Time this operation will be performed 
        for j in range(len_divisor):
            remainder[j]=data[outer] ^ divisor[j]
            print("Outer",outer,data[outer],divisor[j],remainder[j])
        outer=outer+j+1   
        
        print("Before Shifted List1:", outer, remainder)
        
        while remainder[counter]==0 :
            #Here find where  1's starts
            counter=counter+1
            if remainder[counter]==1:
                #Start copy the list3
                rem_list=remainder[counter:].copy()
        
        #print(rem_list)
        remainder=rem_list.copy()
        print("Drop Prefix Zeros Shifted List3: outer", outer, remainder)
        
        #Check here the number of bits to be appended from outer
        while len(remainder)<len_divisor:
            remainder.append(data[outer])
            outer=outer+1
        print("After Shifted List:",remainder)  
        
  ############################################################################### 
    
    elif outer>len_divisor and outer <len_data:
      print()  
      print()
      
      
      for j in range(len_divisor):
          result=remainder[j] ^ divisor[j]
          print("Outer",outer,remainder[j],divisor[j],result)
          remainder[j]=result
      print("Before Shifted List3:", outer, remainder)
      
      
      my_iterator=iter(remainder)
      
      while next(my_iterator)!=1: 
          remainder.remove(0)
          my_iterator=iter(remainder)
      
      rem_list2=remainder.copy()
      list4=rem_list2.copy()
      
      print("Drop Prefix Zeros Shifted List3:", outer, list4)
      #Check here the number of bits to be appended from outer
      
################      
      while  len(list4)<len_divisor and outer<len_data:
           
          print("Here Appending..",data[outer],"outer",outer)
          list4.append(data[outer])
          outer=outer+1
          
          #print(list4,"len:",len(list4))
          
          
          
      if  outer==len_data:
              #Here since the outer has completed the length
              
              remainder=list4.copy()
              print("After Shifted List:", remainder)
              
              result=0
              for j in range(len_divisor):
                  result=remainder[j] ^ divisor[j]
                  print("Final round:",remainder[j],divisor[j],result)
                  remainder[j]=result
              print("Final Shift:", remainder)
              crc=remainder[1:]
              print("CRC:",crc)
              
              for i in range(len(crc)):
                  data_backup.append(crc[i])
              
              print("Data Transmitted along with CRC:",data_backup, "Len_CRC:",len(crc))
              break
      
      if len(list4)==len_divisor:
         remainder=list4.copy()
       
       
