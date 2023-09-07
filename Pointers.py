# Simulating Pointers in Python
# def add_one(x):
#     x[0]+=1
# y=[2337]   
# add_one(y)
# print(y[0])

#--- Create Pointers by using Ctypes Moduele ---

# import ctypes as ct
# value_1 variable stores an integer
# of type Ctypes (not a regular integer)
# value_1 = ct.c_int(10)

# printing the type of value_1
# print(value_1)

# printing the value which value_1 stores
# print(value_1.value)

# value_2=ct.c_float(10.75)
# print(value_2)
# print(value_2.value)

# value_3=ct.c_double(10.689754)
# print(value_3)
# print(value_3.value)


# import ctypes as ct

# # storing a ctypes long value
# value_1 = ct.c_long(10)

# # using pointer() method we are pointing to the
# # value_1 variable and storing it in ptr
# ptr = ct.pointer(value_1)

# print("Contents of value_1 : " ,
# 	value_1)
# print("Real value stored in value_1 : ",
# 	value_1.value)
# print("Address of value_1 : ",
# 	id(value_1.value))

# # If we want to print the contents of a pointer
# # type variable then need to use .contents
# # otherwise only writing the variable is enough like above
# print("Contents of ptr variable : ",
# 	ptr.contents)

# # To print the value stored in the address
# # pointed by that pointer variable
# # we need to use .value after .contents
# print("The value at which ptr points at : ",
# 	ptr.contents.value)

# # Printing the address of the value to
# # which the ptr variable points at
# print("Address of that value which is \
# pointed and stored in ptr : ",id(ptr.contents.value))


# # To change the Value in pointer 

# value_1=ct.c_long(10)
# # test  we use pointer
# print("Address value_1 ==",id(value_1))

# prt=ct.pointer(value_1)
# print("Address prt ==",id(value_1))

# print("Value Before Changing => ",value_1.value)

# prt.contents.value=25

# print("Value After changing => ",value_1.value)

import ctypes as ct

value_1 = ct.c_int(10)

# Creating a void Pointer ptr2
ptr2 = ct.POINTER(ct.c_int)

# Trying to print the contents of the void
# pointer before pointing it to any variable
print("Contents of Void Pointer : ",
	ptr2.contents)

# Now pointing the ptr2 variable to the value_1
# variable which is a ctype c_int
ptr2.contents = value_1

# Now again printing the contents of the ptr2 variable
print("Contents of void pointer after \
pointing it to a variable : ",ptr2.contents)

# Printing the value stored in the Void Pointer
print("Value stored by Void Pointer : ",
	ptr2.contents.value)
