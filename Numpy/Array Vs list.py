import numpy as np 

# my_list=[2,3,6,8,10]
# my_list_two=[200,600,700,500]

# my_array=np.array([2,3,6,8,10])
# my_array_two=np.array([200,600,700,500])

# print(my_list)
# print(my_array)

# print("#"*50)

# print(type(my_list))
# print(type(my_array))

# print("#"*50)

# print(id(my_list))
# print(id(my_list_two))

# print(id(my_array))
# print(id(my_array_two))

# print("#"*50)

# my_array_three=np.array([10,50,60,"a",80])
# print(type(my_array_three[0]))
# print(my_array_three)


# Compare Performance And Memory Use.

import time
import sys
# elements=15000000

# list_one=range(elements)
# list_two=range(elements)


# print(all_list)
# for i in list_one:
#     print(i)

# my_array1=np.arange(elements)
# my_array2=np.arange(elements)

# list_start=time.time()

# all_list=[(n1+n2) for n1,n2 in zip(list_one,list_two)]
# print(f"list Time{time.time() - list_start}")

# array_start=time.time()
# array_result=my_array1 + my_array2
# # print(array_result)
# print(f"Array Time{time.time() - array_start}")

# for i in my_array1:
#     print(i) 

# Using Memory
my_array=np.arange(100)
print(my_array)
print(my_array.itemsize)
print(my_array.size)
print(f"All Bytes =>{my_array.itemsize*my_array.size}")

print("#"*50)

my_list=range(100)
print(sys.getsizeof(my_list[0]))
print(len(my_list))
print(f"All Bytes =>{sys.getsizeof(my_list[0])*len(my_list)}")