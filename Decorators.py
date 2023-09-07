# simple Example
# def dec_founction(main_function):
#     def wrapper_function():
#         print("Before executing the function")
#         main_function()
#         print("After executing the function")
#     return wrapper_function


# @dec_founction
# def hello_function():
#     print("Hello,World")
# hello_function()

# Check Authentication 
# def dec_func(check_user):
#     def wrap():
#        user_name=input("Enter Your name: ")
#        password=int(input("Enter a Password:  "))
#        if user_name== 'Ahmed2004':
#             if password == 12345678910:
#                 print("You Can Enter into a Email")
#             else:
#                 print("You Can not acces from this Email")


#             check_user()
#     return wrap

# @dec_func
# def user_information():
#     pass
# user_information()

# check time 
# import time

# def dec_func(Check_time):
#     def wrapper():

#         Check_time()
#         print(f"time to excute is {time.time()}")
#     return wrapper
# @dec_func
# def test_time():
#     list=[1,2,3,4,5,6,7,8,9]
#     sum=0
#     for i in list:
#         sum+=i
#     print(sum)
# test_time()

# import time

# def dec_func(Check_time):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = Check_time(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f"Execution time: {execution_time} seconds")
#         return result
#     return wrapper

# @dec_func
# def test_time(numbers):
#     sum = 0
#     for num in numbers:
#         sum += num
#     return sum

# numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = test_time(numbers_list)
# print(f"Sum: {result}")

# def dec_func(divide):
#     def wrapper(num1,num2):
#         try:
#             if num1 / num2:
#                 print("Yes")
#         except:
#             if num2 == 0:
#                 print("you can divide into Zero")
#                 divide(num1,num2)
#     return wrapper

# @dec_func
# def divide_number(num1,num2):
#     pass
# divide_number(2,0)

