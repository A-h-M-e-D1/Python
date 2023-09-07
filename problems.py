# num1,num2=map(int,input().split())
# for i  in range(num1,num2+1):
#       has_4_or_7 = False
#       if i % 10==4 or i % 10== 7:
#           if i % 100 ==4 or i % 100==7:
#               if i % 1000== 4 or i % 1000== 7 :
#                   if i %10000== 4 or i % 10000== 7:
#                       if i % 100000== 4 or i % 100000== 7:
#                              print(i,end=" ")

# import math
# num=int(input())
# elements=list(map(int,input().split()))
# array=array("i",elements)
# sum=0

# for i in array:
#     sum+=i
# print(abs(sum))    

# from array import array
# num_element=int(input())

# Array_nums=list(map(int,input().split()))

# search_num=int(input())

# array=array("i",Array_nums)

# if search_num in array:
#     print(array.index(search_num))
# else:
#     print(-1)

# from array import array
# element_numbers=int(input())

# elements=list(map(int,input().split()))

# array=array("i",elements)

# for i in elements:
#     if i > 0:
#         i=1
#         print(i,end=" ")
#     elif i < 0:
#         i=2
#         print(i,end=" ")
#     else:
#         print(i,end=" ")


# import numpy

# def arrays(arr):
#       return numpy.array(arr[::-1],float)
# arr = input().strip().split(' ')
# result = arrays(arr)
# print(result)


# def down_number():
#     Number=int(input())
#     for i in range(1,Number+1,): # Add a comma after Number
#         print(i,)
# down_number()

# def swaping():
#      x,y=map(int,input().split())
#      a=

# x=6
# y=7

# e=x-y # 3
# x=x-e 
# y=y+e
# print(x) #2
# print(y) # 5

# def swap():
#     x,y=map(int,input().split())
#     e=x-y
#     x=x-e
#     y=y+e
#     print(x,y)
# swap()    

# number=int(input())
# print( f"The multiplication table for {number} is:")
# for i in range(13):
#     print(f"{number} x {i} ={number*i}")

# def countdown(number):
   
#     if number == 1:
#         return
#     else:
#         countdown(number-1)
# n=int(input())
# print(countdown(n))

# def countdown(number):
#     if number ==1:
#         return 
#     else:
        
#         print(number - 1,end=" ")
#         countdown(number - 1)
      

# n = int(input())
# print(n,end=" ")
# countdown(n)

# string_one=input()
# string_two=input()
# print(len(string_one),len(string_two))
# print(string_one+" "+string_two)

# m=int(input()) # size of set1
# M=list(map(int,input().split()))
# set1=set((M)) # Creat of set 1

# n=int(input()) # size of set 2
# N=list(map(int,input().split()))
# set2=set((N)) # Creat of set 2
# # symmetric difference 
# dif=set1.symmetric_difference(set2)
# dif2=sorted(dif)
# for i in dif2:
#     print(i)
    




# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# A = set(map(int, input().split()))
# B = set(map(int, input().split()))

# happiness = 0
# for num in arr:
#     if num in A:
#         happiness += 1
#     elif num in B:
#         happiness -= 1

# print(happiness)


# number_elements_set=int(input())
# set=set(map(int, input(). split()))
# number_commend=int(input())
# user_input=input() # commend
# operation, *item = user_input.split()
# sum=0
# while number_commend < 20:
#     if operation == 'pop':
#         set.pop()
#     elif operation =='remove':
#      set.remove(int(item[0]))
#     elif operation =='discard':
#      set.discard(int(item[0]))
#     sum+=set
# print(sum)    

# n=int(input()) # number student English
# set1=set(map(int,input().split()))
# b=int(input()) # number student Frensh
# set2=set(map(int,input().split()))
# oper=list(set1 | set2)
# length=0
# for i in oper:
#      length+=oper[0]
# print(length) 

# Next Alphabet

# Alphabets={
#         'a':'b',
#         'b':'c',
#         'c':'d',
#         'd':'e',
#         'e':'f',
#         'f':'g',
#         'g':'h',
#         'h':'i',
#         'i':'j',
#         'j':'k',
#         'k':'l',
#         'l':'m',
#         'm':'n',
#         'n':'o',
#         'o':'p',
#         'p':'q',
#         'q':'r',
#         'r':'s',
#         's':'t',
#         't':'u',
#         'u':'v',
#         'v':'w',
#         'w':'x',
#         'x':'y',
#         'y':'z',
#         'z':'a'

     
# }
# user_input=input()

# if user_input == 'a':
#      print(Alphabets['a'])
     
# elif user_input =='b':
#      print(Alphabets['b'])
     
# elif user_input =='c':
#      print(Alphabets['c'])

# elif user_input =='d':
#      print(Alphabets['d'])

# elif user_input =='e':
#      print(Alphabets['e'])
     
# elif user_input =='f':
#      print(Alphabets['f'])
     
# elif user_input =='g':
#      print(Alphabets['g'])
     
# elif user_input =='h':
#      print(Alphabets['h'])
     
     
# elif user_input =='i':
#      print(Alphabets['i'])
     
# elif user_input =='j':
#      print(Alphabets['j'])
     
# elif user_input =='k':
#      print(Alphabets['k'])
     
# elif user_input =='l':
#      print(Alphabets['l'])
     
# elif user_input =='m':
#      print(Alphabets['m'])
     
# elif user_input =='n':
#      print(Alphabets['n'])
     
# elif user_input =='o':
#      print(Alphabets['o'])
     
# elif user_input =='p':
#      print(Alphabets['p'])
     
# elif user_input =='q':
#      print(Alphabets['q'])
     
# elif user_input =='r':
#      print(Alphabets['r'])
     
# elif user_input =='s':
#      print(Alphabets['s'])
     
# elif user_input =='t':
#      print(Alphabets['t'])
     
# elif user_input =='u':
#      print(Alphabets['u'])
     
# elif user_input =='v':
#      print(Alphabets['v'])
     
# elif user_input =='w':
#      print(Alphabets['w'])
     
# elif user_input =='x':
#      print(Alphabets['x'])
     
# elif user_input =='y':
#      print(Alphabets['y'])
     
# elif user_input =='z':
#      print(Alphabets['z'])

# size_of_group=int(input())

# unordered_element=set(map(int,input().split()))

# r=list(unordered_element)
# print(r[-1])



# def count_substring(string, sub_string):
#      return string.find(sub_string)

# if __name__ == '__main__':
#      string = input().strip()
#      sub_string = input().strip()
    
#      count = count_substring(string, sub_string)
#      print(count)

# eyes,mouths,bodies=map(int,input().split())

# conditions="Two eyes and one body."
# "Two eyes, one mouth, and one body."
# "One eye, one mouth, and one body." 
# max_num=0
# if eyes==0:
#     print(0)





# my_list=list(map(int,input().split()))
# n=int(input())

# *list,n=map(int,input().split())

# for i in list:
#      if i==n**n:
#             list.remove(i)
#             print(list)


# a,b,c=map(int,input().split())
# Katryoshka=0
# if a ==0:
#     print(0)
# if  a == 2 and c==1:
#     Katryoshka+=1
#     print(Katryoshka)

arr = [1,2,3,8,10,8,9,7,20]
sli = arr[0:8:3]
print(sli) # [1,8]