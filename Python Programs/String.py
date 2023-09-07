# ---Revision---#
# s1="12"

# s2='Hello'
# print(type(s1)) # string
# print(type(s2)) # string

# string1="i love python,"Good"" # SyntaxError: invalid syntax
# print(string1)

# length of a string
# string="python"
# print(len(string)) # 6

# docstrings used to document custom functions
#Ex: 
# """
# This Type string
# """

# Concatenation 
# one way
# first_name="Ahmed"
# last_name="Ashraf"
# full_name=first_name +" "+ last_name
# print(full_name)

# two way
# first_name="Ahmed"
# last_name="Ashraf"
# full_name=' '.join([first_name,last_name])
# print(full_name)

# three way
# first_name="Ahmed"
# last_name="Ashraf"
# full_name='%s %s'%(first_name,last_name)
# print(full_name)

# last way
# first_name="Ahmed"
# last_name="Ashraf"
# full_name='{} {}'.format(first_name,last_name)
# print(full_name)

# String Indexing
# string_one="Python"
# index=string_one[0:4]
# print(index) #Pyth

# string_two="Python"
# index=string_one[::-1]
# print(index) # nohtyP

# index Vs find

# string_three="Python"
# index=string_three.index('p') # ValueError: substring not found
# print(index)

# string="Python"
# find=string.find("f") # -1
# print(find)

# String Slicing
# string="python"
# slicing=string[0:3]
# print(slicing) # pyt

# String Are Immutable
# string="python"
# string[0]="8"
# print(string) # TypeError: 'str' object does not support item assignment

# To alter a string
# string="Cyber"
# new_string= '8' +string[0:]
# print(new_string) # 8yber

# String methods
# string="PyThon"
# string_lower=string.lower() 
# string_upper=string.upper()
# print(string_lower) # python
# print(string_upper) # PYTHON

# string="  python   9"
# strip_string1=string.strip()
# strip_string2=string.rstrip()
# strip_string3=string.lstrip()
# print(strip_string1) # "python   9"
# print(strip_string2) # "  python   9"
# print(strip_string3) # "python  9"

# string="python"
# check_start=string.startswith("p")
# check_end=string.endswith("f")
# print(check_start) # True
# print(check_end) # false

# String  And Arithmetic Operators
# num="2"
# print(type(num+num)) #22 => Type(string)

# String Formatting
# old Way
# % s => string
# %d => numbeer
# %f => float // % .{number appare after}f
# pi=3.14159
# print(f"{pi:.2f}") # 3.14
# print('{:.2f}'.format(pi))
# first_name="Ahmed"
# last_name="Ashraf"
# full_name=f"My name is {first_name} {last_name} "
# print(full_name)

# Boolean 
