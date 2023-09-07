# ---Revision--- #
# List Are mutable Sequences
# my_list=[1,"Red",10.55,True]
# print(type(my_list))
# print(my_list)
# my_list=list((1,2,3))
# print(type(my_list))
# print(my_list)

# my_string="Python"
# list=list(my_string)
# print(list)
# print(type(list))

# indexing And Slicing
# numbers=[1,2,3,4]
# print(numbers[0]) # 1
# numbers[1]="Ahmed"
# print(numbers)

# list comprehensions
# numbers=(1,2,3,4,5)
# squares=[num**2 for num in numbers]
# print(squares)

# numbers=(1,2,60,50,25,14,7)
# my_list=[num for num in numbers if num % 2==0]
# print(my_list) # [2, 60, 50, 14]

# print("#"*50)

# numbers=(1,2,60,50,25,14,7)
# my_list=[]
# for num in numbers:
#     if num % 2==0:
#         my_list.append(num)
# print(my_list) # [2, 60, 50, 14]

# Nested list 
# nest_list=[[1,2],[3,4]]
# print(nest_list[0])#[1,2]
# print(nest_list[0][1])# => 2

# Tuple 
my_tuple1=(2,3,7,10,13,100)
# my_tuple2=2,3,7,10,13,100
# print(type(my_tuple1))
# print(type(my_tuple2))
# print(dir(tuple))

# indexing && sclice
# print(my_tuple1[0:3]) #(2,3,7)

# my_tuple1=(2,3,7,10,13,100)
# my_tuple1[0]=5
# print(my_tuple1) # TypeError: 'tuple' object does not support item assignment

# Concatenation
# tuple1=(2,6,7)
# tuple2=(10,11,12)
# print(tuple1+tuple2) # (2,6,7,10,11,12)
# max_tuple=(21,'h',True,10.5)
# print(max_tuple)

# tuple methods
# tuple=(2,2,2,2,25,6,10)
# print(tuple.count(2)) #4
# print(tuple.index(10)) #6

# Remark
# x1=(9)
# x2=(9,)
# print(type(x1)) # int 
# print(type(x2)) # tuple

# tuple=(1,2,3,9,6,7)
# # print(len(tuple)) #6


# Tuple Packing and Unpacking
# coordinates=4.21,9.29
# x,y=coordinates
# print(x)
# print(y)

# aTuple = (100, 200, 300, 400, 500)
# print(aTuple[-2])
# print(aTuple[-4:-1])