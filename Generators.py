# def main_func():
#     print("Hello")
# main_func()

# def main_func():
#      return "Hello"
# print(main_func())

# Generators
# def odd_numbers(n):
#       # initialize the counter
#   num = 1
#   # loop until the counter is less than or equal to n
#   while num <= n:
#     # yield the current value of the counter
#     yield num
#     # increment the counter by 2
#     num += 2

# # create a generator object from the function
# odd_gen = odd_numbers(10)
# # iterate over the generator and print the values
# for i in odd_gen:
#   print(i)

# def func(n):
#     yield n*3
#     yield n*4
# print(func(5)) # <generator object func at 0x0000029FFF834C40>

# def func(n):
#     yield n*3
#     yield n*4
# for i in func(5):
#     print(i)

# def func3(n):
#      i=1
#      while i <=n:
#             yield i
#             i+=1
# my_generator=func3(5)
# لطباعه عناصر محدده
# print(next(my_generator))
# print(next(my_generator))

# لطباعه كل العناصر مره واحده
# for i in my_generator:
#       print(i)

# print("#"*50)

# def func2(n):
#      return n*3

# print(func2(5)) # 15

# def sum_numbers(num1,num2):
#     sum=0
#     for i in range(num1,num2+1):
#        sum+=i
#        yield sum
# my_gen=sum_numbers(1,10)
# # print(next(my_gen))
# for j in my_gen:
#     print(j)

# def alt_case(text):
#     for letter in str(text):
#         yield letter.upper()
#         yield letter.lower()
# my_gen=alt_case('ahmed')

# for t in my_gen:
#     print(t)

# check prime number
# def check_prime(n):
#     if n < 2:
#         yield "Not Prime"
#     else:
#         for i in range(2, n):
#             is_prime = True
#             for j in range(2, int(i/2)+1):
#                 if i % j == 0:
#                     is_prime = False
#                     break
#             if is_prime:
#                 yield i

# my_gen = check_prime(100)

# for j in my_gen:
#     print(j)

