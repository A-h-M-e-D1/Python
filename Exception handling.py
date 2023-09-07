# def fetcher(obj,index):
#     return obj[index]
# x='spam'
# print(fetcher(x,4)) # IndexError

# Exception handling
# try => except => finnally => assert => raise => with/as
# try:
#     print(fetcher(x,1000))
# except IndexError:
#     print("got exception")

# raise statement

# try:
#     raise IndexError
# except IndexError:
#     print("succed to manage error")

# build my Exceptions
# class Bad(Exception):
#     pass             # User-defined exception

# def doomed():
#     raise Bad()      # Raise an instance 
# try:
#     doomed()
# except Bad:
#     print('got Bad')

# termination ==> finally

# x=1
# y=2
# try:
#    pass #   pass print(x/y)
# except ZeroDivisionError:
#      print(f"You Cannot divide into Zero: {x} / {y}")
# else:
#      print(f"Not found Error and the result is {x / y}")
# finally:
#      print("you can excute program on the way out")

# assert statment

# def f(x):
#      assert x < 0,'x must be negative'
#      return x ** 2
# print(f(2))

# def divide(a,b):
#     assert b!=0,'cannot divide by Zero'
#     return a /b
# print(divide(10,5))
# print(divide(10,0))


# problem solving
# num_test_caes=int(input())
# for _ in range(num_test_caes):
#     a,b=map(str,input().split())
#     try:
#          result=int(a) // int(b)
#          print(result)

#     except ZeroDivisionError as z:
#         print("Error Code:",z)

#     except ValueError as v:
#         print("Error Code:",v)




