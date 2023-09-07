#-------------Dynamic Programming--------------#
# 1- divide the problem into subproblems
# 2- solve the problem recursivly
# 3- store subproblems in array or table instead of recalculte it

# simple example 
# Diffrence Detween solution fib series by recurssivly and DyamicProgramming

# Fib by Recursivly
# def fib(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1 
#     else:
#         return fib(num-1)+fib(num-2)
# num = 9
# print(fib(num))

# solution by Dynamic programming
# def fib(num):
#     arr = [0,1]
#     for i in range(2,num+1):
#         arr.append(  arr[i-1] + arr[i-2] )
#     return arr[num]
# print(fib(9))