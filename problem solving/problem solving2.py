# maximum

# symbol=input()
# number_of_element=int(input())
# arr=[]
# numbers=list(map(int,input().split()))
# for i in numbers:
#     histogram= symbol * i
#     arr.append(histogram)
# for j in arr:
#     print(j)

# def count_substring(string, sub_string):
#     count=0
#     for i in range(len(string)):
#         if string[i:i+len(sub_string)] == sub_string:
#             count+=1
#     return count

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()

#     count = count_substring(string, sub_string)
#     print(count)

# #adding bits
# number1,number2 = map(int,input().split())

# number1_binary = '{0:032b}'.format(number1)
# number2_binary = '{0:032b}'.format(number2)

# # adding_bits = number1_binary + number2_binary
# import textwrap

# s="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
# print(textwrap.fill(s,4))

# import textwrap

# def wrap(string, max_width):
#    return textwrap.fill(string,max_width)


# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)



# while True:
#     n, m = map(int, input().split())
#     if n <= 0 or m <= 0:
#         break
    
#     if n > m:
#         n, m = m, n
    
#     numbers = list(range(n, m+1))
#     sum_numbers = sum(numbers)
    
#     output = ' '.join(map(str, numbers)) + ' sum =' + str(sum_numbers)
#     print(output)

# design

# #convert

# num = int(input())


# octal = '{:0o}'

# hex = '{:0x}'

# binary = '{:0b}'

# for i in range(1,num+1):
#     print(i,end=" ")
#     print(octal.format(i),end=" ")
#     print(hex.format(i),end=" ")
#     print(binary.format(i))


# def print_formatted(number):
#     width = len(bin(number)[2:])
#     for i in range(1,n+1):
#         deciaml = str(i).rjust(width)
#         octal = str(oct(i)[2:]).rjust(width)
#         hexdecimal = str(hex(i)[2:]).upper().rjust(width)
#         binary = str(bin(i)[2:]).rjust(width)
#         print(f"{deciaml} {octal} {hexdecimal} {binary}")


# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)


import re

# number_test_case = int(input())

# for i in range(number_test_case):
#     string = input()
#     try:
#         if string in re.search(string):
#             print(string)


# n,m = map(int,input().split())
# for i in range(1,n,2):
#      print((i*'.|.').center(m,"-"))
# print("WELCOME".center(m,'-'))
# for j in range(n-2,-1,-2):
#      print((j * '.|.').center(m,'-'))

# a,b = map(int,input().split())

# oper = a- b

# if oper >= 0:
#     print(oper)
# else:
#     print(0) 

# t_case = int(input())

# for i in range(t_case):
#     # user input
#     x, y = map(int, input().split())
    
#     if x > y:
#         x, y = y, x

#     odd_sum = 0

#     for j in range(x + 1, y):
#         if j % 2 != 0:
#             odd_sum += j

#     print(odd_sum)

# user input

# n ,a ,b = map(int,input().split())
# sum = 0
# for i in range(1,n+1):
#     x = i

#     while(x > 0):
#         z = x% 10
#         sum+=z
#         x//=10
#     if sum>=a and sum <=b:
#         sum+=i
# print(sum)

# n, a, b = map(int, input().split())
# total_sum = 0

# for i in range(1, n+1):
#     current_num = i
#     digit_sum = 0

#     while current_num > 0:
#         digit_sum += current_num % 10
#         current_num //= 10

#     if a <= digit_sum <= b:
#         total_sum += i

# print(total_sum)

# num,size = map(int,input().split())
# numbers = list(map(int,input().split()))

# arr = []
# count = 0
# min_value = float('inf')
# for num in numbers:
#     min_value = min(min_value,num)
#     count+=1
#     if count == size:
#         arr.append(min_value)
#         min_value = float('inf')
#         count = 0
# if count > 0:
#     arr.append(min_value)
# for min_num in arr:
#     print(min_num,end=" ")
# import math

# AB = float(input())
# Bc = float(input())


# Angle_by_degrees = (math.degrees(math.atan(AB / Bc)))

# print(f"{round(Angle_by_degrees)}{chr(0xB0)}")

# number_of_element = int(input())

# arr = list(map(int,input().split()))

# for i in range(len(arr)):
#     if arr[i] <= 10:
#         print(f"A[{i}] = {arr[i]}")

# number_of_element = int(input())
# arr = list(map(int,input().split()))

# min_number = arr[0]
# min_position = 0
# for index in range(len(arr)):
#     if arr[index] < min_number:
#         min_number = arr[index]
#         min_position = index
#         break
# print(min_number,min_position+1)

# number_of_element = int(input())
# arr = list(map(int,input().split()))

# reversed_array = arr[::-1] 

# for i in reversed_array:
#     print(i,end=" ")

