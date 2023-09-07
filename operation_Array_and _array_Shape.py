# ---------------------------------------------
# -- Numpy => Arithmetic & Useful Operations --
# ---------------------------------------------
# - Addition
# - Subtraction
# - Multiplication
# - Dividation
# ----------------
# - min
# - max
# - sum
# - ravel => Returns Flattened Array 1 Dimension With Same Type
# ----------------
import numpy as np
# => Addition,Subtraction, Multiplication ,Dividation
# my_array1=np.array([1,2,3])
# my_array2=np.array([4,5,6])
# print(my_array1 + my_array2) #[5,7,9]
# print(my_array1 - my_array2) # [-3,-3,-3]
# print(my_array1 * my_array2) # [4,10,18]
# print(my_array1 / my_array2)# [0.25 ,0.4, 0.5]

# print("#"*50)

# my_array3=np.array([[1,2,3],[4,5,6]])
# my_array4=np.array([[7,8,9],[10,11,12]])
# print(my_array3 + my_array4)
# print(my_array3 - my_array4)
# print(my_array3 * my_array4)
# print(my_array3 / my_array4)

# my_array5=np.array([[[1,2,3]],[[4,5,6]]])
# my_array6=np.array([[[7,8,9]],[[10,11,12]]])
# print(my_array5 + my_array6)
# print(my_array5 - my_array6)
# print(my_array5 * my_array6)
# print(my_array5 / my_array6)

# # Max,Min,Sum
# my_array7=np.array([10,200,600])
# print(my_array7.max())
# print(my_array7.min())
# print(my_array7.sum())

# # Ravel
# my_array8=np.array([[200,40,30],[20,60,70]])
# print(my_array8.ravel())


# Array Shape And ReShape

# my_array1=np.array([1,2,3])
# print(my_array1.ndim)
# print(my_array1.shape)
# Shape_array1=my_array1.reshape(3,1)
# print(Shape_array1)

# my_array2=np.array([[1,2,3],[4,5,6]])
# print(my_array2.ndim)
# print(my_array2.shape)
# Shape_array2=my_array2.reshape(3,2)
# print(Shape_array2)
# print(Shape_array2.shape)

# my_array3=np.array([[[1,2,3]],
#                     [[4,5,6]],
#                     [[7,8,9]],
#                     [[10,11,12]]]
#                    )
# print(my_array3.ndim)
# print(my_array3.shape)
# Shape_array3=my_array3.reshape(6,1,2)
# print(Shape_array3)

