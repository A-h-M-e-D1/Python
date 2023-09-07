# Create Array 
import numpy as np

from array import array

# my_array=array("i",[10,50,60,80,100])

# Type Array

# print(type(my_array))

# sum=0
# for num in my_array:
#     sum+=num
# print(sum)    

# my_array[-1]=50
# print(my_array)

# print(dir(np))

print("#"*50)

# My_Array_2=np.array([10,200,70,40])

# # print(My_Array_2[0])

# My_Array_2[1]=300

# print(My_Array_2) # [10 300 70 40]

# print("#"*50)

# sum=0
# for num in My_Array_2:
#      sum+=num
# print(sum)  #420      

# print("#"*50)

my_array_3=np.array([[1,3],[5,6]])

print(my_array_3[0]) # [1 3]
print(my_array_3[1]) # [5 6]

# To Find Element 

print(my_array_3[0][0]) # =>print(my_array_3[0,0])  ==>1
print(my_array_3[0,1]) # 3

print(type(my_array_3))

print("#"*50)

my_array_4=np.array([[[200,500]],[[600,700]],[[1000,7000]]])

print(my_array_4[0]) # [[200 500]]
print(my_array_4[0,0]) # [200 500]
print(my_array_4[0,0,0]) # 200

# for i in my_array_4[0]:
#     print(i[0]) ==>200




