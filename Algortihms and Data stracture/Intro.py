# intro to Algrathims and data structure

# Design Simple Alograthims 
# Algrathims To sum 3 numbers

# Variables to take the input of
# the 3 numbers 

# num1=num2=num3=0

# Define sum

# sum=0

# Take three numbers from users

# num1 = int(input("Enter The 1st Number: "))
# num2 = int(input("Enter The 2nd Number: "))
# num3 = int(input("Enter The 3rd Number: "))

# sum Three numbers

# sum = num1 + num2 + num3

# print the sum of three numbers

# print("\nSum of the 3 numbers is: ",sum)


# simple Algorthims to show time,space complexity

# def factorial(number):
    # """

    # This function to find factorial by spacial Algorthims

    # """
#     fact = 1
#     i = 2
#     while i <= number:
#         fact*=i
#         i = i + 1
#     return fact

# print(factorial(5))


# def countfreq(arr,n):
#     """
#     This function to show count frequence of element in array
#     """
#     freq=dict()
#     for i in arr:
#         if i not in freq:
#             freq[i]=0
#         freq[i]+=1
#     for x in freq:
#         print(f"{x} count number in array {freq[x]}")
# arr = [10,20,20,10,10,20,5,20]
# n = len(arr)
# countfreq(arr,n)

# Linear search

# def linear_search(arr,num):
#     """
#     this Algorthims to search number  
#     """
#     for i in range(len(arr)):
#         if arr[i] == num:
#             return f"The number {num} is found in index {i}"
#     return f"The number {num} not found in array"
# print(linear_search([1,2,3,4,5,6,8,10],0))


# Binary search

# def Binary_search(arr,left,right,element):
#     """
#     This function to make BinarySearch
#     """
#     while left <= right:
#         middle = left + (right-1) // 2
#         if arr[middle] == element:
#             return f"The element {element} found in index {middle}"
#         elif arr[middle] < element:
#             left = middle + 1
#         else:
#             right = middle - 1
#     return f"The Element {element} Not found in array"
# arr = [2,3,4,10,40]
# left = 0
# right = len(arr)-1
# element = 3
# print(Binary_search(arr,left,right,element))

