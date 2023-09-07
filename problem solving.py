# coder: Ahmed Ashraf Mohamed

# size_of_array = int(input())

# arr = list(map(int,input().split()))

# max_num = arr[0]
# count = 0

# #find max num
# for i in range(len(arr)):
#     if(arr[i] > max_num):
#         max_num = arr[i]

# #count number of max_number
# for j in range(len(arr)):
#     if arr[j] == max_num:
#         count+=1
# print(count)


# str = input()

# sum = 0
# for latters in range(len(str)):
#     sum+=int(str[latters])
# print(sum)

# size = int(input())

# for i in range(1,size+1):
#     space = " " * (size-i)
#     shape = "#" * i
#     print(space+shape)
# num_of_test = int(input())



# num_test = int(input())
# for _ in range(num_test):
#     nums = int(input())
#     is_prime = True
#     for j in range(nums):
#         for i in range(2,int(j*0.5)+1):
#             if j % i == 0:
#                 is_prime = False
#             if(is_prime):
#                 max_factor = 0
#                 for k in range(i):
#                     if k > max_factor:
#                         max_factor = k 
#                         print(max_factor)

# size = int(input())
# arr = list(map(int,input().split()))

# for i in range(len(arr)):
#     if arr[0:] == arr[::-1]:
#         print("YES")
#         break
#     else:
#         print("NO")
#         break


# def factorial(num):
#     # base case
#     if num == 0:
#         return 1
#     if num == 1:
#         return 1
#     else:
#         return num*factorial(num-1)
# num = int(input())
# print(factorial(num)

#insert element
# arr = [1,2,3,4,5]
# num = int(input("Enter a number to insert it:\n "))
# position = int(input("Enter a position of num:\n "))
# size = len(arr)
# for i in range(size-1,position):
#     arr[i+1] = arr[i]
#     i-=1
# arr[position] = num
# size+=1
# print(arr)

# # Delete element
# arr = [1,2,3,4,5]
# size = len(arr)
# position = int(input("Enter a position of num:\n "))
# print(arr)

# for i in range(position,size-1):
#          arr[i] = arr[i+1]

# size-=1   
# print(arr)


# time = input().strip()
# h,m,s = map(int,time[:-2].split(":"))
# p = time[-2:]
# h = h%12+(p.upper() == "PM")*12
# print(('%02d:%02d:%02d') % (h, m, s))




# size = int(input())
# arr=[]
# for _ in range(size):
#     nums = int(input())
#     arr.append(nums)
#     count = 0
#     x =0
#     for i in range(len(arr)):
#         x = arr[i]
#         if x % 5 == 0:
#             x = arr[i]
#         elif x < 38:
#             x = arr[i]
#         else:
#             for j in range(1,3):
#                 x+=1
#                 count+=1
#                 if(x % 5 == 0):
#                     arr[i] = x
#                 elif(x%5!=0 ) and count > 2:
#                     arr[i] = x
#         count =0
# for k in range(len(arr)):
#     print(arr[k])

# s,t = map(int,input().split())
# apple,orange = map(int,input().split())
# m,n = map(int,input().split())
# arr_a = list(map(int,input().split()))
# arr_b = list(map(int,input().split()))

# count_apple = 0
# count_orange = 0

# for i in range(len(arr_a)):
#     res = arr_a[i] + apple
#     if res in range(s,t+1):
#         count_apple+=1
# for j in range(len(arr_b)):
#      res2 = arr_b[j]+orange
#      if res2 in range(s,t+1):
#          count_orange+=1
# print(count_apple)
# print(count_orange)



# def r(s):
#     dict1 = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000,
#     }
    
#     total = 0
#     p_value = 0
    
#     for char in s[::-1]:  
#         value = dict1[char]
#         if current_value >= prev_value:
#             total += current_value
#         else:
#             total -= current_value
#         prev_value = current_value
    
#     return total

# s= input()
# print(r(s))

# m,n = map(int,input().split())
# a = list(map(int,input().split()))
# b = list(map(int,input().split())) 

# max_a = max(a)
# min_b = min(b)+1
# res=0
# for i in range(max_a,min_b):
#     isfactor = True
#     for nums in a:
#         if i % nums!=0:
#             isfactor = False
#             break;
#     for nums2 in b:
#         if  nums2 % i != 0:
#             isfactor = False
#             break;
#     if isfactor == True:
#         res+=1
# print(res)
