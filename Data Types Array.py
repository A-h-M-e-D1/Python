# -------------------------------------------
# -- Numpy => Data Types And Control Array --
# -------------------------------------------
# https://numpy.org/devdocs/user/basics.types.html
# https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html#specifying-and-constructing-data-types
# -------------------------------------------
# '?' boolean
# 'b' (signed) byte
# 'B' unsigned byte
# 'i' (signed) integer
# 'u' unsigned integer
# 'f' floating-point
# 'c' complex-floating point
# 'm' timedelta
# 'M' datetime
# 'O' (Python) objects
# 'S', 'a' zero-terminated bytes (not recommended)
# 'U' Unicode string
# 'V' raw data (void)
# ------------------------------------------------
import numpy as np
# To Known Date Type 
my_array1=np.array([1,2,6,7])
my_array2=np.array([200.3,60.2,7.5])
my_array3=np.array(["A","Ahmed","ibrahim"])
print(my_array1.dtype)
print(my_array2.dtype)
print(my_array3.dtype)

print("#"*50)
# Create Array With Specific Data Type
my_array1=np.array([1,2,6,7],dtype="f")
my_array2=np.array([200.3,60.2,7.5],dtype="i")
# my_array3=np.array(["A","Ahmed","ibrahim"],dtype="i") #ValueError
my_array4=np.array([0,1,3,0,5],dtype="?")
print(my_array1.dtype)
print(my_array2.dtype)
# print(my_array3.dtype)
print(my_array4.dtype)



